---
article_id: 14785606827799
category: Faturamento - Cadastros
content_hash: 08b75a00693ae79e15e35aa59dd434c5d2448934f2aed544da24ac955fd87580
fetched_at: '2026-06-28T22:38:36.853918+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Campo "RG/Ced.Estr."
  (A1_PFISICA) não gera o código do cliente
type: support-article
updated_at: '2023-05-23T18:45:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14785606827799-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Campo-RG-Ced-Estr-A1-PFISICA-n%C3%A3o-gera-o-c%C3%B3digo-do-cliente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Ao preencher o campo "RG/Ced.Estr." (A1\_PFISICA) não é gerado o "Codigo" (A1\_COD) do cliente automaticamente?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

O campo "RG/Ced.Estr." (A1\_PFISICA) não possui a funcionalidade de criar o "Codigo" (A1\_COD) quando o CNPJ estiver em branco, a validação deste campo (função A030VldUCod) é específica para a integração Protheus x Datasul referente ao Código Único ([Cadastros e Código Único - Integração Protheus SIGATMS Datasul](https://tdn.totvs.com/x/m_byE))

A partir desta integração, é possível fazer a rotina criar o código do cliente de acordo com o código do fornecedor com mesmo CNPJ e Inscrição Estadual.

**Saiba mais:**

* [Clientes (MATA030 - SIGAFAT)](https://tdn.totvs.com/x/mQ8NF)
* [Pasta Cadastrais](https://tdn.totvs.com/x/og8NF)
* [Cadastro de Clientes Estrangeiros](https://tdn.totvs.com/x/zCMwDg)
