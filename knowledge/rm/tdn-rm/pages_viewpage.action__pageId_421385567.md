---
content_hash: fbbb7303b92f5e1dc8bd8449800860c29eec855482f10c592d07ca47d033b704
fetched_at: '2026-06-29T00:09:16.821638+00:00'
page_id: '421385567'
product: rm
source: tdn-rm
title: Reajuste de Períodos Liberados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385567
version: 3
---

Define-se um novo índice de reajuste para um período já liberado, este período pode ter sido liberado sem reajuste ou com um reajuste diferente do reajuste definitivo, gerando um valor "a pagar" ou "a receber" com a diferença entre o reajuste liberado e o novo reajuste. O reajuste definitivo não altera o valor do contrato e só pode ser efetuado uma vez por período.  
  
 Aparecerá uma janela com os seguintes campos:  
 Os campos Período, Data Início e Data Final serão preenchidos de acordo com o período selecionado.  
  
 Data da Liberação: Informe a data da liberação do valor do reajuste definitivo.  
  
 % Inicial: Virá preenchido com o valor percentual do reajuste da liberação da medição.  
  
 % Definitivo: Informe o valor percentual do reajuste definitivo.  
  
 Valor a Pagar: Virá preenchido com diferença do valor com o percentual que foi liberada a medição do valor com o percentual definitivo.  
  
 Valor da Medição: Básico - valor sem reajuste. Reajuste Inicial - valor com o reajuste que foi liberada a medição. Reajuste Definitivo - valor com o reajuste definitivo.

Caso o parâmetro de **Utiliza Valor do Reajuste na Medição (PI + R)** esteja habilitado, os períodos liberados ao realizar o reajuste para um dos períodos, o sistema não irá incluir um novo período de reajuste e sim, gera um valor de saldo na coluna Saldo de reajuste. O saldo de reajuste pode ser utilizado no período posterior, podendo ser consumido somente o saldo de reajuste.
