---
article_id: 360018668771
category: ADVPL - Classe e Função
content_hash: 185f23894fdc244a402b3da4af9714fc96f23271905d669dd602271fc590d7c0
fetched_at: '2026-06-28T22:40:15.745489+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Declaração de sgbd
  'max' não funciona em advpl
type: support-article
updated_at: '2025-07-07T19:00:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018668771-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Declara%C3%A7%C3%A3o-de-sgbd-max-n%C3%A3o-funciona-em-advpl
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28309375638167)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Ao utilizar a declaração de banco "MAX" para trabalhar com grandes tipos de dados, é retornado erro nas funções de execução de comandos SQL (*Structured Query Language*) na linguagem ADVPL (*Advanced Protheus Language*).  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**O problema acontece devido ao *driver SQL Server Native Client*, que retorna o tamanho da coluna NVARCHAR(MAX) retornar o valor de tamanho como 0.  
  
**Solução**Caso seja utilizado o driver SQL Server, o DbAccess irá identificar esse tipo como campo Memo e retirar essa coluna do retorno, conforme documentado no TDN em [DbAccess - Perguntas frequentes](http://tdn.totvs.com/display/tec/DBAccess+-+Perguntas+frequentes).  
Para resolver essa situação, deve-se alterar a declaração MAX para um valor numérico (8000, por exemplo), pois dessa forma o DbAccess irá identificar como campo caractere e retornar o valor corretamente.  
  
Exemplo

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
#Include "TOPCONN.ch"  
#Include "TBICONN.ch"  
  
// FUNÇÃO PRINCIPAL (PARA TESTE)  
User Function TTCQUERY()  
    Local cQuery := ""  
  
    RPCSetEnv("99", "01") // REMOVER SE EXECUTADO VIA SMARTCLIENT  
        // cQuery += "SELECT CONVERT(VARCHAR(MAX), " // REMOVER E TROCAR POR NÚMERO  
        cQuery += "SELECT CONVERT(VARCHAR(8000), "  
        cQuery += "(SELECT TOP 1 C6_MOPC FROM SC6990 "  
        cQuery += "WHERE C6_NUM = 'PDV024')) AS BINARY_TO_VARCHAR"  
  
        TCQUERY cQuery NEW ALIAS QRY  
    RPCClearEnv() // REMOVER SE EXECUTADO VIA SMARTCLIENT  
Return (NIL)
```

Para campos com valores extensos é necessário verificar as configurações das chaves MaxStringSize e MemoMega para que possa efetuar a leitura desses campos. Verificar os limites das chaves em suas documentações.

**Saiba mais**  
[Microsoft docs - Using large value types](https://docs.microsoft.com/en-us/sql/relational-databases/native-client/features/using-large-value-types?view=sql-server-2017)

[MaxStringSize](https://tdn.totvs.com/pages/viewpage.action?pageId=161349793)

[MemoMega](https://tdn.totvs.com/display/tec/Application+Server+-+%5BDBAccess%5D+-+MemoMega)
