---
content_hash: 0744652cdde4a60650da24cbb7126c9067dd74773fe529cf003339aa75bbe090
fetched_at: '2026-06-29T00:12:15.104414+00:00'
page_id: '969994406'
product: rm
source: tdn-rm
title: DT - Importação e Exportação - Remoção de campos não utilizados nas tabelas
  de Sindicato e Função
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=969994406
version: 15
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Importação e Exportação - Remoção de campos não utilizados nas tabelas de Sindicato e Função |
| Issue: | [DRHROTRM-14445](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14445) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2410.276
* 12.1.2502.180
* 12.1.2506.122 e superiores

## **03. SITUAÇÃO/REQUISITO**

Realizar a atualização dos processos de importação e exportação, com a remoção dos campos não utilizados das seguintes tabelas:

* **PFUNCAO.JORNADAREF** (Função)
* **PSINDIC.DIASDEEXPERIENCIA** (Sindicato)

## **04. SOLUÇÃO**

Visando otimizar os processos e manter as integrações alinhadas com os campos efetivamente utilizados no sistema, realizamos uma tratativa nos processos de **importação e exportação** das tabelas **Função** e **Sindicato**, com a **remoção dos campos PFUNCAO.JORNADAREF e PSINDIC.DIASDEEXPERIENCIA**, que não são mais utilizados.

IMPORTANTE:

Após a atualização dos patches mencionados no item 02, torna-se obrigatório importar os leiautes atualizados para evitar erros. Os leiautes são:

* FOPLAY0042 09.004.008 Exportação de Sindicato.TotvsGen
* FOPLAY0042 09.004.011 Exportação de Funções.TotvsGen

## **05. DOCUMENTAÇÃO**

         [Layout do Cadastro de Função](https://tdn.totvs.com/pages/viewpage.action?pageId=452719348)

[Layout do Cadastro de Sindicato](https://tdn.totvs.com/pages/releaseview.action?pageId=452719311)
