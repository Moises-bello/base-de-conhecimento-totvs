---
content_hash: e9a366e910470de58fc20e3f3f026474f2d04d2ba70f9a57e49d8eda6f18b7e6
fetched_at: '2026-06-29T00:12:02.679948+00:00'
page_id: '90275924'
product: rm
source: tdn-rm
title: RMFIS00003_Geração da Rotina - DACON
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=90275924
version: 9
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.52 |
| **Processo** | **:** | DACON - Demonstrativo de Apuração de Contribuições Sociais |
| **Subprocesso** | **:** | Como gerar a Rotina |
| **Data da publicação** | **:** | 29/10/2013 |

**Introdução**

Estão obrigadas à entrega do **DACON** as pessoas jurídicas de direito privado em geral e as que lhes são equiparadas pela legislação do Imposto de Renda, submetidas à apuração da Contribuição para o PIS/Pasep e da Contribuição para o Financiamento da Seguridade Social (Cofins), nos regimes cumulativo e não-cumulativo, inclusive aquelas que apuram a Contribuição para o PIS/Pasep com base na folha de salários.

O **DACON**, à partir do ano-calendário de 2010, será apresentado de forma centralizada pelo estabelecimento matriz mensalmente, por todas as pessoas jurídicas obrigadas à entrega do **DACON**.

([IN RFB nº 1.015, de 5 de março de 2010](http://www.receita.fazenda.gov.br/Legislacao/Ins/2010/in10152010.htm)). Para o preenchimento do **DACON** deve ser utilizado o programa gerador disponível na página da [RFB](http://www.receita.fazenda.gov.br/pessoajuridica/dacon/DefaultProgramas.htm).

 

**Parâmetros**

Acessar o parâmetro em **Opções | Parâmetros | Gerais / Tabelas | Rotinas Legais | Rotinas Federais | DACON**e informar o diretório onde será criado o arquivo temporário. O processo **DACON** depende do processo de apuração do PIS/PASEP e COFINS, de forma que esses devem estar previamente parametrizados.

 

**Passo a Passo para Geração da Rotina**

**1º Passo: Geração das fichas**

1) Fichas referentes aos Dados Cadastrais 

2) Fichas Especiais 

*Fichas referentes aos **Dados Cadastrais** – Fichas internas do sistema.*

**R01:** Esta ficha recebe os dados iniciais da **DACON**.

O CNPJ do contribuinte, localizado nesta e nas demais fichas, é preenchido com o CNPJ da Filial Matriz, definido nos parâmetros do sistema. A maioria dos campos localizados nesta ficha é preenchida com base nas informações constantes na tela da rotina.

**R02:** Esta ficha recebe os dados cadastrais da empresa definida como Filial Matriz.

**R03:** Esta ficha recebe informações do *Representante* e do *Contador*, definidas para a empresa selecionada como Filial Matriz, na pasta Dados Fiscais do cadastro de Filiais.

**Fichas especiais**

Acessar **Cadastros I Tabelas auxiliares I Obrigações Federais I Dacon**:

Estas fichas são inseridas automaticamente através de um script contido na aplicação. Este script segue o layout da **DACON** 2010. Sendo assim, ao ser executado, são criadas no banco de dados, automaticamente, as fichas: **06A**, **06B**, **07A**, **07B**, **08A**, **08B**, **08C**, **14**, **15A**, **15B**, **16A**, **16B**, **17A**, **17B**, **18A**, **18B**,**18C**, **24**, **25A**, e **25B**.

Após gerar as fichas, faz-se necessário alterar a origem de cada um dos campos contidos nela para que no momento da geração do arquivo da **DACON** o sistema possa identificar o local a partir de onde estas informações serão obtidas. As opções são:

*Contas contábeis*: O usuário poderá definir regras de cálculo dos campos com base no plano de contas. Neste caso, para cada campo o usuário poderá definir quais contas preenchem aquele campo. Os tipos de cálculo disponíveis são: Débito, Crédito, Movimentação, Saldo Anterior e Saldo Atual. Os dois últimos são úteis na definição das fichas referentes ao Ativo e Passivo, que possuem colunas referentes ao Saldo Anterior e Saldo Atual. O sistema irá considerar o valor do rateio gerencial, se existir conta gerencial definida, ou o valor da conta quando ela estiver definida nos lançamentos contábeis. Serão totalizados todos os lançamentos dentro do intervalo de datas definido para a **DACON.**

1. DÉBITO: Conta (Devedora): este valor será somado ao campo da **DACON**, visto que o tipo é débito e a natureza da conta é devedora.
2. CRÉDITO: Conta (Devedora): este valor será subtraído do campo da **DACON**, visto que o tipo é crédito e a natureza da conta é devedora.
3. DÉBITO: Conta (Credora): este valor será subtraído do campo da **DACON**, visto que o tipo é débito e a natureza da conta é credora.
4. CRÉDITO: Conta (Credora): este valor será somado ao campo da **DACON**, visto que o tipo é crédito e a natureza da conta é credora.
5. MOVIMENTAÇÃO: Conta (Devedora) = DÉBITO(Conta) - CRÉDITO(Conta)
6. MOVIMENTAÇÃO: Conta (Credora) = CRÉDITO(Conta) - DÉBITO(Conta)
7. SALDO ANTERIOR: O sistema carregará o total a débito e o total a crédito dos lançamentos contábeis cuja data seja anterior ao início do período da **DACON**.

*Funções:* Habilitando este tipo de origem, o sistema exibirá a pasta “Funções” para configuração do cálculo do campo corrente. O usuário deverá selecionar um Tributo e a Função correspondente para o cálculo. São disponibilizadas as seguintes funções:

* Base Cálculo – Lucro Real (Válida somente para IRPJ e CSLL)

* Valor Imposto – Lucro Real (Válida somente para IRPJ e CSLL)

* Valor Adicional – Lucro Real (Válida somente para IRPJ)

* Base Cálculo – Lucro Presumido (Válida somente para IRPJ e CSLL)

* Valor Imposto – Lucro Presumido (Válida somente para IRPJ e CSLL)

* Valor Adicional – Lucro Presumido (Válida somente para IRPJ)

* Base Cálculo – Lucro Estimado (Válida somente para IRPJ e CSLL)

* Valor Imposto – Lucro Estimado (Válida somente para IRPJ e CSLL)

* Valor Adicional – Lucro Estimado (Válida somente para IRPJ)

* Base Cálculo – Não Cumulativo (Válida somente para PIS e COFINS)

* Valor Imposto – Não Cumulativo (Válida somente para PIS e COFINS)

* Base Cálculo – Cumulativo (Válida somente para PIS e COFINS)

* Valor Imposto – Cumulativo (Válida somente para PIS e COFINS)

*Períodos Fiscais:* É habilitada a pasta “Período Fiscal” onde o usuário deve selecionar o Tributo de origem e o Campo da tabela de Períodos Fiscais que irá preencher o campo editado. Exemplo: o campo será calculado para os Períodos Fiscais de PIS com base no campo “Bens para Revenda”. Neste caso o sistema buscará o(s) período(s) de PIS correspondente ao período da **DACON** e totalizará no campo corrente o Valor dos Créditos do(s) período(s) selecionado(s), ou seja, o somatório.

*Nenhuma:* Serve para gerar espaços em branco ou zeros, evitando problemas de posicionamento no arquivo texto.

Para que sejam visualizadas as fichas criadas, basta clicar no botão “Fichas/ Campos da declaração/ Demonstrativo”, será então exibida à lista contendo todas as fichas já cadastradas.

**Observação:** Para que as fichas sejam inseridas no arquivo no momento de sua geração é necessário editar as fichas e marcar a opção “Gerar”.

*Campos das Fichas*

*Coluna*: A maioria das fichas possui um campo chamado coluna. Na ficha **25B**, por exemplo, existem 2 colunas: Regime não cumulativo e Regime Cumulativo. Isto significa que cada campo da Ficha **25B** será escrito 2 vezes, na primeira linha com o Regime não cumulativo e na segunda linha com o Regime Cumulativo. Por este motivo existem 2 registros para cada campo da Ficha **25B**, exemplo: Ordem: 1 - Cofins Apurada: existem 2 registros para este campo no cadastro da Ficha **25B**, um com a coluna 01 e outro com a coluna 02. Os campos são exibidos ordenados por Coluna e Ordem.

Ordem: Representa a ordem que o campo será escrito no arquivo texto. Para todas as fichas será gerado um cabeçalho que é transparente para o usuário. A partir do campo de Ordem 01, o sistema irá gerar a ficha conforme parametrização do usuário.

**2º Passo – Geração da Rotina:**

Acessar a opção **Rotinas Legais** | **Rotinas Federais** | **Demonstrativo de Apuração de Contribuições Sociais – DACON**

Arquivo texto: Deverá ser informado o nome do arquivo texto a ser gerado pela rotina, sendo que a extensão ‘.imp’ não pode ser alterada, pois a mesma é definida pelo programa Validador da **DACON**.

Situação Especial: Deverá ser selecionado se o demonstrativo se referir a um dos eventos listados. Nestes casos, informar obrigatoriamente a data do evento.

Desenquadramento: Este campo é habilitado somente para empresas imunes e isentas, devendo ser utilizado na hipótese de suspensão ou revogação do gozo da imunidade ou da isenção no curso do mês. Neste caso deverá informar a data do desenquadramento.

Qualificação da Pessoa Jurídica: Selecionar a qualificação da pessoa jurídica entre as alternativas disponíveis.

Tipo de Entidade: Este campo é habilitado somente quando for selecionada no campo "Qualificação da Pessoa Jurídica" a opção "Imune do IRPJ" ou a opção "Isenta do IRPJ".

Versão do PGD: Neste campo deverá ser informada a versão do Programa Gerador do Demonstrativo.

Salvar Preferência do Usuário: Habilitando este campo os campos terão o valor informado como default nas próximas vezes que a tela for acessada. (exceto os campos que se referem às datas).

**Dica:**

Os campos das fichas são disponibilizados para parametrização conforme layout da **DACON**, porém os campos que são calculados pela **DACON** mesmo que sejam preenchidos, serão recalculados pelo programa validador.

Regime: Este campo somente será habilitado quando for selecionado, no campo "Qualificação da Pessoa Jurídica", as alternativas: "PJ em geral" ou "Isenta do IRPJ" (nesta última hipótese, exceto quando selecionarem, no campo "Tipo de Entidade", as alternativas: "Entidade Aberta de Previdência Complementar (Sem Fins Lucrativos)", "Entidade Fechada de Previdência Complementar" ou "Associação de Poupança e Empréstimo").

Os outros campos somente serão habilitados quando for selecionado no campo "Qualificação da Pessoa Jurídica", as alternativas: "PJ em geral", "Imune do IRPJ" ou "Isenta do IRPJ" (nesta última hipótese, exceto quando selecionarem, no campo "Tipo de Entidade", as alternativas: "Entidade Aberta de Previdência Complementar (Sem Fins Lucrativos)", "Entidade Fechada de Previdência Complementar" ou "Associação de Poupança e Empréstimo"), as quais deverão selecionar as opções "Contribuinte" e/ou "Substituto Tributário".

**Outros Dados**

Inclusão no Simples: Este campo será preenchido com “ 0 – Não se aplica” quando for selecionado no campo "Qualificação da Pessoa Jurídica", as alternativas: "Imune do IRPJ" ou "Isenta do IRPJ".

Apuração de créditos sobre operações de importação: Informar se houve apuração de créditos a serem descontados no mercado interno, decorrentes de operações de importação. Este campo somente será habilitado quando for selecionado no campo "Qualificação da Pessoa Jurídica" as alternativas: "PJ em geral" ou "Isenta do IRPJ".

Adição de Contribuição ou Crédito Diferido em meses anteriores: Devem selecionar este campo as pessoas jurídicas que procederam ao diferimento da tributação da Contribuição para o PIS/Pasep e da Cofins em meses anteriores, nos termos da legislação em vigor, e recebeu no mês parcela da receita em relação a qual houve o diferimento das contribuições.

Diferimento de Contribuição ou Crédito no Mês: Devem selecionar este campo as pessoas jurídicas que procederam ao diferimento da tributação da Contribuição para o PIS/Pasep e da Cofins para meses posteriores, nos termos da legislação em vigor.

Método de Determinação dos Créditos: Este campo deve ser preenchido, conforme o regime de apuração da Contribuição para o PIS/Pasep e da Cofins adotado. Ele não será habilitado quando for selecionado no campo "Regime”, as alternativas: "Não se aplica" ou "Regime Cumulativo".

Contribuição e Créditos Diferidos Transferidos de Sucedidas no Mês: Devem selecionar este campo as pessoas jurídicas que, ao sucederem outras pessoas jurídicas, receberam, por transferência, créditos das sucedidas decorrentes do regime de incidência não-cumulativa da Contribuição para o PIS/Pasep e da Cofins, que tenham sido diferidos em meses anteriores nos termos da legislação em vigor.

Desconto no Mês de Créditos Transferidos por PJ Sucedidas: Devem selecionar este campo as pessoas jurídicas sucessoras que descontaram, créditos recebidos das sucedidas por transferência, por eventos ocorridos em meses anteriores ou no mês do Demonstrativo, decorrentes do regime de incidência não-cumulativa da Contribuição para o PIS/Pasep e da Cofins.

Créditos Transferidos de Sucedidas no Mês: Devem selecionar este campo as pessoas jurídicas que, ao sucederem outras pessoas jurídicas, receberam, por transferência, créditos das sucedidas decorrentes do regime de incidência não-cumulativo da Contribuição para o PIS/Pasep e da Cofins,nos termos da legislação em vigor.

Natureza Jurídica: Informe conforme tabela legal, a Natureza Jurídica da Empresa.

Buscar as Retenções de PIS e COFINS no RM Liber ou RM Fluxus: Deverá ser selecionado de onde o sistema irá buscar as informações das (retenções de PIS e COFINS). Caso seja selecionado o RM Fluxus são selecionado lançamentos a Pagar ou a Receber que tenha estes tributos.

**Atenção:** Não é possível habilitar os dois campos ao mesmo tempo.

|  |  |
| --- | --- |
| **Registros** | **Sistema Gera** |
| Registro Header– Informações do Contribuinte | Sim |
| Registro Tipo 9 – Encerramento | Sim |
| R01 - Ficha 01 - Dados Iniciais | Sim |
| R02 - Ficha 02 – Dados Cadastrais | Sim |
| R03 - Ficha 03 - Dados do Representante e do Responsável | Sim |
| R04 - Ficha 04A - Cadastro de Produtos Sujeitos a Alíquotas Diferenciadas | Não |
| R04 - Ficha04B - Cadastro de Produtos Sujeitos a Alíquotas Diferenciadas Substituto Tributário | Não |
| R05 - Ficha 05A – Cadastro de Produtos Sujeitos a Alíquotas por Unidade de Medida | Não |
| R05 - Ficha 05B - Cadastro de Produtos Sujeitos à Alíquotas por Unidade de Medida Substituto Tributário | Não |
| R06 - Ficha 06A – Apuração dos Créditos de PIS/Pasep - Aquisições no Mercado Interno Regime Não-Cumulativo | Sim |
| R06 - Ficha 06B - Apuração dos Créditos de PIS/Pasep - Importação Regime Não-Cumulativo | Sim |
| R07 - Ficha 07A - Cálculo da Contribuição para o PIS/Pasep Regime Não-Cumulativo – Incidência Total | Sim |
| R07 - Ficha 07B - Cálculo da Contribuição para o PIS/Pasep Regime Não-Cumulativo – Incidência Parcial | Sim |
| R08 - Ficha 08A - Cálculo da Contribuição Para o PIS/Pasep Regime Cumulativo | Sim |
| R08 - Ficha 08B - Cálculo da Contribuição Para o PIS/Pasep Instituições Financeiras, Seguradoras, Previdência Aberta e Capitalização | Sim |
| R08 - Ficha 08C- Cálculo da Contribuição para o PIS/Pasep Entidades Fechadas de Previdência Complementar | Sim |
| R09 - Ficha 09A - Cálculo da Contribuição para o PIS/Pasep Alíquotas Diferenciadas | Não |
| R09 - Ficha 09B - Cálculo da Contribuição para o PIS/Pasep - Substituto Tributário Alíquotas Diferenciadas | Não |
| R10 – Ficha 10A - Cálculo da Contribuição para o PIS/Pasep Alíquotas por Unidade de Medida de Produto | Não |
| R10 – Ficha 10B – Cálculo da Contribuição para o PIS/Pasep – Substituto Tributário Alíquotas por Unidade de Medida de Produto | Não |
| R11 – Ficha 11 – Controle do Diferimento – Valores Adicionados no Mês – PIS/Pasep | Não |
| R12 – Ficha 12 - Controle do Diferimento – Valores Diferidos no Mês – PIS/Pasep | Não |
| R13 – Ficha 13A - Créditos Descontados no Mês – PIS/Pasep Regime Não-Cumulativo | Não |
| R13 – Ficha 13B - Créditos Descontados no Mês Transferidos por PJ Sucedidas – PIS/Pasep Regime Não-Cumulativo | Não |
| R14 – Ficha 14 - Controle de Utilização dos Créditos no Mês - PIS/Pasep Regime Não-Cumulativo | Sim |
| R15 – Ficha 15A - Resumo – Contribuição para o PIS/Pasep Regime Cumulativo | Sim |
| R15 – Ficha 15B - Resumo - Contribuição para o PIS/Pasep Regime Não-Cumulativo | Sim |
| R16 – Ficha 16A - Apuração dos Créditos da Cofins - Aquisições no Mercado Interno Regime Não-Cumulativo | Sim |
| R16 – Ficha 16B - Apuração dos Créditos da Cofins – Importação Regime Não-Cumulativo | Sim |
| R17 – Ficha 17A - Cálculo da Cofins Regime Não-Cumulativo – Incidência Total | Sim |
| R17 – Ficha 17B - Cálculo da Cofins Regime Não-Cumulativo – Incidência Parcial | Sim |
| R18 – Ficha 18A - Cálculo da Cofins Regime Cumulativo | Sim |
| R18 – Ficha 18B - Cálculo da Cofins Instituições Financeiras, Seguradoras, Previdência Aberta e Capitalização | Sim |
| R18 – Ficha 18C- Cálculo da Cofins Entidades Fechadas de Previdência Complementar | Sim |
| R19 – Ficha 19A – Cálculo da Cofins Alíquotas Diferenciadas | Não |
| R19 – Ficha 19B -  Cálculo da Cofins - Substituto Tributário Alíquotas Diferenciadas | Não |
| R20 – Ficha 20A – Cálculo da Cofins Alíquotas por Unidade de Medida de Produto | Não |
| R20 – Ficha 20B – Cálculo da Cofins – Substituto Tributário Alíquotas por Unidade de Medida de Produto | Não |
| R21 – Ficha 21 -  Controle do Diferimento – Valores Adicionados no Mês – Cofins | Não |
| R22 – Ficha 22 – Controle do Diferimento – Valores Diferidos no Mês – Cofins | Não |
| R23 – Ficha 23A – Créditos Descontados no Mês – Cofins Regime Não-Cumulativo | Não |
| R23 – Ficha 23B – Créditos Descontados no Mês Transferidos por PJ Sucedidas – Cofins Regime Não-Cumulativo | Não |
| R24 – Ficha 24 – Controle de Utilização dos Créditos no Mês – Cofins Regime Não-Cumulativo | Sim |
| R25 – Ficha 25A - Resumo – Cofins Regime Cumulativo | Sim |
| R25 – Ficha 25B - Resumo – Cofins Regime Não-Cumulativo | Sim |
| R26 – Ficha 26A – Saldos de Créditos Não Utilizados Transferidos de Sucedidas – PIS/Pasep | Não |
| R27 – Ficha 27A – Saldos de Contribuições e Créditos Diferidos Transferidos de Sucedidas - PIS/Pasep | Não |
| R28 – Ficha 28A – Saldos de Créditos Não Utilizados Transferidos de Sucedidas – Cofins | Não |
| R29 – Ficha 29A - Saldos de Contribuições e Créditos Diferidos Transferidos de Sucedidas – Cofins | Não |
| R30 – Ficha 30 -  Demonstrativo do PIS/Pasep e da Cofins Retidos na Fonte | Não |

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
