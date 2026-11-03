---
article_id: 360052698773
category: NFe - Nota Fiscal Eletrônica
content_hash: 1c6bcb85c54a2b9a4bcd9847a07e6379a4d9986d2ea6cf71bc89dc518c132536
fetched_at: '2026-06-28T22:40:03.909044+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 333 - Rejeição:
  Informar a UF do adquirente ou do encomendante nesta forma de importação'
type: support-article
updated_at: '2025-07-14T14:14:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052698773-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-333-Rejei%C3%A7%C3%A3o-Informar-a-UF-do-adquirente-ou-do-encomendante-nesta-forma-de-importa%C3%A7%C3%A3o
---

**Dúvida**Como solucionar a rejeição 333 : Informar a UF do adquirente ou do encomendante nesta forma de importação ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

Ao fazer nota de **importação** conforme o Manual de Orientação do Contribuinte  página **246,** se gerar a TAG **tpIntermedio** igual a **2 ou 3** é necessário gerar a TAG  **UFTerceiro.**

1. Quando ***não usa integração*** com o ***módulo SIGAEIC é necessário que o parâmetro no configurador MV\_EASY= N***

**![20201201_145829.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33452950711191)**

2. Acesse a rotina *****Livros Fiscais**-> **Atualizações**->**Movimentos**->**NF manual de Entrada**->**Outras ações**->**Complementos**->**Importação:*****

****![20201201_145142.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33452981239831)****

3. Preencher o campo **Forma Import** "***CD5\_INTERM"***  no complemento de importação dos ***Livros fiscais = 1 Importação por conta própria;***

**![333.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414048529303)**

4. **Se  for  *2 = Importação por conta e ordem ou 3 = Importação por encomenda*** preencha o campo  **UF Terceiro** "**CD5\_UFTERC"** no complemento de importação dos Livros fiscais.

![UF_TERCEIRO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414039857815)

5.*Verifique a **opção correta** a ser utilizada, a**pós isso, **retransmita a nota.***

* **Saiba mais:**

A informação obrigatória no caso de importação **por conta e ordem ou por encomenda**. **Não aceita** o valor **"EX".**

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083004734)
