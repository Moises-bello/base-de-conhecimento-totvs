---
article_id: 4440959975575
category: SIGAEST - CUSTOS
content_hash: 630d8946a588d0e9f4d97c4917e7a406d965635b2d0271254e380e67129b7da9
fetched_at: '2026-06-28T22:39:00.898794+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - É possível uma nota
  de saída não possuir custo (D2_CUSTO1 ) como bonificação?
type: support-article
updated_at: '2023-11-16T19:13:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4440959975575-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-uma-nota-de-sa%C3%ADda-n%C3%A3o-possuir-custo-D2-CUSTO1-como-bonifica%C3%A7%C3%A3o
---

**Dúvida**Existe a possibilidade de efetuar uma nota de saída, do tipo bonificação, para que a mesma não alimente o custo (D2\_CUSTO1) no documento de saída?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**A nota do tipo bonificação, pode ser utilizada hoje somente para um documento de entrada.

Para saber mais sobre esse processo, [**clique aqui**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087404):

Caso o cliente queira que o **custo de saída não seja alimentado (D2\_CUSTO1)**, somente é possível via Ponto de Entrada, disponibilizado no módulo de Faturamento.

Abaixo um exemplo, utilizando o **PE** **MA330D2**, qualquer dúvida, deve ser avaliada junto a um Desenvolvedor, visto que abaixo se trata apenas de um exemplo explicativo de como seria para que o custo de saída fosse zero para as 5 moedas.

|  |
| --- |
| **User Function MA330D2()**    **If SF4->F4\_BONIF == "S"**  **If RecLock("SD2",.F.)**  **SD2->D2\_CUSTO1 := 0.0**  **SD2->D2\_CUSTO2 := 0.0**  **SD2->D2\_CUSTO3 := 0.0**  **SD2->D2\_CUSTO4 := 0.0**  **SD2->D2\_CUSTO5 := 0.0**  **MsUnlock()**  **EndIf**  **EndIf**    **Return** |

Segue abaixo boletim:

[MP - FAT - Atualização do campo D2\_CUSTO1 ao utilizar TES que não atualiza estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021429372-MP-FAT-Atualiza%C3%A7%C3%A3o-do-campo-D2-CUSTO1-ao-utilizar-TES-que-n%C3%A3o-atualiza-estoque)

**Saiba mais**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es-#:~:text=Clique%20aqui%20e%20veja%20mais%20artigos%20sobre%20Custos%20no%20Estoque)
