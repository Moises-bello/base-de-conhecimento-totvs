---
article_id: 360026238652
category: Configurador
content_hash: 9a859f57ccc03d29a8102d3a1019224d5f83baddd329291d629991de5a279514
fetched_at: '2026-06-28T22:42:19.068560+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Login no Protheus com Active Directory
type: support-article
updated_at: '2024-05-08T11:52:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026238652-Framework-Linha-Protheus-Login-no-Protheus-com-Active-Directory
---

**Dúvida**  
É possível integrar o login do Protheus ao Active Directory, fazendo um login único?  
  
**Ambiente**  
Protheus - Configurador - A partir da versão 11  
  
**Solução**O Protheus permite a integração do login de usuário Protheus com o usuário de rede do AD (Active Directory). Desta forma, pode-se vincular um usuário do Protheus a um usuário do AD, e então o Protheus passará a aceitar o login pelo usuário de rede.  
  
Para efetuar esta configuração, siga os passos abaixo:  
1. Acesse Configurador > Usuário > Senhas > **Política**  
2. Na primeira aba (Política de Segurança / Regras de senha), altere a opção **Habilitar single sign-on** para **Obrigatório** (se quiser forçar o uso do Single Sign-On com AD para todos os usuários) ou **Opcional** (se quiser permitir que os usuários façam login com seu próprio usuário e senha do Protheus, ou se utilizam o usuário de rede)  
3. Em **Modalidade de Single Sign-on**, selecione **Active Directory**, e clique em **Confirmar**![AD_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360025788811)  
  
4. Acesse o Cadastro de Usuários (Usuário > Senhas > **Usuários**)  
5. Clique sobre o usuário, e clique em **Alterar**  
6. Na aba principal (Usuário), clique na aba **Active Directory**  
7. Clique 2 vezes abaixo da coluna **Domínio** e digite o domínio de rede do seu AD  
8. Clique 2 vezes abaixo da coluna **Usuário** e digite o login do usuário de rede que ficará vinculado a este usuário do Protheus  
9. Clique em **Confirmar**  
  
![AD_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360025776332)  
  
10. Após essa configuração, ao abrir o Smartclient, já irá aparecer por padrão o domínio\nome de usuário de rede. Se você inserir a senha deste usuário de rede, ele já entra com o usuário do Protheus que está vinculado a ele.
