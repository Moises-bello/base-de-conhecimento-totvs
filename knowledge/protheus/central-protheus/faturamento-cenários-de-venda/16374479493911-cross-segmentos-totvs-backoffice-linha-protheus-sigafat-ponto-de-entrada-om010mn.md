---
article_id: 16374479493911
category: Faturamento - Cenários de Venda
content_hash: 8c0e409cfedd997a2161a3290f0737ee5472c33fd8558ede1bacfbd9d97f95fe
fetched_at: '2026-06-28T22:38:34.129054+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  OM010MNU
type: support-article
updated_at: '2023-07-28T20:13:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16374479493911-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-OM010MNU
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16374465858327) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **OM010MNU - Inclusão de novas opções**.  
  
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
  
User Function OM010MNU()  
  
    Alert("Passou pelo Ponto de Entrada OM010MNU")  
    Aadd(aRotina,{'TITULO DO BOTAO',"U_TESTE()",0,3,0,NIL})  
  
Return aRotina  
  
User Function TESTE()  
  
    Alert("Entrou na funcao de usuario TESTE")  
  
Return Nil
```

**Saiba Mais**

**[PE OM010MNU - Inclusão de novas opções](https://tdn.totvs.com/x/NhihJQ)**
