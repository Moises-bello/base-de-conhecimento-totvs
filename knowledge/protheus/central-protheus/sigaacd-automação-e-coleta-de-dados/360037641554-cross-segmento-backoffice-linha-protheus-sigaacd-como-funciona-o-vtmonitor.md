---
article_id: 360037641554
category: SIGAACD - Automação e Coleta de Dados
content_hash: 9dca723556e23132bb81bdf0107b866618e28c871aee9500ad16cc6b3cefea4f
fetched_at: '2026-06-28T22:39:12.580326+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como funciona o VTMONITOR.
type: support-article
updated_at: '2025-03-12T12:45:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037641554-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-funciona-o-VTMONITOR
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24763225303703) Tempo aproximado para leitura: **00:01:00 min***  
**Dúvida**Como funciona rotina VTACDMONIT?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17   
  
**Solução**

Para o correto funcionamento da rotina habilitar o **MV\_VTLOGIN**- Parâmetro responsável efetuar o login ou não do **VtMonitor**, caso o parâmetro esteja como .T. o usuário só irá acessar a rotina no modulo de estoque quando tiver o logado no sistema e o mesmo tiver permissão para o acesso, caso esteja como .F. o usuário irá acessar a rotina da mesma maneira que é acessada hoje abrindo o smartclient e acessando a rotina. O valor padrão do parâmetro é .T.

Acessar via smatclient o **VTDEBUG** e depois acessar a rotina.

Os módulos que irão parecer no menu serão :

SIGAEST | SIGACOM | SIGAFAT E SIGAWMS

**Fonte envolvido:** VtMonit.prw

**Saiba Mais:**  
[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas#:~:text=Saiba%20Mais%3A,Coleta%20de%20Dados)
