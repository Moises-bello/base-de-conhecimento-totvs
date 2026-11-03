---
article_id: 360051188333
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 78e3c5384a0d26063a178335959a88952ea5795d14040f46b2c42f1dbe48f274
fetched_at: '2026-06-28T22:39:20.427081+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como gerar tag cBenef
  para ICMS ST com CST "Situação Tributária do ICMS"  60 '
type: support-article
updated_at: '2021-07-13T17:23:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051188333-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-tag-cBenef-para-ICMS-ST-com-CST-Situa%C3%A7%C3%A3o-Tribut%C3%A1ria-do-ICMS-60
---

**Dúvida**Como gerar tag cBenef para ICMS ST com CST "Situação Tributária do ICMS" 60  
   
 **Ambiente**Protheus– fiscal – A partir da versão 12.1.17  
  
**Solução**Segue exemplo como tratar a geração da tag cBenef para ICMS ST com Sit.Trib.ICMS 60

A escolha do código de valor declaratório (Tabela 5.2 ) é de responsabilidade do fiscal ou contabilidade da empresa informar.

Para o devido tratamento deve seguir as minhas orientações abaixo:

O parâmetro **MV\_MTCLF3K**deve estar igual a 0.

![](https://totvssuporte.zendesk.com/attachments/token/BcumO5O4XTbgaa4Rml4Qu2NP3/?name=inline-1536579336.png)​  
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=520651465>  
  
  
TES:  
Calcula ICMS = NÃO  
Livro Fiscal de ICMS = OUTROS  
CFOP Operação 5405  
Sit Trib Icm = 60  
  
![](https://totvssuporte.zendesk.com/attachments/token/PuAneG8Jl6YNZePgIg5CDv5LX/?name=inline-342188845.png)​  
  
Código de reflexo FISA072  
Base p/Calculo = 2- Valor Contábil  
Alíquota = 1 - Aliq ICMS  
Valor = 3 - Merc.  
  
![](https://totvssuporte.zendesk.com/attachments/token/7blrXzlbM7zwIpZCzfJlfPsLM/?name=inline-1673795440.png)​  
  
Itens X Cod.val.declaratórios (FISA140)  
Produto = Informe o código de produto a ser Utilizado   
CFOP = Informe o CFOP  
Cod.Val Decl = Informe o codigo pertinente ao Sit.trib ICMS   
Cod. reflexo = Informe o código configurado na FISA072  
  
![](https://totvssuporte.zendesk.com/attachments/token/WWciR5QPhGvL4YuGuTGvhBTAH/?name=inline-596910456.png)​  
  
Ao fazer o pedido de venda, usando o produto e TES, ao clicar em valor declaratório sera apresentada a informação da cBenef.  
![](https://totvssuporte.zendesk.com/attachments/token/InfwjWDp5KCY8Qcscn236NTt7/?name=inline502651646.png)​  
  
Apos emitir a NF as informações serão gravadas na tabela CDV.  
![](https://totvssuporte.zendesk.com/attachments/token/rIg2WqkXkUPx5Ntb4KQSEcoz7/?name=inline613405102.png)​
