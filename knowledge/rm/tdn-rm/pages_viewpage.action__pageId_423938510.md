---
content_hash: 85113b7a01edbc1b451b1889012188ab68c9256bfa6277a6a4eaa5955925f8db
fetched_at: '2026-06-29T00:09:27.389870+00:00'
page_id: '423938510'
product: rm
source: tdn-rm
title: Layout de Importação de Plano de Contas Paralelo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938510
version: 6
---

Para a realização da importação do plano de contas paralelo, é necessário primeiramente cadastrar o tipo de plano paralelo via sistema e em seguida, informar o código do plano criado no arquivo a ser importado.

As informações do layout abaixo deverão ser disponibilizadas em um único arquivo, pois no momento da importação o sistema irá distinguir a informação através do identificador de Linha.

1. Plano de Contas Paralelo

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **#** | **Descrição** | **Tipo** | **Tamanho** | **Obrigatório** | **Observação** |
| **1** | Identificador de linha | Alfa | 1 | X | Sempre "M" |
| **2** | Código plano paralelo | Alfanumérico | 10 | X |  |
| **3** | Código da Conta no Plano Paralelo | Alfanumérico | 40 | X |  |
| **4** | Descrição | Alfanumérico | 100 | X |  |
| **5** | Natureza da Conta | D ou C | 1 | X | D= Débito  C=Crédito |
| **6** | Conta Analítica ou Sintética | A ou S | 1 | X | S= Sintética  A= Analítica |

2. Linhas Opcionais (Contas Contábeis Relacionadas)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **#** | **Descrição** | **Tipo** | **Tamanho** | **Obrigatório** | **Observação** |
| **1** | Identificador da linha | \* | 1 | X |  |
| **2** | Código do Plano de Contas Paralelo | Alfanumérico | 10 | X |  |
| **3** | Código da Conta no Plano de Contas Paralelo | Alfanumérico | 40 | X |  |
| **4** | Código da Conta no Plano de Contas Contábil | Alfanumérico | 40 | X |  |

3. Linhas Opcionais (Centro de Custo/ Conta Gerencial Associado à Conta Contábil)

Somente é possível realizar a importação de centro de custo / Conta gerencial se for informada uma linha para importação da conta contábil Associada.

Associar Centro de Custo

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **#** | **Descrição** | **Tipo** | **Tamanho** | **Obrigatório** | **Observação** |
| **1** | Identificador da linha | C | 1 | X | Sempre "C" |
| **2** | Código do Plano de Contas Paralelo | Alfanumérico | 10 | X |  |
| **3** | Código da Conta no Plano de Contas Paralelo | Alfanumérico | 40 | X |  |
| **4** | Código da Conta no Plano de Contas Contábil | Alfanumérico | 40 | X |  |
| **5** | Código do Centro de Custo | Alfanumérico | 25 | X |  |

Associar Conta Gerencial

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **#** | **Descrição** | **Tipo** | **Tamanho** | **Obrigatório** | **Observação** |
| **1** | Identificador da linha | G | 1 | X | Sempre "G" |
| **2** | Código do Plano de Contas Paralelo | Alfanumérico | 10 | X |  |
| **3** | Código da Conta no Plano de Contas Paralelo | Alfanumérico | 40 | X |  |
| **4** | Código da Conta no Plano de Contas Contábil | Alfanumérico | 40 | X |  |
| **5** | Código da Conta Gerencial | Alfanumérico | 40 | X |  |

**Observações**

As linhas de Contas Contábeis relacionadas, quando presentes, devem obrigatoriamente seguir linhas de Contas Paralelas. Elas indicam o relacionamento do Plano Contábil com o Plano Paralelo. O sistema irá acusar erro caso sejam informadas linhas de contas contábeis sem antes informar uma linha de conta paralela.

Mais informações

* Contas Paralelas
