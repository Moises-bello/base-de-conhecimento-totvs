---
content_hash: 0ed0a8176d7f067b356a70e9fa42f6217e8ead34a4eb21302a7a5f8ee5b5d63c
fetched_at: '2026-06-29T00:09:11.275230+00:00'
page_id: '403742748'
product: rm
source: tdn-rm
title: 2335846 FOPCALCULO01-4155 Folha Agraria - Indenização Art. 14 da Lei 5.889/73
  (Safra)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403742748
version: 4
---

# Indenização por tempo de serviço do Safrista

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Rescisão |
| **Situação/Requisito:** | Nas rescisões de término de contrato de safra, é devido o pagamento a titulo de Indenização, conforme art. 14 da lei 5.889/73 , no valor correspondente a 1/12 avos do salário do funcionário, por mês ou fração superior a 14 dias. Cliente solicita que o sistema calcule esta indenização, tendo em vista que é uma obrigação legal que poderá ser cobrada pelo governo e que consta na tabela 03 do e-social em rubrica específica para este evento (rubrica 6103). |
| **Solução/Implementação:** | Foi criado um parâmetro 'Lança indenização por tempo de serviço de safrista (Rural)' que determina se será pago a indenização conforme a lei especifica.  Foi criado o CC 379, que calcula a indenização por tempo de serviço do safrista e o CC 380 que lança a diferença de indenização tempo de serviço do safrista. |
| **Tickets relacionados:** | 2335846 |
| **Documento de Referência:** | <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.IndenizacaoTempoServicoSafrista.aspx>  <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.DiferencaIndenizacaoTempoServicoSafrista.aspx>  <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.Calculo.aspx> |
