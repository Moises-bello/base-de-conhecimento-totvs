---
content_hash: 15cedd65501ec433247d6a3dee6fe14ad79260f48c3685fd1232a7abcdef626a
fetched_at: '2026-06-29T00:11:50.901858+00:00'
page_id: '845418813'
product: rm
source: tdn-rm
title: DT -  Relatório de Conferência de INSS Patronal e Lançamento Financeiro - Percentual
  Autônomos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=845418813
version: 17
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Relatório de Conferência de INSS Patronal e Lançamento Financeiro - Autônomos |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-8034](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8034 "View this issue") |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2306.264
* 12.1.2310.213
* 12.1.2402.155 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Permitir a configuração de um percentual diferenciado para autônomos para calcular o INSS Patronal sobre a base de cálculo dos autônomos, tanto no **Relatório de Conferência de INSS Patronal** quanto no lançamento financeiro do tipo "**25 - Total Guia INSS DCTFWeb**". Esta modificação é necessária para atender situações específicas onde há isenção da parte patronal para autônomos ou CLT.

## **04. SOLUÇÃO**

No cadastro de Seção, no anexo "**Histórico de Percentuais para INSS**", disponibilizamos o campo "% Autônomos". Com essa adição, as gerações dos processos do Relatório de Conferência de INSS Patronal e do Lançamento Financeiro tipo "**25 - Total Guia INSS DCTFWeb"** passam a considerar o valor cadastrado nesse campo para o cálculo da parte empresa.

falseATENÇÃO!

1. Após a atualização da versão será necessário executar o sistema **RM.Atualizador.exe** para a criação do novo campo %Autônomos.
2. Se o novo campo '% **Autônomos**' estiver em branco (NULL), o sistema utilizará o percentual informado no campo '**% Empresa'**. Se estiver preenchido com zero ou qualquer outro valor, o sistema utilizará o próprio valor do campo '% Autônomos'. Essa adaptação foi feita para evitar que clientes sem diferenças nos percentuais entre os campos sejam obrigados a preencher o novo campo.

**Tratativa realizada no produto**

1) No menu Administração de Pessoal | Seções | Anexos | Histórico de Percentuais para INSS será apresentando o campo "**%Autônomos**", conforme demonstrado abaixo: 

2) Na geração do Relatório Conferência INSS Patronal ao calcular o campo "Total Empresa" será verificando esse campo quando o tipo do funcionário for "**A-Autônomo**".

Seção 01

Seção 02

3) No processo Encargos | Geração do Lançamento Financeiro será considerado o novo campo no cálculo, conforme demonstrado abaixo:

## **5.****DEMAIS INFORMAÇÕES**

[Relatório de Conferência INSS Patronal](https://tdn.totvs.com/pages/viewpage.action?pageId=714242305)

<https://tdn.totvs.com.br/pages/viewpage.action?pageId=496388652>
