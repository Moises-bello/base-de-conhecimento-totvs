---
article_id: 1500001245802
category: Financeiro - Contas a Pagar - PIX
content_hash: 44ec31505edeaf25b5bebadb3d6cabe7d8338f925823b1e9016a88d2f81248bc
fetched_at: '2026-06-28T22:38:11.336564+00:00'
product: protheus
section_id: 1500001550462
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA420 - QR CODE Pix
  estático X dinâmico '
type: support-article
updated_at: '2023-06-26T01:55:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001245802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA420-QR-CODE-Pix-est%C3%A1tico-X-din%C3%A2mico
---

**Dúvida**Qual a diferença entre o QR CODE do PIX estático e o dinâmico?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Financeiro - FINA420 - A partir da versão 12.1.23  
  
**Solução**Estático: O mesmo QR CODE poderá ser usado em várias transações e permite um valor fixo.  
Dinâmico: Uso exclusivo em cada transação, permitindo outros dados além do valor, como por exemplo identificação do recebedor. Facilita a conciliação.  
  
**Exemplos**Estático: Pipoqueiro com um QR CODE com o preço da pipoca doce e outro QR CODE com o preço da pipoca salgada.  
Dinâmico: Pagamento de contas diversas ou mesmo através do CNAB.  
  
**Importante**O Protheus está preparado para trabalhar apenas com o modelo de QR CODE Dinâmico.  
  
Lembramos que somente QR Codes Dinâmicos são enviados para o CNAB de pagamento nativamente com o modelo disponibilizado pelo **CNAB CLOUD**. Como exemplo de diferença entre um QR Code Dinâmico e Estático, após ser decodificado, podemos citar que o **Dinâmico tem uma URL** e o **Estático tem a chave Pix do recebedor** :

* **Exemplo Fictício de um QR Code Dinâmico :**  
  00020101021226740014br.gov.bcb.pix2552example.com/pix/8baaa2f3-9c41-40d1-a91a-bc93113bd4415204000053039865406123.455802BR5913Fulano de Tal6008BRASILIA62190515RP12345678-20196304FA24
* **Exemplo Fictício de um QR Code Estático:**  
  00020101021126440014br.gov.bcb.pix0122fulano2019@example.com5204000053039865802BR5913FULANO DE TAL6008BRASILIA6304DAE3   
    
  **Saiba mais**  
  <https://tdn.totvs.com/pages/releaseview.action?pageId=569478747>
