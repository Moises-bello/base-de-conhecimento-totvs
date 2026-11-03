---
article_id: 16818928702615
category: Faturamento - Cenários de Venda
content_hash: fa358c1020b31bde69afcf59c168276050f97fed4121f893cd32bd5b3e47ffb8
fetched_at: '2026-06-28T22:38:34.121930+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  FT050MNU
type: support-article
updated_at: '2023-08-16T20:59:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16818928702615-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-FT050MNU
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16818960189847) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **FT050MNU - Antecede abertura do Browse**.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

O ponto de entrada **FT050MNU**é disparado:

* antes da abertura do Browse, caso Browse inicial da rotina esteja habilitado, ou
* antes da apresentação do Menu de opções, caso Browse inicial esteja desabilitado.

Para habilitar ou desabilitar o Browse, entre na rotina, clique em Configurações/Browse Inicial e selecione a opção desejada:

* **Sim** - Habilitar Browse Inicial
* **Não** - Desabilitar Browse Inicial

Este ponto de entrada pode ser utilizado para inserir novas opções no array aRotina.

**Exemplo**

```
#INCLUDE 'PROTHEUS.CH'  
#INCLUDE 'PARMTYPE.CH'  
  
User Function FT050MNU()  
  
    Local aRotina := {}  
  
    Alert("Passou pelo Ponto de Entrada FT050MNU")  
    Aadd(aRotina,{'TITULO DO BOTAO',"U_TESTE2()",0,3,0,NIL})  
  
Return aRotina  
  
User Function TESTE2()  
  
    Alert("Entrou na funcao de usuario TESTE2")  
  
Return Nil
```

**Saiba Mais**

**[FT050MNU - Antecede abertura do Browse](https://tdn.totvs.com/x/RIRn)**
