---
content_hash: 38b4174a50350030ef186498aa508bedeb218b8ab00082de9d7177fe7c9cdfa9
fetched_at: '2026-06-29T00:08:10.887860+00:00'
page_id: '241699457'
product: rm
source: tdn-rm
title: NFE0023_TAGS_xPed_(numero_do_pedido_de_compra)_e_nItemPed_(item_do_pedido_de_compra)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=241699457
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | 11.52 e 11.82 |
| **Ocorrência:** | Gerar as tags xPed (numero do pedido de compra) e nItemPed (item do pedido de compra) |
| **Passo a passo:** | **Introdução:**  No layout da NF-e 2.00 foram criados dois campos para as empresas que desejam informar na Nota o número e item do pedido de compra. Este campo é opcional e para levado no XML basta seguir este procedimento.  **1º Passo:** Criar dois campos complementares no produto **ou no item de movimento**:  É necessário criar dois campos complementares do tipo texto no produto com os nomes XPED e NITEMPED  *****Acesse o RM Nucleus no seguinte menu: Cadastros / Campos Complementares / Produtos*******ou  ***Cadastros / Campos Complementares / Itens de Movimentos.*****    Procedimento para criação dos dois Campos Complementares:  Clique na opção “Novo” (Incluir), em “Nome da Coluna” preencha “XPED” em “Descrição” preencha “XPED”. Clique em “Salvar”.    Para incluir o segundo, clique novamente em “Novo” (Incluir), em “Nome da Coluna” preencha “NITEMPED” em “Descrição” preencha “NITEMPED” e clique em “Salvar”.    **Parametrização no produto**: no cadastro de Produtos aba “Campos complementares” existem estes dois campos e sempre que estiverem preenchidos serão levados no XML da Nota.    **Parametrização do item de movimento**:  Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Outras Movimentações/Vendas/Compras (dependendo da classificação do tipo movimento desejado) | Selecione o Tipo de movimento e clique em Parametrizar:  **Etapa "item - campos complementares**: inclua os campos criados.    **OBS:** O Preenchimento destes campos (tamanho mínimo e máximo) deve seguir as regras do manual de integração 5.00 que define a NF-e 2.00  Essa documentação não se aplica na versão 12, pois os campos estão nativos na base nesta versão. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
