---
article_id: 360018453112
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 1c8e67d0743d777c66e51a5684b40d3807f6f6ceb4ddbc0d211d39890ce26714
fetched_at: '2026-06-28T22:38:43.913760+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Qual o procedimento
  para gerar uma NCC pelo módulo  faturamento
type: support-article
updated_at: '2023-03-13T21:39:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018453112-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Qual-o-procedimento-para-gerar-uma-NCC-pelo-m%C3%B3dulo-faturamento
---

**Dúvida**

Qual procedimento para gerar uma **NCC** pelo módulo de faturamento?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Para solucionar , efetue o procedimento abaixo:

1- Registrar Documento de Saída com um TES que gera duplicata e no qual esteja relacionado o devido TES de Devolução;  
**Observação:** O TES de Devolução deverá Gerar Duplicata = Sim.

2 -O Documento de Saída gera título de Tipo "NF" no "Financeiro > Funções Ctas a Receber";

3- Ao Incluir um "Retorno" pela rotina de documento de Entrada relacionando ao documento de Saída. Ele irá trazer o TES de Devolução que foi registrado no TES de Saída;

4- O Documento de Entrada gera título de Tipo NCC no Financeiro > Funções Ctas a Receber;

5- Para realizar a Compensação da Nota de Crédito, selecionar o NCC:

Ações Relacionadas > Compensação > OK > Selecione o título que se deseja compensar > Confirmar valor (Total / parcial) a compensar > OK

Para visualização das telas do Protheus, acesse a FAQ no TDN:**[FAQ de Apoio para Geração de NCC (Nota de Crédito Cliente) pelo módulo de Faturamento](http://tdn.totvs.com/display/PROT/FAT0129_Gerar_NCC_Pelo_Modulo_Faturamento)**
