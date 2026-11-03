---
content_hash: 86ec14cce6cb7bf1f2b002adff7c1f9363d99fa9423dce114b2366d86aa4a984
fetched_at: '2026-06-29T00:11:48.849936+00:00'
page_id: '828426033'
product: rm
source: tdn-rm
title: DT - Base Aceleradora -  Eventos de Média
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=828426033
version: 5
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cópia de Dados - Entidade Evento |
| País: | Brasil |
| Epic | [DRHCALCRM-6044](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6044) |

## **02. SITUAÇÃO/REQUISITO**

Adequar o processo de cópia de dados da entidade de Evento para considerar os eventos de média, pois quando era feita a cópia de dados e existia eventos de média cadastrados para um evento, os eventos de média não estavam sendo considerados/copiados. 

## **03. SOLUÇÃO**

Foi adequada a entidade de Evento para realizar a cópia dos dados e os eventos de média cadastrados para cada evento, constante na tabela PEVTMED.

## **03. EXEMPLO**

No nosso exemplo, vamos supor que temos as bases **ORIGEM** e **DESTINO**:

**Base ORIGEM - Contém os dados da PEVTMED que serão copiados:**

**Base DESTINO - Irá receber os dados da PEVTMED, através da cópia de dados:**

Na base **DESTINO**, verificar no cadastro de base externa está apontando para o Alias criado para base origem corretamente e está ativo:

**Observação: Caso utilize ambiente três camadas e/ou fracionamento de jobs, verificar se está usando o host em 3 camandas e o cockpit ligado para executar processos.**

Na base **DESTINO**, executar a cópia do **template eventos** que contém somente a entidade do cadastro de eventos, marcando a opção substitui registros, caso eles existam:

Executar o processo para a cópia dos eventos de código **1001** e **1002** para a tabela **PEVENTO**:

Veja que na base **DESTINO**, foram inseridos os eventos constantes na tabela **PEVTMED**:

## **04.****ASSUNTOS RELACIONADOS**

* [Cópia de Dados](https://tdn.totvs.com/pages/viewpage.action?pageId=592067102)
