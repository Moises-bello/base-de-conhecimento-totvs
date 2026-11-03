---
content_hash: 034a953594ebd087e70557428db3a020ace07cd993863f22aa060c36f3384367
fetched_at: '2026-06-29T00:10:35.498312+00:00'
page_id: '529307744'
product: rm
source: tdn-rm
title: Gerar DMED
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+DMED
version: 8
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Pré-Requisitos**
3. **Exemplo de utilização**
4. **Passo a passo das telas utilizadas**
5. **Geração DMED**

## **01. VISÃO GERAL**

Essa funcionalidade consiste na produção de uma Declaração de Serviços Médicos e de Saúde pelo sistema que será enviado à Receita Federal. O arquivo gerado pelo sistema (dmed.txt) permite a visualização do log da geração, para avaliação pela receita federal.

O sistema também gera um resumo que contém os valores pagos no período.

## **02. PRÉ-REQUISITOS**

**RM Saúde integrando com "TOTVS Gestão de Estoque, Compras e Faturamento"**

É necessário configurar o tipo de movimento utilizado no RM Saúde para emissão de Notas Fiscais / Recibos, para isto,  acesse o **TOTVS Gestão de Estoque, Compras e Faturamento**

## **03. EXEMPLO DE UTILIZAÇÃO**

**Acesse:**

* TOTVS Gestão de Estoque, Compras e Faturamento, menu Ambiente > Parâmetros > Gestão Estoque, Compras e Faturamento.

## **04. PASSO A PASSO DAS TELAS UTILIZADAS**

Em seleção de processos, selecione o item referente ao processo de vendas e o seu sub item.

Dê um duplo clique no movimento utilizado no RM Saúde para emissão de Notas Fiscais / Recibos.

* TOTVS Gestão de Estoque, Compras e Faturamento integrando com o financeiro (TOTVS Gestão Financeira)
* Selecione o item Fin-Faturamento 1/6 e maque o *checkbox* Fatura o Movimento.

## **05. GERAÇÃO DMED**

1. No TOTVS Gestão Hospitalar acesse Utilitários/Rotinas/ Gerar DMED.
2. Selecione a unidade de faturamento para geração do arquivo. Os dados do arquivo serão correspondentes somente a esta unidade.
3. Preencha no campo Ano Referência o ano vigente e, no campo Ano Calendário, o ano referente ao arquivo que será gerado (normalmente é o ano anterior).
4. Marque a opção Retificadora somente se o arquivo a ser gerado for uma retificação a ser enviada a Receita Federal. Caso o arquivo seja retificação, informe o número do recibo a ser retificado.
5. Em seguida, preencha os dados de CPF, nome e telefone.
6. Para considerar somente valores baixados da Nota Fiscal, marque a caixa Considerar Valores baixados da NF.
7. Para considerar a geração da DMED para todas as unidades de faturamento, marcar a opção Gerar arquivo para todas as unidades de faturamento.
8. Deve-se informar o local onde o arquivo DMED será salvo
9. Clique em Executar.

**Opções > parâmetros > Integração RM nucleus**

* Realize o caminho  e acesse a aba tipo de mov. DMED
* Para gerar o DMED, os tipos de movimentos utilizados devem estar setados na tela abaixo.
