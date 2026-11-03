---
article_id: 33875575382295
category: SIGAACD - Automação e Coleta de Dados
content_hash: b6499fb6c285d6eadf4669f389eca20e38911873efe803f6ca1bc7d5066dfd67
fetched_at: '2026-06-28T22:39:12.766331+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Liberacao parcial
  de saldos na CB0 com CQ
type: support-article
updated_at: '2025-08-01T14:43:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33875575382295-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Liberacao-parcial-de-saldos-na-CB0-com-CQ
---

O artigo aborda a questão da liberação de saldos parciais no controle CB0 no TOTVS Backoffice (Linha Protheus). Esclarece que, no conceito padrão, não é possível realizar baixas parciais. Caso o cliente precise realizar baixas parciais, é necessário estornar todo o processo e criar etiquetas conforme desejado. Existe um parâmetro, "MV\_CBAJUQE", que permite ajustar a quantidade por embalagem na impressão de etiquetas. Para sugestões de melhorias, os usuários são incentivados a utilizar a Central Colaborativa TOTVS. Links para mais informações e vídeos explicativos são fornecidos.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33875575365783) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Posso efetuar a liberacao de saldos parciais com controle na CB0, em baixas do armazem de qualidade seja liberação ou rejeição?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
No conceito padrão da **CB0 não é possivel o controle de saldos parciais (Baixas parciais).**

Caso o Cliente precise fazer a baixa de peças via rotina **MATA175** de forma parcial, é necessario fazer o estorno de todo o processo e dar entrada criando as etiquetas da forma que se deseja liberar.

Ainda existe um parametro chamado "**MV\_CBAJUQE**" que tem o objetivo de permitir ao usuario ajustar a Quantidade por Embalagem na rotina de impressão de etiquetas produtos.

**MV\_CBAJUQE =** Permite ajustar a quantidade por embalagem no relatório Etiqueta Produto NF.  
Conteudo: T – Habilita o ajuste da quantidade por embalagem  
Conteudo: F – Desabilita o ajuste da quantidade por embalagem

<https://tdn.totvs.com/pages/releaseview.action?pageId=235596091>

### **Caso necessite que exista o controle de forma parcial na baixa de CQ:**

A situação reportada nessa solicitação trata-se de uma sugestão de melhoria no produto e deve ser incluída na [**Central Colaborativa TOTVS**](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics), localizada em nosso [**Portal do Cliente**](http://suporte.totvs.com/). É um espaço que você poderá sugerir melhorias, acompanhar a evolução das solicitações já realizadas, comentar, seguir, votar em sugestões feitas por outros clientes e muito mais!

Para conhecer mais sobre as suas **funcionalidades** clique [**AQUI**](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13)e assista o nosso vídeo ou acesse nosso artigo [**Central Colaborativa - Funcionalidades Disponíveis**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466814-Funcionalidades-Dispon%C3%ADveis-na-Central-Colaborativa-TOTVS)**​**.

Você pode acompanhar as suas **sugestões** e **comentários** clicando [**AQUI**](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)**.**  
Acompanhe as **Novidades da Release** clicando [**AQUI**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360009734433-Ciclo-de-Vida-Relat%C3%B3rio-de-Releases).

***Saiba Mais:***  
[*Clique aqui e veja mais artigos sobre o módulo SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017498572/preview/eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MzYwMDE3NDk4NTcyLCJleHAiOjE2Nzg3MzQ5NzN9.TiaFwHli6haWXaeQkUGagxeLmg_dX2xufhmov32ozTQ)
