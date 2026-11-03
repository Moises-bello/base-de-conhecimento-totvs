---
article_id: 360045163554
category: NFe - Nota Fiscal Eletrônica
content_hash: b4d05f973260f2b4dfb2e4d6f95231028471a39039cf531e4ea9029b94282664
fetched_at: '2026-06-28T22:40:00.315957+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como gerar Lote
  no XML e no Danfe '
type: support-article
updated_at: '2024-02-06T18:14:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045163554--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-Lote-no-XML-e-no-Danfe
---

**Dúvida**Como gerar Lote no XML e no Danfe ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Por padrão para gerar o Lote no XML, apenas quando é configurado**o grupo Rastro no XML**conforme o link abaixo:  
  
 [Cross Segmentos - Backoffice Protheus - Como gerar a TAG rastro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004942192)  
  
2 - Dessa forma acima é gerada apenas no XML conforme informação abaixo:

* **Impressão no Danfe:**

O Lote é gerado apenas no XML.  
  
Não existe até o momento um layout da Sefaz para que seja apresentada a informação do Lote, ou seja, não foi criado um novo campo no Danfe, e não há nenhuma informação na nota técnica sobre a obrigatoriedade de mensagem.  
  
Caso seja uma solicitação da Sefaz do seu estado, poderá utilizar um padrão para gerar a mensagem em informações complementares, como exemplo **C5\_MENNOTA e F4\_FORMULA.**

**C5\_MENNOTA**

Campo de complemento da Danfe do campo **Informações complementares** é preenchido no Pedido de Venda.

Além disso é necessário que os campos F2\_MENNOTA e C5\_MENNOTA estejam com o mesmo tamanho no configurador.

![C5_MENNOTA.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21164429322903)

**F4\_FORMULA**

Campo de complemento do Danfe do campo **Informações complementares** é preenchido no TES na aba impostos campo FORMULA.

Colocar nesse campo a numeração da fórmula criada.

![F4_FORMULA.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21164445331223)

Nome : MV\_NFEMSF4   
Tipo : Caractere  
**Descrição:**  
***Parâmetro que determina o tratamento do campo F4\_FORMULA e F4\_FORINFC  para NF-e.***  
C =Inf. Adicionais cliente;  
F =Inf. Adicionais Fisco;  
BRANCO=não considera.  
  
  
3- Além disso, Se desejar  poderá realizar o procedimento do vídeo em anexo no qual o **lote é impresso no Danfe.**

* **Saiba mais:**

Para verificar os campos de inclusão de mensagem em **informações complementares, verificar nos links abaixo:**

*[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773)*

*[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar mensagem em informações complementares (TAG infcpl e infadfisco) do Danfe utilizando fórmula](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871)*

*[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar informações adicionais do Produto no XML (TAG infadprod) e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024934073--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-informa%C3%A7%C3%B5es-adicionais-do-Produto-no-XML-TAG-infadprod-e-no-DANFE?source=search)*
