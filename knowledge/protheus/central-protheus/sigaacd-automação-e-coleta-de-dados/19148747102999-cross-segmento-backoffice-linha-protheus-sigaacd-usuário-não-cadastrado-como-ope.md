---
article_id: 19148747102999
category: SIGAACD - Automação e Coleta de Dados
content_hash: b69daf4489b4511b34deaeca9e4b41dd56c8a3766dc446806dfdc67d9a760e0b
fetched_at: '2026-06-28T22:39:13.876587+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Usuário não Cadastrado
  como Operador.
type: support-article
updated_at: '2026-01-27T12:07:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19148747102999-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Usu%C3%A1rio-n%C3%A3o-Cadastrado-como-Operador
---

Ao sincronizar o Aplicativo Meu Coletor de Dados, se aparecer a mensagem "Usuário não Cadastrado como Operador" ou "Usuário não Autenticado Offline", deve-se fazer backup da pasta Profile, abrir o arquivo Profile.usr ou MP\_SYSTEM\_PROFILE via APSDU, filtrar e deletar os itens P\_PROG='CONPAD' e P\_TASK='CONFIG'. Depois, limpar o cache do aplicativo no celular.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19148736625943) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**

Ao sincronizar o Aplicativo Meu Coletor de Dados ocorre a mensagem" Usuário não Cadastrado como Operador" como corrigir? 

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

**Ao apresentar o HELP** - Usuário não Autenticado Offline

Realize o procedimento abaixo em base de homologação:

* Backup da pasta Profile;
* Via APSDU abra o arquivo Profile.usr ou MP\_SYSTEM\_PROFILE caso o dicionário seja no banco;

Faça o Filtro com os dados abaixo via Banco de Dados ou APSDU:

* MP\_SYSTEM\_PROFILE **P\_PROG='CONPAD'**
* MP\_SYSTEM\_PROFILE **P\_TASK ='CONFIG'**
* Em seguida delete a pasta MP\_SYSTEM\_PROFILE e os itens P\_PROG='CONPAD' e P\_TASK ='CONFIG'
* Realize o backup das informações.

No aplicativo "Meu Coletor de Dados", limpar o cache no celular.

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
