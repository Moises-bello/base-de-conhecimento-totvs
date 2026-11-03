---
article_id: 4409685121943
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 6f6e7043f39067166856f909592383d38e3fafa7a70d349c64842860624153b5
fetched_at: '2026-06-28T22:38:28.503427+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - array out of
  bounds ( 0 of 0 )  on AT600ORC(FATN600A.PRW)
type: support-article
updated_at: '2021-09-29T15:09:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409685121943-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-array-out-of-bounds-0-of-0-on-AT600ORC-FATN600A-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**

Ao utilizar a proposta comercial está gerando o erro: **array out of bounds ( 0 of 0 )  on AT600ORC(FATN600A.PRW) 19/03/2020 14:55:11 line : 441**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Causa**O erro ocorria por falta de uma validação na função **At600Orc** , corrigida pela equipe de desenvolvimento.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do pacote de expedição contínua do módulo faturamento, conforme o seu release: **[SIGAFAT](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859)**   
2. Via  **Vs-Code**, aplique o pacote no ambiente desejado. Lembrando de sempre validar atualizações em ambiente de tes primeiro e efetuar backup do ambiente.  
3. Reinicie o Smartclient e refaça o processo.

***Obs. O processo descrito acima requer conhecimentos de estrutura e VS-CODE, em caso de dúvidas sobre como utilizar o VS-Code, contate nossa equipe de Advpl para auxiliar.***

***Cliente com ambiente cloud, solicitar a equipe cloud a atualização do ambiente desejado.***
