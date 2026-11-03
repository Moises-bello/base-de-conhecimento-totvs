---
article_id: 360053307454
category: Escrita Fiscal - Impostos - Cálculos
content_hash: bb399f1106e96d735ec7b67eed45def498a20260c126a4aa68b89e0c8200e718
fetched_at: '2026-06-28T22:39:30.579430+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Help - REGNOIS -
  Não existe registro relacionado a este código
type: support-article
updated_at: '2021-07-29T14:41:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053307454-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Help-REGNOIS-N%C3%A3o-existe-registro-relacionado-a-este-c%C3%B3digo
---

**Dúvida**  
Help - REGNOIS - Não Existe Registro Relacionado a Este Código  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Referente a mensagem:

Help - REGNOIS - Não Existe Registro Relacionado a Este Código  
  
Essa mensagem é apresentada por motivo do cadastro que esta sendo informado em alguma rotina não existir na base de dados.

Por exemplo:

Foi appendado o cadastro de produto de uma empresa no qual existe os cadastros de armazém normalmente, logo ao appendar o campo Armazém Pad. (B1\_LOCPAD) é gravado a informação 01 por exemplo conforme estava cadastrado na empresa origem.   
  
Ao tentar incluir um documento de entrada, os cadastros são informados normalmente e no caso cadastro do armazém o mesmo é carregado a informação 01 conforme consta no cadastro do produto, mas ao tentar salvar a inclusão do documento é apresentado a mensagem abaixo: 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089885293/mceclip0.png)

Para solucionar o problema da mensagem acima, será necessário verificar se todos os cadastros envolvidos no processo estão cadastrado corretamente na base de dados.
