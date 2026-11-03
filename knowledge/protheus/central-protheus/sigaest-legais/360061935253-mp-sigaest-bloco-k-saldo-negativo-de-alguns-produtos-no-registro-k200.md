---
article_id: 360061935253
category: SIGAEST - LEGAIS
content_hash: bd95daa81d5b42c0cf6c40f46ddf8d254c74505c4c9fe4c964453568d1f31a28
fetched_at: '2026-06-28T22:38:51.922864+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: MP - SIGAEST - Bloco K - Saldo negativo de alguns produtos no Registro K200
type: support-article
updated_at: '2021-07-19T13:58:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061935253-MP-SIGAEST-Bloco-K-Saldo-negativo-de-alguns-produtos-no-Registro-K200
---

**Dúvida**

Ao gerar o SPED com Bloco K, percebo que alguns produtos estão com saldo negativo no registro K200. Porém, nas tabelas SB2 e SB9 não estão com saldo negativo. O que fazer para resolver?

**Ambiente**

Microsiga Protheus - Estoque - A partir da versão 12.1.17

**Solução**

A premissa inicial para análise do saldo negativo é que os fontes responsáveis pela correta geração do SPED estejam atualizados. Por este motivo, recomendamos que aplique a Expedição Contínua do módulo de Estoque/Custos e também de Livros Fiscais. Segue abaixo:

***Pacotes acumulados Estoque/Custos:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571) **|** 12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640) **|** 12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/748747)

***Pacotes acumulados Livros Fiscais:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/956585) **|** 12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/805589) **|** 12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/770598)

**Observação**: Sempre atualizar primeiramente em ambiente de homologação.

Saldo negativo no Registro K200 pode ter relação com o último saldo antes do fechamento. Vamos listar abaixo alguns caminhos que podem ser trilhados para identificação e correção do problema.

**Separando um produto que está com a inconsistência e analisando o Kardex**

A melhor maneira de analisar é separando um específico produto que no K200 está com valor negativo e emitir o Kardex (MATR900) dele do mês ao qual está apurando o SPED. Com isso, compare-o com a SB9 do último (ou últimos) períodos pois pode ser que tenha sido algum fechamento anterior incorreto. Se de fato houver algum fechamento anterior incorreto, a alternativa seria a reabertura do período de estoque para fazer o ajuste do saldo antes de fechar novamente. A TOTVS recomenda a solicitação de um analista in loco para acompanhamento da reabertura de Estoque. Para mais informações sobre, **[clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=235593432).**

**Caso ainda não tenha efetuado a virada de Saldos**

Caso ainda não tenha efetuado a virada de Saldos e identificar via Kardex que o saldo acabou negativando, uma alternativa é efetuar o ajuste por meio de Inventário ([veja mais sobre inventário clicando aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020799592-MP-SIGAEST-Processo-de-Invent%C3%A1rio-Conceito-Exemplo-e-D%C3%BAvidas)).

Após isso, basta gerar o SPED Fiscal novamente que o registro K200 estará com o Estoque Escriturado conforme o saldo desejado.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
