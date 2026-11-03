---
article_id: 360018060952
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b7b3cb3cd807dbfcaa9d5bf90fc5c8a4ba03b1087c28a6fc649f87fbfeb40088
fetched_at: '2026-06-28T22:38:39.697612+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - BackOffice Protheus - SIGAFAT - Como customizar a análise
  de crédito de Cliente (MATA450A)?
type: support-article
updated_at: '2025-03-11T11:09:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018060952-Cross-Segmentos-BackOffice-Protheus-SIGAFAT-Como-customizar-a-an%C3%A1lise-de-cr%C3%A9dito-de-Cliente-MATA450A
---

Exemplo:

```
Programa Fonte: .PRW
```

**Sintaxe**

```
MAAVCRED ( < UPAR> ) --> URET
```

**Parâmetros**

|  |  |  |  |
| --- | --- | --- | --- |
| **Nome** | **Tipo** | **Descrição** | **Obrigatório** |
| UPAR | Vetor | Contém os dados do Pedido de Venda | Sim |

**Retorno**

|  |  |  |  |
| --- | --- | --- | --- |
| **Nome** | **Tipo** | **Descrição** | **Obrigatório** |
| URET | Qualquer | Retorna um valor do tipo carácter ou tipo lógico.  Exemplo retorno de carácter: Retorna o código de bloqueio ou, caso não tenha nenhum bloqueio, retorna contéudo em <branco>.  Exemplo retorno de lógico: retorna .F. para bloquear ou retorna .T. para liberar (Caso utilize o retorno lógico, o bloquei automaticamente será o "01") | X |

* **Retorno Lógico:**

  + `.T.` - Pedido liberado
  + `.F.` - Pedido bloqueado (código "01" de bloqueio será aplicado automaticamente)
* **Retorno Caractere:**

  + Código do motivo de bloqueio ou  caso não haja bloqueio.

**Exemplo de Implementação**

`User Function MAAVCRED()`

`Local cCodCli   := ParamIxb[1]``//Código do Cliente`

`Local cLoja     := ParamIxb[2]``//Código da loja`

`Local nValor    := ParamIxb[3]``//Preço da Venda`

`Local nMoeda    := ParamIxb[4]``//Moeda`

`Local lPedido   := ParamIxb[5]``//Inclusão de pedido de venda`

`Local xReturn   := NIL``//Variável de retorno`

`If cCodcli ==``"000001"` `.And. cLoja =``'01'` `//Caso for o cliente e Loja for igual a 000001 e 01.`

`xReturn :=``"05"` `// Bloqueio Manual/Estorno.`

`ElseIf nValor > 10000``//Caso o total do valor do pedido de venda exceder o limite (Limite de 10000).`

`xReturn :=``"09"` `//Liberação de Crédito Rejeitada.`

`ElseIf cCodcli ==``"000001"` `.And. cLoja ==``'99'` `//Caso contrario, realizar liberacao do credito.`

`xReturn := .T.``//Liberado`

`EndIf`

`Return (xReturn)`

  

Veja também a lista de Pontos de Entrada da rotina **MATA450A - Liberação de crédito cliente:**

**[Lista de Pontos de Entrada da rotina MATA450A - Análise de Crédito Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022359872-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Lista-de-Pontos-de-Entrada-da-rotina-MATA450A-An%C3%A1lise-de-Cr%C3%A9dito-de-Cliente)**

**Saiba mais:**

**[Configurações para bloqueio de crédito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017748031-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Configura%C3%A7%C3%B5es-para-bloqueio-de-cr%C3%A9dito?source=search)**

**[Usabilidade do botão rejeitar na análise de crédito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009773842-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Usabilidade-do-bot%C3%A3o-rejeitar-na-an%C3%A1lise-de-cr%C3%A9dito)**

**[Comportamento do parâmetro MV\_AVALCRD no Pedido de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016176611-MP-FAT-Comportamento-do-par%C3%A2metro-MV-AVALCRD-no-Pedido-de-Vendas)**

**[Como identificar a causa de o Pedido de Venda ter sido liberado/bloqueado por Crédito "indevidamente"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001428228-MP-FAT-Como-identificar-a-causa-de-o-Pedido-de-Venda-ter-sido-liberado-bloqueado-por-Cr%C3%A9dito-indevidamente-)**
