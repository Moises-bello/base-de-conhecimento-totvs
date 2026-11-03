---
article_id: 360006658632
category: Contabilidade Gerencial - Centro de Custo
content_hash: a4df990273701811b5fc96cb42efb1787497ca75cce2ddfd565feb703b8f85d5
fetched_at: '2026-06-28T22:41:02.006865+00:00'
product: protheus
section_id: 1500001537341
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA030 -  Help: QD_QUALITY
  - APRESENTADO NA ALTERAÇÃO/INCLUSÃO CENTRO DE CUSTO'
type: support-article
updated_at: '2025-01-22T23:43:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006658632-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA030-Help-QD-QUALITY-APRESENTADO-NA-ALTERA%C3%87%C3%83O-INCLUS%C3%83O-CENTRO-DE-CUSTO
---

**Ocorrência**Ao realizar Alteração/Inclusão de centro de custo pela rotina CTBA180/CTBA030 é exibido o seguinte

**Help** : QD\_QUALITY

**Problema**:

Existe incompatibilidade de compartilhamento entre as tabelas **QAD** e **SI3**. Contactar o Administrador do Sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007161732)

**Ambiente**  
Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Causa:****Situação pode ser ocasionada  caso haja integração dos módulos do Quality**

* **Tabelas:**
  + QAD - Departamento.
  + SI3 - Centros de Custos.
  + CTT - Centro de custo

**Solução:**

Para que a situação não seja presentada é necessário que o compartilhamento das tabelas abaixo estejam iguais:

* + QAD - Departamento.
  + SI3 - Centros de Custos.
  + CTT - Centro de custo
