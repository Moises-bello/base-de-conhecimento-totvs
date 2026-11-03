---
content_hash: 1571ebf28643195694faef86f6a85fe2f4019b079a05fda1837936a6074e933f
fetched_at: '2026-06-29T00:11:15.713847+00:00'
page_id: '662413804'
product: rm
source: tdn-rm
title: Mão de Obra (F6)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=662413804
version: 6
---

Nos parâmetros de Mobilidade no grupo "Tratamento para sincronismo de equipe em apontamentos" existem dois parâmetros:

* **Tipo de envio de equipe para apontamentos:** Define como será a seleção de equipe e membros de equipe que serão enviados para o coletor;
* **Desconsiderar situação do funcionário/terceiro ao enviar para o coletor:** Define a restrição de situação de funcionários/terceiros que serão enviados para o coletor. Se estiver marcado, não haverá restrição, caso contrário, as situações de pessoas com Aposentadoria por Invalidez(I), Demitido(D),  com Demissão no mês(X) e Contrato de Trabalho Suspenso(C) serão retiradas da lista de envio. Esse parâmetro influencia nas seguintes funcionalidades:
  + Cadastro de Equipe e Membros de Equipe;
  + Cadastro de Folha Tarefa de Produtividade;
  + Alocação de Mão de Obra na Folha Tarefa;
  + Sincronismo de Equipes e Membros para o Coletor.
* **Controlar capacidade da equipe na alocação de mão de obra:** Este parâmetro controla a capacidade de alocação da equipe considerando o período para a capacidade do insumo, exibindo no anexo da equipe de mobilidade o insumo , o total alocado para o insumo , qual a sua capacidade total e saldo.
* **Campos Complementares a serem exibidos no App Minha Obra:**

  Permite parametrizar os Campos Complementares dos apontamentos de Mão de obra (máximo de 5 campos), cujo preenchimento será realizado no App Minha Obra e visualizado nos apontamentos de mão de obra.

  Este parâmetro somente estará habilitado se existirem campos complementares de Apontamentos de Mão de Obra cadastrados em "Cad. Gerais | Campos Complementares | Apontamentos de Mão de Obra". Saiba mais em [Campos Complementares - TOP](https://tdn.totvs.com/display/LRM/Campos+Complementares+-+TCOP)

  Após realizado o cadastro dos campos complementares, basta informá-los nesse parâmetro, e ficarão disponíveis na tela de apontamento de mão de obra no App Minha Obra para preenchimento e no sistema na edição do apontamento de Mão de obra.

  A ordem dos campos complementares definirá a ordem de exibição no App, ou seja, o Campo Complementar 1 será o primeiro a ser exibido na tela do apontamento de Mão de obra do App Minha Obra, o Campo Complementar 2 será o segundo a ser exibido e assim, sucessivamente.

  Cada parâmetro pode ser preenchido com um campo complementar e, na tela de preenchimento dos apontamentos de Mão de obra do App Minha Obra, serão exibidos somente os 5 campos complementares informados nos parâmetros abaixo, conforme parametrizado em cada projeto, ou seja, podem ser parametrizados campos complementares diferentes em cada projeto.

  A limitação da exibição dos nomes dos campos no App Minha Obra é limitada a 30 caracteres.
