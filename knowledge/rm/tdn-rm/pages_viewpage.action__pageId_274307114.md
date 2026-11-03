---
content_hash: 57ca2e68843ba4586f7e8bc612c5c81e0be52c16c5ab6fae4f777c81b5a21683
fetched_at: '2026-06-29T00:08:33.195204+00:00'
page_id: '274307114'
product: rm
source: tdn-rm
title: NFE0034_Valor_do_ICMS_desonerado_(vICMSDeson)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274307114
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 12.1.21 |
| **Ocorrência:** | Desoneração de ICMS |
| **Passo a passo:** | **Introdução:**  Este documento tem como finalidade auxiliar na parametrização do sistema, quando o ICMS for desonerado.  Os Códigos de Situação Tributária que indicam benefícios fiscais do ICMS sujeitos à desoneração são os abaixo relacionados :   * + 20 - Com redução de base de cálculo   + 30 - Isenta ou não tributada e com cobrança do ICMS por substituição tributária   + 40 - Isenta   + 70 - Com redução de base de cálculo e cobrança do ICMS por substituição tributária   + 90 - Outras   Nestes casos, além do preenchimento das tags descritas no layout da NF para os grupos "ICMS20", "ICMS30", "ICMS40", "ICMS70" ou "ICMS90", também devem ser preenchidas as tags :   * + **"vICMSDeson" -**Valor do ICMS desonerado   + **"motDesICMS"** - Motivo da desoneração do ICMS * **Criando uma NF-e com Desoneração de ICMS no sistema:** * Cadastro da CFOP: * No sistema Gestão de estoque, compras e faturamento, menu de cadastros, parte fiscais clicar em "Natureza Fiscal". * Selecionar a natureza que deseja parametrizar para desoneração e clicar no ícone Editar. * Na aba Tributação ICMS/IPI da Natureza editar a regra de ICMS. * Dentro da regra de ICMS, na aba Dados ICMS marcar a flag "ICMS Desonerado" e preencher o "Motivo de desoneração de ICMS".  * **IMPORTANTE:** Caso tenha redução da base do ICMS desonerado basta informar no campo "Redução Base ICMS (%)". * Atualmente os motivos de desoneração de acordo com o Manual de Orientação do Contribuinte da SEFAZ são: * 1 - Táxi 2 - Deficiente Físico 3 - Produtor Agropecuário 4 - Frotista/Locadora 5 - Diplomático/Consular 6 - Utilitários e Motocicletas da Amazônia Ocidental e Áreas de Livre Comércio (Resolução 714/88 e 790/94 – CONTRAN e suas alterações) 7 - SUFRAMA 8 - Venda a Órgão Público 9 - Outros. (NT 2011/004) 10 - Deficiente Condutor (Convênio ICMS 38/12) 11 - Deficiente Não Condutor (Convênio ICMS 38/12) 12 - Órgão de fomento e desenvolvimento agropecuário  Criando o movimento: * Ao criar o movimento de NF-e, informar a CFOP de desoneração de ICMS criada na aba Fiscal do item de movimento. * No menu Tributos e Valores, aba Tributos (Item), automaticamente o sistema preenche o motivo de desoneração de ICMS definido na Natureza Fiscal e o valor do ICMS calculado (Base de calculo \* Alíquota - Redução) como ICMS Desonerado.   Grupo de ICMS no XML gerado do exemplo:    Grupo de totalizadores no XML gerado do exemplo:      A partir do layout 4.0 da NF-e , faz se necessário a subtração do valor do ICMS Desonerado do valor da nota. Segue link para auxilio da criação da formula: |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
