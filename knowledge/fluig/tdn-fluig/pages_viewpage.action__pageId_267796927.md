---
content_hash: 0ac7eee6f4fc336267cfd7d039562c5a7ae9902c73efc40b859dd717b2d8be4d
fetched_at: '2026-06-28T21:35:23.910532+00:00'
page_id: '267796927'
product: fluig
source: tdn-fluig
title: LMS 030 - Quanto tempo leva para que uma requisição de matrícula seja efetivada?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267796927
version: 11
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

***Card*:** LMS

**Versão:** inferiores à 1.6.3 – *Snowflake*

# Ocorrência

Ao matricular um usuário ou grupo de usuários em determinada turma está demorando para que a turma seja exibida na aba Meu aprendizado. Qual é o tempo padrão para que uma requisição de matrícula seja efetivada?

# Solução

Ao solicitar matrícula em uma turma é iniciada uma rotina em segundo plano para realizar o cadastro dos usuários ou grupo de usuários informado. O tempo máximo de execução é de 2 minutos. O usuário recebe uma notificação quando a matrícula é efetivada.

Saiba mais...

As requisições de matrículas são efetivadas por uma tarefa padrão existente no Agendador de tarefas que é executada a cada 2 minutos. Para que a efetivação ocorra antes desse tempo, o administrador da plataforma precisa acessar o agendador e executar a tarefa manualmente. Assim, a turma será exibida no plano de aprendizado dos usuários matriculados assim que a tarefa for executada.

Confira mais informações em .

Importante!

A partir da atualização **[1.6.5-190219](http://tdn.totvs.com/pages/viewpage.action?pageId=442961412#Atualiza%C3%A7%C3%B5es(1.6.5)-190219)**, o **LMS** não faz mais parte da plataforma para **novas instalações**.

Mas, não se preocupe: se você adquiriu a plataforma com o **LMS incluso**, entre em contato com o [Suporte Fluig](https://suporte.fluig.com/) para que você consiga utiliza-lo normalmente – mesmo após a atualização **1.6.5-190219**. Se você não lembra se o LMS está incluso ou não no seu pacote, consulte sua proposta comercial ou entre em contato com o seu ESN.
