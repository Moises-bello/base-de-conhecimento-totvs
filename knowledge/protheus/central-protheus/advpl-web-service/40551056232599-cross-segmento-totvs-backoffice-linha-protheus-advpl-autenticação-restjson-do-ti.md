---
article_id: 40551056232599
category: ADVPL - Web Service
content_hash: 7c4f3962883ec167791905ffa5da0916c309e2eddd2a2405f1efff90e4106b26
fetched_at: '2026-06-28T22:40:10.531826+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Autenticação REST/JSON
  do tipo Digest
type: support-article
updated_at: '2026-06-15T13:45:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40551056232599-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Autentica%C3%A7%C3%A3o-REST-JSON-do-tipo-Digest
---

No Protheus, não há suporte nativo para autenticação digest em requisições REST via ADVPL; apenas BASIC ou Token (JWT) são suportados.

Para usar digest, é necessário montar manualmente o cabeçalho de autenticação, aplicando algoritmos de criptografia e codificando em Base64, conforme a documentação da API destino.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40552430288919)Tempo aproximado para leitura:**00:01:45 min**  
  
**Dúvida**  
Como realizar a autenticação do tipo digest em comunicações REST/JSON via ADVPL?

**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - A partir da versão 12.23.10

**Solução**   
Atualmente, não há uma função, classe ou método nativo homologado no Protheus para realizar a autenticação do tipo DIGEST de forma automática em requisições REST. Para integrações REST, as opções suportadas nativamente pelo framework são a autenticação *BASIC* ou via *Token* (JWT).  
  
Caso seja mandatório o uso da autenticação do tipo *digest* no *endpoint* de destino, será necessário desenvolver a montagem do cabeçalho de autenticação manualmente via código ADVPL.   
  
A autenticação *digest* normalmente exige o envio de informações como *nonce, timestamp* e senha, que são submetidas a um algoritmo de criptografia (como SHA) e posteriormente convertidas para ***Base64***.  
É necessário avaliar a documentação da API terceira (sistema destino) para confirmar quais informações são exigidas no *payload* e qual o algoritmo de criptografia adotado pelo servidor.   
  
Segue um exemplo utilizando a **FWRETSrest** em que, caso o destino exija a criptografia **SHA256**, a lógica estrutural da *string* no ADVPL seguiria o formato:

```
#INCLUDE "PROTHEUS.CH"
#INCLUDE "RESTFUL.CH"

User Function TstDgstR()
    Local oRest       := FWRest():New()
    Local aHeader     := {}
    Local cUrl        := "https://api.exemplo.com.br/v1/endpoint" //informar sua API de exemplo
    Local cUser       := "usuario_api"
    Local cPass       := "senha_api"
    Local cNonce      := "nonce_fornecido_pelo_servidor" 
    Local cStringAuth := ""
    Local cDigestHash := ""
    Local cResponse   := ""

    cStringAuth := cUser + cPass + cNonce
    cDigestHash := Encode64( SHA256( cStringAuth ) );/<------aqui ocorre a uitilização da criptografia
    aAdd( aHeader, "Authorization: Digest " + cDigestHash )// Temos a construção de header de exemplo
    aAdd( aHeader, "Content-Type: application/json" )

    oRest:SetPath( cUrl )
    If oRest:Get( aHeader )
        cResponse := oRest:GetResult()
        ConOut("Requisição realizada com sucesso: " + cResponse)
    Else
        ConOut("Erro na requisição REST. Detalhe: " + oRest:GetLastError())
    EndIf

Return .T.
```

Para viabilizar essa implementação customizada, utilize as funções de criptografia nativas disponibilizadas pela linguagem ADVPL para tratar a *string* antes do envio da requisição.

**Saiba Mais**  
[SHA256](https://tdn.totvs.com/display/tec/SHA256)  
[Criptografia](https://tdn.totvs.com/display/tec/Criptografia)  
[FWRest](https://tdn.totvs.com/display/public/framework/FWRest)
