---
article_id: 360019946851
category: Call Center - Telecobrança
content_hash: 490b3d213d8bb38435f7974d1576a9838526bca3e5e5355b125271e807292fc2
fetched_at: '2026-06-28T22:41:28.678977+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- Simulação de Valores
  - Botão Telecobrança
type: support-article
updated_at: '2022-06-22T17:22:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019946851-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Simula%C3%A7%C3%A3o-de-Valores-Bot%C3%A3o-Telecobran%C3%A7a
---

**Dúvida**

Simulação de Valores - Botão Telecobrança.

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- a partir da versão 11.  
  
  
**Solução**

Foi criada rotina para simular o valor corrigido do título de acordo com a data de pagamento informada. Será acessada através de um botão disponibilizado na barra de ferramentas do atendimento de cobrança. A tela de simulação exibirá todos os títulos que foram carregados no atendimento, onde existirá um campo chamado Data de Pagamento para digitação. Com base na data de pagamento será feito o cálculo de juros para os títulos.  A rotina se baseará no conceito para cálculo de juros do módulo Financeiro que se utiliza dos campos:

|  |  |  |
| --- | --- | --- |
| **Descrição** | **Campo** | **Objetivo** |
| Taxa de Permanência Diária | (E1\_VALJUR) | Valor diário de Juros para dias em atraso |
| Percentual de Juros Diário | (E1\_PORCJUR) | Percentual diário de Juros para dias em atraso |
| Acréscimo | (E1\_ACRESC) | Pode ser utilizado para informar o valor da Multa ou Juros de Mora. |

Os campos que o módulo Financeiro utiliza para cálculo de juros já estão sendo exibidos nos itens do Atendimento de Cobrança. Basta apenas mudá-los de posição no ACOLS para se ter uma melhor visualização dos valores de juros calculados de cada título.

* O campo Prazo de Cobrança é um indicador para o operador ter ciência de quando a conta sairá de sua faixa de cobrança.
* O campo Dias para Prorrogação indica o número máximo de dias em que o operador poderá prorrogar a data de vencimento do título.
* Quando o campo Atualiza o Atendimento, estiver selecionado, irá indicar que os títulos marcados serão prorrogados para a data de pagamento informada. Caso a data de pagamento ultrapasse ao número de dias estipulado para prorrogação do título, a simulação poderá até ser calculada, mas os dados não serão carregados no Acols (Itens de Atendimento).
