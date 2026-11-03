---
content_hash: d22cf47e7c91541383303b253b6bbbcd5b552440a7c887eae9157d0ddc25e4ed
fetched_at: '2026-06-29T00:05:48.133901+00:00'
page_id: '1023305355'
product: rm
source: tdn-rm
title: Reforma Tributária - Cadastro de Sub-Unidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1023305355
version: 5
---

## **Cadastro de Subunidades**

Para atender à legislação atual e à evolução do produto frente à reforma tributária, será necessária a criação dos seguintes campos no cadastro de **Subunidades**:

* **Cadastro Imobiliário Brasileiro (CIB):** composto por sete caracteres alfanuméricos e um dígito verificador, com a estrutura `AAAAAAA-D`.
* **Código Nacional de Matrícula (CNM):** padroniza o número da matrícula em formato nacional (com 16 dígitos estruturados: `CCCCCC.L.NNNNNNN-DD`).
* **Cadastro Imobiliário Fiscal (CIF):** corresponde à inscrição municipal do imóvel, podendo ter diferentes formatos e tamanhos, dependendo do município. Sugere-se criar um campo **string (30)** para maior flexibilidade.
* **Valor de Referência:** valor atualizado anualmente conforme informações oficiais.
* **Ano do Valor de Referência:** ano-base do valor informado.
* **Localização Georreferenciada:** armazenará as coordenadas geográficas (latitude e longitude) da subunidade.

Tipo de Finalidade :

* Comercial
* Residencial
* Misto

A Sub-Unidade pega os parametros do Empreendimento ou da Sub-Unidade caso esteja em branco o parâmetro no Empreendimento.

---

## 🧭 Sugestão de Organização na Tela – Subunidades

* Os cinco primeiros campos devem ser incluídos na aba **“Controle de IPTU / Registro”.**
* O campo **“Localização Georreferenciada”** deve ser posicionado **logo após o endereço**.
