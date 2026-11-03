---
article_id: 4414483695255
category: RH - CNAB
content_hash: 2acb8b18470b971dd59d31e9c839d5623ff5e7a8a13cf7908d6d29d2248ea529
fetched_at: '2026-06-28T22:43:39.235855+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Como utilizar o ponto de entrada GP450VAL
type: support-article
updated_at: '2025-06-16T18:26:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414483695255-RH-Linha-Protheus-GPE-Como-utilizar-o-ponto-de-entrada-GP450VAL
---

**Descrição:**

Este Ponto de Entrada é executado durante a geração do arquivo de Líquidos (Disquete Sispag), no momento que o funcionário corrente está sendo processado.

Neste momento é possível manipular as informações que serão gravadas no arquivo de saída através das variáveis disponíveis.

A função deve retornar Verdadeiro (.T.) ou Falso (.F.). Caso retorne falso, o sistema irá desprezar o funcionário corrente e passará para o próximo registro da tabela Cadastro de Funcionários (SRA).

**Programa Fonte**

```
.PRW
```

**Sintaxe**

GP450VAL - Líquido em Disquete - SISPAG II ( ) --> .T. ou .F.

Retorno

**.T. ou .F.**

(logico)* Se o retorno for falso, o registro que estiver sendo processado será desprezado.

**Exemplos:**  
  
User Function GP450VAL()

Local lRet := .F.

If AllTrim( SRA->RA\_MAT ) == "000001"

Alert("Passou pelo Ponto de Entrada: GP450VAL")

cNome := "FUNCIONARIO 000001" //Nome do funcionario

cConta := "1234567890" //Conta

cBanco := "3411234" //Banco/Agencia

nValor := 2000 //Valor

lRet := .T. //Retorno

EndIf

Return(lRet)

**Variáveis**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  | cNome |  |  | Caracter |  |  | Privado |  |  | Sim |  |  |  |  |
|  | cBanco |  |  | Caracter |  |  | Privado |  |  | Sim |  |  |  |  |
|  | cConta |  |  | Caracter |  |  | Privado |  |  | Sim |  |  |  |  |
|  | cCPF |  |  | Caracter |  |  | Privado |  |  | Sim |  |  |  |  |
|  | nValor |  |  | Numérico |  |  | Privado |  |  | Sim |  |  |  |  |
