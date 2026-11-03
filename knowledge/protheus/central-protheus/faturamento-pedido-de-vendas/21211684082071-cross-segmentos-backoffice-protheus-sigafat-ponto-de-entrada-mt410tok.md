---
article_id: 21211684082071
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: f51268f4b7304ca4362b4b02e353df5cc51d0de52b2dac1bd62f0214512cb129
fetched_at: '2026-06-28T22:38:39.958040+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Ponto de entrada MT410TOK
type: support-article
updated_at: '2026-04-07T19:28:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21211684082071-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Ponto-de-entrada-MT410TOK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21211686483607) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**

Como utilizar o ponto de entrada MT410TOK e qual seu conceito?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

Este ponto de entrada é executado ao clicar no botão OK e pode ser usado para validar a confirmação das operações: incluir, alterar, copiar e excluir.

Se o ponto de entrada retorna o conteúdo .T., o sistema continua a operação, caso contrário, volta para a tela do pedido.

Esse ponto de entrada serve para deixar o pedido de venda ser incluído ou não mediante validações do usuário.

Ele funciona em rotinas automáticas (ExecAuto).

**Retorno:** lRet (booleano)

**Exemplo:**

```
#INCLUDE 'PROTHEUS'

User Function MT410TOK()

Local lRet := .T. // Conteudo de retorno
Local nOpc := PARAMIXB[1] // Opcao de manutencao
Local aRecTiAdt := PARAMIXB[2] // Array com registros de adiantamento
Local cMsg := "nOpc(PARAMIXB[1]): " + cValToChar(nOpc) + " e aRecTiAdt(PARAMIXB[2]): " + cValToChar(aRecTiAdt) + "." // Mensagem de al

Aviso("Teste PE - A410VldTOK (Título) ", cMsg, {"OK"})

If 1 < 3 // Validação customizada
    lRet := .F. // O pedido de venda não será concluido (ficará na tela de pedido de venda sem conseguir salvar) com 'lRet = .F.'
EndIf

Return(lRet)
```

**Saiba mais:**

[MT410TOK - Validar confirmação da operação](https://tdn.totvs.com/x/YYVn)
