---
content_hash: 75f7a67672d6bdc8ec58769605c53093873ae2ecfddc74c717e870f668883671
fetched_at: '2026-06-29T00:08:15.032469+00:00'
page_id: '244725645'
product: rm
source: tdn-rm
title: ER_Vínculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244725645
version: 118
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão Financeira |
| **Segmento Executor** | Educacional | | |
| **Chamado** | TUJRTI | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *,* | | |

## Objetivo

 Revitalização do processo de vínculo de lançamentos financeiros com objetivo de separação do valor a ser dado como crédito entre valor do vínculo e valor de retenção vinculadas quando tiver retenção envolvida no processo. Essa revitalização permitia um melhor entendimento do processo para facilitar a sua evolução futura e manutenção.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Vínculo | Alteração | Contas a Pagar / Receber -> Operações Financeiras -> Lançamentos -> Processos -> Vincular Lançamentos | Vínculos entre lançamentos financeiros |

 A regras de negócio definidas e descritas no documento " **Documentação -** ***Vinculo - FLUXUS.docx*** " em anexo.

## ***Tabelas Utilizadas***

* FLan: Tabela de lançamento financeiro
* FRelLan: Tabela de relacionado entre os lançamentos financeiros vinculados
* FRelLanHST: Tabela de histórico do relacionado entre os lançamentos financeiros vinculados
* FTRBLan: Tabela de tributo do lançamento financeiro
* FTRBLanHST: Tabela de histórico do tributo do lançamento financeiro
* FAdiantamentoRetencao: Tabela de valor da base de cálculo vinculada entre os lançamentos vinculados quando ambos tem retenção
* FLogValores: Tabela com valor restante em aberto do lançamento financeiro

## Dicionário de Dados

**Arquivo ou Código do Script: FS.2016.08\_03 -** FADIANAMENTO  - Tabela de valor da base de cálculo vinculada entre os lançamentos vinculados quando ambos tem retenção 

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | PKFADIANTAMENTORETENCAO: CODCOLIGADA + IDADIANTRETENCAO |
| **02** | IDX\_FADIANTRET\_FLANADIANT: CODCOLIGADA + IDLAN |
| **03** | IDX\_FADIANTRET\_FLANNF: CODCOLIGADA + IDLANVINCULADO |
| **04** | IDX\_FADIANTRET\_FLANBAIXANF: CODCOLIGADA + IDLANVINCULADO + IDBAIXAVINCULADO |
| **05** | IDX\_FADIANTRET\_FLANBAIXAADIANT: CODCOLIGADA + IDLAN + IDBAIXA |
| **06** | IDX\_FADIANTRET\_FTRBLAN: CODCOLIGADA + IDTRBLAN + IDTRBLANVINCULADO |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo** | **Tipo** | **Tamanho** | **Mandatório** | **Descrição** | **Título** |
| IDADIANTRETENCAO | Inteiro |  | Sim (x ) Não (  ) | Id. Adiantamento Retenção | Id. Adiantamento Retenção |
| IDLAN | Inteiro |  | Sim ( ) Não (X ) | Id Lançamento Adiantamento/Crédito Adiantamento | Id Lançamento Adiantamento/Crédito Adiantamento |
| IDLANVINCULADO | Inteiro |  | Sim () Não (X) | Id do Lançamento Nota Fiscal Vinculada | Id do Lançamento Nota Fiscal Vinculada |
| IDBAIXA | Inteiro |  | Sim (  ) Não ( X ) | Id Item Baixa Lançamento Adiantamento/Crédito Adiantamento | Id Item Baixa Lançamento Adiantamento/Crédito Adiantamento |
| IDBAIXAVINCULADO | Inteiro |  | Sim (  ) Não (X  ) | Id Item Baixa Lançamento Nota Fiscal Vinculada | Id Item Baixa Lançamento Nota Fiscal Vinculada |
| BASEDECALCULOLANVINCULADO | Decimal |  | Sim (  ) Não (X  ) | Base Cálculo Vinculada/Baixa Lançamento NF | Base Cálculo Vinculada/Baixa Lançamento NF |

**Arquivo ou Código do Script: FS.2016.08\_03 -** FLANVINCULO\_BKP  - Tabela de backup de lançamento de crédito de adiantamento vinculado com ambos lançamentos com retenção 

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | PKFLANVINCULO\_BKP: CODCOLIGADA + IDLAN + IDLANREL + TIPOREL |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo** | **Tipo** | **Tamanho** | **Mandatório** | **Descrição** | **Título** |
| CODCOLIGADA | Inteiro |  | Sim (x ) Não (  ) | Coligada dos lançamentos | Coligada dos lançamentos |
| IDLAN | Inteiro |  | Sim (x) Não ( ) | ID do lançamento origem | ID do lançamento origem |
| IDLANREL | Inteiro |  | Sim (X) Não () | ID do lançamento relacionado | ID do lançamento relacionado |
| TIPOREL | Inteiro |  | Sim (x ) Não ( ) | Tipo do relacionamento | Tipo do relacionamento |
| VALORVINCULO | Decimal |  | Sim (  ) Não (X  ) | Valor Vínculo | Id Item Baixa Lançamento Nota Fiscal Vinculada |
| VALORORIGINALCREDITO | Decimal |  | Sim (  ) Não (X ) | Valor Original do Crédito Adiantamento | Valor Original do Crédito Adiantamento |
| VALORVINCULADOCREDITO | Decimal |  | Sim (  ) Não (X ) | Valor Vinculado Crédito de Adiantamento | Valor Vinculado Crédito de Adiantamento |

**Arquivo ou Código do Script: FS.2016.08\_03 -** FRELLAN - Tabela de relacionado entre os lançamentos financeiros vinculados

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | PKFRELLAN: CODCOLIGADA + IDLAN + IDLANREL + TIPOREL |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo** | **Tipo** | **Tamanho** | **Mandatório** | **Descrição** | **Título** |
| VALORRETENCAO | Decimal |  | Sim (  ) Não (X  ) | Valor da Retenção Vinculada | Valor da Retenção Vinculada |

**Arquivo ou Código do Script: FS.2016.08\_03 -** FRELLANHST - Tabela de histórico do relacionado entre os lançamentos financeiros vinculados

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | PKFRELLANHST: CODCOLIGADA + IDHISTORICO + IDLAN + IDLANREL + TIPOREL |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo** | **Tipo** | **Tamanho** | **Mandatório** | **Descrição** | **Título** |
| VALORRETENCAO | Decimal |  | Sim (  ) Não (X  ) | Valor da Retenção Vinculada | Valor da Retenção Vinculada |

**Arquivo ou Código do Script: FS.2016.08\_03 -** FTRBLAN- Tabela de tributo do lançamento financeiro

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | PKFTRBLAN: CODCOLIGADA + IDTRBLAN |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo** | **Tipo** | **Tamanho** | **Mandatório** | **Descrição** | **Título** |
| BASECALCULOORIGINAL | Decimal |  | Sim (  ) Não (X  ) | Base Cálculo Original Tributo | Base Cálculo Original Tributo |

**Arquivo ou Código do Script: FS.2016.08\_03 -** FTRBLANHST - Tabela de histórico do tributo do lançamento financeiro

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | PKFTRBLANHST: CODCOLIGADA + IDHISTORICO + IDTRBLAN |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo** | **Tipo** | **Tamanho** | **Mandatório** | **Descrição** | **Título** |
| BASECALCULOORIGINAL | Decimal |  | Sim (  ) Não (X  ) | Base Cálculo Original Tributo | Base Cálculo Original Tributo |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
