---
article_id: 360036878173
category: Escrita Fiscal - Impostos - ICMS
content_hash: 594a6ab6d4c4ebce9e810dea32970636a276e9e6f647145ba99159c8df92b707
fetched_at: '2026-06-28T22:39:26.062437+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: MP - FIS - Qual configuração para gerar a tabela CDV com CST 41 ?
type: support-article
updated_at: '2021-04-28T21:07:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036878173-MP-FIS-Qual-configura%C3%A7%C3%A3o-para-gerar-a-tabela-CDV-com-CST-41
---

**Dúvida** Qual configuração para gerar a tabela CDV com CST 41 operação não tributada?

**Ambiente**  
Microsiga Protheus – Fis – A partir da versão 11.80  
  
**Solução**

Configurar a TES:

Calcula ICMS F4\_ICM=Não

L. Fiscal ICMS F4\_LFICM=Isento/Outras

Sit Trib ICM F4\_SITTRIB=41

Cod.Fiscal F4\_CF= CFOP da operação a ser utilizado

Criar a **amarração** na rotina **FISA140 - Prod. x Cod.V.Decl.;**

Informar:

* Produto
* CFOP da operação a ser aplicado aquele código
* Cod. Val. Decl (Tabela 5.2 da receita federal)
* CST=41
* Código de Reflexo configurado conforme abaixo:

FISA072 - Código de Reflexo

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047552654/mceclip1.png)

Para verificar se os valores serão gravados na CDV acessar na planilha do pedido de venda na aba Lançamento da apuração ->Val Declaratório;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047552554/mceclip0.png)

Tabela CDV

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047552814/mceclip2.png)

**Importante:**

Na rotina FISA156 existe o campo CDY\_NFE "Gera NFE" de acordo com o código de ajuste deve definir o campo como 1- Sim ou 2- Não.

Para levar a TAG Cbenef no XML o campo deve estar configurado diferente de 2 -Não, ou seja com 1 ou em branco

Informações adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=286029741>

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018292572-MP-FIS-Gera%C3%A7%C3%A3o-da-tabela-CDV-para-alimentar-a-tag-cBenef-para-o-estado-do-PR>
