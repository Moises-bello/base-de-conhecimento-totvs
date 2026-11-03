---
content_hash: e25fe53316c7b8c6faefcee1c069292a73459c5e62d762cb5a411748081ad62e
fetched_at: '2026-06-29T00:10:19.037596+00:00'
page_id: '4813034'
product: rm
source: tdn-rm
title: CTRC - Conhecimento de Transporte de Entrada
type: documentation
url: https://tdn.totvs.com/display/LRM/CTRC+-+Conhecimento+de+Transporte+de+Entrada
version: 5
---

BLOCK

CTRC - Conhecimento de Transporte de Entrada

FAQ: **CTRC - Conhecimento de Transporte de Entrada**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para utilizar Conhecimento de Transporte em Movimentações de Entrada?

* ***Definição do Processo***

Utilizada pela unidade fiscalizadora para verificar a veracidade das mercadorias descritas na Nota Fiscal com as mercadorias Transportadas(descritas na NF de Conhecimento de Transporte).

Para utilização do CTRC é necessário que sejam inclusos dois tipos de movimento onde será feito o cadastro do CTRC e a indicação da movimentação de Nota Fiscal que será vinculada ao mesmo.

Solução

* ***Parametrizações Necessárias***

Acessar **| Cadastro | Fórmula | Inserir |** e cadastrar fórmula com conteúdo a ser considerado para o valor do CTRC. Esta informação será apresentada no momento de vincular o CTRC á nota fiscal de entrada.

Ex.:MVB

Importante:

- Deve ser inclusa fórmula com conteúdo de “movimento”, observando que, o valor em questão tem que estar calculado no movimento a ser vinculado para que o campo | Valor | do CTRC seja preenchido.

- Esta fórmula vai definir o valor do CTRC, considerando os dados do movimento de “Cadastro de CTRC”

***Parametrização do movimento de “Cadastro de CTRC******”***

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Fis – Dados (Versões antigas)**

- Usar CTRC : Cadastrar CTRC

- Fórmula do Valor do CTRC a Ratear : código de fórmula inclusa anteriormente

**Etapa Fis – Conhecimento de transporte (Versões mais atuais)**

- Tipo de Operação do Conhecimento de Transporte : Cadastrar CTRC

- Fórmula do Valor do CTRC a Ratear : código de fórmula inclusa anteriormente

**Etapa Mov – Transporte**

- Tipo de Frete | **CIF/FOB** : Edita

**Etapa Fis – Natureza**

- Edição : Edita

- Seleção Automática da Natureza : definir tipo de seleção da natureza

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

**Etapa Fis – Escrituração**

- Gerar Escrituração: habilitar

- Tipo Documento Escrituração | Código Default : informar tipo de documento que possua “Código do Modelo do Documento : 08”

- Tipo do Lançamento Fiscal da Transferência: Entrada

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

**Etapa Fis – Tributação**

Incluir e parametrizar os tributos de forma que atenda aos dados a serem apresentados no item ou movimento

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

***Parametrização do movimento de “Nota Fiscal”***

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Fis – Dados (Versões antigas)**

- Usar CTRC : Indicar CTRC

**Etapa Fis – Conhecimento de transporte (Versões mais atuais)**

- Tipo de Operação do Conhecimento de Transporte : Indicar CTRC

**Etapa Mov – Transporte**

- Tipo de Frete | **CIF/FOB** : Edita

**Etapa Fis – Natureza**

- Natureza | Edição : Edita

- Seleção Automática da Natureza : definir tipo de seleção da natureza

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

**Etapa Fis – Escrituração**

- Gerar Escrituração: habilitar

- Tipo Documento Escrituração | Código Default : informar tipo de documento que deve ser apresentado no Totvs Gestão Fiscal ao gerar escrituração.

- Tipo do Lançamento Fiscal da Transferência: Entrada

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

**Etapa Fis – Tributação**

Incluir e parametrizar os tributos de forma que atenda aos dados a serem apresentados no item ou movimento

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

* ***Descrição do Processo***

***Movimento de “Cadastro do CTRC”***

A inclusão do movimento será feita como de costume, porém para termos de CTRC as abas **| Transporte – CTRC |** têm que ser preenchidas.

**Aba Transporte**

O usuário deverá preencher o tipo de frete pertinente movimentação.

**Aba CTRC Dados do Transporte**

Esta aba deve ser preenchida quando houver dados de coleta x entrega da mercadoria.

O preenchimento dos campos **| Estado – Município |** de coleta e entrega vão interferir diretamente na seleção da natureza de operação(se utilizar), onde será obedecida hierarquia a seguir para apresentação dos códigos fiscais.

1ª Hierarquia: A seleção da natureza de operação será feita obedecendo estado preenchido na aba **| CTRC | Dados de Transporte | Local de Coleta |** onde:

- Se a UF da Coleta = UF da Filial: Utiliza: Utiliza Natureza Interna (1.XXX);

- Se a UF da Coleta <> UF da Filial: Utiliza Natureza Interestadual (2.XXX);

Para operações CTRC de Entrada a natureza de operação será apresentada obedecendo a UF de Coleta, visto que, o imposto é devido no estado de início da operação. Assim, a CFOP a ser utilizada será definida considerando UF da Filial onde a movimentação está sendo incluso e a UF UF de coleta da mercadoria.

2ª Hierarquia: A seleção da natureza de operação será feita obedecendo estado do Cli\for preenchida na aba **| Transporte | Cli\For Origem /Destino |** do movimento;

3ª Hierarquia: A seleção da natureza de operação será feita obedecendo estado do Cli\for preenchido na aba **| Identificação | Cliente \ Fornecedor |**

**Aba CTRC – Dados do CTRC**

Deverá preencher as informações pertinentes notas de CTRC a serem “vinculadas” ao mesmo, sendo necessário preencher os campos:

- Quantidade de Notas do CTRC: informar número de notas que serão acobertadas por este CTRC

- Valor das Notas do CTRC: informar o valor líquido das notas que serão acobertadas pelo CTRC

***Movimento de Nota fiscal onde “indica o CTRC”***

As movimentações serão inclusas como de costume, onde o vínculo com movimento de Cadastro de CTRC vai considerar o valor liquido do movimento de nota fiscal.

***Vínculo de CTRC***

- Acessar aba **| Transporte |** e informar o tipo de **| Frete : FOB |**

- Acessar aba **| CTRC | CTRC Inf.na Entrada |** selecionar movimento de “Cadastro de CTRC” incluso anteriormente na opção **| Conhecimentos de Transporte em Aberto |**. A seguir clicar em **| Incluir |** para que a informação seja gravada no campo **| Valor Frete CTRC |**.

Importante:

- O valor da movimentação de “Cadastro de CTRC” será apresentado obedecendo conteúdo da fórmula parametrizada no 1º movimento incluso.

- O tipo do frete preenchido na aba | Transporte | tem que ser do tipo | FOB |

- O cálculo do “Valor Frete CTRC” será feito de forma proporcional considerando “Valor Líquido” do movimento de nota fiscal.

**Dados do Movimento de “Cadastro de CTRC”**

**Valor do CTRC**:1000,00

**Quantidade de Notas do CTRC**: 3

**Valor das Notas do CTRC**: 6.000

Cálculo realizado para composição do valor do | Valor Frete CTRC |

**Valor do CTRC / Valor das Notas do CTRC**

1000 / 6000 = 0,166666

Importante:

O conteúdo do campo **| Valor Frete CTRC |** do movimento a ser vinculado, vai considerar valor acima x valor liquido do movimento.

**Dados do Movimento de Nota Fiscal**

Valor das movimentações

1ª Movimentação:    3500,00

2ª Movimentação:    1700,00

3ª Movimentação:      800,00

Composição do “Valor Frete CTRC”

**Vr Liq.Movimento                     Valor do CTRC                       Cálculo Valor                Frete CTRC**

            3500,00                              1000,00                                 0,166666 x 3500                 583,33

            1700,00                              1000,00                                 0,166666 x 1700                 283,33

              800,00                              1000,00                                 0,166666 x 800                   133,34

* ***Informações Adicionais***

- O sistema vai ratear os valores das notas considerando valor do conhecimento de transporte, consistindo se houve quantidade, ou valor maior do que o informado no movimento de “cadastro de CTRC”. Caso o valor da(s) nota(s) relacionada(s) ultrapasse(m) o valor do movimento de Conhecimento de transporte será apresentado **"O VALOR DESSA NOTA ULTRAPASSA O VALOR DISPONÍVEL PARA RATEIO DO CTRC"**.

- Após vincular o movimento de CTRC á nota fiscal, a movimentação de “Cadastro de CTRC” será apresentada com mensagem “**MOVIMENTO DE CTRC COM NOTAS RATEADAS”,** impedindo que possa ser feita manutenção do mesmo. Para consultar as notas vinculadas ao mesmo deverá acessar o movimento de “Cadastro de CTRC” na aba **| CTRC | Dados do CTRC | Documentos cobertos pelo CTRC |**

- Os dados de CTRC ficam gravados na tabela **|** **TCTRCENTRADA |** onde o campo **“IDMOVCTRC”** se refere ao IDMOV do movimento de “Cadastro de CTRC”, e o campo **“IDMOVNF”** se refere ao IDMOV das movimentações vinculadas ao CTRC.

* ***Escrituração do Movimento de CTRC***

A escrituração dos movimentos será feita como de costume onde o usuário dever acessar **| Opções | Escrituração de Lançamentos – RMLIBER |** e fazer o filtro das movimentações envolvidas (Movimento de CTRC e Movimentos de NF vinculada a CTRC).

Depois de feita escrituração, ao acessar o RMLIBER em **| Cadastro | Manutenção de Lançamentos de Entrada |** editar o lançamento fiscal de CTRC serão apresentadas informações do conhecimento de transporte na aba **| CTRC | Dados do Transporte |.**

As informações pertinentes “Nota fiscal de Entrada – CTRC” não são apresentadas na pasta **| Notas Fiscais que acobertam a Carga Transportada |**, ressaltando que a rotina de escrituração pertence ao aplicativo RMLIBER.
