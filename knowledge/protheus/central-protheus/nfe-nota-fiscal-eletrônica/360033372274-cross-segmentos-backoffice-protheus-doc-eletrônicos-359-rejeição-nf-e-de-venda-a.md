---
article_id: 360033372274
category: NFe - Nota Fiscal Eletrônica
content_hash: d724b16af228458859b140552b450bbd698e2ba168e6327f6692520226695df8
fetched_at: '2026-06-28T22:40:04.976862+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 359 Rejeição :
  NF-e de venda a Órgão Público sem informar a Nota de Empenho'
type: support-article
updated_at: '2025-08-12T00:45:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033372274-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-359-Rejei%C3%A7%C3%A3o-NF-e-de-venda-a-%C3%93rg%C3%A3o-P%C3%BAblico-sem-informar-a-Nota-de-Empenho
---

**Dúvida**Como corrigir a rejeição abaixo?

 359 Rejeição : NF-e de venda a Órgão Público sem informar a Nota de Empenho

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Ao configurar a nota como ***órgão público*** conforme abaixo:

* Preencher no **cadastro de cliente:**

1- Cadastro de cliente empresa Orgão Público (campo A1\_TPESSOA = EP)

* Preencher **no TES:**

2- Campo Agrega Valor **(F4\_AGREG = “D”)** – Indica que deve descontar o valor do imposto do valor contábil.

3- Campo Cálculo ICMS **(F4\_ICM = “Sim”)** – Indica que haverá o cálculo do ICMS.

4- Campo L.Fiscal ICMS **(F4\_LFICM =”Isento”)** – Indica que será escriturado como Isento.

5- Campo Sit.Trib.ICMS **(F4\_SITTRIB =”40”)** – Indica que Isento.

6- Campo Mot.Desone. **(F4\_MOTICMS=8)**

**A critério da UF pode ser solicitado que seja gera a TAG abaixo:**

**<xNEmp>**000000073**</xNEmp>**  
  
  
Exemplo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/bFGIdkzll0beuUydDDNfJaWzp/?name=inline445464377.png)​  
  
  
7- Para gerar a TAG habilitar o parâmetro no configurador:

* **MV\_NFORGPU=** .T.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042828414)

8- Para gerar a TAG configurar o parâmetro conforme abaixo:

* **MV\_SPEDNAT=** .F.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043668053)

9- Informar no campo **Nt Empenho** **C5\_NTEMPEN** o número do documento que será gerado nessa nota com série mais número.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043668293)

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042818334)
