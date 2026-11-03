---
content_hash: 71c03ead93cf67be3c2795732452bcbe7a50e3e570e93316c2bc5e313c3d2363
fetched_at: '2026-06-29T00:12:09.005052+00:00'
page_id: '938311837'
product: rm
source: tdn-rm
title: Eventos Crédito do Trabalhador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=938311837
version: 5
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Eventos Crédito do Trabalhador**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Mesmo comportamento do anexo do cadastro de funcionários, apenas será considerado para todos os funcionários caso seja inserido eventos no parametrizador. [Eventos Remuneração Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=938311818).

IMPORTANTE:

**Eventos cadastrados aqui serão considerados para todos os funcionários no cálculo da folha ou da rescisão.**

O cálculo da margem consignável do funcionário será sobre o somatório de todas as rubricas de vencimento e descontos com incidência previdenciária subtraindo o desconto de INSS e IRRF, mas o usuário poderá informar quais eventos quer considerar para a margem consignável do desconto do empréstimo da modalidade "Crédito do Trabalhador eSocial" usando esse anexo "[Eventos Remuneração Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=938311818)" do cadastro de funcionários ou o "Eventos do Crédito do Trabalhador" em folha normal no parametrizador.

**ATENÇÃO: Os eventos inseridos nesses cadastros têm prioridade sobre o líquido do movimento, por exemplo, se inserir o evento de dias trabalhados no** **[Eventos do Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311837)** **em folha normal no parametrizador então em todos os funcionários que tiverem o empréstimo da modalidade "Crédito do Trabalhador eSocial" será considerado na base consignável como dias trabalhados menos INSS e IRRF.**

## **02. EXEMPLO DE UTILIZAÇÃO**

FAQ - [Medida Provisória Nº 1.292, de 12 de Março de 2025 - Crédito do Trabalhador - Linha RM](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)

## **03.** **TELA Eventos Crédito do Trabalhador**

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
