---
content_hash: 8b67636f58a120a7aa0c49aa98b80f9acd0cba23c160d423268886e462b45c55
fetched_at: '2026-06-29T00:05:48.136426+00:00'
page_id: '1023305741'
product: rm
source: tdn-rm
title: Reforma Tributária - Banco de Terreno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1023305741
version: 3
---

## **Novos Campos – Banco de Terrenos**

Para atender à legislação atual e à evolução do produto frente à reforma tributária, será necessária a criação dos seguintes campos no cadastro de **Banco de Terrenos**, na **tabela de Lotes**:

* **Cadastro Imobiliário Brasileiro (CIB):** composto por sete caracteres alfanuméricos e um dígito verificador, com a estrutura `AAAAAAA-D`.
* **Código Nacional de Matrícula (CNM):** padroniza o número da matrícula em formato nacional (com 16 dígitos estruturados: `CCCCCC.L.NNNNNNN-DD`).
* **Cadastro Imobiliário Fiscal (CIF):** corresponde à inscrição municipal do imóvel, podendo ter diferentes formatos e tamanhos conforme o município.  
  **Sugestão:** campo do tipo **string (30)** para garantir flexibilidade.

---

## 🗂️ Sugestão de Organização na Tela – Banco de Terrenos

Os campos devem ser incluídos na **aba “Lotes”** do cadastro de Banco de Terrenos.
