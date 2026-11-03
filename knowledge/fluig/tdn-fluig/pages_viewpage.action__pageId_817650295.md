---
content_hash: d268eedd85186efe15612e16ab7ad579ed5c391bbb181a3fb2929616791fd2ec
fetched_at: '2026-06-28T21:35:30.189726+00:00'
page_id: '817650295'
product: fluig
source: tdn-fluig
title: Identity | Como forçar sincronização entre o Active Directory e o Identity?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=817650295
version: 8
---

**Dúvida**

Como forçar uma sincronização entre o *Active Directory* (*AD*) e o *Identity*?

**Solução**

As sincronizações entre o *Active Directory* (*AD*) e o *Identity* via *SmartSync* só ocorrem quando há alguma alteração no cadastro do usuário. Assim, para **forçar uma sincronização**, é necessário:

**01.** Acesse o *Identity* com um usuário administrador, acione a aba **Usuários** e pesquise pelo e-mail do(s) usuário(s) que se deseja alterar:

**02.** Exclua o(s) usuário(s) com problema cadastrado(s) no Identity:

**03.** Abra o cadastro do(s) usuário(s) no **Active Directory local**;

**04**. Adicione uma letra a mais no nome do(s) usuário(s);

**05.** Clique em **"Salvar"**;

**06.** Volte no cadastro do(s) usuário(s) e exclua essa letra a mais;

**07.** Clique em **"Salvar"** novamente;

**08.** No **Identity**, acesse a lista de usuários **rejeitados/pendentes** e aceite o usuário novamente.

Com essa ação, atualizará o status do(s) usuário(s) no cadastro do Identity e ele(s) poderá(ão) logar novamente.

A alteração deve ser realizada sempre no **nome** **(*name/firstName*)** do(s) usuário(s) e nunca no nome para exibição (*displayName*). Saiba mais em:



​​

Caso, por algum motivo, o(s) usuário(s) continue(m) apresentando a mesma situação, nos envie a pasta de logs do*SmartSync*disponível no caminho:

* *C:\ProgramData\SmartSync\logs*

**Observação:** A pasta *ProgramData* é uma pasta restrita, então, é necessário habilitar a opção de exibição de pastas omitidas na configuração da pasta C.
