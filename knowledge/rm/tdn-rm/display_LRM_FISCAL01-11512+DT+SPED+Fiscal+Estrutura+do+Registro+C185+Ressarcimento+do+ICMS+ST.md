---
content_hash: aa0a9a2a60c88681d7cba1e69b94e835316b0cd02ea76ac26c84974940cec91c
fetched_at: '2026-06-29T00:10:44.503319+00:00'
page_id: '552597375'
product: rm
source: tdn-rm
title: FISCAL01-11512 DT SPED Fiscal Estrutura do Registro C185 Ressarcimento do ICMS
  ST
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11512+DT+SPED+Fiscal+Estrutura+do+Registro+C185+Ressarcimento+do+ICMS+ST
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Varejo Gestão Fiscal  TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração de Arquivo SPED Fiscal |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11512 |

## **02. SITUAÇÃO/REQUISITO**

O Registro C185 é “filho” do registro C100 que é o próprio Documento Fiscal. Para gerar esse arquivo é necessário marcar o Parâmetro "**Gerar ressarcimento/complemento ICMS ST**" na tela de geração do SPED Fiscal.

Será preciso informar, também na tela de geração do SPED Fiscal, qual é o critério de informação da unidade para o Estado que está sendo gerado a rotina: se pela unidade do estoque (0200) ou pela unidade de comercialização (unidade informada nos Lançamentos Fiscais).

Serão selecionados os Lançamentos Fiscais que atendam às seguintes regras:

* Lançamentos de saída;
* CFOP associado esteja marcado como operação que controla ressarcimento/complemento do ST (DCFOP.OPERACAOSTCOMPRA)
* Modelos de documentos “01”, “1B”, “04”, “55” e "65";
* Produto estiver marcado como tributado pelo ICMS ST nos Dados Fiscais por UF, considerando a UF da Filial (TPRDCODFISCAL.TRIBUTADOICMSST)
* Exista Lançamento de Ajuste para o Registro C185 associado ao Item do Lançamento

Mais informações sobre o Registro no TDN: <https://tdn.totvs.com/x/WYovGQ>

Nesta tarefa foi implementado dos campos 01 até o 09

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C185” |  |
| 02 | NUM\_ITEM | Número sequencial do item no documento fiscal | Gerado conforme o Número do Item do Lançamento Fiscal |
| 03 | COD\_ITEM | Código do item (campo 02 do Registro 0200) | Código do Item do Lançamento Fiscal |
| 04 | CST\_ICMS | Código da Situação Tributária referente ao ICMS | Código a CST informado no Item do Lançamento Fiscal |
| 05 | CFOP | Código Fiscal de Operação e Prestação | Código da CFOP associada ao Lançamento Fiscal. |
| 06 | COD\_MOT\_REST\_COMPL | Código do motivo da restituição ou complementação conforme Tabela 5.7 | Campo Novo a ser criado no CFOP |
| 07 | QUANT\_CONV | Quantidade do item | Quantidade do item no lançamento fiscal, convertida para a unidade utilizada no controle do ressarcimento/complemento do ICMS ST, se forem diferentes. |
| 08 | UNID | Unidade adotada para informar o campo QUANT\_CONV. | Informar a unidade de medida adotada pela UF para o controle de ressarcimento/restituição de ICMS ST |

**Todos os campos de valores devem ser gerados convertidos para esta unidade**

|  |  |  |  |
| --- | --- | --- | --- |
| 09 | VL\_UNIT\_CONV | Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo “QUANT\_CONV”. | Informar o valor unitário líquido do item/produto (considerando descontos e acréscimos incondicionais aplicados sobre o valor bruto). |
| 10 | VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV | Valor unitário para o ICMS na operação, caso não houvesse a ST, considerando unidade utilizada para informar o campo “QUANT\_CONV”, considerando redução da base de cálculo do ICMS ST na tributação, se houver. | Valor correspondente à multiplicação da alíquota interna do produto  (incluindo FCP) pelo valor correspondente à operação de saída. Esse valor terá que ser calculado porque a operação de saída pode não ser tributada. |

## **03. SOLUÇÃO**

Foi implementado o registro C185 dos campos 01 até o 09 no SPED Fiscal.

Link da Documentação:
