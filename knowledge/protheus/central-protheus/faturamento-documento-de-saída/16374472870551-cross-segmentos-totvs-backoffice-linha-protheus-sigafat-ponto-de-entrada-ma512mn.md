---
article_id: 16374472870551
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: e90f0fac00cbd7099f035aa6662caea5c368fa4560399c52e4e43df4465ea098
fetched_at: '2026-06-28T22:38:45.443728+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  MA512MNU
type: support-article
updated_at: '2023-07-28T20:11:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16374472870551-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-MA512MNU
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16374457548439) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **MA512MNU - Habilitar ou desabilitar browse**.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Esse ponto de entrada é **executado** **antes da abertura do Browse** (caso Browse inicial da rotina esteja habilitado) ou **antes da apresentação do Menu de opções** (caso Browse inicial esteja desabilitado).

Para **habilitar** ou **desabilitar** o Browse, entre na rotina, clique em Configurações/Browse Inicial e selecione a opção desejada:   
**Sim -** Habilitar Browse inicial   
**Não -** Desabilitar Browse inicial   
  
Esse ponto de entrada pode ser utilizado para **inserir novas opções** no array aRotina.  
  
**Exemplo**

```
#INCLUDE 'PROTHEUS.CH'  
#INCLUDE 'PARMTYPE.CH'  
  
User Function MA512MNU()  
  
    Alert("Passou pelo Ponto de Entrada MA512MNU")  
    Aadd(aRotina,{'TITULO DO BOTAO',"U_TESTE()",0,3,0,NIL})  
  
Return aRotina  
  
User Function TESTE()  
  
    Alert("Entrou na funcao de usuario TESTE")  
  
Return Nil
```

**Saiba Mais**

**[MA512MNU - Habilitar ou desabilitar browse](https://tdn.totvs.com/x/KoVn)**
