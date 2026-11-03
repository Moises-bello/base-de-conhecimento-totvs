---
content_hash: 1f1dd09eec94122250ab11357a3b82c4a7797cf773ed0688f0a02fa3e949bd73
fetched_at: '2026-06-29T00:12:09.000785+00:00'
page_id: '938311818'
product: rm
source: tdn-rm
title: Eventos Remuneração Crédito do Trabalhador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=938311818
version: 4
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Eventos Remuneração Crédito do Trabalhador**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O cálculo da margem consignável do funcionário será sobre o líquido do movimento, ou seja, todos os proventos menos os descontos, mas o usuário poderá informar quais eventos quer considerar para a margem consignável do desconto do empréstimo da modalidade "Crédito do Trabalhador eSocial".

Nesse anexo somente será permitido cadastrar eventos de provento e desconto exceto desconto de INSS, IRRF e os eventos adiantamento provento e desconto considerados obrigatórios.

No "código de cálculo 482 - Remuneração Base Empréstimo Crédito do Trabalhador" será lançado o valor da Remuneração considerada para o desconto do empréstimo.

Caso o usuário não informe eventos nestes cadastros "Eventos Remuneração Crédito do trabalhador" (anexo funcionário e parametrizador), será considerado o líquido da Folha. 

IMPORTANTE:

O cálculo da margem consignável do funcionário será sobre o somatório de todas as rubricas de vencimento e descontos com incidência previdenciária subtraindo o desconto de INSS e IRRF, mas o usuário poderá informar quais eventos quer considerar para a margem consignável do desconto do empréstimo da modalidade "Crédito do Trabalhador eSocial" usando esse anexo "Eventos Remuneração Crédito do Trabalhador" do cadastro de funcionários ou o [Eventos do Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311837) em folha normal no parametrizador.

**ATENÇÃO: Os eventos inseridos nesses cadastros têm prioridade sobre o líquido do movimento, por exemplo, se inserir o evento de dias trabalhados no** **[Eventos do Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311837)** **em folha normal no parametrizador então em todos os funcionários que tiverem o empréstimo da modalidade "Crédito do Trabalhador eSocial" será considerado na base consignável como dias trabalhados menos INSS e IRRF.**

## **02. EXEMPLO DE UTILIZAÇÃO**

FAQ -

## **03.****TELA Eventos Remuneração Crédito do Trabalhador**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Cód. Evento | Código do evento |

## **04. TABELAS UTILIZADAS**

* PFEMPRT
* PFDESCEMPRT
* PGRPLANC
* PREMCREDTRAB
* PFREMCREDTRAB
