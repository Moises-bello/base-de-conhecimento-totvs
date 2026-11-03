---
article_id: 17158119200663
category: Faturamento - Cadastros
content_hash: de20001e312dac69c3964ceb9e87aeb37a3b5bf108336b6ccb8212bab4749075
fetched_at: '2026-06-28T22:38:36.655814+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Nota sobre grupo
  econômico no cadastro do cliente
type: support-article
updated_at: '2023-09-04T13:33:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17158119200663-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-sobre-grupo-econ%C3%B4mico-no-cadastro-do-cliente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17158070396695) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Nota sobre grupo econômico no cadastro do cliente  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

No cadastro de clientes, por padrão do Protheus,  não há um campo específico de Grupo Econômico ou mesmo um sub cadastro que possa ser associado a ele.  
Hoje, existe o campo A1\_GRPVEN - (Grupo de Vendas) localizado na Aba Vendas do cadastro do Cliente no qual pode relacionar todos os clientes do mesmo Grupo.  
Porém, é um campo para controle, e não para interferir nos processamentos do sistema.  
   
Dentro do módulo Faturamento, o campo pode ser usado nas rotinas Regra de Negocio, Regra de Desconto, Regra de Bonificação, Cadastro de Regras por margem mínima e Verbas de Venda.  
O campo não será considerado na rotina posição de cliente.

O campo está associado ao cadastro de grupo de clientes, para cadastrar, acesse a rotina FATA110 - Grupos de clientes e crie o grupo.

Depois disso, acesse a rotina de cadastro de cliente, CRMA980 (Antiga MATA030), e vá no campo A1\_GRPVEN e pesquise pelo grupo criado para declarar o cliente "X" pertencente a determinado grupo:

![cadstro do cliente 1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/17159144379031)

![cadstro de grupo de vendas.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/17159129604887)
