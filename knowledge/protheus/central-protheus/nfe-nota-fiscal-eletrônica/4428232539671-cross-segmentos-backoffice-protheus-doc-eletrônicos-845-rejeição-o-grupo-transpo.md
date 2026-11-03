---
article_id: 4428232539671
category: NFe - Nota Fiscal Eletrônica
content_hash: 5698cca0c8f93caa87553e6c8f96021a8efe73930b9ac857afa6599579ca1fb5
fetched_at: '2026-06-28T22:40:05.363023+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 845 Rejeição: O
  Grupo Transportador não pode ser preenchido para Modalidade do frete informada'
type: support-article
updated_at: '2025-02-12T18:21:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4428232539671-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-845-Rejei%C3%A7%C3%A3o-O-Grupo-Transportador-n%C3%A3o-pode-ser-preenchido-para-Modalidade-do-frete-informada
---

**Dúvida**Como solucionar a 845 Rejeição: O Grupo Transportador não pode ser preenchido para  
Modalidade do frete informada ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.27

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se ***Modalidade do Frete = 9*** (id: X02, campo: modFrete), o *Grupo Transportador* (id: X03, campo: transporta) ***não pode ser informado.***

1. No pedido de venda se preenchido no campo ***C5\_TPFRETE Tipo Frete = S*** ou no documento de entrada ***o campo F1\_TPFRETE Tipo Frete = S , 9=Sem Ocorrência de Transporte;***

2. Ao incluir o pedido de vendas retire a informação preenchida no campo da transportadora, campo **Transp  C5\_TRANSP** ou no documento de entrada o campo **Transp F1\_TRANSP;**

3. Caso tenha frete a nota, alterar a modalidade ***diferente de 9- Sem frete*** do campo **C5\_TPFRETE Tipo Frete** ou no documento de entrada **o campo F1\_TPFRETE Tipo Frete**

4. Após isso, prepare o documento **novamente.**

* **Saiba mais:**

**Modalidades de frete:**

**"C"**= **0=**Contratação do Frete por conta do Remetente (CIF);

**"F"** =**1=**Contratação do Frete por conta do Destinatário (FOB);

**"T"=****2=**Contratação do Frete por conta de Terceiros;

**"R"** =**3=**Transporte Próprio por conta do Remetente;

**"D"** =**4=**Transporte Próprio por conta do Destinatário;

**"S"** =**9=**Sem Ocorrência de Transporte;

No Danfe no **quadro Transportador/Volumes transportados só será levado o** conteúdo do grupo das TAGS transp se preenchido os campos ***C5\_TRANSP e C5\_TPFRETE.***

* ***Validação da Sefaz:***

***![845_rejei__o.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4428108125719)***
