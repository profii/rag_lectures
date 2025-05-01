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

['- You can also use linear combination of *rows* to define the rank, i.e. formally there are two ranks: column rank and row rank of a matrix.\n\n**Theorem**  \nThe dimension of the column space of the matrix is equal to the dimension of its row space.\n\n[Proof](https://ocw.mit.edu/courses/mathematics/18-701-algebra-i-fall-2010/study-materials/MIT18_701F10_rrk_crk.pdf)\n\n- In the matrix form this fact can be written as $\\mathrm{dim}\\ \\mathrm{im} (A) = \\mathrm{dim}\\ \\mathrm{im} (A^\\top)$.',
 '## Dimension of a linear space\n\n- The dimension of a linear space $\\text{im}(A)$ denoted by $\\text{dim}\\, \\text{im} (A)$  is the minimal number of vectors required to represent each vector from $\\text{im} (A)$.\n\n- The dimension of $\\text{im}(A)$ has a direct connection to the **matrix rank**.\n\n\n## Matrix rank\n\n- Rank of a matrix $A$ is a maximal number of linearly independent *columns* in a matrix $A$, or the **dimension of its column space** $= \\text{dim} \\, \\text{im}(A)$.',
 '### Instability of the matrix rank\nFor any rank-$r$ matrix $A$ with $r < \\min(m, n)$ there is a matrix $B$ such that its rank is equal to $\\min(m, n)$ and\n\n$$ \\Vert A - B \\Vert = \\epsilon. $$\n\n**Q**: So, does this mean that numerically matrix rank has no meaning? (I.e., small perturbations lead to full rank!)',
 '# Lecture 4:  Matrix rank, low-rank approximation, SVD\n\n## Previous lecture\n\n- Peak performance of algorithm\n- Complexity of matrix multiplication algorithms\n- Idea of blocking (why it is good?)\n\n## Todays lecture\n- Matrix rank\n- Skeleton decomposition\n- Low-rank approximation\n- Singular Value Decomposition (SVD)\n- Applications of SVD\n\n## Matrix and linear spaces\n- A matrix can be considered as a sequence of vectors that are columns of a matrix:\n\n$$ A = [a_1, \\ldots, a_m], $$',
 '$$A = C \\widehat{A}^{-1} R,$$\n\nwhere $C$ is $n \\times r$, $R$ is $r \\times m$ and $\\widehat{A}$ is $r \\times r$, or \n\n$$ A = UV, $$\n\nwhere $U$ and $V$ are not unique, e.g. $U = C \\widehat{A}^{-1}$, $V=R$.\n\n- The form $A = U V$ is standard for skeleton decomposition.\n\n- Thus, every rank-$r$ matrix can be written as a product of a "skinny" ("tall") matrix $U$ by a "fat" ("short") matrix $V$.\n\nIn the index form, it is  \n\n$$ a_{ij} = \\sum_{\\alpha=1}^r u_{i \\alpha} v_{\\alpha j}. $$']
