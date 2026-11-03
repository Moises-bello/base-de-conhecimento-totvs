---
article_id: 15072529307927
category: Call Center - Telecobrança
content_hash: 259c649b233ef3176eec58f66097d19babc5645f45778b0b562eecf674a6b1bb
fetched_at: '2026-06-28T22:41:28.733640+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - Como gerar
  log na rotina de Seleção de Títulos (TMKA180)?
type: support-article
updated_at: '2025-01-10T19:42:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15072529307927-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Como-gerar-log-na-rotina-de-Sele%C3%A7%C3%A3o-de-T%C3%ADtulos-TMKA180
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar log na rotina de Seleção de Títulos (TMKA180)?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - a partir da versão 12.1.33  
  
**Solução**Ao realizar o processo de Seleção de Títulos (TMKA180) é apresentada a seguinte opção abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15071721436695)  
  
Ao selecionar a opção SIM, será gerado, na pasta System do Protheus, o arquivo "tmka180sk1.sql" contendo a uma query (Pesquisa de Banco de Dados) relacionada a tabela de "Referência do Contas a Receber" (SK1).  
  
Os arquivos "tmka180ae1" e "tmka180be1" também são criados na System ao executar a seleção de títulos. Estes arquivos são gerados independente da opção utilizada (SIM ou NÃO), os mesmos possuem referencias de queries relacionadas a tabela de "Contas a Receber" (SE1).
