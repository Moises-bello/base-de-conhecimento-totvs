---
content_hash: 1ff13c9f2f4c79b376772952f9dd4cbc6e95bf2f92caa49e9014bcd1df2bae56
fetched_at: '2026-06-29T00:10:52.345940+00:00'
page_id: '572017307'
product: rm
source: tdn-rm
title: FISCAL01-14125 DT ADRC-ST Paraná
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572017307
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Campos |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14125 |

## **02. SITUAÇÃO/REQUISITO**

Conforme o Leiaute do ADRC-ST – Ressarcimento do Paraná, os campos abaixo devem ser ajustados:

1 -  Necessário alterar no Layout o Campo **"CODIFICAÇÃO DO ARQUIVO"** para **'Unicode UTF-8 sem BOM'**. Atualmente geramos somente com 'Unicode UTF-8' e segundo a SEFAZ do PR este formato é 'UTF-8 BOM'\*\*

2 – Os **campos A9** - CNPJ do Centro de Distribuição e **A10** - Inscrição Estadual do Centro de Distribuição, devem ser gerados com informação.

Nestes campos devem ser informados o CNPJ e Inscrição Estadual do Estabelecimento que Centraliza as aquisições dos Produtos Sujeitos a Substituição Tributária, e caso não existir Centro de Distribuição, **devem ser informados nestes campos o próprio CNPJ e Inscrição Estadual**.

3 – O campo **B11 - ALIQ\_FECOP** Alíquota do FECOP - Informar o percentual da alíquota do ICMS destinada ao FECOP. Deve ser **gerado em branco** quando não houver alíquota do FECP no Produto.

4 - O **Campo CST** dos Registros deve ser gerado com **2 posições** exemplo 10 e não 010, o campo **CSOSN** que deve ser gerado com **3 posições**.

5 - **Não** devem ser geradas no arquivo as **NFe de Entrada** que não tem Saída associada.

6 – Registro 1310- o **Campo I15** - VL\_ICMS\_EFET Valor do ICMS efetivo na saída deve ser gerado em branco quando não houver valor.

## **03. SOLUÇÃO**

Foram realizadas as seguintes alterações no layout ADRC-ST Paraná:

1 - Codificação do arquivo alterada para 'Unicode UTF-8 sem BOM'  
2 - Os campos **A9 - CNPJ do Centro de Distribuição** e **A10 - Inscrição Estadual do Centro de Distribuição** estão sendo preenchidos com o próprio CNPJ e Inscrição Estadual.  Obs.: Atualmente não temos cadastro para buscar o Centro de Distribuição e IE vinculado ao lançamento, sendo assim estamos passando a preencher com os dados da Filial.  
3 - O campo **B11 - ALIQ\_FECOP Alíquota do FECOP** está sendo gerado em branco quando não houver alíquota do FECP no Produto.  
4 - O Campo CST dos Registros está sendo gerado com 2 posições exemplo 10 e não 010. O campo CSOSN que está sendo gerado com 3 posições.  
5 - Nota Fiscal Eletrônica de Entrada que não tem Nota Fiscal de Saída associada não estão sendo mais geradas no arquivo.  
6 - O Registro **1310- o Campo I15 - VL\_ICMS\_EFET Valor do ICMS efetivo na saída**, está sendo gerado em branco quando o valor for "0" (zero).
