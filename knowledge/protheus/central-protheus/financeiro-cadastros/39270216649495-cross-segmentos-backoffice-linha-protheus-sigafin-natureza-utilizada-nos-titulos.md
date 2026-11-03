---
article_id: 39270216649495
category: Financeiro - Cadastros
content_hash: 1063582f8e621aa8a8d2fe85184a726341213b7618fa877cbba1b1a8d991a0e4
fetched_at: '2026-06-28T22:37:53.207832+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Natureza utilizada
  nos titulos de retenção de impostos
type: support-article
updated_at: '2026-03-25T13:39:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39270216649495-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Natureza-utilizada-nos-titulos-de-reten%C3%A7%C3%A3o-de-impostos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39270262016407)****Tempo aproximado para leitura:****00:06 min**

**Dúvida**  
Existe parametrização no padrão que permita que os títulos de retenção de impostos (IRRF, PCC, ISS, INSS) herdem a natureza do título principal no módulo Financeiro?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Financeiro - Todas as versões  
  
**Solução**  
No comportamento padrão do Protheus, os títulos de retenção de impostos não herdam a natureza do título principal (título “pai”). A definição da natureza desses títulos é realizada de forma fixa, por meio de parâmetros específicos do módulo Financeiro.

Os principais parâmetros são:

* **IRRF**  
  **MV\_IRF** – Define a natureza utilizada para o Imposto de Renda
* **PCC (PIS/COFINS/CSLL)**  
  **MV\_PISNAT** – Natureza para títulos de PIS  
  **MV\_COFINS** – Natureza para títulos de COFINS  
  **MV\_CSLL** – Natureza para títulos de CSLL
* **ISS**  
  **MV\_ISS** – Define a natureza dos títulos de ISS
* **INSS**  
  **MV\_INSS** – Define a natureza dos títulos de INSS

---

**Alternativa**

Caso haja necessidade de um controle mais específico, é possível utilizar o **Configurador de Tributos**. Nesse cenário, a natureza pode ser definida por fornecedor, por meio de regras financeiras aplicadas na geração dos títulos.

No entanto, é importante considerar que essa abordagem exige a criação e manutenção de regras individuais por fornecedor.

Saiba Mais:

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - How to configurador de tributos regra financeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33852958399767-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-How-to-configurador-de-tributos-regra-financeira)
