---
article_id: 16940255364887
category: Faturamento - Cadastros
content_hash: cc4bedfd83fff25b8c86c7e01e1f2dfdc415629d1a8eae5c8e2282462ad8884b
fetched_at: '2026-06-28T22:38:36.608553+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  CRMA980 - CRM980MDEF
type: support-article
updated_at: '2023-08-22T13:06:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16940255364887-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-CRMA980-CRM980MDEF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16940214902679) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **CRM980MDEF - Adiciona novas funcionalidades em Ações Relacionadas no browse**.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

A finalidade do ponto de entrada **CRM980MDef** é permitir inclusão de **novas funcionalidades** em **"Outras Ações"** no browse de clientes;  
  
**Exemplo**

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "FWMVCDEF.CH"  
  
User Function CRM980MDEF()  
  
    Local aRotina := {}  
  
    //----------------------------------------------------------------------------------------------------------  
    // [n][1] - Nome da Funcionalidade  
    // [n][2] - Função de Usuário  
    // [n][3] - Operação (1-Pesquisa; 2-Visualização; 3-Inclusão; 4-Alteração; 5-Exclusão)  
    // [n][4] - Acesso relacionado a rotina, se esta posição não for informada nenhum acesso será validado  
    //----------------------------------------------------------------------------------------------------------  
  
    aAdd(aRotina,{"Funcao A","ApMsgAlert('Funcao A')",MODEL_OPERATION_VIEW,0})  
    aAdd(aRotina,{"Funcao B","ApMsgAlert('Funcao B')",MODEL_OPERATION_VIEW,0})  
  
Return( aRotina )
```

**Saiba Mais**

**[PE CRM980MDEF Adiciona novas funcionalidades em Ações Relacionadas no browse](https://tdn.totvs.com/x/R6sGEQ)**
