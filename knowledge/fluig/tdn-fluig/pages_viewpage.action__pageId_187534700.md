---
content_hash: 265bb051bf0a51f1cbfa9a2fabd04e1b46d1975c6045cd744ba82ce6b7653b4c
fetched_at: '2026-06-28T21:35:19.016153+00:00'
page_id: '187534700'
product: fluig
source: tdn-fluig
title: LMS 001 - O que significa a inconsistência "Não foram encontrados arquivos
  anexos" ao publicar um conteúdo SCORM?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=187534700
version: 22
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma

***Card*:** LMS

# Ocorrência

É apresentada a mensagem de inconsistência "Não foram encontrados arquivos anexos" ao publicar um conteúdo do tipo SCORM.

# Causa

Essa mensagem é apresentada quando um arquivo anexado está declarado com o nome errado no arquivo *imsmanifest.xml*.

# Solução

É necessário corrigir o nome do arquivo no *imsmanifest.xml.*

Abaixo está o projeto do conteúdo SCORM, um dos arquivos é o *story.swf* que deve estar declarado no arquivo *imsmanifest.xml.*

Analisando o arquivo *imsmanifest.xml* vamos encontrar a estrutura abaixo. O erro será apresentado por que o nome do arquivo *history.swf* está diferente do arquivo original, o *story.swf* na imagem acima.

Importante!

A partir da atualização **[1.6.5-190219](http://tdn.totvs.com/pages/viewpage.action?pageId=442961412#Atualiza%C3%A7%C3%B5es(1.6.5)-190219)**, o **LMS** não faz mais parte da plataforma para **novas instalações**.

Mas, não se preocupe: se você adquiriu a plataforma com o **LMS incluso**, entre em contato com o [Suporte Fluig](https://suporte.fluig.com/) para que você consiga utiliza-lo normalmente – mesmo após a atualização **1.6.5-190219**. Se você não lembra se o LMS está incluso ou não no seu pacote, consulte sua proposta comercial ou entre em contato com o seu ESN.
