---
content_hash: 0436ad766250b2cf5e145462cd4598d5f30885eefa947dc400a1e9fa446d684f
fetched_at: '2026-06-29T00:11:15.719078+00:00'
page_id: '662415191'
product: rm
source: tdn-rm
title: DT -FISCAL01-17376- INSS - Guia de Recolhimento
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-FISCAL01-17376-+INSS+-+Guia+de+Recolhimento
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Guia de Recolhimento |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17376 |

## **02. SITUAÇÃO/REQUISITO**

Ao acessar o menu Guia de Recolhimento (Em: Backoffice | Gestão Fiscal | Obrigações Principais| Apuração | Mais… | Guias de Recolhimento) e tentar gerar a guia de INSS, o sistema emite a mensagem:

"Erro(s) na inserção de guias de recolhimento: Não existem Lançamentos Fiscais com incidência do imposto no período com os filtros informados!"

## **03. SOLUÇÃO**

Foi realizado ajuste para que o processo Guia de Recolhimento passe a gerar o INSS e também o FUNRURAL.

Antes, a geração  só funcionava no processo: “Geração de Guias Automaticamente”.
