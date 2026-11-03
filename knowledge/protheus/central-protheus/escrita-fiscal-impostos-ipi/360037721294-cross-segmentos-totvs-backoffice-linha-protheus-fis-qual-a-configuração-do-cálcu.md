---
article_id: 360037721294
category: Escrita Fiscal - Impostos - IPI
content_hash: f154c38ac06679db25fcf7a514e833ddba8ebfb8b5fb81ed38d9feae3963dc37
fetched_at: '2026-06-28T22:39:29.042343+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Qual a configuração
  do cálculo do IPI Majorado para as notas fiscais de transferência de mercadoria?
type: support-article
updated_at: '2022-01-13T19:59:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037721294-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-a-configura%C3%A7%C3%A3o-do-c%C3%A1lculo-do-IPI-Majorado-para-as-notas-fiscais-de-transfer%C3%AAncia-de-mercadoria
---

**Dúvida**Qual a configuração do cálculo do IPI Majorado para as notas fiscais de transferência de mercadoria?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Configurar o Parâmetro: MV\_PBIPITR (Informar o  percentual de IPI para as notas de transferência de mercadoria)

**TES:**

Calcula IPI (F4\_IPI)= SIM

Livro Fiscal IPI (F4\_LFIPI) = diferente de não

Trans Filial (F4\_TRANFIL)= Sim

**Produto:**

Preencher a  alíquota do IPI no campo Aliq.IPI (B1\_IPI)

**Procedimentos:**

1º Incluir um pedido de venda e informar a tabela de preço do produto no campo Tabela Trf.(C5\_TABTRF).

2º O preço de vendas desta tabela deverá estar atribuído ao novo campo do item do pedido de vendas (C6\_IPITRF – IPI Transf.).

Ao verificar na Planilha Financeira do Pedido de Venda (MATA410), o sistema deve calcular a base do IPI considerando o percentual informado no parâmetro MV\_PBIPITR.

**Exemplo:**

*MV\_PBIPITR=90*

*Valor do produto na Tabela de Preço 150,00*

*Base calculo do IPI 135,00 (150\*90% calcula a base do IPI considerando o percentual informado no parâmetro MV\_PBIPITR)*

*Valor do IPI  20,25 (Alíquota 15%)*

*Total da NF de transferência (Produto + IPI)=170,25*

Planilha Financeira do Pedido de Venda(MATA410)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419028303639/mceclip0.png)

Informações Adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=254607623>

<https://tdn.totvs.com/pages/releaseview.action?pageId=518481843>

<https://tdn.totvs.com/pages/releaseview.action?pageId=361448653>
