---
article_id: 360031218914
category: eSocial - Saneamento de Dados
content_hash: 8c1ce102633a7d67753dd2f412c017c05386fe59874aec91a596afd75f51574b
fetched_at: '2026-06-28T22:47:13.803697+00:00'
product: rm
section_id: 1500000834361
source: central-rm
title: RH - RM - FOP - eSocial - Validação da base para demitidos antes da obrigatoriedade
  do eSocial
type: support-article
updated_at: '2024-06-20T16:29:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031218914-RH-RM-FOP-eSocial-Valida%C3%A7%C3%A3o-da-base-para-demitidos-antes-da-obrigatoriedade-do-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24315715374231) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Como realizar a validação da base de dados para funcionários demitidos antes da obrigatoriedade do eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da 12.1.22  
  
**Solução**Foi criado em **eSocial | Saneamento de Dados | Validador da Base de Dados** o parâmetro **Considera Demitidos Antes da Obrigatoriedade** para que o sistema possa realizar a validação para demitidos.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042180074)

Será considerada a data do último movimento no cadastro de rescisão para a comparação com a data da competência atual ou com a data de entrega dos eventos **Não Periódicos** no parametrizador. Assim, com o parâmetro marcado, os funcionários demitidos antes da data de obrigatoriedade registrada em **Configurações | Parametrizador | eSocial | Configurações Gerais 1/5**, campo **Não Periódicos**, serão considerados no validador. Sem a marcação do parâmetro, tais funcionários serão desconsideração na validação.  
  
**Saiba mais**  
Para mais informações, acesse:

* [Validação de dados da base para demitidos antes da data de obrigatoriedade de eventos não periódicos](http://tdn.totvs.com/pages/releaseview.action?pageId=415697370)
* [Validador da Base de Dados](http://tdn.totvs.com.br/display/public/LRM/Validador+da+Base+de+Dados)
