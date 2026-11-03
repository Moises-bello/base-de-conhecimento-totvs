---
article_id: 1500003988522
category: RH - Contrato Intermitente
content_hash: 5651afb51e951e8f333d94b5b1b1a95112cf3ef51fab5eb40a38ec27aa36cbb5
fetched_at: '2026-06-28T22:43:40.108581+00:00'
product: protheus
section_id: 360003139951
source: central-protheus
title: RH - Linha Protheus - GPE - Criação automática de períodos ao cadastrar convocação
  para funcionário de contrato intermitente
type: support-article
updated_at: '2025-04-15T18:14:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003988522-RH-Linha-Protheus-GPE-Cria%C3%A7%C3%A3o-autom%C3%A1tica-de-per%C3%ADodos-ao-cadastrar-convoca%C3%A7%C3%A3o-para-funcion%C3%A1rio-de-contrato-intermitente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25967361282327)** Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida** **Criação automática de períodos** ao cadastrar **convocação** para funcionário de **contrato intermitente.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Criado um **facilitador de cadastro automático de períodos** a partir do **cadastro de convocação de funcionário de contrato intermitente** conforme o **período da convocação** e a **data de pagamento**, caso o parâmetro **MV\_PONINTE** esteja ativo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31434741381911)  
  
Com o parâmetro **MV\_PONINTE** ativo, ao efetuar a **confirmação da manutenção** na rotina de cadastro de **convocação** será efetuado uma verificação no cadastro de período e **caso não haja cadastro de período com a data de pagamento da convocação** será efetuado a **gravação automática de um novo período baseado no período da convocação e na data de pagamento da convocação.**  
  
**Exemplo**  
No cadastro de períodos, há apenas um cadastro:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Período | Semana | Data inicial | Data final | Data de pagamento |
| 202402 | 1 | 01/02/2024 | 28/02/2024 | 05/03/2024 |
| 202402 | 2 | 08/02/2024 | 16/02/2024 | 18/02/2024 |

Para um funcionário de contrato intermitente, será incluído uma convocação de 08/02/2024 a 15/02/2024 com data de pagamento em 18/02/2024. Ao confirmar o cadastro, o sistema fará a inclusão de um novo período e o cadastro de períodos ficará conforme abaixo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Período** | **Semana** | **Data inicial** | **Data final** | **Data de pagamento** |
| 202402 | 1 | 01/02/2024 | 28/02/2024 | 05/03/2024 |
| 202402 | 2 | 08/02/2024 | 15/02/2024 | 18/02/2024 |

Para um outro funcionário de contrato intermitente, será incluído uma convocação de 10/02/2024 a 16/02/2024 com data de pagamento em 18/02/2024. Ao confirmar o cadastro, o sistema verificará que já existe um período em 02/2024 com data de pagamento em 18/02, mas como a data final do período é menor do que o período de convocação, o sistema fará a exibição de uma mensagem de confirmação para o usuário confirmar a alteração da extensão da data final do período para a data da convocação. Caso seja confirmado, o sistema irá atualizar o cadastro e o cadastro de períodos ficará conforme abaixo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Período** | **Semana** | **Data inicial** | **Data final** | **Data de pagamento** |
| 202402 | 1 | 01/02/2024 | 28/02/2024 | 05/03/2024 |
| 202402 | 2 | 08/02/2024 | 16/02/2024 | 18/02/2024 |

**Obs.**: caso o usuário não confirme a alteração automática do sistema, posteriormente deverá realizar a alteração manual no cadastro de períodos.  
  
Para um outro funcionário de contrato intermitente, será incluído uma convocação de 10/02/2024 a 16/02/2024 com data de pagamento em 20/02/2024. Ao confirmar o cadastro, o sistema fará a inclusão de um novo período e o cadastro de períodos ficará conforme abaixo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Período** | **Semana** | **Data inicial** | **Data final** | **Data de pagamento** |
| 202402 | 1 | 01/02/2024 | 28/02/2024 | 05/03/2024 |
| 202402 | 2 | 08/02/2024 | 16/02/2024 | 18/02/2024 |
| 202402 | 3 | 10/02/2024 | 16/02/2024 | 20/02/2024 |

Para um outro funcionário de contrato intermitente, será incluído uma convocação de 24/02/2024 a 05/03/2024 com data de pagamento em 08/03/2024. Ao confirmar o cadastro, o sistema fará a inclusão de um novo período para 02/2024 e um novo período para 03/2024 e o cadastro de períodos ficará conforme abaixo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Período** | **Semana** | **Data inicial** | **Data final** | **Data de pagamento** |
| 202402 | 1 | 01/02/2024 | 28/02/2024 | 05/03/2024 |
| 202402 | 2 | 08/02/2024 | 16/02/2024 | 18/02/2024 |
| 202402 | 3 | 10/02/2024 | 16/02/2024 | 20/02/2024 |
| 202402 | 4 | 24/02/2024 | 28/02/2024 | 08/03/2024 |
| 202403 | 1 | 01/03/2024 | 05/03/2024 | 08/03/2024 |

**Importante**

O sistema **não** fará a exclusão de períodos caso alguma convocação seja excluída.

O sistema **não** fará a inclusão de cadastro em período anterior ao que está em aberto.  
  
**Saiba Mais**

[Contrato Intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003139951-RH-Contrato-Intermitente)  
[Apuração dos resultados por convocação para funcionário com contrato intermitente](https://tdn.totvs.com/pages/viewpage.action?pageId=561855697)
