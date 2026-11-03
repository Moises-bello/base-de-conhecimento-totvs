---
content_hash: 3471fb5713e3e467121d6847a44920fca9e7a61c9ef8cb2912d7363d778e1d7f
fetched_at: '2026-06-29T00:09:52.230824+00:00'
page_id: '438282654'
product: rm
source: tdn-rm
title: FISCAL01-6649 - DT - Inclusão de Contexto para Cálculo dos valores de Estoque
  - Registro 1050
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=438282654
version: 6
---

# CAT/SP 42/18

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Rotinas Estaduais |
| **Situação/Requisito:** | Criar um contexto de inventário para cálculo do saldo do ICMS no início do período e no final do período. Este contexto será utilizado na geração do Registro 1050 da CAT42 |
| **Solução/Implementação:** | Foi criado o contexto para o cálculo do saldo do ICMS ST no início do período e no final do período onde o cálculo será realizado com base nas últimas entradas do produto (Lançamentos Fiscais de Entrada).  Para geração desta rotina é necessário que o item possua as seguintes informações:  Em "Dados Fiscais do Produto":    Em "Dados Fiscais por UF":    Obs: O cadastro dos dados fiscais por UF deverá ser efetuado para UF da Filial que está gerando a rotina.  Nos lançamentos de entrada serão selecionados os itens suficientes para acobertar a quantidade em estoque considerando somente a quantidade dos itens que não tenham sido referenciados aos itens de saída até aquela data. Quando necessário será realizada uma média ponderada para chegar no valor do "imposto em estoque".  O valor será a soma do ICMS e ICMSST que incidiu na compra dos itens selecionados.  **Exemplo:**  Considerando o período de 01/11/2018 à 30/11/2018 teremos:  **Quantidade inicial:** Será considerado a posição do estoque referente ao fechamento do período anterior, neste caso 31/10/2018.  **Quantidade final:** Será considerado a posição do estoque referente ao fechamento do período atual, neste caso 30/11/2018.  As saídas consideram as entradas mais recentes para referencia do valor suportado sendo que um item que já foi referenciado na saída não pode ser referenciado novamente. Assim, vamos considerar que para cada entrada exista um saldo disponível para ser referenciado ou seja a quantidade que ainda não foi utilizada em um lançamento de saída. Neste caso nossas entradas estão da seguinte forma:   | Data entrada | Qtd na entrada | Qtd já referenciada em saídas | Saldo disponível da entrada | Imposto suportado unitário | | --- | --- | --- | --- | --- | | 01/01/2018 | 20 | 15 = (10 - 01/02 ) + (5 - 01/10) | 5 | 20,90 | | 01/03/2018 | 15 | 15 = ( 15 - 01/10) | 0 | 22,80 | | 15/10/2018 | 10 | 0 | 10 | 23,75 | | 16/11/2018 | 5 | 0 | 5 | 24,70 |   **Valor total do ICMS suportado inicial (31/10/2018):** (10 \* 23,75) + (5 \* 20,90) = 342,00  **Valor total do ICMS suportado final (30/11/2018):** (5 \* 24,70) + (10 \* 23,75) + (5 \* 20,90) = 465,50 ATENÇÃO Este processo não deve ser confundido com o controle de estoque do modulo de Gestão de Estoque, Compras e Faturamento. O estoque será sempre definido pelos controles do modulo de estoque. Os lançamentos fiscais e suas referencias são consideramos somente para cálculo do valor do imposto suporte que existe no estoque. |
