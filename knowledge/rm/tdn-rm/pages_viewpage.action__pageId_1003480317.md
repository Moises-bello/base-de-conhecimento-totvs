---
content_hash: a540667d33ca2683e9ba631a8ed3a8d1db1692d992699ef98195292c6fee3c8f
fetched_at: '2026-06-29T00:05:45.097248+00:00'
page_id: '1003480317'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - Tratativa para Transferido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1003480317
version: 19
---

## **01. DA DOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Integração RM X Ahgora - Tratativa para Transferido |
| Issue: | [DRHROTRM-15297](https://jiraproducao.totvs.com.br/browse/DRHROTRM-15297) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2502.218
* 12.1.2506.166
* 12.1.2510.100 e superiores

## **03. SITUAÇÃO/REQUISITO**

Atualmente, quando um funcionário é transferido entre filiais ou coligadas, o sistema **TOTVS Folha de Pagamento** envia automaticamente a informação na tag <matricula\_anterior> para o **Ponto Web da Ahgora.**

No entanto, em cenários onde a coligada de origem não possui integração ativa, e a coligada de destino possui, ao integrar o funcionário na coligada de destino ocorre o seguinte erro: **“1 - O CPF informado é diferente do cadastrado para o funcionário no Pontoweb.”**

Esse problema ocorre porque o sistema tenta enviar a matrícula de origem (coligada A) mesmo sem integração ativa naquela coligada, ao integrar o funcionário na coligada B.

Além disso, o mesmo comportamento é observado quando o funcionário foi transferido antes do início da integração.

## **04. SOLUÇÃO**

Para viabilizar o preenchimento correto, foram criados os campos **CHAPAANTERIOR** e **CODCOLIGADAANTERIOR** na tabela **PINTEGRACAOENVIOAHGORA,** com isso a chapa de origem (matricula anterior) somente deve ser enviada quando a coligada da chapa de origem estiver com a integração ativa com a Ahgora e o funcionário correspondente já existir na base da Ahgora (ou seja, já estiver integrado).

#### **Regras:**

* Nos cenários de transferência entre coligadas, a tag `<matricula_anterior>` será preenchida quando:

  + A coligada de origem estiver com a integração **ativa**, e
  + A chapa anterior possuir status **Integrado**, ou seja, quando o campo **PINTEGRACAOENVIOAHGORA.STATUS = 1.**

#### **Cenário adicional:**

* Em um cenário onde o cliente já tenha integrado uma chapa A antes da atualização do patch mencionado no item "**02. Liberação**" onde criamos as novas colunas **CHAPAANTERIOR** e **CODCOLIGADAANTERIOR,** e após aplicar a atualização realize a transferência da chapa A para a chapa B, o sistema irá identificar que a chapa A não possui os novos campos preenchidos, mas já está integrada.

  + Nessa situação, o sistema ainda assim preencherá a tag `<matricula_anterior>` ao enviar a chapa B, considerando que a chapa A é a anterior e já se encontra integrada.
  + Foi implementado um tratamento específico para identificar esse cenário e garantir o correto preenchimento, evitando inconsistências durante o processo de transferência.

## **05. DEMAIS INFORMAÇÕES**

* [Integração RM X Ahgora](https://tdn.totvs.com/pages/viewpage.action?pageId=877866931)
