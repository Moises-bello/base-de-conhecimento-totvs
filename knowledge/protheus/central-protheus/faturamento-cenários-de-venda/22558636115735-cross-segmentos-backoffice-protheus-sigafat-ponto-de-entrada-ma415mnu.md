---
article_id: 22558636115735
category: Faturamento - Cenários de Venda
content_hash: 1e6b7d33450264d7a65897360e665d74bd5ca981b17707880863a50156cb5ae1
fetched_at: '2026-06-28T22:38:34.046427+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Ponto de entrada "MA415MNU"
type: support-article
updated_at: '2024-04-05T11:54:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22558636115735-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Ponto-de-entrada-MA415MNU
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22558636099095) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Qual é o exemplo de utilização do Ponto de Entrada MA415MNU?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
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
  
User Function MA415MNU()  
  
    Alert("Passou pelo Ponto de Entrada MA415MNU")  
    Aadd(aRotina,{'TITULO DO BOTAO',"U_TESTE2()",0,3,0,NIL})  
  
Return aRotina  
  
User Function TESTE2()  
  
    Alert("Entrou na função de usuário TESTE2")  
  
Return Nil
```

**OBS:** Toda função passada na posição 2 da inserção de array no deve apresentar os parenteses:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22558657925143)

**Saiba Mais**

**[Ponto de Entrada MA415MNU](https://tdn.totvs.com/x/FYVn)**
