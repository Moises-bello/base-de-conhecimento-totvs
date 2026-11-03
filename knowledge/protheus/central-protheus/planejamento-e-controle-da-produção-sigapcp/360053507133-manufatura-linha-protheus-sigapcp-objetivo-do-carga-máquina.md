---
article_id: 360053507133
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: db688b00a0554fb059f3bdfa9b1203178831efe24664c0b486011354339a76f9
fetched_at: '2026-06-28T22:42:44.671588+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Objetivo do Carga Máquina
type: support-article
updated_at: '2021-08-31T12:54:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053507133-Manufatura-Linha-Protheus-SIGAPCP-Objetivo-do-Carga-M%C3%A1quina
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:25 min**  
**Dúvida**Qual o objetivo do **MATA690 - Carga Máquina**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O **Carga Máquina** da linha **Protheus**, por ser uma rotina **CRP**, faz parte do chamado **MRPII - Manufacturing Resource Planning**, ou seja **MRP - Material Requirement Planning + CRP - Capacity Requirement Planning**.  
  
O **MRP** e o **MRPII** determinam:

![CRP2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360087441833/CRP2.jpg)

A função de **Carga Máquina** da linha **Protheus** também permite o cálculo parcial, posicionando-se sobre uma atividade, e selecionando a opção **Recalcular Carga Máquina**.  
  
Ao **Alterar Data Prevista de Entrega** de uma atividade, e logo após **Recalcular Carga Máquina,** o cenário é executado parcialmente, e o carga máquina é capaz de realizar o novo planejamento considerando as horas executadas. Isto é possível por meio da configuração do parâmetro **considera saldo** que nas opções **operação** e **saldo por tempo** abate os apontamentos de horas já realizados nas operações.  
  
Apesar do **Carga Máquina** permitir a alteração de datas das **OPs - Ordens de Produção** na tela de visualização de alocação, ao recalcular, não é efetuada a explosão das necessidades, como é pelo cálculo do **MRP**. Neste caso, as **OPs** filhas podem ficar incoerentes. Para tentar minimizar este efeito, dever-se-ia alterar manualmente também as datas das **OPs** filhas ainda dentro da tela de alocação, embora assim, seja arriscado já que o **MRP** pode ter unido demandas vindas de vários lugares numa única **Ordem**.  
  
No exemplo de alocação dado acima, PA01, onde originalmente a data de término da alocação é de 08/12/XX, se for antecipada para 05/12/XX por **Alterar Data Prevista de Entrega** ficaria:  
  
**1ª Variação - Sequência**

![variacao1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360087441813/variacao1.jpg)![variacao1Tabela.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360087442593/variacao1Tabela.jpg)

**2ª Variação - Item**

![variacao2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360086256834/variacao2.jpg)

![variacao2Tabela.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360087441853/variacao2Tabela.jpg)

**3ª Variação - Ordem**

![variacao3.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360087441893/variacao3.jpg)

![variacao3Tabela.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360086256974/variacao3Tabela.jpg)

O comportamento da **2ª e 3ª Variação** é exatamente o mesmo, ou seja, não consegue relacionar as ordens, ficando assim inconsistente a montagem de PA01, antes da conclusão da pintura.  
  
**Importante**Quando a relação entre a **ordem Pai** e suas **Filhas** for diferente da **1ª Variação,** faz com que o cálculo do **Carga Máquina** perca o critério de sequência, que relaciona a ordem pai com suas filhas. Para este caso o recálculo não conseguirá alterar a previsão das outras ordens - filhas, sendo necessário alterar a demanda original - **Previsão de Vendas, Pedidos** - e executar o cálculo do **MRP** para acertar as novas demandas.
