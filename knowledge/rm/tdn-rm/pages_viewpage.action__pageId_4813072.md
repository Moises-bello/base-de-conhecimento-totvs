---
content_hash: 5dc19000972261623eb3e0917533cbfaf01960c8206f3a368f6891af15a60565
fetched_at: '2026-06-29T00:10:19.111481+00:00'
page_id: '4813072'
product: rm
source: tdn-rm
title: Geração de INSS e IRRF  Automático para o Totvs Gestão Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813072
version: 6
---

BLOCK

Geração de INSS e IRRF Automático para o Totvs Gestão Financeira

FAQ: **Geração de INSS e IRRF Automático para o Totvs Gestão Financeira**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para gerar INSS e IRRF Automático para o TOTVS Gestão Financeira?

* ***Definição do Processo***

Tem por finalidade gerar lançamento automático de INSS e IRRF – DARF no Totvs Gestão Financeira, fazendo com que serão gerados 03 lançamentos. Estes lançamentos vão obedecer conteúdo da condição de pagamento referenciada na movimentação, sendo apresentado lançamento financeiro, lançamento de INSS e lançamento de IRRF.

Para os lançamentos de INSS e IRRF será obedecido “Fato Gerador” parametrizado no Totvs Gestão Financeira que pode ser “Emissão ou Vencimento”.

Os lançamentos de INSS e IRRF serão gerados apenas para o cliente / fornecedor que seja “**Pessoa Física**”. Para termos de INSS será considera alíquota de 11% por se tratar de prestação de serviço de autônomo, para o cálculo do IRRF será considerada tabela progressiva inclusa no Totvs Gestão Financeira para o IRRF.

A geração dos lançamentos de INSS e IRRF automáticos independem da existência destes tributos no item ou no movimento, sendo considerada parametrização do “tipo de movimento”.

Solução

* ***Parametrizações Necessárias - Totvs Gestão Financeira***

Acessar **| Opções | Parâmetros | RMFluxus | Contas a Pagar |** e parametrizar as opções a seguir:

**Etapa Inclusão**

- Origem Tab.Op.: Cliente / Fornecedor |

**Etapa Geração de INSS**

- Habilitar: Gerar INSS Automaticamente

- Empregador | Origem das Tabelas: Lançamento Original |

- Empregador | Tipo de documento: informar tipo de documento que deve ser apresentado no lançamento de INSS de Empregador que será gerado  *( Este tipo de documento deve ser do tipo "Sem Classificação")*

- Empregado | Origem das Tabelas: Lançamento Original

- Empregado | Tipo de documento: informar tipo de documento que deve ser apresentado no lançamento de INSS de Empregado que será gerado  *( Este tipo de documento deve ser do tipo "Sem Classificação")*

- Fornecedor: informar código do cliente \ fornecedor que será apresentado no lançamento gerado

- Data base para Geração: informar data a ser considerada para geração da DARF

- Valor Mínimo: informar valor mínimo para geração do lançamento. A receita aceita pagamentos a partir de 10,00 |

**Etapa Geração de IRRF**

- Habilitar: Gerar Imposto de Renda Automaticamente

- Origem Default das Tabelas: Lançamento Original

- Valor Mínimo: informar valor mínimo para geração do lançamento. A receita aceita pagamentos a partir de 10,00 |

**Etapa Geração de IRRF – PF**

- Data Base para Geração: informar data a ser considerada para geração da DARF

- Fornecedor: informar código do cliente \ fornecedor que será apresentado no lançamento gerado

- Tipo de Documento: informar tipo de documento que deve ser apresentado no lançamento que será gerado  *( Este tipo de documento deve ser do tipo "Sem Classificação")*

***Parametrizações Necessárias - Totvs Gestão de Estoque, Compras e Faturamento***

Acessar | **Cadastro | Tabelas Auxiliares | Tipo de Documento |** e incluir tipo de documento específico para este fim, onde deverá informar | **Classificação : Gera IRRF e INSS |**.

Se o cliente \ fornecedor a ser utilizado possuir “Valor pago em outra empresa” e/ou “SEST/SENAT” a informação deverá ser preenchida em **| Cadastro | Cliente \ Fornecedor | Dados Fiscais | Tributos | Dados Relacionados ao INSS | Pessoa Física | Categoria do Autônomo |**.

Acessar **| Cadastro | Produto | Dados Fiscais do Produto | INSS |** e definir os percentuais de INSS a serem considerados para **INSS Empregado - INSS Empregador**

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Fin – Faturamento**

Fatura o movimento: Habilita

Fatura na Inclusão: Habilita

Tipo de Geração: Edita

Tipo de Documento Gerado: Outros

Tipo de Documento Duplicata: informar local de onde será buscado tipo de documento a ser considerado para este fim. Se escolher a opção “Utiliza do Tipo de Movimento” será apresentado campo **| Tipo de Documento Duplicata Default** | para informar o tipo de documento, caso contrário será consistido código do tipo de documento informado no cadastro do cliente \ fornecedor preenchido no movimento.

Tipo de Documento Duplicada Default: informar o tipo de documento que será utilizado neste tipo de movimento

Numeração do Lançamento: informar se deseja utilizar “número do movimento + sequencial” ou apenas “sequência”

- Caso queira que a base de cálculo do INSS tenha a mesma informação do “Valor Original do lançamento financeiro” deve preencher o mesmo código da “Fórmula de Valor a Ratear” no campo **| Fórmula para Cálculo Valor de Serviço |**. Se a base de cálculo de INSS for considerar outra informação, deverá cadastrar uma fórmula com o conteúdo desejado e referenciar no campo em questão.

- Caso queira que a base de cálculo do IRRF tenha a mesma informação do “Valor Original do lançamento financeiro” deve preencher o mesmo código da “Fórmula de Valor a Ratear” no campo **| Fórmula para Cálculo de IRRF |**. Se a base de cálculo de IRRF for considerar outra informação, deverá cadastrar uma fórmula com o conteúdo desejado e referenciar no campo em questão.

Importante:

Todo tributo do tipo “RF – Retido na Fonte” necessita de um Código da Receita para que o lançamento financeiro seja incluso. Para buscar o código da receita do cadastro de Cliente \ Fornecedor o campo | **Fórmula para Cálculo de IRRF** | tem que estar preenchido, caso contrário será considerado código da receita preenchido no cadastro do produto.

* ***Descrição do Processo***

A inclusão dos movimentos será feita como de costume, porém se o cliente \ fornecedor possuir “Valor pago em outra empresa” ou “SEST/SENAT” deverá acessar a aba **| Tributos | INSS Pessoa Física |** e preencher os dados:

Ocorrência do Autônomo: seu preenchimento é obrigatório quando o autônomo prestar serviço em mais de uma empresa. O campo “Valor Pago em Outra Empresa” deve ser preenchido quando a ocorrência de autônomo for de | 5 a 8 |.

Valor Retido em outra Empresa: se refere ao valor do INSS referente serviço prestado em outra empresa. O mesmo se refere a 11% do valor preenchido em “Base INSS Outras Empresas”.

Base INSS Outras Empresas: se refere á base de calculo do INSS retido em outras empresas onde o trabalhador prestou serviço dentro do período de inclusão do movimento.

% sobre Vr. Serviço Empregado: percentual definido em **| Cadastro | Produto | Dados fiscais do Produto | INSS | Percentual de Dedução Empregado |**

% sobre Vr. Serviço Empregador: percentual definido em **| Cadastro | Produto | Dados fiscais do Produto | INSS | Percentual de Dedução Empregador |**

Cli\For Origem: em que cliente o fornecedor autônomo prestou serviços

O cálculo dos tributos **| INSS e IRRF |** serão visualizados ao editar a aba **| Contas a Pagar | Lançamento Financeiro | Valores | Impostos \ Tributos |**.

No campo **| INSS |** serão apresentados:

Valor do Serviço: resultado da fórmula utilizada para composição da base de cálculo deste tributo

Ocorrência do Autônomo: informação preenchida na aba | Tributos | INSS Pessoa Física |

Cat. do Autônomo: informação preenchida em **| Dados Fiscais | Tributos | Dados Relacionados ao INSS | Pessoa Física | Categoria do Autônomo |**. Esta informação não pode ser preenchida na inclusão do movimento.

Vr. Base em outra empresa: base de cálculo do INSS paga em outra empresa

% sobre Vr. Serviço Empregado: percentual definido em **| Cadastro | Produto | Dados fiscais do Produto | INSS | Percentual de Dedução Empregado |**

% sobre Vr. Serviço Empregador: percentual definido em **| Cadastro | Produto | Dados fiscais do Produto | INSS | Percentual de Dedução Empregador |**

Valor INSS: Valor do INSS calculado considerando valor pago em outra empresa se houver

Cliente Origem: código do cliente onde o fornecedor autônomo prestou serviço

No campo **| IRRF |** serão apresentados:

Valor do Serviço: resultado da fórmula utilizada para composição da base de cálculo deste tributo

Código da Receita: código utilizado para geração da DARF

Valor IRRF: valor calculado do tributo considerando tabela progressiva inclusa no Totvs Gestão Financeira

O valor calculado também pode ser consultado na visão de movimento na aba | Identificação | **Vl Líquido Fin |**. Neste campo será possível visualizar o valor financeiro considerando a dedução dos tributos em questão. Esta informação não tem “nenhuma” relação com o “valor líquido” do movimento.

* ***Informações Adicionais***

**Composição do Valor do INSS**

O cálculo é feito obedecendo conteúdo da tabela de INSS com vigência a partir de 01/02/2010. O valor será acumulativo no mês até que seja atingido teto máximo 3.416,54(base de cálculo) para dedução, desta forma, o INSS será deduzido no máximo até 375,81(Vr calculado). Por se tratar de “autônomo” será considerada alíquota fixa de 11% sobre o valor do serviço prestado.

**[![clip_image002](http://lh4.ggpht.com/_G7KXZLoZDsY/TKsvoZtPUQI/AAAAAAAABow/yN05GBo1YyA/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKsvnaeYREI/AAAAAAAABos/3B1tWFFft4Q/s1600-h/clip_image002%5B4%5D.jpg)**

**Cálculo do INSS sem Valor Pago em Outra Empresa**

Base de Cálculo: 3.500,00 Teto Máximo de INSS: 3.416,54 Alíquota: 11%

(Base de cálculo x Alíquota) = Valor de INSS

3.416,54 x 11% = 375,81 **Valor do INSS : 375,81**

O cálculo do IRRF é feito considerando conteúdo da tabela progressiva do IRRF com vigência a partir de 2010. O tributo tem cumulatividade mensal até que seja atingido teto máximo de dedução.

[![clip_image004](http://lh4.ggpht.com/_G7KXZLoZDsY/TKsvsYYT9qI/AAAAAAAABo4/G4giCqqWnpE/clip_image004_thumb%5B1%5D.jpg?imgmax=800 "clip_image004")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKsvpRvSHCI/AAAAAAAABo0/M8c2Zoc2Mf0/s1600-h/clip_image004%5B4%5D.jpg)

**Cálculo do IRRF sem dependentes**

Histórico de cálculo

Base de Cálculo: 3.500,00

Valor calculado do INSS: (375,81)

Total para cálculo do IRRF: 3.124,19

Base de cálculo de IRRF: **3.124,19**

Parcela a Deduzir: (505,62)

Alíquota: 22,50%

(Base de cálculo – Vr Calculado do INSS) = Total para cálculo do IRRF

(Total para cálculo do IRRF x Alíquota ) = Valor Calculado de IRRF

(Valor Calculado de IRRF – Parcela a Deduzir) = Valor de IRRF

3.500,00 – 375,81 = 3.124,19

3.124,19 x 22,50% = 702,94

702,94 – 505,62 = 197,32

Importante:

A parcela a deduzir, assim como alíquota para cálculo do IRRF vão obedecer tabela progressiva cadastrada anteriormente no Totvs Gestão Financeira

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Rpt/Rpt.Reports.aspx)

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
