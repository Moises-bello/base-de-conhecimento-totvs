---
content_hash: 0a14708e702ab2bd57c2c3e982ab708ced1423b8197d54bf158f1c6c67200fda
fetched_at: '2026-06-29T00:09:33.290422+00:00'
page_id: '425458956'
product: rm
source: tdn-rm
title: TOTVS Incorporação x BackOffice Protheus - Gerar Lançamentos Contábeis - Apuração
  do POC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458956
version: 2
---

**TOTVS Incorporação x BackOffice Protheus - Gerar Lançamentos Contábeis - Apuração do POC**

Foi evoluída a integração TIN x Protheus para atender a demanda de realizar a Apuração de resultados (POC) integrado. Foi ajustado no adapter "**AccountingEntry**" (criada a versão 2.001) para que sejam trafegados os dados de rateio gerencial (plano de contas gerencial), viabilizando assim a integração dos lançamentos contábeis a partir do módulo de apuração de POC do TOTVS Incorporação.

Após realizar a Apuração do POC, o TOTVS Incorporação possibilita o envio da **Contabilização da Apuração** realizada e também o seu **Estorno/Exclusão** para o Protheus. Com isso, será gerada a mensagem **AccountingEntry**.   
 Processos que geram Lançamentos Contábeis para o Protheus:

TOTVS Incorporação -> Apuração de Resultado Contábil pelo POC -> Regras de Apuração -> Contabilização das Apurações Realizadas

TOTVS Incorporação -> Apuração de Resultado Contábil pelo POC -> Regras de Apuração -> Estornar/Excluir Contabilização

É possível ver os detalhes da mensagem enviada em Integração / Integração / Mensagem Única / Fila de Mensagens Únicas. Esta tela mostra os campos: Identificador da transação, Uuid mensagem, Versão de Mensagem, Criação da mensagem e Identificador da Integração. Esta tela ainda possui um anexo que mostra as Informações de execução da mensagem.
