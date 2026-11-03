---
article_id: 34185850238615
category: Folha Mensal
content_hash: f6f056410d8d6a6c23f6d55e0efcece30e3e97433d2d04a9a59b2956a45ad0f8
fetched_at: '2026-06-28T22:46:58.014155+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Diferença salarial - Erro: Evento de diferença salarial com
  incidência em INSS não é único'
type: support-article
updated_at: '2025-08-14T17:53:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34185850238615-RH-RM-FOP-Diferen%C3%A7a-salarial-Erro-Evento-de-diferen%C3%A7a-salarial-com-incid%C3%AAncia-em-INSS-n%C3%A3o-%C3%A9-%C3%BAnico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34185878411159) Tempo aproximado para leitura: **00:02:23min**  
  
**Ocorrência**  
Ao processar a diferença salarial, o sistema apresenta a mensagem:

**"Evento de diferença salarial com incidência em INSS não é único. Está(ão) faltando o(s) seguinte(s) Código(s) de Cálculo no cadastro de Eventos: 037 - Diferença salarial SEM incidência de INSS."**  
  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34185891560855)**  
  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
No processo de diferença salarial, é obrigatório que existam apenas dois eventos com Código de Cálculo 37:

* 1 evento **com** incidência em INSS.
* 1 evento **sem** incidência em INSS.

O erro ocorre porque existem vários eventos cadastrados com incidência em INSS e nenhum evento com CC37 sem incidência em INSS, o que não atende à parametrização correta exigida pelo sistema.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o cadastro de eventos em **Administração de Pessoal | Eventos**, filtre pelo  Código de Cálculo 37 para que apareçam somente os eventos com este Código de Cálculo.

Ajuste para que permaneçam somente dois eventos:

* Um com incidência em INSS.
* Outro sem incidência em INSS.

No exemplo abaixo, foi criado o evento com código 0037 e Código de Cálculo 37 com incidência em INSS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34185878412055)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34185878413335)

E também foi criado o evento com código 0244 e Código de Cálculo 37, porém sem incidência em INSS marcada. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34185850215063)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34185850215191)

2. Caso haja eventos excedentes com CC37 e incidência em INSS, remova a incidência ou altere o Código de Cálculo conforme necessário. O importante é que na base do RM contenham apenas os dois eventos necessários.

Em caso de dúvidas, consulte também o material: [RH - RM - FOP - Eventos que compõem a diferença salarial por dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018592811-RH-RM-FOP-Eventos-que-comp%C3%B5em-a-diferen%C3%A7a-salarial-por-diss%C3%ADdio)
