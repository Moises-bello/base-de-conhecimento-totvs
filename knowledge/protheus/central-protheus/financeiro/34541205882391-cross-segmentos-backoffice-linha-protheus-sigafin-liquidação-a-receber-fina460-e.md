---
article_id: 34541205882391
category: Financeiro
content_hash: e2e21ea04098f7fe71d9978f4757a5272a3a35fe7191163b8edf59304f3697ef
fetched_at: '2026-06-28T22:38:03.382694+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice linha Protheus - SIGAFIN - Liquidação a receber
  (FINA460) - ExecAuto. Podemos utilizar Begin Transaction em um fonte customizado
  e chamar um execauto padrão e depois encerrar  End Transaction?
type: support-article
updated_at: '2025-09-08T18:41:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34541205882391-Cross-Segmentos-Backoffice-linha-Protheus-SIGAFIN-Liquida%C3%A7%C3%A3o-a-receber-FINA460-ExecAuto-Podemos-utilizar-Begin-Transaction-em-um-fonte-customizado-e-chamar-um-execauto-padr%C3%A3o-e-depois-encerrar-End-Transaction
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34541205851415) Tempo aproximado para leitura: **00:15:00min**  
  
**Dúvida**  
Podemos utilizar Begin Transaction em um fonte customizado e chamar um execauto padrão e depois encerrar  End Transaction?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
A utilização do comando **Begin Transaction** em conjunto com rotinas automáticas (ExecAuto) padrão não é recomendada, exceto quando expressamente documentado no execauto pontual da rotina a sua utilização.  
  
Essa prática pode interferir nos controles internos de transação do sistema, resultando em comportamentos inesperados, tais como:

* **Tabelas temporárias não finalizadas, causando erros como:**  
  **"Application Server Work area table full (Max=1024)"**
* **Falhas de validação**
* **Inconsistências de dados**
* **Outros erros não previstos**

Caso o controle de transação seja realmente necessário, recomenda-se uma análise criteriosa e o uso de DisarmTransaction() com responsabilidade, evitando conflitos com o fluxo padrão do sistema.

Por esse motivo, nas documentações oficiais de cada ExecAuto de cada rotina deve estar claramente especificado quais comandos e práticas são permitidos.

**Exemplo de falha:**

```
User Function U_TESTEFINA()  
  
Local lSucesso := .T.  
Local aParametros := {}  
  
  
Begin Transaction // Não é recomendado ter essa chamada, a não ser que tenha documentado na documentação da rotina oficinal o uso do Begin Transaction  
  
aParametros := {  
"FILIAL" => "01", // Código da filial  
"TIPO" => "R", // Tipo de título: R = Receber, P = Pagar  
"NUMERO" => "000123", // Número do título  
"PARCELA" => "01", // Parcela  
"VALOR" => 100.00, // Valor da baixa  
}  
  
lSucesso := ExecAuto("FINA460", aParametros) // <---- Chamada de um execauto exemplo  
  
DisarmTransaction()  
  
End Transaction // Não é recomendado ter essa chamada, a não ser que tenha documentado na documentação da rotina oficinal o uso do End Transaction  
  
Return
```

**Saiba mais:**  
[ADVPL - Begin transaction](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020775851-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Begin-transaction)

[Controle de transações](https://tdn.totvs.com/pages/releaseview.action?pageId=271843449)

[Liquidação a receber (FINA460) - ExecAuto](https://tdn.totvs.com/pages/releaseview.action?pageId=650494634)
