---
article_id: 1500002037442
category: LEGAIS - BLOCO H/MATR460
content_hash: 68026f23a9fefa3b239d3846a4aa3aadd9221a205264c40a06be6dc2214d8a08
fetched_at: '2026-06-28T22:42:15.089377+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 (P7) - Saldo
  físico em Estoque De/Em Terceiros negativo/divergente. O que fazer?
type: support-article
updated_at: '2021-06-24T13:20:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002037442-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-P7-Saldo-f%C3%ADsico-em-Estoque-De-Em-Terceiros-negativo-divergente-O-que-fazer
---

**Dúvida**Ao emitir o relatório de Inventário Mod. 7 (MATR460) verifiquei que meu saldo físico em de/em terceiros está negativo/divergente. Como posso diagnosticar este saldo incorreto?  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O relatório de Inventário Mod. 7 é um inventário de extrema complexidade no que diz respeito às perguntas e aos parâmetros (SX6) que podem mudar a impressão dele. Como esse ponto é de extrema importância, vamos listar as documentações que abordam estes dois assuntos abaixo para um melhor entendimento antes de partirmos para possíveis análises de divergências de saldo no P7:

- [MP - SIGAEST - Parâmetros (SX6) relacionados ao relatório MATR460 - Registro de Inventário Modelo 7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901)

- [MP - SIGAEST - Perguntas do relatório MATR460 (Inventário Modelo 7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001540542)

Recomendamos fortemente a leitura destas duas documentações para melhor entendimento do real significado das perguntas e dos parâmetros SX6 relacionados a este relatório e como elas influenciam nos dados impressos.

**Saldo negativo ou divergente no Estoque De/Em Terceiros:**

**➣** Selecionar a "Data de Fechamento" = Data da última Virada de Saldos da SB9;

➣ Selecionar o campo **"Saldo em Poder de 3°s?" = Sim**;

➣ Separar um produto para analisar, assim obterá maior assertividade na análise;

**➣** Atentar-se à tela das perguntas, por exemplo: "**Prods c/ Saldo Neg?**", " **Prods c/ Saldo Zerado?**", "**Lista Custo Zerado?**". Estas perguntas podem fatalmente gerar impressão diferente do desejado.

**Exemplo de possível "impressão incorreta" no MATR460:**  Se parametrizar o campo **"Prods com Saldo Zerado?" = Não**, se um produto A tiver armazém 01 e 02 e, por algum motivo no armazém 01 tiver saldo físico zerado, **a impressão ignorará o custo que estiver atrelado ao armazém 01**. Ele só irá trazer o custo e quantidade do armazém 02.

**➣** Validar se utiliza o parâmetro MV\_CONTERC em conjunto ao MV\_ALMTERC. Para entender melhor as condições e utilidade destes parâmetros, **[clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020343832-MP-SIGAEST-Funcionalidade-dos-par%C3%A2metros-MV-CONTERC-e-MV-ALMTERC-para-controle-do-poder-EM-terceiros)**

**➣** Avalie se o saldo em poder de/em terceiros é coerente utilizando o Relatório MATR480 (Relatório de controle de poder de/em terceiros). Nele é possível filtrar o produto e um período extenso para entender, na coluna "**Saldo**", qual o saldo de poder de/em terceiros para o produto;

**➣** Validar o conteúdo do parâmetro **MV\_SDTESN3** para checar se o saldo está coerente com as remessas/devoluções;

**➣** Se por padrão **não** usar TES que **não** atualiza estoque, deixe o parâmetro MV\_SDTESN3 = 0.

**➣** Se nos movimentos de controle de poder de terceiros costumar utilizar TES que não atualiza estoque (pode-se diagnosticar pela tabela SB6 -> B6\_ESTOQUE. N é quando o movimento usou TES que não atualiza estoque e S é quando o movimento utilizou TES que atualiza estoque), validar a utilização do MV\_SDTESN3 para considerar na impressão movimentos com TES que não atualizam estoque.

**➣** Executar à rotina Refaz Poder de Terceiros (MATA216) para o produto em questão que estiver com a divergência e checar se os saldos nos relatórios MATR480 e MATR460 se equalizam.

Se mesmo com as validações acima identificar que de fato o P7 é que está trazendo um saldo em poder de terceiros incorreto, acione o time de Suporte Técnico do Módulo de Estoque/Custos com as evidências necessárias para auxílio na identificação do problema.

**Saiba mais:**

*[MP - SIGAEST - Dicas de Análise dos Saldos no Relatório MATR460 (P7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061829673)*

*[MP - SIGAEST - Perguntas do relatório MATR460 (Inventário Modelo 7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001540542)*

*[MP - SIGAEST - MATR460 (P7) - Saldo em Estoque Próprio negativo/divergente. O que fazer?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001933381)*

*[Clique aqui e veja mais artigos sobre Bloco H/MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)*
