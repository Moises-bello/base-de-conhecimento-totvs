---
content_hash: c584ea5c656df51f7240d4326bf085cd48471ef63ef8b08f354ba4e807aa40c1
fetched_at: '2026-06-29T00:06:17.230692+00:00'
page_id: '213975517'
product: rm
source: tdn-rm
title: FIS0002_Nota_Técnica_2015.002_Nota_fiscal_Eletrônica_Complemento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=213975517
version: 18
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 11.82.42.104 ou 12.1.8.110 ou posteriores. |
| **Ocorrência:** | Nota Técnica 2015.002 - Complemento |
| **Ambiente:** | Criação dos campos referente ao Enquadramento de IPI |
| **Passo a passo:** | * Realize o download do pacote **SCRIPT\_NT2015002\_NT2015003\_11\_82.ZIP para a versão 11.82** ou**SCRIPT\_NT2015002\_NT2015003\_12\_1\_8.ZIP para a versão 12.1.8** na central de downloads do cliente e o execute no RM.Script. Execute os scripts do pacote de acordo com o passo a passo:   <http://tdn.totvs.com/display/public/rm/Executor+de+Scripts+RM>   * Para confirmar a criação do campo CODENQIPI na tabela TTRMOV pelo script da NT2015.002 sobre enquadramento do IPI, favor executar o seguinte select no Banco de dados Corpore:   SELECT CODENQIPI,\* FROM TTRBMOV       * O campo será criado na tributação do movimento ou do item de movimento, com o nome "Código de enquadramento IPI". O preenchimento do campo deverá ser efetuado de acordo com a NT2015.002.      1 incomplete     2 incomplete Somente deverá ser preenchido o valor na linha do tributo IPI. No envio da NF-e, a tag do XML preenchida será a <cEnq>.    3 incomplete    4 incomplete    ---    Para criação dos campos de CNPJ/CPF autorizados a visualizar o XML da NF-e no site da SEFAZ, deverão ser criados os devidos campos complementares no movimento.    Os campos deverão ser do tipo Alfanumérico e no tamanho 20.  Poderão ser criados até 5 campos com os nomes (Não é necessário a criação de 05 campos complementares):     | NOME DA COLUNA | DESCRIÇÃO | | --- | --- | | CNPJCPF1 | CNPJ/CPF Para Acesso 1 | | CNPJCPF2 | CNPJ/CPF Para Acesso 2 | | CNPJCPF3 | CNPJ/CPF Para Acesso 3 | | CNPJCPF4 | CNPJ/CPF Para Acesso 4 | | CNPJCPF5 | CNPJ/CPF Para Acesso 5 |        5 incomplete  **Observação:** Serão levados os dados da transportadora quando a mesma possuir CNPJ/CPF igual ao do Cliente/Fornecedor.  Para que os Campos Complementares criados sejam visíveis no movimento, acesse os parâmetros:  Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento.  Acessar o parâmetro do tipo de movimento, na etapa Mov – Campos Complementares e adicione os campos complementares aos campos que serão visíveis:   6 incomplete    7 incomplete    8 incomplete   Lembrando que estes campos seguirão as regras de tamanho e quantidade definidos no manual de orientação do contribuinte.  Preencher os campos no movimento na aba Informações adicionais > Campos complementares:    A tag preenchida no XML será <AutXml> |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |

divs
