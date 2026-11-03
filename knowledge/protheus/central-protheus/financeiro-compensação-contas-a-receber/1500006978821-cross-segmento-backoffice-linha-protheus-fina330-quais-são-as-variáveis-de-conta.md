---
article_id: 1500006978821
category: Financeiro - Compensação Contas a Receber
content_hash: 8a466dda4f6239539dcdd5952c9ff6c074f786ce6ffa923f92030d2c00e0909f
fetched_at: '2026-06-28T22:37:40.431734+00:00'
product: protheus
section_id: 35056224784407
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA330 - Quais são as variáveis
  de contabilização (online e off-line) da Compensação de Contas à Receber
type: support-article
updated_at: '2026-01-21T16:40:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006978821-Cross-Segmento-Backoffice-Linha-Protheus-FINA330-Quais-s%C3%A3o-as-vari%C3%A1veis-de-contabiliza%C3%A7%C3%A3o-online-e-off-line-da-Compensa%C3%A7%C3%A3o-de-Contas-%C3%A0-Receber
---

**Dúvida**

Quais são as variáveis de contabilização (online e off-line) da Compensação de Contas à Receber?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA330 - CTBAFIN - Todas as versões  
  
**Solução**

Para contabilização do **Lançamento Padrão** **596**  (Compensação CR) **ONLINE**, as variáveis a seguir estarão disponíveis:

* **VALOR**- armazena o valor compensado  
  **VALORMF**- armazena o valor compensado na moeda correspondente do título  
  **VALOR2**- Valor de IRRF  
  **VALOR3**- Valor de PIS  
  **VALOR4**- Valor de COFINS  
  **VALOR5**- Valor de CSLL  
  **VALOR6**- Valor de INSS  
  **VALOR7**- Valor de decréscimos  
  **VALOR8**- Valor de acréscimos  
  **VARIACAO**- Variação da correção monetária  
  **ABATIMENTO**- Valores de abatimentos  
  **REGVALOR**- RECNO do registro atual  
  **STRLCTPAD**- Chave do título principal + número do documento

Para contabilização do **Lançamento Padrão 596**(Compensação CR) **OFFLINE (CTBAFIN)** e geração de impostos na **Baixa**, as variáveis a seguir estarão disponíveis:

* **VALOR**- Valor da NF compensada deduzindo os impostos/valores acessórios.  
  **VALOR2** - ISS  
  **VALOR3**- INSS  
  **VALOR4**- IRRF  
  **VALOR5**- PIS  
  **VALOR6**- COFINS  
  **VALOR7**- CSLL  
  **VALOR8**- Valor acréscimo  
  **VALOR9**- Valor decréscimo  
  **VARIACAO**- Variação da correção monetária da NF  
  **VARIACAORA**- Variação da correção monetária do RA

**REGVALOR**- RECNO da NF

Para contabilização do **Lançamento Padrão 588**(Estorno de compensação CR) **ONLINE**, as variáveis a seguir estarão disponíveis:

* **VALOR**- Valor compensado  
  **VALOR2** - Valor de IRRF  
  **VALOR3**- Valor de PIS  
  **VALOR4**- Valor de COFINS  
  **VALOR5**- Valor de CSLL  
  **VALOR6**- Valor de INSS  
  **VALOR7**- Valor de decréscimos  
  **VALOR8**- Valor de acréscimos  
  **VARIACAO**- Variação da correção monetária  
  **REGVALOR** - RECNO do registro atual  
    
  **Saiba Mais**  
  [Variáveis de contabilização da Compensação de Contas à Receber (online e offline)](https://tdn.totvs.com/pages/releaseview.action?pageId=233747403)
