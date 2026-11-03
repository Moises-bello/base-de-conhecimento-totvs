---
article_id: 16447759856151
category: 'Aplicativo MNTNG '
content_hash: 8781df6f4daebd8e9a27e23089cb7b07b2c4ad384784924725a198e01c1a0bdd
fetched_at: '2026-06-28T22:42:37.616493+00:00'
product: protheus
section_id: 360010992174
source: central-protheus
title: Manufatura - Linha Protheus - APP MNT - Como Configurar no Aplicativo MNT NG
  a Regra/Conceito de Autenticação Single sign-on
type: support-article
updated_at: '2026-05-08T11:30:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16447759856151-Manufatura-Linha-Protheus-APP-MNT-Como-Configurar-no-Aplicativo-MNT-NG-a-Regra-Conceito-de-Autentica%C3%A7%C3%A3o-Single-sign-on
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16447788460951)*** Tempo aproximado para leitura: **00:00:50 min**  
  
**Dúvida**  
Como configurar no aplicativo **MNT NG** a regra/conceito de autenticação *Single sign-on*?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura Linha Protheus - Aplicativo MNT NG - Todas as versões  
  
**Solução**  
Para que o usuário utilize esta funcionalidade, é necessário realizar algumas configurações no **Protheus***.* Desta forma, basta seguir as instruções:  
  
No **Protheus** é necessário definir a integração do **Protheus** com o *Single sign-on*.  
Para definir a integração acesse o módulo **Configurador** - **SIGACFG** e navegar pelos menus **Usuário / Senhas / Política.** No campo **Habilitar** *Single sign-on -***USR\_SSIGNON** selecione a opção **1 - Obrigatório** ou **2 - Opcional** e no campo **Modalidade de** *Single sign-on -* **USR\_SSOTYPE** a opção de acordo com a modalidade que deseja utilizar Neste exemplo estamos utilizando a modalidade **3 - Active Directory**. Ao parametrizar no configurador o campo **Habilitar** *Single sign-on -* **USR\_SSIGNON** como **1 - Obrigatório**, este torna-se o único meio de autenticação do usuário, já na configuração na qual o campo **Habilitar** *Single sign-on -* **USR\_SSIGNON** é definido como **2 - Opcional**, a utilização do usuário e senha padrão do **Protheus** também são permitidos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16444978071575)

Após confirmar os ajustes na política, basta incluir um usuário no **Protheus** ainda no módulo Configurador através do menu **Usuário / Senhas / Usuários.** Selecione a opção incluir e preencha as informações necessárias para efetuar o *login* no aplicativo posteriormente. Na aba ***Active Directory***, informar o usuário que será utilizado pelo *Active Directory* correspondente a este usuário do Sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16445502146839)  
  
Após essa configuração será possível logar com o *Single sign-on* tanto no aplicativo **MNT NG** quanto no **Protheus**.
