---
content_hash: 0113a94ae917e4be54f78371c5ff751cfd9240183063f1da2d4a826ddc7b3a49
fetched_at: '2026-06-29T00:11:16.948691+00:00'
page_id: '674554533'
product: rm
source: tdn-rm
title: FISCAL01-17624 - DT Ajustes da Review na NFTS
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-17624+-+DT+Ajustes+da+Review+na+NFTS
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotinas Fiscais |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17624 |

## **02. SITUAÇÃO/REQUISITO**

Alterar o comportamento da NFTS (Campo 7 Registro 4) para que os Lançamentos de entrada não considerem a imunidade da Filial e sim o tipo de recolhimento do tributos ISS.

Manual da NFTS: [http://notadomilhao.prefeitura.sp.gov.br/cidadao/informacoes-gerais/manuais](http://notadomilhao.prefeitura.sp.gov.br/cidadao/informacoes-gerais/manuais "Follow link") - Manual de Envio de Arquivo - Emissão de NFTS em lote.

Devido ao grande risco de impacto, se a alteração for realizada no contexto, gentileza implementar de forma especifica para a NFTS de São Paulo,

Simulação:

Informações do campo 7, posição 30 do registro 4:

Informe a Situação com 01 posição.  
T - Operação normal  
I - Imune  
J – ISS Suspenso por Decisão Judicial (neste caso, informar no campo Discriminação dos Serviços, o número do processo judicial na 1ª instância).

## **03. SOLUÇÃO**

Foi alterado o campo 7 do layout da NFTS de São Paulo. É verificado apenas o Tipo Recolhimento do item de tributo ISS.  
Regra para preenchimento do campo 7 do registro 4:

Nenhum - T

Devido - T

RetidoFonte - T

RetidoFonte\_Deduzido - T

Deposito\_Juizo - T

Isento - T

Imune - I
