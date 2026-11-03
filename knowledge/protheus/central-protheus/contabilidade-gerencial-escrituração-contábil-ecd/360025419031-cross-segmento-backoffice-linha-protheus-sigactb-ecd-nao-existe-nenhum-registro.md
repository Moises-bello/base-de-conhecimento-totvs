---
article_id: 360025419031
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 3157e58db288ed4dcf62df01f2f5286e19c6122c0dfa0564a6939249b1448f7f
fetched_at: '2026-06-28T22:40:45.669148+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: ECD NAO EXISTE NENHUM
  REGISTRO J800 COM J800.TIPO_DOC= 10, 11, 12 OU 99 ATRELADO'
type: support-article
updated_at: '2024-04-22T19:27:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025419031-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-NAO-EXISTE-NENHUM-REGISTRO-J800-COM-J800-TIPO-DOC-10-11-12-OU-99-ATRELADO
---

**Ocorrência:**

**J100** Foi informado código de nota explicativa para demonstração sendo validada mas não existe nenhum registro J800.TIPO\_DOC=10,11,12 ou 99 atrelado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023962432)  
   
 **Ambiente**Protheus – Contabilidade Gerencial– A partir da versão 12.1.17  
  
   
**Solução**Ao relacionar um identificador de nota explicativa (NOTA\_EXP\_REF) para os demonstrativos (J100, J150 e/ou DMPL)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023963112)

É necessário informar o campo "tipo de documento"  TIPO\_DOC (Campo 02) do registro J800, igual a :

“010 – Notas Explicativas”,

“011 – Relatório da Administração”,

“012 – Parecer dos Auditores” ou

“999 – Outros”

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023987331)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023963232)

Saiba mais:

<http://tdn.totvs.com/display/PROT/ECD_SPED_CONTABIL_Alteracoes_para_Leiaute_7_00>
