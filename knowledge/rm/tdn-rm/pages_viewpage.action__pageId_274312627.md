---
content_hash: c0fca3aa842f991f713393d9c14b76a63f73f81d009350fc37e05a78ba7a8121
fetched_at: '2026-06-29T00:08:33.299634+00:00'
page_id: '274312627'
product: rm
source: tdn-rm
title: NFE_Rejeição_599_CFOP_de_Importação_e_não_informado_dados_de_II.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274312627
version: 1
---

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Rejeição 599 - CFOP de Importação e não informado dados de II |
| **Passo a passo:** | **Causas:**  Essa validação que entrou em vigor com a NT 2011.004 essa rejeição ocorre quando você informa um CFOP de Importação (Iniciado por 3 - Consultar tabela de CFOP) e não informa o grupo do imposto de importação (II).  Veja a regra da SEFAZ:    **Verificações para solução:**  Para resolver o problema será necessário adicionar o tributo II ao item de movimento, gentileza acessar:  Ambiente | Parâmetros | Gestão de estoque, compras e faturamento | Parametrizar o tipo de movimento | Etapa - Fis - Tributação Item |    Ficando disponível no item de movimento:      **Obs: Caso já possua o item de criado no movimento e não esteja apresentando o tributo, será necessário excluir o mesmo e adicionar novamente para que a nova parametrização seja apresentada.**  Fonte:  Nota Técnica 2011/004 - <https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ysYXxjwjYyk=> |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
