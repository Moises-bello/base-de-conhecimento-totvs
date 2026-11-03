---
content_hash: 08228889ef5df5b4d5e9b8055afa3adcbe3659ef02a9a3dd06568a3c023a8a7f
fetched_at: '2026-06-29T00:09:02.939525+00:00'
page_id: '381033476'
product: rm
source: tdn-rm
title: DT Continuidade de afastamento - Parametrizador
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Continuidade+de+afastamento+-+Parametrizador
version: 3
---

# Continuidade de Afastamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Parametrizador |
| **Situação/Requisito:** | Deverá ser criado um parâmetro para tratamento do cálculo da continuidade de afastamento informada pelo usuário, possibilitando que afastamento de tipos e/ou doença relacionada diferentes sejam continuados para pagamento devido da parte da empresa e afastamentos gerados pelo INSS. |
| **Solução/Implementação:** | Foi implementado o parâmetro 'Habilita Controle Manual de continuidade de afastamentos com atestado médico' na pasta Folha Normal | Afastamentos, onde o mesmo, quando marcado, irá verificar a data de continuidade de afastamento informada no histórico para cálculo de dias de atestado pagos pela empresa e dias de afastamentos pela previdência. Este parâmetro também verifica avos perdidos para pagamento de 13º salário e perda de período aquisitivo de férias.  Mesmo marcado, este parâmetro continua verificando o período de carência informado no campo "Dias de carência para afastamento com atestado médico". |
| **Tickets relacionados:** | 1313196 |
| **Documento de Referência:** | <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.ParamAfastamento.aspx> |
