---
article_id: 5726991438743
category: RH - CNAB
content_hash: 3ef7c742bdcc78a7d72a410cac77bc72542a2d6a5f142b2b2ccff19b6ae1711a
fetched_at: '2026-06-28T22:43:39.275957+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - GP080USR - Validação do usuário ou alterar caminho
  onde será salvo o arquivo
type: support-article
updated_at: '2025-06-16T18:35:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5726991438743-RH-Linha-Protheus-GPE-GP080USR-Valida%C3%A7%C3%A3o-do-usu%C3%A1rio-ou-alterar-caminho-onde-ser%C3%A1-salvo-o-arquivo
---

A execução é realizada antes da apresentação do log de geração. Caso esteja inconsistente o caminho digitado, o log desse ponto não será apresentado. 

**EXEMPLO DE UTILIZAÇÃO**

**//Exemplo 01**

#Include '[Protheus.ch](http://protheus.ch/)'  
  
User Function GP080USR()

Local cPath := PARAMIXB[1]

Local cPathDefault := "C:\CNAB"

Local lRet := .T.  
  
If cPath <> cPathDefault

     lRet := .F.

EndIf  
  
Return lRet

**//Exemplo 02**

#Include '[Protheus.ch](http://protheus.ch/)'

        User Function GP080USR()

             Local cRet := ""

             cRet := "C:\CNAB"

        Return cRet

#### **VARIÁVEIS DE RETORNO**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17439912241815)

Ponto de entrada sendo executado durante o processamento da rotina GPEM080:   
![GP080USR.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17443268032535)

**Saiba Mais:**

[RH - Linha Protheus - GPE - Quais são os pontos de entrada disponíveis na rotina GPEM080](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045165513-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM080)

[RH - Linha Protheus - GPE - Passo a passo para geração do Arquivo CNAB (GPEM080)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8420406092951-RH-Linha-Protheus-GPE-Passo-a-passo-para-gera%C3%A7%C3%A3o-do-Arquivo-CNAB-GPEM080-)

[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
