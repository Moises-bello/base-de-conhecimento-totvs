---
content_hash: 09d5fbe1647d5b4de00f6948ac573cfa0f94f6c337809409616b99ce94e83588
fetched_at: '2026-06-29T00:10:52.230504+00:00'
page_id: '571264295'
product: rm
source: tdn-rm
title: 9993957 FISCAL01-14086 DT Geração dos campos 15 e 16 do registro C185
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=571264295
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração dos campos 15 e 16 do registro C185 - SPED Fiscal |
| Ticket: | 9993957 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14086 |

## **02. SITUAÇÃO/REQUISITO**

Foi solicitada a implementação do Código MG200 no Registro C185, referente ao Ressarcimento MG, conforme legislação.

## **03. SOLUÇÃO**

Foram feitas alterações para que sejam calculados os valores dos campos 15 e 16 do registro C185, no arquivo gerado para SPED FISCAL.  
Os valores dos campos 15 e 16 serão calculados quando o parâmetro "Gerar ressarcimento/complemento ICMS ST" estiver selecionado.
