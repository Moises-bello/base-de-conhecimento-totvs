---
article_id: 360050784254
category: Encargos
content_hash: f14d9ecdd3f50a932e1fbf85350df9503b83b9da41804ba2786a18fd3e45b8f0
fetched_at: '2026-06-28T22:46:53.308020+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - A partida do lançamento não pode ser incluída
type: support-article
updated_at: '2025-03-12T13:54:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050784254-RH-RM-FOP-A-partida-do-lan%C3%A7amento-n%C3%A3o-pode-ser-inclu%C3%ADda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:20 min  
  
Dúvida**  
Como corrigir o erro **A partida x do Lançamento xxxxx** não pode ser incluída pois o Histórico Padrão **xxx** tem complemento obrigatório e o complemento da partida não foi informado. No processo geração dos lançamentos contábeis.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**S****olução**O erro é apresentado pelo sistema quando se utiliza Complementos de Histórico e algumas verbas não possuem o campo **complemento** informado.  
  
1. Primeiramente, devemos verificar nos Lotes Contábeis se as verbas possuem o campo **Complemento** preenchido:  
  
![](https://totvssuporte.zendesk.com/attachments/token/llLIqfXjnbs3EIDO1WJ4ROwSe/?name=inline-388963919.png)  
  
2. Esse complemento deverá ser preenchido dentro do Cadastro do Evento, acessando o menu **Administração de Pessoal | Eventos | Eventos**:  
![](https://totvssuporte.zendesk.com/attachments/token/gaFcfFAjtqJviyVdtp4yar8Ti/?name=inline2055198703.png)  
  
3. Esse complemento precisa ser preenchido também dentro do Cadastro do Encargo, acessando o menu **Encargos | Cadastros | Encargos**:  
![](https://totvssuporte.zendesk.com/attachments/token/ftyYRvz40q4tZphJoIP36d2Rh/?name=inline-814596497.png)  
  
Após informar os Complementos do Histórico nos Encargos e nos Eventos, o erro deixará de ser exibido e será possível realizar o Lançamento Contábil.
