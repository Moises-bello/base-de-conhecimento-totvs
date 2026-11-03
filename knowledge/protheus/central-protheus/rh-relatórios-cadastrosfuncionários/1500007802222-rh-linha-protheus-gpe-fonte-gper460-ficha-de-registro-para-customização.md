---
article_id: 1500007802222
category: RH - Relatórios Cadastros/Funcionários
content_hash: b35ab6f8b34fed84520b86551792b855992a4fa2557e88e1abc7e800e1114b5c
fetched_at: '2026-06-28T22:43:18.426110+00:00'
product: protheus
section_id: 360010843654
source: central-protheus
title: RH - Linha Protheus - GPE - Fonte GPER460 (Ficha de Registro) para customização
type: support-article
updated_at: '2025-09-15T18:48:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007802222-RH-Linha-Protheus-GPE-Fonte-GPER460-Ficha-de-Registro-para-customiza%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15509009289495) Tempo aproximado para leitura: **00:01:00 min****Dúvida**A rotina **Ficha de Registro** - GPER460, é um ***rdmake***?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Por padrão a rotina **GPEA260** executa o fonte **GPER460**, que se trata de um ***rdmake* disponível para customização.**  
Para que o sistema acate a modificação, deve ser alterado o conteúdo da variável **cImpFch** através do Ponto de Entrada **[FIMPFCH.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32717961003927-RH-Linha-Protheus-GPE-Ponto-de-Entrada-FIMPFCH-Ficha-de-Registro)**  
  
É importante ressaltar que a rotina GPER460 não deve ser configurada para ser acessada através de outros menus pois pode ocasionar erros, portanto, ela deve ser chamada diretamente a partir da rotina GPEA260.   
Caso o cenário acima não seja respeitado, será exibida a mensagem abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32740709936279)

**Saiba Mais:**[DT - Ficha de Registro](https://tdn.totvs.com/pages/releaseview.action?pageId=852902992)[RH - Linha Protheus - GPE - Ponto de Entrada FIMPFCH - Ficha de Registro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32717961003927-RH-Linha-Protheus-GPE-Ponto-de-Entrada-FIMPFCH-Ficha-de-Registro)  
[RH - Linha Protheus - GPE - Como adicionar ou remover informações da Ficha de Registro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061657113-RH-Linha-Protheus-GPE-Como-adicionar-ou-remover-informa%C3%A7%C3%B5es-da-Ficha-de-Registro?source=search)  
[RH - Linha Protheus - GPE - Como ordenar os campos para Impressão da Ficha de Registro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035616213-RH-Linha-Protheus-GPE-Como-ordenar-os-campos-para-Impress%C3%A3o-da-Ficha-de-Registro?source=search)
