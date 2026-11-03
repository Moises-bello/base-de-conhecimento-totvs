---
article_id: 1500000237842
category: Financeiro - Controle Direitos Autorais
content_hash: 02b3144fefecca05dace3eb58e0bfa725be690d4df6b79795d18d287dd9daca4
fetched_at: '2026-06-28T22:38:17.713646+00:00'
product: protheus
section_id: 1500001550442
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Direitos Autorais
  ( SIGACDA )  - Gerando títulos de adiantamento no financeiro '
type: support-article
updated_at: '2024-01-17T17:02:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000237842-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Direitos-Autorais-SIGACDA-Gerando-t%C3%ADtulos-de-adiantamento-no-financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:07:00 min**

**Dúvida**Modulo (45) - Direitos Autorais (SIGACDA), como gerar Títulos no Financeiro pelo Documento de Entrada ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Passo (1) - Parametrizar ( Configurador - SIGACFG ) - De acordo com seu conteúdo, é possível obter diferentes resultados  
  
**MV\_CDAACER** (Informe o código do TIPO de acertos, se tiver mais ) **=** H  
**MV\_CDAAVSF** (Identifica se habilita o aviso de proximidade do termino do contrato de acordo com AH1\_DIAST)  = S  
**MV\_CDACHKC** (Identifica se o contrato faz parte da chave, se (S) eh verificado CONTRATO+SEQUENCIA+PRODUTO+FOR- NECEDOR, (N) verifica PRODUTO + FORNECEDOR = N   
**MV\_CDACONS** (Informe o código de TES de consignações, se tiver mais de um código, separe-os por / (barra) Utilizado no sistema de Royalty = 9   
**MV\_CDADVCO** (Parâmetro de controle para as devoluções de Vendas em consignação, ou seja, informar o tipo de operação.(DEVOLUCAO DA REMESSA DE CONSIGNACAO) = G   
**MV\_CDAEXC** (Determina se o calculo dos direitos autorais, se exclusivo (S), só uma estação utilizando o sistema ou compartilhado (N) = S   
**MV\_CDAEXCL** (Informe o código do lançamento padrão para a contabilidade, referente ao cancelamento de títulos a pagar ) = **518**   
**MV\_CDAFECH** (Data do ultimo fechamento do controle de royalty (direito)) = **30/05/2020**  
**MV\_CDALANC** (Informe o código do lançamento padrão para a contabilidade, títulos de direito autoral para a contabilidade) =**519**   
**MV\_CDALOC** (Almoxarifado reservado aos produtos utilizados no Controle de Direitos Autorais) = **01**   
**MV\_CDANUME** (Informe a tabela a ser utilizada para controle de títulos a pagar, cujo prefixo seja RYI ou RYE) = **H2**   
**MV\_CDAPRF** (Prefixo para geração do titulo do CDA) =  **If(SA2->A2\_TIPO = "X", "RYE", "RYI")**   
**MV\_CDAPROM** (Informe o código de TES de promoções, se tiver mais de um código, separe-os por / (barra)) = **W**   
**MV\_CDAVCON** (Informe o código do TES de venda de consignação, se tiver mais de um código, separe-os por /(barra)) = **G**   
**MV\_CDAVEND** (Informe o código do TIPO de vendas, se tiver mais de um código, separe-os por /(barra))= **V**   
**MV\_COFINS** (Natureza para títulos referentes a COFINS) = **COFINS**   
**MV\_COFINS1** ( % do PIS/COFINS)  = **25**

Passo (2) - Cadastro

1- **Produtos**:  Modulo ( 45 )  
No Menu ->Atualizações(2) -> Cadastro(15) -> Produtos ( MATA010 )  
Exemplo 

**PRODUTO CDA000001**

**Pasta Cadastrais**

|  |  |
| --- | --- |
| **Código** | CDA000001 |
| **Descrição** | Livro01 |
| **Tipo** | PA |
| **Unidade** | UN |
| **Armazém****Pad.** | 01 |
| **Preço****Venda** | 10,00 |

**Pasta Impostos**

|  |  |
| --- | --- |
| **Aliq. ICMS** | 18,00 |
| **Aliq. IPI** | 0,00 |

**Pasta Direitos Autorais**

|  |  |
| --- | --- |
| **Série/Coleção** | 1 |
| **Nr. Faixas CD** | 0 |
| **Nro Paginas** | 100 |
| **Código ISBN** | 1 (caso não visualize esse campo (necessário habilitar configurador) |
| **Tit. Original** | LIVRO01 |
| **Língua****Orig.** | Portuguesa |
| **Nro.****Edição** | 1 |
| **Obs. ISBN** | <EM BRANCO> |
| **Qtde. Acum.** | 0 |
| **Qtd. Inic.****mês** | 0 |

**PRODUTO CDA000002**

**Pasta Cadastrais**

|  |  |
| --- | --- |
| **Código** | CDA000002 |
| **Descrição** | Livro02 |
| **Tipo** | PA |
| **Unidade** | UN |
| **Armazém****Pad.** | 01 |
| **Preço****Venda** | 20,00 |

**Pasta Impostos**

|  |  |
| --- | --- |
| **Aliq. ICMS** | 18,00 |
| **Aliq. IPI** | 0,00 |

**Pasta Direitos Autorais**

|  |  |
| --- | --- |
| **Série/Coleção** | 2 |
| **Nr. Faixas CD** | 0 |
| **Nro Paginas** | 200 |
| **Código ISBN** | 2 |
| **Tit. Original** | LIVRO02 |
| **Língua****Orig.** | Portuguesa |
| **Nro.Edicao** | 2 |
| **Obs. ISBN** | <EM BRANCO> |
| **Qtde. Acum.** | 0 |
| **Qtd. Inic. mes** | 0 |

2- **Master**:  Modulo ( 45 ) - E um produto fictício que e utilizado como um acumulador de vendas, para produtos que a ele estão associados, que conforme e alterado o numero de edições o numero do código e alterado.

No Menu ->Atualizações(2) -> Cadastro(15) -> Master (CDAA060)  
Exemplo:

**LIVRO01**

|  |  |
| --- | --- |
| **Prod. Master** | 1 |
| **Desc. Tombo** | Livro01 |
| **Cod. Produto** | CDA000001 |
| **Desc. Produto** | Livro01 |
| **Qtd. Acumul.** | 0 |
| **Qtd. Inic. Mês** | 0 |

**LIVRO02**

|  |  |
| --- | --- |
| **Prod. Master** | 2 |
| **Desc. Tombo** | Livro02 |
| **Cod. Produto** | CDA0000012 |
| **Desc. Produto** | Livro02 |
| **Qtd. Acumul.** | 0 |
| **Qtd. Inic. Mês** | 0 |

3- **FORNECEDOR**:  Modulo ( 45 ) -  Cadastro das empresas com quem a empresa trabalha  
No Menu ->Atualizações(2) -> Cadastro(15) -> Fornecedor (MATA020)  
Exemplo:

**FORNECEDOR CDA001**

**Pasta Cadastrais**

|  |  |  |  |
| --- | --- | --- | --- |
| **Código** | CDA001 | **Loja** | 01 |
| **Razão Social** | Autor01 | **Nome Fantasia** | Autor01 |
| **Endereço** | Av. São Paulo,1 | **Bairro** | Centro |
| **Município** | São Paulo | **Estado** | SP |
| **CEP** | 01000-000 | **Tipo** | Físico |

**Pasta Direitos Autorais**

|  |  |
| --- | --- |
| **Royalty** | A |
| **Estado Civil** | 1-Solteiro |
| **Royalt Mínimo** | 0.00 |
| **Receb. Pagto.** | Sim |

**FORNECEDOR CDA002**

**Pasta Cadastrais**

|  |  |  |  |
| --- | --- | --- | --- |
| **Código** | CDA002 | **Loja** | 01 |
| **Razão Social** | Autor02 | **Nome Fantasia** | Autor02 |
| **Endereço** | Av. São Paulo,2 | **Bairro** | Centro |
| **Município** | São Paulo | **Estado** | SP |
| **CEP** | 01000-000 | **Tipo** | Físico |

**Pasta Direitos Autorais**

|  |  |
| --- | --- |
| **Royalty** | A |
| **Estado Civil** | 2- Casado |
| **Royalt Mínimo** | 0.00 |
| **Receb. Pagto.** | Sim |

**4- BANCOS:** Modulo ( 45 ) - Bancos que a empresa opera

No Menu ->Atualizações(2) -> Cadastro(15) -> Bancos (MATA070) **Exemplo :**

**Banco 001**

|  |  |
| --- | --- |
| **Código** | 001 |
| **Número da Agência** | 00001 |
| **Número da Conta** | 0000000001 |
| **Nome do Banco** | BANCO DO BRASIL S/A. |
| **Nome reduzido do banco** | BB |
| **Endereço** | Rua Paula Souza, 500 |
| **Bairro** | Centro |
| **Município** | São Paulo |
| **CEP** | 99002-909 |
| **Estado** | SP |

**5- Moedas:** Modulo ( 45 ) - O cadastro de Moedas deverá ser incluso ou alterado somente se houver a necessidade de controlar os movimentos  em outras moedas diferentes da corrente.

No Menu ->Atualizações(2) -> Cadastro(15) -> Moedas (MATA090 )

**5- Condição de Pagamento:** Modulo ( 45 ) - Cadastro de condições de pagamento

No Menu ->Atualizações(2) -> Cadastro(15) -> Cond. de Pagamento (MATA360)

**Exemplo :**

**CONDIÇÃO DE PAGTO  001**

|  |  |  |  |
| --- | --- | --- | --- |
| **Código** | 001 | **Tipo** | 1 |
| **Cond. Pagto** | 00 | **Descrição** | A VISTA |

**CONDIÇÃO DE PAGTO  002**

|  |  |  |  |
| --- | --- | --- | --- |
| **Código** | 002 | **Tipo** | 1 |
| **Cond. Pagto** | 1,30 | **Descrição** | 1/30 DIAS |

**6- Contrato de Direitos Autorais:** Modulo ( 45 ) - O cadastro de Contrato de Direito Autoral tem como finalidade definir as regras do contrato com o fornecedor, controla datas de início e fim do contrato, quantidade de venda de exemplares e define a faixa de percentuais dos direitos autorais que deve ser pago ao autor. Pode-se aplicar um percentual ou valor para cada faixa de venda do produto, assim como informar se o preço a ser utilizado para cada faixa será o preço de tabela ou o preço de venda.  
Neste cadastro serão informados o número do contrato, nome do autor, nome da obra,  dados que serão considerados no cálculo dos direitos autorais da obra, a periodicidade para a prestação de contas com os autores, a forma de pagamento e o tipo de moeda que será adotada (corrente/forte) para o cálculo dos direitos autorais.

No Menu ->Atualizações(2) -> Cadastro(15) -> Contratos Direitos Autorais (CDAA010)

**Exemplo :**

**CONTRATO 000001/01 – AUTOR01**

**Pasta Dados Cadastrais**

|  |  |
| --- | --- |
| **Nro. Contrato** | 000001 |
| **Seq. Contrato** | 01 |
| **Data Vigenc.** | dd/mm/aaaa (dia/mês/ano corrente) |
| **Cod. Produto** | CDA000001 |
| **Desc. Produto** | LIVRO01 ( Será preenchido automaticamente após entrar com o código do Produto ) |
| **Fornecedor** | CDA001 |
| **Loja Fornec** | 01 ( Será preenchido automaticamente após entrar com o código do Fornecedor ) |
| **Nome Autor** | Autor01 ( Será preenchido automaticamente após entrar com o código do Fornecedor ) |
| **Data Contrat** | dd/mm/aaaa (dia/mês/ano corrente) |
| **Vig. Indeterm.** | Sim |
| **Ano Vigenc.** | 0 ( Este campo deverá ser preenchido somente se a Vigência for determinada) |
| **Data do término** | Deixar <EM BRANCO>  ( Este campo será preenchido automaticamente se for determinada a quantidade de anos de vigência do contrato) |
| **Anos Renova** | 0 |
| **Observação** | <EM BRANCO> |
| **Titulo Orig.** | Livro01 |

**Pasta Informações Para Cálculo**

|  |  |
| --- | --- |
| **Prod. Master** | 1 |
| **Cond. Pagto.** | 001 (A Vista) |
| **Período** | 01 - Mensal |
| Calc. Cor/For | 1 – Corrente |
| **Agente Liter** | CDA001 |
| **Loja agente** | 01 |
| **Moeda Prest.** | 1 |
| **Sld.Inic. Mes** | 0,000 |
| **Saldo Adiant.** | 0,000 |
| **Saldo Qtde** | 0 |
| **Valor Adiant.** | 0,0000 |

**Pasta Informações Contratuais**

|  |  |
| --- | --- |
| **Ult/1a.Prest** | <EM BRANCO> |
| **Qtde Venda** | 0 |

**Itens Contrato (Item 01)**

|  |  |
| --- | --- |
| **Item Regra** | 01 |
| **Faixa Inicio** | 1 |
| **Faixa Final** | 10 |
| **% Desc. Acima** | 0,00 |
| **% Dir. Aut.** | 1,00 |
| **Vlr Dir. Aut.** | 0,00 |
| **Prc. Aplicado** | 1 - Preço de Tabela |
| **Desc.Comerc.** | Não |
| **Abate ICMS** | Não |
| **Abate IPI** | Não |
| **Abate COFINS** | Não |
| **% Outros Desc** | 0,00 |

**Itens do Contrato (Item 02)**

|  |  |
| --- | --- |
| **Item Regra** | 02 |
| **Faixa Inicio** | 11 |
| **Faixa Final** | 20 |
| **% Desc. Acima** | 0,00 |
| **% Dir. Aut.** | 0,00 |
| **Vlr Dir. Aut.** | 10,00 |
| **Prc. Aplicado** | 1 - Preço de Tabela |
| **Desc.Comerc.** | Não |
| **Abate ICMS** | Não |
| **Abate IPI** | Não |
| **Abate COFINS** | Não |
| **% Outros Desc** | 0,00 |

**Itens do Contrato (Item 03)**

|  |  |
| --- | --- |
| **Item Regra** | 03 |
| **Faixa Inicio** | 21 |
| **Faixa Final** | 99.999.999 |
| **% Desc. Acima** | 0,00 |
| **% Dir. Aut.** | 10,00 |
| **Vlr Dir. Aut.** | 0,00 |
| **Prc. Aplicado** | 2 – Preço de Venda |
| **Desc.Comerc.** | Não |
| **Abate ICMS** | Não |
| **Abate IPI** | Não |
| **Abate COFINS** | Não |
| **% Outros Desc** | 0,00 |

**CONTRATO 000002/01 – AUTOR02**

**Pasta Dados Cadastrais**

|  |  |
| --- | --- |
| **Nro. Contrato** | 000002 |
| **Seq. Contrato** | 01 |
| **Data Vigenc.** | dd/mm/aaaa (dia/mês/ano corrente) |
| **Cod. Produto** | CDA000002 |
| **Desc. Produto** | LIVRO02 ( Será preenchido automaticamente após entrar com o código do Produto ) |
| **Fornecedor** | CDA002 |
| **Loja Fornec** | 01 ( Será preenchido automaticamente após entrar com o código do Fornecedor ) |
| **Nome Autor** | Autor02 ( Será preenchido automaticamente após entrar com o código do Fornecedor ) |
| **Data Contrat** | dd/mm/aaaa (dia/mês/ano corrente) |
| **Vig. Indeterm.** | Sim |
| **Ano Vigenc.** | 0 ( Este campo deverá ser preenchido somente se a Vigência for determinada) |
| **Data do término** | Deixar <EM BRANCO>  ( Este campo será preenchido automaticamente se for determinada a quantidade de anos de vigência do contrato) |
| **Anos Renova** | 0 |
| **Observação** | <EM BRANCO> |
| **Titulo Orig.** | Livro02 |

**Pasta Informações Para Cálculo**

|  |  |
| --- | --- |
| **Prod. Master** | 2 |
| **Cond. Pagto.** | 002 (1/30 DIAS) |
| **Período** | 01 - Mensal |
| **Calc. Cor/For** | 1 – Corrente |
| **Agente Liter** | CDA002 |
| **Loja agente** | 01 |
| **Moeda Prest.** | 1 |
| **Sld.Inic. Mes** | 0,000 |
| **Saldo Adiant.** | 0,000 |
| **Saldo Qtde** | 0 |
| **Valor Adiant.** | 0,0000 |

**Pasta Informações Contratuais**

|  |  |
| --- | --- |
| **Ult/1a.Prest** | <EM BRANCO> |
| **Qtde Venda** | 0 |

**Itens do Contrato (Item 01)**

|  |  |
| --- | --- |
| **Item Regra** | 01 |
| **Faixa Inicio** | 1 |
| **Faixa Final** | 10 |
| **% Desc. Acima** | 0,00 |
| **% Dir. Aut.** | 2,00 |
| **Vlr Dir. Aut.** | 0,00 |
| **Prc. Aplicado** | 1 – Preco de Tabela |
| **Desc.Comerc.** | Não |
| **Abate ICMS** | Não |
| **Abate IPI** | Não |
| **Abate COFINS** | Não |
| **% Outros Desc** | 0,00 |

**Itens do Contrato (Item 02)**

|  |  |
| --- | --- |
| **Item Regra** | 02 |
| **Faixa Inicio** | 11 |
| **Faixa Final** | 20 |
| **% Desc. Acima** | 0,00 |
| **% Dir. Aut.** | 0,00 |
| **Vlr Dir. Aut.** | 20,00 |
| **Prc. Aplicado** | 1 – Preço de Tabela |
| **Desc.Comerc.** | Não |
| **Abate ICMS** | Não |
| **Abate IPI** | Não |
| **Abate COFINS** | Não |
| **% Outros Desc** | 0,00 |

**Itens do Contrato (Item 03)**

|  |  |
| --- | --- |
| **Item Regra** | 03 |
| Faixa Inicio | 21 |
| **Faixa Final** | 99.999.999 |
| **% Desc. Acima** | 0,00 |
| **% Dir. Aut.** | 20,00 |
| **Vlr Dir. Aut.** | 0,00 |
| **Prc. Aplicado** | 2 – Preço de Venda |
| **Desc.Comerc.** | Não |
| **Abate ICMS** | Não |
| **Abate IPI** | Não |
| **Abate COFINS** | Não |
| **% Outros Desc** | 0,00 |

**7- Tipos de Entrada e Saída:** Modulo ( 45 ) - Cadastro de Entradas e Saídas

No Menu ->Atualizações(2) -> Cadastro(15) -> Cadastro de Entradas e Saída (MATA080 )

**Exemplo :**

**TES 001**          

**Pasta Adm/Fin/Custo**

|  |  |  |  |
| --- | --- | --- | --- |
| **Cod. Tipo** | 001 | **Tipo do TES** | Entrada |
| **Credita ICMS ?** | Sim | **Credita IPI ?** | Não |
| **Gera Dupl. ?** | Sim | **Atu. Estoque ?** | Sim |
| **Poder Terc.** | Não Controla | **Atu. Pr. Compr.** | Sim |
| **Atual. Tecn.?** | <EM BRANCO> | **Atual. Ativo ?** | <EM BRANCO> |
| **Crd.ICMS ST ?** | <EM BRANCO> |  |  |

**Pasta Impostos**

|  |  |  |  |
| --- | --- | --- | --- |
| **Calcula ICMS** | Sim | **Calcula IPI ?** | Não |
| **Cod. Fiscal** | 1102 | **Txt Padrão** | Entrada Mercadorias |
| **L. Fisc. ICMS** | Tributado | **L. Fiscal IPI** | Não |
| **Destaca IPI ?** | Não | **IPI na Base ?** | Não |
| **Calc. Dif. ICM** | Não |  |  |

**TES 133**

**Pasta Adm/Fin/Custo**

|  |  |  |  |
| --- | --- | --- | --- |
| **Cod. Tipo** | 133 | **Tipo do TES** | Entrada |
| **Credita ICMS ?** | Sim | **Credita IPI ?** | Não |
| **Gera Dupl. ?** | Não | **Atu. Estoque ?** | Sim |
| **Poder Terc.** | Não Controla | **Atu. Pr. Compr.** | Sim |
| **Atual. Tecn.?** | Não | **Atual. Ativo ?** | Não |
| **Crd.ICMS ST ?** | Não |  |  |

**Pasta Impostos**

|  |  |  |  |
| --- | --- | --- | --- |
| Calcula ICMS | Sim | **Calcula IPI ?** | Não |
| Cod. Fiscal | 132 | **Txt Padrão** | Dev. Vendas Com. |
| L. Fisc. ICMS | Tributado | **L. Fiscal IPI** | Não |
| Destaca IPI ? | Não | **IPI na Base ?** | Não |
| Calc. Dif. ICM | Não |  |  |

**TES 502**

**Pasta Adm/Fin/Custo**

|  |  |  |  |
| --- | --- | --- | --- |
| **Cod. Tipo** | 502 | **Tipo do TES** | Saída |
| **Credita ICMS ?** | Sim | **Credita IPI ?** | Não |
| **Gera Dupl. ?** | Sim | **Atu. Estoque ?** | Sim |
| **Poder Terc.** | Não Controla | **Atu. Pr. Compr.** | Não |
| **Atual. Tecn.?** | Não | **Atual. Ativo ?** | Não |
| **Crd.ICMS ST ?** | Não |  |  |

**Pasta Impostos**

|  |  |  |  |
| --- | --- | --- | --- |
| **Calcula ICMS** | Sim | **Calcula IPI ?** | Não |
| **Cod. Fiscal** | 5102 | **Txt Padrão** | Saída de Mercadorias |
| **L. Fisc. ICMS** | Tributado | **L. Fiscal IPI** | Não |
| **Destaca IPI ?** | Não | **IPI na Base ?** | Não |
| **Calc. Dif. ICM** | Não |  |  |

**TES 532**

**Pasta Adm/Fin/Custo**

|  |  |  |  |
| --- | --- | --- | --- |
| **Cod. Tipo** | 532 | **Tipo do TES** | Saída |
| **Credita ICMS ?** | Sim | **Credita IPI ?** | Não |
| **Gera Dupl. ?** | Não | **Atu. Estoque ?** | Sim |
| **Poder Terc.** | Não Controla | **Atu. Pr. Compr.** | Não |
| **Atual. Tecn.?** | Não | **Atual. Ativo ?** | Não |
| **Crd.ICMS ST ?** | Não |  |  |

**Pasta Impostos**

|  |  |  |  |
| --- | --- | --- | --- |
| **Calcula ICMS** | Sim | **Calcula IPI ?** | Não |
| **Cod. Fiscal** | 5202 | **Txt Padrão** | Dev. Compras p/ Com. |
| **L. Fisc. ICMS** | Tributado | **L. Fiscal IPI** | Não |
| **Destaca IPI ?** | Não | **IPI na Base ?** | Não |
| **Calc. Dif. ICM** | Não |  |  |

**8- Unidade de Media:** Modulo ( 45 ) - Cadastro de Unidades de Medida

No Menu ->Atualizações(2) -> Cadastro(15) -> Unidades de Medida ( QIEA030 )

**9- Contatos:** Modulo ( 45 ) - Cadastro de Contatos 

No Menu ->Atualizações(2) -> Cadastro(15) -> Contatos ( TMKA070 )

**10- Complemento de Produtos:** Modulo ( 45 ) - Cadastro de Complemento de Produtos

No Menu ->Atualizações(2) -> Cadastro(15) -> Complemento de Produtos ( MATA180 )

**11- Grupo de Produtos:** Modulo ( 45 ) - Cadastro de Grupo de Produtos 

No Menu ->Atualizações(2) -> Cadastro(15) -> Grupo de Produtos (MATA035)

**12- Clientes:** Modulo ( 05 - Faturamento ) -  Cadastro de Clientes da empresa

No Menu ->Atualizações(17) -> Cadastro(35) -> Clientes (MATA030)

**Exemplo :**

**CLIENTE CDA001**

**Pasta dados Cadastrais**

|  |  |
| --- | --- |
| **Código** | CDA001 |
| **Loja** | 01 |
| **Nome** | Cliente Padrão Dentro do Estado (RISCO A) |
| **Física/Jurid.** | J = Jurídica |
| **Nome Fantasia** | CLIENTE1 |
| **Tipo** | Revendedor |
| **Endereço** | Av. São Paulo, 1 |
| **Município** | São Paulo |
| **Estado** | SP |
| **Bairro** | Centro |
| **CEP** | 01000-000 |

**Pasta Vendas**

|  |  |
| --- | --- |
| **Risco** | Risco A |

**CLIENTE CDA002**

**Pasta dados Cadastrais**

|  |  |
| --- | --- |
| **Código** | CDA002 |
| **Loja** | 01 |
| **Nome** | Cliente2-Padrão Dentro do Estado |
| **Física/Jurid.** | F = Física |
| **Nome Fantasia** | CLIENTE2 |
| **Tipo** | Cons. Final |
| **Endereço** | Av. São Paulo, 2 |
| **Município** | São Paulo |
| **Estado** | SP |
| **Bairro** | Centro |
| **CEP** | 01000-000 |

**13- Natureza:** Modulo ( 05 - Faturamento ) 

No Menu ->Atualizações(17) -> Cadastro(35) -> Naturezas ( FINA010 )

**Exemplo :**

**NATUREZA DP00000001 – DUPLICATAS A PAGAR SEM IMPOSTOS**

|  |  |  |  |
| --- | --- | --- | --- |
| **Código** | DP00000001 | **Descrição** | Dup. a Pagar sem impostos |
| **Calcula IRRF ?** | Não | **Calcula ISS ?** | Não |
| **Porc. IRRF** | 0,00 | **Calcula INSS ?** | Não |
| **Porc. INSS** | 0,00 | **Calcula CSLL ?** | Não |
| **Calc. COFINS ?** | Não | **Calcula PIS ?** | Não |
| **Porc. CSLL** | 0,00 | **Porc. COFINS** | 0,00 |
| **Porc. PIS** | 0,00 | **Dedução PIS** | Não |
| **Dedução COFINS** | Não |  |  |

**NATUREZA DR00000001 – DUPLICATAS A RECEBER SEM IMPOSTOS**

|  |  |  |  |
| --- | --- | --- | --- |
| **Código** | DP00000002 | **Descrição** | Dup. a Receber sem impostos |
| **Calcula IRRF ?** | Não | **Calcula ISS ?** | Não |
| **Porc. IRRF** | Não | **Calcula INSS ?** | Não |
| **Porc. INSS** | 0,00 | **Calcula CSLL ?** | Não |
| **Calc. COFINS ?** | Não | **Calcula PIS ?** | Não |
| **Porc. CSLL** | 0,00 | **Porc. COFINS** | 0,00 |
| **Porc. PIS** | 0,00 | **Dedução PIS** | Não |
| **Dedução COFINS** | Não |  |  |

Passo (3) - Adiantamento para o Fornecedor 

## **Adiantamento para o Fornecedor**

1- Adiantamento Modulo ( 45 )   
No Menu ->Atualizações(2) -> Movimentos ( 4 ) -> Adiantamentos ( CDAA020 )

Exemplo 1

**ADIANTAMENTO PARA O FORNECEDOR CDA001**

|  |  |  |  |
| --- | --- | --- | --- |
| Produto | CDA000001 | **Nro. Título** | RYI000001 |
| Loja Fornec. | 01 | **Fornecedor** | CDA001 |
| Valor Movim. | 100,00 | **Data Movim.** | dd/mm/aaaa |
| Histórico | ADIANTAMENTO DE DA - AUTOR01 | **Nro. Exemplar** | 0 |
| Qtde / Valor | 2 - Valor | **Despesa/Rec** | Despesa |
| Gera Título | 1 - Sim (\*) | **Moeda Título** |  |

(\*) Definirá se gerará título no Financeiro. O Número do título será gerado automaticamente pelo sistema após a confirmação das informações e o seu conteúdo (sequencial) ficará armazenado na tabela H2.

Confirmando os dados, aparecerá a tela de Título com a Série RYI e o Título 000001. Confirmando a tela, aparecerá outra tela com os parâmetros a serem configurados:

|  |  |
| --- | --- |
| **Tipo do Título ?** | PA |
| **Natureza do Título ?** | DP00000001 |
| **Prazo de Pagamento ?** | 001    (A VISTA) |

**Confirmando a tela de parâmetros, o título 000001 foi gerado para o Fornecedor  CDA001.**

**ADIANTAMENTO PARA O FORNECEDOR CDA002**

|  |  |  |  |
| --- | --- | --- | --- |
| **Produto** | CDA000002 | **Mov. D/C** | Débito |
| **Loja Fornec.** | 01 | **Fornecedor** | CDA002 |
| **Valor Movim.** | 200,00 | **Data Movim.** | dd/mm/aaaa |
| **Histórico** | Adiantamento De Direito Autoral-Autor02 | **Nro. Exemplar** | 10 |
| **Qtde / Valor** | 1 - Qtde | **Despesa/Rec** | Despesa |
| **Gera Título** | 1 - Sim (\*) | **Moeda Título** | 1 |

(\*) Definirá se gerará título no Financeiro. O Número do título será gerado automaticamente pelo sistema após a confirmação das informações e o seu conteúdo (sequencial) ficará armazenado na tabela H2.  
Confirmando os dados, aparecerá a tela de Título com a Série RYI e o Título 000002. Confirmando a tela, aparecerá outra tela com os parâmetros a serem configurados:

|  |  |
| --- | --- |
| **Tipo do Título ?** | PA |
| **Natureza do Título ?** | DP00000001 |
| **Prazo de Pagamento ?** | 002    (2 PARCELAS) |

**Confirmando a tela de parâmetros, o título 000002 foi gerado para o Fornecedor  CDA002.**

**No Modulo ( 06 - FINANCEIRO ),**No Menu ->Atualizações(15) -> Contas a Pagar(22) -> Contas a Pagar ( FINA050 ) E assim será incluso o titulo no **FINANCEIRO**

**Saiba Mais**

<https://tdn.totvs.com/display/public/PROT/Controle+de+Direitos+Autorais+-+P12#ControledeDireitosAutorais-P12-04.CONFIGURA%C3%87%C3%83O>
