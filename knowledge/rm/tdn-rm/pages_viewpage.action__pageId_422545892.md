---
content_hash: c53cf36d2fe097cfd63b52c0250f97f716831118ce41b1cee96b80ca724b1441
fetched_at: '2026-06-29T00:09:21.744516+00:00'
page_id: '422545892'
product: rm
source: tdn-rm
title: Apuração IRPJ e CSLL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545892
version: 34
---

# Conteúdo

**Regime Lucro Presumido com Presunção nonefalse**

# 1. Introdução

O cálculo de tributos como IRPJ e CSLL tem como base dados contábeis processados conforme regras pré-definidas nos **Eventos Tributários**. Essas regras determinam como as obrigações tributárias são calculadas e reportadas em cada **Período de Apuração**.

# 2. Regras para Cálculo dos Tributos

## 2.1. Encerramento do Período de Apuração

* Para calcular o **Débito/Crédito** de um tributo em um período:

  1. Selecione o **Período de Apuração** desejado.
  2. Encerre o período no sistema.
  + - O sistema preencherá automaticamente os campos (como base de cálculo, alíquotas e créditos) com base nos **Eventos Tributários vinculados**.

## 2.2. Fontes de Dados para o Cálculo

* **Parâmetros do Cadastro de Tributos**:

  + Os campos **Alíquota**, **Alíquota Adicional**, **Valor Parcela Isenta**, **%Serviços**, **%Vendas** e **%Compensação** são extraídos diretamente do cadastro de tributos.
* **Regras dos Eventos Tributários**:

  + O sistema identifica o **Evento Tributário** aplicável pelo cadastro de **Vigência Eventos Tributários**. A validade é determinada pelas datas inicial e final do Período de Apuração e pelo tributo associado.
* **Integração Contábil**:

  + Apenas **Lançamentos Contábeis integrados ao Lote Zero** são considerados no cálculo.

## 2.3. Consolidação entre Filiais

* Os cálculos são realizados de forma **consolidada** na filial matriz, agregando dados de todas as filiais, com exceção das Filiais SCP.

## 2.4. Unicidade das Regras

* Cada **Período de Apuração** deve ter **uma única regra tributária** aplicável. Regras duplicadas para o mesmo período não são permitidas.

# 3. Procedimentos Específicos por Tributo

## 3.1. IRPJ e CSLL

* **Anexo "Detalhamento da Apuração"**:
  + Ao encerrar o período, o sistema exibe um detalhamento dos valores que compõem a apuração, permitindo maior transparência ao usuário.

# 4. Responsabilidades do Usuário

* **Parametrização**: O contribuinte deve configurar o sistema conforme suas obrigações legais.
* **Validação**: Garantir que não existam regras duplicadas para períodos sobrepostos.

# 5. Resumo

* O cálculo tributário depende da correta configuração de:

  + **Cadastros de tributos** (alíquotas, percentuais).
  + **Eventos Tributários** (validade, regras).
* O encerramento do Período de Apuração aciona o preenchimento automático dos valores, com base em dados contábeis consolidados e regras definidas.
* Para mais informações consulte a documentação sobre as .

# 6. Documentações relacionadas
