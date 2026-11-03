---
article_id: 1500003342362
category: Manutenção de Ativos (SIGAMNT)
content_hash: d87189f477b85e7094f58a90e3c6b45e517bf3281dfde20922ed2a3b61ff938f
fetched_at: '2026-06-28T22:42:33.107200+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Custo Standard Ordem de Serviço
type: support-article
updated_at: '2021-07-02T14:57:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003342362-Manufatura-Linha-Protheus-MNT-Custo-Standard-Ordem-de-Servi%C3%A7o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como é formado o custo da **O.S. -** **Ordem de Serviço** quando não integrado com **Estoque - SIGAEST**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**O **Manutenção de Ativos - SIGAMNT** permite obter a análise dos custos das **Ordens de Serviço** de manutenção pela comparação dos valores previstos com os realizados, com base em valores do custo *standard* quando **não** há integração com o **Estoque**, ou seja, o parâmetro **MV\_NGMNTES** - Integração com Estoque igual a **N - Não**.   
  
Os custos previstos são aqueles estimados para uso na execução da **O.S.**, e os custos realizados são aqueles relacionados aos insumos efetivamente consumidos na **O.S.** Ao incluir um produto como insumo realizado na **O.S.**, o campo **TL\_CUSTO - Custo do Insumo** é atualizado conforme o custo *standard* do produto.   
  
A valorização da **O.S.** pelo **Custo Standard** relaciona-se a adoção de valores não fiscais, isto é, valores modificáveis conforme a necessidade e intenção do usuário, permitindo o exercício de simulação.   
O custeio pelo *Standard* independe no **SIGAMNT** de estar integrado ao **SIGAEST**, já que as informações de valores necessárias são modificáveis no módulo de **Manutenção**.  
  
A obtenção dos custos dos insumos previstos e realizados quando não há integração com o estoque são detalhados na tabelas abaixo: 

|  |  |  |
| --- | --- | --- |
| **Tipo de insumo** | **INSUMO PREVISTO** | **INSUMO REALIZADO** |
| **Produtos** | **Custo Standard - B1\_CUSTD** | **Custo Standard - B1\_CUSTD** ou o valor alterado pelo usuário no momento de informação do consumo. |
| **Mão de Obra** | **Valor do Salário Hora - T1\_SALARIO** quando preenchido ou **T0\_SALARIO** quando o campo **T1\_SALARIO** vazio | **Valor do Salário Hora - T1\_SALARIO** ou o valor alterado pelo usuário no momento de informação do consumo. |
| **Especialidade** | **Valor do Salário Hora - T0\_SALARIO** | Não se aplica. |
| **Ferramentas** | **Custo Hora da Ferramenta - H4\_CUSTOH** | **Custo Hora da Ferramenta -H4\_CUSTOH** ou o valor alterado pelo usuário no momento de informação do consumo. |
| **Terceiro** | **Custo Hora do Serviço - TPO\_CUSTO** | **Custo Hora do Serviço - TPO\_CUSTO** ou o valor alterado pelo usuário no momento de informação do consumo. |
