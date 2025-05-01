# RAG for QA based on a Lecture


*Example of data:*

| Variable  | Value |
| ------------- | ------------- |
| `query`  | What is the matrix rank definition? |
| `result`  | The matrix rank definition is the maximal number of linearly independent columns in a matrix, or the dimension of its column space. The matrix rank has a direct connection to the dimension of the column space, and it is a measure of the stability of the matrix. |



- `Sentence Transformer` for corpus embedding (*all-MiniLM-L6-v2*)
- `FAISS` for indexing
- `Llama-2-7b-chat-hf` as a generator



---

Here `retrieved_chunks` got:

['- You can also use linear combination of *rows* to define the rank, i.e. formally there are two ranks: column rank and row rank of a matrix.\n\nTheorem  \nThe dimension of the column space of the matrix is equal to the dimension of its row space.\n\n[Proof](https://ocw.mit.edu/courses/mathematics/18-701-algebra-i-fall-2010/study-materials/MIT18_701F10_rrk_crk.pdf)\n\n- In the matrix form this fact can be written as $\\mathrm{dim}\\ \\mathrm{im} (A) = \\mathrm{dim}\\ \\mathrm{im} (A^\\top)$.',  
 '## Dimension of a linear space\n\n- The dimension of a linear space $\\text{im}(A)$ denoted by $\\text{dim}\\, \\text{im} (A)$  is the minimal number of vectors required to represent each vector from $\\text{im} (A)$.\n\n- The dimension of $\\text{im}(A)$ has a direct connection to the matrix rank.\n\n\n## Matrix rank\n\n- **Rank of a matrix $A$ is a maximal number of linearly independent *columns* in a matrix $A$, or the dimension of its column space $= \\text{dim} \\, \\text{im}(A)$**.',  
 '### Instability of the matrix rank\nFor any rank- $r$ matrix $A$ with $r < \\min(m, n)$ there is a matrix $B$ such that its rank is equal to $\\min(m, n)$ and\n\n$$ \\Vert A - B \\Vert = \\epsilon$$. \n\nQ: So, does this mean that numerically matrix rank has no meaning? (I.e., small perturbations lead to full rank!)',]
