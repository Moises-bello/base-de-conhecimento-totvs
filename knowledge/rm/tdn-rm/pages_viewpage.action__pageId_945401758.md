---
content_hash: 545583abc813f804096b22de5e87ffe6e9d3207487dc973d4ae090f3292687d3
fetched_at: '2026-06-29T00:12:09.375279+00:00'
page_id: '945401758'
product: rm
source: tdn-rm
title: DT - eSocial - Rubrica 9912 - Desconto de Assistência Médica ou Odontológica
  (plano diferente de coletivo empresarial)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=945401758
version: 5
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmeto: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | eSocial - Natureza da rubrica |
| País: | Brasil |
| Issue: | [DRHROTRM-13885](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13885 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.278
* 12.1.2410.232
* 12.1.2502.146 e superiores

## **03. SITUAÇÃO/REQUISITO**

Em conformidade com a [notícia](https://www.gov.br/esocial/pt-br/noticias/esocial-disponibiliza-natureza-de-rubrica-9253-para-desconto-do-credito-do-trabalhador#:~:text=9912%20%E2%80%93%20%22Desconto%20de%20assist%C3%AAncia%20m%C3%A9dica,empregado%20em%20planos%20coletivos%20empresariais) publicada no site oficial do governo em **17/04/2025**, foi disponibilizada a nova rubrica **"9912 – Desconto de assistência médica ou odontológica (plano diferente de coletivo empresarial)"**.

Diante disso, é necessário realizar as devidas adequações noTOTVS Folha de Pagamento para garantir total conformidade com as exigências legais e manter a segurança nas entregas do eSocial.

## **04. SOLUÇÃO**

Adequamos o TOTVS Folha de Pagamento com a criação da nova natureza de rubrica do eSocial **"9912 – Desconto de assistência médica ou odontológica (plano diferente de coletivo empresarial)"**.

Essa rubrica deve ser utilizada para registrar os descontos relacionados a planos de saúde ou odontológicos que **não estejam vinculados a planos coletivos empresariais**. Aplica-se, por exemplo, a situações em que o **plano é contratado diretamente pelo trabalhador** e o valor correspondente é descontado em folha e repassado pela empresa à operadora ou administradora do plano.

Com essa atualização, garantimos conformidade com o eSocial e maior segurança no processamento das informações legais.

Para a criação da rubrica é necessário executar o script no sistema **RM.Atualizador.exe**

Após a execução a nova rubrica constará na tabela "Natureza das rubricas da folha de pagamento", conforme demonstrado abaixo:
