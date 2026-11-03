---
content_hash: 09afe3db17ad6986480f982a14c4f76847ef548c136aab49eca622491a3499e7
fetched_at: '2026-06-29T00:09:26.563067+00:00'
page_id: '423938320'
product: rm
source: tdn-rm
title: Layout Importação de Rateio Gerencial do Patrimônio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938320
version: 4
---

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Descrição** | **Tipo** | **Tamanho** | **Obrigatório** | **Observação** |
| **1** | Código do Patrimônio | Alfanumérico | 25 | X |  |
| **2** | Código da Conta Gerencial | Alfanumérico | 40 | X |  |
| **3** | Percentual | Numérico(15,2) | 3 | X |  |
| **4** | Tipo | Numérico | 1 | X | 0 = Rateio Gerencial  1 = Rateio Gerencial (Reavaliação) |

**Regras de Importação:**  
1- O percentual deverá ser igual a 100 independente de quantas contas gerencias serão usadas;

2- A conta gerencial não poderá ser repetida no mesmo tipo de rateio, ou seja, caso esteja importando rateio gerencial no arquivo .txt não poderá ter a conta (por exemplo) 5.01 repetida para o tipo 0.

3- Como o campo Percentual é numérico as casas decimais deverão ser separadas por vírgula, exemplo "100,00".
