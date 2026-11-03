---
article_id: 4410633146519
category: eSocial - Middleware
content_hash: d981c7c6f41ae7ade0b8f359c5bbe22af7037214849a10a868fad986643bee18
fetched_at: '2026-06-28T22:47:05.576214+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na ativação do Middleware: (404) Not Found'
type: support-article
updated_at: '2025-02-26T19:41:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410633146519-RH-RM-FOP-eSocial-Erro-na-ativa%C3%A7%C3%A3o-do-Middleware-404-Not-Found
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao realizar a ativação do Middleware é apresentado o erro: **Ocorreu erro que impediu a execução do processo. The remote server returned an error: (404) Not Found. {"errorCode":404,"errorMessage":"The server can't find the requested resource."}**.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro geralmente ocorre quando o TAF não está atualizado para a versão compatível com o Middleware, ou quando a instalação do TAF não foi realizada de forma adequada.  
  
**Solução**Para validação, informe no navegador web (Chome, Firefox, Internet Explorer, etc.) a URL do **Web Service do TAF** seguido da palavra **rest**, conforme exemplo abaixo.

***http://servidor:porta/rest***

Deve-se localizar a *API* de nome **WSESOCIAL**, responsável pela transmissão e consulta de dados para o Middleware.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410625269143/mceclip0.png)

Caso não encontre o serviço, deverá verificar se a instalação do TAF foi feita de forma adequada ou se o TAF está atualizado conforme pacote mais atual disponível na Central de Downloads.  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [TAF - ATUALIZAÇÃO - Como atualizar o TAF e o TSS via atualizador? (SEGREGADO)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020127812)  
     - [Mensagem de erro 404 na ativação do Middleware](https://tdn.totvs.com/pages/releaseview.action?pageId=544710507)
