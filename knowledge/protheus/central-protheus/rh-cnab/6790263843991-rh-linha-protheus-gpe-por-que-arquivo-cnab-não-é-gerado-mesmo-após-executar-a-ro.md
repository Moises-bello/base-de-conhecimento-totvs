---
article_id: 6790263843991
category: RH - CNAB
content_hash: c4ba1faed6f8e452561394f3082e1c6f55e1553cc7f7dd0ac741f6d055708141
fetched_at: '2026-06-28T22:43:39.318505+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Por que arquivo CNAB não é gerado mesmo após executar
  a rotina o sistema apresentar log de ocorrência com o valor do arquivo
type: support-article
updated_at: '2025-06-17T18:15:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6790263843991-RH-Linha-Protheus-GPE-Por-que-arquivo-CNAB-n%C3%A3o-%C3%A9-gerado-mesmo-ap%C3%B3s-executar-a-rotina-o-sistema-apresentar-log-de-ocorr%C3%AAncia-com-o-valor-do-arquivo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32877294881559) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Por que arquivo CNAB não é gerado mesmo após executar a rotina e o sistema apresentar *log* de ocorrência com o valor do arquivo?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Uma das causas que podem levar o CNAB a não ser gerado é o preenchimento incorreto do campo **Arquivo de Saída** em parâmetros. Caso seja informada somente a pasta (diretório) para geração, o arquivo não será gerado, é necessário informar a pasta de destino com um nome para o arquivo.

**Exemplo:**

**Somente com o diretório de destino.**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6790129493911)

**Com diretório e nome arquivo.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6790121659031)

**Saiba Mais**

[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
