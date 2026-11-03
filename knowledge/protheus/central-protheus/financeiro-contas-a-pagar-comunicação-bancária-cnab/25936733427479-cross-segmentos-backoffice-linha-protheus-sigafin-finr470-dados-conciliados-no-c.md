---
article_id: 25936733427479
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 43ff11e7eacd9c2878a542bd457b8f35a4d6ed07339c5e70fff578959232dcbb
fetched_at: '2026-06-28T22:37:56.376931+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR470 - Dados conciliados
  no Conciliador não aparecem no Extrato Bancário
type: support-article
updated_at: '2024-08-27T13:46:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25936733427479-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR470-Dados-conciliados-no-Conciliador-n%C3%A3o-aparecem-no-Extrato-Banc%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25936717099543) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**

No módulo Financeiro, ao tentar realizar a conciliação na **CTBA940**, e validar no **FINR470** com o pergunte **Conciliacao ? = Conciliados** não aparece no Extrato Bancário

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2310  
  
**Causa**O **Novo Conciliador BackOffice - CTBA940** foi desenvolvido para atender as conciliações de N módulos, porém, sua visão já está integrada ao **SmartView**, no qual ações, por exemplo, de **Conciliação Manual / Automática** para controle das movimentações financeiras, se faz necessário ter o **Smart-View** configurado.

O objeto de negócio Extrato Bancário pode ser executado via menu do Protheus através do programa **FINSV014**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25936733400727)

**Saiba mais**  
**[Smart View - Configuração do produto Protheus integrado ao Smart View](https://tdn.totvs.com/pages/releaseview.action?pageId=665287989)**

**[Conciliadores Bancários Manual e Automático (FINA380 e FINA473)](https://tdn.totvs.com/pages/releaseview.action?pageId=754946735)**
