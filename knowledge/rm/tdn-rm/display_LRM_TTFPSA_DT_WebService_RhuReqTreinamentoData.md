---
content_hash: fde9f31971ea9a08836cd020eac4ecd51d21c54bd5d9daea60dbda7ca0e3da9e
fetched_at: '2026-06-29T00:06:11.735914+00:00'
page_id: '203770335'
product: rm
source: tdn-rm
title: TTFPSA_DT_WebService_RhuReqTreinamentoData
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFPSA_DT_WebService_RhuReqTreinamentoData
version: 1
---

# DATASERVER RHUREQTREINAMENTODATA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | DataServer RhuReqTreinamentoData |
| **Situação/Requisito:** | Ao realizar a chamado via SOAP do DataServer RhuReqTreinamentoData, usando o método SaveRecord é apresentado mensagem informando que o campo CODTPDEMANDA não pode ter seu valor nulo, porém ao criar  uma requisição de treinamento através da MDI, o sistema permite a criação da requisição sem a necessidade de informar o CODTPDEMANDA. |
| **Solução/Implementação:** | Alteração na forma em que o schema é montado quanto se trata de chamava via WebService. É necessário validar o tipo de acesso que ocorre ao DataServer e depois aplicar a validação do schema. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTFPSA |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | 12.1.8 |
