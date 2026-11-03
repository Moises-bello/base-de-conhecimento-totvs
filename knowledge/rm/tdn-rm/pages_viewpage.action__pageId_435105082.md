---
content_hash: 81706834c15cada23f4b6687427dcac5f6486a4225b03efb1c9eb4f8985b5ee9
fetched_at: '2026-06-29T00:09:47.838244+00:00'
page_id: '435105082'
product: rm
source: tdn-rm
title: Nota Promissória
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105082
version: 2
---

As explicações dos itens A e B mostram as formas ideais para se gerar Notas Promissórias provenientes das vendas imobiliárias.

**A - Processo de configuração do Sistema Totvs Incorporação para numeração correta das parcelas quando a geração dos respectivos lançamentos do Totvs Gestão Financeira**  
 Abaixo seguem os passos necessários:

* Acessar as parametrizações do Totvs Incorporação;
* Selecionar o conjunto de parâmetros em Contrato/Plano de Financiamento;
* Na opção Parâmetros do Plano deve-se marcar as opções "Nota Promissória com c/ nº sequencial" e "Numerar por Ordem de Vencimento e Grupo", ir para a Última Etapa e clicar em Concluir;
* Configurar a Geração do Número da Parcela e onde o mesmo será gerado:  
  + Acessar as parametrizações do Totvs Incorporação;
  + Deve-se selecionar o conjunto de parâmetros em Integração Financeira e clicar em Avançar;
  + No primeiro item Integração Fin. Param. Gerais em seu parâmetro "Gera nº de parcela para o campo opcional?" deve ser selecionada a opção "Nota Promissória" e selecionar o "Campo Opcional Nº Parcela" no qual será gerada a numeração de parcelas no Totvs Gestão Financeira, ir para a Última Etapa e clicar em Concluir;

Estas configurações feitas, basta que na geração do Plano de Financiamento, na edição dos componentes geradores de parcela, seja feita a informação do campo "Código de Ligação entre Grupos".  Se desejar que vários componentes tenham suas parcelas sequenciadas e totalizadas em conjunto, basta informar o mesmo código para cada um dos componentes, estando no mesmo grupo ou não. Se desejar que componentes sejam sequenciados e totalizados separadamente, informe códigos diferentes, estando no mesmo grupo ou não.

**B - Processo de configuração do Sistema Totvs Incorporação para numeração de parcelas quando da geração dos respectivos lançamentos no Totvs Gestão Financeira por grupo sem utilizar Geração de Nota Promissória**  
 Configurar para NÃO gerar Número de Nota Promissória. Abaixo seguem os passos necessários:  
 Abaixo seguem os passos necessários:

* Acessar as parametrizações do Totvs Incorporação;
* Selecionar o conjunto de parâmetros em Contrato/Plano de Financiamento;
* Na opção Parâmetros do Plano deve-se marcar as opções "Nota Promissória com c/ nº sequencial" e "Numerar por Ordem de Vencimento e Grupo", ir para a Última Etapa e clicar em Concluir;
* Configurar a geração do Número da Parcela e onde o mesmo será gerado.
  + Acessar as parametrizações do Totvs Incorporação;
  + Deve-se selecionar o conjunto de parâmetros em Integração Financeira e clicar em Avançar;
  + No primeiro item Integração Fin. Param. Gerais em seu parâmetro "Gera nº de parcela para o campo opcional?" deve ser selecionada a opção "Sim" e selecionar o "Campo Opcional Nº Parcela" no qual será gerada a numeração de parcelas no Totvs Gestão Financeira, ir para a Última Etapa e clicar em Concluir.

Feitas estas configurações, basta gerar o plano de financiamento que os lançamentos no Totvs Gestão Financeira e serão gerados com a numeração por grupo. Importante ressaltar que esta regra funciona para Planos de Financiamento onde exista apenas um componente gerador por Grupo. Se existirem mais, é necessário seguir a parametrização de geração por Nota Promissória que exige que sejam configurados os componentes para que a geração ocorra corretamente.
