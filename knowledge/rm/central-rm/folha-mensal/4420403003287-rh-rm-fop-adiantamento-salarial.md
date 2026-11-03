---
article_id: 4420403003287
category: Folha Mensal
content_hash: 1e174fac7197ea695904627458cbd7f53f41ba170f110022517e2efbf4acd226
fetched_at: '2026-06-28T22:46:59.247669+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Adiantamento Salarial
type: support-article
updated_at: '2025-01-21T20:42:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420403003287-RH-RM-FOP-Adiantamento-Salarial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29401177338391) Tempo aproximado para leitura: **00:00:50 min****Dúvida**Como se processa Pagamento e Desconto de Adiantamento de salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Primeiramente cria-se os eventos de [Código de Cálculo 19 - Adiantamento](https://tdn.totvs.com/pages/releaseview.action?pageId=452719767#:~:text=Desconto%20do%20tipo%20valor.,c%C3%A1lculo%20034%20%2D%20Pagamento%20de%20Adiantamento.)  e o evento de [Código de Cálculo 34 - Pagamento Adiantamento](https://tdn.totvs.com/pages/releaseview.action?pageId=452718730). Para isso, acesse: **Administração de Pessoal | Eventos | Eventos:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29401185570711)** **![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420402809879)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420411185047)**2. O lançamento dos eventos deverão ser executados através do menu **Folha Mensal | Lançamentos | Grupos de Eventos**, sendo que o evento de código de cálculo 19 deverá ser lançado após o lançamento do código de cálculo 34 em um Grupo de Evento separado.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29401185572759)  
  
**Importante**  
Nada impede, no entanto, que se criem fórmulas para os eventos associados a códigos de cálculo. Neste caso, o sistema dará prioridade às fórmulas.  
  
**Saiba Mais**  
[RH - RM - FOP - Lançamento dos grupos de eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014011632-RH-RM-FOP-Lan%C3%A7amento-dos-grupos-de-eventos)
