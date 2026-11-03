---
article_id: 4415329649943
category: Configurações
content_hash: d08e310cf70e87ad7b5bf8a7c50bdb74becbabc02a65295dc86ee91fa11501b2
fetched_at: '2026-06-28T22:46:49.546898+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Desabilitar triggers e fórmulas visuais
type: support-article
updated_at: '2025-03-12T13:41:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415329649943-RH-RM-FOP-Desabilitar-triggers-e-f%C3%B3rmulas-visuais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:01:00 min****Dúvida**Às vezes, é necessário desabilitar triggers e fórmulas visuais para testar problemas de desempenho ou erros específicos no sistema. Como faço para desabilita-las?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Em primeiro lugar, para que não haja impactos em sua base de produção, prepare uma base de homologação com o problema simulado antes de prosseguir. Para desabilitar as triggers e fórmulas visuais, acesse **Menu** | **Serviços Globais** | **Sentinela** | **Tarefas de execução agendada** | **Desabilitar Triggers** | **Desmarque todas as triggers e clique em executar**conforme o print:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6745684617623/mceclip0.png)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415329622679/mceclip0.png)  
  
Nesta mesma tela, é possível **Desabilitar Fórmulas Visuais**. Veja, também, que há a opção de Habilitar Fórmulas Visuais, quando quiser retorna-las para ativas.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415321985943/mceclip1.png)  
  
Após desabilitar suas triggers e fórmulas visuais, faça novamente o teste em que era apresentado erro ou onde o desempenho do sistema deixava a desejar.
