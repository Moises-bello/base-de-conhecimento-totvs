---
content_hash: 858dcc51c67371e2d65fba49e5c6b8cc4082482324bb5118dbbd4c950f3d3e96
fetched_at: '2026-06-29T00:10:38.646105+00:00'
page_id: '544705534'
product: rm
source: tdn-rm
title: Faturamento Direto - Entendendo que há de novo (12.1.28)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544705534
version: 12
---

A partir da 12.1.28 o processo de Faturamento Direto sofreu algumas alterações visando simplificar e melhorar sua usabilidade.

**Então, o que há de novo no processo de Faturamento Direto (12.1.28)**

Agora é feito um cálculo proporcional de dedução.

O sistema passará a realizar o cálculo do valor a deduzir considerando a medição efetuada no período e rateio da tarefa.

Essa regra é aplicada no contrato de insumo e da mesma forma no contrato de serviços.

Nos parâmetros de projetos será possivel definir se deseja "Validar faturamento direto pelo saldo do contrato" ou seja  o calculo do valor a deduzir ira  considerar a mediçao e rateio. Como default o parametro ficara true e nao optando por sua utilizacao basta desmarca-lo. Que o sistema continuara utilizando sem essa validacao.

**Entendendo o que muda na visão deste processo:**

**Exemplo 1:**

**Realizando Faturamento Direto Totvs Obras e Projetos**

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

Foi criado um contrato a pagar de serviço com os seguintes itens:

Ao criar um pedido de faturamento direto no Totvs Obras e Projetos foi informado no pedido duas tarefas:

Tarefa 1

|  |
| --- |
| Tarefa 099.02.11  Produto: 07.21  Quantidade: 50  Valor: 10,00  Valor total do item na tarefa: 500 |

Tarefa 2

|  |
| --- |
| Tarefa 099.02.12  Produto: 07.22  Quantidade: 10  Valor: 10,00  Valor total do item na tarefa: 100 |

Valor total do Pedido de Faturamento Direto no Top = 600,00

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Foi gerado um movimento no BackOffice e recebido o mesmo em seu valor total.

Valor total da nota recebida no BackOffice = 600,00

Foi realizada uma medição de duas tarefas no período 001, sendo elas:

|  |
| --- |
| Tarefa 099.02.12  Valor :200,00  Tarefa 099.02.13  Valor: 300 |

|  |
| --- |
| Total da medição no período 001 = 500 |

567px

Considerando o valor medido (500,00 para tarefa 099.02.011 e tarefa 099.02.13) com o valor recebido na nota (600,00 para tarefa 099.02.11 e tarefa 099.02.12) demonstrado neste exemplo o valor disponível para dedução neste período será apenas 100,00 em relação a tarefa 099.02.012.

Com isso conforme o novo comportamento de validação será exibido a tela **“Associar Faturamento Direto”** com as seguintes informações por período:

A coluna Valor da dedução virá destacada informando o valor da dedução neste período em sua totalidade. Permitindo edição caso seja necessária uma dedução inferior ao que se tem disponível no período.

**Total calculado para dedução:** Total calculado para dedução no período vigente.

**Código do produto:** Código do produto faturado no período.

**Descrição do produto:** Descrição do produto faturado no período.

**Código da tarefa:** Código da tarefa vinculada a dedução no período.

**Número do documento:** Número do documento recebido.

**Valor do produto na tarefa:** Valor do produto na tarefa utilizada na dedução.

**Valor da dedução:** Valor total de dedução.(Este campo estará destacado na visão. Permitindo deduzir o valor total exibido ou um valor inferior.)

**Saldo a deduzir:** Saldo de dedução disponível.

**Valor medido no período:** Valor da medição no período vigente.

**Saldo disponível a deduzir no período:** Saldo ainda disponível no período vigente

**Período:** Período vigente

Quando for utilizado valor total da tarefa e a mesma não possuir mais saldo disponível para dedução o sistema não exibirá a mesma na tela de associar produto faturado.

Caso seja deduzido um valor superior ao Saldo permitido a deduzir o sistema exibirá na grid os valores “estourados” com uma mensagem informativa do porque estão destacados na grid e mesmo que seja executado processo não será finalizado enquanto não for ajustado as inconsistências manualmente.

Caso seja deduzido um valor superior ao Saldo permitido a deduzir o sistema exibirá na grid os valores “estourados” com uma mensagem informativa do porque estão destacados na grid e mesmo que seja executado processo não será finalizado enquanto não for ajustado as inconsistências manualmente.

IMPORTANTE: Hoje o faturamento direto não está disponível e adaptado para ser utilizado com contratos que utilizam a planilha de serviços. Desta forma, deve-se utilizar a planilha de atividades para sua utilização adequada.
