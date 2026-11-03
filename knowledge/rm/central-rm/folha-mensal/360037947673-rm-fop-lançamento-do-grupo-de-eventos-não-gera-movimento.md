---
article_id: 360037947673
category: Folha Mensal
content_hash: 2e06b495d65877787de1b736ba307d95046fd9697f236d949646c5fa92c8d3a2
fetched_at: '2026-06-28T22:46:59.527369+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RM - FOP - Lançamento do Grupo de Eventos não gera movimento
type: support-article
updated_at: '2025-03-07T14:55:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037947673-RM-FOP-Lan%C3%A7amento-do-Grupo-de-Eventos-n%C3%A3o-gera-movimento
---

**Ocorrência**Ao lançar grupo de eventos, o produto executa a rotina sem erros, porém ao verificar o envelope do funcionário, não consta nenhum lançamento.   
  
 **Ambiente**RM - FOP - Folha de Pagamento - Todas as versões.  
  
 **Causa**Isso pode ocorrer devido a uma parametrização presente em **Configurações | Parametrizador | Folha Normal | Cálculo,** em que caso a flag *Utiliza gerenciador de movimento* esteja marcada, o lançamento dos eventos na folha do funcionário, serão lançados através do menu **Folha Mensal | Gerenciador de Movimento | Lançamento.**

**![PARAMETRO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049982753/PARAMETRO.png)**

![MENU.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049983293/MENU.png)

**Solução**Deve-se verificar se de fato a empresa utiliza esta tratativa de lançamento da folha. Se para a empresa não faz necessário trabalhar dessa forma, basta desmarcar a flag citada acima no parametrizador, para que assim o lançamento da folha seja feito diretamente do grupo de eventos.
