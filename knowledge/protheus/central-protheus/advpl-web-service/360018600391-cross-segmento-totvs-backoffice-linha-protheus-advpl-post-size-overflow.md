---
article_id: 360018600391
category: ADVPL - Web Service
content_hash: 97670bbbc4ad32cfd6b4d3e71621389b6c02e9e12d7cd94fcd852d20437805e0
fetched_at: '2026-06-28T22:40:10.494649+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Post Size overflow
type: support-article
updated_at: '2021-12-29T14:06:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018600391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Post-Size-overflow
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**

Erro post size overflow, ocorre quando o número de informações (linhas) no WEBSESRVICE é grande.

Post Size overflow  
Post Size overflow  
Post Size overflowWEBSERVICE - Using ABENDLOCK configuration.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Causa**  
Esse erro ocorre devido a falta da definição da instância **maxStringSize**  
**Solução**  
É necessário que seja definida a instância **maxStringSize** no **AppServer.ini.**Essa instância define para a instância atual o comprimento máximo de uma cadeia de caracteres.  
  
Exemplo de conteúdo:  
[general]  
maxStringSize=2

**Saiba Mais**

[MaxStringSize](http://tdn.totvs.com/pages/viewpage.action?pageId=161349793)

[String size overflow](http://tdn.totvs.com/display/tec/String+size+overflow)
