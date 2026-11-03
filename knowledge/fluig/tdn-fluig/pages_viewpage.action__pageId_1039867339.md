---
content_hash: d49a4e69bc07c3a18a66c8ae9af62a6b11ff796e8f5aee3b70eccd970de0ea25
fetched_at: '2026-06-28T21:35:17.280727+00:00'
page_id: '1039867339'
product: fluig
source: tdn-fluig
title: ECM - Como desabilitar o uso do recurso Documento externo?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1039867339
version: 9
---

4true.\*ndicenone

# Plataforma

---

**Produto:**Fluig

**Versão:** a partir da 2.0.0

# Ocorrência

---

Existe a necessidade de desabilitar o uso do recurso  para algumas empresas.

# Causa

---

A partir da atualização **Voyager 2.0.0-260317**, é possível desabilitar o uso do recurso Documento externo na empresa se assim for desejado, para aumentar a segurança do ambiente e evitar a exploração de possíveis vulnerabilidades que um endereço externo à plataforma pode permitir.

# Solução

---

Para desabilitar o uso do recurso Documento externo, é necessário cadastrar a chave **show.external.document** com o valor **false** nos dados adicionais da empresa.

Para isso:

**01.** Acesse o Fluig com o usuário **wcmadmin**.

**02.** No menu lateral, clique em **Painel de controle**.

**03.** No agrupador **WCM**, clique em **Empresas**.

**04.** Selecione a empresa para a qual deseja desabilitar o uso do recurso Documento externo.

**05.** Clique em **Editar**.

**06.** Na aba **Geral**, clique em **Cadastrar dados adicionais**.

**07.** Em **Chave**, preencha com **show.external.document**.

**08.** Em **Valor**, preencha com **false**.

**09.** Clique em **Salvar** e, na edição da empresa, clique em **Salvar** novamente.

# Recomendação!

---

Se o uso do recurso Documento externo for realmente necessário e você optar por mantê-lo habilitado, recomendamos a implementação de validações no processo de *upload*/criação de documentos externos utilizando o evento *validateUpload*, conforme descrito na documentação oficial [Eventos de Documentos](https://tdn.totvs.com/display/fluig/Eventos+de+Documentos#EventosdeDocumentos-ValidateUpload) para aumentar a segurança do seu ambiente.
