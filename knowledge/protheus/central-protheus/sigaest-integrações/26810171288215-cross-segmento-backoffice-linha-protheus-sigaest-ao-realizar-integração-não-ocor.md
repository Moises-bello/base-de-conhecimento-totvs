---
article_id: 26810171288215
category: SIGAEST - INTEGRAÇÕES
content_hash: 36ba3f3dba18899c910955e9b6ef4a10be6737b000d37efb065cf745c6a9b990
fetched_at: '2026-06-28T22:38:46.213046+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao realizar integração
  não ocorre erro, porém não gera mensagem na XX3
type: support-article
updated_at: '2024-10-03T14:45:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26810171288215-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-realizar-integra%C3%A7%C3%A3o-n%C3%A3o-ocorre-erro-por%C3%A9m-n%C3%A3o-gera-mensagem-na-XX3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26810133303319) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao efetuar uma integração o Protheus não informa nenhum erro, porém não gera mensagem na XX3 não integrando com outro sistema  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release Todas as versões  
  
**Causa**Esse tipo de caso geralmente está ligado quando ocorre um desbalanceamento entre o campo XX4\_FILIAL e XX4\_FILEXE, onde o tamanho de um campo esta menor que outro.   
  
Quando isso ocorre apesar de não gerar um erro na integração o Protheus, não efetua o envio dos dados e nem gera a XX3 com XML.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
**Em ambiente de homologação:**  
1. Verifique em sua XX4 o tamanho dos campo, exemplo abaixo;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26810171245847)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26810133307159)  
  
  
2. Após isso efetue o backup de sua XX4, para não ocorrer a necessidade de cadastrar novamente os ADAPTER's;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26810133310359)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26810171250583)  
  
  
3. Efetue o DROP da XX4, e após isso feche a tabela;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26810171254039)

4. Abra o SIGACFG, e entre no cadastro de ADAPTER's;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26810171255447)

5. Abra novamente a XX4 e efetue o Apeend do Backup;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26810171256727)![](https://centraldeatendimento.totvs.com/hc/article_attachments/26810171258519)

Agora o sistema já irá gerar XX3, onde caso ocorra algum erro irá ser reportado nos logs da mesma.

***Saiba mais:***

[*Clique aqui e veja mais artigos sobre Integrações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)
