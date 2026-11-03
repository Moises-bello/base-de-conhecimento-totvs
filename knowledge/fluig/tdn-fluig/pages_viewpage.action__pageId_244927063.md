---
content_hash: 05bf2171b0a2d3c2d7eb2d089103e5e6c5b810bee5c8bba5e0cbe3c9171b190e
fetched_at: '2026-06-28T21:35:23.384796+00:00'
page_id: '244927063'
product: fluig
source: tdn-fluig
title: LMS 021 - Como permitir que alunos cancelem suas matrículas em trilhas e treinamentos?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244927063
version: 23
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

***Card*:** LMS

**Ambiente:** Windows / Linux

# Ocorrência

É necessário permitir que os alunos / usuários comuns possam cancelar suas matrículas em trilhas e treinamentos a partir da opção **Cancelar matrícula** exibida no menu **Meu Aprendizado** → **Início**.

# Causa

Por padrão, apenas usuários que pertencem ao papel admin da plataforma possuem permissão para cancelar matrículas.

# Solução

Incluir os grupos/papéis/usuários que devem receber a permissão de cancelamento de matrícula no recurso  do Painel de Controle da plataforma.

falsecancelarPasso 1

* Acesse o **Painel de Controle** → agrupador **Pessoas** → **Permissões**.

Dica!

Para versões anteriores à 1.6.5, acesse **Painel de Controle** **→ Gerais** **→ Permissões**.

Passo 2

* Selecione a opção **Recursos do sistema** e clique em **Próxima etapa**.

Passo 3

* Na coluna da esquerda, pesquise pelo termo "Matrículas" e selecione o recurso **Aprendizado - Matrículas**.

Observação

Este recurso abrange as seguintes permissões:

* Matricular todos usuários
* **Cancelar matrículas em treinamentos/trilhas**
* Cancelar matrículas em turmas
* Cancelar matrículas
Passo 4

* O recurso selecionado será exibido na coluna da direita. Clique em **Próxima etapa**.

Passo 5

* Nesta página são apresentadas as permissões configuradas para o recurso **Aprendizado - Matrículas**.

* Selecione a aba **Por Papel** e verifique que, por padrão, apenas o papel **admin** está cadastrado no recurso e possui as permissões de cancelamento habilitadas.

Passo 6  

* Para incluir novos grupos/papéis/usuários às permissões, acesse a aba desejada e acione o botão **Adicionar**.

* Utilize os botões **ON/OFF** para definir quais ações poderão ser tomadas pelos grupos/papéis/usuários cadastrados.

Dica

Para liberar as permissões para todos os usuários da plataforma, adicione o papel **user**.

* Após definir as permissões desejadas, acione o botão **Aplicar permissões**.

Saiba mais...

Para mais informações acesse ,  e .

Importante!

A partir da atualização **[1.6.5-190219](http://tdn.totvs.com/pages/viewpage.action?pageId=442961412#Atualiza%C3%A7%C3%B5es(1.6.5)-190219)**, o **LMS** não faz mais parte da plataforma para **novas instalações**.

Mas, não se preocupe: se você adquiriu a plataforma com o **LMS incluso**, entre em contato com o [Suporte Fluig](https://suporte.fluig.com/) para que você consiga utiliza-lo normalmente – mesmo após a atualização **1.6.5-190219**. Se você não lembra se o LMS está incluso ou não no seu pacote, consulte sua proposta comercial ou entre em contato com o seu ESN.
