---
content_hash: 8122b29a99c86399bd075d47e12127710ab8db1b000489690ca3d7d19850e992
fetched_at: '2026-06-28T21:35:23.372945+00:00'
page_id: '244925032'
product: fluig
source: tdn-fluig
title: LMS 036 - É possível configurar quantidade de tentativas no pós-teste de trilhas
  e treinamentos?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244925032
version: 10
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

***Card*:** LMS

# Ocorrência

Existe a possibilidade de configurar a quantidade de tentativas que o aluno pode realizar o pós-teste de um treinamento, assim como é feito nos itens de tópico, quando se utiliza a estrutura de disciplinas e turmas?

# Solução

Atualmente não existe este recurso. Contudo, pode-se utilizar a estrutura de disciplinas e turmas para realizar esta configuração fazendo da seguinte forma:

Criar três tópicos sendo eles:

* Um tópico (1) + um item de tópico com avaliação (representando o pré-teste);

* Um tópico (2) + itens de tópicos com conteúdo (representando os conteúdos da trilha ou treinamento). Na configuração do tópico, no campo **Inicialização** selecionar a opção **Liberação após conclusão de pré-requisitos** e marcar como pré-requisito o tópico 1;

* Um tópico (3) + um item de tópico com avaliação (representando o pós-teste). Na configuração do tópico, no campo **Inicialização**, selecionar a opção **Liberação após conclusão de pré-requisitos** e marcar como pré-requisito os tópicos 1 e 2. E, na configuração do item de tópico, configurar o número de tentativas desejados.

Saiba mais...

Confira informações mais detalhadas em , ,  e nos itens de tópico dos tipos  e .

Importante!

A partir da atualização **[1.6.5-190219](http://tdn.totvs.com/pages/viewpage.action?pageId=442961412#Atualiza%C3%A7%C3%B5es(1.6.5)-190219)**, o **LMS** não faz mais parte da plataforma para **novas instalações**.

Mas, não se preocupe: se você adquiriu a plataforma com o **LMS incluso**, entre em contato com o [Suporte Fluig](https://suporte.fluig.com/) para que você consiga utiliza-lo normalmente – mesmo após a atualização **1.6.5-190219**. Se você não lembra se o LMS está incluso ou não no seu pacote, consulte sua proposta comercial ou entre em contato com o seu ESN.
