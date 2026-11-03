---
content_hash: 04619c21438532abe0a414a0785707c1b945d31d135ffb386ae07c58b4fea4ad
fetched_at: '2026-06-29T00:05:57.856768+00:00'
page_id: '184780837'
product: rm
source: tdn-rm
title: INOVAR - Auto Declaração de Vendas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=184780837
version: 20
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.82.3x\12.1.x |
| **Processo** | **:** | Inovar - Auto Declaração de Vendas |
| **Subprocesso** | **:** | Geração da rotina |
| **Data da publicação** | **:** | 03/02/2014 |

**Inovar-Auto**

O Programa de Incentivo à Inovação Tecnológica e Adensamento da Cadeia Produtiva de Veículos Automotores (Inovar-Auto) é o regime automotivo do Governo Brasileiro que tem como objetivo a criação de condições para o aumento de competitividade no setor automotivo, produzir veículos mais econômicos e seguros, investir na cadeia de fornecedores, em engenharia, tecnologia industrial básica, pesquisa e desenvolvimento e capacitação de fornecedores. Criado pela Lei n 12.715/2012, o programa possui validade para o período de 2013 a 2017.

**Parametrização**

**TOTVS Gestão Financeira**

Primeiramente, é necessário criar um campo complementar para o cadastro de Cliente/Fornecedor, para posterior preenchimento, de todos que irão participar do programa.

**Nome da Coluna**: INOVAR\_AUTO                                                     **Tipo**: Inteiro

**Obs**.: Obrigatoriamente, este deve ser o nome do campo.                 **Valor**: 0 = Não / 1 = Sim

 Informativo: Na conversão para o ambiente da 12.1.4, este campo será criado na base e preenchido automaticamente com os valor informado no campo complementar.

**TOTVS Gestão de Estoque, Compras  e Faturamento**

  Para o cálculo da parcela Dedutível, será verificado os Movimentos de Entrada e Insumos utilizados  na produção dos produtos vendidos para as montadoras. **Obs**.: Este cálculo somente será realizado, quando houver integração com o Gestão Fiscal.

  PORTARIA 257, DE 23 DE SETEMBRO DE 2014 ANEXO III

    Item Pai: será gerado com o item da nota fiscal de venda para montadora (cliente cujo o Campo Complementar “INOVAR\_AUTO”, citado acima, estiver preenchido com “1” - Sim).

    Itens Filhos (Insumos): São os itens que compõe o “item pai”. Será selecionados os movimentos de compra desses itens associados ao “Item Pai” no processo de produção.

**Obs**.: Caso não encontre movimentos de entrada no período da geração, serão selecionados movimentos dentro do próprio período da geração. As Notas Fiscais de Devolução devem descontar no valor Total das Notas Fiscais do Cliente. Serão tratadas apenas notas de devolução referentes ao mês de geração da Rotina, caso a Devolução seja maior que o valor de Venda, será informado 0 para este item.

**Demonstração dos cálculos – Memória de Cálculo**

    O cálculo da parcela dedutível será realizado mensalmente para todos os itens das Nota Fiscais de Venda do mês informado na Tela de Geração da Rotina. Considera os componentes (insumos) dos itens vendidos e verifica as notas fiscais de compra, importação e/ou devolução do mês mais recente do período processado. Depois dessa verificação o sistema realizará uma média da parcela dedutível, somando o valor total sem IPI de cada insumo no período de processamento e dividindo pela quantidade total de cada insumo. Para então multiplicar o valor dessa divisão pela quantidade necessária do componente e obter o valor da parcela.

-1
incomplete


139
incomplete
 Na Tela de Geração da Rotina será possível gerar um arquivo de Log. Onde será demonstrado a Memória de Cálculo dos Valores gerados no Arquivo XML.

140
incomplete
 A geração do log será solicitada pelo usuário, na tela de execução do processo.

141
incomplete
 Dependendo da quantidade de produtos que terá a Parcela Dedutível calculada automaticamente e o volume de movimentações na base, a execução desse log poderá comprometer a performance do processo.

142
incomplete
 Encontrado insumo na NF de entrada do período, busca todas as NFs do período para calcular o preço médio da parcela dedutível;

143
incomplete
 Considera regras de CST, Classificação Fiscal e Imposto Importação.

     Observação: Quando a Nota Fiscal não apresentar o Código CST, considerar sempre CST 2.

-1
incomplete


144
incomplete
    Calcula a parcela dedutível média no período para o insumo (subtrai devoluções de entrada)

145
incomplete
    Parcela Dedutível Média = (total(Parcela Dedutível Unitária)/total(Quantidade)) \* Qtde Usada

**Exemplo do Cálculo**

**TOTVS Gestão Fiscal**

Detalhes da Parametrização do Processo

**Obs**.:  Na versão 11.82.3x este menu será exibido apenas quando o campo Complementar **INOVAR\_AUTO** existir no cadastro de Cliente/Fornecedor.

Tela do processo onde o usuário vai informar os Parâmetros para a geração do Arquivo.

Caso não trabalhe com o controle de Produção do RM Nucleus/Factor, terá a opção de informar a parcela dedutível **por cliente** que será impressa no arquivo. **Obs**.: Caso esta informação esteja preenchida o sistema vai utilizar este valor e não o fazer o cálculo como proposto acima.

O Sistema irá Selecionar todos os Lançamentos Fiscais de Saída do período e das filiais informados no momento da geração do arquivo onde o Cliente/Fornecedor estiver marcado com o campo **INOVAR\_AUTO** igual a "1 – Sim”. Buscará por item em todas as entradas dos insumos utilizados para fabricação de cada item vendido para as montadoras (Cálculo da Parcela Dedutível), estes valores serão somados e apresentados no arquivo.

**Exemplo do arquivo gerado**

**Mapeamento do layout do arquivo XML referente a Auto Declaração de Vendas.**

|  |  |  |  |
| --- | --- | --- | --- |
| **TAG** | **DESCRIÇÃO** | **ORIGEM DOS DADOS** | **OBSERVAÇÃO** |
| **<?xml version="1.0"?>** | Cabeçalho do arquivo XML não devendo ser alterado | Gerado Internamente |  |
| **<tns:AutoDeclaracao**  **xmlns:tns =**[**http://www.tarea.com.br/InovarAuto/AutoDeclaracao**](http://www.tarea.com.br/InovarAuto/AutoDeclaracao)  **xmlns:xsi="<http://www.w3.org/2001/XMLSchema-instance>">** | Utilizada apenas para agrupar os dados da auto declaração |  | Preencha com “true” quando se tratar de uma declaração **retificadora** ou “false” quando não for. Campo de preenchimento obrigatório |
| **<tns:retificadora>** | Indica se esta declaração é retificadora ou não. | Gerando conforme informação da Tela |  |
| **<tns:declarante>** | Utilizada apenas para agrupar os dados do declarante |  |  |
| **<tns:tipo\_declarante>** | Indica o tipo de pessoa jurídica que está gerando o arquivo, neste caso um fornecedor. |  | Preencha com “F” por se tratar de fornecedor direto de montadora. Se uma montadora atuar como fornecedora direta de outra montadora, também deve preencher com “F”. Campo de preenchimento obrigatório |
| **<tns:razao\_social>** | Razão social da empresa que está gerando o arquivo, no caso, o fornecedor direto da montadora | Gerado conforme o cadastro da Filial |  |
| **<tns:cnpj>** | Número do CNPJ da empresa que está gerando o arquivo | Gerado conforme o cadastro da Filial |  |
| **<tns:matriz>** | Indica se o CNPJ do fornecedor é da matriz ou não | Gerado conforme o cadastro da Filial | apenas com os caracteres numéricos, ignorando “.” e “/”. |
| **<tns:operacao>** | Utilizada apenas para agrupar os dados da operação realizada pelo fornecedor |  |  |
| **<tns:natureza\_operacao>** | Indica a natureza da operação, ou seja, que o registro desta operação está tratando de uma venda |  | Preencha com “V” por se tratar de vendas diretas para montadoras. Campo de preenchimento obrigatório |
| **<tns:empresa>** | Utilizada apenas para agrupar os dados da empresa que está vendendo para a montadora que gera o arquivo |  |  |
| **<tns:razao\_social>** | Razão social da montadora para quem se realizou a venda | Gerado Conforme o Cadastro do Cliente\Fornecedor – Que o Campo Halibitado para Inovar\_Auto esteja habilitado |  |
| **<tns:cnpj>** | Número do CNPJ da montadora que adquiriu a venda realizada pelo fornecedor direto, gerador deste arquivo | Gerado Conforme o Cadastro do Cliente\Fornecedor – Que o Campo Halibitado para Inovar\_Auto esteja habilitado |  |
| **<tns:mes\_ref>** | Mês de referência dos dados | Conforme informado na tela de geração |  |
| **<tns:ano\_ref>** | Ano de referência dos dados | Conforme informado na tela de geração |  |
| **<tns:vl\_total\_notas>** | Valor total de notas fiscais do fornecedor direto da montadora | Soma das Vendas realizadas no período de geração |  |
| **<tns:vl\_parc\_dedutivel>** | Valor total da parcela dedutível | Gerado conforme serviço do Nucleus ou informado pelo cliente | Entradas dos insumos dos produtos |

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
