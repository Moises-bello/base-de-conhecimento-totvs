---
article_id: 360049968093
category: NFe - Nota Fiscal Eletrônica
content_hash: 1f466a67366d897d5840e661653936b9afb1689adb52fc9f7ced4feddb420952
fetched_at: '2026-06-28T22:40:05.021012+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 387 Rejeição: Código
  de Enquadramento Legal do IPI inválido'
type: support-article
updated_at: '2024-05-29T18:54:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049968093-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-387-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-Enquadramento-Legal-do-IPI-inv%C3%A1lido
---

**Dúvida**Como corrigir a rejeição abaixo ?

387 Rejeição: Código de Enquadramento Legal do IPI inválido

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A Sefaz retorna essa rejeição  quando o **Código de Enquadramento Legal do IPI inválido** tag **<cEnq>**

Sendo necessário consultar o anexo: **Anexo XIV - Código de Enquadramento Legal do IPI no link abaixo:**

[Nota Técnica 2020.002 - v.1.00 - Publicada em 18/05/2020](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=2aYIAayNJAU=)

Página 5 até 11

* Exemplo o XML gerou **conforme abaixo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074672253)

* Conforme abaixo deve ser utilizado o código na **TAG cEnq** de acordo com a **situação tributária do IPI :**

Para o CST 05 ou 55 (Suspensão):

Enq.IPI (F4\_GRPCST e B1\_GRPCST) deve ser entre **101 a 162**

Para o CST 04 ou 54 (Imune):

Enq.IPI (F4\_GRPCST e B1\_GRPCST) deve ser entre **001 a 099**

Para o CST 02 ou 52 (Isento):

Enq.IPI (F4\_GRPCST e B1\_GRPCST) deve ser entre **301 a 399**

Porém, **dentro desses ranges não existe na lista todos os códigos** ao apresentar a rejeição é devido a esse motivo.

1- Verifique se a situação tributária do IPI está correta no TES no campo F4\_CTIPI **Cod. trib. IPI**  
  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23821144052247)​

2- Consulte a lista do **Anexo XIV - Código de Enquadramento Legal do IPI no link abaixo Página 5 até 11 e verifique se**cEnq gerado no XML é valido**:**

[Nota Técnica 2020.002 - v.1.00 - Publicada em 18/05/2020](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=2aYIAayNJAU=)

3- Altere para um código válido nos campos no cadastro de produto "B1\_GRPCST" **Enq. IPI** e  no TES através do campo "F4\_GRPCST"  **Enq. IPI**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073499634)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074675293)

4 - Após isso, exclua a nota e gere novamente.

* **Saiba mais:**

Os dois campos podem ser **preenchidos ou apenas o do cadastro de produto ou do TES.**

**Se os dois estiverem preenchidos** a prioridade do fonte é verificar o campo do **cadastro do produto.**

Se estiver **preenchido diferente** nos dois campos a informação será levada do **cadastro de produto.**

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073507854)**
