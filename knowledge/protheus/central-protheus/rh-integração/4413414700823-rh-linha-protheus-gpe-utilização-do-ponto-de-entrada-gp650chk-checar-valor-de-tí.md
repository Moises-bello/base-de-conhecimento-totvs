---
article_id: 4413414700823
category: RH - Integração
content_hash: 855b9a69873475042db4619aba0bf9a067a161f2d71a16ae105776b3def6f58b
fetched_at: '2026-06-28T22:43:44.986741+00:00'
product: protheus
section_id: 360003115611
source: central-protheus
title: RH - Linha Protheus - GPE - Utilização do ponto de entrada GP650CHK - Checar
  valor de títulos
type: support-article
updated_at: '2025-09-11T12:10:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413414700823-RH-Linha-Protheus-GPE-Utiliza%C3%A7%C3%A3o-do-ponto-de-entrada-GP650CHK-Checar-valor-de-t%C3%ADtulos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28422841018903) Tempo aproximado para leitura: **01:00:00** min**Dúvida**Utilização do ponto de entrada GP650CHK  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões

**Solução**

**01. Visão Geral**

O ponto de entrada GP650CHK serve para checar o valor do título e está localizado dentro da função fGravTit (Gravação dos valores gerados no arquivo de títulos).

**Programa Fonte**  
GPEM650.PRW

Sintaxe  
GP650CHK - Checar Valor de Títulos ( )  
Retorno  
Deve ser Retornado um array com duas posições:

* Na primeira, deve ser retornado o Recno do registro.
* Na segunda, uma variável lógica para execução ou não da gravação do titulo.

       aRet[1] := Numérico (Recno)

       aRet[2] := Lógico (Validação do Registro)

**02. Variáveis**

Outras Ações / Ações relacionadas

| Nome | Tipo | Escopo | Pode Alterar |
| --- | --- | --- | --- |
| nVlTotTit | Numérico | Privado | Não |

**Importante:**

#### Caso seja uma inclusão a primeira posição do array de retorno ( aRet[1] ) deve ser 0, dessa forma um novo registro será gerado na tabela RC1. Caso seja retornado um RECNO válido da tabela RC1 o valor do título ( nVlTotTit ) será somado ao campo RC1\_VALOR do registro indicado.

**Saiba Mais:**  
<https://tdn.totvs.com/display/PROT/GP650CHK+-+Checar+Valor+de+Titulos>
