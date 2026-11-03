---
article_id: 4411789546903
category: RH - Folha de Pagamento
content_hash: f39040cd67ec4b665e0725525cb937b1b6ea39b5ba22ea26cc34bcd4b385ddac
fetched_at: '2026-06-28T22:44:12.073131+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de Hora extra para Tarefeiro
type: support-article
updated_at: '2025-08-11T21:02:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411789546903-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Hora-extra-para-Tarefeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26337957661719) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Cálculo de Hora extra para Tarefeiro  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para o cálculo de Hora extra e faltas para tarefeiro é necessário lançar as verbas respectivas na tabela **S070** na rotina manutenção de tabelas em **Atualizações > Definições de cálculos > Manutenção tabelas**.

O cálculo das horas extras e faltas são baseados no valor unitário da tarefa, lembrando que, no caso de horas extras o resultado do valor unitário x quantidade de horas extras será valorizado de acordo com o percentual de pagamento definido na verba de Hora Extra.

Exemplo:

Verba HE 50% e o valor da tarefa unitário do período é 15,00, então o valor a ser lançado na tarefa de HE será **15,00 + 50% = 22,50**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411788214679)

**Observação**: A verbas de Hora extra e Falta informadas dentro da tabela S070 precisam ser vinculadas a tarefa de cálculo do período.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411796345623)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411796366743)

E na rotina de tarefas lançar a quantidade de HE que deseja pagar para o tarefeiro no mês.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411788622615)

Cálculo da folha

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411788693911)

**Importante:** As colunas HE e Faltas da tabela S070 são exclusivamente para Professores, onde se amarrado a verba de HE para o Tarefeiro não surtirá efeito, pois na rotina de Lançamento de Tarefas não há campo onde informar as horas que deseja pagar de Hora Extra para esse tarefeiro.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Cálculo para tarefeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037394713-RH-Linha-Protheus-GPE-C%C3%A1lculo-para-tarefeiro)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
