---
content_hash: 430dbaab56aa158d32becf27333356ed6825b57ce42a001d3db738d5c3cb5113
fetched_at: '2026-06-29T00:12:00.744457+00:00'
page_id: '887742090'
product: rm
source: tdn-rm
title: Parâmetros Mão de Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=887742090
version: 2
---

Nessa tela são citados todos os parâmetros que tem relação ao apontament de mão de obra ou algum processo que tenha vinculo com o mesmo tema.

Para mais detalhes de parâmetros que envolve Mobilidade acesse:  e  e

* O parâmetro “ Tarefa para rateio de horas improdutivas” é utilizado nos processos de rateio e revaloração de apontamentos de equipamentos e mão de obra. Caso esteja habilitado, as horas improdutivas apontadas serão apropriadas de acordo com a tarefa e motivo de improdutividade informados;

* A inclusão de apropriação que representa a improdutividade, somente acontecerá se o parâmetro de "Motivo de Improdutividade Mão de Obra" estiver definido;
* Para maiores detalhes sobre o parâmetro “Enviar e-mail de log de erros” vide Parametrização Geral; Para mais detalhes de parâmetros que envolve Mobilidade acesse:  e  e

* O parâmetro para definição de “Eventos/ Verbas” é utilizado no processo de rateio e revaloração de mão de obra para buscar o custo. Quando informado o sistema busca somente os custos dos eventos/verbas informados para o funcionário. Caso contrário, o sistema busca o custo total. Aplicável somente quando integrado com Folha de Pagamento do PROTHEUS;

* Para que seja permitido o cadastro de funcionários como membros de equipe o projeto deve estar integrado com o TOTVS Folha de Pagamento.
* O parâmetro "Considerar funcionário/terceiro de:" serve para filtrar os funcionários/terceiros.

Nos parâmetros de Mobilidade no grupo "Tratamento para sincronismo de equipe em apontamentos" existem dois parâmetros:

* **Tipo de envio de equipe para apontamentos:** Define como será a seleção de equipe e membros de equipe que serão enviados para o coletor;
* **Desconsiderar situação do funcionário/terceiro ao enviar para o coletor:** Define a restrição de situação de funcionários/terceiros que serão enviados para o coletor. Se estiver marcado, não haverá restrição, caso contrário, as situações de pessoas com Aposentadoria por Invalidez(I), Demitido(D),  com Demissão no mês(X) e Contrato de Trabalho Suspenso(C) serão retiradas da lista de envio. Esse parâmetro influencia nas seguintes funcionalidades:
  + Cadastro de Equipe e Membros de Equipe;
  + Cadastro de Folha Tarefa de Produtividade;
  + Alocação de Mão de Obra na Folha Tarefa;
  + Sincronismo de Membros para o Coletor;
  + Sincronismo de Equipes para o Coletor (se o parâmetro **não estiver marcado,** não serão sincronizadas as equipes cujos responsáveis estejam nas situações de pessoas com Aposentadoria por Invalidez(I), Demitido(D), Demissão no mês(X) e Contrato de Trabalho Suspenso(C)).

* **Controlar capacidade da equipe na alocação de mão de obra:**Este parâmetro controla a capacidade de alocação da equipe considerando o período para a capacidade do insumo, exibindo no anexo da equipe de mobilidade o insumo , o total alocado para o insumo , qual a sua capacidade total e saldo.
* **Campos Complementares a serem exibidos no App Minha Obra:**

  Permite parametrizar os Campos Complementares dos apontamentos de Mão de obra (máximo de 5 campos), cujo preenchimento será realizado no App Minha Obra e visualizado nos apontamentos de mão de obra.

  Este parâmetro somente estará habilitado se existirem campos complementares de Apontamentos de Mão de Obra cadastrados em "Cad. Gerais | Campos Complementares | Apontamentos de Mão de Obra". Saiba mais em [Campos Complementares - TOP](https://tdn.totvs.com/display/LRM/Campos+Complementares+-+TOP)

  Após realizado o cadastro dos campos complementares, basta informá-los nesse parâmetro, e ficarão disponíveis na tela de apontamento de mão de obra no App Minha Obra para preenchimento e no sistema na edição do apontamento de Mão de obra.

  A ordem dos campos complementares definirá a ordem de exibição no App, ou seja, o Campo Complementar 1 será o primeiro a ser exibido na tela do apontamento de Mão de obra do App Minha Obra, o Campo Complementar 2 será o segundo a ser exibido e assim, sucessivamente.

  Cada parâmetro pode ser preenchido com um campo complementar e, na tela de preenchimento dos apontamentos de Mão de obra do App Minha Obra, serão exibidos somente os 5 campos complementares informados nos parâmetros abaixo, conforme parametrizado em cada projeto, ou seja, podem ser parametrizados campos complementares diferentes em cada projeto.

  A limitação da exibição dos nomes dos campos no App Minha Obra é limitada a 30 caracteres.

* Para apontamentos retroativos há um parâmetro que determina o número máximo de dias que um usuário pode retroceder. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=421385196)

* O parâmetro do “Configuração de WebService para Folha de Pagamento de Ponto Protheus” é utilizado para buscar informações de folha de pagamento e folha de ponto no Protheus.

Detalhamento do Processo : [Rateio e Revaloração](https://tdn.totvs.com/pages/editpage.action?pageId=421385566)
