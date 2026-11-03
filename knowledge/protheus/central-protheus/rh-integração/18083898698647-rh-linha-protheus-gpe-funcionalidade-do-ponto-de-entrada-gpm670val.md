---
article_id: 18083898698647
category: RH - Integração
content_hash: 100b071e562aa0dbaed4a4f6076f6ec74b5beeebc77bb847985db22a6a734c95
fetched_at: '2026-06-28T22:43:44.948052+00:00'
product: protheus
section_id: 360003115611
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionalidade do ponto de entrada GPM670VAL
type: support-article
updated_at: '2025-09-11T11:30:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18083898698647-RH-Linha-Protheus-GPE-Funcionalidade-do-ponto-de-entrada-GPM670VAL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18083921376279) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Funcionalidade do ponto de entrada GPM670VAL  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
  
**Solução**

Ponto-de-Entrada: **GPM670VAL - Validação do Título no Financeiro**

|  |  |
| --- | --- |
| Versões: | A partir Microsiga Protheus 10 |
| Compatível Países: | Todos |
| Sistemas Operacionais: | Todos |
| Compatível às Bases de Dados: | Todos |

Ponto de entrada permite usuário fazer validação da integração do título no financeiro  
  
**Programa Fonte**GPEM670.PRX

**Sintaxe**

GPM670VAL - Validação do Título no Financeiro ( [ ] ) --> lRet

Parâmetros:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  |  |  |  | Array of Record |  |  |  |  |  |  |  |  |  |  |  |  |  |

Retorno

**lRet**

(logico)* Indica se é permitido realizar a integração ou não

Observações

O ponto de entrada deve retornar um valor lógico. .T. indica que a rotina deve realizar a integração e .F. indica que não deve realizar a integração.

**Exemplos:**

Nesse exemplo, é verificado se o valor do título ultrapassa R$ 1500. Caso o valor seja maior a rotina não realiza a integração com o financeiro.  
  
#INCLUDE 'PROTHEUS.CH',

User Function GPM670VAL()

Local lRet := .T.//Alert( "Passou pelo PE GPM670VAL" )//

//Processos de validação

If RC1->RC1\_VALOR >= 1500

lRet := .F.

EndIf

Return (lRet)

**Variáveis**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  |  |  |  | Array of Record |  |  | Global |  |  | Não |  |  |  |  |

![GP670VAL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18084909040791)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Quais os pontos de entrada disponíveis na rotina GPEM670](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018319712-RH-Linha-Protheus-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM670)

[RH - Linha Protheus - GPE - Na integração de títulos é apresentada a mensagem: Um ou mais campos obrigatórios não foram preenchidos C. de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057605734-RH-Linha-Protheus-GPE-Na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-%C3%A9-apresentada-a-mensagem-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-C-de-Custo)

<https://tdn.totvs.com/pages/releaseview.action?pageId=6079202>
