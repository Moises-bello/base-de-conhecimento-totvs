---
content_hash: 0e847db9c30f321adcabe6fd7b08cfd4a906f9c55ed8a036d246401368c0988a
fetched_at: '2026-06-29T00:11:57.014402+00:00'
page_id: '874201500'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - Disponibilização do campo "Utiliza Ponto Ahgora"
  e do "Histórico Utiliza Ponto Ahgora"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=874201500
version: 7
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM X Ahgora - Disponibilização do campo "Utiliza Ponto Ahgora" e do "Histórico Utiliza Ponto Ahgora" |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11539](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11539) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.249
* 12.1.2406.187
* 12.1.2410.120 e superiores

## **03. SITUAÇÃO/REQUISITO**

Criação de um campo no sistema para identificar se o funcionário bate ponto no produto Ponto Web da Ahgora, incluindo também o histórico desse campo, para garantir o correto rastreamento e identificação das alterações realizadas.

## **04. SOLUÇÃO**

Foi criada uma nova aba denominada "Ahgora" no cadastro de funcionário, que será habilitada quando, em **Configurações | Parametrizador | Integrações | Ahgora**, a integração estiver ativa.

**Passo 1** - Verifique se a integração está ativa em Configurações | Parametrizador | Integrações | Ahgora.

**Passo 2** - Acesse Administração de Pessoal | Funcionários | Submenu Registros, será apresentada a nova aba "**Ahgora**", onde você poderá marcar a opção de utilização de ponto.

**Passo 3** - Acesse o menu Serviços Globais | Segurança | Perfis, e conceda permissão para acesso ao histórico do campo "**Ahgora**".

**Passo 4** - Acesse Administração de Pessoal | Funcionários | Anexos | Históricos | Histórico Utiliza Ponto Ahgora, para vusualizar o histórico cadastrado para o campo de utilização do Ponto Web Ahgora.

## **05. DEMAIS INFORMAÇÕES**

[Informações Contratuais](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719370)

[Histórico Utiliza Ponto Ahgora](https://tdn.totvs.com.br/pages/viewpage.action?pageId=874201514)
