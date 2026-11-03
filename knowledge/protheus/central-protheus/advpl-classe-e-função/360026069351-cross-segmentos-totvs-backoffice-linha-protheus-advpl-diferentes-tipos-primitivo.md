---
article_id: 360026069351
category: ADVPL - Classe e Função
content_hash: 0a5df2f058110a9456a009d51ec1f20d555a5f48854b1b11b99c255fa26ae5cc
fetched_at: '2026-06-28T22:40:18.284787+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Diferentes tipos
  primitivos com tipagem forte
type: support-article
updated_at: '2022-01-06T18:48:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026069351-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Diferentes-tipos-primitivos-com-tipagem-forte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Seria possível utilizar mais de uma tipagem em uma variável TL++? Por exemplo a variável cUserId poder receber apenas os tipos caractere e numérico.  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.23  
  
**Solução**Na linguagem TL++ não é possível realizar tipagem múltipla, porém pode ser mantido o padrão legado da linguagem ADVPL não definindo a tipo primitivo da variável/propriedade.  
  
Fonte

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// VALIDAÇÃO DE TIPAGEM TL++  
User Function T191TIPAGEM()  
    Local cUserId // As Character // REMOVER A TIPAGEM  
  
    // COM A TIPAGEM REMOVIDA É POSSÍVEL ATRIBUIR  
    // MAIS DE UM TIPO PRIMITIVO A VARIÁVEL CUSERID  
    cUserId := "guilherme.bigois"  
    cUserId := 301000271  
Return (NIL)
```

**Saiba mais**  
[Tipagem de Dados](https://tdn.totvs.com/display/tec/Tipagem+de+Dados)
