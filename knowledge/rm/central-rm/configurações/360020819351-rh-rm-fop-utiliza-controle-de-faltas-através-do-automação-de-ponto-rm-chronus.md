---
article_id: 360020819351
category: Configurações
content_hash: 24d7f89e6e57ceb1d372e187f83997fa481a83d74b3d2292c1e33395bb3d8e47
fetched_at: '2026-06-28T22:46:49.639519+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Utiliza Controle de Faltas através do Automação de Ponto (RM
  Chronus)
type: support-article
updated_at: '2025-03-13T11:20:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020819351-RH-RM-FOP-Utiliza-Controle-de-Faltas-atrav%C3%A9s-do-Automa%C3%A7%C3%A3o-de-Ponto-RM-Chronus
---

**Dúvida**Qual a funcionalidade do parâmetro **Controle de faltas através do RM Chronus**?  
   
 **Ambiente**RM - Folha de Pagamento - Todas as versões  
  
**Solução**Antes de prosseguir a análise do parâmetro propriamente dito, tire suas dúvidas sobre o parâmetro **[Controle de Faltas para Cálculo de Avos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020486611)**.  
  
Marcando este parâmetro será disponibilizado no **RM Chronus**, na rotina de Lançamento de Eventos para o RM Labore, o parâmetro **Grava controle de faltas para cálculo de avos na folha**. Este parâmetro permite ao usuário definir se grava o controle de faltas no momento do lançamento do evento de desconto de faltas.  
  
O evento de desconto de faltas será lançado na movimentação temporária (**PFMOVTEMP**) e os dias de faltas serão lançados no **Controle de Faltas** do cadastro do funcionário (**PFHSTFALTA**).  
  
Para ativar o parâmetro, acesse o módulo **Folha de Pagamento** e depois acesse o caminho **Configurações | Parametrizador | Folha de Pagamento | Folha Normal** e marque os parâmetros ****[Controle de Faltas para Cálculo de Avos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020486611)**** e depois marque também ****Controle de faltas através do RM Chronus****.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360017271772/mceclip0.png)  
  
Após marcar este parâmetro será disponibilizado um histórico de controle de faltas, disponível no cadastro do funcionário, em **Anexos | Movimento | Grava controle de faltas para cálculo de avos na folha,**possibilitando a geração do controle de faltas no lançamento do evento de desconto de faltas.  
  
  
**Observação**Para mais informações sobre o controle de faltas, [clique aqui](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.ControleFaltas.aspx).
