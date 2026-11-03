---
content_hash: 49aad2dfc48cc2d4686026e10601635e17d784f70d49e04cd14739f312b0d437
fetched_at: '2026-06-28T21:35:23.445171+00:00'
page_id: '254609816'
product: fluig
source: tdn-fluig
title: LMS 022 - É possível desativar o acesso à Agenda de aprendizado?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=254609816
version: 13
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

***Card*:** LMS

**Versão:** a partir da 1.6.2

# Ocorrência

É necessário desativar o recurso Agenda do item de Aprendizado para os usuários com papel *User.* É possível?

# Solução

Sim, é possível ocultar o recurso Agenda para os usuários comuns definindo algumas opções de permissão.

0.5falsesamplesfade1Passo 1

* Faça o *login* com um usuário administrador e acesse **Painel de Controle** → agrupador **Pessoas** **→** **Permissões**.

2Passo 2

* No recurso **Permissões**, escolha a opção **Recurso** e depois acione **Próxima etapa**.

3Passo 3

* Efetue uma busca por "Agenda".
* Selecione os recursos **WIDGET Agenda** e **PAGE Agenda - pageschedule**.
* Depois de selecionar os recursos, acione **Próxima etapa**.

4Passo 4

* Para cada recurso, acione a aba **Papel** e desative as permissões **Visualizar *widget*** e **Visualizar página**, respectivamente, para o papel **user**.
* Acione **Aplicar permissões**.

Assim, o recurso Agenda não será mais exibido no menu para os usuários comuns.

Saiba mais...

Confira as opções de permissão dos demais recursos de aprendizado em .

Importante!

A partir da atualização **[1.6.5-190219](http://tdn.totvs.com/pages/viewpage.action?pageId=442961412#Atualiza%C3%A7%C3%B5es(1.6.5)-190219)**, o **LMS** não faz mais parte da plataforma para **novas instalações**.

Mas, não se preocupe: se você adquiriu a plataforma com o **LMS incluso**, entre em contato com o [Suporte Fluig](https://suporte.fluig.com/) para que você consiga utiliza-lo normalmente – mesmo após a atualização **1.6.5-190219**. Se você não lembra se o LMS está incluso ou não no seu pacote, consulte sua proposta comercial ou entre em contato com o seu ESN.
