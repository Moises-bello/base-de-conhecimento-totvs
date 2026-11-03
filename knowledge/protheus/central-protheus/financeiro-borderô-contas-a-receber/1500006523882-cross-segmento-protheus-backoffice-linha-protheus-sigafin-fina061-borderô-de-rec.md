---
article_id: 1500006523882
category: Financeiro - Borderô contas a Receber
content_hash: 0f044256334d5c3a27626b78c92436c0bcdda83d63b617d32a023a9e0756f8e9
fetched_at: '2026-06-28T22:37:39.735938+00:00'
product: protheus
section_id: 35057237655191
source: central-protheus
title: Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN - FINA061 - Borderô
  de Recebimento de Impostos
type: support-article
updated_at: '2025-11-26T20:01:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006523882-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-FINA061-Border%C3%B4-de-Recebimento-de-Impostos
---

**Dúvida**  
Como gerar borderô de recebimento de impostos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA061 - Todas as versões  
  
**Solução**

Semelhante ao **FINA060**, existe uma opção de borderô em que é possível preencher os parâmetros para a seleção de títulos e definir o **Portador** e a **Situação de cobrança.**

**Regras:**

* **Pessoa Jurídica:**

**Física/Jurídica(A1\_PESSOA) = J (Jurídica)**

* **PCC:**  
  **Retenção na baixa** **(MV\_BR10925 = 1)**
* **IRRF:**

**Retenção na baixa:**

**Tp. Entidade(A1\_ENTID) = Diferente de 00, 02 ou 10. (Cadastro do Cliente/Aba Fiscal)**

**IRPJ Baixa(A1\_IRBAX) = 1 (Sim)**

**Recolhe IRRF(A1\_RECIRRF) = 1 (Sim)**

* As situações que não utilizam portador não devem gerar os títulos dos impostos **(PCC e IR).**
* A rotina de **Borderô Rec. Impostos (FINA061.PRX)** deve ser substituída pelo uso da rotina **Transferências (FINA060.PRX).**
* Os títulos referentes aos **impostos (IRRF e PCC)** gravados na tabela **SE1** terão o status baixado e a chave do titulo pai (origem de retenção).
