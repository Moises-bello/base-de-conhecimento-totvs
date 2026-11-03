---
article_id: 37839579944599
category: Financeiro - Compensação Contas a Pagar
content_hash: 9d18a62a2f961e626efdd72154fe0029ac881b9565d30fa09b51361edf4449b2
fetched_at: '2026-06-28T22:37:33.681641+00:00'
product: protheus
section_id: 35057559197335
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA340 É possível
  realizar compensação de uma devolução do tipo:NDF com o tipo:INS impostos de INSS?
type: support-article
updated_at: '2026-01-21T20:12:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37839579944599-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA340-%C3%89-poss%C3%ADvel-realizar-compensa%C3%A7%C3%A3o-de-uma-devolu%C3%A7%C3%A3o-do-tipo-NDF-com-o-tipo-INS-impostos-de-INSS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37839532294423) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
FINA340 É possível realizar compensação de uma devolução do tipo:NDF com o tipo:INS impostos de INSS?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
No processo de entrada de mercadorias via módulo Compras (SIGACOM), a nota fiscal de 10 mil gerou uma divisão de títulos no Financeiro (SIGAFIN) devido às configurações de retenção de impostos (INSS).

Título Principal (**NF**): **R$ 8.900,00** (Valor líquido após retenções).

Título de Imposto (**INS**): **R$ 1.100,00** (Valor retido na fonte).

Total da Nota de Entrada: R$ 10.000,00.

Após o cancelamento da compra, foi gerada uma Nota Fiscal de Devolução pelo módulo de Faturamento (SIGAFAT), que originou uma Nota de Crédito ao Fornecedor (**NDF**) no valor total de **R$ 10.000,00.**

**FINA340 - Compensação Contas a Pagar**

1. A compensação entre **NF** (R$ 8.900,00) e **NDF** (R$ 10.000,00) foi realizada com sucesso.
2. Restou um saldo residual na **NDF** de **R$ 1.100,00**.
3. O sistema **não permite** a compensação desse saldo da NDF contra o título de imposto (**INS**), mantendo ambos em aberto no Contas a Pagar, por terem naturezas distintas

4. O objetivo da **NDF** na compensação é fazer a contra partida do documento de entrada (**NF**), existem algumas exceções, mas esse é o objetivo principal.  O **INS** deve ser compensado com **INA** tipo gerado no PA. (**DFINCOM-7240**)

**Sugestão**:

1) Na rotina "FINA080 - Baixas a pagar" poderá utilizar o motivo de baixa **DACAO** para eliminar os saldo dos registros, sem que faça a movimentação bancária .

2) Poderá utilizar o ponto de entrada [F340FCPTOP](https://tdn.totvs.com/pages/viewpage.action?pageId=274328751). para inserir o tipo de título INS no momento da compensação

Segue um exemplo utilizando o P.E.

```
#Include "Protheus.ch"
User Function F340FCPTOP()

Local cCondicao := ParamIXB[1]
   cCondicao := IncluiTipoINS(cCondicao)
Return cCondicao

//------------------------------------------------------------

Static Function IncluiTipoINS(cQuery)
Local cUpper := Upper(cQuery)

// Remove INS de NOT IN
cUpper := StrTran(cUpper, "'INS',", "")
cUpper := StrTran(cUpper, ",'INS'", "")
cUpper := StrTran(cUpper, "'INS'", "")

Return cUpper
```

**Saiba mais:**  
[**DT F340FCPTOP Cria filtro na rotina de compensação cp**](https://tdn.totvs.com/pages/releaseview.action?pageId=274328751)

[**Cria filtro na rotina de compensação contas a pagar**](https://tdn.totvs.com/pages/viewpage.action?pageId=274328751)  
[**SIGAFIN - FINA340 - Compensação de títulos TX (ISS) x PA**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038887293-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA340-Compensa%C3%A7%C3%A3o-de-t%C3%ADtulos-TX-ISS-x-PA)
