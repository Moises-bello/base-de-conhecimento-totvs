---
article_id: 360020482111
category: SIGAEST - CÁLCULOS
content_hash: 528836dce63e0078b69d34fffabe0d63cbd1e41513ae4f0c3a1a2e42fc766317
fetched_at: '2026-06-28T22:39:04.005466+00:00'
product: protheus
section_id: 1500001550082
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA290 - Consumo
  Médio e gravação da tabela de Demandas (SB3)
type: support-article
updated_at: '2026-05-27T12:14:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020482111-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA290-Consumo-M%C3%A9dio-e-grava%C3%A7%C3%A3o-da-tabela-de-Demandas-SB3
---

A rotina MATA290 no TOTVS Protheus gera indicadores de consumo, cálculo de lote econômico, ponto de pedido e classificação ABC, otimizando estoque. A tabela SB3 armazena dados dos últimos 12 meses, atualizados pela rotina Virada de Saldos (MATA280) se o parâmetro MV\_ZERADEM estiver ativo. Valores incorretos podem ocorrer por fechamentos retroativos ou ausência da virada. A rotina permite recalcular consumo mensal, mas deve ser executada para cada mês individualmente.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503094779671) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Como avaliar os valores gravados pela rotina MATA290 na tabela de Demandas SB3?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

A rotina de Consumo e Indicador (MATA290) auxilia a empresa na geração de indicadores importantes em cima do Consumo do seu Estoque. Através desta rotina, pode-se obter dados como: Consumo mensal por pesos ou pela tendência, calcular o Lote Econômico, Ponto de Pedido e Classificação ABC.

**Com isso, a empresa obtém vantagens como:**

* Menor quantidade de espaço físico para armazenamento;
* Menor risco de obsolescência e deterioração;
* Menor custo de seguro;
* Menor risco de desperdício.

O conflito entre as vantagens e desvantagens na quantidade a encomendar a cada nova compra e/ou produção é resolvido através do cálculo do Lote Econômico.

Por meio dessa rotina podemos obter:

* O cálculo do lote econômico pela disponibilidade financeira
* A Classificação ABC dos materiais
* O consumo médio de produtos, por peso ou por tendência
* O cálculo do ponto de pedido

Para obter maiores informações conceituais (com exemplos) sobre esta rotina, [**clique aqui.**](https://tdn.totvs.com/pages/releaseview.action?pageId=347442943)

**Ao gerar o Consumo Médio verifiquei que na tabela que os alimenta (SB3) estão com valores incorretos. O que fazer?**

Antes de abordarmos o mérito da gravação dos dados de Consumo Médio na tabela SB3 (Demandas), é importante termos o entendimento dos critérios que o sistema utiliza para gerar o Consumo Médio de um produto, para entendermos melhor este conceito e os critérios, [**clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029003612)**.**

A tabela SB3 (Demandas) é atualizada on-line a partir das movimentações realizadas, porém como esta armazena apenas os doze últimos meses (contendo 12 campos para guardar as informações de cada mês), o sistema terá que zerar em algum momento a informação de um mês para reiniciar sua contagem. Isto acontece quando executada a rotina Virada de Saldos (MATA280), desde que o parâmetro **MV\_ZERADEM** esteja ativo. Portanto, quando realizado fechamento de estoque com data retroativa, a demanda calculada na tabela SB3 poderá ficar incorreta ou até mesmo zerada. Se a Virada de Saldos não for realizada, o sistema irá acumular valores do ano anterior com o consumo do ano atual. No entanto, a rotina Lote Econômico (Miscelânea/Cálculos/Consumo e Indicador) permite que o consumo do mês seja recalculado, quando marcada a opção  Atualização do Consumo do Mês antes da execução da rotina. Tal rotina, no entanto, atualiza apenas o mês referente a data base utilizada, ou seja, para atualizar os doze meses a rotina terá que ser executada uma vez para cada mês, com alteração da data base a cada processamento.

Vale lembrar que o consumo pode ficar zerado ou até mesmo negativo mesmo após esta atualização, já que o sistema também considera devoluções para abatimento do consumo do período.

**Saiba mais:**

[*Conceito e exemplos do cálculo de Consumo Médio, Ponto de Pedido, Curva ABC dos Produtos e Lote Econômico*](https://tdn.totvs.com/pages/releaseview.action?pageId=347442943)

[*Conceito e interpretação do relatório de Consumo Mensal.*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029003612)

[*Clique aqui e veja mais artigos sobre Cálculos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550082-SIGAEST-C%C3%81LCULOS)
