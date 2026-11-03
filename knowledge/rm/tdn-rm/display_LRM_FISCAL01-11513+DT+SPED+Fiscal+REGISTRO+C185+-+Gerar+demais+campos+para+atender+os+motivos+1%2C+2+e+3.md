---
content_hash: 13e7cf7f0b55d66e1327a222d65230479e3cfc73e82d19385337876d42389b88
fetched_at: '2026-06-29T00:10:46.151571+00:00'
page_id: '553908851'
product: rm
source: tdn-rm
title: FISCAL01-11513 DT SPED Fiscal REGISTRO C185 - Gerar demais campos para atender
  os motivos 1, 2 e 3
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11513+DT+SPED+Fiscal+REGISTRO+C185+-+Gerar+demais+campos+para+atender+os+motivos+1%2C+2+e+3
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Varejo Gestão Fiscal  TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Geração do Arquivo SPED Fiscal |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11513 |

## **02. SITUAÇÃO/REQUISITO**

Complementação da geração do Registro C185 do SPED Fiscal.

O registro C185 é filho do C100 que é o documento fiscal. Este registro deve ser gerado para Lançamentos Fiscais que atendam às seguintes regras, SE o flag para geração dos registros de ressarcimento/complemento estiver marcado na tela de geração do SPED:

* Lançamentos de saída;
* CFOP associado esteja marcado como operação que controla ressarcimento/complemento do ST
* Modelos de documentos “01”, “1B”, “04” e “55”;
* Produto estiver marcado como tributado pelo ICMS ST nos Dados Fiscais por UF, considerando a UF da Filial

Para correta geração é imprescindível que o processo de associação já tenha sido executado para que sejam buscadas as Notas Fiscais de Entrada que saíram no registro C180 em períodos anteriores.

**REGISTRO C185 - INFORMAÇÕES COMPLEMENTARES DAS OPERAÇÕES DE SAÍDA DE MERCADORIAS SUJEITAS À SUBSTITUIÇÃO TRIBUTÁRIA (CÓDIGO 01, 1B, 04, 55 e 65).**

Este registro deve ser a soma dos valores detalhados no 1255.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Campo | Descrição | Motivo Retenção "0" | Motivo Retenção "1" | Motivo Retenção "2" | Motivo Retenção "3" |
| 1 | REG | Texto fixo contendo "C185” | C185 | | | |
| 2 | NUM\_ITEM | Número sequencial do item no documento fiscal | Gerado conforme o Número do Item do Lançamento Fiscal | | | |
| 3 | COD\_ITEM | Código do item (campo 02 do Registro 0200) | Código do Item do Lançamento Fiscal | | | |
| 4 | CST\_ICMS | Código da Situação Tributária referente ao ICMS | Código a CST informado no Item do Lançamento Fiscal | | | |
| 5 | CFOP | Código Fiscal de Operação e Prestação | Código da CFOP associada ao Lançamento Fiscal. | | | |
| 6 | COD\_MOT\_REST\_COMPL | Código do motivo da restituição ou complementação conforme Tabela 5.7 | Código do Ajuste associado ao Item | | | |
| 7 | QUANT\_CONV | Quantidade do item | Quantidade do Item **X** Fator de Conversão\*  ***\* Caso tenha optado por usar a Unidade do Estoque será obtido o Fator de Conversão entre a Unidade do Item da NF e a Unidade Controle do Produto.*** | | | |
| 8 | UNID | Unidade adotada para informar o campo QUANT\_CONV. | Unidade de Medida do Item ou Unidade de Controle do Produto, caso tenha sido marcada a opção na tela de geração da rotina | | | |
| 9 | VL\_UNIT\_CONV | Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo “QUANT\_CONV”. | ((Valor de Mercadoria - Descontos + Despesas + Seguro + Frete) **X** Fator de Conversao\*) **/** Quantidade do Item. | | | |
| 10 | VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV | Valor unitário para o ICMS na operação, caso não houvesse a ST, considerando unidade utilizada para informar o campo “QUANT\_CONV”, considerando redução da base de cálculo do ICMS ST na tributação, se houver. | NULO | Alíquota Interna do Produto para o Estado da Filial X VL\_UNIT\_CONV | NULO | Alíquota Interna do Produto para o Estado da Filial X VL\_UNIT\_CONV |
| 11 | VL\_UNIT\_ICMS\_OP\_CONV | Valor unitário do ICMS que o contribuinte teria se creditado referente à operação de entrada da mercadoria, caso estivesse submetida ao regime comum de tributação, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo “QUANT\_CONV” | NULO | NULO | Campo gerado com "0" pois MG não trata esse campo. | NULO |
| 12 | VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV | Valor médio unitário do ICMS que o contribuinte teria se creditado referente à operação de entrada das mercadorias em estoque caso estivesse submetida ao regime comum de tributação, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo “QUANT\_CONV” | NULO | Somatório do campo "VL\_UNIT\_ICMS\_OP\_CONV" dos registros C180 referenciados neste item + "VL\_ICMS\_OP" do Registro H030 | | |
| 13 | VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV | Valor médio unitário do ICMS/ST, incluindo FCP ST, das mercadorias em estoque, considerando a unidade utilizada para informar o campo “QUANT\_CONV” | NULO | Somatório do campo "VL\_UNIT\_ICMS\_ST\_CONV" dos registros C180 referenciados neste item + "VL\_ICMS\_ST" do Registro H030 | | |
| 14 | VL\_UNIT\_FCP\_ICMS\_ST\_ESTOQUE\_CONV | Valor médio unitário do FCP ST agregado ao ICMS das mercadorias em estoque, considerando a unidade utilizada para informar o campo “QUANT\_CONV” | NULO | Somatório do campo "VL\_UNIT\_FCP\_ST\_CONV" dos registros C180 referenciados neste item + "VL\_FCP" do Registro H030 | | |
| 15 | VL\_UNIT\_ICMS\_ST\_CONV\_REST | Valor unitário do total do ICMS/ST, incluindo FCP ST, a ser restituído/ressarcido, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo “QUANT\_CONV”. | NULO | (Campo 12 + Campo 13) - Campo 10 | Campo gerado com "0" pois MG não trata esse campo. | NULO |
| 16 | VL\_UNIT\_FCP\_ST\_CONV\_REST | Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo “VL\_UNIT\_ICMS\_ST\_CONV\_REST”, considerando a unidade utilizada para informar o campo “QUANT\_CONV” | NULO | %FECP do Produto para o Estado da Filial X VL\_UNIT\_ICMS\_ST\_CONV\_REST | Campo gerado com "0" pois MG não trata esse campo. | NULO |
| 17 | VL\_UNIT\_ICMS\_ST\_CONV\_COMPL | Valor unitário do complemento do ICMS, incluindo FCP ST, considerando a unidade utilizada para informar o campo “QUANT\_CONV” | NULO | NULO | NULO | (Campo 10 - Campo 12 - Campo 13) |
| 18 | VL\_UNIT\_FCP\_ST\_CONV\_COMPL | Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo “VL\_UNIT\_ICMS\_ST\_CONV\_COMPL”, considerando unidade utilizada para informar o campo “QUANT\_CONV”. | NULO | NULO | NULO | %FECP do Produto para o Estado da Filial **X** VL\_UNIT\_ICMS\_ST\_CONV\_COMPL |

## **03. SOLUÇÃO**

Foi implementado a geração do registro C185 em sua totalidade.
