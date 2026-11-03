---
content_hash: 46aaccd003fe3520223668a8bd94d9996b60f27a0d312523254d781b02b23984
fetched_at: '2026-06-29T00:10:25.192270+00:00'
page_id: '502445512'
product: rm
source: tdn-rm
title: FISCAL01-9798 ER - EFD-REINF - Encerramento e Reabertura
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-9798+ER+-+EFD-REINF+-+Encerramento+e+Reabertura
version: 77
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão Fiscal |
| **Segmento Executor** | Backoffice | | |
| **Requisito/Story/Issue** | FISCAL01-9796 | **Subtarefa** | FISCAL01-10244 |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

# Objetivo

 Detalhar as alterações necessárias no módulo TOTVS Gestão Fiscal para a implementação dos Eventos Periódicos R-2099 e R-2098 da EFD-REINF.

# R-2099 Fechamento dos Eventos Periódicos

Ao final do período é necessário executar o fechamento do mesmo junto a RFB através do evento R-2099. 

Deverá ser criado um processo com nome "R-2099 Fechamento dos Eventos Periódicos" de controle do Evento R-5011 que será disponibilizado somente na lista de processos da visão do R-5011. Este processo será integrado com o TSS já no momento de sua inclusão. Ao ser executado com sucesso o status do Evento R-5011 deve ser alterado para Encerrado e se durante a consulta do R-2099 o mesmo for rejeitado o R-5011 voltará para o status de "Aberto". O primeiro passo deste processo será a execução do processo "Gerar Eventos Periódicos" e se for identificado algum Evento ainda não autorizado o processo deverá alertar o usuário e confirmar a execução do R-2099.

## Regras

* Ao executar o R-2099 o sistema deverá alertar ao usuário sobre eventos não autorizados, mas não deverá impedir o encerramento e neste caso deve ser gravado no log do histórico uma indicação da escolha do usuário e os detalhes dos eventos não autorizados**;**
* O encerramento só poderá ser executado se os Períodos de Apuração dos tributos que são considerados na EFD-REINF estiverem fechados (INSS, Funrural e CPRB)**;**
* Enquanto o período estiver encerrado o sistema deverá bloquear a alteração em eventos existentes e a inclusão de novos eventos no período;
* O processo só pode ser executado para Períodos (R-5011) com Status "Aberto";
* O período de apuração dos tributos não poderá ser reaberto enquanto o período da EFD-REINF permanecer encerrado.

# R-2098 Reabertura dos Eventos Periódicos

Conforme necessário o período da EFD-REINF poderá ser reaberto através do Evento R-2098. Deverá ser criado um processo com nome "R-2098 Reabertura dos Eventos Periódicos" de controle do Evento R-5011 que será disponibilizado somente na lista de processos da visão do R-5011. Este processo será integrado com o TSS já no momento de sua inclusão. Se o Evento R-2098 for autorizado com sucesso o status do R-5011 deverá ser alterado para Aberto e os dados de encerramento do R-5011 devem ser apagados sendo necessário executar novamente o encerramento em outro momento.

## Regras

* O processo só pode ser executado para Períodos (R-5011) com Status "Encerrado".

# Layout dos Eventos

false0left0R-2099xmlExemplo R-2099


{...}
{...}
{...}
{...}
]]>1R-2098xmlExemplo R-2098


{...}
{...}
]]>

## Origem dos dados

Abaixo seguem as estruturas e o mapeamento das origens campo a campo.

false1left0ideRespInf

## Responsável pelas informações

xmlideRespInf
str1234
str12340000
str1234
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| nmResp | DFILIAL.NOMECONTADOR |
| cpfResp | DFILIAL.CPFCONTADOR |
| telefone | DFILIAL.DDDCONTADOR + DFILIAL.TELEFONECONTADOR |
| email | DFILIAL.EMAILCONTADOR |

1infoFech

## Informações do Fechamento

xmlinfoFech
S
S
S
S
S
S
str1234
1999-05
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| evtServTm | Se Existe algum Algum Evento R-2010 autorizado deverá ser gerado com  Então "S"  Senão "N" |
| evtServPr | Se Existe algum Algum Evento R-2020 autorizado deverá ser gerado com  Então "S"  Senão "N" |
| evtAssDespRec | Se Existe algum Algum Evento R-2030 autorizado deverá ser gerado com  Então "S"  Senão "N" |
| evtAssDespRep | Se Existe algum Algum Evento R-2040 autorizado deverá ser gerado com  Então "S"  Senão "N" |
| evtComProd | Se Existe algum Algum Evento R-2050 autorizado deverá ser gerado com  Então "S"  Senão "N" |
| evtCPRB | Se Existe algum Algum Evento R-2060 autorizado deverá ser gerado com  Então "S"  Senão "N" |
| evtPgtos | Se Existe algum Algum Evento R-2070 autorizado deverá ser gerado com  Então "S"  Senão "N" |
| compSemMovto | Quando não existir nenhum Evento Periódico Autorizado no período, solicitar ao usuário que preencha a informação |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
