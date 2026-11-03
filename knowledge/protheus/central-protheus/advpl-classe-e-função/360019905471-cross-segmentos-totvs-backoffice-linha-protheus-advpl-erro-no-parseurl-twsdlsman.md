---
article_id: 360019905471
category: ADVPL - Classe e Função
content_hash: df9fdc14e74707bfe5e2403cf294427c9d9b426e0807301228fc38d30df0e043
fetched_at: '2026-06-28T22:40:18.357192+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro no ParseURL
  TWSDLSManager
type: support-article
updated_at: '2022-01-10T14:29:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019905471-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-no-ParseURL-TWSDLSManager
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Problemas com a classe **TWSDLManager** utilizando o método **ParseURL**().   
"*Can't create file name:* *80*   
*Can't open file 1.: Invalid argument"*

Mesmo verificando todas as permissões de pastas e compartilhamento de rede o erro persiste.   
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Se o binário do protheus for **32** **bits** o erro ocorre quando a pasta **SysWOW64** está muito cheia  
Se o binário do protheus for **64 bits** o erro ocorre quando a pasta **System32** está muito cheia.

Quando essa pasta (C:\Windows\SysWOW64)  esta acima dos 65 mil arquivos o **TWSDLManager** só funciona com o server em modo console, apagando os arquivos (.**tmp**) da pasta ele volta a funcionar como serviço

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
Deletar os arquivos .**tmp** destas pastas
