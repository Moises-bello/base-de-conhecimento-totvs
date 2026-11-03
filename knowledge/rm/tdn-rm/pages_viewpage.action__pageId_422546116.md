---
content_hash: 3f7e624105f7c82c1e48e7367d005eb6841f11a450d13ba270ad25192dd2b22c
fetched_at: '2026-06-29T00:09:23.755797+00:00'
page_id: '422546116'
product: rm
source: tdn-rm
title: Sub Apuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546116
version: 9
---

Um mesmo Decreto pode conceder vários benefícios. O objetivo deste cadastro é concatenar todas as informações necessárias para que o sistema possa realizar as Sub-Apurações de forma automática. Este cadastro deve contém as seguintes informações:

* Identificador do Benefício
* Código**¹** (auto incremento)
* Indicador da Sub-apuração
* Descrição
* Percentuais de Incentivo – Devem ser apresentados os seguintes campos, em função do "**Indicador do enquadramento do benefício**":

**Indústria** (crédito presumido):  
Percentual do Crédito Presumido do ICMS  
Percentual do Crédito Presumido do ICMS para operações para Fora do Nordeste

***Importante!!!*** (diferimento/crédito presumido):

Percentual de incentivo nas saídas Interestaduais  
Percentual de crédito presumido para as saídas internas, por faixa de alíquota:

| Faixa | Carga Tributária |
| --- | --- |
| 1 | Até 7% |
| 2 | Acima de 7% e até 12% |
| 3 | Acima de 12% e até 17% |
| 4 | Acima de 17% |

**Central de distribuição** (entradas/saídas):  
Percentual de incentivo para as entradas  
Percentual de incentivo para as saídas  
  
***Importante!!!***Os percentuais são exclusivos. O sistema deve permitir o preenchimento de apenas um percentual por Sub-Apuração: Indústria, ou Importação ou Central de Distribuição.   
*¹Deve ser atribuído um código distinto para cada hipótese de apuração a partir do código "2", sequencial e consecutivamente. O código "1" é reservado para itens NÃO incentivados. Orientações constantes do Manual de Orientações da SEF (Registros 8515 e 8535).*

---
