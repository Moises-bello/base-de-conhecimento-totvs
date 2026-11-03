---
content_hash: 1aa323e98c7c8a511c4b2d561560d6d724de450a185247c56d23f9995b588f27
fetched_at: '2026-06-29T00:11:48.581252+00:00'
page_id: '82477744'
product: rm
source: tdn-rm
title: RMFIS00001_Como gerar DIPJ 2014
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00001_Como+gerar+DIPJ+2014
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão:**11.5x |
| **Processo** | **:** | DIPJ 2014 |
| **Subprocesso** | **:** | Geração da rotina |
| **Data da publicação** | **:** | 20/09/2013 - Atualizado - 27/06/2014 |

**Introdução**

A Declaração de Informações Econômico-Fiscais da Pessoa Jurídica – **DIPJ**, instituída pela Instrução Normativa nº 127 de 30/10/1998 deve ser apresentada, de forma centralizada pela matriz, por todas as pessoas jurídicas inclusive as equiparadas, na forma da legislação pertinente. A obrigatoriedade não se aplica às microempresas e empresas de pequeno porte, optantes pelo regime do Sistema Integrado de Impostos e Contribuições das Microempresas e Empresas de Pequeno Porte – SIMPLES, aos órgãos públicos, às autarquias e fundações públicas, e às pessoas jurídicas inativas, conforme definidas em ato da Secretaria da Receita Federal do Brasil.

**Local de Entrega**

A DIPJ deve ser transmitida pela Internet, por meio do programa *Receitanet* disponível no endereço [http://www.receita.fazenda.gov.br](http://www.receita.fazenda.gov.br/)

**PERIODICIDADE**

* A periodicidade da apresentação é Anual.

**Desenvolvimento/Procedimento**

**DIPJ** – Declaração de Informações Econômico- Fiscais da Pessoa Jurídica

A geração da **DIPJ** poderá ser dividida em 3 etapas:

**1) Fichas referentes aos dados cadastrais;**

* **Fichas referentes aos Dados Cadastrais – Informações geradas a partir do Cadastro da Filial:**

**R01 - **Dados Iniciais****

Esta ficha recebe os dados iniciais da **DIPJ**. O CNPJ do contribuinte, localizado nesta e nas demais fichas, é preenchido com o CNPJ da Filial Matriz. A Filial Matriz é informada no campo Filial Matriz do Estabelecimento em **Opções | Parâmetros | Gerais / Tabelas Etapa 15 –Geração de Guias Darf**.

 **Atenção -**

O sistema somente gera a rotina se o campo Filial Matriz do Estabelecimento estiver preenchido nos parâmetros supracitados.

**R02 - **Dados Cadastrais**** 

Esta ficha recebe os dados cadastrais da empresa definida como Filial Matriz.

**R03 - **Dados do Representante e do Responsável****

Esta ficha recebe informações do Representante e do Contador, definidas para a empresa selecionada como Filial Matriz, na pasta Dados Fiscais do cadastro de Filiais.

**2) Geração de fichas que referenciam os Lançamentos Fiscais;**

* **Fichas que referenciam os Lançamentos Fiscais – informações geradas a partir dos Lançamentos Fiscais :**

 Serão selecionados os Lançamentos Fiscais da Coligada corrente, pertencentes ao intervalo de filiais selecionado na tela da rotina, dentro do período informado. O Status deve ser diferente de “Cancelado”. Além disso, a Natureza de Operação associada aos Lançamentos Fiscais deve se encontrar com o campo Natureza com ICMS/IPI habilitado e estes Lançamentos Fiscais devem possuir no mínimo um item cadastrado.

**R19/Ficha19 - Estabelecimentos Industriais ou Equiparados**

Todos os estabelecimentos, pertencentes à mesma pessoa jurídica, que realizem as operações descritas na letra "m" das instruções da Abertura Ficha Nova Declaração, devem ser relacionados nesta ficha.

Observar as seguintes instruções de preenchimento: 

**Código/Tipo de Estabelecimento:**

Indicar, neste campo, o código do tipo de estabelecimento conforme Tabela de Classificação do Estabelecimento, disponível na Caixa de Combinação e constante destas instruções de preenchimento, com o respectivo embasamento legal.

√  **Campo Informado no Cadastro da Filial**

Recebe a informação localizada no campo de mesmo nome da pasta Dados Fiscais no Cadastro de Filiais

**R20/ Ficha 20 - Apuração do Saldo do IPI**

Esta ficha é gerada conforme períodos de IPI cadastrados no Sistema TOTVS Gestão Fiscal, recebe informações referentes à apuração do IPI. Serão geradas informações para os 3 decêndios de todos os meses que englobam o período informado na tela da rotina. Se o campo Apuração Mensal do IPI estiver habilitado, será gerado um registro para cada mês com o decêndio 0 (zero). Se o campo IPI Quinzenal estiver habilitado, serão geradas duas linhas para cada mês, uma para primeira quinzena e outra para segunda quinzena

 **Atenção -**

O sistema estará selecionando todos os períodos de IPI que se encontram dentro do período informado na tela da rotina, ordenando por Data Inicial e Data Final. Para cada registro encontrado, será gerada uma *linha 29* correspondente. Para a correta geração desta ficha, os períodos de IPI deverão se encontrar encerrados e parametrizados com as datas conforme periodicidade.

**R21/Ficha 21 - Entradas e Créditos** 

Esta ficha refere-se às entradas e aos créditos de IPI no período. O sistema gera 3 linhas deste registro, uma para a coluna “Com Créditos”, outra para coluna “Sem Créditos” e outra para a coluna “IPI Creditado”.

O campo “Estorno de Débitos” recebe o total dos valores dos lançamentos de outros débitos e créditos do tipo “Estorno Débito” e subtipo “Não se aplica” de todos os períodos de IPI dentro do período de geração da **DIPJ**. O campo “Outros” se refere ao tipo “Crédito” e subtipo “Não se aplica”.

**R22/Ficha 22 - Saídas e Débitos**

A ficha 22 é semelhante à ficha 21, porém refere-se às saídas e débitos do IPI. As duas últimas fichas, recebem também informações referentes aos Outros Débitos, Créditos, Estorno de Débitos, Estorno de Créditos e Deduções. Estes valores serão carregados a partir dos Lançamentos de Outros Débitos / Créditos para o IPI, porém os períodos fiscais devem se encontrar encerrados.

O campo “Estorno de Créditos” recebe o total dos valores dos lançamentos de outros débitos e créditos do tipo “Estorno Crédito” e subtipo “Não se aplica” de todos os períodos de IPI dentro do período de geração da **DIPJ**. Os campos “Transferência de Créditos”, “Ressarcimento de Créditos” e “Outros” se referem ao tipo “Débito” e subtipos “Transferência de Crédito”, “Ressarcimento de Crédito” e “Não se aplica”, respectivamente.

**R23/Ficha 23 - Remetentes de Insumos/Mercadorias**

**R25/Ficha 25 - Destinatários de Produtos/Mercadorias/Insumos** 

Estas fichas referem-se às informações dos Remetentes / Destinatários de Produtos / Mercadorias / Insumos. Serão totalizados a Base IPI com Isentos IPI e Outros IPI no campo *Valor* destas fichas e Valor ST no campo Substituição Tributária. Este somatório será agrupado por Cliente/Fornecedor. Informar, por ordem decrescente de valor, os dados dos maiores destinatários de produtos e fornecedores, mercadorias e/ou insumos (inclusive isentos, alíquota zero, com suspensão, imunes e não tributados).

O campo CNPJ/CPF estará recebendo o CNPJ/CPF do Cliente/Fornecedor envolvido na operação.

Nestas fichas serão selecionados os Lançamentos Fiscais não Cancelados e não Estornados. Além disso, o campo “Natureza Fiscal” do Cadastro de Naturezas de Operação, deverá se encontrar habilitado.

Serão considerados os seguintes *CFOP's(Entrada)*: 1.101, 1.102, 1.111, 1.113, 1.116, 1.117, 1.118, 1.120, 1.121, 1.122, 1.124, 1.125, 1.126, 1.151, 1.152, 1.154, 1.401, 1.403, 1.408, 1.409, 1.410, 1.411, 1.414, 1.415, 1.501, 1.503, 1.504, 1.901, 1.902, 1.903, 1.904, 1.905, 1.906, 1.907, 1.908, 1.909, 1.910, 1.911, 1.912, 1.913, 1.914, 1.915, 1.916, 1.917, 1.918, 1.919, 1.920, 1.921, 1.922, 1.923, 1.924, 1.925, 1.926, 1.949, 2.101, 2.102, 2.111, 2.113, 2.116, 2.117, 2.118, 2.120, 2.121, 2.122, 2.124, 2.125, 2.126, 2.151, 2.152, 2.154, 2.401, 2.403, 2.408, 2.409, 2.410, 2.411, 2.414, 2.415, 2.501, 2.503, 2.504, 2.901, 2.902, 2.903, 2.904, 2.905, 2.906, 2.907, 2.908, 2.909, 2.910, 2.911, 2.912, 2.913, 2.914, 2.915, 2.916, 2.917, 2.918, 2.919, 2.920, 2.921, 2.922, 2.924, 2.925, 2.949, 3.101, 3.102, 3.126, 3.127, 3.503, 3.530 e 3.949.

Serão considerados os seguintes CFOP's(Saída): 5.101, 5.102, 5.103, 5.104, 5.105, 5.106, 5.109, 5.110, 5.111, 5.112, 5.113, 5.114, 5.115, 5.116, 5.117, 5.118, 5.119, 5.120, 5.122, 5.123, 5.124, 5.125, 5.151, 5.152, 5.155, 5.156, 5.401, 5.402, 5.403, 5.405, 5.408, 5.409, 5.414, 5.415, 5.501, 5.502, 5.503, 5.901, 5.902, 5.903, 5.904, 5.905, 5.906, 5.907, 5.908, 5.909, 5.910, 5.911, 5.912, 5.913, 5.914, 5.915, 5.916, 5.917, 5.918, 5.919, 5.920, 5.921, 5.922, 5.923, 5.924, 5.925, 5.949, 6.101, 6.102, 6.103, 6.104, 6.105, 6.106, 6.107, 6.108, 6.109, 6.110, 6.111, 6.112, 6.113, 6.114, 6.115, 6.116, 6.117, 6.118, 6.119, 6.120, 6.122, 6.123, 6.124, 6.125, 6.151, 6.152, 6.155, 6.156, 6.401, 6.402, 6.403, 6.404, 6.408, 6.409, 6.502, 6.503, 6.505, 6.901, 6.902, 6.903, 6.904, 6.905, 6.906, 6.907, 6.908, 6.909, 6.910, 6.911, 6.912, 6.913, 6.914, 6.915, 6.916, 6.917, 6.918, 6.919, 6.920, 6.921, 6.922, 6.923, 6.924, 6.925, 6.949, 7.101, 7.102, 7.105, 7.106, 7.127, 7.501 e 7.949.

**R24/Ficha 24 - Entradas de Insumos/Mercadorias**

**R26/Ficha 26 - Saídas de Produtos/Mercadorias/Insumos**

Nestas fichas serão informados os produtos associados aos itens de operações de entrada e saída. Por ordem decrescente de valor.

Serão considerados os seguintes *CFOP's*(Entrada):  1.101, 1.102, 1.111, 1.113, 1.116, 1.117, 1.118, 1.120, 1.121, 1.122, 1.124, 1.125, 1.126, 1.151, 1.152, 1.154, 1.401, 1.403, 1.408, 1.409, 1.410, 1.411, 1.414, 1.415, 1.501, 1.503, 1.504, 1.901, 1.902, 1.903, 1.904, 1.905, 1.906, 1.907, 1.908, 1.909, 1.910, 1.911, 1.912, 1.913, 1.914, 1.915, 1.916, 1.917, 1.918, 1.919, 1.920, 1.921, 1.922, 1.923, 1.924, 1.925, 1.926, 1.934, 1.949, 2.101, 2.102, 2.111, 2.113, 2.116, 2.117, 2.118, 2.120, 2.121, 2.122, 2.124, 2.125, 2.126, 2.151, 2.152, 2.154, 2.401, 2.403, 2.408, 2.409, 2.410, 2.411, 2.414, 2.415, 2.501, 2.503, 2.504, 2.901, 2.902, 2.903, 2.904, 2.905, 2.906, 2.907, 2.908, 2.909, 2.910, 2.911, 2.912, 2.913, 2.914, 2.915, 2.916, 2.917, 2.918, 2.919, 2.920, 2.921, 2.922, 2.923, 2.924, 2.925, 2.934, 2.949, 3.101, 3.102, 3.126, 3.127, 3.503 e 3.949.

Serão considerados os seguintes *CFOP's*(Saída):  5.101, 5.102, 5.103, 5.104, 5.105, 5.106, 5.109, 5.110, 5.111, 5.112, 5.113, 5.114, 5.115, 5.116, 5.117, 5.118, 5.119, 5.120, 5.122, 5.123, 5.124, 5.125, 5.151, 5.152, 5.155, 5.156, 5.401, 5.402, 5.403, 5.405, 5.408, 5.409, 5.414, 5.415, 5.501, 5.502, 5.503, 5.901, 5.902, 5.903, 5.904, 5.905, 5.906, 5.907, 5.908, 5.909, 5.910, 5.911, 5.912, 5.913, 5.914, 5.915, 5.916, 5.917, 5.918, 5.919, 5.920, 5.921, 5.922, 5.923, 5.924, 5.925, 5.949, 6.101, 6.102, 6.103, 6.104, 6.105, 6.106, 6.107, 6.108, 6.109, 6.110, 6.111, 6.112, 6.113, 6.114, 6.115, 6.116, 6.117, 6.118, 6.119, 6.120, 6.122, 6.123, 6.124, 6.125, 6.151, 6.152, 6.155, 6.156, 6.401, 6.402, 6.403, 6.404, 6.408, 6.409, 6.502, 6.503, 6.505, 6.901, 6.902, 6.903, 6.904, 6.905, 6.906, 6.907, 6.908, 6.909, 6.910, 6.911, 6.912, 6.913, 6.914, 6.915, 6.916, 6.917, 6.918, 6.919, 6.920, 6.921, 6.922, 6.923, 6.924, 6.925, 6.949, 7.101, 7.102, 7.105, 7.106, 7.127, 7.501 e 7.949.

**Classificação Fiscal**

Informar, na primeira linha da segunda coluna da ficha, a classificação fiscal do insumo/mercadoria adquirido pelo declarante, constante da Tipi, e vigente na data da operação, que seja o mais representativo, em termos de valor, durante o ano de apuração. O campo Classificação Fiscal receberá o Código NCM, localizado no Cadastro de Produtos.

**R57/Ficha 57 - Demonstrativo do Imposto de Renda, CSLL e Contribuição Previdenciária Retidos na Fonte (LR, LP e LA)**

O sistema estará totalizando os Outros Tributos dos Lançamentos Fiscais (Base de Cálculo e Valor), agrupando por CNPJ da Filial, Código de Receita do Tributo (Cadastro de Tributos) e CNPJ/CPF do Cliente/Fornecedor.

Serão considerados os Lançamentos Fiscais de Saída de todas as filiais que se encontrem dentro do intervalo de filiais informado na tela da rotina, dentro do período, também informado na tela da rotina. Também considerando somente os Lançamentos Fiscais não Cancelados cujo CFOP associado seja Fiscal, ou seja, campo “Natureza Fiscal” habilitado. Os tributos considerados para a geração desta ficha serão do tipo IRRF e CSLL (Cadastro de Tributos). O novo campo “Órgão Público Federal” será preenchido de acordo com o campo “Órgão Público” do cadastro de Cliente/Fornecedor.

**Atenção**

O campo **Forma de Determinação da Base de Cálculo** para as fichas 11 e 16 da **DIPJ** 2006 será preenchidos com o valor 0 - Com Base na Receita Bruta e Acréscimos para Lucro Estimado. Já para Lucro Real, é preenchido com o valor 1 - Com Base em Balanço ou Balancete de Suspensão ou Redução. Portanto, para preencher este campo automaticamente, estaremos verificando mês a mês qual é a forma de tributação válida para o tributo no mês: IRPJ (R11) e CSLL (R16). Neste caso, o sistema estará consultando o cadastro de Vigência de Eventos Tributários.

Se a forma de tributação é Lucro Estimado, o campo na DIPJ receberá o valor "0". Se for Lucro Real, o sistema estará preenchendo o valor "1". "0" será o valor default, caso a parametrização no cadastro de vigências e eventos não esteja correta.

**3) Geração das fichas especiais (baseadas no plano de contas contábeis ou períodos fiscais)**

* **Fichas Especiais – Informações geradas a partir definidas no Cadastro da DIPJ:**

 Algumas fichas não relacionadas anteriormente poderão ser geradas utilizando o novo cadastro de layouts da **DIPJ**, implementado no Sistema de Gestão Fiscal. Este cadastro encontra-se no menu **Cadastro \ Tabelas Auxiliares \ Obrigações Federais \ DIPJ.**

 Através deste recurso, poderão ser geradas fichas como 04A, 05A,05C, 06A, 09A, 10, 11, 12A, 16 e outras. A maioria destas fichas possui informações relacionadas ao plano de Contas Contábeis, outras relacionadas a campos dos Períodos Fiscais e outras associadas a funções de cálculo como BC IRPJ (Lucro Real). Por este motivo implementamos este cadastro onde o usuário estará definindo as regras para o cálculo de cada um dos campos destas fichas.

√  **Cadastro de DIPJ:**

**Cadastro\Tabelas Auxiliares\Obrigações Federais\DIPJ**. Neste cadastro o usuário estará definindo a descrição e a vigência do layout da **DIPJ** selecionado

Neste Cadastro serão informados os *Layout´s* para geração da rotina **DIPJ/DACON**, de acordo com o layout pré-estabelecido pela Receita Federal. O usuário deverá definir as fichas e campos a ser gerados, as regras de acordo com os Períodos Fiscais ou as Movimentações de Contas Contábeis do RM Saldus. Por esta opção, são cadastrados os períodos de Vigências e a descrição do layout da DIPJ/ DACON selecionado.

Após cadastrar a **DIPJ** – Selecionar a **DIPJ** e no Ícone Gerar Fichas/Campos **DIPJ**2014. Essa opção irá gerar automaticamente todas as fichas e campos da **DIPJ** Layout 2014

Após gerar as Fichas é necessário editar as Fichas e Campos através do Ícone **‘Fichas/Campos da Declaração/Demonstrativos’**

√ **Pasta Identificação - Fichas**

**Código da Ficha:**

Informe o código da Ficha.

**Gerar**

Através deste campo o sistema gerará ou não a ficha.

**Descrição:**

Informe a descrição da Ficha.

**Periodicidade:**

Informe a periodicidade de acordo com a Ficha, Anual, Mensal ou Trimestral

**√ Observação:**

**Caso a Ficha seja Mensal o sistema irá habilitar os campos Mês Inicial e Mês Final. Os campos devem ser preenchidos, pois algumas Fichas da DIPJ possuem meses específicos independente do período da rotina. Se uma determinada Ficha deve ser gerada somente para os meses de 02 a 12, esses valores deverão ser informados e a linha referente a Janeiro não será gerada**

√  **Pasta Identificação Campos**

**Coluna:**

Informe a coluna. Representa a coluna que o campo será escrito no arquivo texto.

**Ordem:**

Informe a ordem. Representa a ordem que o campo será escrito no arquivo texto.

**Tamanho:**

Informe o tamanho. Representa o tamanho do campo no arquivo texto.

**Formato:**

Informe se o campo é do tipo Caractere ou Numérico.

√  **Observação:**

O Formato Caractere será válido apenas para Origem igual a “Nenhuma”. Este recurso é utilizado para que o validador da rotina não encontre erros referentes a posicionamentos.

Digamos que existe um campo do tipo caractere no layout que deve receber 10 espaço sem branco. Este campo deve ser informado com o Formato = Caractere, Tamanho = 10 e Origem = Nenhuma. Se este mesmo campo deve ser escrito com zeros, o Formato deverá ser Numérico.

* **Origem:**

Informe o tipo de origem do campo. As opções são origem Conta Contábil, Período Fiscal, ou “Nenhuma”.

**√ Observação**:

O tipo de origem “Nenhuma” serve para gerar espaços em branco ou zeros, de acordo com a definição do campo Formato, evitando problemas de posicionamento de campos no arquivo texto.

√  **Pasta Identificação - Contas Contábeis - Campos**

Conforme a Origem informada será apresentada a Pasta Contas Contábeis

Por esta opção o usuário deverá definir regras de cálculo dos campos com base no Plano de Contas Contábil/Gerencial. Neste caso, para cada campo da ficha o usuário poderá definir quais contas contábeis preencherão aquele campo. Poderá ser incluídos ainda filtros por Filial, Departamento, Centro de Custo e Rateios Gerenciais específicos para buscar as movimentações das contas no RM Saldus.

**Tipo:**Informe que tipo de totalização será feita, com base nas Contas Contábeis, ou seja, o que será considerado para totalização e composição deste campo na rotina. O sistema estará considerando a natureza da Conta (Credora ou Devedora).

√ **As opções são**:

**Débito:** Conta (Devedora): este valor será somado ao campo da DIPJ, visto que o tipo é débito e a natureza da conta é devedora. 

**Débito:**Conta (Credora):este valor será subtraído do campo da DIPJ, visto que o tipo é débito e a natureza da conta é credora. 

**Crédito:**Conta (Devedora): este valor será subtraído do campo da DIPJ, visto que o tipo é crédito e a natureza da conta é devedora.

**Crédito:** Conta (Credora): este valor será somado ao campo da DIPJ, visto que o tipo é crédito e a natureza da conta é credora

**Movimentação:**Conta (Devedora) = Débito (Conta) – Crédito (Conta)

**Movimentação:**Conta (Credora) = Crédito (Conta) – Débito (Conta)

**Saldo Anterior:** o sistema estará carregando o total a débito e o total a crédito dos lançamentos contábeis cuja data seja anterior ao início do período da **DIPJ**. Feito isto, estará efetuando o seguinte cálculo:

Conta (Devedora) = (Total Débito Anterior - Total Crédito Anterior) + Saldo Acumulado

Conta (Credora) = (Total Crédito Anterior - Total Débito Anterior) - Saldo Acumulado

O Saldo Acumulado é o Saldo Anterior da conta no RM Saldus.

**Saldo Atual:** o sistema estará carregando o Saldo Anterior + Movimentação da conta.

**Conta Contábil:**

Informe a conta contábil a ser utilizada na totalização.

√  **Observação:**

Poderá informar Contas de qualquer Nível, assim, se tiver um Grupo de Contas de Receitas, e todas interferirem no cálculo, basta informar o nível sintético.

Se o resultado for negativo, o sistema estará gerando o campo zerado. O campo será informado no log **DIPJxxxx**(Anos).**ERR**.

O sistema estará considerando o valor do rateio gerencial, se existir conta gerencial definida, ou o valor da conta quando ela estiver definida nos lançamentos contábeis. Serão totalizados todos os lançamentos dentro do intervalo de datas definido para a **DIPJ**. No caso de fichas mensais, será totalizado dentro do mês a ser gerado, ou seja, uma conta X definida para um determinado campo de uma ficha mensal, será totalizada 12 vezes, uma para cada mês.

**Atenção**

Os Lançamentos contábeis associados a Histórico de Fechamento não serão selecionados no cálculo das movimentações contábeis para **DIPJ/DACON**.

**Exemplo:**

Conta 1.1.1.001 (Débito) R$1.000,00

Conta 1.1.1.001 (Crédito)R$1.000,00 (Histórico Padrão x)

Digamos que no exemplo acima o Histórico Padrão x esteja definido como Histórico de Fechamento.

Considerando o Histórico Padrão x a movimentação desta conta seria 0 (zero), pois o sistema estaria calculando da seguinte forma: (1000 - 1000). Desconsiderando o Histórico a movimentação será 1000, pois o lançamento a crédito não será considerado.

* **Dentro da Pasta de Contabilidade temos 03 Opções de Filtros**

√  **Pasta Faixa de C.Custo**

**Atenção**

Caso não queira informar uma faixa de Centro de Custo, basta deixar o Código (Final) em branco.

Para excluir um Centro de Custo cadastrado indevidamente, marque-o e clique no ícone "excluir".

Para excluir todos Centro de Custo cadastrado indevidamente, clique no ícone "Excluir Todos".

**√ Pasta Contas Gerencias**

**√ Atenção:**

Se associar uma Conta Contábil analítica que não tenha rateio gerencial o sistema não irá permitir que seja associada uma Conta Gerencial.

Se associar uma Conta Contábil sintética que tenha rateio gerencial em qualquer conta analítica do seu grupo o sistema irá permitir que seja associada uma Conta Gerencial.

√  **Pasta Histórico Padrão**

Nesta pasta poderá definir os Históricos Padrões que deverão ser desconsiderados no cálculo dos valores (SALDO MOVIMENTAÇÃO, SALDO DA CONTA, ETC.)

 Informe o Histórico Padrão, ou digite o primeiro número e clique, para que sejam mostrados todos os históricos cadastrados que iniciem com o número informado. Escolha o desejado, desta forma, o campo já será preenchido automaticamente.

* **Pasta Funções - Campos**

Através desta opção será possível informar Funções para preencher os campos das Fichas **DIPJ/DACON**. Somente poderão ser selecionados tributos dos tipos: IRPJ, CSLL, PIS e COFINS

**Tributo:**

Informe o Tributo para o preenchimento deste campo.

**Função:**

Informe qual Função será utilizada para o preenchimento do campo. 

 √ Para o tributo **IRPJ** as seguintes Funções poderão ser utilizadas:

Base de Cálculo - Lucro Real

Valor Imposto - Lucro Real

Valor Adicional - Lucro Real

Base de Cálculo - Lucro Presumido

Valor Imposto - Lucro Presumido

Valor Adicional - Lucro Presumido

Base de Cálculo - Lucro Estimado

Valor Imposto - Lucro Estimado

Valor Adicional - Lucro Estimado

√  Para o tributo **CSLL** as seguintes Funções poderão ser utilizadas:

Base de Cálculo - Lucro Real

Valor Imposto - Lucro Real

Base de Cálculo - Lucro Presumido

Valor Imposto - Lucro Presumido

Base de Cálculo - Lucro Estimado

Valor Imposto - Lucro Estimado

√ Para os tributos **PIS** e **COFINS** as seguintes Funções poderão ser utilizadas:

Base de Cálculo – Não Cumulativo

Valor Imposto – Não Cumulativo

Base de Cálculo – Cumulativo

Valor Imposto – Cumulativo

**Atenção**

Durante a geração da **DIPJ**, ao encontrar um campo calculado através de uma Função vinculada a um tributo, o sistema estará realizando as seguintes tarefas:

 Serão selecionados todos os períodos fiscais do tributo selecionado que se encontram dentro do período da **DIPJ**, visto que as Funções serão calculadas com base nos campos dos períodos que deverão se encontrar encerrados. Se a ficha a ser calculada é Mensal, o sistema estará selecionando os períodos mês a mês, visto que cada mês estará gerando uma linha na **DIPJ** para a ficha.

Os períodos fiscais serão ordenados pela data. Para funções referentes ao regime Lucro Real o sistema estará posicionando no último período, visto que os valores são acumulados no último período para este regime. Nos demais tipos, o sistema estará percorrendo período a período, calculando o valor correspondente à função e acumulando no campo corrente da **DIPJ**.

Ao final do cálculo, se o valor do campo for negativo, o valor do mesmo na **DIPJ** será 0 (zero) e o campo será acrescentado no **LOG** da rotina. **DIPJxxxx.ERR**.

**Pasta Período Fiscal – Campos**

Esta pasta será exibida ser for informado a Origem igual a Período Fiscal na Pasta Identificação de campos . O usuário deverá definir o Tributo de origem e o Campo da tabela de Períodos Fiscais que estará preenchendo o campo editado.

**Tributo Origem:**

Informe de qual o tributo serão buscados os dados para preenchimento deste campo

**Campo Origem:**

Informe qual campo do cadastro de período, referente ao tributo anteriormente selecionado, será utilizado para preenchimento deste campo da rotina. Será exibido o nome da coluna na tabela, bem como a descrição deste no Cadastro.

**Observação:**

- O campo Saldo Credor/Devedor do período foi retirado da lista de Campos pois este pode receber valores negativos, como saldo devedor e a **DIPJ** deixou de receber valores negativos.

- Nas fichas mensais, o sistema estará somando o campo selecionado para todos os períodos do tributo de origem que se encontrem dentro de cada mês da **DIPJ**, ou seja, para cada mês da **DIPJ**, o sistema estará selecionando os períodos, totalizando e gerando a ficha.

**Exemplo:**

O campo será calculado para os Períodos Fiscais de INSS com base no campo Valor dos Créditos. Neste caso o sistema estará buscando o(s) período(s) de INSS correspondente ao período da DIPJ e totalizando no campo corrente o Valor dos Créditos do(s) período(s) selecionado(s), ou seja, estará realizando um somatório

**Tela de Geração da Rotina**

**Informe os campos:**

**Modelo:**

Informe o modelo a ser gerado..

**√ Observação:**

Esse modelo deve ser de acordo com o layout que deseja validar a rotina

**Filial Inicial:**

Informe a Empresa / Filial Inicial a qual será gerado o arquivo.

**Filial Final:**

Informe a Empresa / Filial Final a qual será gerado o arquivo

**Período de Atividade:**

Informado pela Matriz na Ficha Nova Declaração.

Entretanto, se for o caso de período de atividade diferente daquele informado para a matriz, este campo deverá ser preenchido com o período de atividade no ano-calendário de 2012, relativo a cada estabelecimento.

**Situação Especial:**

Informe se a Empresa se enquadra em Situações Especiaisconforme a tabela apresentada.  
Se o Ano de Calendário for 2012, então informar 0 Não se Aplica

As opções são:

0 – Não se Aplica

1 – Extinção

2 – Fusão

3 – Incorporação / Incorporada

4 – Cisão Total

5 – Cisão Parcial

**Classificação de Municípios:**

Informe a Classificação de Municípios que será utilizada na geração da rotina. A Classificação de Município é cadastrada em Cadastros | Tabelas Auxiliares | Classificação de Município. Vem preenchido com o valor default informado em Opções | Parâmetros | Gerais/Tabelas.

**Regime Especial de Substituição Tributária:**

Informe o Regime Especial de Substituição Tributária:

**As opções são:**0 – Não se aplica  
1 – Substituto  
2 – Substituído  
3 – Substituto e Substituído

Caso esteja sujeito a Regime Especial de Substituição Tributária do IPI, conforme IN SRF nº 260, de 18 de dezembro de 2002, assinalar, neste campo, a situação em que se enquadra o contribuinte: substituto ou substituído.

**Data Evento:**

Informe a Data do Evento para a Situação Tributária.

**Arquivo Texto:**

Informe o nome do arquivo texto a ser gerado pela rotina

**√ Observações:**

O nome dos arquivos tem que estar de acordo com o modelo escolhido. Caso escolha o modelo **DIPJ** 2007 o nome deverá ser**DIPJ2007.TXT**, caso escolha o modelo **DIPJ** 2014 o nome deverá ser **DIPJ2014.TXT**, etc

Todos os arquivos gerados por esta rotina, serão gravados no caminho indicado pelo campo “Diretório Arq. Temporários” em **Opções | Parâmetros | Gerais / Tabelas**

Caso haja algum erro na geração dos arquivos, o sistema irá gerar no caminho indicado pelo campo “Diretório Arq. Temporários” em **Opções | Parâmetros | Gerais / Tabelas**

**Declaração Retificadora:**

Informe se a declaração é retificadora

Recibo **DIPJ** Retificada:

Informe o número de recibo constante no recibo de entrega da última **DIPJ** transmitida. 

**Escrituração por Processamento Eletrônico:**

Informe se a Escrituração será por processamento Eletrônico.

Clicar "sim", caso seja optante pelo Convênio ICMS nº 57/95, ou por outro Convênio ICMS, que disponha sobre escrituração por sistema de processamento eletrônico de dados; caso contrário, clicar "não".

**Destino:**

Informe o destino para geração do arquivo  
As opções são:  
Drive A  
Drive B  
Drive C:

√  **Observação:** 

Se a escolha for c:, o arquivo será gravado no caminho indicado pelo campo “Diretório Arq. Temporários” em **Opções | Parâmetros | Gerais / Tabelas**

**Atenção**

O sistema somente gera a rotina se o campo Filial Matriz do Estabelecimento estiver preenchido em **Opções | Parâmetros | Gerais / Tabelas Etapa 15 –Geração de Guias Darf**

**Forma Tributação:**

Informe a forma de Tributação quanto ao IRPJ (Imposto de Renda Pessoa Jurídica ) conforme a tabela apresentada.  
As opções são:  
1 – Real  
2 – Presumido  
3 – Arbitrado  
4 – Real / Arbitrado  
5 – Pres./ Arbitrado  
6 – Imune IRPJ  
7 – Isenta IRPJ  
8 – Real / Presumido  
9 – Real/ Presumido / Arbitrado

**Qualificação:**

Informe a qualificação da Empresa. As opções são:  
0 – Não se Aplica  
1 – PJ em Geral  
2 – Financeira  
3 – Seguradora  
4 - Corretora Autônoma de Seguros

**Atenção**

O Campo não se aplica quando Forma de Tributação = "6" ou Forma de Tributação = "7".

Se a Forma de Tributação = "2" ou Forma de Tributação = "5" ou Forma de Tributação = "8"  ou a Forma de Tributação = "9", o campo só pode ser preenchido com o valor 1.

**Natureza Jurídica:**

Informe conforme tabela legal, a Natureza Jurídica da Empresa

**Apuração IRPJ:**

Informe a forma de Apuração do IRPJ (Imposto de Renda Pessoa Jurídica )   
As opções são:  
0 – Não se Aplica   
1 – Anual  
2 – Trimestral  
3 – Desobrigada

O valor "0" não é permitido para Forma de Tributação = "1" ou "4".   
Se a Forma de Tributação = "2","3" ou "5", obrigatório preencher com "2".   
Se a Forma de Tributação = "8" ou "9", obrigatório preencher com "0".   
O valor "3" só se aplica se Forma de Tributação = "6" ou "7".

**Apuração do IRPJ por Trimestre:**

Informe a forma de Apuração do IRPJ por Trimestre, caso a pessoa jurídica optante pelo Refis, adotar a Forma de Tributação do Lucro: Real/Presumido ou Real/Presumido/Arbitrado

As opções são:  
0 – Não se Aplica   
1 – Real - Estimativa  
2 – Real - Trimestral  
3 – Presumido  
4 – Arbitrado

Se  a Forma de Tributação diferente de "8" e Forma de Tributação diferente de "9", obrigatório preencher com "0".

Para Forma de Tributação = "8" ou "9", utilize cada posição para indicar a forma como foi realizada a Apuração do IRPJ e da CSLL no trimestre (valores "1" a "4"), onde a 1ª posição corresponde ao 1º trimestre, a 2ª posição corresponde ao 2º trimestre e assim sucessivamente.

O valor "0" também deverá ser utilizado para trimestres não incluídos no período da declaração.

**Tipo Entidade:**

Informe o Tipo de Entidade em que a Empresa se enquadra.

Se a Forma de Tributação diferente de "6" e "7", preencher com zeros.   
Para Forma de Tributação = "6"(Imune do IRPJ), aplicam-se os valores "01","02","03" e "99".   
Para Forma de Tributação = "7"(Isenta do IRPJ), aplicam-se os valores de "04" a "12" e "99".

As opções são:  
00 – Não se aplica  
01 – Assist. Social  
02 – Assist. Educacional  
03 – Sind. Trabalhadores  
04 – Associação Civil  
05 – Cultural  
06 – Previdência Privada  
07 – Filantrópica   
08 – Sindicato  
09 – Recreativa  
10 – Científica  
11 – Associação de Poupança ou Empréstimo  
99 – Outras

**Desenquadramento:**

Informe se houve ou não Desenquadramento da Empresa no ano calendário

**Data do Desenquadramento:**

Informe a Data do Desenquadramento

**Observação:**

Este campo somente será editado se o campo acima “Desenquadramento” estiver habilitado

**PIS/Pasep – Cumulativo/Não Cumulativo:**

Informe a forma de Cálculo do PIS/Pasep foi em Regime Cumulativo ou Não Cumulativo

**Métodos Créd. PIS/Pasep Não Cumulativo:**

Caso o regime da Empresa for Não Cumulativo informe os Métodos de Determinação dos Créditos As opções são:

0– Não se Aplica

1 – Receita Total

 2 – Receita Parcial / Exp. Custos 

3 – Receita Parcial / Exp. Receita Bruta

**Trimestres de Lucro Arbitrado:**

Indique se há situação de arbitramento e em quais trimestres. O Campo deve ser preenchido com zeros, se Forma de Tributação diferente de "3" e Forma de Tributação diferente de "4" e Forma de Tributação diferente de "5".  Para Forma de Tributação = "3","4" ou "5", utilize cada posição para indicar a situação de arbitramento("0" ou "1") no trimestre, onde a 1ª posição corresponde ao 1º trimestre, a 2ª posição corresponde ao 2º trimestre e assim sucessivamente.  O valor "0" também deverá ser utilizado para trimestres não incluídos no período da declaração. Apuração e Informações de IPI no Período:

Informe se houve apuração de IPI no período de geração do arquivo.

****√ As informações desta tela é preenchida conforme e necessidade de cada Empresa.****

**Para maiores informações:**

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.DIPJ.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
