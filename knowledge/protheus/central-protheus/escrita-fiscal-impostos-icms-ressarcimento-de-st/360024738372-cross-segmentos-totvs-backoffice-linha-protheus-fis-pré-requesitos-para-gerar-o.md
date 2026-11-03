---
article_id: 360024738372
category: Escrita Fiscal - Impostos - ICMS - Ressarcimento de ST
content_hash: 6c454e156ed59fab58cbb44a08143939c632498b7780c4874f4101ee7335d91a
fetched_at: '2026-06-28T22:39:27.408769+00:00'
product: protheus
section_id: 1500001538661
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Pré - Requesitos para
  gerar o ressarcimento/ complemento de ICMS ST para RS - Não Varejista
type: support-article
updated_at: '2021-07-15T18:20:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024738372-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Pr%C3%A9-Requesitos-para-gerar-o-ressarcimento-complemento-de-ICMS-ST-para-RS-N%C3%A3o-Varejista
---

**Dúvida**

Como gerar a apuração do ressarcimento/complemento RS para Não Varejista?

**Ambiente**

Protheus - Fiscal - FISA196  - A partir da versão 12.1.17  
  
  
   
**Solução**

Parâmetros:

MV\_ESTADO = RS

MV\_APUSEP = 1/2/3 -  Informar o número dos livros que indicam as Apurações Separadas para gerar os registros 1900 e filhos no EFD ICMS/IPI.

Cadastro de produtos

* Class Fiscal - (B1\_CLASFIS) = 60

 TES

* Campo - NR. LIVRO - (F4\_NRLIVRO)
* Nas TES de Entrada - Não tem necessidade de ter código de ajuste x reflexo
* Nas TES de Saída - Cadastrar 2 Códigos de Ajuste , 1 para ICMS Efetivo e outro para o Ressarcimento.

Códigos de Lançamento no TES:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023381312/mceclip0.png)

Código para ICMS Efetivo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023420851/mceclip1.png)

Código de Reflexo para o Ressarcimento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023421291/mceclip3.png)

 Acessar a rotina FISA196

Cadastrar as regras

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023393772/mceclip0.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023382012/mceclip4.png)

Gerar a Apuração do Ressarcimento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023382692/mceclip6.png)

O inventário será usado somente para Varejista

Após processar a Apuração do Ressarcimento, gere a apuração do icms como sub-apuração de acordo com o numero do livro configurado na TES

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023382752/mceclip7.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023422331/mceclip8.png)

Após gerar a apuração com o livro selecionado = \*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023422351/mceclip9.png)

No exemplo o valor do icms st deu a restituir.

Boletim

[http://tdn.totvs.com/pages/releaseview.action?pageId=463811572#PR%C3%89-REQUISITO--1299589273](https://www.google.com/url?q=http://tdn.totvs.com/pages/releaseview.action?pageId%3D463811572%23PR%25C3%2589-REQUISITO--1299589273&sa=D&source=hangouts&ust=1554311148889000&usg=AFQjCNG5tgjDhiVmI1Fz86G9cNYa5CEgiw)
