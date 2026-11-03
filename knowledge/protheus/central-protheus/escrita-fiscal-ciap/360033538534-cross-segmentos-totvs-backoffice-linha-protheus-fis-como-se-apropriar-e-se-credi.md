---
article_id: 360033538534
category: Escrita Fiscal - CIAP
content_hash: 3fe3d3013325421bfa1113811ccb63a64ac7e4eab5378d93d31c91bdf4d65808
fetched_at: '2026-06-28T22:39:33.837583+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como se apropriar
  e se creditar no CIAP somente do ICMS ST de fornecedor Simples Nacional
type: support-article
updated_at: '2021-07-29T13:11:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033538534-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-se-apropriar-e-se-creditar-no-CIAP-somente-do-ICMS-ST-de-fornecedor-Simples-Nacional
---

**[Remover as instruções entre colchetes]**  
**Dúvida**Como se apropriar e se creditar no CIAP somente do ICMS ST fornecedor Simples Nacional?  
  
**Ambiente**

Protheus  - Livros Fiscais - Todas as Versões  
  
**Solução**

Configurar a TES:

Credita ICMS = Sim  
Calcula ICMS = Não  
L. Fiscal ICMS = Outros  
Material de Consumo = Sim  
L. Ciap = Sim

Sit.Trib.ICM = 10

**Mkp ICM Comp. (F4\_MKPCMP)** = **Não;**

**Marg. Solid. (F4\_MKPSOL)** = **Configuração.**

Fornecedor:  
A2\_SIMPNAC = Sim

Produto

**Solid. Entr. (B1\_PICMENT)** - informe o MVA do produto para entrada.
