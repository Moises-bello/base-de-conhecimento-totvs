---
article_id: 360045402233
category: ADVPL - Web Service
content_hash: 67642dae0e57fbc5e3d232e45533a5ac10a317ac1e873bdde058b99c302df657
fetched_at: '2026-06-28T22:40:10.175605+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Codigos de erros
  HTTP mais comuns
type: support-article
updated_at: '2022-06-14T12:58:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045402233-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Codigos-de-erros-HTTP-mais-comuns
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**O que significa os erros 400 ,401,403 ,404 e 500 no ***WebService***?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**

Os códigos de *status* das respostas HTTP indicam se uma requisição HTTP foi corretamente concluída. As respostas são agrupadas em cinco classes:

* Respostas de informação (`100`-`199`);
* Respostas de sucesso      (`200`-`299`);
* Redirecionamentos          (`300`-`399`);
* Erros do cliente                (`400`-`499`);
* Erros do servidor             (`500`-`599`).

Aqui, vamos comentar os códigos de erros mais comuns em uma requisição ***REST*** no **PROTHEUS**, porém para identificar o problema, precisara de uma analise mais a fundo por parte do desenvolvedor.

**400 *Bad Request***  
Alguma regra de negocio foi violada ou algum parâmetro estava incorreto  
  
**401 *Unauthorized***  
Usuário não está autenticado, ou a autenticação é invalida   
  
**403 *Forbidden***  
Usuário está autenticado, mas não possui permissão para acesso   
  
**404 *Not Found***  
Não foi encontrado o recurso.  
  
**500 *Internal Server Error***  
O servidor encontrou uma situação com a qual não sabe lidar.(Geralmente erros na customização)

**Saiba mais**[Códigos de status de respostas HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status)
