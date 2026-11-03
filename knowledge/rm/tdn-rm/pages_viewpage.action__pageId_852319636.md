---
content_hash: 7c7375a55e06d8716aad74d16f5595ca5d6d08411d9a489ac7cd57a33a1ff8e0
fetched_at: '2026-06-29T00:11:53.847570+00:00'
page_id: '852319636'
product: rm
source: tdn-rm
title: 20408495 DDWMS-13341 - DT ERRO - Rotina 3774 - Separação Peso Variável (erro
  ao preencher código de barras com mais de 14 caracteres)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=852319636
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS Distribuição Linha Winthor |
| Linha de Produto: | Linha Winthor |
| Segmento: | Distribuição TOTVS Goiânia |
| Módulo: | 37 - RÁDIO FREQUÊNCIA WMS |
| Função: | 3774 - SEPARAÇÃO PESO VARIÁVEL |
| Ticket: | [20408495](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%2220408495%22 "20408495") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DDWMS-13341](https://jiraproducao.totvs.com.br/browse/DDWMS-13341) |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar a separação de um carregamento pela rotina 3774, está sendo retornado a mensagem de erro: "Access violation at adress 02383 10E in module 'PCSIS3774.EXE'...";

## **03. SOLUÇÃO**

Foi corrigido o tratamento de código de barras com quantidade de caracteres maior que 14, entrando na validação de "EAN128", que estava causando erro de memória.

* [Saiba como utilizar](https://tdn.totvs.com/pages/viewpage.action?pageId=846866958#tabs-Saiba%20como%20utilizar)

Favor atualizar rotina **3774** para versão igual ou superior a descrita abaixo:

* Versão **36.0.0.9**;

**Passo a passo:**

* Abra a rotina **3774**;
* Informe os campos conforme a necessidade:

* No campo "Cod.Barras", adicione um código de barras VÁLIDO com mais de 14 caracteres e pressione a tecla **ENTER**;

* Por fim, preencha os demais campos conforme a necessidade e finalize o processo pelo botão **Finalizar**.

**Observações:**

* A rotina continuará funcionando da mesma forma que a versão anterior, visto que o ajuste foi feito apenas na validação do código de barras.

## **04. DEMAIS INFORMAÇÕES**

        Não se aplica

## **05. ASSUNTOS RELACIONADOS**

        Documentação de como utilizar a rotina **3774**:
