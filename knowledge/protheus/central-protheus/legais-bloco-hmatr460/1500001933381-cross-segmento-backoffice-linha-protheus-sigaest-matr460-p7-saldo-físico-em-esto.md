---
article_id: 1500001933381
category: LEGAIS - BLOCO H/MATR460
content_hash: 979eaecea6a8dc2bd5a2a8f49d7494937a83f633c5f239bc06f47993192da65b
fetched_at: '2026-06-28T22:42:14.998414+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  MATR460 (P7) - Saldo
  físico em Estoque Próprio negativo/divergente. O que fazer?
type: support-article
updated_at: '2021-06-24T13:19:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001933381-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-P7-Saldo-f%C3%ADsico-em-Estoque-Pr%C3%B3prio-negativo-divergente-O-que-fazer
---

**Dúvida**Ao emitir o relatório de Inventário Mod. 7 (MATR460) verifico que meu saldo físico em Estoque Próprio está negativo/divergente. Como posso diagnosticar este saldo incorreto?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**O relatório de Inventário Mod. 7 é um inventário de extrema complexidade no que diz respeito às perguntas e aos parâmetros (SX6) que podem mudar a impressão dele. Como esse ponto é de extrema importância, vamos listar as documentações que abordam estes dois assuntos abaixo para um melhor entendimento antes de partirmos para possíveis análises de divergências de saldo no P7:

- [MP - SIGAEST - Parâmetros (SX6) relacionados ao relatório MATR460 - Registro de Inventário Modelo 7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901)

- [MP - SIGAEST - Perguntas do relatório MATR460 (Inventário Modelo 7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001540542)

Recomendamos fortemente a leitura destas duas documentações para melhor entendimento do real significado das perguntas e dos parâmetros SX6 relacionados a este relatório e como elas influenciam nos dados impressos.

**Saldo negativo ou divergente no Estoque Próprio**

É importante enfatizar que é recomendável o relatório P7 ser emitido com a "Data Fechamento"= Data da última Virada de Saldos, pois desta forma o relatório fará uma busca em B9\_DATA (Data do Fechamento), B9\_QINI (Saldo na data do fechamento) e B9\_VINI1 (Custo na data do fechamento). Com isso, segue abaixo maneiras de se diagnosticar o problema:

**➣** Parametrizar a pergunta **"Saldo em Poder de 3°s?" = Não**, para garantir que não tenha algum composto do saldo de/em terceiro influenciando no saldo em estoque próprio;

**➣** Caso parametrizar o "Saldo em Poder de 3°s = Não" e o saldo ficar correto, provavelmente o problema esteja relacionado ao uso do parâmetro **MV\_SDTESN3.** [Clique aqui e entenda melhor a utilidade dele no P7.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060289014)

**➣** Separe um produto para analisar o seu saldo no P7, em seguida, basta emitir um Kardex (MATR900) do mesmo produto filtrando o mês em que o último dia bata com a "Data de Fechamento" do P7 para melhor entendimento de qual foi o saldo final do produto na data em que foi feita a Virada de Saldos.

         EX: Se o fechamento foi em 31/12/2020, emitir o Kardex de 01/12/2020 à 31/12/2020.

**➣** Analisar na tabela SB9 se o saldo no(s) armazém(ns) bate(m) com o que está sendo impresso no P7 e MATR900 - **Este ponto é importante para identificar se há ou não problema no MATR460.**

**➣** Se o saldo da SB9 bater com o P7 (filtrando com a data correta do fechamento), provavelmente o problema não seja nele;

Caso mesmo com essas análises não conseguir diagnosticar de onde o saldo P7 está imprimindo a quantidade incorreta, recomendamos que acione ao nosso time de Suporte Técnico do estoque evidenciando os relatórios e bases de análises previamente feitas.

**Saiba mais:**

*[MP - SIGAEST - Dicas de Análise dos Saldos no Relatório MATR460 (P7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061829673)*

*[MP - SIGAEST - MATR460 (P7) - Saldo em Estoque De/Em Terceiros negativo/divergente. O que fazer?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002037442)*

*[Clique aqui e veja mais artigos sobre MATR460 (P7)/Bloco H no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)*
