---
article_id: 4415557605911
category: Rescisão
content_hash: 7a7c871afd90a67f8d10c2ce8ed1891a945137e388832d8651d3cd6ef948d8be
fetched_at: '2026-06-28T22:46:54.427731+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - GRRF: Código de Saque inválido para Código de Movimentação
  e Categoria informados e Indicativo de Aviso só pode ser 1,2 ou 3'
type: support-article
updated_at: '2024-10-18T15:59:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415557605911-RH-RM-FOP-GRRF-C%C3%B3digo-de-Saque-inv%C3%A1lido-para-C%C3%B3digo-de-Movimenta%C3%A7%C3%A3o-e-Categoria-informados-e-Indicativo-de-Aviso-s%C3%B3-pode-ser-1-2-ou-3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:30:00 min****Ocorrência**No módulo Folha de Pagamento, ao gerar a GRRF apresentam os seguintes erros: **480- Código de Saque inválido para Código de Movimentação e Categoria informados** e **80- Indicativo de Aviso só pode ser 1,2 ou 3**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415587617943/mceclip0.png)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415587634583/mceclip1.png)  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois o parâmetro **Ativar alterações da Reforma Trabalhista de acordo com a Lei N° 13.467 de 13 de Julho de 2017** não está marcado.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse: **Configurações | Parametrizador | Folha Normal | Geral** e marque o parâmetro **Ativar alterações da Reforma Trabalhista de acordo com a Lei N° 13.467 de 13 de Julho de 2017está marcada.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415574149015/mceclip2.png)**  
2. Logo, gere a GRRF novamente.
