---
content_hash: fcd335bddd8eef90ac5495412c373e03f71c5da7508fbb113c6875124d935bb7
fetched_at: '2026-06-28T21:35:26.676902+00:00'
page_id: '391552192'
product: fluig
source: tdn-fluig
title: Identity | Mensagem "Error converting XML. Attempt to write a read-only database
  attempt to write a readonly database." ao executar o Smartsync
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=391552192
version: 5
---

---

**Ocorrência**

Ao executar o SmartSync é apresentada a seguinte mensagem de erro:

**Causa**

O usuário do sistema operacional utilizado para executar o SmartSync não possui permissão de escrita na pasta de instalação do SmartSync da aplicação, "C:\ProgramData\SmartSync" (esta pasta é oculta).

**Solução**

Acessar o sistema operacional e executar o SmartSync com um usuário que possua permissão de escrita no diretório de instalação ("C:\ProgramData\SmartSync").

**Observações**

Para identificar qual usuário do sistema está executando o SmartSync, basta abrir o menu **Serviços** do Windows, localizar o serviço **SmartSync** na listagem, clicar com o botão direito e selecionar **Propriedades**. Na aba Logon será exibido o usuário que executa o SmartSync. Este usuário deve possuir permissão de escrita no diretório "C:\ProgramData\SmartSync".
