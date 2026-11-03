---
article_id: 4576020312087
category: Integrações Outros BackOffice
content_hash: 2569bceec6b861dc7b4921560d8e5b69153933326c9f2d11ac12e29ea12faa29
fetched_at: '2026-06-28T22:46:42.166161+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RM - FOP - Integração RM Labore x BackOffice Protheus Configurador EAI 2.0
type: support-article
updated_at: '2025-02-10T16:50:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4576020312087-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Configurador-EAI-2-0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:03 min****Ocorrência**Ao acessar o Configurador do EAI 2.0 ao clicar em avançar é apresentado uma mensagem informando que podem existir inconsistências.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Validar se ao marcar as demais opções abaixo ao validação será efetuada com sucesso.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4575806935063/mceclip0.png)

Caso deseje alterar posteriormente o nível é possível realizar a edição:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4575846792599/mceclip1.png)

Caso ainda apresente falha na validação será necessário ajustar no Protheus de acordo com as instruções informadas no campo de "log de diagnostico" de cada *adapter* apresentado.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4575893469719/mceclip2.png)

Acessar o Protheus **SIGACFG / base de dados / dicionário / base de dados /** edite a tabela que foi retornada pelo *log* do *adapter* informando o compartilhamento esperado no qual foi apontado pelo *log*.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4575891723927/mceclip3.png)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4677579073943/mceclip0.png)  
**Para mais informações acesse:** [Configurador EAI 2.0](https://tdn.totvs.com/display/public/INT/Configurador+EAI+2.0+-+RM+x+PROTHEUS#Pacotes-Diagn&oacute;stico)
