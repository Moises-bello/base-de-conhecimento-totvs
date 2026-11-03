---
article_id: 360024556551
category: ADVPL - Classe e Função
content_hash: eb367ed6db0f0a720c9a8606c749842eaec5355bbc3bb272dc284a0bd00d934a
fetched_at: '2026-06-28T22:40:19.495823+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - FwFileReader posicionar
  no topo e/ou retornar uma linha
type: support-article
updated_at: '2022-01-10T22:29:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024556551-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-FwFileReader-posicionar-no-topo-e-ou-retornar-uma-linha
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Teria algum modo de posicionar na primeira linha de um arquivo ou retornar a quantidade de linhas do mesmo?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**A classe FwFileReader() não permite o posicionamento no início do arquivo após a leitura completa, assim sendo, para posicionar em uma linha específica, será necessário o uso do método GetAllLines() para retornar um vetor com todas as linhas e utilizar o índice do vetor para posicionar na linha desejada.  
  
**Saiba mais**  
[FWFileReader - Realiza a leitura do conteúdo de um arquivo](http://tdn.totvs.com/display/framework/FWFileReader)
