---
article_id: 37350638069143
category: Financeiro - Novo Gestor Financeiro
content_hash: 850d96e1777b3a31bcb59467dec70c501c8e599e0da309e0760a3a9812205d91
fetched_at: '2026-06-28T22:37:41.526420+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA713 - Santander
  - Error: java.lang.Exception: Access denied: certificate not found'
type: support-article
updated_at: '2025-12-31T11:03:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37350638069143-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Santander-Error-java-lang-Exception-Access-denied-certificate-not-found
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37350610560279) Tempo aproximado para leitura: **03:00 min**

**Dúvida:**  
Ao realizar a transmissão de boleto para o banco **Santander** através da rotina Novo Gestor Financeiro (FINA710), ocorre o erro: "Error: java.lang.Exception: Access denied: certificate not found". O que deve ser verificado?  
  
**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - 12.1.2210 e superiores

**Solução:**

A mensagem de erro ocorre quando há uma rejeição por parte do banco **Santander** em relação ao certificado digital utilizado. Este cenário é comum quando o cliente ativa junto instituição bancária uma comunicação via **API**, enquanto o processo de transmissão de boletos no Protheus para esta funcionalidade utiliza o formato **XML**.

Atualmente, a integração para cobrança eletrônica homologada no Protheus utiliza o XML, e a integração direta via API para este processo específico não está disponível como padrão.

Para corrigir a situação, certifique-se de que o contrato e a configuração junto ao banco estejam parametrizados para a modalidade de transmissão de arquivos compatível com o Protheus, e não exclusivamente via API.

I**mportante: Este retorno é destinado para uso no processo de comunicação com o banco Santander.**
