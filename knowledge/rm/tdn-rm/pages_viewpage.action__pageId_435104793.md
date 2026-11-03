---
content_hash: d075660d8019535a8ac6af08380559206b0bbf4ab63a0970f5d9f559eac6c5dc
fetched_at: '2026-06-29T00:09:46.443852+00:00'
page_id: '435104793'
product: rm
source: tdn-rm
title: Incluindo as Fórmulas para Cálculo de Juros, Multa e Desconto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104793
version: 3
---

**Incluindo as Fórmulas para Cálculo de Juros, Multa e Desconto**  
**Passo 1** - Acesse: TOTVS Serviços Globais/ Administração/ Fórmulas   
**Passo 2** - Selecione o Contexto do sistema de Gestão Financeira e clique em Incluir Fórmula.   
**Passo 3** - Informe o Código e Título.   
**Passo 4** - Selecione "Fórmula RM" no radioButton \[Linguagem\].  
**Passo 5** - Preencha a fórmula de acordo com sua finalidade e clique em Salvar. Os valores básicos para os cálculos são :

* **Juros:** (VALORCAMPOLANCAMENTOGERADOR('VALORJUROSBX') \* (VALORCAMPOLANCAMENTOREPASSE('PERCENTJUROS')/100)) \* (VALORCAMPOLANCAMENTOREPASSE('PERCENTUAL')/100)

* **Multa:** (VALORCAMPOLANCAMENTOGERADOR('VALORMULTABX') \* (VALORCAMPOLANCAMENTOREPASSE('PERCENTMULTA')/100)) \* (VALORCAMPOLANCAMENTOREPASSE('PERCENTUAL')/100)
* **Desconto:** (VALORCAMPOLANCAMENTOGERADOR('VALORDESCONTOBX') \* (VALORCAMPOLANCAMENTOREPASSE('PERCENTDESCONTO')/100)) \* (VALORCAMPOLANCAMENTOREPASSE('PERCENTUAL')/100)

**Observação: As 3 fórmulas devem ser inseridas no sistema, pois serão vinculadas ao Tipo de Documento de Repasse Condicional.**  
    
 Voltar
