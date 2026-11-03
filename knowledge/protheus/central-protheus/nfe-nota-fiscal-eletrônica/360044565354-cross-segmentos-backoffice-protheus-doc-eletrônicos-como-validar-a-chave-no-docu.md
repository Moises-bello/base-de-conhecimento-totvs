---
article_id: 360044565354
category: NFe - Nota Fiscal Eletrônica
content_hash: 9d012284059714477672f6aa2d5052f2c60913fd4d55f48574ace49cb54d04da
fetched_at: '2026-06-28T22:40:03.121079+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -   Como validar a
  chave no documento de entrada (MV_CHVNFE) e (MV_DCHVNFE)
type: support-article
updated_at: '2023-09-19T13:26:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044565354-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-validar-a-chave-no-documento-de-entrada-MV-CHVNFE-e-MV-DCHVNFE
---

**Dúvida** Como validar a chave no documento de entrada (MV\_CHVNFE) e (MV\_DCHVNFE) ?   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Para validar a chave no documento de entrada, na rotina SPEDNFE o ambiente e a modalidade da autorização da chave deve ser o mesmo da autorização.**

1- No site da**SEFAZ consulte o link abaixo:**

***<https://www.nfe.fazenda.gov.br/portal/principal.aspx>***

***2-** Neste link, **Clique em Serviços -> Consultar NF-e;***

***3- Consulte** a chave e verifique **a modalidade de autorização.***

Se necessário alterar a modalidade de transmissão, o processo abaixo para clientes que usam a transmissão via **TSS**

**1-** Normal

![modalida_normal.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17645485710103)

**2-** Contingência off-line

![modalida_offline.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17645493091607)

**3-** Contingência Scan

![modalida_scan.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17645493092247)

**4-** Ambiente Nacional

![ambiente_nacional.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17645485728279)

**5-** Contingência DPEC/ EPEC

![epec.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17645485733143)

**6-** Sefaz virtual

![6_modalidade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17645485734551)

**7-** Contingência FS-DA

![7_modalidade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17645493107607)

**8-** Contingência SVC-AN

![8_modalidade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17645493111703)

**9-** Contingência SVC-RS

![9_modalidade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17645493113367)

**A chave** é validada no **Documento de Entrada** para nota com **Formulário próprio = Não**

1- Para habilitar a validação da chave no documento de Entrada que digitada no campo **F1\_CHVNFE "Chave NFE"  preencher Form. prop. = Não e a Espécie da nota.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060907854)

2- Habilitar o parâmetro abaixo no configurado **MV\_CHVNFE = .T.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060909714)

3- Habilitar o parâmetro abaixo no configurado **MV\_DCHVNFE = .T.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060911854)

* **Saiba mais:**

Para validar chaves de notas diferentes de **SPED e CTE** realizar o procedimento do link abaixo:

[MP - SIGACOM - Como habilitar o campo F1\_CHVNFE com espécie da NF de entrada diferente de SPED e CTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004845552)

* Como **validar se a chave** informada no campo **Chave NFe ( F1\_CHVNFE )** confere com a nota que está sendo digitada temos o artigo do link abaixo:

[MP - SIGACOM - Como validar se a chave informada no campo Chave NFe ( F1\_CHVNFE ) confere com a nota que está sendo digitada ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018061492)

**Observação:**  
A validação dos parâmetros, após o alerta de incorreto, faz a limpeza do campo da chave para que possa ser digitado novamente. Não é possível manter o conteúdo incorreto e fazer o ajuste apenas do dígito ou parte da chave digitada incorretamente incorreto. A mesma deve ser totalmente reescrita.
