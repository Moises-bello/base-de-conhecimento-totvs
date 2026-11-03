---
article_id: 360031739273
category: Configurador
content_hash: 9361e829ba5cb43a6619ea7fcba44dd423f3ddab0165bfeac207d4ceed6f2184
fetched_at: '2026-06-28T22:42:19.252162+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Reset de Senha do Admin com Dicionário no Banco
type: support-article
updated_at: '2024-05-08T11:57:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031739273-Framework-Linha-Protheus-Reset-de-Senha-do-Admin-com-Dicion%C3%A1rio-no-Banco
---

**Dúvida**Como posso efetuar o reset da senha do Admin, tendo base com o Dicionário de Dados no Banco de Dados?  
  
**Ambiente**Protheus - Configurador - Versão 12  
  
**Solução**Para bases que utilizam o **Dicionário de Dados no Banco de Dados**, o arquivo de usuários e senhas não fica fisicamente em uma pasta da estrutura do Protheus, fica dentro do Banco de Dados. Mediante esta situação, foi criado um mecanismo específico de recuperação da senha do usuário Administrador do Protheus caso necessário.  
  
Recomendamos sempre que os dados de SMTP estejam configurados (Configurador > Usuário > Senhas > Política > Aba **Conexões**), e que o usuário Admin possua um **e-mail cadastrado**, pois desta forma, ao clicar em **Esqueceu sua senha**, uma nova senha temporária é enviada para o e-mail do Admin.  
  
Contudo, se eventualmente o usuário estiver sem um e-mail cadastrado, ou se os dados de SMTP não estiverem configurados ou estiverem incorretos, será necessário o envio de um **Token** para o **Suporte Framework Protheus**, e então entrar em contato com o Suporte com as informações necessárias para receber o Token.  
  
Para o procedimento detalhado para obtenção do Token e Reset da Senha do Admin, clique no link abaixo:  
<http://tdn.totvs.com/pages/viewpage.action?pageId=433237404>
