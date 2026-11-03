---
article_id: 360063515473
category: Manutenção de Ativos (SIGAMNT)
content_hash: f429946139c0337144c6860dffbf04df1d1c56cf3debda9f2b2dd0b944fac569
fetched_at: '2026-06-28T22:42:33.097655+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Custo Médio Ordem de Serviço
type: support-article
updated_at: '2024-03-12T16:52:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063515473-Manufatura-Linha-Protheus-MNT-Custo-M%C3%A9dio-Ordem-de-Servi%C3%A7o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:30 min**  
**Dúvida**Como é formado o custo da **O.S. - Ordem de Serviço** quando integrado com **Estoque - SIGAEST**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**O **Manutenção de Ativos - SIGAMNT** permite obter a análise dos custos das **Ordens de Serviço** de manutenção pela comparação dos valores previstos com os realizados, com base em valores do custo médio quando há integração com o **Estoque**, ou seja, o parâmetro **MV\_NGMNTES** - Integração com Estoque igual a **S - Sim**.   
  
Os custos previstos são aqueles estimados para uso na execução da **O.S.**, e os custos realizados são aqueles relacionados aos insumos efetivamente consumidos na **O.S.** Ao incluir um produto como insumo realizado na **O.S.**, o campo **TL\_CUSTO - Custo do Insumo** é atualizado conforme o custo médio do produto.   
  
No sentido inverso, o **Estoque** realiza a função de recálculo de custo médio dos produtos. Nesse contexto são atualizadas as movimentações de entrada e saída de estoque que estão relacionadas aos insumos utilizados nas **Ordens de serviço**. Dessa forma tanto o custo dos insumos quanto o valor da **O.S** é atualizado quando é feito o processo de recálculo de custo médio. Importante ressaltar que apenas as **Ordens de serviço** incluídas no intervalo definido pelo parâmetro **MV\_ULMES - Que indica a data do último fechamento do estoque são atualizadas**.   
  
A obtenção dos custos dos insumos previstos e realizados quando há integração com o **Estoque** são detalhados na tabelas abaixo:

|  |  |  |  |
| --- | --- | --- | --- |
| **Tipo de Insumo** | **Insumo previsto** | **Insumo realizado** | **Detalhe do campo para realizado** |
| **Produtos** | **Preço médio atual -  B2\_CM1**. Não é modificado quando há modificação do preço médio | **Preço médio atual - B2\_CM1**. Ao ser recalculado o preço médio no estoque, haverá modificação do custo do insumo. | **B1\_COD - Código do Produto** |
| **Mão de Obra** | **Preço médio atual- B2\_CM1** do registro **MOD**. Não é modificado quando há modificação do preço médio. | **Preço médio atual - B2\_CM1**. Ao ser recalculado o preço médio no estoque, haverá modificação do custo do insumo. | **'MOD' + T1\_CCUSTO Centro de custo do funcionário** |
| **Especialidade** | **Preço unitário da especialidade** - **T0\_SALARIO - Valor Salário Hora** - na inclusão da **O.S**. | Não se aplica. O usuário não pode reportar o consumo de especialidade. Deve informar o funcionário que executou o serviço. | Não se aplica |
| **Ferramentas** | **Preço unitário da ferramenta - H4\_CUSTOH** na inclusão da **O.S**. | **Preço unitário da ferramenta - H4\_CUSTOH** no reporte da utilização da ferramenta. | **B1\_COD - Código do Produto** associado à ferramenta conforme o parâmetro **MV\_PRODFER - Item de Estoque que indica a Ferramenta no SIGAMNT**. |
| **Terceiro** | **Preço unitário do fornecedor - TPO\_CUSTO** na inclusão da **O.S**. | Preço informado na digitação da **NF - Nota Fiscal**. | **B1\_COD - Código do Produto -** associado ao terceiro conforme parâmetro **MV\_PRODTER - Item de Estoque que indica Terceiro no SIGAMNT** . |

**Importante**  
Ao incluir os insumos em uma **O.S.**, os produtos de mesmo código são agrupados, como por exemplo, dois funcionários de um mesmo centro de custo. O valor unitário é calculado como o valor total sobre a quantidade. Se, porventura, um insumo acrescer o valor total de horas extras, seu valor unitário calculado já contemplará esse valor.
