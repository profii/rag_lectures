from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, T5ForConditionalGeneration, AutoModelForCausalLM

import torch
import numpy as np
import faiss
import codecs
import json

device = 'cuda' if torch.cuda.is_available() else 'cpu'


query = "What is the matrix rank definition?"
file_name = "lecture-5.ipynb"


def ask(file_name, query):
    # model_name = 't5-large'
    model_name = "meta-llama/Llama-2-7b-chat-hf"


    def chunking(text):
        ''' Chunking data
        Args:
            text (String): string that contains data
        Returns:
            list: list of chunks
        '''
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_text(text)

        return chunks

    def retriever(chunks, query):
        ''' Embed the Corpus and Retrieve Top-k Documents
        Args:
            chunks (list): list of chunked data
            query (str): Question
        Returns:
            list: list of top-k retrieved chunks
        '''
        model = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = model.encode(chunks)

        # index using FAISS
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(np.array(embeddings))

        query_embedding = model.encode([query])
        _, indices = index.search(np.array(query_embedding), k=5)
        retrieved_chunks = [chunks[i] for i in indices[0]]

        return retrieved_chunks

    def generetor(model, tokenizer, retrieved_chunks, query):
        input_context = " ".join(retrieved_chunks)

        input_text = f"### Input:\nAnswer the question based on the context only.\nQuestion:{query}\nContext:\n{input_context}\n\n### Output:"  
        inputs = tokenizer(input_text, return_tensors="pt").to(device)
        inputs_length = len(inputs['input_ids'][0])
        with torch.inference_mode():
            results = model.generate(**inputs, max_new_tokens=100,
                                do_sample=True, temperature=0.1, top_p=0.6,
                                pad_token_id=tokenizer.eos_token_id)

        result = tokenizer.decode(results[0][inputs_length:], skip_special_tokens=True)

        return result



    f = codecs.open(file_name, 'r')
    source = f.read()

    y = json.loads(source)
    data_lines = [''.join(source_i['source']) for source_i in y['cells']]
    data_lines = '\n\n'.join(data_lines)

    # print(data_lines[:200])


    if 't5' in model_name:
        model = T5ForConditionalGeneration.from_pretrained(model_name, device_map=device) #.to('cuda')
        tokenizer = AutoTokenizer.from_pretrained(model_name)
    if 'llama' in model_name:
        model = AutoModelForCausalLM.from_pretrained(model_name, load_in_8bit=True, device_map=device)
        tokenizer = AutoTokenizer.from_pretrained(model_name)


    chunks = chunking(data_lines)
    retrieved_chunks = retriever(chunks, query)
    result = generetor(model, tokenizer, retrieved_chunks, query)

    # print(f'From this context:\n{retrieved_chunks}')
    print(f'The answer to the question [{query}] is:')
    print(result)


ask(file_name, query)