---
article_id: 15867594425751
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 47c1c34b0c9ba0f070e19f6c9c8c8ce6c812bcd3d717cfca1a2400e38d196cc1
fetched_at: '2026-06-28T22:38:42.754316+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - MA410MNU
type: support-article
updated_at: '2023-07-07T20:28:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15867594425751-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-MA410MNU
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15867636498327) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **MA410MNU**  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Ponto de entrada disparado **antes da abertura do Browse**, caso Browse inicial da rotina esteja habilitado, ou antes da apresentação do Menu de opções, caso Browse inicial esteja desabilitado.

Para habilitar ou desabilitar o Browse, entre na rotina, clique em Configurações/Browse Inicial e selecione a opção desejada:  
**Sim -** Habilitar Browse Inicial  
**Não -** Desabilitar Browse Inicial

Este ponto de entrada pode ser utilizado para inserir novas opções no array aRotina.

**Exemplo**

```
#INCLUDE 'PROTHEUS.CH'  
#INCLUDE 'PARMTYPE.CH'  
  
User Function MA410MNU()  
  
    Alert("Passou pelo Ponto de Entrada MA410MNU")  
    Aadd(aRotina,{'TITULO DO BOTAO',"U_TESTE2()",0,3,0,NIL})  
  
Return aRotina  
  
User Function TESTE2()  
  
    Alert("Entrou na funcao de usuario TESTE2")  
  
Return Nil
```

**Saiba Mais**

**[Ponto de Entrada MA410MNU](https://tdn.totvs.com/x/DoVn)**
