---
article_id: 32567137861015
category: Originação de Grãos (OG)
content_hash: 96073c634276947d1d51649f9424a7d9dd15b45a8d0d37fcb42e00640c83aa18
fetched_at: '2026-06-28T22:45:42.997138+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para Manipular dados do Pedido
  de Compra da Comissão
type: support-article
updated_at: '2025-06-13T21:16:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32567137861015-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-Manipular-dados-do-Pedido-de-Compra-da-Comiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32567137844631) Tempo aproximado para leitura: **00:02:25 min** **Dúvida**O Ponto de Entrada para manipular dados do **Pedido de Compra da Comissão**. Como funciona?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGC120 | Painel Financeiro | |
| **Ponto de Entrada:** | OGC120CVLD |
| **País(es):** | Todos |
| **Pacote:** | 12.1.23 |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Localização:** | Ao salvar a vinculação ou remoção do vínculo entre Previsão Financeira e Recebimento Antecipado |
| **Programa Fonte:** | OGC120CVLD |
| **Função:** | Permitir validar os dados antes de efetivar o vínculo/desvinculo da Previsão Financeira e Recebimento Antecipado (RA). |
| Parâmetros: | | Nome | Tipo | Descrição | Obrigatório | | --- | --- | --- | --- | | PARAMIXB[1] | Char | Ação realizada (1 - Vínculo, 2 - Desvinculo) | Sim | | PARAMIXB[2] | Array | Array com os dados da previsão financeira.  Exemplo:  {cFilial, cCodCTR, cItemPrev, cParcPrev, nVlrVinc} | Sim | | PARAMIXB[2] | Array | Array com os dados do Recebimento Antecipado (RA).  Exemplo:  { cTipoRA, cPrefixRA, cNumRA, cParcRA, cFilTitRA} | Sim | |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **lContinua** | Lógico | Indica se o processo de vínculação/desvinculação deve continuar.  .T. = Continua a ação de vincular/desvincular.  .F. = Cancela a ação de vínculo/desvínculo. | |

**Exemplo:**

`User Function OGC120CVLD()`

`Local lAcao    := PARAMIXB[1]`

`Local aDadosPR := aClone(PARAMIXB[2])`

`Local aDadosRA := aClone(PARAMIXB[3])`

`Local lRet     := .T.`

`If lAcao == "1"  //Ação de vincular`

`If aDadosPR[05] > 10000`

`MsgInfo("Somente é possível vincular até 10.000.")`

`lRet := .F.`

`EndIf`

`EndIf`

`Return lRet`
