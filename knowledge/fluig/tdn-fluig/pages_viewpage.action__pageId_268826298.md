---
content_hash: 1a27c2ea1d84335599f7add5edf9165e9cfd9b4584563b4ae2ca38b8a149b49b
fetched_at: '2026-06-28T21:35:24.059150+00:00'
page_id: '268826298'
product: fluig
source: tdn-fluig
title: LMS 025 - Por que não é possível excluir um treinamento?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268826298
version: 10
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

***Card*:** LMS

# Ocorrência

Ao tentar excluir um treinamento é exibida a mensagem "Não é possível remover o Treinamento, existem matrículas ativas ou finalizadas".

# Causa

O treinamento possui matrículas ou requisição de matrícula.

# Solução

Um treinamento só pode ser excluído se nenhuma requisição de matrícula foi realizada. Caso uma matrícula ou requisição de matrícula tenha sido realizada, o treinamento não pode ser excluído, pois fica salvo como histórico. Nem mesmo cancelando as matrículas o treinamento pode ser excluído, pois este procedimento também fica registrado em histórico.

O que pode ser feito?

Uma alternativa é ocultar o treinamento do catálogo. Para isso, é necessário que:

* nas , a opção **Permite visualizar treinamentos e trilhas arquivados** esteja configurada com a opção **Não**;
* o campo **Situação** do cadastro do  esteja configurado com a opção **Arquivado**.

Assim, os treinamentos arquivados não serão exibidos no catálogo.

Importante!

A partir da atualização **[1.6.5-190219](http://tdn.totvs.com/pages/viewpage.action?pageId=442961412#Atualiza%C3%A7%C3%B5es(1.6.5)-190219)**, o **LMS** não faz mais parte da plataforma para **novas instalações**.

Mas, não se preocupe: se você adquiriu a plataforma com o **LMS incluso**, entre em contato com o [Suporte Fluig](https://suporte.fluig.com/) para que você consiga utiliza-lo normalmente – mesmo após a atualização **1.6.5-190219**. Se você não lembra se o LMS está incluso ou não no seu pacote, consulte sua proposta comercial ou entre em contato com o seu ESN.
