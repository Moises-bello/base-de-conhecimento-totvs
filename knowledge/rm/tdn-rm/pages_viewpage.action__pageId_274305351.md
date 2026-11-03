---
content_hash: 1a79199e47efd54ce9adb5310fe2b1eb6d79701b7eadc65e0743b9dfb1aeb7bd
fetched_at: '2026-06-29T00:08:33.162740+00:00'
page_id: '274305351'
product: rm
source: tdn-rm
title: NFE_Rejeição_696_Operação_com_não_contribuinte_deve_indicar_operação_com_consumidor_final
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274305351
version: 4
---

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 12.1.8 |
| **Ocorrência:** | Rejeição 696 - Operação com não contribuinte deve indicar operação com consumidor final |
| **Passo a passo:** | **Causas:**  Essa rejeição é apresentada quando for emitida uma NF-e para um Destinatário, onde o Indicador de IE (indIEDest) for igual a "9" - Não Contribuinte, e a operação não ocorrer com consumidor final (indFinal diferente de 1).  Veja a regra da SEFAZ:    **Verificações para solução:**  No sistema, o que isto quer dizer ? Deve-se verificar com o cliente qual é a situação cadastral do mesmo junto a receita. Obs: Se o cliente for Pessoa Física é "Não Contribuinte" de ICMS.  Caso o cliente seja Contribuinte de ICMS ou Contribuinte ISENTO, deve-se acessar o cadastro do cliente no sistema, na aba Dados Fiscais | Outros Dados e marcar o campo Contribuinte ICMS como "Contribuinte ICMS" ou "Contribuinte isento de inscri...", de acordo com a situação do cliente informada.  Se o cliente realmente for "não contribuinte" de ICMS, é necessário no movimento de NF-e, na aba Fiscal seja marcado a flag "Consumidor Final".    Fonte:  Nota Técnica 2015/003 (v. 1.90) - <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=pLuHNFf7xvE=> |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
