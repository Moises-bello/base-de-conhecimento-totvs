---
article_id: 19124711142679
category: RH - Fechamento Período
content_hash: c8e56c20a7cfa0503d1a2e828fe1416ea30d64c862ec78e226efbe2c8ce377cd
fetched_at: '2026-06-28T22:43:24.464555+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - Implementação de GRID no Fechamento de Período
type: support-article
updated_at: '2025-04-16T12:20:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19124711142679-RH-Linha-Protheus-GPE-Implementa%C3%A7%C3%A3o-de-GRID-no-Fechamento-de-Per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19124685972119) Tempo aproximado para leitura: **01:00:00 min** **Dúvida**Possibilitar o fechamento de períodos utilizando grid de processamento para melhoria de performance

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - à partir da versão 12.1.2210  
  
**Solução**

Visando atender as necessidades de **performance** de nossos clientes, estamos disponibilizando a possibilidade de efetuar o **fechamento** **de período** (GPEM120) utilizando **[GRID](https://tdn.totvs.com/pages/releaseview.action?pageId=6065059).**

A configuração é a mesma utilizada nas [rotinas de cálculo](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=267782422), e para quem ainda não utiliza GRID, poderá utilizar o [Wizard](https://tdn.totvs.com/pages/viewpage.action?pageId=707369936)de configuração para efetuar a implantação.

Agora é possível escolher entre o uso de **multi-thread, GRID,** ou ambos ao mesmo tempo.  Abaixo um diagrama das possibilidades de execução que estarão disponíveis a partir de agora:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19124672651159)

**Multi-Thread** → Recomendado para clientes que possuam vários processos com poucos funcionários alocados em cada um. Exige pouco no que tange a infraestrutura.

**GRID** → Recomendado para clientes com poucos processos e muitos funcionários alocados. Exige muitos recursos de infraestrutura.

**Multi-Thread com GRID** → Recomendado para clientes que possuem vários processos com muitos funcionários alocados em cada um deles. Exige alto investimento em infraestrutura e implantação.

**Importante**

A utilização de **multi-threads** com **GRID** exige uma infraestrutura capaz de suportar o processamento paralelo. Não existe uma quantidade ideal de threads ou agentes do GRID.Sugerimos que esta análise seja realizada durante o processo de implantação, realizando **testes** pontuais, iniciando, por exemplo, com **duas threads** e **dois agentes,** e aumentando progressivamente de acordo com as estatísticas de performance. Quando a performance alcançar o pico de rendimento, no próximo aumento de thread ou agente a **velocidade** tende a diminuir progressivamente, por isso é importante encontrar a **melhor relação** **Threads x Agentes x Infraestrutura**. Essa relação deve estar alinhada com a quantidade de usuários que poderão acessar o sistema e concorrer com o cálculo, de modo a não formar gargalos.

Para utilização de multi-thread com GRID deve ser feita toda a **implantação** relacionada ao GRID através do **[link](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=267782422),** além da definição de quantidade de threads no parâmetro MV\_CALCTHD.  
Na rotina de fechamento, as threads só serão iniciadas em um cenário que haja mais de **300 registros ativos** na tabela **SRA** (funcionários) para o processo.

O parâmetro **MV\_GPEGRID** também deverá ser configurado de acordo com as rotinas que deseja utilizar GRID sendo:  
**1** = Provisão  
**2** = Cálculo por Roteiros  
**3** = Fechamento  
**Vazio** = Todas as rotinas

Se quiser utilizar apenas com provisão e fechamento, por exemplo, o parâmetro deve ser configurado com: "**13**".

**Saiba mais**:  
[RH - Linha Protheus - GPE - Como realizar o fechamento mensal de determinado período da folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027259971?source=search)  
[RH - Linha Protheus - GPE - Melhoria de performance no fechamento mensal com MV\_CALCTHD ativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050884333?source=search)  
[RH - Linha Protheus - GPE - Implementação do Multi Thread no fechamento da folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034908554?source=search)
