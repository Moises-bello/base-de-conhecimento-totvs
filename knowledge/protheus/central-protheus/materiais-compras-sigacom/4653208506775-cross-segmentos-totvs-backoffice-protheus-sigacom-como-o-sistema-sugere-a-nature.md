---
article_id: 4653208506775
category: Materiais - Compras (SIGACOM)
content_hash: e209901b2ac041f1307ced778c498adb6452a6635e45324951c744d12ad4e34d
fetched_at: '2026-06-28T22:41:15.987934+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como o sistema sugere
  a natureza no documento de entrada do tipo D (Devolução)
type: support-article
updated_at: '2024-03-27T19:28:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4653208506775-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-o-sistema-sugere-a-natureza-no-documento-de-entrada-do-tipo-D-Devolu%C3%A7%C3%A3o
---

**Dúvida**Como o sistema sugere a natureza no Documento de Entrada do tipo D (Devolução)?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões

**Solução**Por padrão, o sistema verifica dois parâmetros que atuam em conjunto com relação ao preenchimento da variável **cNatureza** cuja informação será gravada no campo **E1\_NATUREZ**, em uma nota de entrada do tipo D ( devolução de vendas ), onde se o TES estiver configurado com o campo gera financeiro = Sim, para que seja gerado um título tipo NCC para o cliente que efetuou a devolução. São eles :

[MV\_NFENAT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022043091-MP-SIGACOM-Como-deixar-o-campo-Natureza-CNATUREZA-na-aba-Duplicatas-obrigat%C3%B3rio-ao-inserir-uma-Nota-Fiscal-de-Entrada-)

[MV\_1DUPNAT](https://tdn.totvs.com/display/PROT/DOC0021_Natureza_no_Pedido_de_Vendas)

Para que o conteúdo do parâmetro MV\_1DUPNAT seja verificado é necessário que o parâmetro MV\_NFENAT esteja com conteúdo T, ou seja, habilitado.

Por exemplo : Conteúdo do **MV\_1DUPNAT** = SC5->C5\_NATUREZ e **MV\_NFENAT** = T, no momento da entrada da nota tipo D para preenchimento da variável **cNATUREZ** o sistema verificará a natureza usada no cabeçalho do pedido de vendas e a carregará, e, por consequência será essa a informação gravada no campo **E1\_NATUREZ** do título tipo NCC que será gerado, se o **TES da devolução** estiver com o campo **Gera financeiro = Sim**.

***Saiba Mais :***

*[PÁGINA CENTRALIZADORA DO COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)*

*[Mais Artigo Materiais - COMPRAS ( SIGACOM )](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)*
