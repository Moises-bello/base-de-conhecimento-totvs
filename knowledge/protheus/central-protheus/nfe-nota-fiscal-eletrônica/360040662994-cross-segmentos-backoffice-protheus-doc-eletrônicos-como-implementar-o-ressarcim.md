---
article_id: 360040662994
category: NFe - Nota Fiscal Eletrônica
content_hash: e57956dc0d607c02e89a1450b7163870c4667637e43c52119595b5f45aeb7160
fetched_at: '2026-06-28T22:40:01.769091+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como implementar
  o Ressarcimento de ICMS ST '
type: support-article
updated_at: '2023-12-04T17:47:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040662994--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-implementar-o-Ressarcimento-de-ICMS-ST
---

**Dúvida**

Como implementar o Ressarcimento de ICMS ST ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Implementado o Ressarcimento de ICMS ST na NF-e de saída (NF-e de Ajuste) conforme determina a Orientação de Preenchimento da NF-e - versão 1.04 – 31/10/2012:  
  
1. Informar a finalidade da emissão = NF-e de Ajuste **(finNfe = 3).**  
  
2. Informar a Natureza da operação = Ressarcimento de ICMS-ST **(natOp = Ressarcimento de ICMS-ST).**  
  
3. Código do Produto; utilizar o código do CFOP. Exemplo: CFOP=5.603, Código do produto = CFOP5603 **(cProd = CFOP5603).**  
  
4. Descrição do produto; preencher com a expressão: Ressarcimento de ICMS-ST **(xProd = Ressarcimento de ICMS-ST).**  
  
5. Código NCM; no caso de ressarcimento de ICMS-ST informar 00 **(NCM = 00).**  
  
6. Valor Total Bruto dos Produtos ou Serviços; informar o valor total do ressarcimento **(vProd = Valor total do ressarcimento).**  
  
7. Informar a modalidade sem frete; código 9 **(modFrete = 9).**  
  
No Cadastro de Tipos de Entrada/Saída (MATA080), informe um TES com os seguintes detalhes:  
  
Campo Cred. ICMS **(F4\_CREDICM = N)**= indica se credita ou não o ICMS para calculo do custo.  
Campo Gera Dupl. **(F4\_DUPLIC = S)**= indica se gera ou não duplicatas.  
Campo Calcula ICMS **(F4\_ICM = N)=** indica se calcula ICMS.  
Campo Cod.Fiscal **(F4\_CF = 5603)=** indica o código fiscal de Ressarcimento de ICMS ST.  
Campo Txt Padrão **(F4\_TEXTO)** = RESSARCIMENTO DE ICMS-ST): informar exatamente este texto. Campo Agrega Valor **(F4\_AGREG = S)**: indica como é tratado o valor do item no total do documento.  
Campo Agrega Solid **(F4\_INCSOL = N)**: Indica o critério de calculo de ICMS Solidário.  
Campo Fórmula **(F4\_FORMULA)**: 'RESSARCIMENTO DE ICMS-ST'  
Campo Ajuste CIAP **(F4\_AJUSTE = S)**: indica que a finalidade da NF-e (tag finNfe = 3 no XML) é uma NF-e de Ajuste.  
  
  
2. No Cadastro de Produtos **(MATA010)**, informe um produto com os seguintes detalhes:  
  
Campo Código **(B1\_COD = CFOP5603)**: utilizar o código do CFOP. Exemplo CFOP=5603; Código do produto = CFOP5603.  
  
 Campo Descrição **(B1\_DESC = RESSARCIMENTO DE ICMS-ST)**: informar exatamente esta descrição para o produto.  
  
Campo Pos.IPI/NCM **(B1\_POSIPI = 00)**: informar exatamente este código para o NCM.  
  
3. Na inclusão de um Pedido de Venda (MATA410), considere o preenchimento dos campos:  
  
Tipo Pedido **(C5\_TIPO = I-Comp.ICM)**: tipo do pedido de venda = Complemento de ICMS; por se tratar de uma NF-e de Ajuste.  
  
Tipo de Frete **(C5\_TPFRETE = S-Sem Frete)**: tipo de Frete utilizado.
