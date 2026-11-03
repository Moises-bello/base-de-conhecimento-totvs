---
article_id: 9525473721751
category: Originação de Grãos (OG)
content_hash: 3fff98bd2cdbf247f399ed706d0cc1f4c60f89601ef782acde3d64347b1d703c
fetched_at: '2026-06-28T22:45:45.272774+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Visão Geral - Contrato de Venda - Conceito e
  Campos Principais
type: support-article
updated_at: '2025-06-21T15:42:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9525473721751-Agro-Linha-Protheus-AGR-Vis%C3%A3o-Geral-Contrato-de-Venda-Conceito-e-Campos-Principais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21053254929303) Tempo aproximado para leitura: **00:01:35 min** **Dúvida**Quais são os **Principais Campos** e qual o conceito do Contrato de Venda?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Principais Campos - Conceitos Clássicos:**O Contrato de Venda quando a inclusão é realizada por meio da rotina clássica de comercialização **MV**[**\_ARO002**](https://tdn.totvs.com/pages/viewpage.action?pageId=370616326) com conteúdo igual .F, possui os principais campos citados abaixo:

* **Dados Básicos**
* **Quantidades**
* **Dados Negócio/ Financeiro**
* **Logística**
* **Previsão de Entregas**
* **Financeiro**

| Campo | Descrição |
| --- | --- |
| Entidade | Código do cliente para quem destina-se a venda. |
| Safra | Código da Safra na qual o commodities se refere. |
| Produto | Código do produto que será comercializado no contrato de venda. |
| TES | Tipo de Entrada/Saída. A TES é responsável pela correta classificação tributária dos documentos fiscais de entrada e saída registrados no Sistema. |
| Operação | Permite informar o código da operação. Esse dado é apenas informativo. O cadastro da operação é realizada por meio do programa. OGA310 - Operações. |

**Principais Campos - Conceito da Nova Comercialização:**

O Contrato de Venda quando gerado por meio da rotina da Nova Comercialização **MV**[**\_ARO002**](https://tdn.totvs.com/pages/viewpage.action?pageId=370616326) com conteúdo igual .T, possui os principais campos citados abaixo:

* **Dados Básicos**
* **Quantidades**
* **Dados Negócio/Financeiro**
* **Logística**
* **Previsão de Entregas**
* **Financeiro**
* **Corretoras**
* **Exportação**
* **PREPO**
* **Recebimento**

Nesse espaço são definidos os itens principais do contrato de venda como: cliente, safra, produto e TES.

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Entidade | Código do cliente para quem destina-se a venda. |
| Safra | Código da Safra na qual o commodities se refere. |
| Produto | Código do produto que será comercializado no contrato de venda. |
| TES | Tipo de Entrada/Saída. A TES é responsável pela correta classificação tributária dos documentos fiscais de entrada e saída **registrados no Sistema.** |
| Tipo Embalagem | Tipo de embalagem. Quando definido no Cadastro de Produto na pasta de Logística o preenchimento é automático. |
| Bolsa referência | Indica o código da Bolsa de Referência utilizada para buscar a cotação e exibir nos componentes vinculados a bolsa selecionada. |
| Moeda de Faturamento | Indica a moeda utilizada para buscar a cotação para faturamento. Esse campo somente é habilitado para situação de comercialização para Mercado Interno e Moeda Estrangeira definida no Registro de Negócio. |
| Referência | Indica a referência de recebimento. Esse campo somente é habilitado para situação de comercialização para Mercado Interno e Moeda Estrangeira definida no Registro de Negócio.  Os valores aceitos são:  **1 - Faturamento.** Esta opção quando selecionada utilizará a cotação da moeda de faturamento para faturar e gerar a previsão financeira.  **2 - Pagamento.** Esta opção quando selecionada utilizará a cotação da moeda de faturamento para faturar enquanto não houver o pagamento. E a previsão financeira será gerada na cotação futura da moeda de pagamento. |
| Moeda de Pagamento | Indica a moeda utilizada para buscar a cotação para geração da previsão financeira e faturamento após o recebimento. Esse campo somente é habilitado quando a Referência é do tipo 2 - Pagamento. |
| Qtd Dias | Indica a quantidade de dias para considerar na cotação. Exemplo: Se a previsão financeira foi gerada para o dia04/02/2019 e o campo Qtd Dias for informado "2" a cotação a ser considerada será06/02/2019 . Essa situação é válido tanto para a moeda de faturamento como de pagamento. |
