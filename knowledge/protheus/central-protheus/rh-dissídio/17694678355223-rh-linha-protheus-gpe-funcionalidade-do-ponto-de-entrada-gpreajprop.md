---
article_id: 17694678355223
category: RH - Dissídio
content_hash: f5cdbfa3825bf14a2c798bbbff4b3916d23562a5194c01e5a2d837ace65bd8be
fetched_at: '2026-06-28T22:43:43.378814+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionalidade do ponto de entrada GPREAJPROP
type: support-article
updated_at: '2025-08-08T14:52:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17694678355223-RH-Linha-Protheus-GPE-Funcionalidade-do-ponto-de-entrada-GPREAJPROP
---

Ponto-de-Entrada: **GPREAJPROP - Altera Meses Proporcionais no Cálculo do Dissídio Retroativo**

|  |  |
| --- | --- |
| Abrangências: | Microsiga Protheus 10 , Microsiga Protheus 11 |
| Versões: | Microsiga Protheus 10 , Microsiga Protheus 11 |
| Compatível Países: | Todos |
| Sistemas Operacionais: | Todos |
| Compatível às Bases de Dados: | Todos |
| Idiomas: | Português (Brasil) |

**Descrição:**

Este ponto de entrada altera os meses proporcionais caso o cálculo do Dissídio Retroativo seja proporcional à admissão do funcionário

**Programa Fonte:**

GPEM690

**Sintaxe**

GPREAJPROP - Altera Meses Proporcionais no Cálculo do Dissídio Retroativo ( [ ] )

Parâmetros:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  |  |  |  | Numérico |  |  |  |  |  |  |  |  |  |  |  |  |  |

Retorno

(nulo)

**Exemplos:**  
User Function GPREAJPROP ()   
nBaseMesAux:= 6  
Return Nil

**Variáveis**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  | nBaseMesAux |  |  | Numérico |  |  | Privado |  |  | Sim |  |  | Meses a serem utilizados como base no Cálculo do Dissídio Retroativo |  |

![GPREAJPROP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17708210437527)

**Saiba Mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6079249>
