---
content_hash: 5e8bb97c14bc7a9c3b073aec17da2cca8a85826401386292abe42f2096be1b97
fetched_at: '2026-06-29T00:11:43.038649+00:00'
page_id: '801316924'
product: rm
source: tdn-rm
title: Cadastro do eventos S-2501 - Leiaute 1.2
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+do+eventos+S-2501+-+Leiaute+1.2
version: 19
---

Evento S-2501 - Leiaute 1.2NovidadesNovidades

Foram implementadas melhorias na usabilidade das telas, otimizando a navegação e proporcionando uma experiência mais intuitiva e eficiente para os usuários. Calendário de liberação dessas melhorias:

* Linha Datasul: expedição do dia
* Linha Protheus: expedição do dia
* Linha RM: disponível a partir dos patches 12.1.2310.254, 12.1.2402.221, 12.1.2406.149 e superiores.

**Menu retrátil**

**Exibição da versão**

Na linha Datasul esta opção não está disponível.

**Fácil visualização dos botões de Edição e Exclusão**

Tela de pesquisa

Permite a pesquisa () dos tributos já cadastrados para edição ou exclusão. Se for cadastrar um novo tributo, deve-se clicar no botão **+Incluir tributos**.

Edição de informações de tributos

Permite a pesquisa () do processo incluído no evento S-2500. O tributo é cadastrado para o Período e Trabalhador associado ao processo.

Os grupos/campos contemplados na tela de edição:

|  |  |  |
| --- | --- | --- |
| **Título do campo** | **Grupo/Campo** | **Descrição** |
| Identificação do processo. Os campos abaixo pertencem ao grupo **ideProc**. | | |
| Número do processo | nrProcTrab | Exibe a relação dos processos cadastrados no evento S-2500. |
| Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença | perApurPgto | Exibe o período (mês/ano) em que é devida a obrigação de pagar a parcela prevista no acordo/sentença. |
| Observação | obs | Exibe a observação referente ao pagamento de parcela prevista no acordo/sentença. |
| Visão de trabalhadores associados ao processo selecionado. Os campos abaixo pertencem ao grupo **ideTrab**. | | |
| CPF | cpfTrab | Exibe o CPF do trabalhador. |
| Nome | nmTrab | Exibe o nome do trabalhador, caso tenha sido informado. |
| Data de nascimento | dtNascto | Exibe a data de nascimento trabalhador, caso tenha sido informado. |

Leiaute1.2-S2501Informação do período e base de cálculo

Os grupos/campos contemplados na aba "**Identificação do período e da base de cálculo dos tributos**":

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Título do campo** | **Grupo/Campo** | **Tipo** | **Ocorrência** | **Tamanho** | **Descrição** |
| Identificação do período e da base de cálculo dos tributos. Os campos abaixo pertencem ao grupo **calcTrib**, cujo preenchimento é opcional. | | | | | |
| Referência | perRef | C | 1 | 7 | Informar o mês/ano (formato AAAA-MM) de referência das informações. Validação: Deve ser um período existente no evento S-2500 para o trabalhador indicado em CPF do Trabalhador (cpfTrab) e igual ou posterior a [2008-12]. |
| Valor da base de cálculo da contribuição previdenciária sobre a remuneração mensal do trabalhador | vrBcCpMensal | N | 1 | 14,2 | Valor da base de cálculo da contribuição previdenciária sobre a remuneração mensal do trabalhador. Validação: Deve ser maior ou igual a 0 (zero). |
| Valor da base de cálculo da contribuição previdenciária sobre a remuneração do trabalhador referente ao 13º salário | vrBcCp13 | N | 1 | 14,2 | Valor da base de cálculo da contribuição previdenciária sobre a remuneração do trabalhador referente ao 13º salário. Validação: Deve ser maior ou igual a 0 (zero). |

Informação de IRRF

Os grupos/campos contemplados na aba "**Incluir IRRF**":

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Título do campo** | **Grupo/Campo** | **Tipo** | **Ocorrência** | **Tamanho** | **Descrição** |
| Informações de IRRF. Os campos abaixo pertencem ao grupo **infoCRIRRF**, cujo preenchimento é opcional. | | | | | |
| Código de Receita | tpCR | N | 1 | 6 | Código de Receita - CR relativo a Imposto de Renda Retido na Fonte. Valores válidos: 593656 - IRRF - Decisão da Justiça do Trabalho 188951 - IRRF - RRA - Decisão da Justiça do Trabalho |
| Valor | vrCR | N | 1 | 14,2 | Valor correspondente ao Código de Receita - CR. Validação: Deve ser informado de acordo com a legislação em vigor na competência. Deve ser maior ou igual a 0 (zero). |
| Informações complementares, vinculadas ao campo "Código de Receita" (infoCRIRRF/tpCR), relacionadas a rendimentos tributáveis e a deduções e/ou isenções de acordo com a legislação aplicada ao imposto de renda. Os campos abaixo pertencem ao grupo **infoIR**, cujo preenchimento é opcional. | | | | | |
| Valor do rendimento tributável mensal do Imposto de Renda | vrRendTrib | N | 0-1 | 14,2 |  |
| Valor do rendimento tributável do Imposto de Renda referente ao 13º salário - Tributação exclusiva | vrRendTrib13 | N | 0-1 | 14,2 | Valor do rendimento tributável do Imposto de Renda referente ao 13º salário - Tributação exclusiva. Validação: Deve ser maior ou igual a 0 (zero). Não informar se o campo "Código de Receita" (infoCRIRRF/tpCR) = [188951]. |
| Valor do rendimento isento por ser portador de moléstia grave atestada por laudo médico | vrRendMoleGrave | N | 0-1 | 14,2 | Valor do rendimento isento por ser portador de moléstia grave atestada por laudo médico. Validação: Deve ser maior ou igual a 0 (zero). |
| Valor de parcela isenta de aposentadoria para beneficiário de 65 anos ou mais | vrRendIsen65 | N | 0-1 | 14,2 | Valor de parcela isenta de aposentadoria para beneficiário de 65 anos ou mais. Validação: Deve ser maior ou igual a 0 (zero). |
| Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função | vrJurosMora | N | 0-1 | 14,2 | Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função. Validação: Deve ser maior ou igual a 0 (zero). |
| Valor de outros rendimentos isentos ou não tributáveis | vrRendIsenNTrib | N | 0-1 | 14,2 | Valor de outros rendimentos isentos ou não tributáveis. Validação: Deve ser maior ou igual a 0 (zero). |
| Valor referente à previdência oficial | vrPrevOficial | N | 0-1 | 14,2 | Valor referente à previdência oficial. Validação: Deve ser maior ou igual a 0 (zero). |
| Descrição do rendimento isento ou não tributável informado em "Valor de outros rendimentos isentos ou não tributáveis" | descIsenNTrib | C | 0-1 | 1-60 | Descrição do rendimento isento ou não tributável informado no campo "Valor de outros rendimentos isentos ou não tributáveis" (vrRendIsenNTrib). Validação: Somente informar se o campo "Valor de outros rendimentos isentos ou não tributáveis" (vrRendIsenNTrib) [vrRendIsenNTrib](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/index.html#2501_ideTrab_infoCRIRRF_infoIR_vrRendIsenNTrib) > 0. |
| Informações complementares de RRA. Os campos abaixo pertencem ao grupo **infoRRA**, cujo preenchimento é obrigatório se o campo "Código de Receita" (infoCRIRRF/tpCR) = [188951]. Caso contrário não deve ser informado. | | | | | |
| Descrição dos Rendimentos Recebidos Acumuladamente | descRRA | C | 1 | 1-50 | Descrição dos Rendimentos Recebidos Acumuladamente - RRA. |
| Número de meses relativo aos Rendimentos Recebidos Acumuladamente | qtdMesesRRA | N | 1 | 1-4 | Número de meses relativo aos Rendimentos Recebidos Acumuladamente - RRA. |
| Detalhamento das despesas com processo judicial. Os campos abaixo pertencem ao grupo **despProcJud**, cujo preenchimento é opcional. | | | | | |
| Valor das despesas com custas judiciais | vlrDespCustas | N | 1 | 14,2 | Preencher com o valor das despesas com custas judiciais. |
| Valor total das despesas com advogado(s) | vlrDespAdvogados | N | 1 | 14,2 | Preencher com o valor total das despesas com advogado(s). |
| Dedução do rendimento tributável relativa a dependentes. Os campos abaixo pertencem ao grupo **dedDepen**. Se o campo "Código de Receita" (infoCRIRRF/tpCR)  = [188951] não deve ser informado, caso contrário é opcional. | | | | | |
| CPF do dependente | cpfDep | C | 1 | 11 | Informar o número de inscrição do dependente no CPF. Validação: Deve ser um CPF de dependente cadastrado no eSocial (S-2200/S-2205/S-2300 ou no grupo "Informações de dependentes não cadastrados pelo S-2200/S-2205/S-2300" (infoDep)). |
| Tipo de rendimento | tpRend | N | 1 | 2 | Tipo de rendimento. Valores válidos: 11 - Remuneração mensal 12 - 13º salário |
| Valor da dedução da base de cálculo | vlrDeducao | N | 1 | 14,2 | Preencher com o valor da dedução da base de cálculo. Validação: O valor informado neste campo deve ser menor ou igual ao valor unitário da dedução por dependente definido na legislação. Deve ser maior que 0 (zero). Em caso de inconsistência na validação, o arquivo será aceito, porém com alerta ao contribuinte. |
| Informação dos beneficiários da pensão alimentícia. Os campos abaixo pertencem ao grupo **penAlim**, cujo preenchimento é opcional. | | | | | |
| CPF do dependente/beneficiário da pensão alimentícia | cpfDep | C | 1 | 11 | Número do CPF do dependente/beneficiário da pensão alimentícia. Validação: Deve ser um CPF de dependente cadastrado no eSocial (S-2200/S-2205/S-2300 ou no grupo "Informações de dependentes não cadastrados pelo S-2200/S-2205/S-2300" (infoDep)). |
| Tipo de rendimento | tpRend | N | 1 | 2 | Tipo de rendimento. Valores válidos: 11 - Remuneração mensal 12 - 13º salário 18 - RRA 79 - Rendimento isento ou não tributável Validação: Se o campo "Código de Receita" (infoCRIRRF/tpCR) = [188951], deve ser igual a [18]. |
| Valor relativo à dedução do rendimento tributável correspondente a pagamento de pensão alimentícia | vlrPensao | N | 1 | 14,2 | Valor relativo à dedução do rendimento tributável correspondente a pagamento de pensão alimentícia. Validação: Deve ser maior que 0 (zero). |
| Identificação de advogados. Os campos abaixo pertencem ao grupo **ideAdv**, cujo preenchimento é opcional. | | | | | |
| Tipo de inscrição | tpInsc | N | 1 | 1 | Preencher com o código correspondente ao tipo de inscrição, conforme [Tabela 05](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/tabelas.html#05). Valores válidos: 1 - CNPJ 2 - CPF |
| Número de inscrição do advogado | nrInsc | C | 1 | 11 ou 14 | Informar o número de inscrição do advogado. Validação: Deve ser um número de inscrição válido, de acordo com o tipo de inscrição indicado no campo "Tipo de inscrição" (ideAdv/tpInsc), considerando as particularidades aplicadas à informação de CNPJ de órgão público em S-1000. Se o campo "Tipo de inscrição" (ideAdv/tpInsc) = [1], deve possuir 14 (catorze) algarismos e, no caso de declarante pessoa jurídica, ser diferente do CNPJ base do empregador. Se o campo "Tipo de inscrição" (ideAdv/tpInsc) = [2], deve possuir 11 (onze) algarismos e, no caso de declarante pessoa física, ser diferente do CPF do empregador. |
| Valor da despesa com o advogado | vlrAdv | N | 0-1 | 14,2 | Valor da despesa com o advogado, se houver. |
| Informações de processos relacionados a não retenção de tributos ou a depósitos judiciais. Os campos abaixo pertencem ao grupo **infoProcRet**. Se o campo  "Código de Receita" (infoCRIRRF/tpCR) = [188951] não deve ser informado, caso contrário é opcional. | | | | | |
| Tipo de processo | tpProcRet | N | 1 | 1 | Preencher com o código correspondente ao tipo de processo. Valores válidos: 1 - Administrativo 2 - Judicial |
| Número do processo administrativo/judicial | nrProcRet | C | 1 | 17, 20 ou 21 | Informar o número do processo administrativo/judicial. Validação: Deve ser um número de processo administrativo ou judicial válido e existente na Tabela de Processos (S-1070). |
| Código do indicativo da suspensão | codSusp | N | 0-1 | 1-14 | Código do indicativo da suspensão, atribuído pelo empregador em S-1070. Validação: Preenchimento obrigatório se houver informação de codSusp em S-1070. Se informado, deve constar na Tabela de Processos (S-1070), campo codSusp, vinculado ao número do processo informado em nrProcRet. |
| Informações de valores relacionados a não retenção de tributos ou a depósitos judiciais. Os campos abaixo pertencem ao grupo **infoValores**, cujo preenchimento é opcional. | | | | | |
| Indicativo de período de apuração | indApuracao | N | 1 | 1 | Indicativo de período de apuração. Valores válidos: 1 - Mensal 2 - Anual (13° salário) |
| Valor da retenção que deixou de ser efetuada em função de processo administrativo ou judicial | vlrNRetido | N | 0-1 | 14,2 | Valor da retenção que deixou de ser efetuada em função de processo administrativo ou judicial. Validação: Deve ser maior que 0 (zero). |
| Valor do depósito judicial em função de processo administrativo ou judicial | vlrDepJud | N | 0-1 | 14,2 | Valor do depósito judicial em função de processo administrativo ou judicial. Validação: Informação permitida apenas se indDeposito informado em S-1070 for igual a [S]. Se informado, deve ser maior que 0 (zero). |
| Valor da compensação relativa ao ano calendário em função de processo judicial | vlrCmpAnoCal | N | 0-1 | 14,2 | Valor da compensação relativa ao ano calendário em função de processo judicial. Validação: Informação permitida apenas se o campo "Tipo de processo" (tpProcRet) = [2]. Se informado, deve ser maior que 0 (zero). |
| Valor da compensação relativa a anos anteriores em função de processo judicial | vlrCmpAnoAnt | N | 0-1 | 14,2 | Valor da compensação relativa a anos anteriores em função de processo judicial. Validação: Informação permitida apenas se o campo "Tipo de processo" (tpProcRet) = [2]. Se informado, deve ser maior que 0 (zero). |
| Valor do rendimento com exigibilidade suspensa | vlrRendSusp | N | 0-1 | 14,2 | Valor do rendimento com exigibilidade suspensa. Validação: Se "Indicativo de período de apuração" (indApuracao) = [1], não pode ser maior que o campo "Valor do rendimento tributável mensal do Imposto de Renda" (vrRendTrib). Se "Indicativo de período de apuração" (indApuracao) = [2], não pode ser maior que o campo "Valor do rendimento tributável do Imposto de Renda referente ao 13º salário - Tributação exclusiva" (vrRendTrib13). Se informado, deve ser maior que 0 (zero). |
| Detalhamento das deduções com exigibilidade suspensa. Os campos abaixo pertencem ao grupo **dedSusp**, cujo preenchimento é opcional. | | | | | |
| Indicativo do tipo de dedução | indTpDeducao | N | 1 | 1 | Indicativo do tipo de dedução. Valores válidos: 1 - Previdência oficial 5 - Pensão alimentícia 7 - Dependentes |
| Valor da dedução da base de cálculo do imposto de renda com exigibilidade suspensa | vlrDedSusp | N | 0-1 | 14,2 | Valor da dedução da base de cálculo do imposto de renda com exigibilidade suspensa. Validação: Informação permitida apenas se o campo "Valor do rendimento com exigibilidade suspensa" (vlrRendSusp) > 0. Se "Indicativo do tipo de dedução" (indTpDeducao) = [5, 7], e o grupo "Informação das deduções suspensas por dependentes e beneficiários da pensão alimentícia" (benefPen) for preenchido, o valor informado neste campo deve ser a soma do(s) campo(s) "Valor da dedução relativa a dependentes ou a pensão alimentícia com exigibilidade suspensa" (vlrDepenSusp) do grupo "Informação das deduções suspensas por dependentes e beneficiários da pensão alimentícia" (benefPen) . Deve ser maior que 0 (zero). O não preenchimento do grupo "Informação das deduções suspensas por dependentes e beneficiários da pensão alimentícia" (benefPen) indica que o contribuinte declarante não possui as informações detalhadas por dependente/alimentando. |
| Informação das deduções suspensas por dependentes e beneficiários da pensão alimentícia. Os campos abaixo pertencem ao grupo **benefPen**, cujo preenchimento é opcional. | | | | | |
| Número de inscrição no CPF | cpfDep | C | 1 | 11 | Número de inscrição no CPF. Validação: Deve ser um CPF de dependente cadastrado no eSocial (S-2200/S-2205/S-2300 ou no grupo "Informações de dependentes não cadastrados pelo S-2200/S-2205/S-2300" (infoDep)). |
| Valor da informação relativa a dependentes ou a pensão alimentícia com exigibilidade suspensa | vlrDepenSusp | N | 1 | 1-14 | Valor da dedução relativa a dependentes ou a pensão alimentícia com exigibilidade suspensa. **Validação:** Deve ser maior que 0 (zero). |

Informações de retenção na fonte e dependentes

Os grupos/campos contemplados na aba "**Informações de retenção na fonte e Dependentes**":

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Título do campo** | **Grupo/Campo** | **Tipo** | **Ocorrência** | **Tamanho** | **Descrição** |
| Informações relacionadas à retenção na fonte, aos rendimentos tributáveis e não tributáveis, deduções e/ou isenções, etc., de acordo com a legislação aplicada ao imposto de renda. Os campos abaixo pertencem ao grupo **infoIRComplem**, cujo preenchimento é opcional. | | | | | |
| Data da moléstia grave atribuída pelo laudo | dtLaudo | D | 0-1 | - | Data da moléstia grave atribuída pelo laudo. Validação: Não pode ser anterior ao ano de 1900. |
| Informações de dependentes não cadastrados pelo S-2200/S-2205/S-2300. Os campos abaixo pertencem ao grupo **infoDep**, cujo preenchimento é opcional. | | | | | |
| CPF | cpfDep | C | 1 | 11 | Número de inscrição no CPF. Validação: Deve ser um CPF válido e diferente do CPF do declarante pessoa física e do beneficiário (CPF do Trabalhador (cpfTrab)). |
| Nome | nome | C | 0-1 | 2-70 | Preencher com a data de nascimento. Validação: Deve ser maior ou igual que 01/01/1890 e menor ou igual à data atual. |
| Data de nascimento | dtNascto | D | 0-1 | - | Nome do dependente. |
| Dedução IRRF | depIRRF | C | 0-1 | 1 | Somente informar este campo em caso de dependente do trabalhador para fins de dedução de seu rendimento tributável pelo Imposto de Renda. Valores válidos: S - Sim |
| Tipo de dependente | tpDep | C | 0-1 | 2 | Tipo de dependente. Validação: Preenchimento obrigatório e exclusivo se o campo "Dedução IRRF" (depIRRF) = [S]. Deve ser um código válido e existente na [Tabela 07](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/tabelas.html#07). |
| Descrição da dependência | descrDep | C | 0-1 | 1-100 | Informar a descrição da dependência. Validação: Informação obrigatória e exclusiva se o campo "Tipo de dependente" (tpDep) = [99] (Agregado/Outros). |
