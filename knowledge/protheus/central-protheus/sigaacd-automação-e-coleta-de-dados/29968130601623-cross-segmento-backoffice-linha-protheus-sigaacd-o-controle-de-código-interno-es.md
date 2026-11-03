---
article_id: 29968130601623
category: SIGAACD - Automação e Coleta de Dados
content_hash: 7538c29bdcadedd32fbd4bc2c66fac8e23ed93bcb917cfa1685d5f6d9975d523
fetched_at: '2026-06-28T22:39:12.876958+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - O controle de código
  interno está habilitado, nesse caso, o endereçamento deverá ser pelo pelas rotinas
  do ACD" como corrigir ?
type: support-article
updated_at: '2025-02-13T18:36:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29968130601623-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-O-controle-de-c%C3%B3digo-interno-est%C3%A1-habilitado-nesse-caso-o-endere%C3%A7amento-dever%C3%A1-ser-pelo-pelas-rotinas-do-ACD-como-corrigir
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29968121668503) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Quando apresenta a mensagem " O controle de código interno está habilitado, nesse caso, o endereçamento deverá ser pelo pelas rotinas do ACD" como corrigir.   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Essa mensagem é setada devido ao parâmetro [MV\_ACDCB0](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14441132913943-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-MV-ACDCB0-quais-op%C3%A7%C3%B5es-dispon%C3%ADveis-no-par%C3%A2metro) do seu ambiente está preenchido. Esse parâmetro faz controle de integração de processos com o modulo SIGAACD(Automação e Coleta de Dados) que valida a integração através do parâmetro MV\_INTACD.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29968130591511)  
  
Quando utilizado MV\_ACDCB0 = Vazio, é possível realizar o endereçamento através da rotina padrão do módulo Estoque MATA265.  
  
Agora quando o  MV\_ACDCB0 = 01, obrigatoriamente deverá ser utilizada a rotina do coletor ACDV060, usando os emuladores VTDEBUG ou TERA TERM.   
  
Se deseja endereçar somente pela rotina MATA265, basta deixar MV\_ACDCB0 = Vazio.

***Saiba Mais:***

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV060 - Pontos de Entrada disponíveis na rotina*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13408354022551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV060-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina)
