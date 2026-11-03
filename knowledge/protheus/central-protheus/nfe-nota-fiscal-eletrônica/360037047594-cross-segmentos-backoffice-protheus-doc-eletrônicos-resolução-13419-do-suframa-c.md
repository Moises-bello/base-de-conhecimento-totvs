---
article_id: 360037047594
category: NFe - Nota Fiscal Eletrônica
content_hash: 75f5123db72d97a217038dd3b237c510bf6b3979345bd80312db16705109a87f
fetched_at: '2026-06-28T22:40:01.959591+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Resolução 134/19
  do Suframa clausula 7 '
type: support-article
updated_at: '2021-11-04T18:07:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037047594--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Resolu%C3%A7%C3%A3o-134-19-do-Suframa-clausula-7
---

**Dúvida**

Como configurar no Protheus Resolução 134/19 do Suframa clausula 7 ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

a) número de inscrição na SUFRAMA do destinatário;

1- Será necessário que o parâmetro **MV\_SUFRAMA** exista no configurador:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049705833/mceclip0.png)

2- Preencher no cadastro de cliente o campo **Suframa A1\_SUFRAMA**com a inscrição

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048809114/mceclip1.png)

Será gerado no XML:

* TAG **ISUF**

b) indicação do **valor do ICMS desonerado;**

Será gerado no XML:

* TAG **Vicmsdeson**

c) **motivo da desoneração** do ICMS: SUFRAMA.

* TAG **Moticmsdeson**

* Para os itens **b e c** realizar a configuração do suframa do link abaixo:

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar o sistema para calcular SUFRAMA?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034294253)

* **Saiba mais:**

1- Configurar na  **TES** no campo **Sit. trib. ICMS** **F4\_SITTRIB =** 40, 41 ou 50 ou quando houver calculo de ICMS-ST no campo **Sit. trib. ICMS** **F4\_SITTRIB =**  = 30

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041920134/mceclip2.png)

2- Preencher na**TES** na Aba **Outros**o campo **Mot. Desone.** F4\_MOTICM = 7- Suframa

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042764713/mceclip3.png)

**II – Nas Informações Complementares:**

a) dispositivo legal referente à isenção ou suspensão do Imposto sobre Produtos Industrializados - IPI, no que couber;

1- Utilizar os campos padrões do sistema para gerar a mensagem em informações complementares, conforme os links abaixo:

[MP-NFE- Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773)

[MP-NFE- Gerar mensagem em informações complementares do Danfe utilizando fórmula ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871)

Exemplo:

* **Importante:**

Se utilizar apenas uma fórmula na nota utilizar o campo **F4\_FORMULA** ou **C5\_MENPAD** não informar a mesma fórmula nos **dois campos.**

* Cadastro das Fórmulas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026275971/mceclip5.png)

* Pedido de Venda com os campos preenchidos. A fórmula 001 está vinculada no campo C5\_MENPAD.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026275931/mceclip4.png)

* A fórmula 002 está vinculada na TES utilizada no pedido:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026276011/mceclip6.png)

* DANFE:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026275811/mceclip3.png)

* **Importante:**

b) número e ano do Programa Especial de Exportação da Amazônia - PEXPAM, caso seja destinada à industrialização de produtos para atendimento específico de programa de exportação aprovado pela SUFRAMA.

Caso utilize o item b será necessário informar como é configurado hoje no sistema, para suas exportações.

* **Saiba mais:**

Conforme a Consultoria tributária da TOTVS:

O documento oficial reconhecido pela **RFB é sempre o xml** e **no Danfe não existem campos específicos** para informação do Suframa.

As informações sobre a desoneração do ICMS caso o contribuinte queira informá-los no Danfe deverá sempre fazê-lo no Quadro Dados Adicionais, campos Informações Complementares, ou aquele designado pelo fisco, quando não há tags próprias.

Além disso há um parecer da consultoria de segmentos no link abaixo:

[Parecer da consultoria](https://tdn.totvs.com/pages/releaseview.action?pageId=522010209)
