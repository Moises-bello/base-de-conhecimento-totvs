---
content_hash: 6318ab94bdf7a706a2b38fe48f4d5995e985aa94772772d76c71ff7178d150c5
fetched_at: '2026-06-29T00:11:05.063604+00:00'
page_id: '628118686'
product: rm
source: tdn-rm
title: 11767815 FISCAL01-15981 DT Gerar evento REINF - Ajuste no R-2030 e R-2040 tag
  InfoRecurso
type: documentation
url: https://tdn.totvs.com/display/LRM/11767815+FISCAL01-15981+DT+Gerar+evento+REINF+-+Ajuste+no+R-2030+e+R-2040+tag+InfoRecurso
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | REINF |
| País: | Brasil |
| Ticket: | 11767815 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15981 |

## **02. SITUAÇÃO/REQUISITO**

 Erro envio evento REINF: Código MS1076: Já existe outra tag 'infoRecurso: tpRepasse' com mesma chave no evento

## **03. SOLUÇÃO.**

Ajuste na geração dos registros da REINF, R-2030 e R-2040, para que na tag InfoRecurso, os movimentos sejam agrupados pelo CNPJ da Associação Desportiva + Tipo de Repasse
