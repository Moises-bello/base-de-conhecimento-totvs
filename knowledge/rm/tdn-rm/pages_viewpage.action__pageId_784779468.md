---
content_hash: 4dbe15c455299827c171935659469a03f0ace8984e42947b8e368176fab26487
fetched_at: '2026-06-29T00:11:38.785117+00:00'
page_id: '784779468'
product: rm
source: tdn-rm
title: Valor Dedução do Rendimento Tributável
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=784779468
version: 6
---

**CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Valor Dedução do Rendimento Tributável**

1. **Principais Campos e Parâmetros**

5. **Tabelas utilizada**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2302.144
* 12.1.2306.140
* e Superiores

## **02.** **VISÃO GERAL**

Este anexo contém informações dos valores dedutíveis do rendimento tributável por dependente. Dados que irão ser utilizados no envio do evento **S-1210** do **eSocial**.

Será discriminado mensalmente os dados do dependente que foram utilizados no cálculo do Imposto de Renda Retido na Fonte (IRRF), incluindo o valor utilizado para a dedução.

No momento do cálculo de folha, férias e 13º salário quando o dependente incidir em IRRF, dentro das condições legais, os valores serão inseridos neste anexo.

**Observação:**

**01 -** Quando for selecionado a inclusão de um registro utilizando o **Tipo 3 - Férias** , será necessário a inclusão da **Dt. Vencto Férias** e **Dt. Pagto.  Férias.**

**02 -** Para o IRRF de participação nos lucros não serão inseridos dados no anexo. Para usuários do parâmetro “Deduz valor por dependente na base de IRRF PL” marcado será emitido mensagem conforme TDN - [Parâmetros de Cálculo 2/2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=561848185) - 

**03** - Para acessar essa nova funcionalidade, deve-se permitir o acesso ao menu **[01.01.01.01] Valor Dedução do Rendimento Tributáve**l no perfil de segurança em serviços globais. 

## **03.** **EXEMPLO DE UTILIZAÇÃO**

Veja exemplos detalhados em:

[Alterações do Cálculo Para O Esocial Atender A Substituição Da Dirf - Valor Dedução do Rendimento Tributável no Cadastro de Dependentes](https://tdn.totvs.com/pages/viewpage.action?pageId=786553670)

## **04.** **TELA Valor Dedução do Rendimento Tributável**

 **Principais Campos e Parâmetros**

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Ano de Competência | Ano competência a que o registro se refere |
| Mês de Competência | Mês competência a que o registro se refere |
| Período | Período a que o registro se refere |
| Ano Caixa | Ano Caixa a que o registro se refere |
| Mês Caixa | Mês Caixa a que o registro se refere |
| Tipo de Movimento | Tipo de movimento deste registro, indica se é um registro referente a Folha de pagamento, 13° Salário, Férias ou Férias Rescisão |
| Valor | Valor do rendimento tributável |
| Dt. Vencto Férias | Caso o registro seja do tipo 3 - Férias, esse campo deve ser preenchido com a data de vencimento das férias do funcionário |
| Data Pagto. Férias | Caso o registro seja do tipo 3 - Férias, esse campo deve ser preenchido com a data de pagamento das férias do funcionário |

**Tela - Valor Dedução do Rendimento Tributável**

## **05.** **TABELAS UTILIZADAS**

* PFDEPEND
* PFDEPIRRFDED
