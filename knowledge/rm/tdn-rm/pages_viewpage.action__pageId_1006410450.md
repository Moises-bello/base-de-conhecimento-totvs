---
content_hash: 955690e54b983cf8884a2198acbab5de51f848ffdc02bcccb484c98a3fb2c7b9
fetched_at: '2026-06-29T00:05:47.126745+00:00'
page_id: '1006410450'
product: rm
source: tdn-rm
title: DT - Folha Analítica - Nome Social
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1006410450
version: 5
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Folha Analítica - Nome Social |
| País: | Brasil |
| Issue: | [DRHROTRM-15428](https://jiraproducao.totvs.com.br/browse/DRHROTRM-15428) [DRHROTRM-15312](https://jiraproducao.totvs.com.br/browse/DRHROTRM-15312) |

## **02. LIBERAÇÃO**

  Lembrando que, será a partir dos patches:

* 12.1.2502.223
* 12.1.2506.172
* 12.1.2510.104 e superiores

## **03. SITUAÇÃO/REQUISITO**

A Folha Analítica atualmente não exibe o Nome Social do funcionário, mostrando apenas o nome de registro, o que contraria o Decreto Federal nº 8.727/2016 que assegura o uso do nome social na administração pública.

## **04. SOLUÇÃO**

Tratativa para que, ao gerar a Folha Analítica, use o **Nome Social** sempre que ele estiver preenchido no cadastro do Funcionário. Caso contrário, o sistema continuará utilizando o **Nome** padrão registrado.

**Exemplo:**  
No menu Administração de Pessoal | Funcionários | Aba Identificação, o funcionário com chapa 00001 possui o **Nome Social** preenchido, conforme demonstrado abaixo:

Ao gerar a Folha Analítica para a Chapa 00001 através do menu Folha Mensal | Folha Analítica, o sistema irá gerar o **Nome Social** no campo **Nome do Funcionário**.

O funcionário com chapa 00003 possui o **Nome Social** em branco, conforme demonstrado abaixo:

Ao gerar a Folha Analítica para a Chapa 00003 através do menu Folha Mensal | Folha Analítica, o sistema irá gerar o **Nome** no campo **Nome do Funcionário**.

## **05. DEMAIS INFORMAÇÕES**

* [Folha Analítica](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719339)
