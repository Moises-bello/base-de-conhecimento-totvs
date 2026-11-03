---
article_id: 360045641374
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 7497232672edbee98388081305a4d94ca32ff2f7af50632772a22ce06920c980
fetched_at: '2026-06-28T22:37:24.004334+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Parâmetro MV_CNVLAMR
  - Como validar se há amarração do Produto x Fornecedor e Grupo x Fornecedor para
  o item da Planilha do Contrato ?
type: support-article
updated_at: '2022-05-19T21:30:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045641374-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Par%C3%A2metro-MV-CNVLAMR-Como-validar-se-h%C3%A1-amarra%C3%A7%C3%A3o-do-Produto-x-Fornecedor-e-Grupo-x-Fornecedor-para-o-item-da-Planilha-do-Contrato
---

**Dúvida**Parâmetro MV\_CNVLAMR - Como validar se há amarração do Produto x Fornecedor e Grupo x Fornecedor para o item da Planilha do Contrato ?   
  
**Ambiente**Protheus – Gestão de Contratos – A partir da versão 11.80  
  
**Solução:**

A funcionalidade do parâmetro ***MV\_CNVLAMR***, é validar se há amarração do Produto x Fornecedor e Grupo x Fornecedor para o item da planilha do contrato.

Quando o parâmetro está ativo, o sistema verifica se há relação a Amarração do Produto x Fornecedor se houver, utiliza o código do Grupo informado no cadastro do produto, para verificar se há cadastro do Grupo x Fornecedor.

Caso não haja o cadastro do Grupo x Fornecedor, será apresentado o seguinte HELP:

**Help: CNT300FPPROD - O produto informado não está relacionado ao fornecedor da planilha.Solução:Verifique o cadastro da Amarração do Produto x Fornecedor e/ou Grupo x Fornecedor**

Para solucionar essa dúvida, realize os seguintes passos:

**1.** É necessário que o Grupo seja informado o Grupo **(B1\_GRUPO)** no Cadastro do Produto **(MATA010)**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063994434/mceclip0.png)

**2.** Realize o Cadastro da Amarração do Produto x Fornecedor Rotina**(MATA061).**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063994614/mceclip1.png)

**3.** Ao efetuar do Cronograma Financeiro na Inclusão do Contrato Rotina**(CNTA300)** caso não tenha o Cadastro do Grupo x Fornecedor será apresentado o Help abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065008833/mceclip2.png)

Ao Fechar a mensagem e clicar em confirmar apresentará outro Help abaixo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063996094/mceclip4.png)

Só será permitido finalizar a Inclusão do Contrato se realizar o Cadastro da Amarração do Grupo X Fornecedor **(MATA065)**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065009513/mceclip5.png)

**Obs:** Se o Parâmetro estiver ativo e os Cadastros não forem realizados corretamente, conforme as orientações acima não haverá validação alguma na inclusão da planilha.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
