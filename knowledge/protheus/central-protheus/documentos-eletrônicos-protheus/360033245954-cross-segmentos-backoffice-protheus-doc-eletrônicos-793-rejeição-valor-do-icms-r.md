---
article_id: 360033245954
category: Documentos Eletrônicos Protheus
content_hash: fea6799b4097715a304bb02ab2088df9a94ef994abc338e2e5262c16e45d1250
fetched_at: '2026-06-28T22:36:30.959146+00:00'
product: protheus
section_id: 1500001533661
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 793 Rejeição: Valor
  do ICMS relativo ao Fundo de Combate à Pobreza na UF de destino difere do calculado'
type: support-article
updated_at: '2026-06-25T17:18:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033245954-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-793-Rejei%C3%A7%C3%A3o-Valor-do-ICMS-relativo-ao-Fundo-de-Combate-%C3%A0-Pobreza-na-UF-de-destino-difere-do-calculado
---

**Dúvida**  
Como corrigir a rejeição abaixo

793 Rejeição: Valor do ICMS relativo ao Fundo de Combate à Pobreza na UF de destino difere do calculado ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

**Solução**

Ao fazer nota de **operação interestadual, para consumidor final e não contribuinte** a Sefaz espera que seja gerado o grupo no XML**ICMSUFDest.**

* **Conforme o XML de exemplo abaixo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070604354)

1- A rejeição ocorre quando **não gera o calculo da**  TAG abaixo conforme o **Exemplo:**

**<vFCPUFDest>13.26</vFCPUFDest>**

* A Sefaz fará o seguinte calculo:  
    
  <vBCUFDest>663.12</vBCUFDest> \*  <pFCPUFDest>2.0000</pFCPUFDest> / 100   
    
    
  =<vFCPUFDest>13.26</vFCPUFDest>

* O conteúdo das TAGS são levados da tabela **CD2:**  
    
  **Tag** vBCUFDest -> CD2\_BC

**Tag** pFCPUFDest -> CD2\_PFCP

**Tag**vFCPUFDest -> CD2\_VFCP

2- Se o valor do calculo acima estiver errado configurar a nota **conforme o link abaixo:**

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=287056662>

3- Após isso, exclua a nota e gere novamente.

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042617314)**
