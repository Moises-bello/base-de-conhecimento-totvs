---
content_hash: aaf3d43272f93d496afd4bdd619aef2ef0eb76c0bf9f76abf50dc574d039a2f7
fetched_at: '2026-06-29T00:08:33.886985+00:00'
page_id: '274332247'
product: rm
source: tdn-rm
title: NFE_Rejeição_697_Alíquota_interestadual_do_ICMS_com_origem_diferente_do_previsto.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274332247
version: 1
---

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 12.1.8 |
| **Ocorrência:** | Rejeição 697 - Alíquota interestadual do ICMS com origem diferente do previsto |
| **Passo a passo:** | **Causas:**  Essa rejeição é apresentada quando for emitida uma NF-e com o valor do campo pICMSInter=4.00  (4.00% de Alíquota) e a Origem da Mercadoria(orig) for:   * + 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8;   + 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes;   + 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%;   + 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural;   + 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural.  **Ou**   Se emitida uma NFe com o valor do campo pICMSInter=7.00 (7.00% de Alíquota) e a Origem da Mercadoria(orig) for:   * + 1 - Estrangeira - Importação direta, exceto a indicada no código 6; ou   + 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; ou   + 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%; ou   + 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%.   Veja a regra da SEFAZ:    **Verificações para solução:**  A duas formas de corrigir o problema onde é necessário verificar com o setor fiscal qual a ser realizada:  **Alterar a alíquota no cadastro da CFOP:**  Cadastros | Natureza de Operação (CFOP) | Editar a Natureza utilizada | Aba Tributação ICMS/IPI | Regra de ICMS | Dados ICMS    Ajustar para alíquota correta conforme tabela abaixo:    **Ou**  **Alterar a origem da mercadoria:**  Cadastros | Produtos e Serviços | Aba Detalhes | Outros Dados    Também pode ser efetuado a alteração direto no item de movimento:      Fonte:  Nota Técnica 2015/003 (v. 1.90) - <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=pLuHNFf7xvE=> |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
