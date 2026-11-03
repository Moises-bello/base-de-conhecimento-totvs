---
content_hash: 14cb5cb4a03b2752461b8170fde2284d7c93fc3b3261b25de03bf232398993f2
fetched_at: '2026-06-29T00:06:13.138016+00:00'
page_id: '208339993'
product: rm
source: tdn-rm
title: DT_Melhorias na Importação /Exportação de Movimentos e Produtos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=208339993
version: 3
---

# MELHORIAS NOS PROCESSOS DE IMPORTAÇÃO / EXPORTAÇÃO VIA TBC

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Importação /Exportação via TBC |  |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Movimento | Cadastro de Movimentos | | Produto | Cadastro de Produtos | |
| **Cadastros Iniciais:** | Conceito / Lauyout de Exportação |
| **Parâmetro(s):** | N/A |
| **Requisito (ISSUE):** | * [PCREQ-7757](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-7757 "PCREQ-7757") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas utilizadas:** | * TMOV – Movimento * TMOVCOMPL – Campos Complementares do Movimento * TMOVRELAC – Relacionamento entre Movimentos * TITMMOV – Item de Movimento * TITMMOVCOMPL – Campos Complementares do Item de Movimento * TITMMOVGRD – Itens do Movimento por Grade * TITMLOTEPRD – Lotes do Item de Movimento * TITMNUMSERIEPRD – Números de serie dos itens movimentados * TITMMOVRELAC – Relacionamentos entre Itens de Movimento * TTRBMOV – Tributos por Movimento * TMOVPAGTO – Pagamentos por movimento * TCTRC – Notas Fiscais Conhec.Transporte * DCTRC – Itens de CTRC * TITMMOVRATCCU – Itens de Rateio por Centro de Custo * TITMMOVRATDEP – Itens de Rateio por Departamento * TMOVRATCCU – Rateios por Centro de Custo * TMOVRATDEP – Rateios por Departamento * TMOVHISTORICO – Histórico do Movimento * TITMMOVHISTORICO – Histórico do Item de Movimento * TNFTERCEIROS – Notas Fiscais de Terceiros * TMOVFISCAL – Dados Fiscais do Movimento * TITMMOVFISCAL – Dados Fiscais do Item de Movimento * TMOVDISPOSITIVO – Numeração Dos Disp. Impressos |
| **Sistema(s) operacional(is):** | Windows 7 SP1 ou superior. |
| **Versões/Release:** | 12.1.8 |

## Descrição

Implementar as melhorias identificadas nos arquivos de conceito de Importação / Exportação de Movimentos e  Importação / Exportação de produtos liberados na 12.1.4.

## Procedimento para Implantação

**Exportação de movimentos**

 Para Realizar a exportação dos movimentos utiliza-se o gerador de Saídas. Neste caso deve-se primeiro ter importado o layout de exportação disponibilizado na pasta de objetos gerenciais.

 - Para Acessar o Gerador de Saídas, acesse primeiro o Módulo Integrações, e navegue para a aba Integrações | Gerador de Saídas | Layouts.

 - Na visão da tela do Gerador de Saídas, selecione a opção **Processos | Importar Layout**. Selecione o arquivo de layout disponível na pasta de objetos gerenciais e informe um nome e a categoria para a importação.

 - Após a importação selecione o layout na visão e execute o processo em **Processos | Geração de Saídas**

 - Após a conclusão do processo o arquivo com os movimentos selecionados estará disponível em : C:\totvs\CorporeRM\RM.Net\Saídas (Caso o sistema esteja instalado na pasta default do sistema).

**Importação de movimentos**

 Para realizar a importação de movimentos, é necessário antes, importar o layout de importação através da ferramenta Conceito, que compõe o TOTVS Business Conector (TBC).

Neste caso deve-se primeiro ter importado o layout de importação disponibilizado na pasta de objetos gerenciais.

 - Para Acessar o Conceito, primeiro acesse o modulo Integrações, e navegue para a aba **Integrações | Conceito**.

 - Na visão da tela do Conceito, selecione a opção **Processos | Importar de Conceito**. Selecione o arquivo de conceito disponível na pasta de objetos gerenciais e informe o nome para a importação.

 - Após a importação selecione o conceito na visão e execute o processo em **Processos | Processar novo conceito** selecionando o arquivodesejado no mesmo formato do layout de exportação

 - Após a conclusão do processo os movimentos informados no arquivo de importação estarão atualizada no sistema.

## Procedimento para Utilização

As melhorias realizadas nos arquivos de importação / Exportação foram realizadas conforme a descrição abaixo:

 

1. As informações sobre a formatação padrão dos campos contidos nos arquivos para importação será a mesma definida para a exportação podendo ser verificada através da edição do Gerador de Saídas pela opção “Gerar Documentação”.  Por exemplo como deve ser feito o preenchimento dos campos quando a informação não ocupar todo o espaço a ela reservado por tipo de campo ou preencher com 0(zeros) a esquerda para campos do tipo INT.
2. A exportação / importação da contabilidade do movimento foi disponibilizado na versão release 12.1.6 podendo ser utilizada em qualquer versão dos layouts de Importação/Exportação.
3. Os arquivos de Conceito foram atualizados para que o parâmetro antes denominado “Cliente/Fornecedor identificado pelo CGCCFO” seja o seguinte: “Cliente/Fornecedor identificado pelo CNPJ/CPF”.
4. O campo DTCADASTRO, da tabela TPRDCODIGO nos layouts de exportação de produtos não será importado, sendo este desconsiderado na importação mesmo que estiver informado no arquivo, pois o mesmo é setado automaticamente com a data do sistema na inclusão. Na exportação não haverá alterações e o campo ainda será exportado mantendo assim o legado no layout.

divs
