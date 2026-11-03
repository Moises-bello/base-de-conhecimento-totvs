---
content_hash: 2efb17b0baf370c74343c2b18342d9ff7ac3c21e021bbe01ea67dbbb9b99467d
fetched_at: '2026-06-29T00:09:48.575939+00:00'
page_id: '435105196'
product: rm
source: tdn-rm
title: Cobrança por Orçamento - Modelo de Cálculo de Rateio - Rateio por CRD
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105196
version: 15
---

O CRD (Coeficiente de Rateio de Despesa) é um anexo do cadastro de subunidade. Neste cadastro o usuário informa o valor do CRD, datas de início e fim e o item de cobrança. No cálculo do rateio por CRD, o sistema irá multiplicar o valor da despesa pelo valor do CRD:

|  |
| --- |
| **Valor Total da Despesa \* CRD** |

Desta forma o sistema irá obter o CRD de cada subunidade verificando se o item de cobrança é o mesmo cadastrado para a despesa e considerando a validade do CRD de acordo com as datas.  
Neste modelo o usuário pode definir as seguintes associações:

* **Um empreendimento:** Rateio será realizado para todas as subunidades do empreendimento definido;
* **Uma ou mais unidades:** Rateio será realizado para todas as subunidades da unidade ou de um conjunto de unidades;
* **Uma ou mais subunidades:** Rateio será realizado diretamente na subunidade definida ou no conjunto de subunidades;

Dessa forma esse rateio pode ser aplicado para todas as despesas associadas aos seguintes níveis:

|  |  |  |  |
| --- | --- | --- | --- |
| Rateio | Empreendimento | Unidade | Subunidade |
| Rateio por CRD | X | X | X |

**Observação:**

* Caso pelo menos uma das subunidades estiver associada a um imóvel do módulo de Aluguel , tendo como Tipo de Locação "Áreas Fracionadas" ou "Áreas Unificadas", a apuração não será executada para a despesa relacionada.
* Somente será apurado o CRD com o mesmo Item de Cobrança da despesa e com período dentro da competência do fechamento.
* Para que a cobrança do orçamento seja calculada corretamente, todas as subunidades devem possuir o cadastro de CRD correspondente. Caso alguma subunidade não possua CRD preenchido o processo de cálculo de fechamento não será executado.
* A partir da versão 12.1.2306 o gestor de contratos terá a opção de informar os Fatores que compõem o CRD. Estes fatores e seus nomes irão aparecer na tela para o usuário utilizar após realizar a configuração nos parâmetros da Gestão do Condomínio.

                   

### Rateio por CRD utilizando fórmulas

---

A partir da versão 12.1.2209, foi disponibilizado na interface do Coeficiente de Rateio de Despesa um campo onde o usuário poderá utilizar uma fórmula para realizar os devidos cálculos. Dessa forma, flexibilizamos a cobrança através do CRD, possibilitando que o usuário desenvolva fórmulas cujo resultado irá refletir no fechamento do condomínio quando o orçamento for realizado via rateio por CRD.

Atenção

Utilizar fórmulas pode acarretar em perda de performance durante os processos de fechamento.

Abaixo, um exemplo de fórmula que utiliza os fatores de CRD retornando seus respectivos valores:

Veja Também

---

* # [Manutenção de Empreendimentos - Condomínio](http://tdn.totvs.com/pages/viewpage.action?pageId=435105121)
