---
article_id: 360027493372
category: Materiais - Compras (SIGACOM)
content_hash: c32ac33be904b862524f88b989b8c523dc6d9b4138c21a42773c3973776a02b8
fetched_at: '2026-06-28T22:41:10.070562+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - No Documento de Entrada,
  ao incluir uma nota de devolução, ocorre o Help: F4NAONOTA'
type: support-article
updated_at: '2023-07-31T17:37:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027493372-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-No-Documento-de-Entrada-ao-incluir-uma-nota-de-devolu%C3%A7%C3%A3o-ocorre-o-Help-F4NAONOTA
---

**Ocorrência**No Documento de Entrada, ao incluir uma nota de devolução, ocorre o Help: F4NAONOTA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027419431)

**Ambiente:**Protheus – Compras – A partir da versão 11.80  
  
**Solução:**

Existem 4 possibilidades que podem geram o help F4NAONOTA, são elas:

**1 -) Quando já foi feita uma devolução para a nota de saída em questão.**

Para verificar se já foi feita uma devolução para a nota de saída, siga os passos abaixo:

1. abra a tabela SD2 na APSDU

2. Vá em Útil -> Filtrar -> Selecione o campo D2\_DOC e coloque o número da nota de saída -> Incluir -> Ok

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16422285354775)

3. Localize os campos D2\_VALDEV e D2\_QTDEDEV

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16422425282839)

Se os campos estiverem zerados, significa que não foi realizada nenhuma devolução. Se estiverem preenchidos, significa que uma devolução já foi realizada.

**2-) Quando o tipo da nota de saída não é coerente com o tipo da nota de entrada (retorno)**

Quando a nota de saída for do tipo **B ( utilzando fornecedor )**, o documento de entrada a ser usado é o **Normal.** Para que o sistema busque o cadastro do fornecedor. 

Quando a nota de saída for do tipo **Normal** será utilizado um cliente, o documento de entrada deverá ser do tipo **Beneficiamento**. Para que o sistema busque o cadastro do cliente. 

**3-) Quando um dos TES utilizados na nota de saída não possui TES de devolução amarrado.**

Nesse cenário é sugerido que solicite a sua área fiscal que um TES de devolução seja amarrado no TES de saída.

**4-) O controle de poder de terceiros da TES de saída de ser correspondente à TES de entrada, conforme documentações abaixo.**

<https://tdn.totvs.com/pages/releaseview.action?pageId=285642640>

<https://tdn.totvs.com/display/public/PROT/Controle+de+Poder+de+Terceiros>

***Saiba mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar uma Devolução de Vendas na rotina de Documento de Entrada ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010638982-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-uma-Devolu%C3%A7%C3%A3o-de-Vendas-na-rotina-de-Documento-de-Entrada-?source=search)
