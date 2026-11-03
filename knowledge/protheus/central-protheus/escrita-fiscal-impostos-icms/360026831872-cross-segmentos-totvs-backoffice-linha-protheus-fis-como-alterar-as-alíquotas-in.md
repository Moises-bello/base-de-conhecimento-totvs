---
article_id: 360026831872
category: Escrita Fiscal - Impostos - ICMS
content_hash: 0b40d5703fa52af75c989427381842eec8e7154741217b6feb926bed36b66fa4
fetched_at: '2026-06-28T22:39:24.145640+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como alterar as Alíquotas
  Internas ICMS e a do ICMS ST e ICMS complementar
type: support-article
updated_at: '2024-01-18T13:39:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026831872-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-alterar-as-Al%C3%ADquotas-Internas-ICMS-e-a-do-ICMS-ST-e-ICMS-complementar
---

**Dúvida**

Como alterar a alíquota interna do ICMS e aliquota ICMS ST e ICMS Complementar?   
  
**Ambiente**

Protheus – Livros Fiscais– Todas Versões  
  
**Solução**

Para uma operação interna ou seja Origem e Destino dentro do mesmo estado.  
O sistema tem esta validação:

Parâmetro MV\_ICMPAD

Caso tenha uma aliquota a ser tratada diferente do parametro utilizar Exceção Fiscal no campo Aliq Interna ou do cadastro produto Aliquota de ICMS.

Qual a regra e nível  da validação da aliquota ICMS interna no Protheus

1º) O sistema vai validar a alíquota de ICMS da sua exceção fiscal no campo Aliq interna.  
2º) Caso não tenha exceção fiscal, então o sistema vai validar a alíquota de ICMS do cadastro de produto.  
3º) Caso não tenha alíquota no cadastro de exceção fiscal e no cadastro de produto, os sistema vai validar o cadastro do parametro MV\_ICMPAD

Agora para a alíquota do ICMS RETIDO e ICMS COMPLEMENTAR.

Quando a operação é interestadual e tem ICMS RETIDO ou ICMS Complementar será validado Exceção Fiscal ou UF x UF ou MV\_ESTICM

Primeiro será validado se existe informação na sua Exceção Fiscal (MATA540) no campo Al.ICM.Dest ou na rotina UFxUF (FISA080) no campo Al.ICM.Dest

Na ausência de aliquota na Exceção Fiscal (MATA540) no campo Al.ICM.Dest ou na rotina UFxUF (FISA080) no campo Al.ICM.Dest será validado o parametro MV\_ESTICM.

Segue documentação do parametro MV\_ESTICM

CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o parâmetro MV\_ESTICM?

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028735071-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-par%C3%A2metro-MV-ESTICM->
