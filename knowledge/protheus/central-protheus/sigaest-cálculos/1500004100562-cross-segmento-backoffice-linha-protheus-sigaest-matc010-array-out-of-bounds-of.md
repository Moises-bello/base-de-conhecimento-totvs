---
article_id: 1500004100562
category: SIGAEST - CÁLCULOS
content_hash: c1a8afcd4f3cacd480f82b7c0a1885616210b582fdc1ef011281ff320000e355
fetched_at: '2026-06-28T22:39:04.158758+00:00'
product: protheus
section_id: 1500001550082
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATC010 - array out
  of bounds of on PLANILHA(MATC010.PRW)
type: support-article
updated_at: '2025-03-12T12:24:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004100562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATC010-array-out-of-bounds-of-on-PLANILHA-MATC010-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503274212375) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**

Ao clicar no botão "Planilha" dentro da rotina Formação de Preços - MATC010 - a planilha não abre e apresenta-se o error.log abaixo:

"*THREAD ERROR - array out of bounds [1] of [0] on PLANILHA(MATC010.PRW)*"

Como corrigir este problema?

**Ambiente**Microsiga Protheus – Estoque/Custos– A partir da versão 11.80  
  
**Solução**

Para a correção do problema, siga os passos abaixo:

1 - Ative o parâmetro **MV\_REVPLAN**, deixando com conteúdo = .T.

2 – Faça o download do arquivo SCO.dtc anexado ao final do artigo;

3 – Descompacte o arquivo SCO.dtc na pasta System;

OBS: Antes de efetuar o append, caso necessário, faça o ajuste do campo filial para que se adapte ao usado em sua empresa.

4 – Abra, via APSDU, a tabela SCO e faça o append (importação) do arquivo  SCO.dtc. Desta forma os registros da tabela SCO ficarão conforme imagem abaixo.

![TABELA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503261710103)

OBS: **É importante que seja feita a correção do campo da filial conforme o padrão usado na empresa.**

Após isso, ao clicar na Planilha dentro da Formação de Preços não ocorrerá mais o Error.log

**Saiba mais:**

*[MP - SIGAEST - Rotina Formação de Preço (MATC010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022184251-MP-SIGAEST-Rotina-Forma%C3%A7%C3%A3o-de-Pre%C3%A7o-MATC010-)*

*[Clique aqui e veja mais artigos sobre Cálculos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199493-SIGAEST-C%C3%81LCULOS)*
