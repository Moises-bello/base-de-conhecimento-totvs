---
content_hash: 48fd40cb743a6a7e5da0ecbcb50623ff432f656f90ec6b4fe43f9e1c5089a234
fetched_at: '2026-06-29T00:10:26.892069+00:00'
page_id: '515292161'
product: rm
source: tdn-rm
title: Execução de Conceito via WebService
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515292161
version: 23
---

# Índice:

---

.\*ndice:

# Objetivo:

---

   O objetivo desse documento é esclarecer e exemplificar a execução de um novo Conceito via WebService.

Veja mais em: 

# wsProcess:

---

   Para executar um [Novo Conceito](https://tdn.totvs.com/display/LRM/Conceito) via webservice é necessário utilizar o [wsProcess](https://tdn.totvs.com/x/HZdpCw): o webservice responsável pela execução de processos do sistema.

   O método que deverá ser utilizado é o "**ExecuteWithXmlParams**", o qual possui dois parâmetros:

* O parâmetro **<tot:ProcessServerName>** deve ser preenchido com o processo "ConConceptProcess".
* O parâmetro **<tot:strXmlParams>** deve ser preenchido com o [XML de Parâmetro de Jobs](https://tdn.totvs.com/x/fgARGQ) do processo de execução do Conceito.

Lembre-se:

* No parâmetro "strXmlParams", deve ser adicionada a tag **<![CDATA[ ]]>**. o XML de Parâmetro de Jobs deve ser passado dentro dos colchetes.
* É na tag **ConceptID**, do XML de Parâmetro de Jobs do Conceito, que é passado o ID do Conceito que será executado.

# Exemplo:

---

   Após executar o conceito através da MDI, o XML do processo será obtido na [tela de Parâmetros de Job](https://tdn.totvs.com/x/fgARGQ), onde deverá ser copiado para posterior utilização.

   Em uso do wsProcess, o método ExecuteWithXmlParams será então preenchido da seguinte forma:

ConConceptProcess

]]>

Ao fazer a requisição, certifique-se de selecionar o mecanismo de autorização com "basic", preenchendo os campos "username" e "password" em sua ferramenta de teste/consumo de webservices (ex: SoapUI)

   Após execução do XML, é possível ver o log de execução pela MDI, na tela de Gerenciamento de Jobs:

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Execução de Conceito via WebService

falsefalse

**Status:** Finalizado

false

**Data:** 16/09/2019

false

**Autores:**
