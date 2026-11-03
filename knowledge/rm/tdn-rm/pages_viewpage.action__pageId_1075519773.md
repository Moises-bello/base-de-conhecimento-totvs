---
content_hash: aa240f3471ef34db8b4db2909af0d600f4f6058ecf8207772ee188af31d52bc1
fetched_at: '2026-06-29T00:05:54.137920+00:00'
page_id: '1075519773'
product: rm
source: tdn-rm
title: DT - Integração RM X Quírons - Tratativa da 'Data de Continuidade'  do Histórico
  de Afastamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1075519773
version: 8
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Integração RM X Quírons - Tratativa da 'Data de Continuidade' do Histórico de Afastamento |
| País: | Brasil |
| Épico: | [DRHROTRM-11373](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11373) |

## **02. VERSÃO**

* 12.1.2506.324
* 12.1.2510.254
* 12.1.2602.169 e Superiores

## **03. S****ITUAÇÃO/REQUISITO**

Permitir que a Quírons envie a informação da **Data de Continuidade de Afastamento** através da API **"leaveofabsencecontrol"**,  para que essa informação seja gravada automaticamente no cadastro de **Histórico de Afastamento** da Folha de Pagamento RM.

## **04.****SOLUÇÃO**

Implementado o recebimento da informação de **Data de Continuidade de Afastamento** enviada pela tag **sequence** da API **leaveofabsencecontrol**.

O preenchimento dessa informação ocorrerá somente quando o parâmetro **"Habilita controle manual de continuidade de afastamentos com atestado médico"**, disponível no menu Folha de Pagamento | Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Afastamento 1/2, estiver habilitado.

Nessa condição, o valor recebido na tag **sequence** será utilizado para preencher o campo **Data de Continuidade de Afastamento** no cadastro de Histórico de Afastamento do funcionário.

### Exemplo

Abaixo está um exemplo da API, destacando responsável pelo envio da informação de **Data de Continuidade de Afastamento**.

Abaixo está um exemplo da API, com a data responsável pelo envio da informação de **Data de Continuidade de Afastamento**.

## **05. DEMAIS INFORMAÇÕES**
