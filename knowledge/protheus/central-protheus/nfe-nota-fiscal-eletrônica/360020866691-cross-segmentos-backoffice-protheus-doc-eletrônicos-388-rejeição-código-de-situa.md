---
article_id: 360020866691
category: NFe - Nota Fiscal Eletrônica
content_hash: b8959c5a8c8ce49eeca700cb83c45d752901506bdcc08acdf3529431a4a5ca97
fetched_at: '2026-06-28T22:40:00.241547+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  388 Rejeição
  : Código de Situação Tributária do IPI incompatível com o Código de Enquadramento
  Legal do IPI'
type: support-article
updated_at: '2021-06-28T18:26:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020866691--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-388-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-Situa%C3%A7%C3%A3o-Tribut%C3%A1ria-do-IPI-incompat%C3%ADvel-com-o-C%C3%B3digo-de-Enquadramento-Legal-do-IPI
---

**Dúvida**Como resolver a rejeição:

388 Rejeição : Código de Situação Tributária do IPI incompatível com o Código de Enquadramento Legal do IPI ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.23

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A Sefaz retorna essa rejeição  quando o **Código de Enquadramento Legal do IPI inválido ou não foi informada** tag **<cEnq>**

Sendo necessário consultar o anexo: **Anexo XIV - Código de Enquadramento Legal do IPI no link abaixo:**

[Nota Técnica 2020.002 - v.1.00 - Publicada em 18/05/2020](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=2aYIAayNJAU=)

Página 5 até 11

* Exemplo o XML gerou **conforme abaixo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074672253/mceclip0.png)

* Conforme abaixo deve ser utilizado o código na **TAG cEnq** de acordo com a **situação tributária do IPI :**

Para o CST 05 ou 55 (Suspensão):

Enq.IPI (F4\_GRPCST e B1\_GRPCST) deve ser entre **101 a 199**

Para o CST 04 ou 54 (Imune):

Enq.IPI (F4\_GRPCST e B1\_GRPCST) deve ser entre **001 a 099**

Para o CST 02 ou 52 (Isento):

Enq.IPI (F4\_GRPCST e B1\_GRPCST) deve ser entre **301 a 399**

Para os demais casos, informar cEnq com um valor entre **"601 a 608" ou "999".**

Porém, **dentro desses ranges não existe na lista todos os códigos.**

1- Verifique se a situação tributária do IPI está correta no TES no campo F4\_CTIPI **Cod. trib. IPI**  
  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057026893/mceclip0.png)​

2- Consulte a lista do **Anexo XIV - Código de Enquadramento Legal do IPI no link abaixo Página 5 até 11 e verifique se**cEnq gerado no XML é valido**:**

[Nota Técnica 2020.002 - v.1.00 - Publicada em 18/05/2020](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=2aYIAayNJAU=)

3- Altere para um código válido nos campos no cadastro de produto "B1\_GRPCST" **Enq. IPI** e  no TES através do campo "F4\_GRPCST"  **Enq. IPI**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073499634/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074675293/mceclip3.png)

4 - Após isso, exclua a nota e gere novamente.

* **Saiba mais:**

Os dois campos podem ser **preenchidos ou apenas o do cadastro de produto ou do TES.**

**Se os dois estiverem preenchidos** a prioridade do fonte é verificar o campo do **cadastro do produto.**

Se estiver **preenchido diferente** nos dois campos a informação será levada do **cadastro de produto.**

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074681133/mceclip0.png)
