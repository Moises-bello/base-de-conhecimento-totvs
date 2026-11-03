---
content_hash: bbfb2677ddde40ce6c2033004db5356ffd4ce89eefcf21d95a0cb7ecc34095f4
fetched_at: '2026-06-29T00:10:53.023124+00:00'
page_id: '574380610'
product: rm
source: tdn-rm
title: Validações TISS - MatMed
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=574380610
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

As seguintes validações são referentes a Guias Tiss para MatMeds:

- Verifica se existe registro na Tabela de Material e Medicamento Usada para o código TISS, se não houver, dar alerta com a mensagem: “Existem tabelas de MAT/MED sem a referência na ANS.”

**-** Se padrão faturamento codificação for "CBHPM 5ª EDIÇÃO + Assefaz - DTS - " e Tipo de Paciente for interno, verificar:

  Se houver SADT e houver Numero de guia, retornar erro “MATMED X esta com referência a guia de exame X. Data XX/XX/XXXX. Desmarque ou digite o exame realizado no paciente na pagina Diagnose e Terapia.”

- Se não tiver esses valores, validar se existem registros na tabela de Correlação de Unidade de Medida com parâmetros Versão Tiss e Unidade de Faturamento , se não houver registros, retornar mensagem “Unidade de medida X informada no lançamento X não esta relacionado a nenhuma definida na versão X do padrão TISS - ANS.”

## **02. EXEMPLO DE UTILIZAÇÃO**

**Passo 1: Escolher registro que possua MatMed.**

**Passo 2: Executar o processo de encerramento de conta**

**Passo 3: Verificar mensagens de erro no log do encerramento da conta.**

## **03. TABELAS UTILIZADAS**

* SZATENDMATMED
* SZATENDIMENTO
* SZTABMATMED
* SZANSUNDCORRELA

]]>
