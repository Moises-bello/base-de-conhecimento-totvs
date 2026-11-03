---
article_id: 36322177178903
category: Financeiro - Manutenção de Extratos
content_hash: abc5882edf119e0450d38a96b36ce6e6286ff45c04f654a355d4c0f6a0929aca
fetched_at: '2026-06-28T22:37:31.198090+00:00'
product: protheus
section_id: 35057672519319
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA474 - Importação
  de arquivo extensão OFX ou OFC
type: support-article
updated_at: '2025-11-14T18:47:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36322177178903-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA474-Importa%C3%A7%C3%A3o-de-arquivo-extens%C3%A3o-OFX-ou-OFC
---

**Dúvida:**  
É possivel importar arquivos de extratos utilizando a extensão OFX ou OFC?

**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210 e superior

**Solução**  
Não é possível realizar a importação de extratos com a extensão **OFX** ou **OFC** diretamente nas rotinas nativas do Protheus Financeiro (SIGAFIN).  
   
O padrão homologado e suportado pela TOTVS para a comunicação bancária (incluindo a importação de extratos e conciliação) é o uso de arquivos no formato **CNAB (Febraban)**, que geralmente possuem a extensão .**RET** (Retorno).
