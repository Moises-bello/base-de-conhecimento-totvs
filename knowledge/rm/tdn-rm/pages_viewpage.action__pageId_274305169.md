---
content_hash: 06a3529c677993b4609e989e0e53386708a521dc1d54b60e5b23cd466b118367
fetched_at: '2026-06-29T00:08:33.136967+00:00'
page_id: '274305169'
product: rm
source: tdn-rm
title: NFE_Rejeição_694_Não_informado_o_grupo_de_ICMS_para_a_UF_de_Destino.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274305169
version: 3
---

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 12.1.8 |
| **Ocorrência:** | Rejeição 694 – Não informado o grupo de ICMS para a UF de Destino. |
| **Passo a passo:** | **Causas:**  Validações da SEFAZ que entrou em vigor em 01/07/2016:  - Operação Interestadual (idDest=2) e - Operação com Consumidor Final (indFinal=1) e - Operação com Não Contribuinte (indIEDest=9)  Veja a regra da SEFAZ:      **Verificações para solução:**  1 - Caso  Deverá ser verificado com o setor fiscal:  # A operação é para Consumidor Final?  # O destinatário é não contribuinte?  Caso o mesmo seja consumidor final e não contribuinte de ICMS será necessário parametrizar o sistema para geração da partilha de ICMS conforme a documentação abaixo:    2 - Caso  # A operação é para Consumidor Final? # O destinatário é não contribuinte?  Caso o mesmo não seja Consumidor Final é necessário desmarcar a flag "Consumidor Final" na aba integrações | fiscal Para verificação do cadastro do destinatário é necessário a verificação do cadastro do mesmo no SINTEGRA :  <http://www.sintegra.gov.br/>  Após a verificação do cadastro do contribuinte, gentileza acessar o cadastro do cli/for, aba Dados Fiscais | Outros dados | no campo “Contribuinte ICMS” marque uma das opções abaixo conforme o cadastro “Contribuinte Isento” ; “Contribuinte ICMS” ; “Não Contribuinte ”.  Faça o envio da nota novamente para correta autorização.    Fonte:  Nota Técnica 2015/003 (v. 1.90) - <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=pLuHNFf7xvE=> |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
