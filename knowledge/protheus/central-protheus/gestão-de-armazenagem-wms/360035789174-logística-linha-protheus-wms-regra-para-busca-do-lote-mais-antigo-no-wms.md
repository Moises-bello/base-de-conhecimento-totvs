---
article_id: 360035789174
category: Gestão de Armazenagem (WMS)
content_hash: c64dae4bf26d0b66d28fc8c24227218aafef1e72c054d327526641450802ea6a
fetched_at: '2026-06-28T22:45:48.153725+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Regra para busca do lote mais antigo no
  WMS
type: support-article
updated_at: '2024-09-09T17:24:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035789174-Log%C3%ADstica-Linha-Protheus-WMS-Regra-para-busca-do-lote-mais-antigo-no-WMS
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26246082904983)***Tempo aproximado para leitura: **00:03:00 min****Dúvida**Qual é a regra utilizada para que seja possível efetuar a busca do lote mais antigo no **WMS - Warehouse Management System?**  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - Versão 12  
  
**Solução**Para que seja possível buscar o lote mais antigo no **TOTVS Logística WMS - Linha Protheus** -é necessário informar, no campo **Regra WMS - C6\_REGWMS**, uma das seguintes opções:  
  
**1 - Data/Sequência de Abastecimento**O Sistema seguirá a ordem das estruturas físicas da sequência de abastecimento do produto para buscar o lote mais antigo e considerando o **Tipo de Separação - DC3\_TIPSEP**e a **Separação Mínima - DC3\_QTDUNI**. Logo, pode acontecer de algum lote mais antigo não ser considerado.  
  
**Exemplo:**

|  |  |  |
| --- | --- | --- |
| **Estrutura Física** | **Descrição** | **Norma** |
| 000002 | *Picking* | 40 |
| 000001 | Pulmão | 40 |

|  |
| --- |
| **Pedido de Venda** |
| **Regra WMS** = 3 - Data/Sequência de abastecimento |

Neste caso, a busca será realizada em cada estrutura, sendo ordenada pelo lote mais antigo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Estrutura** | **Endereço** | **Lote** | **Data de Validade** | **Saldo** |
| 000002 | R010301 | 400829 | 25/06/2020 | 17 |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Estrutura** | **Endereço** | **Lote** | **Data de Validade** | **Saldo** |
| 000001 | R010302 | 400829 | 25/06/2020 | 25 |
| 000001 | R030301 | 400829 | 25/06/2020 | 30 |
| 000001 | R010304 | 400842 | 14/09/2020 | 09 |
| 000001 | R020302 | 400842 | 14/09/2020 | 25 |
| 000001 | R030302 | 400842 | 14/09/2020 | 20 |
| 000001 | R010303 | 400843 | 14/09/2020 | 40 |
| 000001 | R020303 | 400843 | 14/09/2020 | 40 |
| 000001 | R030303 | 400860 | 20/09/2020 | 40 |
| 000001 | R070301 | 400860 | 20/09/2020 | 18 |
| 000001 | R080301 | 400860 | 20/09/2020 | 40 |

**Importante**  
Para cada endereço será realizada a validação do **Tipo de Separação - DC3\_TIPSEP** e **Separação Mínima - DC3\_QTDUNI** na separação.   
  
Considerando a estrutura acima, na qual o tipo de separação é **Saldo Restante**, o Sistema irá desconsiderar os lotes mais antigos.

![Op__o_3.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360046783174)

**2 - Data**O sistema consolidará todos os endereços das estruturas físicas cadastradas na sequência de abastecimento do produto, ordenando pelo lote mais antigo e também considerando o **Tipo de Separação - DC3\_TIPSEP** e **Separação Mínima** - **DC3\_QTDUNI**. Nessa opção também pode ocorrer de algum lote mais antigo ser desconsiderado.  
  
**Exemplo 1:**

|  |  |  |
| --- | --- | --- |
| **Estrutura Física** | **Descrição** | **Norma** |
| 000002 | *Picking* | 40 |
| 000001 | Pulmão | 40 |

|  |
| --- |
| **Pedido de Venda** |
| **Regra WMS** = 4 - Data |

  A busca será realizada em todos os endereços das estruturas físicas cadastradas:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Estrutura** | **Endereço** | **Lote** | **Data de Validade** | **Saldo** |
| 000002 | R010301 | 400829 | 25/06/2020 | 17 |
| 000001 | R010302 | 400829 | 25/06/2020 | 25 |
| 000001 | R030301 | 400829 | 25/06/2020 | 30 |
| 000001 | R010304 | 400842 | 14/09/2020 | 09 |
| 000001 | R020302 | 400842 | 14/09/2020 | 25 |
| 000001 | R030302 | 400842 | 14/09/2020 | 20 |
| 000001 | R010303 | 400843 | 14/09/2020 | 40 |
| 000001 | R020303 | 400843 | 14/09/2020 | 40 |
| 000001 | R030303 | 400860 | 20/09/2020 | 40 |
| 000001 | R070301 | 400860 | 20/09/2020 | 18 |
| 000001 | R080301 | 400860 | 20/09/2020 | 40 |

Para cada endereço será realizada a validação do **Tipo de Separação - DC3\_TIPSEP** e **Separação Mínima** - **DC3\_QTDUNI** na separação.  
  
Considerando a estrutura acima, na qual o tipo de separação é **Saldo Restante**, o Sistema irá desconsiderar os lotes mais antigos.

![Op__o_4.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360047652553)

**Exemplo 2:**

|  |  |  |
| --- | --- | --- |
| **Estrutura Física** | **Descrição** | **Norma** |
| 000002 | *Picking* | 45 |
| 000001 | Pulmão | 45 |

|  |
| --- |
| **Pedido de Venda** |
| **Regra WMS** = 4 - Data |

  A busca será realizada em todos os endereços das estruturas físicas cadastradas:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Estrutura** | **Endereço** | **Lote** | **Data de Validade** | **Saldo** |
| 000002 | R020401 | 400910 | 12/02/2022 | 8 |
| 000001 | R030401 | 400910 | 12/02/2022 | 45 |
| 000001 | R020402 | 400910 | 12/02/2022 | 45 |
| 000001 | R010402 | 400911 | 20/05/2022 | 20 |
| 000001 | R030402 | 400912 | 30/06/2022 | 45 |
| 000001 | R020403 | 400912 | 30/06/2022 | 45 |

Para cada endereço será realizada a validação do **Tipo de Separação - DC3\_TIPSEP** e **Separação Mínima - DC3\_QTDUNI** na separação.  
  
Considerando a estrutura acima e que o **Tipo de Separação - DC3\_TIPSEP** da estrutura de *Picking* é igual a **Quantidade mínima**, e que para a estrutura de **Pulmão** é **Somente norma** e a **Quantidade mínima** é igual a **Norma 45**, neste cenário o lote mais antigo é utilizado para o reabastecimento e, por sequência, será utilizado também na separação.

![WMS_Protheus_Exemplo_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360072136854)
