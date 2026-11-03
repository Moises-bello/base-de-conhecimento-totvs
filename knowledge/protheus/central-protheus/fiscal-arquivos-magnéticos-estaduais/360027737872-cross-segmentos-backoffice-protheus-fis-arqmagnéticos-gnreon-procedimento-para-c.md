---
article_id: 360027737872
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 3af4771940d6dcddcd92cd42796e8709064d06e1f7fe5af830a287f4f7473b66
fetched_at: '2026-06-28T22:42:11.735594+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GNREON Procedimento
  para criar TAG C39 no XML da GNREON
type: support-article
updated_at: '2022-08-18T13:55:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027737872-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GNREON-Procedimento-para-criar-TAG-C39-no-XML-da-GNREON
---

**Ocorrência**  
Erro da não geração da **TAG C39 GNREON**.  
   
 **Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
   
 **Causa**

O erro ocorre quando a **SX5** não está preenchida, pois a partir desta tabela é gerado a **TAG C39** com as informações extras e chave eletrônica da Nota Fiscal.  
  
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Crie a **tabela 88** na **SX5**;  
 2. Inclua o código da informação extra referente a chave da **NF-e/ CT-e/ DF-e** caso tenha alguma alteração;  
 3. Exemplo de preenchimento:   
Chave: **MA (UF)**  
Descrição: 100099-85/

A estrutura de preenchimento deve ser conforme exemplo acima, para o correto funcionamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027873571/mceclip0.png)

Para saber as regras do preenchimento da **TAG C39** consulte o portal da **GNRE**, informe o Estado e o código da Receita da operação, segue link:

<http://www.gnre.pe.gov.br/gnre/portal/automacao.jsp#>

Mais informações:   
  
[http://tdn.totvs.com/display/public/PROT/FIS0017\_GNREON\_Guia\_Nacional\_de\_Recolhimento\_de\_Tributos](https://www.google.com/url?q=http://tdn.totvs.com/display/public/PROT/FIS0017_GNREON_Guia_Nacional_de_Recolhimento_de_Tributos&sa=D&source=hangouts&ust=1557322363970000&usg=AFQjCNEoLvvhHja3iyUu_RAGoViSgr4x1Q)
