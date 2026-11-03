---
article_id: 1500002593642
category: NFe - Nota Fiscal Eletrônica
content_hash: 63854c275c7573e2603dceca8d5978efbd5c3f0ba0f99a26e082da6d34ad65fc
fetched_at: '2026-06-28T22:40:05.047985+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 440 Rejeição :
  CNPJ do intermediador da transação inválido'
type: support-article
updated_at: '2025-07-14T14:08:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002593642-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-440-Rejei%C3%A7%C3%A3o-CNPJ-do-intermediador-da-transa%C3%A7%C3%A3o-inv%C3%A1lido
---

**Dúvida**Como solucionar a rejeição 440 : CNPJ do intermediador da transação inválido ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

1- Se informado **Indicador do Intermediador IGUAL a “1=Operação em site ou plataforma de terceiros (intermediadores/marketplace)”**

De ser vinculado o intermediador através do campo no pedido de vendas  Código do intermediador **C5\_CODA1U**  no Documento de entrada **F1\_CODA1U**

 2- O intermediador vinculado será Obrigatório o preenchimento das Informações do **Intermediador da Transação no Menu e campos abaixo**

![intermediador_campos.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/33452783791767)

3- Corrija o conteúdo do campo **A1U\_CNPJ "CNPJ do Intermediador" Verificar CNPJ com zeros, nulo ou DV inválido.**

4- Após isso, **exclua a nota e gere novamente.**

* **Validação da Sefaz:**

![440_rejeicao.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007826941)
