---
content_hash: 7af7939a197a4efb25f205b0efd44a11d50ffe9e8d405e9875702388fe3055b4
fetched_at: '2026-06-29T00:10:51.583611+00:00'
page_id: '568948658'
product: rm
source: tdn-rm
title: FISCAL01-13624 DT Gerar Guias do ICMS-ST - Substituto Tributário/Antecipado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=568948658
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Gestão Fiscal - Geração de Guias Automáticas - ICMS ST |
| Ticket: | FISCAL01-13624 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13623 |

## **02. SITUAÇÃO/REQUISITO**

 Recolhimento Antecipado – Art. 426-A do RICMS

Gerar Guias Automáticas:

ICMS-ST - Substituto Tributário/Antecipado

## **03. SOLUÇÃO**

O Processo de Geração de Guias ICMS-ST:

* 1) Guias do ICMS Antecipado:
  + O sistema deve permitir gerar as guias com o Período de Apuração aberto. Isto é necessário porque as guias devem ser geradas à medida que as notas são emitidas e não somente após o encerramento do período.
  + Devem ser selecionados apenas Lançamentos Fiscais de **entrada**, cuja Situação da Retenção do ICMS ST da Regra de ICMS associada ao CFOP esteja marcado como "**Antecipação**" e que já não tenha guia GNR associada.
  + O lançamento que tiver sua guia gerada deve ser "marcado" para que não sejam geradas guias em duplicidade (DLAFGUIA)

* 2) Guias do ICMS Substituto Tributário
  + As guias referente à substituição tributária (Situação da Retenção do ICMS ST da Regra de ICMS associada ao CFOP esteja marcado como "**Substituto Tributário**") precisam ser geradas após o encerramento do Período de Apuração.
  + Devem ser selecionados apenas Lançamentos Fiscais de **saída**, cuja Situação da Retenção do ICMS ST da Regra de ICMS associada ao CFOP esteja marcado como "**Substituto Tributário**".
