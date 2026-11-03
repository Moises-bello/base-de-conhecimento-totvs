---
content_hash: be04cb9af9f18ee9a8459c74694ab9ae86fdb431fa3bbe89cabca8451a0ffcfb
fetched_at: '2026-06-29T00:05:48.209564+00:00'
page_id: '1024333187'
product: rm
source: tdn-rm
title: DT - S-1200 - Atribuição do lançamento do autônomo no CNO da obra própria
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1024333187
version: 13
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-1200 - Atribuição do lançamento do autônomo no CNO da obra própria |
| Pais: | Brasil |
| Issue: | [DRHROTRM-13268](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13268) |

## **02. LIBERAÇÃO**

  Lembrando que, será a partir dos patches:

* 12.1.2502.278
* 12.1.2506.243
* 12.1.2510.167 e superiores

## **03. SITUAÇÃO/REQUISITO**

Tratar a alocação do serviço prestado por um autônomo (cliente/fornecedor) no produto TOTVS Gestão Financeira, de forma que o recolhimento do INSS seja vinculado ao CNO (Cadastro Nacional de Obras) da obra própria, garantindo o envio adequado das informações ao eSocial.

## **04. SOLUÇÃO**

Implementada tratativa para que, na geração do XML do evento S-1200 do autônomo, o sistema passe a considerar o campo **CNO do tomador**, informado no cadastro do cliente/fornecedor, aba **“Integração Folha”**.

**Exemplo:**

1) Acesse o menu Administração de Pessoal | Cliente/Fornecedor | Anexos | Lançamentos, edite o lançamento desejado, acesse a aba **Integração Folha** e vincule o cliente/fornecedor ao **CEI da obra** correspondente.

Nesta tela, devem ser alocados somente CNOs vinculados a obras próprias.IMPORTANTE!

**2)**Ao gerar o XML do evento **S-1200**, será considerado o **CNO vinculado na aba Integração Folha**.

## **05. DEMAIS INFORMAÇÕES**
