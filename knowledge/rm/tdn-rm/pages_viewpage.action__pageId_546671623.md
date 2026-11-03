---
content_hash: 6b9919da980440d724e6b86beac048a0923468515b8444a52f4713669f62f6b0
fetched_at: '2026-06-29T00:10:41.790031+00:00'
page_id: '546671623'
product: rm
source: tdn-rm
title: FISCAL01-12882 DT RESSARCIMENTO - SUB APURAÇÃO - Flag "Considera todas as entradas"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546671623
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Subapuração |
| Ticket: | FISCAL01-12882 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12882 |

## **02. SITUAÇÃO/REQUISITO**

No Período de Apuração do Tributo - Anexo Sub Apuração - Campo "**Considera todas as entradas" -** 

* Este flag vai identificar se, na apuração, o sistema deve considerar todas as entradas do período (varejista) ou somente as entradas que tiveram saídas no período (não varejista).

Não está funcionando.

## **03. SOLUÇÃO**

Implementação da funcionalidade referente a flag "**Considerar somente as Entradas referenciadas em notas de Saída**" da subapuração do Período de Apuração.

* Caso a flag esteja *marcada* o sistema irá considerar todas as e Entradas referenciadas em notas de Saída (varejista)
* Caso a flag esteja *desmarcada* o sistema irá considerar todas as Entradas (não varejista).

Não afeta a seleção de dados das notas de Saída.

Informações Adicionais

Se existir em um mesmo subperiodo de apuração flags "**Considerar somente as Entradas referenciadas em notas de Saída**"  marcadas e desmarcadas será considerada a primeira opção da seleção de dados. Todos os subperiodos de um mesmo período devem ter a flag marcada ou desmarcada.
