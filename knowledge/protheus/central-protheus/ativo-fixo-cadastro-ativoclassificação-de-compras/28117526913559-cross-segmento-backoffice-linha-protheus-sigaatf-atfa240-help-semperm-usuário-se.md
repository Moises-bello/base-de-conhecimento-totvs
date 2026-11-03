---
article_id: 28117526913559
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 13692a509a09848c8679db925e6301323440d5c63aac35c52e4a0b7ae5350ec6
fetched_at: '2026-06-28T22:41:48.255561+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA240 - HELP: SEMPERM
  usuário sem permissão para utilizar esta rotina'
type: support-article
updated_at: '2024-11-27T20:24:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28117526913559-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-HELP-SEMPERM-usu%C3%A1rio-sem-permiss%C3%A3o-para-utilizar-esta-rotina
---

Ocorrência:

Quando usuário tentar realizar uma classificação de compras através da rotina ATFA240 (Classificação de Compras) é apresentado HELP: SEMPERM

![sem_perm.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28117526890775)

Ambiente:  
Cross Segmento - Backoffice Linha Protheus –  Ativo Fixo  – Todas as versões

Causas:

Este HELP é apresentado quando o Acesso '3 e 43' do Cadastro Usuário ou Grupo de Usuários está desmarcado.

Solução:

Primeiramente verificar o Cadastro de Usuários (CFGA510) seguindo os seguintes passos:

1. Acesse o Configurador (SIGACFG);  
2. Usuário > Senhas > Usuários;  
3. Selecione o Usuário > Alterar;  
4. Aba Restrições de acesso > Acessos;  
5. Verifique se o Acesso '3 - Excluir Cadastros' está Marcado;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28117526892695)

6. Verifique também se o Acesso '43 - Alterar o Bem no Ativo Fixo' está Marcado;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28117551680919)

Caso no cadastro de usuário esteja correto, verifique no Cadastro de Grupos (CFGA520) seguindo os seguintes passos:

1. Acesse o Configurador (SIGACFG);  
2. Usuário > Senhas > Grupos;  
3. Selecione o Grupo > Alterar;  
4. Aba Restrições de acesso > Acessos;

5. Verifique se o Acesso '3 - Excluir Cadastros' está Marcado;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28117526892695)

6. Verifique também se o Acesso '43 - Alterar o Bem no Ativo Fixo' está Marcado; **![](https://centraldeatendimento.totvs.com/hc/article_attachments/28117551680919)**
