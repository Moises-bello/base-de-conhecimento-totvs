---
content_hash: 0f41a8d8da9f76917d980d52460ec5317557a6480b1e0b98eb534385d90a3418
fetched_at: '2026-06-29T00:11:16.516713+00:00'
page_id: '672103984'
product: rm
source: tdn-rm
title: FISCAL01-17501 - DT - NFTS SP Registro 4 Campo 7 (regime tributário imune)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=672103984
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotinas Fiscais |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17501 |

## **02. SITUAÇÃO/REQUISITO**

Alterar o comportamento da NFTS (Campo 7 Registro 4) para que os Lançamentos de entrada não considerem a imunidade da Filial e sim o tipo de recolhimento do tributos ISS

Manual da NFTS: [http://notadomilhao.prefeitura.sp.gov.br/cidadao/informacoes-gerais/manuais](http://notadomilhao.prefeitura.sp.gov.br/cidadao/informacoes-gerais/manuais "Follow link") - Manual de Envio de Arquivo - Emissão de NFTS em lote

Devido ao grande risco de impacto, se a alteração for realizada no contexto, gentileza implementar de forma especifica para a NFTS de São Paulo,

Simulação:

Informações do campo 7, posição 30 do registro 4:

Informe a Situação com 01 posição.  
T - Operação normal  
I - Imune  
J – ISS Suspenso por Decisão Judicial (neste caso, informar no campo Discriminação dos Serviços, o número do processo judicial na 1ª instância).

## **03. SOLUÇÃO**

Foi criado uma regra específica para a NFTS de São Paulo, em que não considera o tipo recolhimento dos dados fiscais da Filial. É considerado o que foi registrado no item ou no lançamento do tipo tributo ISS.
