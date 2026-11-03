---
content_hash: 829b7a2fac2a48dca4910b5e66e7cd34bd6ee76f90ad0599f763f0e33785e5fb
fetched_at: '2026-06-29T00:10:10.495822+00:00'
page_id: '452719854'
product: rm
source: tdn-rm
title: Diferença de 13º Salário - FOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719854
version: 7
---

A diferença de 13º salário pode ocorrer quando o funcionário tiver reajuste salarial no mês dezembro e já tiver recebido o 13º com o salário anterior. Esta diferença poderá ser paga na competência dezembro ou janeiro, dependendo do mês de competência em que o usuário se encontra.

Ao pagar a diferença de 13º salário no mês de Dezembro o sistema assumirá o evento com Código de Cálculo 66 cadastrado no Grupo 0 no campo Evento de Diferença pasta diferença de 13º salário, caso o evento não esteja cadastrado o sistema assumirá o 1º evento cadastrado com código de cálculo (66) na tabela de eventos.  
Se a diferença for paga no mês de Janeiro irá abrir um combo apresentando os eventos com CC(66) com incidência em INSS folha.  
Somente nos meses de dezembro e janeiro é passível pagar a diferença de 13º salário.  
As tabelas de cálculo utilizadas na diferença são:   
*Pagamento da diferença em dezembro:*  
Tabela INSS – dezembro  
Tabela IRRF - dezembro  
*Pagamento da diferença em janeiro do ano seguinte:*  
Tabela INSS - Janeiro  
Tabela IRRF – dezembro  
  
**Observação 1:**

* Se o lançamento de 13º Salário ocorrer em janeiro, o usuário deverá criar um novo evento com de Código de Cálculo 066 - Diferença de 13º Salário e com incidência em INSS (Folha de Pagamento). Isto acontece porque o provento pago em janeiro participa do cálculo de INSS de Folha e utiliza a tabela de cálculo de INSS de janeiro, ou seja, o recolhimento de INSS será feito juntamente com a folha de janeiro (conforme legislação vigente). O evento deverá incidir também em IRRF 13º salário.

**Observação 2:**

* Ao calcular a diferença em Janeiro se existir alguma média discriminada o sistema irá lançar toda a diferença no evento com o CC(66).

O campo DISSÌDIO é marcado Sim quando o cálculo da diferença for por dissidio. Quando estiver em competência diferente de Dezembro e Janeiro este parâmetro ficará desabilitado, porque nestes meses somente a diferença de 13º por dissidio pode ser paga.

**Observação 3:**

* Para o cálculo de diferença por dissídio de 13º salário deverá ser utilizado o Cód. Cálculo 180 - DIFERENÇA DE 13º SALÁRIO POR DISSÍDIO.
* Para o cálculo de diferença de 13º salário deverá ser utilizado o Cód. Cálculo 66 - DIF. DE 13º SALÁRIO.

**Observação 4:**

* Não será tratada a emissão da guia de INSS por dissídio pelo sistema. Esta guia deve ser emitida pelo validador do SEFIP com os códigos de recolhimentos específicos para estes fins, sendo o código de recolhimento de FGTS de dissídio = 650 - Recolhimento ao FGTS e informações à Previdência Social relativo a dissídio coletivo, reclamatória trabalhista ou conciliação perante as Comissões de Conciliação Prévia (no prazo ou em atraso).

**Observação 5:**

* No processo da Diferença de 13º Salário, o sistema irá verificar na competência dezembro o envelope de pagamento que contém eventos com os códigos de cálculo de 13º e recalcular os valores devido ao funcionário, considerando médias, alterações salariais, fórmulas, etc. Quando não existir nenhum envelope em dezembro contendo eventos de 13º, será criado um período 99 para armazenar as verbas geradas por diferença, caso seja encontrado algum valor devido.

Marcando o parâmetro "**Permite lançamento de restituição de IRRF 13º**" ao recalcular o envelope da 2º parcela de 13º e o valor de IRRF ficar menor que o descontado, o sistema irá lançar a restituição de IRRF de forma automática no processamento da diferença de 13º. Este parâmetro deve ser utilizado antes do envio do valor descontado para receita.

Dica:

Veja também informação importante no cálculo de diferença quando envolve Pensão Alimentícia no TDN
