---
content_hash: 293d7e45b2f8c6b0b2c70a1f7172fa981610d948a6859f8c40d12a31c20ea334
fetched_at: '2026-06-29T00:11:10.957929+00:00'
page_id: '644711368'
product: rm
source: tdn-rm
title: FISCAL01-16342 DT Consultar a autorização do Cancelamento de Comprovante de
  Entrega da NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=644711368
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Consultar Evento Comprovante de Entrega NF-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16341 |

## **02. SITUAÇÃO/REQUISITO**

Consultar a autorização de um Evento de Cancelamento de Comprovante de Entrega da NF-e

## **03. SOLUÇÃO**

```
Implementado o processo de consulta para o Cancelamento do Comprovante de Entrega NFe.
```

Em ***RM → Backoffice → Gestão de Estoque, Compras e Faturamento → Vendas → Faturamento → SPED (Estadual) → Anexo → Eventos → Processos → Consultas de Eventos***

Regras para Consulta de Eventos:

1. Necessário um Evento de Cancelamento de Comprovante de Entrega **Pendente.**
2. Aplicar apenas para o Evento de Cancelamento de Comprovante de Entrega.
3. Aplicar no Evento de Comprovante de Entrega "Pendente Cancelamento" não é aceito.

Resultado:

1. Evento Cancelamento de Comprovante de Entrega com status **Aceito.**
2. Evento Comprovante de Entrega com status **Cancelado**.
