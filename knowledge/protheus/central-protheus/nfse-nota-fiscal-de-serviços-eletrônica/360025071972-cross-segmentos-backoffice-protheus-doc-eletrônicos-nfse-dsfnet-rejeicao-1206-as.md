---
article_id: 360025071972
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 683a39eb2cfcf68f1bce5825e51fb0fbf8558d393802ea96e9eda8bfb29e244d
fetched_at: '2026-06-28T22:39:56.475189+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - DSFNET:
  Rejeicao_1206_Assinatura_do_RPS_Incorreta '
type: support-article
updated_at: '2025-07-08T19:59:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025071972-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-DSFNET-Rejeicao-1206-Assinatura-do-RPS-Incorreta
---

**Dúvida**REJEIÇÃO 1206: Assinatura do RPS incorreta. Código Hash gerado para o campo assinatura do RPS está inválido.  
  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

O manual webservice DSFNET, passa o procedimento abaixo para correção do erro 1206:

"O campo Assinatura do RPS não esta correto, verifique a regra de preenchimento deste campo no manual."

O código Hash gerado para Assinatura do RPS é montado pelo TSS, porém é composto pelas informações abaixo, conforme layout DSFNET, ou seja, se houver informações incorretas o código Hash ficará incorreto e será apresentado a rejeição.

Nesse caso, deverá analisar os dados abaixo para RPS em questão e corrigir o que for necessário para autorização da nota.

01 - Inscrição municipal do contribuinte  
02 – Série do RPS  
03 – Número do RPS  
04 – Data de Emissão do RPS  
05 – Tributação  
06 - Situação do RPS  
07 - Tipo Recolhimento, se for “A” preenche com “N” senão “S”  
08 - Valor do serviço subtraindo a dedução  
09 - Valor da Dedução  
10 - Código da atividade  
11 - CPF/CNPJ do tomador

Após alteração cadastral, refaça a nota.  
  
*Obs: Para algumas prefeituras que utilizam o mesmo Provedor (DSFNET) o arredondamento do Valor Total da Nota pode causar esta rejeição.*
