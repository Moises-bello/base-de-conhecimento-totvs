---
content_hash: 61babec850a23e8aaf3419e0e05c3e20e1cc3299286f793afcb5e4be4058494b
fetched_at: '2026-06-29T00:05:51.720924+00:00'
page_id: '1054121536'
product: rm
source: tdn-rm
title: DT - S-1010 - Adequação da tag <codIncIRRF> para estorno de pensão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1054121536
version: 24
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-1010 - Adequação da tag <codIncIRRF> |
| País: | Brasil |
| Issue: | [DRHROTRM-18115](https://jiraproducao.totvs.com.br/browse/DRHROTRM-18115) |

## **01. VERSÕES**

**A partir das Versões:**

* 12.1.2506.281
* 12.1.2510.201
* 12.1.2602.124 e Superiores

## **02. SITUAÇÃO/REQUISITO**

Adequação dos valores gerados na tag <codIncIRRF> dos eventos de estorno de pensão ao eSocial.

## **03. SOLUÇÃO**

Com a inclusão do IRRF no eSocial, foi necessário realizar ajustes nos valores de incidência  de IRRF (tag <codIncIRRF>) no evento S-1010 para rubricas destinadas a estornos de pensão. 

Essa adequação tem como objetivo evitar qualquer discrepância entre a folha de pagamento e os valores retornados pelo governo.

**Para garantir que a tag  `<codIncIRRF>`  seja gerada corretamente, certifique-se de que os códigos de cálculo 199, 200, 201 e 327 estejam configurados com incidência de IRRF.**

**O que foi ajustado?**

Nos patches acima mencionados, os valores enviados no XML do evento S-1010 para os códigos de cálculos abaixo sofrerão as seguintes alterações:

|  |  |  |
| --- | --- | --- |
| **CÓDIGO DE CÁCULO** | **CODINCIRRF ANTES DO AJUSTE** | **CODINCIRRF DEPOIS DO AJUSTE** |
| [199 - ESTORNO DE PENSÃO ALIMENTÍCIA SOBRE FOLHA](https://tdn.totvs.com/pages/viewpage.action?pageId=452718666) | 00 | 51 |
| [200 - ESTORNO DE PENSÃO ALIMENTÍCIA SOBRE 13º SALÁRIO](https://tdn.totvs.com/pages/viewpage.action?pageId=452718671) | 00 | 52 |
| [201 - ESTORNO DE PENSÃO ALIMENTÍCIA SOBRE FÉRIAS](https://tdn.totvs.com/pages/viewpage.action?pageId=452718669) | 00 | 53 |
| [327 - ESTORNO DE PENSÃO DE RESCISÃO](https://tdn.totvs.com/pages/viewpage.action?pageId=452718658) | 00 | 53 |

1Como realizar a geração dos gatilhos do S-1010?

* Acessar o menu eSocial | Outros processos |[Comparativo de Incidências de Rubricas](https://tdn.totvs.com.br/pages/releaseview.action?pageId=519195285).

* Executar o relatório marcando a opção "<codIncIRRF>" e comparar a tags <codIncIRRF>, conforme demonstrado abaixo:

* Após a execução do processo, serão listados os registros das rubricas que possuem as tags com divergência ao clicar no botão "**Exibir Visão do Resultado**".

* Esta listagem será apresentada conforme a seleção realizada.

* Através do menuProcessos | Gerar gatilho de rubricas divergentes entre o último XML e a base, é possível gerar o gatilho na fila de eventos para as rubricas que apresentaram divergências.

* Acessar o menu eSocial | Fila de Eventos | Gerar o XML, e gerar para todos os eventos ajustados através do processo citado anteriormente e enviar para o governo.

* Para que a atualização seja realizada corretamente, **será necessário editar os gatilhos**(gerados através do processo) e ajustar o início de validade da verba. Para isso **basta alterar o campo "Competência" dentro do gatilho para o mês/ano desejado e, após isso, executar o processo de gerar o XML e transmitir ao governo.**

**Exemplo:**

Após a execução da rotina [Comparativo de Incidências de Rubricas](https://tdn.totvs.com.br/pages/releaseview.action?pageId=519195285), foram listados registros com inconsistência de tags.

Foi executado o processo "Gera gatilho de rubricas divergentes entre último XML e base".

Os registros dos gatilhos do evento S-1010 foram gerados da Fila de Eventos com o status de "Pendente".

Editando o gatilho, é possível alterar a data de vigência do mês/ano.

Retificação do evento S-1210

* + Realizar a retificação do evento S-1200 e S-1210 através do menu eSocial | Eventos Periódicos.

* Selecione o período de apuração que seja realizada a retificação dos evento S-1200e S-1210, e marque os registros a serem retificados e execute o processo "Gerar Retificação Arquivo eSocial".

## **04. ASSUNTOS RELACIONADOS**
