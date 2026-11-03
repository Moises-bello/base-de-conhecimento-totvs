---
content_hash: 71e120d11f877a07c1fb37dc4210256fa6b5bdf23cb8c76bbe1986a97841d9df
fetched_at: '2026-06-29T00:08:33.167868+00:00'
page_id: '274305459'
product: rm
source: tdn-rm
title: NFE_Rejeição_817_Unidade_Tributável_incompatível_com_o_NCM_informado_na_operação_com_Comércio_Exterior_[nItem:nnn]
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274305459
version: 2
---

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 12.1.15 |
| **Ocorrência:** | Rejeição 817 - Unidade Tributável incompatível com o NCM informado na operação com Comércio Exterior [nItem:nnn] |
| **Passo a passo:** | **Causas:**  Essa rejeição é apresentada quando for emitida uma NF-e com Unidade Tributável (uTrib) incompatível com o  NCM (Nomenclatura Comum do Mercosul) informada em Operação de Exportação (tpNF = 1 e idDest = 3) ou com o CFOP igual a 1501, 2501, 5501, 5502, 5504, 5505, 6501, 6502, 6504 ou 6505.  Veja a regra da SEFAZ:    Exemplo de XML com a inconsistência:      De acordo com a Tabela NCM e [Unidades de Medidas Tributáveis no Comércio Exterior](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=iJc0Ir1ISII=), divulgado pela Sefaz, para o NCM 82090011 , deve ser usar para o campo uTrib, a abreviatura KG(Quilograma). Nessa situação, como foi informado Unidade de Medida incompatível com o NCM, a NF-e será rejeitada pelo motivo 817.   **Verificações para solução:**  Para resolver o problema será necessário efetuar o ajuste da tabela de medida ou no NCM do produto.Para o ajuste na tabela de medida gentileza verificar a documentação abaixo: [Nota Técnica 2016/001 - Unidade Tributável no Comércio Exterior](http://tdn.totvs.com/pages/releaseview.action;jsessionid=54BD66633C99B201EBBE2E750E3D8E13?pageId=270900577) Caso deseje alterar o NCM, gentileza acessar o cadastro do produto em:Cadastros | Produtos e Serviços | Selecionar o produto | Detalhes | Outros Dados    Fonte:  Nota Técnica 2016/001 (v. 1.00) - <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=AxGR9dPwVBM=> |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
