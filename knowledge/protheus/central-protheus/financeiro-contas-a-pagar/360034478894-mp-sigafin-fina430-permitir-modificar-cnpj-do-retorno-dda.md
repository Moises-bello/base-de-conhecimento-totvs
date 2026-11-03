---
article_id: 360034478894
category: Financeiro - Contas a Pagar
content_hash: d0ccd964b193644594b1b79bd271203c432df79bb5f48247d226fc060b5eb398
fetched_at: '2026-06-28T22:38:09.921666+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - FINA430 - Permitir modificar CNPJ do retorno DDA
type: support-article
updated_at: '2021-04-28T15:18:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034478894-MP-SIGAFIN-FINA430-Permitir-modificar-CNPJ-do-retorno-DDA
---

**Dúvida**  
Como modificar CNPJ do retorno DDA?  
   
 **Ambiente**  
Microsiga Protheus - Financeiro - A partir da versão 11.80  
   
**Solução**Ponto-de-Entrada: **FA430FIG - Permitir modificar CNPJ do retorno DDA  
  
Descrição:**Este Ponto de Entrada permite modificar o **CNPJ** obtido da leitura do arquivo de **retorno DDA**, de modo que a tabela **SA2** seja posicionada por meio do **CNPJ** modificado neste Ponto de Entrada.

**Eventos:**

Antes da gravação do movimento DDA na tabela FIG.

Programa Fonte **FINA430.PRX**

**Sintaxe:**  
**FA430FIG** - Permitir modificar CNPJ do retorno DDA ( < cCNPJ> ) --> cCNPJ

****Parâmetros:****

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | cCNPJ |  |  | Caracter |  |  | CNPJ obtido do arquivo de retorno DDA |  |  |  |  |  | X |  |  |  |  |

  
**Retorno:**

**cCNPJ**(caracter)  
      CPNJ customizado no ponto de entrada **FA430FIG**

**Observações:**  
Está presente na função fA430Ger()

**Exemplos:**

```
#include "rwmake.ch"User Function FA430FIG             
Local cCNPJ := ParamIxb[1]cCNPJ := SubStr( cCNPJ, 1, Len( cCNPJ ) - 2 )  
Aviso( "Ponto de Entrada FA430FIG", "CNPJ modificado: " + cCNPJ, { "Ok" } )  
Return cCNPJ
```

**Variáveis:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  |  |  |  | Array of Record |  |  | Global |  |  | Não |  |  |  |  |
