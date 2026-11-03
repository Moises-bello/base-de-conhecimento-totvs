---
article_id: 360050498933
category: ADVPL - Rotina Automática
content_hash: 81c4ae4884287fbfc373378d7ac151cb7e0648f654792fa38f844864e48712a9
fetched_at: '2026-06-28T22:40:23.986612+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - ADVPL - Empenhos Simples: ExecAuto'
type: support-article
updated_at: '2021-12-29T14:03:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050498933-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Empenhos-Simples-ExecAuto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Quando executado o ExecAuto() MATA380 é apresentado erro de; "**O Lote selecionado não possui saldo suficiente para este empenho.**"

**Ambiente**Protheus – ADVPL – A partir da versão P12  
  
**Solução**Quando existe saldo no produto/lote, informações a serem avaliadas.A informação do campo "**D4\_LOTECTL**" tem que ser enviada com o tamanho correto, de acordo com o tamanho no dicionário/banco de dados.   
**Exemplo**: Se o tamanho é 10, logo deve ser enviado como "**LOTE380** ", adicionando os espaços.  
O array de empenhos tem que ser enviado por parâmetro para o **MsExecAuto**, dessa forma: **MSExecAuto({|x,y,z| mata380(x,y,z)},aVetor,3,aEmpenhos)**

**SAIBA MAIS****[MATA380 - Ajuste de Empenhos](https://tdn.totvs.com/display/public/PROT/MATA380+-+Ajuste+de+Empenhos)**
