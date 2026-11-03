---
article_id: 360060560754
category: LEGAIS - BLOCO H/MATR460
content_hash: 532c7254ca14b30616ec5c752f8608681c1f22e21db8310ac69ca422a40135e4
fetched_at: '2026-06-28T22:42:15.115687+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Custo em
  Estoque Próprio negativo/divergente na impressão do P7
type: support-article
updated_at: '2021-06-14T14:30:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060560754-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Custo-em-Estoque-Pr%C3%B3prio-negativo-divergente-na-impress%C3%A3o-do-P7
---

**Dúvida**Ao emitir o P7 verifiquei que no estoque próprio existem produtos com custo incorreto. Como identificar e corrigir o problema?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17

**Solução**O Custo no P7 é algo bem importante de se avaliar, principalmente quando se trata de fechamento ou na entrega do Bloco H. Neste artigo daremos algumas dicas de como identificar o porquê o custo no MATR460 pode ser impresso de forma incorreta.

O relatório de Inventário Mod. 7 é um inventário de extrema complexidade no que diz respeito às perguntas e aos parâmetros (SX6) que podem mudar a impressão dele. Como esse ponto é de extrema importância, vamos listar as documentações que abordam estes dois assuntos abaixo para um melhor entendimento antes de partirmos para possíveis análises de divergências de saldo no P7:

- [MP - SIGAEST - Parâmetros (SX6) relacionados ao relatório MATR460 - Registro de Inventário Modelo 7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901)

- [MP - SIGAEST - Perguntas do relatório MATR460 (Inventário Modelo 7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001540542)

Recomendamos fortemente a leitura destas duas documentações para melhor entendimento do real significado das perguntas e dos parâmetros SX6 relacionados a este relatório e como elas influenciam nos dados impressos.

**Análise de Custo incorreto no P7**

É importante enfatizar que é recomendável o relatório P7 ser emitido com a "Data Fechamento"= Data da última Virada de Saldos, pois desta forma o relatório fará uma busca em B9\_DATA (Data do Fechamento), B9\_QINI (Saldo na data do fechamento) e B9\_VINI1 (Custo na data do fechamento). Com isso, segue abaixo maneiras de se diagnosticar o problema:

**➣** Separar um produto para melhor assertividade nas análises;

**➣** Atentar-se à tela das perguntas, por exemplo: "**Prods c/ Saldo Neg?**", " **Prods c/ Saldo Zerado?**", "**Lista Custo Zerado?**". Estas perguntas podem fatalmente gerar impressão diferente do desejado.

**Exemplo de possível "impressão incorreta" no MATR460:**  Se parametrizar o campo **"Prods com Saldo Zerado?" = Não**, se um produto A tiver armazém 01 e 02 e, por algum motivo no armazém 01 tiver saldo físico zerado, **a impressão ignorará o custo que estiver atrelado ao armazém 01**. Ele só irá trazer o custo e quantidade do armazém 02.

**➣** Avaliar se na tabela SB9 -> B9\_VINI1 no(s) armazém(ns) em questão o custo está de fato incorreto;

**➣** Emitir um Kardex (MATR900) do mesmo produto filtrando o mês em que o último dia bata com a "Data de Fechamento" do P7 para melhor entendimento de qual foi o saldo final do produto na data em que foi feita a Virada de Saldos.

         EX: Se o fechamento foi em 31/12/2020, emitir o Kardex de 01/12/2020 à 31/12/2020.

**➣** Checar se o custo entre Kardex, MATR460 e SB9 tem alguma similaridade;

**➣** Se ocorrer diferença apenas no MATR460 com relação aos dois, avalie se não há nenhuma personalização/customização neste relatório;

**➣** Caso esteja 100% padrão, considere a possibilidade de atualizar o seu ambiente do Estoque/Custos:

***Pacotes acumulados Estoque/Custos:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571) **|** 12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640) **|** 12.1.23- [Clique aqui.](https://suporte.totvs.com/portal/p/10098/download#detail/748747)

Caso com estes passos acima não for possível diagnosticar/resolver o problema, recomendamos que solicite o apoio da nossa Equipe de Suporte Técnico do Estoque por meio do portal de atendimento, evidenciando as análises previamente efetuadas.

Recomendamos que evidencie filtrando um produto os relatórios de Kardex, Posição de Estoque e P7, além das tabelas SB2, SB9, SX6 em formato .DTC.

**Saiba mais:**

[*MP - SIGAEST - MATR460 (P7) - Saldo físico em Estoque Próprio negativo/divergente. O que fazer?*](https://www.google.com/url?q=https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001933381&sa=D&ust=1611600079426000&usg=AFQjCNF5dPuIkqgkPZ-6TrAp2s2yNehJTw)

*[Clique aqui e veja mais artigos sobre Bloco H/MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)*
