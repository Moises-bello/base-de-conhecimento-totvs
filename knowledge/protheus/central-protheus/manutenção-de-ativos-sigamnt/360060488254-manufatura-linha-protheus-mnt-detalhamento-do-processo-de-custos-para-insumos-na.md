---
article_id: 360060488254
category: Manutenção de Ativos (SIGAMNT)
content_hash: 58cfeea3a50a06fdc7284a1a4172f1fc2f7a0791ba5624894a228656d19dfa75
fetched_at: '2026-06-28T22:42:33.130222+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Detalhamento do processo de custos para
  insumos nas Ordens de Serviço
type: support-article
updated_at: '2021-10-29T11:42:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060488254-Manufatura-Linha-Protheus-MNT-Detalhamento-do-processo-de-custos-para-insumos-nas-Ordens-de-Servi%C3%A7o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:05:00 min**  
**Dúvida**Como são formados os custos para insumos na **O.S - Ordem de Serviço**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**O **SIGAMNT - Manutenção de Ativos** permite obter a análise dos custos das **Ordens de Serviço** de manutenção pela comparação dos valores previstos com os realizados, com base em valores de preço médio ou preço s*tandard*, e conforme a condição do módulo estar ou não integrado ao módulo **SIGAEST - Estoque**.  
  
Os custos previstos são aqueles estimados para uso na execução da **O.S**, e os custos realizados são aqueles relacionados aos insumos efetivamente consumidos na **O.S**.  
  
Ao incluir um produto como insumo realizado na **O.S**, o campo **TL\_CUSTO - Custo do Recurso**, que representa o custo do insumo, e consequentemente o custo total da **O.S**, é atualizado conforme o custo do produto. No que se refere aos custos de produtos, há dois custos utilizados no **SIGAMNT**, o custo médio e o custo *standard*. O custo *standard* é utilizado no cadastro de **Produtos - SB1** e o custo médio é atualizado no cadastro de **Saldos em Estoque - SB2**.  
  
Quando há integração com o **Estoque**, ou seja, o parâmetro **MV\_NGMNTES - Integração Manutenção (MNT) com Estoque (EST)** igual a **S - Sim**, as **O.S.'s** obtém o valor do custo médio do produto. O custo médio é recalculado pelo módulo de **Estoque** mensalmente e/ou conforme parametrizações e quando há **O.S.'s** que utilizam insumos do tipo produto/terceiros esse recálculo também atualiza os custos das ordens no **SIGAMNT**. Nesse contexto são atualizadas as movimentações de entrada e saída de estoque que estão relacionadas aos insumos utilizados nas **O.S.'s**. Dessa forma tanto o custo dos insumos quanto o valor da **O.S** é atualizado quando é feito o processo de recálculo de custo médio. Importante ressaltar que apenas as **O.S.'s** incluídas no intervalo definido pelo parâmetro **MV\_ULMES - Indica a data do último fechamento do estoque** são atualizadas.   
  
Ao incluir os insumos em uma **O.S**, os produtos de mesmo código são agrupados, como por exemplo, dois funcionários de um mesmo centro de custo. O valor unitário é calculado como o valor total sobre a quantidade. Se, por ventura, um insumo acrescer o valor total de horas extras, seu valor unitário calculado já contemplará esse valor.   
  
A obtenção dos custos dos insumos previstos e realizados quando há integração com o estoque são detalhados na tabelas abaixo:

|  |  |  |  |
| --- | --- | --- | --- |
| **Tipo de Insumo** | **Insumo Previsto** | **Insumo Realizado** | **Detalhe do campo para realizado** |
| **Produtos** | **Preço médio atual - B2\_CM1**. Não é modificado quando há modificação do preço médio | **Preço médio atual - B2\_CM1**. Ao ser recalculado o preço médio no estoque, haverá modificação do custo do insumo. | **B1\_COD - Código do Produto** |
| **Mão de Obra** | **Preço médio atual - B2\_CM1** do registro **MOD - Mão de obra**. Não é modificado quando há modificação do preço médio. | **Preço médio atual - B2\_CM1**. Ao ser recalculado o preço médio no estoque, haverá modificação do custo do insumo. | **MOD + T1\_CCUSTO - Centro de Custo do Funcionário**. |
| **Especialidade** | Preço unitário da especialidade **T0\_SALARIO - Salário Hora**, na inclusão da **O.S**. | Não se aplica. O usuário não pode reportar o consumo de especialidade. Deve informar o funcionário que executou o serviço. | Não se aplica |
| **Ferramentas** | **Preço unitário da ferramenta - H4\_CUSTOH**, na inclusão da **O.S**. | **Preço unitário da ferramenta -H4\_CUSTOH**, no reporte da utilização da ferramenta. | **B1\_COD - Código do Produto**, associado à ferramenta conforme o parâmetro **MV\_PRODFER - Item de estoque que indica Ferramentas no SIGAMNT**. |
| **Terceiro** | **Preço unitário do fornecedor - TPO\_CUSTO** na inclusão da **O.S**. | Preço informado na digitação da nota fiscal. | **B1\_COD - Código do Produto** associado ao terceiro conforme parâmetro **MV\_PRODTER - Item de Estoque que indica Terceiros no SIGAMNT**. |

Quando não há integração com o **Estoque**, ou seja, o parâmetro **MV\_NGMNTES** igual a **N - Não**, as **O.S.'s** obtém o valor do custo *standard* do produto. A valorização da ordem de serviço pelo custo *standard* relaciona-se a adoção de valores não fiscais, isto é, valores modificáveis conforme a necessidade e intenção do usuário, permitindo o exercício de simulação.  
  
A obtenção dos custos dos insumos previstos e realizados quando não há integração com o **Estoque** são detalhados na tabelas abaixo: 

|  |  |  |
| --- | --- | --- |
|  | **Insumo previsto** | **Insumo realizado** |
| **Produtos** | **Custo Standard - B1\_CUSTD** | **Custo Standard - B1\_CUSTD** ou o valor alterado pelo usuário no momento de  informação do consumo. |
| **Mão de Obra** | **T1\_SALARIO - Valor do Salário Hora** quando preenchido ou **T0\_SALARIO - Salário Hora**, quando campo **T1\_SALARIO** vazio | **T1\_SALARIO - Valor Salário Hora** ou o valor alterado pelo usuário no momento de  informação do consumo. |
| **Especialidade** | **Valor do Salário Hora - T0\_SALARIO** | Não se aplica. |
| **Ferramentas** | **Custo Hora da Ferramenta - H4\_CUSTOH** | **Custo Hora da Ferramenta - H4\_CUSTOH** ou o valor alterado pelo usuário no momento de  informação do consumo. |
| **Terceiro** | **Custo Hora do Serviço - TPO\_CUSTO** | **Custo Hora do Serviço - TPO\_CUSTO** ou o valor alterado pelo usuário no momento de  informação do consumo. |
