---
article_id: 360029046751
category: Materiais - Compras (SIGACOM)
content_hash: fc62a94853228301f4def2fdf3cd802858bb083b6e130b4fafa44e2749694131
fetched_at: '2026-06-28T22:41:24.073963+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Principais Motivos
  para o Help MTA179PRD (Central de Compras)
type: support-article
updated_at: '2024-11-12T11:38:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029046751-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Principais-Motivos-para-o-Help-MTA179PRD-Central-de-Compras
---

**Dúvida**

Principais Motivos para o Help MTA179PRD ao executar a rotina Central de Compras (MATA179):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029885031)

**Ambiente**Protheus – Compras – A partir da versão 11.80

**Solução**

Abaixo vamos listar os Principais Motivos para o HELP MTA179PRD ao executar a rotina Central de Compras (MATA179):

- Verificar campo Tip Sugestão no cadastro de Produtos (Deve estar 1 = Normal) - **Item Importante**

- Verificar se existem registros criados para os produtos na rotina Saldo Inicial - MATA220 (Tabela SB2) **- Item Importante**

- Verificar se existem amarração de Produto x Fornecedor na rotina MATA161 **- Item Importante**

- Verificar se existe configuração de grupo de compras, realize um teste desabilitando o parâmetro **MV\_RESTCOM**, para mais informações [clique aqui](https://tdn.engpro.totvs.com.br/display/public/PROT/6+-+Grupo+de+Compras) - **Item Importante**

- Verificar a criação da Matriz de Abastecimento ([MATA001](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=312156856)) - **Item Importante**

- Verificar os parâmetros informações na Central de Compras (MATA179) **- Item Importante**

- Verificar o saldo atual do produto, pode ser visualizado no browse do cadastro, ou através do relatório Kardex - Matr900.

- Caso esteja utilizando o campo **Tp Sugestão = Transferência**, revise as configurações [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5040977401495)

Conheça sobre a Rotina **MATA179** [clicando aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021601092)

- Caso o campo de descrição do produto **B1\_DESCRI** seja diferente do campo **DBI\_DESCPR**, a Central de Compras não será gerada.

**Para saber mais sobre Central de Compras acesse nossa pagina no YouTube:**

[How To | MP - SIGACOM - Central de Compras - Metodo de Previsão de Vendas](https://youtu.be/c6yl7zgAZu4)

[How To | MP - SIGACOM - Central de Compras - Método Media de Vendas](https://youtu.be/XwfWQ5Rfw8s)

[How To | MP - SIGACOM - Central de Compras - Médodo Demanda Gerada](https://youtu.be/qm8qJEus_YU)

[How To | MP - SIGACOM - Central de Compras - Transferencia entre filiais](https://www.youtube.com/watch?v=xbL8WIt6nhg)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
