---
article_id: 360045900994
category: NFe - Nota Fiscal Eletrônica
content_hash: b1822652d23b89c3f8193734e3620a969d96920713eb6d4f175059d704496ccb
fetched_at: '2026-06-28T22:40:03.819858+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 255 Rejeição :
  NF-e complementar possui mais de uma NF referenciada'
type: support-article
updated_at: '2025-06-18T14:31:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045900994-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-255-Rejei%C3%A7%C3%A3o-NF-e-complementar-possui-mais-de-uma-NF-referenciada
---

**Dúvida**Como corrigir a rejeição 255 : NF-e complementar possui mais de uma NF referenciada ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**Se feita no sistema uma nota de  complemento, será gerada a **TAG finNFe=2**

**1. Documento de entrada:**

**![complemento_de_entrada.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/13465518514199)**

**2. Pedidos de Vendas:**

![pedidos_de_venda.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/13465839932567)

2. Verificar as notas  **referenciadas ao documento** de origem corretamente, e a espécie das notas nos campos **F2\_ESPECIE ou F1\_ESPECIE, F3\_ESPECIE e FT\_ESPECIE**

D2\_ITEMORI, D2\_SERIORI, D2\_NFORI **(nota de saída)**

![referecia_nt_saida.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896221533591)

D1\_ITEMORI, D1\_SERIORI, D1\_NFORI **(nota de entrada)**

**![referecia_nt_entrada.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896221535639)**

Se a mesma for referenciada manualmente deve se preencher os campos **NF . Ori , Serie Ori e Item Ori** .   
  
Se for preenchido automaticamente pelo gatilho **F4 (Nota de saída) ou F7 (Nota entrada)** os campos são alimentados automaticamente.

**![F1_ESPECIE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896221543191)**

3. Em caso de complemento a Sefaz não permite que seja referenciada mais de uma ocorrência **(NF-e, NFC-e, NF modelo 1)**

Sendo assim, se foi  referenciada mais de uma ocorrência, será necessário excluir a nota criar notas separadas e gerar novamente.

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064783554)
