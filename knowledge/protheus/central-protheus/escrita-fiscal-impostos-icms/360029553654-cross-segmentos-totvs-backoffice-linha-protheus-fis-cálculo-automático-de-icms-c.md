---
article_id: 360029553654
category: Escrita Fiscal - Impostos - ICMS
content_hash: 37d47a0b75613676cee8c0762a9deb20c2abf7ce523753448584d847a76b5f65
fetched_at: '2026-06-28T22:39:24.293147+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Cálculo Automático
  de ICMS com Alíquota de 7% nas Operações Interestaduais de Compra e Venda
type: support-article
updated_at: '2024-02-16T14:00:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029553654-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-Autom%C3%A1tico-de-ICMS-com-Al%C3%ADquota-de-7-nas-Opera%C3%A7%C3%B5es-Interestaduais-de-Compra-e-Venda
---

**Dúvida**  
Como configurar o Protheus para que possa calcular de forma automática de ICMS com Alíquota de 7% nas operações interestaduais de compra e venda.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Para que o sistema adote a alíquota de 7% de ICMS na operação de venda interestadual, o estado de destino deve ser informado no parâmetro **MV\_NORTE.**Para adotar alíquota de 7% de ICMS na operação de compra interestadual o parâmetro MV\_ESTADO deve ser informado algum estado que esteja informado no parâmetro **MV\_NORTE.** 

Exemplo de preenchimento do parâmetro MV\_NORTE:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21398587757719)  
  
Fluxo completo sobre alíquotas do ICMS :

**Cálculo do Sistema para localizar alíquota de ICMS para venda - (MATA103):**

**MV\_ESTADO: GO  
FORNECEDOR: MG**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21398587764247)**

**Cálculo do Sistema para localizar alíquota de ICMS para venda - (MATA410):**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21398598770455)**

**Cálculo do Sistema para localizar alíquota de ICMS para venda - (MATA920):**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21398587780887)
