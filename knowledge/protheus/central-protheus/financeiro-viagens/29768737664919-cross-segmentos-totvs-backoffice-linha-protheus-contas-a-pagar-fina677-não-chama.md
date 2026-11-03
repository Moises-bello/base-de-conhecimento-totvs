---
article_id: 29768737664919
category: Financeiro - Viagens
content_hash: 512c006c64f344b5b49c9f141dd705564db21ca828999b729a14694fde8c31f3
fetched_at: '2026-06-28T22:38:21.315236+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - TOTVS BackOffice (Linha Protheus) - Contas a Pagar - FINA677
  - Não chama o LP 510 e apresenta lançamentos contabeis online
type: support-article
updated_at: '2025-02-05T13:17:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29768737664919-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-Contas-a-Pagar-FINA677-N%C3%A3o-chama-o-LP-510-e-apresenta-lan%C3%A7amentos-contabeis-online
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29768737643031) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a contabilização das prestações de contas ao liberar financeiro, não está chamando o LP 510 - Inclusão de Titulos a Pagar e não contabiliza online registros oriundos da Prestação de Contas

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois os LP´s responsáveis pela contabilização da prestação de contas, deve ser chamado pelos LP´s abaixo:

A contabilização da prestação de contas possui lançamentos específicos para a contabilização das despesas, sendo eles:

**8B3 - Item da Prestação de Contas/Despesa**  
**8B4 - Estorno do Item da Prestação de Contas/Despesa**  
**8B5 - Cabeçalho da Prestação de Contas\***  
**8B6 - Estorno do Cabeçalho da Prestação de Contas\***  
\*Os totalizadores da prestação de contas são gravados na tabela **FLF - Cabeçalho da Prestação de Contas**

Para a contabilização off-line da prestação de contas: **[LP 8B3 e 8B5 - Contabilização da Prestação de Contas Off-line](https://tdn.totvs.com/pages/releaseview.action?pageId=856944140)**

**Solução**Necessário configurar os LP´s de Prestação de contas, segue exemplo abaixo:

Utilizado nas rotinas**Prestação de contas (FINA677)** e na **Contabilização Offline (CTBAFIN)**

**8B3 - Prestação de Contas**

**Exemplo:**

|  |  |
| --- | --- |
| **CT5\_FILIAL** | D MG 01 |
| **CT5\_LANPAD** | 8B3 |
| **CT5\_STATUS** | 1 |
| **CT5\_DESC** | LP8B3 - PRESTACAO DE CONTAS |
| **CT5\_DC** | 3 |
| **CT5\_DEBITO** | 001 |
| **CT5\_CREDIT** | 002 |
| **CT5\_MOEDAS** | 12222 |
| **CT5\_VLR01** | FLE->FLE\_VALREE |
| **CT5\_HIST** | LP8B3 - PRESTACAO DE CONTAS |

Importante

1) Pode ser utilizado o campo **FLE\_QUANT** para retornar a quantidade relacionada a Despesa.

2) Formas de utilizar esse lançamento padrão: [LP 8B3 e 8B5 - Contabilização da Prestação de Contas Off-line](https://tdn.totvs.com/pages/viewpage.action?pageId=856944140)

**8B4 - Estorno da Prestação de Contas**

**Exemplo:**

|  |  |
| --- | --- |
| **CT5\_FILIAL** | D MG 01 |
| **CT5\_LANPAD** | 8B4 |
| **CT5\_STATUS** | 1 |
| **CT5\_DESC** | LP8B4 - ESTORNO PRESTACAO DE CONTAS |
| **CT5\_DC** | 3 |
| **CT5\_DEBITO** | 001 |
| **CT5\_CREDIT** | 002 |
| **CT5\_MOEDAS** | 12222 |
| **CT5\_VLR01** | FLE->FLE\_VALREE |
| **CT5\_HIST** | LP8B3 - ESTORNO PRESTACAO DE CONTAS |

Importante

Esse lançamento padrão, somente deve ser utilizado na **Contabilização Online**.

**8B5 - Cabeçalho Prestação de Contas**

**Exemplo:**

|  |  |
| --- | --- |
| **CT5\_FILIAL** | D MG 01 |
| **CT5\_LANPAD** | 8B5 |
| **CT5\_STATUS** | 1 |
| **CT5\_DESC** | LP8B5 - CABECALHO PREST CONTAS |
| **CT5\_DC** | 3 |
| **CT5\_DEBITO** | 001 |
| **CT5\_CREDIT** | 002 |
| **CT5\_MOEDAS** | 12222 |
| **CT5\_VLR01** | FLF->FLF\_TVLRE1 |
| **CT5\_HIST** | LP8B5 - CABECALHO PREST CONTAS |
| **CT5\_HAGLUT** |  |

Importante

Formas de utilizar esse lançamento padrão: [LP 8B3 e 8B5 - Contabilização da Prestação de Contas Off-line](https://tdn.totvs.com/pages/viewpage.action?pageId=856944140)

**8B6 - Estorno do Cabeçalho  Prestação de Contas**

**Exemplo:**

|  |  |
| --- | --- |
| **CT5\_FILIAL** | D MG 01 |
| **CT5\_LANPAD** | 8B6 |
| **CT5\_STATUS** | 1 |
| **CT5\_DESC** | LP8B5 - ESTORNO CABECALHO PREST CONTAS |
| **CT5\_DC** | 3 |
| **CT5\_DEBITO** | 001 |
| **CT5\_CREDIT** | 002 |
| **CT5\_MOEDAS** | 12222 |
| **CT5\_VLR01** | FLF->FLF\_TVLRE1 |
| **CT5\_HIST** | LP8B6 - ESTORNO CABECALHO PREST CONTAS |

Importante

Esse lançamento padrão, somente deve ser utilizado na **Contabilização Online**.

Importante

Caso a prestação de contas seja estornada e seu LP (8B4 e 8B6) esteja desativado, o campo FLE\_LA continuará com seu conteúdo igual a "S", para que a contabilização da prestação de contas não seja duplicada.

Neste caso é possível a utilização do parâmetro MV\_CTBAPLA conforme documentações abaixo,  para que a contabilidade seja corrigida e a *flag*da tabela limpa.

[MV\_CTBAPLA - Limpeza do Flag de Contabilização](https://tdn.totvs.com/pages/viewpage.action?pageId=6068578)

[SIGACTB - Diversos -- 24238](https://tdn.totvs.com/display/LMPESP/SIGACTB+-+Diversos+--+24238)
