---
article_id: 39473387491991
category: Contabilidade Gerencial - Entidades
content_hash: 15689b45dd7380f8086443ea5709b7a9999f02c66350e2b700a28fec5fc5fe78
fetched_at: '2026-06-28T22:40:49.782722+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial
  (SIGACTB) - CTBA080 - Carga inicial de Lançamentos Padronizados (LPs)
type: support-article
updated_at: '2026-04-02T17:51:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39473387491991-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Contabilidade-Gerencial-SIGACTB-CTBA080-Carga-inicial-de-Lan%C3%A7amentos-Padronizados-LPs
---

A funcionalidade de inclusão e carga inicial de Lançamentos Padronizados (LPs) no Protheus realiza uma carga automática na tabela CT5, usando a tabela de relacionamentos CTL, abrangendo códigos de 500 a 9ZZ. O processo é feito pela rotina Lançamentos Padrões (CTBA080), acessando "Outras Ações" e selecionando "Carga de LP", seguindo as orientações para concluir a carga.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39479048030615) Tempo aproximado para leitura: 00:05 min

**Dúvida**  
Como funciona a funcionalidade de inclusão e carga inicial de Lançamentos Padronizados (LPs) a partir da tabela CTL?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade Gerencial - a partir da release 12.1.2410

**Solução**  
O sistema disponibiliza a funcionalidade de carga inicial dos Lançamentos Padronizados (LPs), na qual é efetuada uma carga na tabela CT5. Esta carga contempla exemplos e regras simples de posicionamentos das tabelas que envolvem cada lançamento padrão.

O processo de Carga de LP realiza a inclusão automática de lançamentos padrões utilizando a tabela de relacionamentos (CTL). Esta rotina abrange a geração para os LPs a partir do código 500 até 9ZZ.

Acesse a rotina Lançamentos Padrões (CTBA080).  
No menu superior, clique em Outras Ações.  
Selecione a opção Carga de LP.  
Confirme e siga as orientações em tela para concluir o processamento da carga.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39473425704087)

**Saiba mais**  
[**Funcionalidade de Inclusão de Lançamentos Padronizados a partir da CTL**](https://tdn.totvs.com/pages/viewpage.action?pageId=704936549)
