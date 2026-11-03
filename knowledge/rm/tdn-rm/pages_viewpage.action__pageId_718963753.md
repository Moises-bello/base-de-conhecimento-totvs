---
content_hash: fb2e62223b2b39916211d3f2ec5735aaf2fafaa98a24f59b207555d8ff4e2b36
fetched_at: '2026-06-29T00:11:26.639661+00:00'
page_id: '718963753'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Aluguel - Contrato de Locação - Aplicar
  Reajuste em CTO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=718963753
version: 14
---

Atenção: Devido a modificação dos parâmetros de aluguel complementar que passam a compor as faixas, toda a alteração realizada via Reajuste de CTO será diretamente na faixa de faturamento.

Os processos de Aplicar/Desfazer Reajuste agora contemplam também os valores de CTO Fixo e CTO Mínimo.

* O valor do CTO Mínimo é apresentado no contrato de locação e também no anexo Reajustes Vigentes.
* Os valores do CTO Fixo são apresentados nas faixas de faturamento de acordo com as datas de início e fim.

A memória de cálculo de ambos os reajustes irão aparecer em ***Anexo / Histórico de Reajustes.***  
  
  
  
O processo de Reajuste do CTO irá incluir uma nova faixa de faturamento com os valores reajustados e iniciando sempre na data do reajuste, como mostra a imagem abaixo:  
No exemplo, o reajuste ocorreu em 01/04/2022.

Caso existam faixas de faturamento subsequentes, todas terão seus valores atualizados, refletindo o reajuste a partir desta data.

Observação:

* Importante:
  + Existe uma consistência no sistema que respeita a ordem cronológica dos reajustes com os aditivos. Ou seja, não é possível reajustar um contrato com data anterior à data de aditivo (prevalecendo sempre a data do aditivo incluído).
  + Como o campo **valor período** é afetado pelo **reajuste do CTO**, o sistema irá se basear no **histórico de reajuste** para realizar os cálculos do valor mínimo em determinado período. Dessa forma, caso sejam gerados lançamentos retroativos a uma data de reajuste, estes lançamentos irão valer-se do valor período mínimo que era vigente nesta data.
  + Independente do valor reajustado o campo "Desconto do CTO" não sofrerá modificações, fazendo parte da nova faixa caso o mesmo exista no período do reajuste.
  + Independente do valor mínimo cadastrado ou não, o reajuste do aluguel irá sempre reajustar a faixa do CTO caso exista.
  + Caso a Faixa de Faturamento tenha a opção "desconsiderar reajuste" qualquer reajuste que seja efetuado na mesma data da faixa não será considerado.

## **Reajuste de CTO com Cálculo Pro-Rata**

Quando um contrato de locação sofre um reajuste em uma data que não seja o primeiro dia do mês, o valor da parcela deve ser dividido proporcionalmente:

* **Período A:** Dias antes do reajuste (valor antigo).
* **Período B:** Dias a partir do reajuste (valor novo).

Se os parâmetros do sistema não estiverem alinhados, o sistema poderá ignorar essa divisão e cobrar o valor cheio (reajustado) pelo mês inteiro, gerando valores incorretos.

## Exemplo Prático (Cenário de Janeiro)

Para facilitar o entendimento, veja como o sistema calcula o valor proporcional em um mês de 31 dias, com reajuste aplicado a partir do dia 20:

| **Período** | **Dias** | **Valor de Referência** | **Cálculo Proporcional** | **Subtotal** |
| --- | --- | --- | --- | --- |
| **01 a 19/01** | 19 | R$ 25.444,76 (Antigo) | (25.444,76 / 31) x 19 | R$ 15.595,20 |
| **20 a 31/01** | 12 | R$ 29.745,83 (Novo) | (29.745,83 / 31) x 12 | R$ 11.514,51 |
| **Total Mensal** | **31** | - | **Soma dos Períodos** | R$ 27.109,71 |

Observação:

* O valor final depende da consistência dos parâmetros abaixo para que o divisor (31 dias do mês civil ou 30 dias do mês comercial) seja o mesmo em todas as etapas do cálculo.

## **Regra de Consistência de Parâmetros**

Para que o cálculo exemplificado acima funcione, é fundamental que as configurações nos **Dados do Reajuste do Contrato** e nos **Parâmetros Gestão de imóveis** estejam corretamente parametrizados.

### Onde Configurar?

#### A. No Cadastro do Contrato (Dados do Reajuste)

Os campos abaixo devem possuir a **mesma definição**:

* **Rateio de índice:** Definir como "Mês Civil" ou "Mês Comercial".
* **Aplicação de índice:** Deve ser igual ao campo acima.

#### B. Nos Parâmetros Gestão de imóveis \ Aluguel \ Contrato de Locação

As marcações devem seguir a escolha feita no contrato:

| **Se no Contrato você escolheu** | **Nos Parâmetros Gerais você deve...** |
| --- | --- |
| **Mês Civil** | **MARCAR** as opções:  1. "Considera Mês Civil para cálculo do rateio"  2. "Considera Mês Civil para aplicação de valores rateados" |
| **Mês Comercial** | **DESMARCAR** as opções:  1. "Considera Mês Civil para cálculo do rateio"  2. "Considera Mês Civil para aplicação de valores rateados" |

falseChecklist de Solução de Problemas

Se o valor gerado estiver "bem acima" do esperado (como o caso do Fundo de Promoção citado no log):

1. Verifique se o reajuste não está sendo aplicado retroativamente ao mês inteiro.
2. Confirme se não há divergência entre "Mês Civil" e "Mês Comercial" nos parâmetros citados no item 3.
3. **Importante:** A inconsistência entre esses parâmetros faz com que o sistema se perca no cálculo do divisor diário, podendo gerar valores distorcidos no log de cálculo.
