---
content_hash: 1fedae4abcfee6671d1b78bea4aab130b782888d44208ddcdabf96c09651038b
fetched_at: '2026-06-29T00:09:23.868580+00:00'
page_id: '422546144'
product: rm
source: tdn-rm
title: Auto Declaração de Vendas - Requisitos Necessários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546144
version: 4
---

**TOTVS Gestão Financeira**

---

Primeiramente, é necessário criar um campo complementar para o cadastro de Cliente/Fornecedor, para posterior preenchimento, de todos que irão participar do programa.  
 Nome da Coluna: INOVAR\_AUTO Tipo: Inteiro  
 Valor de preenchimento: 0 = Não / 1 = Sim   ***Observação***: Obrigatoriamente, este deve ser o nome do campo.

***Informativo***: Na conversão para o ambiente da 12.1.4, este campo será criado na base e preenchido automaticamente com os valor informado no campo complementar.                
    
 **TOTVS Gestão de Estoque, Compras  e Faturamento**     
 Para o cálculo da parcela Dedutível, será verificado os Movimentos de Entrada e Insumos utilizados na produção dos produtos vendidos para as montadoras. Obs.: Este cálculo somente será realizado, quando houver integração com o Gestão Fiscal.     
 PORTARIA 257, DE 23 DE SETEMBRO DE 2014 ANEXO III  
 Item Pai: será gerado com o item da nota fiscal de venda para montadora (cliente cujo o Campo Complementar "INOVAR\_AUTO", citado acima, estiver preenchido com "1" - Sim).  
 Itens Filhos (Insumos): São os itens que compõe o "item pai". Será selecionados os movimentos de compra desses itens associados ao "Item Pai" no processo de produção.  
 Obs.: Caso não encontre entradas do Insumo no período de geração, o processo busca no período anterior (sucessivamente no prazo de 24 meses). *S*e esgotar as possibilidades será considerado, o valor da operação ocorrida no próprio mês do fornecimento. As Notas Fiscais de Devolução devem descontar no valor Total das Notas Fiscais do Cliente. Serão tratadas apenas notas de devolução referentes ao mês de geração da Rotina, caso a Devolução seja maior que o valor de Venda, será informado 0 para este item.

**Cálculo da Parcela Dedutível**  
 O cálculo da parcela dedutível será realizado mensalmente para todos os itens das Nota Fiscais de Venda do mês que for informado na tela de Geração da Rotina. Considera os componentes (insumos) dos itens vendidos e verifica as notas fiscais de compra, importação e/ou devolução do mês mais recente do período processado.   
 Depois dessa verificação o sistema realizará uma média da parcela dedutível, somando o valor total sem IPI de cada insumo no período de processamento e dividindo pela quantidade total de cada insumo. Para então multiplicar o valor dessa divisão pela quantidade necessária do componente e obter o valor da parcela.  
 Na Tela de Geração da Rotina será possível gerar um arquivo de Log. Onde será demonstrado a Memória de Cálculo dos Valores gerados no Arquivo XML. A geração do log será solicitada pelo usuário, na tela de execução do processo.  
 Dependendo da quantidade de produtos que terá a Parcela Dedutível calculada automaticamente e o volume de movimentações na base, a execução desse log poderá comprometer a performance do processo.  
 Encontrado insumo na NF de entrada do período, busca todas as NFs do período para calcular o preço médio da parcela dedutível.

|  |  |  |  |
| --- | --- | --- | --- |
| **Código de Situação Tributária - CST** | **Origem da Mercadoria** | **Conteúdo Importado**   **Critério Resolução SF 13** | **Parcela Dedutível**   **Critério Inovar Auto** |
| **0** | Nacional (exceto código 3,4,5 e 8) | 0% | 0% |
| **1** | Estrangeira (exceto cód. 6) - Importação direta | 100% | 100% |
| **2** | Estrangeira (exceto cód. 7) adquirida no mercado interno | 100% | 100% |
| **3** | Nacional com > 40% <= 70% de importado | 50% | 50% |
| **4** | PPB - Processo de Produção Básica | 0% | 50% |
| **5** | Nacional com < 40% de importado | 0% | 0% |
| **6** | Estrangeira (sem simular nacional - constante em Resolução Carmex e gás natural) - adquirida no mercado interno | 0% | 100% |
| **7** | Estrangeira (sem simular nacional - constante em Resolução Carmex e gás natural) - adquirida no mercado interno | 0% | 100% |
| **8** | Nacional com > 70% de importado | 100% | 100% |

Considera regras de CST, Classificação Fiscal e Imposto Importação.  
 Observação: Quando a Nota Fiscal não apresentar o Código CST, considerar sempre CST 2.  
 Calcula a parcela dedutível média no período para o insumo (subtrai devoluções de entrada) Parcela Dedutível Média = (total(Parcela Dedutível Unitária)/total(Quantidade)) \* Qtde Usada

**TOTVS Gestão Fiscal**  
 A Rotina Federal Inovar Auto será gerada através do menu: ***Obrigações Acessorias | Federais | Inovar Auto | Auto Declaração de Vendas.***  
 Obs.:  Na versão 11.82.3x este menu será exibido apenas quando o campo Complementar INOVAR\_AUTO existir no cadastro de Cliente/Fornecedor.  
 Caso não trabalhe com o controle de Produção TOTVS Planejamento e Controle da Produção ou o Totvs Gestão de Estoque, Compras  e Faturamento, terá a opção de informar a parcela dedutível por cliente que será impressa no arquivo.   
 Obs.: Caso esta informação esteja preenchida o sistema vai utilizar este valor e não o fazer o cálculo conforme informado acima na descrição do Totvs Gestão de Estoque, Compras  e Faturamento.  
 O Sistema irá Selecionar todos os Lançamentos Fiscais de Saída do período e das filiais informadas no momento da geração do arquivo onde o Cliente/Fornecedor estiver marcado com o campo INOVAR\_AUTO igual a "1 – Sim".   
 O sistema irá buscar por item em todas as entradas dos insumos utilizados para fabricação de cada item vendido para as montadoras (Cálculo da Parcela Dedutível), estes valores serão somados e apresentados no arquivo.
