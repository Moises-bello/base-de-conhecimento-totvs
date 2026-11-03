---
article_id: 12386801718167
category: eSocial - Gerar XML/ Integração Evento
content_hash: b4a93f879504ff1fc1cf9380cc47aff009d23b2f09c629f3004777c9cc71bc9f
fetched_at: '2026-06-28T22:47:13.031303+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Gatilho do evento S-1005 não é criado na Fila de
  Eventos após mudança do FAP
type: support-article
updated_at: '2024-12-30T13:56:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12386801718167-RH-RM-FOP-eSocial-Gatilho-do-evento-S-1005-n%C3%A3o-%C3%A9-criado-na-Fila-de-Eventos-ap%C3%B3s-mudan%C3%A7a-do-FAP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00****:03:00 min** **Dúvida**Gatilho do evento S-1005 não é criado na Fila de Eventos após mudança do FAP.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Mediante a [notícia publicada no site do eSocial no dia 26/07/2021](https://www.gov.br/esocial/pt-br/noticias/ajuste-no-procedimento-de-informacao-do-fap-em-s-1005-versao-s-1.0), foi realizado um ajuste no procedimento de informação do FAP no evento S-1005 para a versão S-1.0. Com isto, o gatilho do evento S-1005 não é gerado automaticamente ao alterar o FAP no sistema. 

Esse ajuste será temporário até que a situação no ambiente do governo seja regularizada, uma vez que somente deve-se preencher os campos **GILRAT** e **FAP** quando houver processo **Judicial/administrativo** com **Decisão/sentença** favorável à utilização de alíquota GILRAT ou do FAP diferentes do que é definido pela administração, nos demais casos, os referidos campos não devem ser preenchidos. Conforme instrução do leiaute:

                                                                          *Tag* aliqGilrat

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12461424712087)

**Importante**  
Para os casos em que apresentar o erro **1801 - O FAP do estabelecimento não foi localizado na base**, ou que a empresa queira encaminhar a informação mesmo não sendo obrigatória, será necessário seguir o passo a passo de um dos artigos abaixo:

  • Usuários Middleware:  [Middleware - Erro código 1801: O FAP do estabelecimento não foi localizado na base](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5012268624791-RH-RM-FOP-eSocial-Middleware-Erro-c%C3%B3digo-1801-O-FAP-do-estabelecimento-n%C3%A3o-foi-localizado-na-base-)  
  • Usuários TAF:  [TAF - Erro código 1801: O FAP do estabelecimento não foi localizado na base](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5023139966359-RH-RM-FOP-eSocial-TAF-Erro-c%C3%B3digo-1801-O-FAP-do-estabelecimento-n%C3%A3o-foi-localizado-na-base-#:~:text=Ao%20enviar%20o%20evento%20S,n%C3%A3o%20foi%20localizado%20na%20base.&text=Mediante%20a%20not%C3%ADcia%20publicada%20no,para%20a%20vers%C3%A3o%20S%2D1.0.)
