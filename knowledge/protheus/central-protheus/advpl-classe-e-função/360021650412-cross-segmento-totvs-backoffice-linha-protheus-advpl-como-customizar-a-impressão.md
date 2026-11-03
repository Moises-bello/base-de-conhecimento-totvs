---
article_id: 360021650412
category: ADVPL - Classe e Função
content_hash: 1e73922cb62887901f51b66a49f77642ec2ac69a971121881a6ae076b24d8f28
fetched_at: '2026-06-28T22:40:15.515457+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como customizar
  a impressão da NFE  em impressoras não fiscais. '
type: support-article
updated_at: '2022-01-04T20:04:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021650412-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-customizar-a-impress%C3%A3o-da-NFE-em-impressoras-n%C3%A3o-fiscais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como customizar a impressão da NFE em impressoras não fiscais?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Para realizar as modificações utilizando a impressora não fiscal que esta configurada no cadastro de estações realize os seguintes procedimentos:

1 - O parâmetro MV\_LJSTPRT deve estar com o conteúdo = 1 , Imprime Não Fiscal.

2 - Realize as modificações na Função LjRDnfNFCe , esta função se encontra no Rdmake LojRNfce.prw. Rdmake que é baixado do portal.

3 - Verifique se as alterações foram compiladas no RPO, ver a data e horário do fonte no repositório.

4 - Um teste simples, realize a modificação de alguma string como "NOTA FISCAL DE CONSUMIDOR ELETRÔNICA"

**Saiba mais**[DT\_MV\_LJSTPRT](http://tdn.totvs.com/display/public/PROT/DT_MV_LJSTPRT)
