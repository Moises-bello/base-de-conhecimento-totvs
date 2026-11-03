---
content_hash: 590d7ec7fabde7ff921950485f26277d614ecd21120c2e5be2e439faaced1d07
fetched_at: '2026-06-29T00:10:09.924415+00:00'
page_id: '452719736'
product: rm
source: tdn-rm
title: Cancelar Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719736
version: 8
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Cancelar Rescisão**
   1. **Principais Campos e Parâmetros**
5. **Tabelas utilizada**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2310 e Superiores

## **02. VISÃO GERAL**

Havendo necessidade a rescisão calculada no mês e no próximo mês para um ou vários funcionários poderá ser cancelada pelo módulo Cancelar Rescisão.  
   
**Atenção:**  
Se não houver informação na Seleção de Funcionários serão canceladas todas as rescisões do mês do próximo mês. Para que somente as rescisões do mês atual sejam canceladas deve-se selecionar apenas os funcionários demitidos no mês, devendo ser feito o mesmo procedimento no caso de cancelamento das rescisões para o próximo mês.  
   
Será apresentada uma mensagem alertando que após o cancelamento da rescisão do funcionário, deverão ser verificados alguns itens como a Movimentação, a Situação, o Parcelamento Automático, o Cadastro de férias (caso o funcionário tenha gozo de férias no mês) e o Cadastro de Chefes/Supervisores (caso o funcionário seja chefe ou supervisor).   
   
Quando for solicitado o cancelamento de rescisão constante em um período bloqueado, será apresentada mensagem ao final do processo informando que não houve cancelamento devido ao bloqueio, bastando desbloquear o movimento pelo módulo de Bloqueia Recálculo em Folha Mensal para que o processo seja executado.  
   
O movimento poderá ser cancelado ou não de acordo com a necessidade caso o parâmetro "Cancela Movimentação da rescisão para demitidos do mês atual".  
Se este parâmetro for marcado a movimentação do mês do funcionário será cancelada, se for desmarcado o movimento não será cancelado, devendo ser cancelado, posteriormente pelo módulo de Cancelamento em Folha Mensal.  
   
Os códigos fixos cadastrados no anexo de Funcionários são decrementados de acordo com os lançamentos feitos e no momento do Cancelamento de Rescisão poderá ser incrementado novamente para que volte ao valor anterior à rescisão.  
Marcando o parâmetro "Incrementa Códigos Fixos" incrementará o número de vezes do Código Fixo do funcionário este código for diferente de 999.  
   
O movimento cancelado do funcionário poderá ser gravado através do parâmetro "Grava Movimento" e poderá ser importado através do módulo de Importação de Movimento em Folha Mensal.  
   
**Observação:**  
Na importação dos dados de rescisão o movimento será importado para o mês de competência atual, portanto quando o usuário cancelar a rescisão do mês seguinte, a movimentação não será importada para o mês seguinte.  
   
O arquivo com a movimentação gravada poderá ser substituído pelo arquivo gerado anteriormente ou adicionado dados cancelados ao final do arquivo existente de acordo com a necessidade/escolha.

## **03. EXEMPLO DE UTILIZAÇÃO**

**Dados Fictícios: Base exemplo**

**Funcionário 00004**

**Rescisão Calculada através do Cálculo da Rescisão Individual**

**Tipo 2 - Inic. Empregador sem justa causa**

**Acessar o módulo de Cancelamento de Rescisão:**

**Tela de parâmetross de Cancelamento de Rescisão Informados:**

## **04.****TELA Cancelar Rescisão**

**Principais Campos e Parâmetros**

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Cancela movimentação da rescisão para demitidos no mês atual | Se este parâmetro for marcado a movimentação do mês do funcionário será cancelada, se for desmarcado o movimento não será cancelado, devendo ser cancelado, posteriormente pelo módulo de Cancelamento em Folha Mensal. |
| Incrementa códigos fixos | Se este parâmetro for marcado, será  incrementado o número de vezes do Código Fixo do funcionário este código for diferente de 999. |
| Grava Movimento | Se for marcado, será gravado em arquivo, o movimento cancelado e poderá ser importado através do módulo de Importação de Movimento em Folha Mensal. |
| Caminho informado para o Arquivo | Informar o nome e o caminho do arquivo a ser gravado no cancelamento do movimento da rescisão. |
| Substituir arquivo | Informar se deseja substituir o arquivo. |
| Adicionar ao final do arquivo | Informar se deseja adicionar o movimento do cancelamento da rescisão ao final do arquivo. |
| Quebra de seção | Informar a quebra de seção. |
| Seleção de Funcionário | Filtrar os funcionários (Chapa, Situação, Tipo, Recebimento, Filtro e Fórmula Seleção) que deseja cancelar a rescisão. |

**Tela de Parâmetros de Cancelamento de Rescisão Informados:**

## **05.****TABELAS UTILIZADAS**

* PFUNC
* PFPERFF
* PFFINANC
* PDADOSRESCISAO
