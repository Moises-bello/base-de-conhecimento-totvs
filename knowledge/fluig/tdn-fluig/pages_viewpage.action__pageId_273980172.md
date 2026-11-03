---
content_hash: 9ef200ba1d6d81a1a73e7d3c875ec1aaf3b38507c01349dada70d100fa7b1fea
fetched_at: '2026-06-28T21:35:25.046326+00:00'
page_id: '273980172'
product: fluig
source: tdn-fluig
title: Identity | Notificações via e-mail
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273980172
version: 40
---

# Falando de notificações via e-mail...

---

O conteúdo das mensagens de e-mail enviadas pelo TOTVS Identity pode ser visualizado e editado pelo administrador da empresa. Os *templates* de e-mail podem ser alterados diretamente pelo editor *online* disponibilizado na página de Notificações via e-mail. O editor possui opções de formatação de fonte, tabulação, cores, inclusão de imagens, *links*, etc.

O idioma da mensagem é definido pelo Identity de acordo com o dialeto configurado no navegador do usuário que executou a ação. Por exemplo, a mensagem "Redefinir Senha via código" é enviada no idioma do usuário que solicitou a redefinição. Já o e-mail de convite "Novo Usuário" é enviado no idioma utilizado pelo administrador que adicionou a nova conta.

Também é possível bloquear o envio de determinados tipos de mensagens, como o convite para novos usuários e redefinição de senha removendo o conteúdo do respectivo *template*.

## Visualizar *template*de e-mail

---

**01.** Acione o ícone **Configurações**  no canto superior direito e selecione a opção **Notificações via e-mail**.

**02.** Escolha o *template* que deseja visualizar.

#f2f2f2#f2f2f2

Os *templates* de e-mail disponíveis por padrão são:

* **Novo Usuário**
* **Redefinir Senha (Desativado)**
* **Redefinir Senha via código**
* **E-mail de Teste**
* **E-mail de Verificação**
* **Auto-inscrição**
* **Sucesso na Alteração de Senha**
* **Sucesso no Desbloqueio do Usuário**
* **Erro na alteração/desbloqueio de senha**
* **Recurso de Segurança Bloqueado**
* **Geração de relatório iniciada**
* **Geração de relatório concluída**
* **Confirmação de troca de e-mail**
* **Aviso de e-mail alterado**
* **Aviso de expiração de senha**
* **Usuário bloqueado**

Nota:

Os *templates* **Aviso de expiração de senha** e **Usuário bloqueado** são criados automaticamente quando as regras são habilitadas na  da empresa.

**03.** Selecione o idioma em que deseja visualizar o *template*. Os idiomas disponíveis por padrão são: **Inglês**, **Português** ou **Espanhol**.

#f2f2f2#f2f2f2

Após a seleção do *template,* o assunto e o conteúdo do *template* de e-mail são apresentados para visualização em seus respectivos campos.

## Editar *template* de e-mail

---

***100%true5%***

**01.** Acione o ícone **Configurações**  no canto superior direito e selecione a opção **Notificações via e-mail**.

**02.** Escolha o *template* que deseja alterar.

**03.** Selecione o idioma do *template* de e-mail.

**04.** Clique em **Editar** e faça as alterações necessárias no *template*.

#f2f2f2#f2f2f2

Os campos **Assunto**e **Conteúdo** são habilitados para a edição do *template* de e-mail selecionado.

No conteúdo, é possível utilizar variáveis específicas para incluir mais informações na mensagem (por exemplo, o nome da empresa, usuário e IP da máquina do usuário). Para isso, posicione a barra de digitação onde deseja inserir a informação e clique em **Ver variáveis**, marque os itens necessários e clique em **Salvar** para adicioná-los ao conteúdo do template.

@gerais trueClique aqui e veja as variáveis

@gerais#ebecf0

| Item | Variável |
| --- | --- |
| Nome da Empresa | COMPANY\_NAME |
| Nome do Usuário | USER\_FIRST\_NAME |
| Sobrenome do Usuário | USER\_LAST\_NAME |
| Nome completo do Usuário | FULL\_NAME |
| URL de Ativação | NAV\_URL |
| IP da Máquina do Usuário | IP\_MACHINE |
| Tentativa de alteração/desbloqueio de senha | ATTEMPT\_NUMBER |
| Código para reset de senha | RESET\_CODE |
| URL de redirecionamento | REDIRECT\_URL |
| E-mail atual | CURRENT\_EMAIL |
| Novo e-mail | NEW\_EMAIL |
| Data de expiração da senha | PASSWORD\_DTEXPIRATION |

**05.** Acione **Salvar** para salvar as alterações.

#f2f2f2#f2f2f2

Ao salvar as alterações, os próximos e-mails já devem ser enviados com o novo conteúdo.

É necessário repetir os passos acima para todos os *templates* e idiomas desejados.

## Testar o envio do *template* de e-mail

---

**01.** Acione o ícone **Configurações**  no canto superior direito e selecione a opção **Notificações via e-mail**.

**02.** Escolha o *template* que deseja testar o envio.

**03.** Selecione o idioma do *template* de e-mail.

**04.** Clique em **Enviar E-mail**.

**05.** Informe o endereço de e-mail para o qual a mensagem de teste deve ser enviada.

**06.** Acione **Enviar**.

#f2f2f2#f2f2f2

Com isso, é enviada uma mensagem de e-mail de teste com o conteúdo do *template* no idioma selecionado para o endereço informado.

## Reverter as alterações do *template*

---

***100%true5%***

**01.** Acione o ícone **Configurações**  no canto superior direito e selecione a opção **Notificações via e-mail**.

**02.** Escolha o *template* que deseja redefinir.

**03.** Selecione o idioma do *template* de e-mail.

**04.** Clique **Redefinir *template***.

#f2f2f2#f2f2f2

Com isso, o conteúdo e o assunto do *template* selecionado são revertidos para o texto original e todas as alterações são descartadas.

É necessário repetir os passos acima para todos os *templates* e idiomas desejados.

## Desabilitar o envio de e-mail desabilitarenvio

---

***100%true5%***

**01.** Acione o ícone **Configurações**  no canto superior direito e selecione a opção **Notificações via e-mail**.

**02.** Escolha o *template* que deseja redefinir.

**03.** Selecione o idioma do *template* de e-mail.

**04.** Clique em **Editar *Template***.

**05.** Apague todo o conteúdo (caracteres e espaços) do campo **Assunto** e do campo**Conteúdo**.

**06.** Clique em **Salvar** para desabilitar o envio.

#f2f2f2#f2f2f2

Ao remover o assunto e o conteúdo de um *template*, os e-mails relacionados a esse *template* não são mais enviados aos usuários.

É necessário repetir os passos acima para todos os *templates* e idiomas desejados.

]]>
