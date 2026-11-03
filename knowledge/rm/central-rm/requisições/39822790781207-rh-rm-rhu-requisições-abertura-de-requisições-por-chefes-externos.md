---
article_id: 39822790781207
category: Requisições
content_hash: dcc01b64dd1a100d89b2d3df58b275a614233fd893dc905e211d23da80e2604c
fetched_at: '2026-06-28T22:47:25.280665+00:00'
product: rm
section_id: 1500000861382
source: central-rm
title: 'RH - RM - RHU - Requisições: Abertura de Requisições por Chefes Externos'
type: support-article
updated_at: '2026-04-17T14:35:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39822790781207-RH-RM-RHU-Requisi%C3%A7%C3%B5es-Abertura-de-Requisi%C3%A7%C3%B5es-por-Chefes-Externos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39822790756375) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
É possível realizar a abertura de Requisições do módulo de Gestão de Pessoas por Chefes Externos?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **Todas as versões.**  
  
**Solução**  
Por padrão um Externo não poderá criar uma requisição mesmo que este esteja vinculado a uma Seção como Chefe Externo no cadastro de Chefes e Supervisores da Folha de Pagamento. A abertura de Requisições  não é possível com o uso deste tipo de Chefe pois, as chaves das tabelas de Requisição apontam para PFUNC (tabela responsável por armazenar dados de Funcionários) e não possuem relação com a PEXTERNO (tabela responsável por armazenar dados de Externos).

Sendo assim a rotina não permitirá a abertura de Requisições (independente do Tipo de Requisição) por Chefes Externos.

Apenas solicitantes que ***sejam Funcionários (possuam Chapa)*** poderão abrir Requisições, desde que tenham sido devidamente cadastrados como Chefes em alguma Seção no cadastro de Chefes e Supervisores da Folha de Pagamento.

Os Chefes Externos podem apenas participar do fluxo de aprovação através da criação de um Fluxo Customizado pelo TOTVS Aprovações e Atendimentos - TAA ( antigo RM Agilis).

 **Saiba Mais**

Para mais informações, acesse:

[RH - RM - RHU - Customizar o fluxo de requisições do Gestão de Pessoas (Vitae) integrado com o TOTVS Aprovações e Atendimento (Agilis)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034174194-RH-RM-RHU-Customizar-o-fluxo-de-requisi%C3%A7%C3%B5es-do-Gest%C3%A3o-de-Pessoas-Vitae-integrado-com-o-TOTVS-Aprova%C3%A7%C3%B5es-e-Atendimento-Agilis)
