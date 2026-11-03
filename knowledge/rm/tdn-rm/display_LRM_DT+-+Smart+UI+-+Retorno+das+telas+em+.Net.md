---
content_hash: 176333f7b6b8d565bf648b20b17dfaf7974f53065a746dee5f2f8ddbd754795e
fetched_at: '2026-06-29T00:12:16.530799+00:00'
page_id: '993697963'
product: rm
source: tdn-rm
title: DT - Smart UI - Retorno das telas em .Net
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Smart+UI+-+Retorno+das+telas+em+.Net
version: 10
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Smart UI - Retorno das telas em .Net |
| Issue: | [DRHROTRM-14989](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14989)  [DRHCALCRM-9832](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-9832) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2502.215
* 12.1.2506.164
* 12.1.2510.100 e superiores

## **03. SITUAÇÃO/REQUISITO**

Em função de uma limitação funcional, identificamos a necessidade de retornar com as telas antigas .Net no menu da Folha de Pagamento, garantindo a continuidade dos processos e atendendo às demandas dos usuários que necessitam das funcionalidades completas.

## **04. SOLUÇÃO**

As telas que foram migradas para Smart UI agora poderão ser acessadas também em .Net. O usuário poderá optar por qual tela utilizar. Foi criado uma tag de segurança diferenciada para tratamento adequado do menu.

As telas envolvidas são:

* Rateio Fixo
* Histórico Salarial
* Registro Preliminar
* Situação atual
* Histórico de Provisão
* Histórico de Encargos
* Cadastro de Encargo
* Consulta Movimento Passivo Trabalhista
* Dados do Dissídio
* Gerenciador do Log de Cálculo
* Linha de Vale Transporte
* Múltiplos Vínculos que precisa de Recálculo
* Parametrização dos Lançamentos Financeiro
* Tarifas de Vale Transporte

**Exemplo:**

  Na tela de segurança abaixo podemos observar dois menus de **Registro Preliminar**. O usuário poderá dar permissão no menu que ele desejar utilizar.

## **05. DEMAIS INFORMAÇÕES**
