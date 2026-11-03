---
content_hash: 701cd75d1693da910f193627d2a49b72a7dd7acdc851c5d1dc15420c1c76027d
fetched_at: '2026-06-29T00:10:44.380854+00:00'
page_id: '552573288'
product: rm
source: tdn-rm
title: FISCAL01-11499 DT Sped Fiscal C180 Ressarcimento do ICMS ST
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11499+DT+Sped+Fiscal+C180+Ressarcimento+do+ICMS+ST
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Varejo Gestão Fiscal  TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração de Arquivo Sped Fiscal |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11499 |

## **02. SITUAÇÃO/REQUISITO**

O Registro C180 é “filho” do registro C170 que são os itens do Lançamento Fiscal. Este registro deve ser gerado para Lançamentos Fiscais que atendam às seguintes regras, SE o flag para geração dos registros de ressarcimento/complemento estiver marcado na tela de geração do SPED:

* Lançamentos de entrada;
* CFOP associado esteja marcado como operação que controla ressarcimento/complemento do ST
* Modelos de documentos “01”, “1B”, “04” e “55”;
* Produto estiver marcado como tributado pelo ICMS ST nos Dados Fiscais por UF, considerando a UF da Filial
* Exista Lançamento de Ajuste para o Registro C185 associado

Atividades para essa issue:

1. Colocar na tela de geração do Sped um combo para que o usuário informe qual unidade será utilizada para geração dos registros: se pela unidade de controle do estoque ou se pela unidade de comercialização (lçto fiscal).

2. Implementar a geração do Registro C180

Mais informações sobre o Registro no TDN: [https://tdn.totvs.com/pages/viewpage.action?pageId=422546009#BLOCOC-C180](https://tdn.totvs.com/pages/viewpage.action?pageId=422546009#BLOCOC-C180 "Follow link")

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 1 | REG | Texto fixo contendo "C180” |  |
| 02 | COD\_RESP\_RET | Código que indica o responsável pela retenção do ICMS-ST:  1-Remetente Direto  2-Remetente Indireto  3-Próprio declarante | (Gerar igual ao campo 18 do Registro C176) Verificar o campo DREGRAICMS.RETENCAOICMSST: SubstitutoTributario = 1  NaoSeAplica = 2 Antecipação = 3| |
| 03 | QUANT\_CONV | Quantidade do item | Quantidade do item no lançamento fiscal, convertida para a unidade utilizada no controle do ressarcimento/complemento do ICMS ST, se forem diferentes. |
| 04 | UNID | Unidade adotada para informar o campo QUANT\_CONV. | Informar a unidade utilizada no controle do ressarcimento/complemento do ICMS ST. |

**Todos os campos de valores devem ser gerados convertidos para esta unidade**|

|  |  |  |  |
| --- | --- | --- | --- |
| 05 | VL\_UNIT\_CONV | Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo “QUANT\_CONV” | Informar o valor unitário líquido do item/produto (considerando descontos e acréscimos incondicionais aplicados sobre o valor bruto). |
| 06 | VL\_UNIT\_ICMS\_OP\_CONV | Valor unitário do ICMS operação própria que o informante teria direito ao crédito caso a mercadoria estivesse sob o regime comum de tributação, considerando unidade utilizada para informar o campo “QUANT\_CONV” | ATENÇÃO!! Houve alteração nas regras de preenchimento |
| 07 | VL\_UNIT\_BC\_ICMS\_ST\_CONV | Valor unitário da base de cálculo do imposto pago ou retido anteriormente por substituição, considerando a unidade utilizada para informar o campo “QUANT\_CONV”, aplicando-se redução, se houver. | Gerado  de acordo com a BC do ICMS ST do Item (DITEM.BASEICMSSTPRD). |
| 08 | VL\_UNIT\_ICMS\_ST\_CONV | Valor unitário do imposto pago ou retido anteriormente por substituição, inclusive FCP se devido, considerando a unidade utilizada para informar o campo “QUANT\_CONV” | ATENÇÃO!! Houve alteração nas regras de preenchimento |
| 09 | VL\_UNIT\_FCP\_ST\_CONV | Valor unitário do FCP\_ST agregado ao valor informado no campo “VL\_UNIT\_ICMS\_ST\_CONV” | Gerado de acordo com o Valor Unitário do FECP DO ICMS ST do Item (VLRICMSITEMFCPESTDEST.DITEM). |
| 10 | COD\_DA | Código do modelo do documento de arrecadação:  0 – Documento estadual de arrecadação  1 – GNRE | gerar sob demanda |
| 11 | NUM\_DA | Número do documento de arrecadação estadual, se houver | gerar sob demanda |

Quando for selecionada a unidade de controle de estoque para gerar os valores de ressarcimento, buscar o fator de conversão através do serviço do Nucleus entre a unidade de controle e a unidade do lançamento fiscal. Aplicar este fator sobre o valor unitário calculado.

## **03. SOLUÇÃO**

Foi implementado o registro C180 no Sped Fiscal.

Link da Documentação:
