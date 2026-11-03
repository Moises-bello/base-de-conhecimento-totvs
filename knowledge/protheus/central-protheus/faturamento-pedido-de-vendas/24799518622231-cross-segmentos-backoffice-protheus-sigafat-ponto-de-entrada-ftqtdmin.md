---
article_id: 24799518622231
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 63b5ad5ad607e076f0af04de317cc63a337c9601b31a7f7a06ca43011ac5fa02
fetched_at: '2026-06-28T22:38:39.955358+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Ponto de entrada FTQTDMIN
type: support-article
updated_at: '2024-07-11T11:29:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24799518622231-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Ponto-de-entrada-FTQTDMIN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24799518588439) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como usar o ponto de entrada FTQTDMIN com exemplos?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**Este ponto de entrada está dentro da função FtVldQtVen() - FATXFUN, que verifica se a quantidade que se está vendendo de um produto é a do seu lote mínimo.

Esta função exibe um aviso quando a quantidade vendida difere do lote mínimo e não permite a venda do produto. Este ponto de entrada passa essa decisão ao usuário invés da decisão do produto padrão.

**Exemplo simples:**

```
#INCLUDE 'TOTVS.CH'
#INCLUDE 'PRTOPDEF.CH'

User Function FTQTDMIN()
    // .T. - Permite a venda
    // .T. - Não permite a venda
    Local lRet := .F.

    If 2 > 1       // Validação customizada (implementar a desejada)
        lRet := .T.
    ElseIf 10 > 9  // Validação customizada
        lRet := .T.
    EndIf
 
    Alert("Fim do ponto de entrada FTQTDMIN")
Return lRet
```

**Saiba mais:**

[FTQTDMIN - Verifica quantidade de produto](https://tdn.totvs.com/x/fYRn)
