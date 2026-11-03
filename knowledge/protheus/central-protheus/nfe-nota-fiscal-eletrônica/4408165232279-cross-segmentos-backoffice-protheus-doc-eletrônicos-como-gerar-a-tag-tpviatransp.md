---
article_id: 4408165232279
category: NFe - Nota Fiscal Eletrônica
content_hash: f26b2b70b045b99313bc5560110f92580744d99363175e092f4e22dffe50d3a5
fetched_at: '2026-06-28T22:40:01.715876+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a TAG
  tpViaTransp '
type: support-article
updated_at: '2023-08-09T17:56:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408165232279--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-tpViaTransp
---

**Dúvida**Qual campo é preenchido para gerar a TAG tpViaTransp   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Conforme a nota técnica **2020.005\_v\_1.20 página 6, as opções da TAG tpViaTransp :**

**1=**Marítima;   
**2=**Fluvial;   
**3=**Lacustre;   
**4=**Aérea;   
**5=**Postal  
**6=**Ferroviária;   
**7=**Rodoviária;

**8=**Conduto/Rede Transmissão;

**9=**Meios Próprios;

**10=**Entrada/Saída Ficta;

**11=**Courier;

**12=**Em mãos;

**13=**Por reboque;

**1-** Quando **não é utilizada a integração** com o **módulo SIGAEIC é necessário que o parâmetro MV\_EASY= N**

**![20201201_145829.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101037393/20201201_145829.gif)**

**2-** Acesse a rotina ****Livros Fiscais**-> **Atualizações**->**Movimentos**->**NF manual de Entrada**->**Outras ações**->**Complementos**->**Importação:****

****![20201201_145142.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101036933/20201201_145142.gif)****

3- Preencher o campo no complemento de **importação nos Livros fiscais.** **CD5\_VTRANS - Via de Transporte internacional informada na DI.**

![REBOQUE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4408761329559/REBOQUE.gif)

* **Saiba mais:**

Para que seja apresentada na rotina de importação no campo **CD5\_VTRANS opção 13- Reboque é necessário realizar as atualizações do Protheus do link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714) [2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)

* Para acessar o **boletim técnico:**

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=627094959)
