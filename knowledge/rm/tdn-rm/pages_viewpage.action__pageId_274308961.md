---
content_hash: 76e1e2de1b28454fe26a7739d6ee2621d79b34014801c281379c372918ccc26f
fetched_at: '2026-06-29T00:08:33.210678+00:00'
page_id: '274308961'
product: rm
source: tdn-rm
title: NFE_Rejeição_321_NF-e_de_devolução_de_mercadoria_não_possui_documento_fiscal_referenciado.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274308961
version: 8
---

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 11.82.45 |
| **Ocorrência:** | Rejeição 321: NF-e de devolução de mercadoria não possui documento fiscal referenciado |
| **Passo a passo:** | **Causas:**   NF-e com Finalidade (finNFe) igual à "4 - Devolução de mercadoria" e não for informado documento referenciado (NFref ), trecho do XML com a inconsistência:      Veja a regra da SEFAZ:      **Verificações para solução:**  Deve-se informar o documento referenciado (NF-e, NFC-e, NF modelo 1, NF Produto ou ECF) na NF-e. Para toda NF-e com finalidade "4 - Devolução de mercadoria" é necessário que seja informado o documento fiscal que está sendo devolvido, para isso basta necessário seguir a documentação abaixo:    **IMPORTANTE:** Caso seja uma devolução de compra/entrada, o movimento de entrada do produto (Nota que será referenciada) deve estar parametrizada conforme o documento abaixo e com a chave de acesso preenchida corretamente.      Fonte:  Manual de Orientação ao Contribuinte - <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=9hd38oni4Nc=> |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
