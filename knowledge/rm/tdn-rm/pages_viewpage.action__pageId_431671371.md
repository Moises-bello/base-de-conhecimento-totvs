---
content_hash: e5e62c6cfe4b535bd1fe0cb59fd0d1c9da608e33885aca0d1d57201f5196636e
fetched_at: '2026-06-29T00:09:39.462443+00:00'
page_id: '431671371'
product: rm
source: tdn-rm
title: Detalhamento do cálculo da Parcela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=431671371
version: 29
---

---

Consultando a parcela é possível avaliar quais os valores detalhados que á compõe, levando em consideração o cálculo por crédito das disciplinas, descontos de parcelas, descontos por antecipação, aproveitamento de conta corrente, detalhamento das bolsas condicionais e incondicionais entre outros.

Esta funcionalidade retorna de forma detalhada informações relacionadas aos valores que compõem o cálculo da parcela conforme as disciplinas matriculada, levando em consideração a parametrização que define como os crédito serão processados.

Permitindo ainda que sejam realizadas simulação do valor para pagamento, conforme uma data de previsão de baixa, que impacta quando o cliente trabalha com descontos por antecipação ou bolsa condicionadas ao vencimento ou processadas por fórmula.

Para que o usuário verifique a composição das parcelas é necessário seleciona-las e então clicar no botão "Detalhamento do cálculo" (canto inferior direito da tela).

Após a execução, será apresentada a tela com os seguinte itens:

* Parcelas selecionadas (com status: aberto, baixado, vencido, baixado por acordo ou parcialmente)
* Acesso o cadastro do lançamento financeiro
* Simulação das parcelas geradas e que estão em aberto informando a “Data de previsão de baixa”.
* Detalhes do cálculo das disciplinas, tais como n° crédito, valor do crédito, valor da disciplina no contrato e data de matricula, marcando a opção “Mostrar detalhes do cálculo das disciplinas”.
* Disciplinas (quando a parcela estiver parametrizada para calcular por crédito)
* Descontos (descontos por parcela e antecipação)
* Bolsa condicional, incondicional
* Outros (aproveitamento de valores da conta corrente)
* Resumo do cálculo

Procedimento para Utilização

O acesso a tela do detalhamento do cálculo foi disponibilizado na visão de parcelas através do botão “Detalhamento do cálculo”.

Ao selecionar as parcelas  e clicar no botão “Detalhamento do cálculo” será apresentada a tela demonstrando a composição dos valores da parcela.

No menu lateral esquerdo "Parcelas" será listadas todas as parcelas selecionadas anteriormente.

Será possível identificar através dos ícones destacado na parcela, qual o status do lançamento (aberto, baixado, vencido, baixado por acordo ou parcialmente) e ao passar o mouse sobre a parcela serão apresentadas as informações dos lançamentos vinculados, levando em consideração que podemos ter mais de um responsável financeiro ou lançamentos de bolsa de crédito.

Ao clicar sobre a parcela que possuir lançamento gerado, será apresentado abaixo uma lista com os lançamentos da parcela, possibilitando ao usuário acessar o cadastro do lançamento financeiro ao efetuar um double clique sobre o item listado.

Ao clicar sobre a parcela, será listado do lado direito o detalhamento de todo o cálculo.

As informações apresentadas serão divididas em grupos, sendo disciplinas (quando a parcela estiver parametrizada para calcular por crédito), descontos (descontos por parcela e antecipação), bolsa condicional, incondicional, outros (aproveitamento de valores da conta corrente, valor de devolução - bolsa retroativa) e o resumo do cálculo

Em função da parametrização, podemos ter algumas particularidades no cálculo dos valores por disciplinas que poderão ser apresentadas como abatimentos ou acréscimos, neste caso o sistema vai destacar o item com um ícone de exclamação, ao passar o mouse sobre o ícone será apresentado uma descrição informando a que particularidade está relacionado o item de cálculo.

É possível visualizar detalhes do cálculo das disciplinas, tais como n° crédito, valor do crédito, valor da disciplina no contrato e data de matricula, para isso marque a opção “Mostrar detalhes do cálculo das disciplinas”.

Para parcelas com lançamentos gerados e que estão em aberto, será possível realizar a simulação do valor para pagamento informando uma  “Data de previsão de baixa” e clicando no botão atualizar.

Ao posicionar o mouse sobre o nome da bolsa é possível consultar o percentual aplicado para a bolsa.

Quando o lançamento não foi gerado para a parcela, ao clicar sobre a parcela o sistema vai apresentar uma simulação dos valores.

Foi disponibilizado a opção “Copiar para Clipbord” que realiza um ctrl+c do detalhamento do cálculo apresentado, permitido ao usuário realizar um ctrl+v em qualquer editor de texto.

Veja o exemplo após executar o ctrl+v

Informações

* Não será gerado detalhamento do cálculo por disciplina, quando o valor da parcela for fixo.
* Para contratos legados que não exista o detalhamento do cálculo por crédito, o sistema não conseguirá montar um detalhamento que identifique quais parcelas a disciplina foi cobrada e qual o valor a ser devolvido por parcelas.
* Juntamente com esta tela disponibilizamos uma evolução no TOTVS Educacional, que passará a gravar o detalhamento do cálculos por crédito das disciplinas durante a geração do lançamento financeiro.  
  Para maiores informações consulte o documento: [Detalhamento do Cálculo da Parcela por Disciplina](https://tdn.totvs.com.br/pages/viewpage.action?pageId=560631134)

 Como Fazer

---

[Detalhamento do Cálculo da Parcela por Disciplina](https://tdn.totvs.com.br/pages/viewpage.action?pageId=560631134)[Detalhamento dos Valores da Parcela do Contrato via Webservice](http://tdn.totvs.com/x/o8gBGQ)
