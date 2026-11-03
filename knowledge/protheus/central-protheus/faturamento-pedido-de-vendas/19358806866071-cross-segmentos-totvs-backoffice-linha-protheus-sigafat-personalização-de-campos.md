---
article_id: 19358806866071
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 9895730a485e5fbfea527482918f4a4a13536d30477f66f1daafb2d1807ffb04
fetched_at: '2026-06-28T22:38:42.769619+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Personalização
  de Campos nas Visões do browser nos módulos de Faturamento e CRM
type: support-article
updated_at: '2024-12-31T12:43:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19358806866071-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Personaliza%C3%A7%C3%A3o-de-Campos-nas-Vis%C3%B5es-do-browser-nos-m%C3%B3dulos-de-Faturamento-e-CRM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19358827222423) Tempo aproximado para leitura: **00:02:00 min**

## **Dúvida**

Como personalizar campos de visões no browser nos módulos de Faturamento e CRM?  
  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões  
  
  
Dúvida:  
  
**1. Visão "Exibir todos"**

A visão "Exibir Todos" é a única que carrega os campos configurados pelo cliente no browse do MATA410. Isso significa que reflete exatamente as configurações individuais do usuário em relação aos campos exibidos.  
  
**2. Outras Visões Padrões**

As visões "Meus Pedidos", "Pedidos Abertos", "Pedidos Bloqueados por Regra", "Pedidos Bloqueados por Verba", "Pedidos Encerrados" e "Pedidos Liberados" possuem campos fixos. Esses campos são criados de acordo com as regras estabelecidas no módulo de Faturamento e CRM.  
  
  
**Solução:**

Caso seja necessário substituir as visões padrões do Faturamento e CRM, existe um ponto de entrada específico chamado "CRMBRWVIEW". Este ponto de entrada oferece a flexibilidade necessária para personalizar as visões de acordo com as necessidades específicas do usuário.  
  
**Ponto de entrada:**

O ponto de entrada "CRMBRWVIEW" é uma ferramenta essencial para a personalização das visões do browser.  
Ele permite que os usuários substituam as visões do browser padrões por visões personalizadas, alinhadas com suas preferências e requisitos operacionais.  
  
**Exemplo:**

1. Suponha que um usuário deseje substituir a visão padrão "Meus Pedidos" por uma versão personalizada.
2. Utilize o ponto de entrada "CRMBRWVIEW" para realizar essa modificação, adaptando a visão de acordo com as necessidades específicas do usuário.  
     
   **Saiba mais:**Para obter uma orientação detalhada sobre a utilização do ponto de entrada "**CRMBRWVIEW**", consulte a documentação disponível em: [CRMBRWVIEW - Substituição das Visões Padrão do CRM](https://tdn.totvs.com/pages/releaseview.action?pageId=244727349)
