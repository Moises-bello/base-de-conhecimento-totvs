---
article_id: 360022343011
category: ADVPL - Ponto de Entrada
content_hash: a5d3f0665fa876fd9b1c62b08ddabcb584c15490639650ec21dc399648bd2faa
fetched_at: '2026-06-28T22:40:12.840512+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Preencher campo
  antes da abertura da rotina MVC
type: support-article
updated_at: '2021-12-30T17:18:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022343011-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Preencher-campo-antes-da-abertura-da-rotina-MVC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:03:00 min  
  
Dúvida**Como preencher um campo antes da abertura da tela por meio de um ponto de entrada MVC?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Utilize o id BUTTONBAR, pois o mesmo é executado depois de todas as validações básicas para abertura da rotina.  
  
FonteO exemplo abaixo retrata o caso em que o usuário deseja que na cópia de um produto, o campo B1\_COD seja preenchido com o grupo (B1\_GRUPO) do produto que está sendo copiado (produto ainda posicionado na SB1).  
Observação: Este exemplo pode ser aplicado para casos onde o cliente deseje apenas inserir um valor no campo antes da abertura da tela, porém será necessário que seja adaptado a assinatura da função, o submodelo utilizado no método GetModel() e o campo utilizado no método LoadValue():

```
// BIBLIOTECAS UTILIZADAS  
#Include "TOTVS.ch"  
#Include "FWMVCDEF.ch"  
  
// PONTO DE ENTRADA MVC DA MATA010  
User Function ITEM()  
    Local aParam   := PARAMIXB // PARÂMETROS PASSADOS PARA O PONTO (SEMPRE VARIAM)  
    Local xRet     := .T.      // RETORNO LÓGICO PARA PROSSEGUIMENTO DA ROTINA  
    Local oObj     := NIL      // OBJETO QUE ARMAZENARÁ O MODELO TOTAL  
    Local cIdPonto := ""       // ID DO MOMENTO DA CHAMADA DO PONTO  
    Local cIdModel := ""       // QUAL MODELO OU SUBMODELO ESTÁ ATIVO  
  
    // VALIDA SE O PONTO FOI CHAMADO SEM PASSAGEM DE PARÂMETROS  
    If (aParam != NIL)  
        // ATRIBUIÇÃO DE VALORES  
        oObj     := aParam[1]  
        cIdPonto := aParam[2]  
        cIdModel := aParam[3]  
  
        // VERIFICA SE O MOMENTO DA CHAMA É QUANDO O ID IGUAL A BUTTONBAR  
        // E SE A OPERAÇÃO DE INCLUSÃO É PROVENIENTE DE UMA CÓPIA  
        If (cIdPonto == "BUTTONBAR" .And. oObj:IsCopy())  
            // PROCURA O SUBMODELO SB1MASTER E INSERE NO CAMPO B1_COD  
            // O CONTEÚDO DO GRUPO DO PRODUTO DE ORIGEM + UM NÚMERO RANDÔMICO  
            oObj:GetModel("SB1MASTER"):LoadValue("B1_COD", SB1->B1_GRUPO + StrZero(Randomize(0, 100), 5))  
  
            // RECUPERA A VIEW ATIVA E ATUALIZA (NECESSÁRIO PARA EXIBIÇÃO DO CONTEÚDO)  
            oView := FwViewActive()  
            oView:Refresh()  
        EndIf  
    EndIf  
Return (xRet) // RETORNO LÓGICO PARA PROSSEGUIMENTO
```

**Saiba mais**  
[Ponto de Entrada Padrão do MVC](http://tdn.totvs.com/pages/viewpage.action?pageId=208345968)  
[FWViewActive](http://tdn.totvs.com/display/framework/FWViewActive)  
[FWFormView - Objeto de criação de interface gráfica em MVC](http://tdn.totvs.com/display/framework/FWFormView)  
[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Operação de cópia em ponto de entrada MVC (Lcopia)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015971771)
