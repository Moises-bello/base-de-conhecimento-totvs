---
content_hash: 09f6cd4aeb13c1ffff16a1e9c6c1ab27b9626b9cad2a5689447a4ce87fc6da2a
fetched_at: '2026-06-29T00:09:47.828453+00:00'
page_id: '435105079'
product: rm
source: tdn-rm
title: Reajustar Tabela de Preço -  Processo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105079
version: 76
---

**Processo - Reajustar Tabela de Preço**

---

* **Tipo de Reajuste de Preço:** Permite selecionar qual a fórmula de cálculo do reajuste. Temos os seguintes tipos de cálculos:
  + **Reajuste por Percentual:** Quando é selecionada essa opção, o campo Percentual é exibido, permitindo informar o valor percentual do reajuste. Esse valor será multiplicado pelo valor do imóvel na tabela de preço.
  + **Reajuste Por Valor:** Quando é selecionada essa opção, o campo Valor fixo é exibido, permitindo informar o valor de reajuste. Esse valor será somado ao valor do imóvel na tabela de preço.
  + **Reajuste do Preço por Moeda:** Quando é selecionada essa opção são exibidas as seguintes campos:
    - **Moeda/Índice:** Permite informar uma Moeda ou Índice, no qual será utilizado a sua cotação como fórmula de cálculo para o reajuste;
    - **Tipo:** Permite informar qual tipo de Índice é a Moeda/Índice selecionada anteriormente. Possui as opções de "Índice acumulado" e "Índice mensal";
    - **Data Inicial:** Permite informar a Data Inicial da cotação da Moeda/Índice que foi selecionada para o cálculo do reajuste;
    - **Data Final:** Permite informar a Data Final da cotação da Moeda/Índice que foi selecionada para o cálculo do reajuste;
  + Reajuste por Planilha Excel
* **Início de Vigência:** Data de Início  de validade da tabela de preços criada pelo reajuste.
* **Final da Vigência:** Data de Vencimento da tabela de preços. será informado apenas para tabelas secundárias. Tabelas Padrão devem ser Revogadas;
* **Efetivar Automático:** Permite efetivar a tabela de preço criada pelo reajuste após a execução do processo;
* **Limpar Comissão:**  Permite limpar os valores e forma de cálculo de comissão que estiverem nas subunidades que serão selecionadas;
* **Código da Fórmula Comissão:** Permite informar uma fórmula para o cálculo da comissão, tendo a possibilidade de obter o valor de uma forma mais flexível. Ao inserir uma fórmula, o campo % Comissão é bloqueado, pois é necessário somente um forma de cálculo da comissão
* **% Comissão**: Permite informar um percentual para o cálculo da comissão. Esse valor será multiplicado pelo valor do imóvel na tabela de preço. Ao informar um percentual, o campo Código da Fórmula Comissão é bloqueado, pois é necessário somente um forma de cálculo da comissão
