---
content_hash: ab9dc51b2181625493b7f31ef124a3df316582c9facc074154e70ab3edac6614
fetched_at: '2026-06-29T00:11:50.667834+00:00'
page_id: '844262233'
product: rm
source: tdn-rm
title: DT - Cálculo de média de Férias - Período Aquisitivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=844262233
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cálculo de média de férias |
| Issue: | [DRHCALCRM-6494](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6494) |

## **02. SITUAÇÃO/REQUISITO**

Tratar no Cálculo de média de férias para que seja considerado os últimos meses dentro do período aquisitivo conforme parametrizado no sindicato e faça a comparação da média de cada grupo e lançado que for de maior valor.

## **03. SOLUÇÃO**

Será apurado o maior valor de média de férias considerando o valor recebido entre os  últimos meses selecionados dentro do período aquisitivo, dependendo da parametrização.

Exemplo

Realizar o cálculo de Médias de Férias por Período Aquisitivo, mas realizando a Médias dos últimos 12, 6 e 3 meses, conforme exemplo abaixo:

Período Aquisitivo: 01/05/2021 a 30/04/2022

Média 12 Meses Período Aquisitivo: R$ 1.150,00

Média últimos 6 Meses dentro do Per. Aquisitivo: R$ 1.091,67

Média últimos 3 Meses dentro do Per. Aquisitivo: R$ 1.583,33

O maior valor apurado foi R$1.583,33, portanto este deverá ser o valor considerado para pagamento.

Para que o lançamento para a Folha de Pagamento seja realizado, será utilizado o processo padrão do sistema, onde após parametrizar os grupos de médias nos Eventos p/ pagamento de Média de Férias, é necessário informar a incidência de média no cadastro dos eventos pagos ao funcionário.

Processos/Cadastros que serão contemplados:

1. Novos parâmetros no Sindicato (Média de férias e Média de férias Rescisão) para que seja tratado em todos os cálculos

1. Últimos Meses Per. Aquisitivo

2. Cálculo de Férias
3. Cálculo de Rescisão
4. Cálculo de Provisão
5. Passivo Trabalhista
6. Cálculo de Diferença de Férias
7. Cálculo da Rescisão Complementar
8. Funções de Fórmula: CALCMED, CALCMEDDATA, CALCMEDJOR, MEDCOMIS, MEDCOMISDATA
9. Média de comissão (Somente quando não usar parâmetros específicos)
10. Importação/Exportação do Sindicato

Foi alterado também a forma de gravação nas tabelas  PFMEDIACALCULO,PFMEDCALCEVT , PFMEDCALCEVTMES , PFMEDCALCGRUPO ePFMEDCALCFORMADIC considerando "Últimos Meses Per. Aquisitivo" concatenando o valor informado nesses campos com o 99 informado em 'Número de meses'.

## **04.** **ASSUNTOS RELACIONADOS**

* Sindicatos - [Tipo de Cálculo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719183)
* [Layout Para Importação de Parâmetros de Cálculo do Sindicato](https://tdn.totvs.com/pages/viewpage.action?pageId=452719283)
