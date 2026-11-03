---
article_id: 1500002047182
category: LEGAIS - BLOCO H/MATR460
content_hash: ecc44ed85ffa470d7830d65498a77f3d9c260a67240b38683b83ad54a0cd1a46
fetched_at: '2026-06-28T22:42:15.109985+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Custo em
  Estoque DE/EM terceiros negativo/divergente na impressão do P7
type: support-article
updated_at: '2021-11-11T19:37:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002047182-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Custo-em-Estoque-DE-EM-terceiros-negativo-divergente-na-impress%C3%A3o-do-P7
---

**Dúvida**Ao emitir o relatório Inventário Mod. 7 (P7) vejo que o Custo em poder de/em terceiros está incorreto. Como diagnosticar de onde está surgindo essa impressão errada?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17

**Solução**

O Custo no P7 é algo bem importante de se avaliar, principalmente quando se trata de fechamento ou na entrega do Bloco H. Neste artigo daremos algumas dicas de como identificar o porquê o custo no MATR460 pode ser impresso de forma incorreta.

O relatório de Inventário Mod. 7 é um inventário de extrema complexidade no que diz respeito às perguntas e aos parâmetros (SX6) que podem mudar a impressão dele. Como esse ponto é de extrema importância, vamos listar as documentações que abordam estes dois assuntos abaixo para um melhor entendimento antes de partirmos para possíveis análises de divergências de saldo no P7:

- [MP - SIGAEST - Parâmetros (SX6) relacionados ao relatório MATR460 - Registro de Inventário Modelo 7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901)

- [MP - SIGAEST - Perguntas do relatório MATR460 (Inventário Modelo 7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001540542)

Recomendamos fortemente a leitura destas duas documentações para melhor entendimento do real significado das perguntas e dos parâmetros SX6 relacionados a este relatório e como elas influenciam nos dados impresso

**Análise de Custo incorreto em estoque De/Em terceiros no P7**

É importante enfatizar que é recomendável o relatório P7 ser emitido com a "Data Fechamento"= Data da última Virada de Saldos, pois desta forma o relatório poderá (com alguns critérios) ser comparado ao B9\_DATA (Data do Fechamento), B9\_QINI (Saldo na data do fechamento) e B9\_VINI1 (Custo na data do fechamento) caso trabalhe com o parâmetro MV\_CONTERC habilitado. Com isso, segue abaixo maneiras de se diagnosticar o problema:

**➣** É muito importante avaliar se possui o parâmetro MV\_CONTERC habilitado. Se sim, avaliar qual o armazém de terceiros delegado no parâmetro MV\_ALMTERC e se todas a sua base está plenamente configurada para este parâmetro funcionar corretamente. **[Clique aqui e veja as condições em que este parâmetro pode ser utilizado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020343832-MP-SIGAEST-Funcionalidade-dos-par%C3%A2metros-MV-CONTERC-e-MV-ALMTERC-para-controle-do-poder-EM-terceiros)**

**➣** Verifique se nos movimentos que controlou poder de terceiros, o campo valor do campo **B6\_CUSTO1**. Se estiver zerado provavelmente o movimento que alimentou essa linha na SB6 (D1\_CUSTO E/ou D2\_CUSTO1) utilizava TES que **não** atualizava estoque. Neste caso, avaliar internamente se há possibilidade de estorno/alteração até mesmo solicitando o apoio de um analista in loco;

**➣** Se utilizar o parâmetro MV\_CONTERC = S, emitir um Kardex do mês corrente do armazém de terceiros (MV\_ALMTERC) para fins de comparação de saldo e custo com o P7;

**➣**Validar o parâmetro **[MV\_R460TPC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001352161)**, que tem justamente a finalidade de tratar custo em terceiros no P7.

Se mesmo com estas validações não identificar de onde está gerando determinado custo no P7, recomendamos que acione ao Suporte Técnico com evidências e o embasamento de análise para auxílio no diagnóstico e proposição de resolução do problema.

**Saiba mais:**

*[MP - SIGAEST - MATR460 (P7) - Saldo físico em Estoque De/Em Terceiros negativo/divergente. O que fazer?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002037442)*

*[MP - SIGAEST - MATR460 - Custo em Estoque Próprio negativo/divergente na impressão do P7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060560754)*

*[Clique aqui e veja mais artigos sobre Bloco H/MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)*
