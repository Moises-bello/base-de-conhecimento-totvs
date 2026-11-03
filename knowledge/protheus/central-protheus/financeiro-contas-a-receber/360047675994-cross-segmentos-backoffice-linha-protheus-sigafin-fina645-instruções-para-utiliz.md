---
article_id: 360047675994
category: Financeiro - Contas a Receber
content_hash: 08d879b065cf2e1e027ac979009576823cda3948bc3fe02d778e311bf380a1ab
fetched_at: '2026-06-28T22:38:13.899778+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN  - FINA645 - Instruções
  para utilização da rotina Provisão de Devedores Duvidosos '
type: support-article
updated_at: '2026-06-09T21:05:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047675994-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA645-Instru%C3%A7%C3%B5es-para-utiliza%C3%A7%C3%A3o-da-rotina-Provis%C3%A3o-de-Devedores-Duvidosos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:06:00 min  
  
Dúvida**Instruções para utilização da rotina Provisão de Devedores Duvidosos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Para utilização da rotina **FINA645** - **Provisão de Devedores Duvidosos** segue material abaixo com as informações necessárias:

A rotina **FINA645 - PDD (Provisão de Devedores Duvidosos)** constitui a provisão para devedores duvidosos.

Outras denominações dessa provisão:

* Perdas Estimadas em Créditos de Liquidação Duvidosa (PECLD).
* Provisão para Perdas Sobre Créditos (PPSC).
* Provisões para Créditos de Liquidação Duvidosa (PCLD).

Esta provisão cobre perdas prováveis no recebimento das duplicatas. Assim, uma vez constituída tal provisão e, não ocorrendo o recebimento de algumas duplicatas pela empresa, essas eram obrigatoriamente baixadas em contrapartida com a Provisão para Devedores Duvidosos.

**Exemplo**: Se ao final do ano, o total de perdas não atingisse o valor da Provisão, a sobra era revertida, ou seja, era contabilizada como receita, zerando a Provisão antiga, para na sequência efetuar-se uma nova Provisão para o ano seguinte.

* **Parâmetros**

|  |  |
| --- | --- |
| **Nome da Variável** | **MV\_PDDREF** |
| **Tipo** | Caracter |
| **Descrição** | Campo para considerar na regra do PDD: 1= Vencimento Real (**E1\_VENCREA**) 2 = Vencimento do Título (**E1\_VENCTO**) 3 = Vencimento Original (**E1\_VENCORI**) |
| **Valor Padrão** | 1 |

|  |  |
| --- | --- |
| **Nome da Variável** | **MV\_PDDRTNF** |
| **Tipo** | Numérico |
| **Descrição** | Indica se a rotina de **PDD** irá realizar o rateio por item da nota fiscal que gerou o título. 1=Sim ou 2=Não |
| **Valor Padrão** | 2 |

|  |  |
| --- | --- |
| **Nome da Variável** | **MV\_PDDACRE** |
| **Tipo** | Carácter |
| **Descrição** | Selecione se o saldo liquido do **PDD** irá considerar o acréscimo e decréscimo do título. 1=Sim ou 2=Não |
| **Valor Padrão** | 1 |

|  |  |
| --- | --- |
| **Nome da Variável** | **MV\_BAIXPDD** |
| **Tipo** | Lógico |
| **Descrição** | Indica se a rotina de **PDD** irá considerar também os títulos baixados em sua totalidade com atraso. .T. = Irá considerar títulos baixados com atraso. .F. = Não Irá considerar títulos baixados com atraso.  Obs.: Este parâmetro será incorporado ao produto a partir do release 12.1.27. Havendo necessidade de uso é possível a inclusão do mesmo através do módulo configurador. |
| **Valor Padrão** | .F. |

* Tabelas utilizadas:

| Chave | Nome | Modo | PYME |
| --- | --- | --- | --- |
| **FJX** | Processamento PDD | C | S |
| **FJY** | Clientes em PDD | C | S |
| **FJZ** | Títulos Provisicionados | C | S |
| **FWZ** | Rateio de Tìtulos PDD | C | S |
| **FRV** | Situação de Cobrança | C | S |

Saiba mais:  
[Exemplo de utilização PDD](https://tdn.totvs.com/pages/releaseview.action?pageId=452396076#Provis%C3%A3odeDevedoresDuvidosos-FINA645-Financeiro-P12-02.EXEMPLODEUTILIZA%C3%87%C3%83O)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Pontos de Entrada FINA645](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048406293)
