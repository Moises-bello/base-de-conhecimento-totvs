---
content_hash: cb681d3ad358c6482bc1d2bdc0999e3ee54239c4afaebac7e846a1e4f346e65d
fetched_at: '2026-06-29T00:09:23.907512+00:00'
page_id: '422546150'
product: rm
source: tdn-rm
title: Cadastro de Tributos
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+de+Tributos
version: 85
---

![](https://tdn.totvs.com/download/attachments/422546150/Tributos.png?version=1&modificationDate=1745585024176&api=v2)
]]>#002233#B7F5FF#00DBFFdashedAviso Importante:1%99%

**Procurando informações sobre os tributos da Reforma Tributária?**

Acesse a página  para conferir as orientações específicas sobre o cadastro dos novos tributos exigidos pela RTC.

# Conteúdo

**Conteúdo**

# 1. Sobre

O Cadastro de Tributos é uma entidade essencial do Backoffice, responsável por registrar os impostos que impactam as operações da empresa. Ele permite a criação de uma estrutura tributária básica, necessária para configurar adequadamente os demais processos das jornadas do Backoffice.

No cadastro, são informados detalhes como o Código do Tributo, Tipo do Tributo, Abrangência, e os locais de busca para alíquotas, entre outros aspectos relevantes.

Este cadastro está disponível no módulo **Gestão Fiscal**, sendo acessado através do menu **Cadastros | Tributos**.

# 2. Tela do Cadastro

O cadastro é organizado em duas pastas "**Identificação**" e "**Outros Dados**"

CadastroIdentificaçãoIdentificaçãoIdentificaçãoleftTipo da AlíquotaTipo da Alíquota

**Tipo da Alíquota**: Pode ser variável ou fixa:

1. **Variável**: São tributos que terão variação de alíquota por Natureza Fiscal. Desta maneira, não será informada a alíquota na tabela correspondente. Deve ser informada a alíquota no cadastro de Natureza de Operação   
   associando cada alíquota a seu respectivo imposto. Desta maneira, no momento da inclusão do lançamento, o sistema irá assumir a alíquota de acordo com a Natureza do lançamento;
2. **Fixo:** São tributos que terão uma alíquota fixa, independente do Lançamento Fiscal ou da Natureza de Operação do lançamento. Desta maneira, será informada a alíquota na tabela correspondente. O sistema carregará como default, a alíquota da tabela para cálculo automático do lançamento.
Tipo TributoTipo Tributo

**Tipo Tributo:** Informe de acordo com a lista de opções, qual o tipo de tributo do TOTVS Gestão Fiscal será utilizado para identificação destes nas rotinas do TOTVS Gestão de Estoque, Compra e Faturamento - Exportação de Lançamentos Fiscais / Exportação para Secretaria da Fazenda / DCTF, exemplo:

1. Se informar ICMS, significa que o valor deste tributo terá as mesmas regras do ICMS, ou seja, não será somado ao valor contábil da nota;
2. Se informar IPI, significa que o valor deste será somado ao valor da operação (venda ou compra) e fará parte do valor contábil da nota;
3. Se informar COFINS, será considerado nos cálculos do Imposto para a geração da Rotina Legal DCTF.

**Tributos Municipais:**

| **Sigla** | **Descrição do Tributo** |
| --- | --- |
| IBS | Imposto Sobre Bens e Serviços |
| ISS | Imposto Sobre Prestação de Serviços |
| ISS ST Contratante | Imposto Sobre Prestação de Serviços Situação Tributária Contratante |
| ISS ST Subcontratante | Imposto Sobre Prestação de Serviços Situação Tributária Sub Contratante |

**Tributos Estaduais:**

| **Sigla** | **Descrição do Tributo** |
| --- | --- |
| IBS | Imposto Sobre Bens e Serviços |
| ICMS | Imposto Sobre Circulação de Mercadorias e Serviços |
| ICMS Crédito SN | Crédito de ICMS pelo Simples Nacional |
| ICMS ST | Imposto Sobre Circulação de Mercadorias e Serviços Situação Tributária |
| ICMS ST Complementar | Imposto Sobre Circulação de Mercadorias e Serviços ST Complementar |

**Tributos Federais:**

|  |  |
| --- | --- |
| **Sigla** | **Descrição do Tributo** |
| CBS | Contribuição Sobre Bens e Serviços |
| CIDE | Contribuições de Intervenção no Domínio Econômico |
| COFINS | Contribuições de Intervenção no Domínio Econômico |
| COFINS Importação | Contribuição p/ Financiamento da Seguridade Sobre Operações de Importação |
| COFINS RF | Contribuição p/ Financiamento da Seguridade Retido na Fonte |
| Contribuição Previdenciária | Natureza Tributária das Contribuições à Seguridade Social |
| COSIRF | Contribuição Social e Imposto de Renda Retido na Fonte |
| CSLL | Contribuição Social Sobre o Lucro Liquido |
| CSLLRF | Contribuição Social Sobre o Lucro Liquido RF |
| FUNRURAL | Fundação de Assistência ao Trabalhador Rural |
| INSS | Instituto Nacional do Seguro Social |
| IPI | Imposto Sobre Produtos Industrializados |
| IRPJ | Imposto de Renda Pessoa Jurídica |
| IRRF | Imposto de Renda Retido na Fonte |
| IOF | Imposto sobre Operações Financeiras |
| IRRF Importação | Imposto de Renda Retido Fonte Sobre Operações de Importação |
| IRRF PJ | Imposto de Renda Pessoa Jurídica |
| IS | Imposto Seletivo |
| ITR | Imposto Sobre Propriedade Territorial Rural |
| PIS/PASEP | Programa de Integração Social |
| PIS Importação | Programa de Integração Social Sobre Operações de Importação |
| PIS RF | Programa de Integração Social Retido na Fonte |
| RET | Regime Tributário Especial |
| Retenção de PIS, COFINS e CSLL | Contribuição Social Retida na Fonte |
| Simples Nacional | Regime compartilhado de arrecadação, cobrança e fiscalização de tributos aplicável às Microempresas e Empresas de Pequeno Porte. |

AlíquotaAlíquota

**Alíquota (%):** Informe Alíquota definida pelas Secretarias Estaduais, Receita Federal ou Prefeituras.

Código ReceitaCódigo Receita

**Código Receita:** Informe o Código Receita, de acordo com a tabela disponibilizada pela Receita Federal.

Caso o contribuinte possua mais de um Código da Receita, que varia de acordo com os serviços jurídicos contratados e alíquota a ser aplicada, deverá ser criado tantos tributos do tipo IRPJ quantos forem os códigos cadastrados, para correta geração das Guias de Arrecadação dos Tributos Federais - DARF.   
Na geração da DCTF, o sistema verifica o período em que a guia está vinculada para identificar a Variação do Código da Receita. Em função do período de apuração (Data Inicial e Final do período), o sistema identifica a vigência da variação no cadastro do Código de Receita. Se não existir nenhuma variação cuja vigência compreenda todo o período de apuração, o sistema busca a variação do cadastro de Tributo.

AbrangênciaAbrangência

**Abrangência:**

O campo Abrangência e utilizado para filtrar a lista de Tipo de Tributo conforme o visto abaixo:

* **Federal:**IPI, IRRF, IRPJ, CSLL, PIS/PASEP, COFINS, INSS, CSLL RF, PIS RF, COFINS RF, "Retenção PIS, COFINS E CSLL", IRRF PJ, PIS Importação, COFINS Importação, COSIRF, CIDE, Simples Nacional, RET, Contribuição Previdenciária, IRRF Importação, ITR, Outros, Funrural, CSRF, CBS e IS.
* **Estadual:** ICMS, ICMS ST, ICMS ST Complementar, ICMS Crédito SN, Outros, IBS
* **Municipal:** ISS, ISS ST Contratante, ISS ST Subcontratante, Outros, IBS
PeriodicidadePeriodicidade

**Periodicidade:** Diário, Semanal, Decendial, Quinzenal, Mensal, Trimestral, Bimestral, Quadrimestral, Semestral, Anual e Outros.

Cod. Antecipação TributáriaCod. Antecipação Tributária

**Cod. Antecipação Tributária**: Este campo somente aparece quando o Tipo Tributo for igual a ICMS ST Complementar.

***Tributo COSIRF:*** Será informado na pasta Outros tributos do lançamento fiscal, onde deve ser associado o beneficiário e o código da receita. O código da receita poderá ser carregado automaticamente do cadastro de Cliente/Fornecedor ( Beneficiário), ou do cadastro de tributo caso não tenha sido informado na pasta Dados Fiscais do cadastro do Cliente/fornecedor.

Outros DadosOutros DadosOutros Dados DeckleftTipo Base CálculoTipo Base Cálculo

**Tipo Base Cálculo:** Selecione qual o valor que será considerado como Base de Cálculo para o Tributo, que são:

* Valor Contábil
* Valor Contábil - Valor do IP
* Formula" e "Expressão
FórmulaFórmula

**Fórmula:** Informe qual o código da fórmula que será utilizada para compor a base de cálculo do Tributo.

IncidênciaIncidência

**Incidência:** Imposto incidirá somente em produtos, serviços ou ambos. Selecione lookup do campo.

Procurar Alíquota noProcurar Alíquota no

**Procurar Alíquota no:** Em algumas tabelas do TOTVS Gestão de Estoque, nos tipos de movimento, podemos informar qual o imposto incidente e qual a alíquota que será aplicada para o mesmo. Portanto, neste campo informe qual a alíquota que será utilizada para o cálculo deste imposto que está incluindo. As opções disponíveis são:

22
complete
**Produto:** A alíquota aplicada será a informada no cadastro do produto do TOTVS de Gestão de Estoques, Compras e Faturamento.

23
incomplete
**Tributo:**Do próprio cadastro do tributo.

24
incomplete
**Tipo de Movimento:** A alíquota informada no Tipo de Movimento no TOTVS Gestão de Estoque, Compra e Faturamento.

25
complete
**Estado:**Carrega a alíquota interestadual informada no cadastro de Estado para os tributos ICMS e ICMS ST.

26
incomplete
**Tipo Prod P/Filial**: A alíquota aplicada será a informada no cadastro do tipo de produto por filial do TOTVS de Gestão de Estoques, Compras e Faturamento.

27
incomplete
**Natureza:** A alíquota aplicada será a informada no cadastro de Natureza de Operação do TOTVS Gestão Fiscal.

28
incomplete
**INSS/PJ - Fornecedor**: A alíquota aplicada, será a informada Código de receita do INSS selecionada no Cadastro do Cliente/Fornecedor, em Anexos | Defaults de Cliente/Fornecedor | aba Outros Dados. 

29
complete
**Código de Receita**: Carrega a alíquota informada no Código de Receita que foi selecionado conforme regra abaixo:

1. IRRF, IRRF-PJ: (1) Tipo de Movimento; (2) Anexo Cli/For do Produto; (3) Produto; (4) Cliente/Fornecedor.
2. CSRF, PIS-RF, COFINS-RF, CSLL\_RF e COSIRF: (1) Tipo de Movimento; (2) Carregar o Código de Receita informado no Anexo "Tributos Default de Fornecedores" no Cadastro do Cliente/Fornecedor (exceto a COSIRF).
3. INSS e Funrural: (1) Anexo Cliente/Fornecedor do Produto; (2) Anexo Defaults de Cli/For do Cliente/Fornecedor.

30
complete
**Alíquotas do Simples Nacional**: Será considera a Alíquota Simples localizada na pasta Obrigações Principais | agrupador Simples Nacional (não tem tributo retido, apenas tributos sobre o faturamento, ICMS, IPI e ISS).

31
complete
**Pauta do Produto:** Carrega a alíquota informada no cadastro do Produto em anexos, Pauto do Produto. Essa validação se aplica apenas para os tributos PIS, COFINS, IPI, ICMS e ICMSST. Importante ressaltar que, no caso dos movimentos do módulo "TOTVS Gestão de Estoque, Compras e Faturamento", quando essa opção for selecionada no Tributo e outra opção de "Procurar Alíquota no" seja parametrizada no tipo de movimento, a busca por pauta do produto terá prioridade.

32
complete
**Projeto:** A alíquota aplicada será a informada no cadastro de Projetos do TOTVS Gestão Fiscal, quanto se tratar de tributo do tipo ISS.

34
complete
**Dados Fiscais por UF**: Aplicada de acordo com a UF no lançamento informada no no Anexo do cadastro do Produto.
Retenção na Fonte DEDUZRetenção na Fonte DEDUZ

**Retenção na Fonte DEDUZ:** Ao habilitar o campo Valor Contábil indica que o valor tributo da pasta Outros Tributos será deduzido do Valor Contábil do Lançamento Fiscal.  
Ao habilitar o campo Valor Financeiro indica que o valor do tributo da pasta Outros Tributos será deduzido do Valor Financeiro (Integração com TOTVS Gestão Financeira) do Lançamento Fiscal.  
Ao habilitar os dois campos indica que o valor do tributo da pasta Outros Tributos será deduzido do Valor Contábil e do Valor Financeiro do Lançamento Fiscal.  
***Observação*:** A rotina de escrituração só trata o preenchimento do valor contábil. O valor Financeiro do Lançamento Fiscal não é preenchido pela rotina de escrituração. Sendo assim para correta escrituração de movimentos com retenção deve-se habilitar o campo Retenção na Fonte Deduz Valor Contábil, e na formula do valor liquido do movimento colocar a dedução do tributo.

Defaults ContábeisDefaults Contábeis

**Defaults Contábeis**: Nesta pasta, serão informadas as contas contábeis default para débito e crédito para a contabilização dos lançamentos com o tributo que está sendo incluindo. As contas contábeis defaults informadas nesta pasta poderão ser utilizadas nos eventos contábeis. Utilize o ícone "novo" para incluir uma conta contábil default, abrirá uma janela de edição para que informe a conta contábil.

Valor Mínimo Para Geração de GuiasValor Mínimo Para Geração de Guias

**Valor Mínimo Para Geração de Guias:** Informe o valor mínimo para geração de guias de recolhimento.  
***Observação*:** O campo será visível somente para os tributos do tipo COFINS, CSLL, INSS, IRPJ, IRRF PJ e PIS. Por default, receberá valor zero. Se o valor do campo sendo maior que zero, o sistema passará a controlar guias acumuladas para o tributo, caso contrário o controle não existirá.

Percentual de Adição por DoaçõesPercentual de Adição por Doações

**Percentual de Adição por Doações**: será habilitado para os tributos CSLL e IRPJ.

Percentual aplicável s/Receita - p/AtividadePercentual aplicável s/Receita - p/Atividade

**Percentual aplicável s/Receita - p/Atividade:** Nos campos Grupo de Grupo de Alíquota 1,Grupo de Alíquota 2, Grupo de Alíquota 3 e Grupo de Alíquota 4, deverão ser informadas as alíquotas aplicáveis sobre Receita por Atividade para o cálculo do IRPJ - Lucro Presumido. Os Eventos Tributários deverão ser criados de acordo com o Grupo de Alíquotas informado no cadastro de Tributo, exemplo:

| Grupo de Alíquota 1 | |
| --- | --- |
| Conta | 4.1.1.1.008 (Receita de Serviços) |
| Percentual Aplicável S/ Receita p/Atividade | 8% |

| Grupo de Alíquota 2 | |
| --- | --- |
| Conta | 4.1.1.1.009 (Receita de Venda) |
| Percentual Aplicável S/ Receita p/Atividade | 12% |

No cadastro do Evento Tributário, pasta Regras Tributárias | aba Exclusões da Receita foram selecionadas as contas do Grupo de Alíquota 1 e 2 (4.1.1.1.008 e 4.1.1.1.009)  
**Resultado**: Em Exclusões, deverão ser informadas as contas de Exclusões da Receita referentes as Receitas 1 e 2 respectivamente.

***Atenção!***  Alguns campos são habilitados para tipo de tributo específicos conforme tabela abaixo:

|  |  |
| --- | --- |
| **Campo** | **Tipo de Tributo** |
| % Compensação Prejuízo | IRPJ e CSLL |
| % Compensação Base Negativa | CSLL |
| Alíquota de IR Adicional | IRPJ |
| Valor Parcela Isenta IR | IRPJ |
| Valor Mínimo de Guia | IRPJ, IOF, CSLL, PIS, COFINS, CPMF, ITR, INSS, IRPF, IRRFPJ, PISIMPORT, ICMSSTCOMPLEMENTAR, COSIRF, CIDE, SIMPLESNACIONAL, OUTROS, ISS e ICMS. |
| Natureza Orçamentária | IRRF, CSRF, CSLL RF, PIS RF e COFINS RF |
| Percentual aplicável s/Receita - p/Atividade | CSLL e IRPJ |
| Percentual de Adição por Doações | CSLL e IRPJ |

4Alíquota de PresunçãoAlíquota de Presunção

# Foi incluído no cadastro de Tributo o painel **Alíquota de Presunção**, para atender à previsão de majoração da alíquota conforme a LC 224/2025.

**Percentual de Majoração:** Percentual que será acrescido à alíquota original do tributo, quando aplicável.

**Limite Anual Isento da Majoração:** Valor anual até o qual não será aplicada a majoração. A majoração incide apenas sobre valores que ultrapassarem esse limite.

# 3. Cópia de Tributo entre Coligadas

**Objetivo do processo:**

Ser possível copiar *Tributos*de uma Coligada para outra Coligada.

**Como realizar processo:**

Acessando o menu BackOffice → Gestão FIscal → Cadastros →Tributos, será carregado uma visão com todos tributos cadastrados. Ao selecionar o Tributo que se deseja copiar, vá em Processos → Cópia de Tributo entre Coligadas.  
Na visão, será carregado um filtro para seleção da Coligada Destino. Selecione a Coligada e execute o processo.  
É importante que se esteja sempre na Coligada Origem para que se proceda a rotina.

**Exemplo:**

*Caso deseje duplicar as Regiões da Coligada 1 para a Coligada 2, deve Selecionar a Coligada 2 (Coligada Destino)*

falseObservação

* O sistema duplicará todos os campos da tabela de Tributos;
* As Expressões cadastradas na Coligada Origem deverão ser incluídas na Coligada de Destino para duplicação das Expressões vinculadas aos Tributos, que serão utilizadas como Base de Cálculo do imposto.

# 4. Default dos Tributos CBS e IBS

* Ao selecionar um dos tributos **CBS** ou **IBS** no campo "**Tipo Tributo**" os campos "**Incidência**" e "**Procurar Alíquota no**" da aba "**Outros Dados**" serão preenchidos automaticamente. Dessa forma não é necessário acessar a aba "Outros Dados" para salvar o cadastro.
* Ao selecionar a opção "**Estadual/Municipal**" no campo "**Abrangência do Tributo**" o campo: "**Tipo Tributo**" será preenchido automaticamente com o valor "**IBS**" e os campos "**Incidência**" e "**Procurar Alíquota no**" da aba "**Outros Dados**" também serão preenchidos automaticamente.  
    
  Esse comportamento visa facilitar a inclusão dos tributos da Reforma Tributária, mais detalhes sobre a correta inclusão dos tributos acesse a página: .

  GIFs

**Quer contribuir com a evolução da nossa documentação? [Clique aqui e dê um feedback sobre esta página!](https://forms.gle/RZXc3eYwhuq9TNtD6)**

Imagens
