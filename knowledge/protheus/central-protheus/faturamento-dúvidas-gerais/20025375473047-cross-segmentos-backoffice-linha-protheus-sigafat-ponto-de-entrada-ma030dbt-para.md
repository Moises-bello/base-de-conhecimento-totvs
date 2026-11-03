---
article_id: 20025375473047
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: a1b073ee1671749e57ccbac95957328026dde6c234deba2039d4073893773b34
fetched_at: '2026-06-28T22:38:33.002710+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Ponto de Entrada
  MA030DBT para CRMA980 (versão MVC)
type: support-article
updated_at: '2023-12-21T16:38:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20025375473047-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-MA030DBT-para-CRMA980-vers%C3%A3o-MVC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20025375454103) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual o exemplo de uso do PE MA030DBT para CRMA980 (versão MVC)?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Protheus 12 e superiores.

**Solução**OBS: Não é possível usar o ponto de entrada para as rotinas CRMA980 e MATA030 ao mesmo tempo (MVC e sem MVC), para utilizar sem MVC, utilize esse exemplo: [Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Ponto de Entrada MA030DBT para MATA030 (versão não MVC)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20025337804567)

Se usar esse ponto de entrada e houver rotinas sem MVC nos menus dos usuários (MV\_MVCSA1 - .F. | rotina MATA030 - Cadastro de Clientes), ao entrar nessas rotinas MATA030 dará error.log.

**Exemplo do Ponto de Entrada MA030DBT para CRMA980 (versão MVC):**

```
#INCLUDE 'PRTOPDEF.CH'
#INCLUDE 'PROTHEUS.CH'
#INCLUDE "FWMVCDEF.CH"

//Em MVC

User Function MA030DBT()
Local aButtons := {} //Array dos botões
 
Alert("Passou pelo ponto de entrada MA030DBT em MVC, iniciando.")

// Necessário informar na segunda posição em quais operações o botão irá aparecer
// para que o botão não apareça em nenhuma operação, informar um array vazio

// Visualização (MODEL_OPERATION_VIEW)
// Inclusão     (MODEL_OPERATION_INSERT)
// Alteração    (MODEL_OPERATION_UPDATE)
// Exclusão     (MODEL_OPERATION_DELETE)

aAdd( aButtons, { "perfis tributários", { MODEL_OPERATION_VIEW, MODEL_OPERATION_INSERT, MODEL_OPERATION_UPDATE, MODEL_OPERATION_DELETE } } )
// Opção "Perfir tributários" vai aparecer em todas as operações

aAdd( aButtons, { "referencias", {} } )
// Opção "Referências" não vai aparecer em operação nenhuma (array vazio)
 
Alert("Ponto de entrada MA030DBT - MVC ativado com sucesso.")
 
Return aButtons
```
