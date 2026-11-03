---
content_hash: 98f1809a2717ebe7ec59b3ab006277c5fc885617150f28a5edc12e2ff3488fb6
fetched_at: '2026-06-29T00:08:52.764145+00:00'
page_id: '342307314'
product: rm
source: tdn-rm
title: RMFIS00003_Autenticação de Documento Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=342307314
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.x |
| **Ocorrência:** | Autenticação de Documento Fiscal |
| **Ambiente:** |  |
| **Passo a passo:** | A autenticação do documento fiscal é feita através da geração de um código hash, utilizando o algorítimo MD5.  Para que o sistema gere esse código, no Totvs Gestão de estoque, ao incluir um movimento de NF de Serviço de Comunicação, deve-se preencher os seguintes campos:     1. **Tipo de Documento**: deve ser preenchido com um Tipo de Documento que tenha o Código do Modelo do Documento igual a 06, 21 ou 22; 2. **Conta de Consumo**; 3. **Identificador Classe de Consumo**; 4. **Tipo de Assinante**.  Exemplo:           Após salvar o movimento, o código será gerado e gravado na tabela TMOVFISCAL, campo CODAUTENTDIGITALDOC.  Dessa forma, o cliente poderá utilizar o campo em seu relatório referente à impressão da NF de Serviço de Comunicação.  Não existe um padrão para esse documento na legislação. Portanto, o cliente deverá criar o seu relatório utilizando o campo citado acima e homologar o relatório com a SEFAZ. |
| **Observações:** |  |
