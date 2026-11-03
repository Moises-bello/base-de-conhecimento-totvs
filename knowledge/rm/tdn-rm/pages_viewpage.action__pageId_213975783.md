---
content_hash: 9c91a60fdceb876dfc0635f651290c4715f47edcd05832a841f880f5a5c6f729
fetched_at: '2026-06-29T00:06:17.236400+00:00'
page_id: '213975783'
product: rm
source: tdn-rm
title: FIS0001_Nota_Técnica_2015.002_Nota_fiscal_Eletrônica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=213975783
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 11.82.42.104 ou 12.1.8.110 ou posteriores. |
| **Ocorrência:** | Nota Técnica 2015.002 |
| **Ambiente:** | A nova Nota Técnica NT 2015.002, tem como um dos objetivos aprimorar a qualidade de informações referentes à NFC-e e NF-e. |
| **Passo a passo:** | **Nota Técnica 2015.002 – Nota Fiscal Eletrônica**  A nova Nota Técnica NT 2015.002, tem como um dos objetivos aprimorar a qualidade de informações referentes à NFC-e e NF-e.  Destacamos algumas mudanças significativas da nova NT que irão impactar diretamente no dia a dia dos contribuintes. Confira:   * Mudanças para NFe * Enquadramento Legal: IPI   O código deverá ser obrigatoriamente informado para operações referentes a Isenção, Suspenção ou Imunidade, caso contrário será gerado com o valor “999-Outros”.  Código deve constar na lista do Anexo XIV – Código de Enquadramento Legal do IPI da NT 2015/002.  Validação da Sefaz será a seguinte:  Para os CSTs 02 e 52 – Isento de IPI, o Código de enquadramento deve ser entre 301 e 399  Para os CSTs 04 e 54 – Imune de IPI, o Código de enquadramento deve ser entre 001 e 099  Para os CSTs 05 e 55 – Suspenso de IPI, o Código de enquadramento deve ser entre 101 e199   * Regras de Validação Diversas   A partir desta NT será verificado se o NCM informado no item da Nota Fiscal existe na tabela de NCM publicada pelo Ministério do Desenvolvimento (MDIC). Foram alteradas também diversas regras de validação, melhorando a qualidade da informação recebida, afetando, principalmente, os sistemas das SEFAZ Autorizadoras.   * Autoriza Download XML – Criamos o CNPJ   Atualmente na Consulta Pública da NF-e tanto o destinatário, quanto o próprio emitente, podem efetuar o download do XML da NF-e, desde que identificados com seu certificado digital (conforme critério da SEFAZ). Idem para o Transportador citado na NF-e. Criado um novo grupo de informações para que a empresa emitente possa indicar outras pessoas autorizadas a obter o download do arquivo XML da NF-e. Nesta alternativa, a empresa emitente poderá indicar o seu Contador, outras pessoas envolvidas no transporte da mercadoria, etc   * Mudanças para NFCe * NFC-e: Utilização na operação de venda de combustível   Utilização da NFC-e para representar a operação de venda de combustível para consumidor final, efetuada por Posto Revendedor de Combustíveis.   * NFC-e: Formas de Pagamento   Alterado o grupo de informações sobre o pagamento da NFC-e por cartão de crédito / débito, incluindo a informação do tipo de integração do processo de pagamento com o sistema interno da empresa. Foram estabelecidas novas regras de validação nesta área.  É importante que você saiba que:   * O prazo previsto para a implementação pela SEFAZ é: Ambiente de Homologação: 01/10/15. Ambiente de Produção: 01/12/15. * Para a geração é necessário estar na versão de BibliotecaRM  11.82.42.104 ou 12.1.8.110 ou posteriores e TSS 2.52. * Além disso, é necessário a execução do pacote **SCRIPT\_NT2015002\_NT2015003\_11\_82.ZIP para a versão 11.82** ou**SCRIPT\_NT2015002\_NT2015003\_12\_1\_8.ZIP para a versão 12.1.8** * A documentação necessária para parametrização e preenchimento das informações destacadas acima estão disponíveis no TDN através do Link: <http://tdn.totvs.com/pages/releaseview.action?pageId=213975517>   * Para mais informações acesse nosso Wiki Help através do Link: <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.SituacoesComplementaresNFe.aspx> * Acesse nossa comunidade tire suas dúvidas, através do link: <http://fluig.totvs.com/portal/p/10097/subject/rnfe> |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |

divs
