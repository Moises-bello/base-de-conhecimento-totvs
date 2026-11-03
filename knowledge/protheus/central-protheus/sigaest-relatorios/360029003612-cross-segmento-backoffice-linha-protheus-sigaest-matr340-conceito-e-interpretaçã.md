---
article_id: 360029003612
category: SIGAEST - RELATORIOS
content_hash: 5dc81a72739ff32ecf409443f9166e53fdb3ccf05356160a2749137230f5b9c9
fetched_at: '2026-06-28T22:39:06.140964+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR340 - Conceito
  e interpretação do relatório Consumo Mês a Mês
type: support-article
updated_at: '2026-05-07T18:07:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029003612-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR340-Conceito-e-interpreta%C3%A7%C3%A3o-do-relat%C3%B3rio-Consumo-M%C3%AAs-a-M%C3%AAs
---

O relatório MATR340 do Protheus exibe apenas o consumo mensal efetivo (requisitado/vendido como positivo e devoluções como negativo). Para validar corretamente os valores, é necessário rodar a rotina MATA290 mês a mês. Movimentações RE/DE 3,4,7 e 8 não são consideradas. O relatório não serve para fechamento, apenas para análise de consumo.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38390004638359) Tempo aproximado para leitura: **00:03:20 min**

**Dúvida**

Fiz a emissão do Relatório MATR340 (Consumo Mês a Mês) porém os cálculos por mês parecem estar incorretos. Como validar os valores das colunas mês a mês?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**Observações iniciais:**A partir do release 12.1.25 utilizar a consulta **SMARTVIEW Consumo Mês a Mês ESTSV015**. Veja [nesse link](https://tdn.totvs.com/x/eoE1LQ) a documentação da Consulta.

O conceito dessa seção do relatório é apresentar somente o que foi consumido dentro do período, ou seja, tudo que foi **requisitado/vendido** constarão como positivo e tudo que ocorrer por **devoluções/devoluções de vendas** constarão como negativo.

**IMPORTANTE:** Antes da geração do relatorio, efetuar o processamento da rotina **MATA290(Consumo e indicador: sobre** [**clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020482111-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA290-Consumo-M%C3%A9dio-e-grava%C3%A7%C3%A3o-da-tabela-de-Demandas-SB3)**)** , para que seja recalculado os dados, no periodo, pois isso ira reconsiderar os saldos para calculo das tabelas:

**SB1,SD1,SD2,SD3,SB3**

Ou SEJA:

* Se voce quer ver o consumo de **JAN/2025**: Acesse a database no protheus em **31/01/2025** e processe a rotina MATA290.
* Se voce quer ver o consumo de **FEV/2025:** Acesse a database no protheus em **28/02/2025** e processe a rotina MATA290.

**Sim,** se voce quer ver o saldo do consumo mes a mes, voce precisa rodar a rotina MES a MES para que assim ela calcule o consumo do MES.

Atente-se aos perguntes:

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36865752583831)

**Obs**: É importante ressaltar que as movimentações RE/DE 3,4,7 e 8 **não são** consideradas no consumo mensal no relatório MATR340. Veja mais detalhes sobre os códigos dos Tipos de Movimentações [**clicando aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007057091-MP-SIGAEST-Quais-os-significados-dos-c%C3%B3digos-dos-tipos-de-Movimentos-Internos-RE-DE-)

Caso não atenda no padrão, existe o Ponto de Entrada [**MT290SD3**](https://tdn.totvs.com/pages/releaseview.action?pageId=572504431) para validar os Movimentos Internos (SD3) que farão parte do recálculo do consumo médio do mês.

**ESSE RELATORIO NÃO É BASE PRA EFETIVAR FECHAMENTO**, utilize o Kardex(MATR900) ou Posição Analítica (MATR260) para isso.

## ***Observação:***

O sistema realiza o cálculo de consumo considerando exclusivamente os últimos 12 meses retroativos ao período atual, não sendo possível apurar o consumo para períodos anteriores a esse intervalo.

**Saiba mais:**

[Smart View - Consumo Mês a Mês](https://tdn.totvs.com/x/eoE1LQ)

[Smart View - Estoque (Consultas)](https://tdn.totvs.com/x/M8LrL)

[Backoffice (Linha Protheus) - SIGAEST - Descontinuidade de Relatórios do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23374418520087-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Descontinuidade-de-Relat%C3%B3rios-do-Estoque)

[Clique aqui e veja mais artigos sobre Relatórios no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029003612)
