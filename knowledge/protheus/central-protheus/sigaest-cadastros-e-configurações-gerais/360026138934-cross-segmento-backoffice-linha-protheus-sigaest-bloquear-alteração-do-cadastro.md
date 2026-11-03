---
article_id: 360026138934
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 48b512a229b5d80bf38de183688ff480e4e678a885bff17ff7bf979362cde0f3
fetched_at: '2026-06-28T22:39:08.049616+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloquear alteração
  do cadastro de TES (MATA080)
type: support-article
updated_at: '2022-06-24T19:55:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026138934-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloquear-altera%C3%A7%C3%A3o-do-cadastro-de-TES-MATA080
---

**Dúvida**É possivel bloquear a alteração do cadastro de TES?  
  
**Ambiente**Microsiga Protheus – Estoque/Custos – A partir da versão 11.80  
  
**Solução**

- Via configurador (SIGACFG), acesse o menu **Usuário** > **Senhas** > **Usuários;** 

- Selecione o Usuário, clique em **Alterar > Restrições de Acessos > Ambientes** e selecione o Ambiente Estoque/Custos;

- Clique em **Outras Ações** > **Restrição de rotina do menu;**

- Selecione a rotina MATA080 e clique em **"Acesso"**;

- Será aberta a janela abaixo, deixando a cargo do usuário desmarcar ou marcar as opções de acordo com o desejado:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100277914/mceclip0.png)

Obs: Como sugestão, deixe configurado os principais campos, exemplo: 'gera duplicata', 'atualiza estoque' e 'poder de/em terceiros' entre outros, conforme a necessidade operacional de sua empresa. Sendo assim após a inclusão do cadastro, os campos ficarão bloqueados para alteração por parte do usuário.

Caso queira restringir acesso a outras rotinas, **[clique aqui e veja como](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018868272-MP-ADVPL-Restri%C3%A7%C3%B5es-de-acessos-a-rotinas-especificas-).**

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
