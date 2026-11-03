---
content_hash: 882f4d4830a1c1d0c477679a5758c5377915f98871f3e1c350ba1f09d0e0dc30
fetched_at: '2026-06-29T00:11:17.931953+00:00'
page_id: '682054374'
product: rm
source: tdn-rm
title: Importação de batidas integradas via API
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=682054374
version: 19
---

## ****01.**DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | Entrada de dados - Importação de batidas |
| Função: | Permitir a importação das batidas integradas via API |
| País: | Brasil |
| Requisito/Story/Issue: | DRHJORNRM-1750 e DRHJORNRM-8938 |

## **02. SITUAÇÃO/REQUISITO**

Permitir a importação das batidas integradas via API.

## **03. SOLUÇÃO**

Ajustar o processo de importação de batidas para obter os dados da tabela AINTEGRACAOBATIDAS, que foram inseridos por meio da API, e processar as marcações.

## **04. UTILIZAÇÃO**

Para realizar a configuração, siga os passos abaixo:

1. Acesse o menu **Configurações | Parametrizador | 08.01 - Iniciais | Etapa 5 - Integração | Integração Carol/TSA**.
2. Selecione os parâmetros **"Utilizar integração com o TSA"** e **"Importar batidas integradas via API"**.
3. Avance nas telas até concluir o processo.

Para importar as batidas, siga os passos abaixo:

1. Acesse o menu **Entrada de Dados | Importar**.
2. Na tela de importação, marque a opção **"Utilizar integração com o TSA"**.

Ao marcar essa opção, os seguintes campos serão desabilitados automaticamente:

* + Arquivo para importação
  + Layout do Relógio
  + Terminal de Coleta para Histórico
  + Considera última linha importada

      3. Clique em **Executar** para iniciar a importação.

Ao final do processo de importação, será exibido um log contendo os detalhes da execução.

**Importante:**

* Após realizar a importação de batidas, o campo **'****CODIMPORTPRODUT'** localizado na tabela **'****AINTEGRACAOBATIDAS'** terá seu valor alterado para **'1'**, esse valor sinaliza que as batidas foram importadas. Caso as batidas sejam canceladas ou excluídas não poderão ser reimportadas.

Magnetismo de batidas para importação do PontoWeb

O recurso de **magnetismo de batidas** está disponível a partir das versões **12.1.2502.266**, **12.1.2506.228** e **12.1.2510.157**.

Em alguns casos, um funcionário pode possuir mais de um vínculo com a empresa, de modo que o mesmo CPF esteja associado a múltiplas chapas. Nessas situações, durante a importação, o magnetismo de batidas compara o horário da marcação realizada com os horários configurados em cada vínculo e importa a batida para a chapa cujo horário seja o mais próximo da marcação.

Caso a marcação não esteja mais próxima de nenhum horário, ou seja, tenha a mesma distância para todos os horários, a batida será importada para a primeira chapa dos vínculos encontrada pelo sistema. Caso seja necessário considerar um vínculo diferente daquele para o qual a batida foi importada, a alteração deverá ser realizada manualmente.

## **05. ASSUNTOS RELACIONADOS**

**[Parametrizador - Parâmetros de Integração](https://tdn.totvs.com/pages/releaseview.action?pageId=452718976)**

**[API REST - recordClockMarkings/integracaobatidas (v2)](https://tdn.totvs.com/pages/viewpage.action?pageId=993703600)**
