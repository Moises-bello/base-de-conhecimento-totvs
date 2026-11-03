---
article_id: 360063016093
category: PMS - Projetos
content_hash: 2e076826a2925ca05d51b16fb532c66d4445eebd9248737f674ba9035bebdde3
fetched_at: '2026-06-28T22:37:14.958449+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Projeto x Solicitação de
  Compras
type: support-article
updated_at: '2025-04-29T19:14:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063016093-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Projeto-x-Solicita%C3%A7%C3%A3o-de-Compras
---

**Dúvida**

Como integrar as Tarefas do projeto e Pedido de Compras?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as Versões

**Solução**

Siga as configurações para integração:

1. Parâmetros:

MV\_PMSCSC = .F.  
MV\_PMSREPL = 2  
MV\_PMSPREV = 2

**OBS:** O vínculo entre solicitação de compras e projeto se dará na tabela "AFG - Projeto x Solicitação de Compras"

2. A data da necessidade tem que ser menor que a data que esta sendo gerada o planejamento de execução;

![Screenshot_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406028075031)

3. Produto sem Saldo em Estoque ;

![PROJ_SC.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4406028273943)

**Saiba mais**:

**[PMS0006 Gerar Solicitação de Compras Através do Projeto](https://tdn.totvs.com/x/AoU_Dw)**
