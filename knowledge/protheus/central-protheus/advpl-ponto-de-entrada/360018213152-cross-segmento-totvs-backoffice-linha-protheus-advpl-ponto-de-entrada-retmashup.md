---
article_id: 360018213152
category: ADVPL - Ponto de Entrada
content_hash: 9e62f81491e14a57dc26a7a53c0537d340ca51363c28ddba4fb925f5048cb235
fetched_at: '2026-06-28T22:40:12.753240+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  RETMASHUP em rotina MVC
type: support-article
updated_at: '2022-06-21T17:51:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018213152-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-RETMASHUP-em-rotina-MVC
---

**Dúvida**Como atribuir valor customizado a campos do cadastro via ponto de entrada RETMASHUP quando a rotina for MVC  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - A partir da versão 11.80  
  
**Solução**Quando a rotina estiver em **MVC** e utilizar o ponto de entrada **RETMASHUP** para atribuir um valor customizado, a atribuição via variável de memória '**M->**' não terá efeito. Para atender essa necessidade deve-se manipular o objeto do modelo de dados da rotina em questão, realizando a atribuição via método ***SetValue*** ou ***LoadValue***.   
A seguir um exemplo utilizando o ***Mashup***Receita Federal - Consulta Simples Nacional, onde o ponto de entrada **RETMASHUP** é utilizado para manipular o campo **A2\_SIMPNAC** no cadastro de fornecedor;

```
#Include 'Protheus.ch'  
  
User Function RetMashup()  
  
Local cAlias := ParamIXB[1] // Alias da tabela  
Local cMashup := ParamIXB[2] // Nome do serviço do Mashup  
Local cDescri := ParamIXB[3] // Descrição do retorno  
Local cCampo := ParamIXB[4] // Campo de retorno  
Local xConteudo := ParamIXB[5] // Conteúdo  
  
  
If cAlias == "SA2"  
  oModelx := FWModelActive() //Instancia modelo ativo  
  oModelA2 := oModelx:GetModel("SA2MASTER") //Instancia submodelo SA2  
    
  If cDescri == "Situacao no Simples Nacional"   
    If Left(xConteudo, 7) == "Optante"  
      oModelA2:LoadValue('A2_SIMPNAC', "1")  
    Else  
      oModelA2:LoadValue('A2_SIMPNAC', "2")  
    EndIf  
  EndIf  
EndIf   
  
Return
```

**Saiba mais**[Manual ADVPL Utilizando MVC](http://tdn.totvs.com/display/public/PROT/AdvPl+utilizando+MVC)
