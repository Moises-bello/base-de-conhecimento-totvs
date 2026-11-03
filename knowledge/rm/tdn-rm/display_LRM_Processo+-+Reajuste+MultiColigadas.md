---
content_hash: 0d42f536b1752436d424fed13cf8b25ec8c2424fd7d8d6999fe6e9afd276527a
fetched_at: '2026-06-29T00:09:47.802196+00:00'
page_id: '435105073'
product: rm
source: tdn-rm
title: Processo - Reajuste MultiColigadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Processo+-+Reajuste+MultiColigadas
version: 76
---

**Processo - Reajuste MultiColigadas**   
 Através do processo Reajuste MultiColigadas, será possível executar o reajuste de diversas Tabelas de Preços simultaneamente, sendo elas de uma mesma coligada ou de coligadas distintas.  O processo permite que sejam filtradas as tabelas de acordo com o seu tipo e o reajuste pode ser executado por percentual  ou Moeda. Para mais detalhes sobre a execução e como o reajuste é feito, verifique a especificação técnica.  
 **Pré-Condições:**  
 **1-** Ter incluído uma tabela de preços com a situação "Efetivada" **2-** Ter permissão para reajustar e efetivar Tabelas de preços. **3-** Ter incluído para o período que será informado no reajuste as cotações da Moeda que será utilizada em caso de reajuste por Moeda  
 **Executando o processo:**  
 **1-** Acesse: TOTVS Incorporação/ Cadastros/Tabela de Preços **2-** Acesse: Processos/ Reajuste MultiColigadas **3-** Selecione a(s) coligada(s) que serão usadas no processo e clique no botão Avançar  
 **4 -**Será exibida a tela de reajuste MultiColigadas com os seguintes campos:

* **Tipo de geração de preço:** Permite selecionar qual o tipo de reajuste será utilizada. Possui as seguintes opções:

  + **Reajuste por Moeda:** Se for selecionado o Reajuste por Moeda os campos abaixo serão habilitados:
    - **Moeda:**Moeda  com Cotação cadastrada dentro do perído informado para cálculo de reajuste
    - **Data inicial:** Data inicial de corte para a cotação da moeda
    - **Data Final:** Data final de corte para a cotação da moeda
    - **Tipo de Cotação:** Índice Mensal ou Variação Acumulada
* **Efetivar tabela de preço automaticamente:** Ao marcar essa opção, após a execução do reajuste, a tabela que será criada pelo processo será efetivada automaticamente;
* **Data Inicio de vigência:** Determina a data de Inicio da vigência da tabela de preço que será criada pelo processo de reajuste;
* **Data Final de vigência:**  Determina a data de Inicio da vigência da tabela de preço que será criada pelo processo de reajuste;
* **Limpar Comissão:**  Permite limpar os valores e forma de cálculo de comissão que estiverem nas subunidades que serão selecionadas;
* **Código da Fórmula Comissão:** Permite informar uma fórmula para o cálculo da comissão, tendo a possibilidade de obter o valor de uma forma mais flexível. Ao inserir uma fórmula, o campo % Comissão é bloqueado, pois é necessário somente um forma de cálculo da comissão
* **% Comissão**: Permite informar um percentual para o cálculo da comissão. Esse valor será multiplicado pelo valor do imóvel na tabela de preço. Ao informar um percentual, o campo Código da Fórmula Comissão é bloqueado, pois é necessário somente um forma de cálculo da comissão
