---
article_id: 360018329292
category: PMS - Projetos
content_hash: f5b8fc0e5842b8abd49ddf6ae0eb61dcd359dbdc5b04221eaf73f6eefe82579c
fetched_at: '2026-06-28T22:37:14.912209+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Gerar Ordem de Produção através
  de Projetos
type: support-article
updated_at: '2024-02-23T12:14:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018329292-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Gerar-Ordem-de-Produ%C3%A7%C3%A3o-atrav%C3%A9s-de-Projetos
---

**Dúvida**Ordem de Produção através do Módulo Gestão de Projetos

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - A partir da versão 11.80  
  
**Solução**

Para a integração seguimos os passos abaixo;

1. Produto PA e produtos MP (Com saldo em Estoque);  
2. Estrutura do PRODUTO ACABADO –> Estoque -> Engenharia -> Estrutura;

![inline-461057036.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406110679319)

3. Nos itens da tarefa informar também o produto PA  quantidade e data de necessidade​;

![inline-1133244611.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406110725911)

4. Gerar o planejamento (este planejamento vai gerar a OP);

![inline692416940.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406102498967)

OBS : A solicitação de Compras inclua no mesmo projeto um ITEM sem saldo em estoque;

Deve ser criado uma estrutura de produto através da rotina MATA200 - Estrutura. Será necessário utilizar um Produtos do tipo produto acabado (PA) , e como componentes utilize o tipo do produto intermediário (PI), matéria prima (MP), entre outros.

![pmsop.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4406102734999)

**Detalhes em : [PMS0013\_Gerar ordem de produção através do projeto](https://tdn.totvs.com/x/bYVUE)**
