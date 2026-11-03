---
article_id: 360021601092
category: Materiais - Compras (SIGACOM)
content_hash: 92ea0ec05711ac21dcaf3348d4769a64d958a7c21f209aa38554e3a6e8d2eada
fetched_at: '2026-06-28T22:41:10.388201+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual a funcionalidade
  do processo de Central de Compras (MATA179) ?
type: support-article
updated_at: '2024-02-27T20:23:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021601092-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-funcionalidade-do-processo-de-Central-de-Compras-MATA179
---

**Dúvida**Qual a funcionalidade do processo de Central de Compras (MATA179)?

**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Esta rotina tem duas finalidades:   
  
**Calcular a Necessidade de Reposição do Estoque e a Distribuição do Estoque pela filial centralizadora para as demais filiais.**

Por meio destas funcionalidades é possível:  
• Cada filial realizar seu processo de compras.  
• Distribuir o saldo disponível na filial centralizadora para as demais filiais.  
• A filial centralizadora analisar o estoque e compras das demais filiais.

Após o processamento desta rotina, com base na parametrização selecionada, o sistema apresenta uma tela com a necessidade calculada para compra ou distribuição de produtos. Se necessário, o campo **"Nec Inf"** pode ser alterado manualmente, permitindo a digitação de um valor diferente do calculado pelo sistema.

Ao confirmar esta tela, o sistema pode gerar Solicitação de Compras ou Pedido de Compras nas filiais com necessidade e/ou Pedido de Venda na filial centralizadora, indicando a saída dos produtos comprados para a(s) filial(ais) de destino, de acordo com os parâmetros selecionados

**Requisitos Para utilização da Rotina:**

- Cadastrar Produtos - Tp Sugestão deve ser 1= Normal (MATA010);

- Ter Saldo Inicial na tabela SB2 (MATA220);

- Cadastrar Fornecedores (MATA020)

- Vincular Produto x Fornecedor (MATA061)

- Criar Matriz de Abastecimento (MATA001);

- Preenchimento correto dos parâmetros da Central de Compras:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5040288886679/mceclip3.png)

**Campo Tp Sugestão** (Central de Compras)**:**

Esse Campo podemos escolher entre **"1- Compra"** - Que gerará sugestão de uma nova compra, ou **"2- Transfência"** onde distribuirá o saldo de uma filial para outra. Para saber mais sobre a transferência, [clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5040977401495)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5040106437271/mceclip0.png)

**Previsão de Consumo - Método:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5040073272855/mceclip1.png)

Devemos escolher um dos métodos de cálculo:

**- Média de Vendas:** O cálculo será de acordo com as Vendas realizadas com base nos campos "De - Até"

**- Previsão de Vendas:** Irá avaliar as Previsões de Vendas inclusas na Rotina [MATA700](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=555278384)

**- Demanda Gerada:** O calculo será baseado na Demanda Gerada pela Rotina [MATA295](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053860653-MP-SIGACOM-Como-utilizar-a-rotina-de-Gerar-Demanda-MATA295-) gravadas na tabela SBL

**Obs:**

Para considerar Lote Econômico e valores inteiros, marcar o campo Lote/ Eco.Emb

![CENTRAL.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6653051278999/CENTRAL.png)

**Acesse nossa pagina no YouTube:**

[How To | MP - SIGACOM - Central de Compras - Metodo de Previsão de Vendas](https://youtu.be/c6yl7zgAZu4)

[How To | MP - SIGACOM - Central de Compras - Método Media de Vendas](https://youtu.be/XwfWQ5Rfw8s)

[How To | MP - SIGACOM - Central de Compras - Médodo Demanda Gerada](https://youtu.be/qm8qJEus_YU)

[How To | MP - SIGACOM - Central de Compras - Transferencia entre filiais](https://www.youtube.com/watch?v=xbL8WIt6nhg)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [HELP MTA179PRD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029046751)
* [MATA295](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053860653-MP-SIGACOM-Como-utilizar-a-rotina-de-Gerar-Demanda-MATA295-)
* [MATA700](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=555278384)
* [Como utilizar a transfência entre filiais na Rotina Central de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5040977401495)
