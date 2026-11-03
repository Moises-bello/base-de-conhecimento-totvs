---
content_hash: a7fc7338a66a1c0da69ef24bd589a83237c86b02bc227ae75974d4f5f4f40384
fetched_at: '2026-06-29T00:08:35.413648+00:00'
page_id: '280734193'
product: rm
source: tdn-rm
title: NFE_Rejeição_699_Percentual_do_ICMS_Interestadual_para_a_UF_de_destino_difere_do_previsto_para_o_ano_da_Data_de_Emissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=280734193
version: 2
---

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 12.1.13 |
| **Ocorrência:** | Rejeição 699 - Percentual do ICMS Interestadual para a UF de destino difere do previsto para o ano da Data de Emissão |
| **Passo a passo:** | **Causas:**  A rejeição 699 – “Percentual do ICMS Interestadual para a UF de destino difere do previsto para o ano da Data de Emissão” faz parte das validações da Nota Técnica (NT) 2015/003 com entrada em vigor em 01/01/2016.  A partir desta data, serão geradas no XML da nota as tags referentes ao ICMS interestadual nas operações de venda para consumidor final não contribuinte de ICMS, atendendo ao disposto na Emenda Constitucional (EC) 87 de 2015.  Para resolver a rejeição, será necessário verificar no XML da nota qual informação está sendo gerada na tag pICMSInterpart do grupo abaixo:  <ICMSUFDest>  <vBCUFDest>1000.00</vBCUFDest>  <pFCPUFDest>0.0000</pFCPUFDest>  <pICMSUFDest>18.0000</pICMSUFDest>  <pICMSInter>12.00</pICMSInter>  <pICMSInterPart>40.0000</pICMSInterPart>  <vFCPUFDest>00.00</vFCPUFDest>  <vICMSUFDest>24.00</vICMSUFDest>  <vICMSUFRemet>36.00</vICMSUFRemet> </ICMSUFDest>  **Verificações para solução:**  Para resolver o problema será necessário a verificação da tabela abaixo:    Após acessar o cadastro da CFOP para alteração deste valor conforme o ano de emissão em:  Cadastros | Natureza Fiscal | Selecionar a CFOP Utilizada | Aba - Tributação ICMS/IPI | Regra de ICMS | Aba Dados ICMS S.T | Campo % ICMS UF Destinatário                            Fonte:   Nota Técnica 2015.003 v.1.60 - <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=zJGzcwysHPo=> |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
