---
content_hash: d4a7b7e4a93966a2fe46a2fe2a2c85ca08b21e2c6fdbf129e7b0d776613d57d7
fetched_at: '2026-06-29T00:08:33.206151+00:00'
page_id: '274308900'
product: rm
source: tdn-rm
title: NFE_Rejeição_328_CFOP_de_devolução_de_mercadoria_para_NF-e_que_não_tem_finalidade_de_devolução_de_mercadoria.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274308900
version: 2
---

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 11.82.45 |
| **Ocorrência:** | Rejeição 328: CFOP de devolução de mercadoria para NF-e que não tem finalidade de devolução de mercadoria. |
| **Passo a passo:** | **Causas:**  Com a utilização do layout 3.10 é preciso se atentar que quando a nota for emitida com um dos CFOP's relacionados na NT 2013/005 como CFOP de devolução, a nota deverá ser enviada como finalidade '4 - Devolução de mercadoria'.  Veja a regra da SEFAZ:    **Verificações para solução:**  Deve-se verificar a CFOP de devolução de mercadoria contida na [NT2013.005](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y8Fq5xEqz7M=) a partir da página 129.  Caso a NF-e seja de devolução, acessar o cadastro da CFOP em:  Cadastros | Natureza Fiscal | Selecionar a Natureza utilizada | Aba Outros Dados | Em Tipo de Devolução | Marcar a opção "Devolução"      Caso a NF-e não seja de devolução, será necessário efetuar a alteração para outra CFOP que não esteja na lista citada acima.  Fonte:  Nota Técnica 2013.005 (v1.21) - <https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y8Fq5xEqz7M=> |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
