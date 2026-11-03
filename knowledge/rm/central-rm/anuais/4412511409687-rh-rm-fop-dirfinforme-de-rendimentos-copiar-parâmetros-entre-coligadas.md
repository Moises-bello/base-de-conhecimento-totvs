---
article_id: 4412511409687
category: Anuais
content_hash: a3964f09bd9f0e7ba55d2d302ab978cf1cfac9dda1095dc39478de36efb1bc3d
fetched_at: '2026-06-28T22:46:51.113310+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - DIRF/Informe de Rendimentos: Copiar parâmetros entre coligadas'
type: support-article
updated_at: '2025-03-12T13:43:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412511409687-RH-RM-FOP-DIRF-Informe-de-Rendimentos-Copiar-par%C3%A2metros-entre-coligadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como realizar a copia de parâmetros entre coligadas da DIRF/Informe de Rendimentos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A geração de cópia de parâmetros e eventos entre coligadas deve ser executada através da coligada de origem. É possível realizar a cópia dos parâmetros e eventos da coligada de origem para a coligada de destino, mas a DIRF de todas coligadas será gerada pela coligada de origem. Siga os passos abaixo:  
  
Acesse: **Anuais | DIRF/Informe de Rendimentos | DIRF/Informe de Rendimentos**:  
  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412510970391/mceclip1.png)**Na aba **Geração da DIRF/Informe de Rendimentos** deve selecionar a coligada de destino, marcar a coligada da qual será copiada o perfil, gerar a DIRF da coligada origem para que o sistema reconheça.  
  
Depois, acessar novamente o mesmo perfil, na mesma coligada de origem e gerar a DIRF para outra coligada. Lembrando que deve acessar a coligada de origem, pois o sistema não reconhece acessando a outra coligada.  
  
Por exemplo, estou na coligada 1, origem, realizando a cópia dos parâmetros da DIRF para coligada 7, destino, faço o processo de copia, gerando a DIRF referente a coligada 1.  
  
Após a geração na coligada 1, saio dos parâmetros da DIRF, acesso novamente na coligada 1 e não na 7, seleciono a coligada 7 e gero a DIRF, onde o sistema irá buscar todos os dados da coligada 1 de acordo com o perfil gravado, conforme print abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412510896407/mceclip0.png)  
  
Os parâmetros copiados só ficam visíveis para o usuário, perfil e coligada do contexto da coligada que fez a cópia, não sendo acessível na coligada de destino.  
  
**Saiba mais**[DIRF/Informe de Rendimentos](https://tdn.totvs.com/pages/releaseview.action?pageId=452719351)
