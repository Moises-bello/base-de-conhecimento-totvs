---
content_hash: 5146997c86f65e86c5532c660c1d1253f2048a7fb389a4b7434f11d3d0f3e780
fetched_at: '2026-06-29T00:10:21.769442+00:00'
page_id: '493634426'
product: rm
source: tdn-rm
title: FISCAL01-7772 DT Lançamento Fiscal - Inclusão de Conta Contábil Automático
  no Item do Lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493634426
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Cadastro de Lançamentos Fiscais |
| Requisito/Story/Issue (informe o requisito relacionado) : | FIS000062 |

## **02. SITUAÇÃO/REQUISITO**

Tratamento do Serviço de Inclusão de Lançamentos Fiscais para preenchimento automático do campo "Conta Contábil" no Item do Lançamento Fiscal.

A regra para preenchimento do campo é a mesma que está hoje na rotina da EFD Contribuições/Sped Fiscal:

1. Será considerado o Default Contábil informado no CFOP (Natureza de Operação) associado ao Lançamento Fiscal que possua a Classificação “SPED” informada.
2. Se não for encontrado um Default Contábil na CFOP, será selecionado o Default no Cadastro do Produto/Serviço que possua a Classificação “SPED” informada.
3. Não existindo Default Contábil no Cadastro do Produto/Serviço será utilizada a conta contábil informada no Cadastro – Produto - Dados Fiscais.

Demais regras:

* Contas cadastradas como Débito, serão para os lançamentos fiscais de entrada, e por sua vez, as contas cadastradas como Crédito serão para os lançamentos de saída.
* É necessário ter o campo Classificação da Conta preenchido com "SPED"(Em caixa ALTA) no Default Contábil.
* No carregamento do Default contábil será considerado o código da filial também e será priorizado o Default com a filial igual a filial do lançamento.
* Se tiver parametrizado filial no Default contábil com classificação "SPED" e está filial não é a mesma do lançamento a conta contábil será desconsiderada no item daquele lançamento.

## **03. SOLUÇÃO**

Foi implementado no Serviço de Inclusão do Lançamento Fiscal o preenchimento automático da conta contábil no Item.

* **Regra de Preenchimento na ordem abaixo**

1 - Será verificado se existe default contábil e que possua a classificação "SPED" no CFOP (Natureza de Operação) associado ao Lançamento Fiscal.

2 - Será verificado se existe default contábil no Cadastro do Produto/Serviço e que possua a classificação "SPED" informada.

3 - Não existindo Default Contábil no CFOP ou no Produto que atenda as regras acimas, será utilizada a conta contábil informada no Cadastro – Produto - Dados Fiscais se informado.

4 - Se não encontrado Conta Contábil o campo não será preenchido.

* **Observação**

1 - Contas cadastradas como Débito, serão para os lançamentos fiscais de entrada, e por sua vez, as contas cadastradas como Crédito serão para os lançamentos de saída.

2 - Se o Default Contábil estiver parametrizado com uma filial que não é a mesma filial do lançamento fiscal a mesma sera desconsiderada.

* **O preenchimento da conta contábil automático ocorrera quando:**

1 - Inclusão Manual do Lançamento fiscal quando incluído Item.  
2 - No processo de Escrituração e Importação (Web Service) quando não informado conta contábil no item.
