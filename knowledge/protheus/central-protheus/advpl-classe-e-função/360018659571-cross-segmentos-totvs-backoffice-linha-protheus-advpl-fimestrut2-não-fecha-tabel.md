---
article_id: 360018659571
category: ADVPL - Classe e Função
content_hash: 243097a7ecc6d01eef5eb47f7d9daf976bdf5e7965e364a3dad8a335d7c962ea
fetched_at: '2026-06-28T22:40:19.312296+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Fimestrut2 não
  fecha tabela estrut
type: support-article
updated_at: '2022-01-10T19:25:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018659571-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fimestrut2-n%C3%A3o-fecha-tabela-estrut
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao utilizar a função Estrut2() para efetuar a abertura da tabela ESTRUT e em seguida a função FimEstrut2(), a tabela não está sendo devidamente fechada.  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Este incidente é reproduzido quando não são passados todos os parâmetros necessários na função Estrut2().  
  
**Solução**Passar por referência o quarto parâmetro (oTempTable) na função Estrut2() e utilizá-lo para efetuar o fechamento na função FimEstrut2():

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
#Include "TBICONN.ch"  
  
// FUNÇÃO PRINCIPAL (CRIADA PARA TESTE)  
User Function VldEstrut()  
    Local nCont      := 0          // CONTADOR DE LAÇO  
    Local nQuant     := 1          // QUANTIDADE A SER EXPLODIDA  
    Local cProduto   := "PRDT0002" // PRODUTO  
    Local cArquivo   := ""         // ALIAS DO ARQUIVO TEMPORÁRIO  
    Local oTempTable := NIL        // NOME DO OBJETO UTILIZADO PELA TABELA  
    Private nEstru   := 0  
  
    RPCSetEnv("99", "01", NIL, NIL, "PCP", NIL, {"SG1"}) // SE VIA SMARTCLIENT, REMOVER ESTA LINHA  
        // EFETUA 1500 VEZES A ABERTURA E FECHAMENTO DA TABELA  
        While (nCont < 1500)  
            // EFETUA A ABERTURA DA TABELA  
            cArquivo := Estrut2(cProduto, nQuant, NIL, @oTempTable, .T.)  
            ConOut(ESTRUT->CODIGO)  
  
            nCont++ // AUTO INCREMENTA O CONTADOR DO LAÇO  
  
            // EFETUA O FECHAMENTO DA TABELA  
            FimEstrut2(NIL, oTempTable)  
            nEstru:=0  
            ConOut(nCont)  
        End  
    RPCClearEnv() // SE VIA SMARTCLIENT, REMOVER ESTA LINHA  
Return (NIL)
```

**Saiba mais**  
[ESTRUT2 - Explosão de estrutura cadastrada no SG1](http://tdn.totvs.com/pages/viewpage.action?pageId=287060852)  
[FIMESTRUT2 - Apagar os arquivos gerados pela função ESTRUT2](http://tdn.totvs.com/pages/viewpage.action?pageId=287060899)
