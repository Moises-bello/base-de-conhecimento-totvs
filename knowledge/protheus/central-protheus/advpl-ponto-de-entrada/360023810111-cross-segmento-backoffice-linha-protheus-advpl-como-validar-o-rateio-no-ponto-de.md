---
article_id: 360023810111
category: ADVPL - Ponto de Entrada
content_hash: bb21a1540d9964d6fa97ed226aec7b93d3f3f8164fac221f51550b88d80d2919
fetched_at: '2026-06-28T22:40:11.512494+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Como validar o rateio
  no ponto de entrada F050RAT?
type: support-article
updated_at: '2021-12-21T17:22:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023810111-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Como-validar-o-rateio-no-ponto-de-entrada-F050RAT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:04:00 min  
  
Dúvida**Ao utilizar o ponto de entrada **F050RAT** não há dados disponíveis para validarmos as linhas digitadas na grid de rateio da rotina de Contas a Pagar (FINA050), assim sendo como validar os dados digitados pelo usuário?  
  
**Ambiente**  
Cross Segmento - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Ao utilizar o ponto de entrada **F050RAT** é possível enxergar os dados da grid por meio da tabela temporária TMP:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021265511/mceclip0.png)  
  
Todavia por ser um ponto de entrada de validação total da rotina, o mesmo não tem como foco manter a linha posicionada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021265791/mceclip1.png)  
Desta forma, torna-se necessário que ao entrar a primeira vez no ponto seja utilizada a função **DbGoTop()** para avançar ao primeiro registro da tabela temporária e efetuar as devidas validações.  
  
Fonte

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// FUNÇÃO PRINCIPAL  
User Function F050RAT()  
    Local lValid :=.T.                    // VARIÁVEL PARA CONTROLE  
    Local cAlias := aHeader[1][9]         // APELIDO DA TABELA UTILIZADA  
    Local aArea  := (cAlias)->(GetArea()) // CAPTURA O ESTADO ATUAL DA TABELA  
  
    // POSICIONA NO TOPO DA TABELA  
    (cAlias)->(DbGoTop())  
  
    // LAÇO NA QUANTIDADE DE LINHAS DO ARQUIVO  
    While (!(cAlias)->(EOF()))  
        // **EXEMPLO 01: VERIFICA SE A CONTA DE CRÉDITO E DÉBITO SÃO IGUAIS  
        If (AllTrim((cAlias)->CTJ_DEBITO) == AllTrim((cAlias)->CTJ_CREDIT))  
            lValid := .F.  
  
            Help(NIL, NIL, "EQUAL_CRED_DEB", NIL, "As entidades de crédito e débito estão iguais",;  
                1, 0, NIL, NIL, NIL, NIL, NIL, {"Altere uma das entidades para prosseguir com a gravação."})  
        // **EXEMPLO 02: VERIFICA SE O RATEIO PARA UMA DAS UNIDADES É MAIOR QUE 70%  
        ElseIf ((cAlias)->CTJ_PERCEN >70)  
            lValid := .F.  
  
            Help(NIL, NIL, "INVALID_PERCENT", NIL, "O percentual de rateio está maior que 70%",;  
                1, 0, NIL, NIL, NIL, NIL, NIL, {"Reduza o percentual de rateio entre as entidades."})  
        EndIf  
  
        // PULA PARA O PRÓXIMO REGISTRO  
        (cAlias)->(DbSkip())  
    End  
  
    // RESTAURA O ESTADO ANTERIOR DA TABELA  
    RestArea(aArea)  
Return (lValid)
```

**Saiba mais**  
[F050RAT - Ponto de Entrada executado durante a validação da aCols](http://tdn.totvs.com/pages/viewpage.action?pageId=57410083)  
[DBGOTOP() - Posiciona no inicio do arquivo de dados](http://tdn.totvs.com/pages/viewpage.action?pageId=23889274)
