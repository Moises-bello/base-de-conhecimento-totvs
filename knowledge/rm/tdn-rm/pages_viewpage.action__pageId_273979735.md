---
content_hash: a905cfde87aaf9b2c57d19314cde7b782fa9daef5ce831f1de92a2ecebf997ca
fetched_at: '2026-06-29T00:08:31.981367+00:00'
page_id: '273979735'
product: rm
source: tdn-rm
title: ER FINANCEIRO01-43 Geração de Nosso Número e de Código de Barra Banco ABC Brasil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273979735
version: 5
---

# Geração de Nosso Número e de Código de Barra

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| **Segmento Executor:** | Construção e Projetos | | |
| **Módulo:** | Gestão Financeira | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Geração de Nosso Número | Geração de Nosso Número | | Geração de Código de Barra | Geração de Código de Barra | | | |
| **Requisito/Story/Issue:** | FINANCEIRO01-41;FINANCEIRO01-42; | | |
| **País:** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro | | |

  

---

## Objetivo

Este documento visa demonstrar, de acordo com a liberação do documento “Especificações Técnicas para Confecção de Boletos de Cobrança do Nosso Banco – Versão 1 - Autbank” de 14/10/2013, o tratamento de geração de nosso número e código de barra para o Banco ABC Brasil (- 246).

  

---

## Definição da Regra de Negócio

## **Nosso Número**

A montagem do nosso número para o Banco ABC Brasil é definido como **NNNNNNNNNND**, onde

* **NNNNNNNNNN** é o nosso número base calculado a partir do “Tipo de Nosso Número” definido no convênio.
* **D** é o dígito verificador calculado. Digito verificador é calculado (Módulo 10) pelo seguinte formato **AAAACCCNNNNNNNNNN**, onde

   -  **AAAA** é o número da agência sem dígito verificador definido no convênio.

   -  **CCC** é o código da carteira definido no convênio.

   -  **NNNNNNNNNN** é o nosso número base calculado a partir do “Tipo de Nosso Número” definido no convênio.

A regra do calculo do dígito verificador é basicamente multiplicar cada algarismo do número formado pela composição dos campos acima pela sequência de multiplicadores 2,1,2,1,2,1,2 (posicionados da direita para a esquerda). Se a a multiplicação resultar > 9 (por exemplo = 12), soma os dígitos (1 + 2). A seguir, somam-se os algarismos dos produtos e o total obtido é dividido por 10. O DV é a diferença entre o divisor (10) e o resto da divisão: 10 - (RESTO DA DIVISAO) = DV. Se o resto da divisão for zero, o DV é zero.

**Processamento de Geração do Nosso Número**

Montagem do nosso número base depende do valor do tipo de nosso número.

* **Tipo de nosso número**

Informado no convênio utilizado pelo banco, define o modo como será gerado o nosso número

* **Boleto**

A referência do boleto será a base do nosso número gerado. Caso o lançamento não esteja vinculado a um boleto, será exibida a mensagem “O Lançamento não possui Boleto vinculado, portanto não é possível gerar Nosso Número através do Boleto. Utilize outro modo de geração do Nosso Número ou gere Boleto no Lançamento”.

* **Sequencial**

Número sequencial, pertencente a faixa do limite inferir e limite superior, será a base do nosso número. Se o número sequencial for maior que o limite superior, o limite inferior será considerado como o próximo número sequencial. Quando o número sequencial gerado estiver fora da faixa definida no convênio (limite inferior e limite superior), será exibida a seguinte mensagem “O número sequencial não está dentro da faixa para geração do nosso número. Por favor, verificar cadastro de convênio”.

* **Geração Banco**

Base do nosso número é gerada pelo banco.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| FIN000023 – Geração de Nosso Número | Envolvida | Gestão Financeira -> Contas a Pagar / Receber -> Lançamentos -> Processos -> Boleto -> Inclusão de Boleto | - |

## **Código de Barra**

Segundo o documento “Especificações Técnicas para Confecção de Boletos de Cobrança do Nosso Banco – Versão 1 - Autbank” de 14/10/2013, o código de barras para o Banco ABC Brasil deverá ser definido da seguinte forma:

* Posição 1 à 3: Identificação do banco (sem DV)
* Posição 4: Código moeda (9 – Real)
* Posição 5: Dígito verificador do código de barras (DV)
* Posição 6 à 9: Fator de vencimento
* Posição 10 à 19: Valor nominal do título
* Posição 20 à 44: Campo livre

As regras de formatação do campo livre nas posições 20 a 44. Campo livre formatado da seguinte maneira **AAAACCCOOOOOOONNNNNNNNNND**, onde

* **AAAA** é o número da agência sem o digito verificador definido no cadastro da conta caixa utilizada pelo convênio.
* **CCC** é o número da carteira definido pelo convênio.
* **OOOOOOO** é o número da operação definido pelo convênio (número do contrato da operação de crédito).
* **NNNNNNNNNN** é o nosso número definido pelo convênio.
* **D** é o primeiro dígito verificador calculado a partir do nosso número. O dígito verificador depende do número da agência, número da carteira e o nosso número base.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| FIN000024 – Geração de Código de Barras | Envolvida | Gestão Financeira -> Contas a Pagar / Receber -> Boleto -> Processos -> Processo de geração de código de barras | - |
