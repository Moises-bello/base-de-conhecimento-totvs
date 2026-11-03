---
content_hash: f6638f5cc88991b0ee1a5dd79f707131c8a7a384ed9d5902f8c7d806d0a9fc12
fetched_at: '2026-06-29T00:09:23.106734+00:00'
page_id: '422546047'
product: rm
source: tdn-rm
title: Regras aplicadas à geração dos registros M310 e M360
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546047
version: 3
---

O layout e regras aplicadas na geração do registro M310 e M360 são as mesmas, a diferença é que o registro M310 são informações do IRPJ e M360 são informações da CSLL. Não vou detalhar o layout do registro na especificação, qualquer duvida consulte o manual da ECF.

**Como irá funcionar?**

O módulo TOTVS Gestão Contábil irá identificar através do detalhamento do período de apuração todos os itens com origem igual a contábil, e a partir destes itens serão identificados no Evento Tributário as Contas Contábeis parametrizadas para apurar o imposto.  
 O serviço do módulo TOTVS Gestão Contábil irá aplicar as regras abaixo e estruturar os registros M310 e M360.   
 ***Observação***: Os itens do Evento Tributário parametrizado com "Saldo Anterior" não serão considerados para gerar este registro.

Informações enviadas pelo TOTVS Gestão Fiscal:

|  |  |  |
| --- | --- | --- |
| **Descrição** | | **Observação** |
| 1 | Código da Conta | *Conta Contábil parametrizada no Evento Tributário* |
| 2 | Código do Centro de Custo | *Centro de Custo parametrizado no Evento Tributário* |
| 3 | Valor de Detalhamento da Apuração | *Valor processado no detalhamento da apuração* |
| 4 | Indicador do Tipo do Saldo Utilizado | *Opções:*   ü  *1 – Saldo Total (Saldo Atual);*   ü  *2 – Total de Créditos;*   ü  *3 – Total de Débitos;*   ü  *4 – Saldo do Período (Movimentação = Débito - Credito).* |

**Regra?**

O contábil vai validar se o "**Valor de Detalhamento da Apuração**" esta conforme o valor apresentado no registro K155 (contas patrimoniais) ou K355 (contas de resultado), ou seja, o contábil localiza no registro K155 ou K355 através do "**Código da Conta**" e "**Código do Centro de Custo**" o valor e aplica a validação.  
  A tabela abaixo indica qual o valor que o sistema busca no registro para realizar a validação.

|  |  |  |  |
| --- | --- | --- | --- |
| **Indicador do Tipo do Saldo Utilizado** | | **Registro K155** | **Registro K355** |
| 1 | Saldo Total | *VL\_SLD\_FIN* | *VL\_SLD\_FIN* |
| 2 | Total de Créditos | *VL\_CRED* | *Não é valido para conta de resultado* |
| 3 | Total de Débitos | *VL\_DEB* | *Não é valido para conta de resultado* |
| 4 | Saldo do Período | *VL\_DEB – VL\_CRED* | *Não é valido para conta de resultado* |

**1º Cenário: O Fiscal envia os itens sem centro de custo, ou seja, o usuário parametrizou somente a conta contábil no Evento Tributário e o registro K155/K355 é gerado quebrando por Centro Custo.**

Para esta situação o contábil vai estruturar o registro M310 e M360 considerando o centro de custo que estiver no registro K155/K355, exemplo:

Evento Tributário/Detalhamento apuração

|  |  |  |
| --- | --- | --- |
| **Código da Conta** | **Cód. Centro de Custo.** | **Valor da Apuração** |
| 1.1.1.001 | VAZIO | 2.000,00 |

Temos no K155:

|  |  |  |
| --- | --- | --- |
| **Código da Conta** | **Cód. Centro de Custo.** | **Valor da Apuração** |
| 1.1.1.001 | 01.01 | 500,00 |
| 1.1.1.001 | 01.02 | 250,00 |
| 1.1.1.001 | 01.03 | 1.250,00 |

Teremos um M310/M360 assim:

|  |  |  |
| --- | --- | --- |
| **Código da Conta** | **Cód. Centro de Custo.** | **Valor da Apuração** |
| 1.1.1.001 | 01.01 | 500,00 |
| 1.1.1.001 | 01.02 | 250,00 |
| 1.1.1.001 | 01.03 | 1.250,00 |

**2º Cenário: O Fiscal envia os itens com centro de custo, ou seja, o usuário parametrizou a conta contábil e o centro de custo no Evento Tributário, exemplo:**

Evento Tributário/Detalhamento apuração

|  |  |  |
| --- | --- | --- |
| **Código da Conta** | **Cód. Centro de Custo.** | **Valor da Apuração** |
| 1.1.1.001 | 01.02 | 500,00 |

 Temos no K155:

|  |  |  |
| --- | --- | --- |
| **Código da Conta** | **Cód. Centro de Custo.** | **Valor da Apuração** |
| 1.1.1.001 | 01.01 | 500,00 |
| 1.1.1.001 | 01.02 | 250,00 |
| 1.1.1.001 | 01.03 | 1.250,00 |

 Teremos um M310/M360 assim:

|  |  |  |
| --- | --- | --- |
| **Código da Conta** | **Cód. Centro de Custo.** | **Valor da Apuração** |
| 1.1.1.001 | 01.01 | 500,00 |

Será enviada somente a informação equivalente. Deverão ser mostradas no LOG as informações que não foram consideradas para montar o registro M310/M360.

**3º Cenário: O Fiscal envia os itens com centro de custo, ou seja, o usuário parametrizou a conta contábil e o Centro de Custo, porém o Centro de Custo esta parametrizado para não ser enviado para o SPED Contábil (a ECF respeita esta regra).**

No Contábil é possível o usuário identificar no Centro de Custo se deseja que o mesmo seja enviado para o SPED/ECF (vide cadastro), e quando isto ocorre à informação daquele centro de custo é enviada para um Centro de Custo vazio (simbolicamente), exemplo:

Evento Tributário/Detalhamento apuração

|  |  |  |
| --- | --- | --- |
| **Código da Conta** | **Cód. Centro de Custo.** | **Valor da Apuração** |
| 1.1.1.001 | 01.01 (não envia p/ SPED) | 500,00 |
| 1.1.1.001 | 01.03 (não envia p/ SPED) | 700,00 |

Temos no K155:

|  |  |  |
| --- | --- | --- |
| **Código da Conta** | **Cód. Centro de Custo.** | **Valor da Apuração** |
| 1.1.1.001 |  | 1.750,00 |
| 1.1.1.001 | 01.02 | 250,00 |

Teremos um M310/M360 assim:

|  |  |  |
| --- | --- | --- |
| **Código da Conta** | **Cód. Centro de Custo.** | **Valor da Apuração** |
| 1.1.1.001 |  | 500,00 |
| 1.1.1.001 |  | 700,00 |
| 1.1.1.001 | 01.02 | 250,00 |

Observe que nesta situação o valor que o sistema vai considerar para gerar o registro M310/M360 será o valor enviado pelo Fiscal.  
Outro item importante é que quando isto ocorrer o sistema deverá agrupar as informações para que o PVA não apresente erros, pois a chave do registro é COD\_CTA + COD\_CCUS. Após o agrupamento, teremos um M310/M360 assim:

|  |  |  |
| --- | --- | --- |
| **Código da Conta** | **Cód. Centro de Custo.** | **Valor da Apuração** |
| 1.1.1.001 |  | 1.200,00 |
| 1.1.1.001 | 01.02 | 250,00 |

Observe que o valor total (1.750,00) do registro ainda não fechou com o valor do K155 (2.000,00), neste caso será apresentada uma mensagem no LOG.

**4º Cenário: O "Valor de Detalhamento da Apuração" esta diferente do valor apurado no registro K155 ou K355, exemplo:**

Evento Tributário/Detalhamento apuração

|  |  |  |
| --- | --- | --- |
| **Código da Conta** | **Cód. Centro de Custo.** | **Valor da Apuração** |
| 1.1.1.001 |  | 2.000,00 |

Temos no K155:

|  |  |  |
| --- | --- | --- |
| **Código da Conta** | **Cód. Centro de Custo.** | **Valor da Apuração** |
| 1.1.1.001 | 01.01 | 500,00 |
| 1.1.1.001 | 01.02 | 250,00 |

Teremos um M310/M360 assim:

|  |  |  |
| --- | --- | --- |
| **Código da Conta** | **Cód. Centro de Custo.** | **Valor da Apuração** |
| 1.1.1.001 | 01.01 | 500,00 |
| 1.1.1.001 | 01.02 | 250,00 |

Neste cenário será enviado sempre o valor do K155/K355 e mostrado no LOG a diferença de valores.

**Preenchimento do campo "Indicado do Saldo da Conta" no Registro M310/M360**

Este campo será preenchido conforme a tabela abaixo:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Indicador do Tipo do Saldo Utilizado** | | **Registro K155** | **Indicador do Saldo K155** | **Registro K355** | **Indicador do Saldo K355** |
| 1 | Saldo Total | *VL\_SLD\_FIN* | *IND\_VL\_SLD\_FIN* | *VL\_SLD\_FIN* | *IND\_VL\_SLD\_FIN* |
| 2 | Total de Créditos | *VL\_CRED* | *D = Débito* | *Não é valido para conta de resultado* | *Não é valido para conta de resultado* |
| 3 | Total de Débitos | *VL\_DEB* | *C = Crédito* | *Não é valido para conta de resultado* | *Não é valido para conta de resultado* |
| 4 | Saldo do Período | *VL\_DEB – VL\_CRED* | *Se a "Movimentação" < 0 então  "C";*   *Se não "D";* | *Não é valido para conta de resultado* | *Não é valido para conta de resultado* |
