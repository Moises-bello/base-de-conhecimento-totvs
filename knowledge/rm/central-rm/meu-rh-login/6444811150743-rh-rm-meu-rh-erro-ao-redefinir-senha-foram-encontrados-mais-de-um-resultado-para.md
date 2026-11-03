---
article_id: 6444811150743
category: Meu RH - Login
content_hash: 325978da3194fcbc603c1ee5c9115c18789030e2a3fdc77e396f37d415905008
fetched_at: '2026-06-28T22:47:27.280284+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Erro ao redefinir senha "Foram encontrados mais de um resultado
  para o login informado"
type: support-article
updated_at: '2026-01-16T15:26:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6444811150743-RH-RM-Meu-RH-Erro-ao-redefinir-senha-Foram-encontrados-mais-de-um-resultado-para-o-login-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24075409280663) Tempo aproximado para leitura: **00:03:41 min**  
  
**Ocorrência**  
Ao tentar redefinir a senha de primeiro acesso do Meu RH em determinado usuário, é apresentado a mensagem de erro:   
***Foram encontrados mais de um resultado para o login informado. Verifique se existe algum login/e-mail cadastrado em duplicidade.***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6517948015383)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) – Meu RH – A partir da 12.1.33  
  
**Causa**  
Esse erro é apresentado quando há mais de um registro de acesso utilizando o mesmo nome no campo de usuário ou no campo de e-mail. Dessa forma o sistema não consegue identificar qual registro deve ser alterado já que os dados são idênticos.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Vá até registros de usuários pelo caminho **Serviços Globais > Segurança > Perfil,** e procure pelo usuário ou o e-mail cadastrado a fim de encontrar os dois registros duplicados: *(ex abaixo)*

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6518092824727)  
  
**2.** Após econtrar, basta alterar o e-mail de cadastrado em qualquer um dos dois registros, tornando-os registros únicos.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6518220676247)

Após ajustar, será possível redefinir a senha sem erro:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6518318503703)
