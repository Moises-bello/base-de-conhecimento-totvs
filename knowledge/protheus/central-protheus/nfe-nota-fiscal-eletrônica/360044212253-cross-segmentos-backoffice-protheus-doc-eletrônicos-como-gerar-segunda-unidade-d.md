---
article_id: 360044212253
category: NFe - Nota Fiscal Eletrônica
content_hash: 0b6edbaecfeff90fc6d63cd38aa8790d1f4f8e8a507ad293a7e2bc747f286e01
fetched_at: '2026-06-28T22:40:06.767149+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar Segunda
  unidade de medida no XML ?
type: support-article
updated_at: '2026-03-23T14:45:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044212253-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-Segunda-unidade-de-medida-no-XML
---

**Dúvida**  
Como gerar Segunda unidade de medida no XML ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /Cadastros / Parâmetros** clicar em **editar****MV\_NIMP2UM =** **.F.**

**Para emitir a nota com duas unidades de medida no XML:**

**1-** Ir em complemento **do produto:**

![20201201_172957.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101053653)

**2-** Cadastrar o **produto e preencher os campos B5\_CONVDIP e B5\_UMDIPI:**

![20201201_173116.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098840654)

**3-** Após isso, **incluir o pedido de venda e realizar a transmissão da nota:**

**<uCom>UN</uCom> primeira unidade (cadastro de produto)**

**<uTrib>DZ</uTrib> segunda unidade (complemento de produto)**

**Importante:**

* **Configurar o parâmetro do link abaixo para operações nacionais:**

  [**MP - NFE - Como gerar apenas uma unidade de medida no Danfe para operações dentro do País ?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017958992)

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /Cadastros / Parâmetros** clicar em **editar****MV\_NIMP2UM =** **.F.**

Nome: MV\_NIMP2UM  
Descrição: Não imprime a 2ª. Unidade de Medida para operações dentro do País.  
Tipo: Lógico  
Conteúdo: .T. - Não Imprime ou .F. - Imprime (Default)

**![20201201_172751.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098840474)**
