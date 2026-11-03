---
content_hash: 6ab220631d7509f6a5dd695a648ed9aeaea57ce70b69f40c433fb62e7700c112
fetched_at: '2026-06-29T00:11:43.000559+00:00'
page_id: '801316896'
product: rm
source: tdn-rm
title: Cadastro do eventos S-2500 - Leiaute 1.2
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+do+eventos+S-2500+-+Leiaute+1.2
version: 16
---

Evento S-2500 - Leiaute 1.2NovidadesNovidades

Foram implementadas melhorias na usabilidade das telas, otimizando a navegação e proporcionando uma experiência mais intuitiva e eficiente para os usuários. Calendário de liberação dessas melhorias:

* Linha Datasul: expedição do dia
* Linha Protheus: expedição do dia
* Linha RM: disponível a partir dos patches 12.1.2310.254, 12.1.2402.221, 12.1.2406.149 e superiores.

**Menu retrátil**

**Exibição da versão**

Na linha Datasul esta opção não está disponível.

**Fácil visualização dos botões de Edição e Exclusão**

**Disponibilização do botão "Por que não consigo salvar?"**

Este botão será exibido quando o campo obrigatório não estiver preenchido, para facilitar a identificação do motivo do botão Salvar não ficar habilitado.

Ao clicar no botão "Por que não consigo salvar?" a relação da pendência de preenchimento será exibida:

Quando navegar entre as abas, será exibido também um alerta indicando campo obrigatório não preenchido:

NovidadesTela de Pesquisa

Permite a pesquisa () dos processos já cadastrados para edição ou exclusão. Se for cadastrar um novo processo, deve-se clicar no botão **+ Adicionar processo**.

**Importante:** Na linha Protheus a inclusão do processo é realizada através da tela APTA100 do módulo SIGAGPE.

NovidadesAba Identificação do processo

Os grupos/campos contemplados na aba "**Identificação do processo**":

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Título do campo** | **Grupo/Campo** | **Tipo** | **Ocorrência** | **Tamanho** | **Descrição** |
| Informações de identificação do contribuinte (responsável direto), caso tenha havido imposição de responsabilidade indireta. Os campos abaixo pertencem ao grupo **ideResp**, cujo preenchimento é opcional. | | | | | |
| Tipo inscrição | tpInsc | N | 1 | 1 | Preencher com o código correspondente ao tipo de inscrição, conforme [Tabela 05](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/tabelas.html#05). Valores válidos: 1 - CNPJ 2 - CPF |
| Número da inscrição | nrInsc | C | 1 | 11 ou 14 | Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição. a) Se Tipo inscrição = [1], deve ser informado com 14 (catorze) algarismos. b) Se Tipo inscrição = [2], deve ser diferente do CPF do trabalhador. Se o empregador for pessoa física, também deve ser diferente do CPF do empregador. |
| Informações do processo judicial ou de demanda submetida à Comissão de Conciliação Prévia (CCP) ou ao Núcleo Intersindical de Conciliação Trabalhista (NINTER). Os campos abaixo pertencem ao grupo **infoProcesso**, cujo preenchimento é obrigatório. | | | | | |
| Origem | origem | N | 1 | 1 | Informar a origem do processo/demanda. Valores válidos: 1 - Processo judicial 2 - Demanda submetida à CCP ou ao NINTER |
| Número do processo | nrProcTrab | C | 1 | 15 ou 20 | Número do processo trabalhista, da ata ou número de identificação da conciliação. a) Se Origem = [1], deve ser um processo judicial válido, com 20 (vinte) algarismos; b) Se Origem = [2],deve possuir 15 (quinze) algarismos. |
| Observação | obsProcTrab | C | 0-1 | 1-999 | Observações relacionadas ao processo judicial ou à demanda submetida à CCP ou ao NINTER. |
| Informações complementares do processo judicial. Os campos abaixo pertencem ao grupo **infoProcJud**, o preenchimento é obrigatório se a Origem for igual a "Processo judicial". Se a Origem for igual a "Demanda submetida à CCP ou ao NINTER" estes campos não devem ser preenchidos. | | | | | |
| Data da sentença | dtSent | D | 1 | - | Data da sentença ou da homologação do acordo do processo judicial.  Informar a data do(a): a) Trânsito em julgado da decisão líquida proferida no processo trabalhista; b) Homologação de acordo judicial; ou c) Trânsito em julgado da decisão homologatória dos cálculos de liquidação da sentença. Validação: Deve ser igual ou anterior à data atual. |
| UF | ufVara | C | 1 | 2 | Preencher com a sigla da Unidade da Federação onde está localizada a Vara em que o processo tramitou. Valores válidos: AC, AL, AP, AM, BA, CE, DF, ES, GO, MA, MT, MS, MG, PA, PB, PR, PE, PI, RJ, RN, RS, RO, RR, SC, SP, SE, TO |
| Município | codMunic | N | 1 | 7 | Preencher com o código do município, conforme tabela do IBGE. Validação: Deve ser um código válido e existente na tabela do IBGE. |
| Identificador da vara | idVara | N | 1 | 2 | Código de identificação da Vara em que o processo tramitou. |
| Informações complementares da demanda submetida à CCP ou ao NINTER. Os campos abaixo pertencem ao grupo **infoCCP**, o preenchimento é obrigatório se a Origem for igual a "Demanda submetida à CCP ou ao NINTER". Se a Origem for igual a "Processo judicial" estes campos não devem ser preenchidos. | | | | | |
| Data da conciliação | dtCCP | D | 1 | - | Data da conciliação. Validação: Deve ser igual ou anterior à data atual. |
| Âmbito | tpCCP | N | 1 | 1 | Indicar o âmbito de celebração do acordo. Valores válidos: 1 - CCP no âmbito de empresa 2 - CCP no âmbito de sindicato 3 - NINTER |
| CNPJ sindicato | cnpjCCP | C | 0-1 | 14 | Identificar o CNPJ do sindicato representativo do trabalhador, no âmbito da CCP ou NINTER. Validação: O preenchimento é obrigatório e exclusivo se Âmbito for igual a [2] ou [3]. Deve ser um número de CNPJ válido. |

NovidadesIdentificação da pessoa trabalhadora e contrato de trabalho

Os grupos/campos contemplados "**Identificação da pessoa trabalhadora**":

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Título do campo** | **Grupo/Campo** | **Tipo** | **Ocorrência** | **Tamanho** | **Descrição** |
| Informações do trabalhador. Os campos abaixo pertencem ao grupo **ideTrab**, cujo preenchimento é obrigatório. | | | | | |
| CPF | cpfTrab | C | 1 | 11 | Preencher com o número do CPF do trabalhador. |
| Nome | nmTrab | C | 0-1 | 2/70 | Informar o nome do trabalhador. Validação: Preenchimento obrigatório se não existir contrato com o campo "Indicativo se o contrato possui informação no evento S-2190, S-2200 ou S-2300 no declarante" = [S]. |
| Data de nascimento | dtNascto | D | 0-1 | - | Preencher com a data de nascimento. Validação: Preenchimento obrigatório se não existir contrato com o campo "Indicativo se o contrato possui informação no evento S-2190, S-2200 ou S-2300 no declarante" = [S].  Deve ser maior ou igual que 01/01/1890 e menor ou igual à data atual. |

Os grupos/campos contemplados "**Contratos de trabalhos**":

### **Tela de pesquisa**

Permite a pesquisa () dos processos já cadastrados para edição ou exclusão. Se for cadastrar um novo processo, deve-se clicar no botão **+ Adicionar Contrato**.

Contrato de trabalhoInformações geraisInformações gerais

Os grupos/campos contemplados na sub-aba "**Informações gerais**":

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Título do campo** | **Grupo/Campo** | **Tipo** | **Ocorrência** | **Tamanho** | **Descrição** |
| Informações do contrato de trabalho. Os campos abaixo pertencem ao grupo **infoContr**,cujo preenchimento é obrigatório. | | | | | |
| Tipo | tpContr | N | 1 | 1 | Tipo de contrato a que se refere o processo judicial ou a demanda submetida à CCP ou ao NINTER. Valores válidos: 1 - Trabalhador com vínculo formalizado, sem alteração nas datas de admissão e de desligamento 2 - Trabalhador com vínculo formalizado, com alteração na data de admissão 3 - Trabalhador com vínculo formalizado, com inclusão ou alteração de data de desligamento 4 - Trabalhador com vínculo formalizado, com alteração nas datas de admissão e de desligamento 5 - Empregado com reconhecimento de vínculo 6 - Trabalhador sem vínculo de emprego/estatutário (TSVE), sem reconhecimento de vínculo empregatício 7 - Trabalhador com vínculo de emprego formalizado em período anterior ao eSocial 8 - Responsabilidade indireta 9 - Trabalhador cujos contratos foram unificados (unicidade contratual) Validação: Deve ser igual a [8] se o grupo ideResp for informado. |
| Possui informação no evento S-2190, S-2200 ou S-2300 no declarante? | indContr | C | 1 | 1 | Indicativo se o contrato possui informação no evento S-2190, S-2200 ou S-2300 no declarante. Valores válidos: S - Sim N - Não Validação: Deve ser igual a [N] se o grupo ideResp for informado. |
| Data de admissão | dtAdmOrig | D | 0-1 | - | Preencher com a data de admissão original do vínculo (data de admissão antes da alteração). Validação: Preenchimento obrigatório se o campo "Tipo" = [2, 4]. Deve ser posterior à data de nascimento do trabalhador. |
| Reintegração | indReint | C | 0-1 | 1 | Indicativo de reintegração do empregado. Valores válidos: S - Sim N - Não Validação: Preenchimento obrigatório e exclusivo se o campo "Tipo" for diferente de [6] e o campo "Possui informação no evento S-2190, S-2200 ou S-2300 no declarante?" = [S]. |
| Reconhecimento da categoria | indCateg | C | 1 | 1 | Indicativo se houve reconhecimento de categoria do trabalhador diferente da informada (no eSocial ou na GFIP) pelo declarante. Valores válidos: S - Sim N - Não |
| Reconhecimento da natureza atividade | indNatAtiv | C | 1 | 1 | Indicativo se houve reconhecimento de natureza da atividade diferente da cadastrada pelo declarante. Valores válidos: S - Sim N - Não |
| Reconhecimento motivo desligamento | indMotDeslig | C | 1 | 1 | Indicativo se houve reconhecimento de motivo de desligamento diferente do informado pelo declarante. Valores válidos: S - Sim N - Não |
| Matrícula | matricula | C | 0-1 | 01-30 | Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Se o campo "Possui informação no evento S-2190, S-2200 ou S-2300 no declarante?" = [N], deve ser criada uma matrícula para o trabalhador. Se o campo "Possui informação no evento S-2190, S-2200 ou S-2300 no declarante?" = [S], deve corresponder à matrícula informada pelo empregador no evento S-2190, S-2200 ou S-2300 do respectivo contrato. O campo não deve ser informado somente no caso de TSVE cadastrado em versão do leiaute anterior a S-1.0.  Se o campo "Tipo" (infoContr/tpContr) = [9], deve ser preenchida a matrícula que incorporará as demais (informadas no grupo unicContr). |
| Código da categoria | codCateg | N | 0-1 | 3 | Preencher com o código da categoria do trabalhador. Validação: Informação obrigatória e exclusiva se o campo "Possui informação no evento S-2190, S-2200 ou S-2300 no declarante?" = [N] ou se o campo matricula não estiver preenchido. Deve ser um código válido e existente na [Tabela 01](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/tabelas.html#01) e obedecer ao que segue: a) Se o campo matricula não estiver preenchido, deve ser igual ao código de categoria informado no evento S-2300; b) Se o campo "Possui informação no evento S-2190, S-2200 ou S-2300 no declarante?" = [N] e o campo "Tipo" for diferente de [6], deve ser um código de categoria compatível com o evento S-2200; c) Se o campo "Possui informação no evento S-2190, S-2200 ou S-2300 no declarante?" = [N] e o campo "Tipo" = [6], deve ser um código de categoria compatível com o evento S-2300. |
| Data de início TSVE | dtInicio | D | 0-1 | - | Data de início de TSVE, que pode ser: a) Para o cooperado, a data de ingresso na cooperativa; b) Para o diretor não empregado, a data de posse no cargo; c) Para o dirigente sindical, a data de início do mandato no sindicato; d) Para o estagiário, a data de início do estágio; e) Para o trabalhador avulso, a data de ingresso no Órgão Gestor de Mão de Obra - OGMO ou no sindicato; f) Para o servidor público exercente de cargo eletivo, a data de início do mandato; g) Para os demais trabalhadores, a data de início das atividades. Validação: Informação obrigatória e exclusiva se (o campo "Tipo" = [6] e o campo "Possui informação no evento S-2190, S-2200 ou S-2300 no declarante?" = [N]) ou se o campo matricula não estiver preenchido. Deve ser posterior à data de nascimento do trabalhador. Se o campo matricula não estiver preenchido, deve ser igual à data de início informada no evento S-2300. |
| Identificação do estabelecimento. Os campos abaixo pertencem ao grupo **ideEstab**, cujo preenchimento é obrigatório | | | | | |
| Tipo de inscrição | tpInsc | N | 1 | 1 | Preencher com o código correspondente ao tipo de inscrição do estabelecimento, de acordo com as opções da [Tabela 05](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/tabelas.html#05). No caso de empregador doméstico, informar [3] (CAEPF). Valores válidos: 1 - CNPJ 3 - CAEPF 4 - CNO |
| Número de inscrição | nrInsc | C | 1 | 12 ou 14 | Informar o número de inscrição do estabelecimento do contribuinte de acordo com o tipo de inscrição indicado no campo acima. No caso de empregador doméstico, informar os 9 (nove) primeiros dígitos do CPF do empregador, seguidos de 5 (cinco) dígitos 0 (zero). Por exemplo, se o CPF do empregador doméstico for 111111111-99, informar 11111111100000. Validação: A inscrição informada deve ser compatível com o campo "Tipo de inscrição". Se o processo for referente a empregado doméstico, a inscrição informada deve ser igual aos 9 (nove) primeiros dígitos do CPF do empregador, seguidos de 5 (cinco) dígitos 0 (zero). |
| Informações dos períodos e valores. Os campos abaixo pertencem ao grupo **infoVlr**, cujo preenchimento é obrigatório | | | | | |
| Competência inicial | compIni | C | 1 | 7 | Competência inicial a que se refere o processo ou conciliação, no formato AAAA-MM. Validação: Devem ser obedecidas as seguintes regras: a) Se o campo "Tipo" = [1, 3, 7, 8, 9], deve ser igual ou posterior ao mês/ano da data de admissão; b) Se o campo "Tipo" = [2, 4, 5], deve ser igual ao mês/ano da data de admissão; c) Se o campo "Tipo" = [6], deve ser igual ou posterior ao mês/ano da data de início do TSVE. |
| Competência final | compFim | C | 1 | 7 | Competência final a que se refere o processo ou conciliação, no formato AAAA-MM. Validação: Deve ser igual ou posterior ao campo "Competência inicial", igual ou anterior ao mês/ano do campo "Data da sentença" ou do campo "Data da conciliação". |
| Indicativo de repercussão | indReperc | N | 1 | 1 | Repercussão do processo trabalhista ou de demanda submetida à CCP ou ao NINTER. Valores válidos: 1 - Decisão com repercussão tributária e/ou FGTS 2 - Decisão sem repercussão tributária ou FGTS 3 - Decisão com repercussão exclusiva para declaração de rendimentos para fins de Imposto de Renda |
| Houve decisão para pagamento da indenização substitutiva do seguro-desemprego? | indenSD | C | 0-1 | 1 | Houve decisão para pagamento da indenização substitutiva do seguro-desemprego? Valores válidos: S - Sim |
| Houve decisão para pagamento da indenização substitutiva de abono salarial? | indenAbono | C | 0-1 | 1 | Houve decisão para pagamento da indenização substitutiva de abono salarial? Valores válidos: S - Sim |
| Identificação do(s) ano(s)-base em que houve indenização substitutiva de abono salarial. Os campos abaixo pertencem ao grupo **abono**. Se o campo "Houve decisão para pagamento da indenização substitutiva de abono salarial?" for igual a "S" , o preenchimento deste grupo é obrigatório. Caso contrário, este grupo não deve ser preenchido. | | | | | |
| Ano base | anoBase | C | 1 | 4 | Ano-base em que houve indenização substitutiva do abono salarial. |
| Identificação do período ao qual se referem as bases de cálculo. Os campos abaixo pertencem ao grupo **idePeriodo**. Se o campo "Repercussão" for igual a 1 (Decisão com pagamento de verbas de natureza remuneratória), o preenchimento deste grupo é obrigatório. Caso contrário, o preenchimento deste grupo é opcional. | | | | | |
| Período | perRef | C | 1 | 7 | Informar o mês/ano (formato AAAA-MM) de referência das informações. Validação: Deve ser um período compreendido entre os campos "Competência inicial" e "Competência final", informado no formato AAAA-MM. |
| Bases de cálculo de contribuição previdenciária e FGTS decorrentes de processo trabalhista e ainda não declaradas. Os campos abaixo pertencem ao grupo **baseCalculo**, cujo preenchimento é opcional. | | | | | |
| Base de cálculo da contribuição previdenciária sobre a remuneração mensal do trabalhador | vrBcCpMensal | N | 1 | 14,2 | Valor da base de cálculo da contribuição previdenciária sobre a remuneração mensal do trabalhador. Validação: Deve ser maior ou igual a 0 (zero). |
| Base de cálculo da contribuição previdenciária sobre o 13º salário | vrBcCp13 | N | 1 | 14,2 | Valor da base de cálculo da contribuição previdenciária sobre a remuneração do trabalhador referente ao 13º salário. Validação: Deve ser maior ou igual a 0 (zero). |
| Grau de exposição a agentes nocivos. Os campos abaixo pertencem ao grupo **infoAgNocivo**.  Este grupo é obrigatório se: O campo "Código de categoria" for igual a [1XX, 2XX, 3XX, 731, 734, 738] ou se o campo "Código de categoria" for igual a [4XX] em S-2300 = [1XX, 2XX, 3XX, 731, 734, 738]. Caso contrário, este grupo não deve ser preenchido. | | | | | |
| Grau de exposição a agentes nocivos | grauExp | N | 1 | 1 | Preencher com o código que representa o grau de exposição a agentes nocivos, conforme [Tabela 02](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/tabelas.html#02). Valores válidos: 1 - Não ensejador de aposentadoria especial 2 - Ensejador de aposentadoria especial - FAE15\_12% (15 anos de contribuição e alíquota de 12%) 3 - Ensejador de aposentadoria especial - FAE20\_09% (20 anos de contribuição e alíquota de 9%) 4 - Ensejador de aposentadoria especial - FAE25\_06% (25 anos de contribuição e alíquota de 6%) |
| Informações referentes a bases de cálculo de FGTS para geração de guia. Os campos abaixo pertencem ao grupo **infoFGTS**, cujo preenchimento é opcional. | | | | | |
| Base de cálculo do FGTS sobre a remuneração do trabalhadores (sem 13º salário) | vrBcFGTSProcTrab | N | 1 | 14,2 | Valor da base de cálculo de FGTS ainda não declarada em SEFIP ou no eSocial, inclusive de verba reconhecida no processo trabalhista. Validação: Deve ser maior ou igual a 0 (zero). |
| Base de cálculo do FGTS sobre o 13º salário | vrBcFGTSSefip | N | 0-1 | 14,2 | Valor da base de cálculo de FGTS declarada apenas em SEFIP (não informada no eSocial) e ainda não recolhida. Validação: Deve ser maior que 0 (zero). |
| Pago diretamente ao trabalhador? | vrBcFGTSDecAnt | N | 0-1 | 1 | Valor da base de cálculo de FGTS declarada anteriormente no eSocial e ainda não recolhida. Validação: Somente pode ser informado se o campo "Período" (perRef) for anterior ao início do FGTS Digital. Deve ser maior que 0 (zero). |
| Bases de cálculo já declaradas em GFIP, no caso de reconhecimento de mudança de código de categoria. Os campos abaixo pertencem ao grupo **baseMudCateg.**  O preenchimento deste grupo é opcional se o campo "Reconhecimento da categoria" for igual a "S". Caso contrário não deve ser preenchido. | | | | | |
| Categoria | codCateg | N | 1 | 3 | Preencher com o código da categoria do trabalhador declarado no período de referência. Validação: Deve ser um código válido e existente na[Tabela 01](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/tabelas.html#01). |
| Remuneração do trabalhador a ser considerada para fins previdenciários declarada em GFIP ou em S-1200 de trabalhador sem cadastro no S-2300 | vrBcCPrev | N | 1 | 14,2 | Valor da remuneração do trabalhador a ser considerada para fins previdenciários declarada em GFIP ou em S-1200 de trabalhador sem cadastro no S-2300. Validação: Deve ser maior que 0 (zero). |
| Informação do novo código de categoria e/ou da nova natureza da atividade. Os campos abaixo pertencem ao grupo **mudCategAtiv.**  O preenchimento deste grupo é opcional se o campo "Reconhecimento da categoria" for igual a "S" OU se o campo "Reconhecimento da natureza atividade" for igual a "S". Caso contrário não deve ser preenchido. | | | | | |
| Código | codCateg | N | 1 | 3 | Preencher com o código da categoria do trabalhador. Validação: Deve ser um código válido e existente na [Tabela 01](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/tabelas.html#01). |
| Natureza da atividade | natAtividade | N | 0-1 | 1 | Natureza da atividade. Valores válidos: 1 - Trabalho urbano 2 - Trabalho rural Validação: Não informar se o campo "Código" = [721, 722, 771, 901]. Se o campo "Código" = [104], não pode ser preenchido com [2]. Se o campo "Código" = [102], não pode ser preenchido com [1]. |
| Data da mudança | dtMudCategAtiv | D | 1 | - | Data a partir da qual foi reconhecida a nova categoria e/ou a nova natureza da atividade. Validação: Deve ser igual ou posterior à data de admissão (ou de início) e igual ou anterior à data de desligamento, se informada.  Se o campo "Indicativo se o contrato possui informação no evento S-2190, S-2200 ou S-2300 no declarante?" (indContr) = [N], deve ser uma data posterior à data de admissão (ou de início). |
| Informações dos vínculos/contratos incorporados. Os campos abaixo pertencem ao grupo **unicContr**.  O preenchimento deste grupo é obrigatório se o campo "Tipo" (infoContr/tpContr) for igual a "9". Caso contrário não deve ser preenchido. | | | | | |
| Matrícula incorporada | matUnic | C | 0-1 | 1-30 | Informar a matrícula incorporada (matrícula cujo vínculo/contrato passou a integrar período de unicidade contratual reconhecido judicialmente). O campo não deve ser informado somente no caso de TSVE cadastrado em versão do leiaute anterior a S-1.0. Validação: Deve corresponder a uma matrícula existente no RET para o respectivo trabalhador e diferente do vínculo/contrato informado em infoContr. |
| Código | codCateg | N | 0-1 | 3 | Preencher com o código da categoria do trabalhador (código de categoria cujo contrato passou a integrar período de unicidade contratual reconhecido judicialmente). Validação: Informação obrigatória e exclusiva se o campo "Matrícula incorporada" não estiver preenchido. Deve ser igual a um código de categoria de contrato cadastrado no evento S-2300 e diferente do contrato informado em infoContr. |
| Data de início de TSVE | dtInicio | D | 0-1 | - | Data de início de TSVE (data de início cujo contrato passou a integrar período de unicidade contratual reconhecido judicialmente). Validação: Informação obrigatória e exclusiva se o campo "Matrícula incorporada" não estiver preenchido. Deve ser igual a uma data de início de contrato cadastrado no evento S-2300 e diferente do contrato informado em infoContr. |

Informações geraisInformações complementares

Os grupos/campos contemplados na sub-aba "**Informações complementares**":

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Título do campo** | **Grupo/Campo** | **Tipo** | **Ocorrência** | **Tamanho** | **Descrição** |
| Informações complementares do contrato de trabalho. Os campos abaixo pertencem ao grupo **infoCompl**. Se o campo "Possuir informação no evento S-2190, S-2200 ou S-2300 no declarante?" for igual a "N", o preenchimento deste grupo é obrigatório. Caso contrário, o preenchimento é opcional. | | | | | |
| Classificação Brasileira de Ocupações - CBO | codCBO | C | 0-1 | 6 | Classificação Brasileira de Ocupações - CBO. Validação: Preenchimento obrigatório se infoContr/codCateg for diferente de [901, 903, 904]). Se informado, deve ser um código válido e existente na tabela de CBO, com 6 (seis) posições. |
| Natureza da atividade | natAtividade | N | 0-1 | 1 | Natureza da atividade. Valores válidos: 1 - Trabalho urbano 2 - Trabalho rural Validação: Preenchimento obrigatório se o campo "Código da categoria" for relativo a "Empregado", "Agente Público", "Avulso" ou igual a [401, 731, 734, 738]. Não deve ser preenchido se o campo "Código da categoria" = [721, 722, 771, 901]. Se o campo "Código da categoria" = [104], deve ser preenchido com [1]. Se o campo "Código da categoria" = [102], deve ser preenchido com [2]. |
| Informações de término de TSVE. Os campos abaixo pertencem ao grupo **infoTerm**. Se o campo "Tipo" for igual a "6" (Trabalhador sem vínculo de emprego/estatutário (TSVE), sem reconhecimento de vínculo empregatício), o preenchimento deste grupo é opcional. Caso contrário, não deve ser preenchido. | | | | | |
| Data de término | dtTerm | D | 1 | - | Data do término. Validação: Deve ser igual ou posterior a dtInicio e igual ou anterior à data atual acrescida de 10 (dez) dias. |
| Motivo do término do diretor não empregado, com FGTS | mtvDesligTSV | C | 0-1 | 2 | Motivo do término do diretor não empregado, com FGTS. Valores válidos: 01 - Exoneração do diretor não empregado sem justa causa, por deliberação da assembleia, dos sócios cotistas ou da autoridade competente 02 - Término de mandato do diretor não empregado que não tenha sido reconduzido ao cargo 03 - Exoneração a pedido de diretor não empregado 04 - Exoneração do diretor não empregado por culpa recíproca ou força maior 05 - Morte do diretor não empregado 06 - Exoneração do diretor não empregado por falência, encerramento ou supressão de parte da empresa 99 - Outros Validação: Informação obrigatória e exclusiva se o campo "Código da categoria" = [721]. |
| Informações da remuneração e periodicidade de pagamento. Os campos abaixo pertencem ao grupo **remuneracao**. O preenchimento deste grupo deve obedecer as regras abaixo:  Se o campo "Tipo" for diferente de "6" (Trabalhador sem vínculo de emprego/estatutário (TSVE), sem reconhecimento de vínculo empregatício) e o campo "Tipo de regime trabalhista" for igual a "2" (Estatutário/legislações específicas (servidor temporário, militar, agente político, etc.)), este grupo não deve ser preenchido.  Se o campo "Tipo" for diferente de "6" (Trabalhador sem vínculo de emprego/estatutário (TSVE), sem reconhecimento de vínculo empregatício) e o campo "Tipo de regime trabalhista" for igual a "1" (CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas) OU o campo "Código da categoria" for igual a [721, 722, 771], este grupo é de preenchimento obrigatório.  Caso contrário, seu preenchimento é opcional. | | | | | |
| Data | dtRemun | D | 1 | - | Data a partir da qual as informações de remuneração e periodicidade de pagamento estão vigentes. Validação: Deve ser igual ou posterior à data de admissão (ou de início) e igual ou anterior à data de desligamento (ou de término), se informada. |
| Salário base | vrSalFx | N | 1 | 14,2 | Salário base do trabalhador, correspondente à parte fixa da remuneração informada no campo "Data". Validação: Se o campo "Unidade" for igual a [7], preencher com 0 (zero). |
| Unidade | undSalFixo | N | 1 | 1 | Unidade de pagamento da parte fixa da remuneração. Valores válidos: 1 - Por hora 2 - Por dia 3 - Por semana 4 - Por quinzena 5 - Por mês 6 - Por tarefa 7 - Não aplicável - Salário exclusivamente variável |
| Descrição | dscSalVar | C | 0-1 | 1-999 | Descrição do salário por tarefa ou variável e como este é calculado. Ex.: Comissões pagas no percentual de 10% sobre as vendas. Validação: Preenchimento obrigatório se o campo "Unidade" for igual a [6, 7]. |

Informações geraisInformações de vínculo

Os grupos/campos contemplados na sub-aba "**Informações de vínculo**":

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Título do campo** | **Grupo/Campo** | **Tipo** | **Ocorrência** | **Tamanho** | **Descrição** |
| Informações sobre o vínculo trabalhista. Os campos abaixo pertencem ao grupo **infoVinc**. Se o campo "Tipo" (infoContr/tpContr) for diferente de "6" (Trabalhador sem vínculo de emprego/estatutário (TSVE), sem reconhecimento de vínculo empregatício), o preenchimento deste grupo é obrigatório. Caso contrário não deve ser preenchido. | | | | | |
| Tipo de regime trabalhista | tpRegTrab | N | 1 | 1 | Tipo de regime trabalhista. Valores válidos: 1 - CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas 2 - Estatutário/legislações específicas (servidor temporário, militar, agente político, etc.) Validação: Se o campo "Código da categoria" (infoContr/codCateg) = [104], deve ser preenchido com [1]. |
| Tipo de regime previdenciário | tpRegPrev | N | 1 | 1 | Tipo de regime previdenciário. Valores válidos: 1 - Regime Geral de Previdência Social - RGPS 2 - Regime Próprio de Previdência Social - RPPS 3 - Regime de Previdência Social no exterior Validação: Se o campo "Código da categoria" (infoContr/codCateg)  = [104], deve ser preenchido com [1]. Se o campo "Código da categoria" (infoContr/codCateg)  = [101, 102, 103, 105, 106, 107, 108, 111], não pode ser preenchido com [2]. |
| Data de admissão | dtAdm | D | 1 | - | Preencher com a data de admissão do trabalhador. Validação: Deve ser posterior à data de nascimento do trabalhador. |
| Tipo contrato em tempo parcial | tmpParc | N | 0-1 | 1 | Preencher com o código relativo ao tipo de contrato em tempo parcial. Informar este campo apenas no caso de empregado submetido a horário de trabalho (Capítulo II do Título II da CLT). Valores válidos: 0 - Não é contrato em tempo parcial 1 - Limitado a 25 horas semanais 2 - Limitado a 30 horas semanais 3 - Limitado a 26 horas semanais Validação: Informação obrigatória e exclusiva se "Tipo de regime previdenciário" (tpRegTrab) = [1]. O código [1] só é válido se Se o campo "Código da categoria" (infoContr/codCateg) = [104]. Os códigos [2, 3] não são válidos se o campo "Código da categoria" (infoContr/codCateg) = [104]. |
| Duração do contrato de trabalho. Os campos abaixo pertencem ao grupo **duracao**. Se o campo "Tipo de regime trabalhista" (tpRegTrab) for igual a "1" (CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas), o preenchimento deste grupo é obrigatório. Caso contrário não deve ser preenchido. | | | | | |
| Tipo contrato | tpContr | N | 1 | 1 | Tipo de contrato de trabalho. Valores válidos: 1 - Prazo indeterminado 2 - Prazo determinado, definido em dias 3 - Prazo determinado, vinculado à ocorrência de um fato |
| Data de término | dtTerm | D | 0-1 | - | Data do término do contrato por prazo determinado. Validação: O preenchimento é obrigatório se "Tipo contrato" (duracao/tpContr) = [2]. Não informar se "Tipo contrato" (duracao/tpContr) = [1]. Se preenchido, deve ser igual ou posterior à data de admissão (no caso de transferência, igual ou posterior a "Data da transferência" (sucessaoVinc/dtTransf)). |
| Cláusula assecuratória | clauAssec | C | 0-1 | 1 | Indicar se o contrato por prazo determinado contém cláusula assecuratória do direito recíproco de rescisão antes da data de seu término. Valores válidos: S - Sim N - Não Validação: O preenchimento é obrigatório se "Tipo contrato" (duracao/tpContr) = [2, 3]. Não preencher se "Tipo contrato" (duracao/tpContr) = [1]. |
| Objeto de contratação | objDet | C | 0-1 | 1-255 | Indicação do objeto determinante da contratação por prazo determinado (obra, serviço, safra, etc.). Validação: O preenchimento é obrigatório e exclusivo se "Tipo contrato" (duracao/tpContr) = [3]. |
| Grupo de informações da sucessão de vínculo trabalhista/estatutário. Os campos abaixo pertencem ao grupo **sucessaoVinc**, cujo preenchimento é opcional. | | | | | |
| Tipo inscrição | tpInsc | N | 1 | 1 | Preencher com o código correspondente ao tipo de inscrição, conforme [Tabela 05](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/tabelas.html#05). Valores válidos: 1 - CNPJ 2 - CPF 5 - CGC 6 - CEI Validação: Somente é possível informar [5] se "Data da transferência" (dtTransf) for igual ou anterior a [1999-06-30]. |
| Número inscrição | nrInsc | C | 1 | 8-14 | Informar o número de inscrição do empregador anterior, de acordo com o tipo de inscrição indicado no campo "Tipo inscrição" (sucessaoVinc/tpInsc). Validação: Se "Tipo inscrição" (sucessaoVinc/tpInsc) = [1], deve possuir 14 (catorze) algarismos e ser diferente do CNPJ base do empregador. Se "Tipo inscrição" (sucessaoVinc/tpInsc) = [2], deve possuir 11 (onze) algarismos. Se "Tipo inscrição" (sucessaoVinc/tpInsc) = [5], deve possuir somente algarismos. Se "Tipo inscrição" (sucessaoVinc/tpInsc) = [6], deve possuir 12 (doze) algarismos. |
| Matrícula anterior | matricAnt | C | 0-1 | 1-30 | Matrícula do trabalhador no empregador anterior. |
| Data da transferência | dtTransf | D | 1 | - | Preencher com a data da transferência do empregado para o empregador declarante. Validação: Deve ser posterior à data de admissão do trabalhador. |
| Informações do desligamento. Os campos abaixo pertencem ao grupo **infoDeslig**, cujo preenchimento é obrigatório. | | | | | |
| Data do desligamento | dtDeslig | D | 1 | - | Preencher com a data de desligamento do vínculo (último dia trabalhado). Validação: Deve ser igual ou posterior ao campo "Data de admissão" (dtAdm) e não superior à data atual (data do envio do evento) acrescida de 10 dias corridos. |
| Motivo | mtvDeslig | C | 1 | 2 | Código de motivo do desligamento. Validação: Deve ser um código válido e existente na [Tabela 19](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/tabelas.html#19). |
| Data aviso prévio | dtProjFimAPI | D | 0-1 | - | Data projetada para o término do aviso prévio indenizado. Validação: Se informada, deve ser igual ou posterior ao campo "Data do desligamento" (dtDeslig). |
| Indicativo de pensão alimentícia para fins de retenção de FGTS | pensAlim | N | 0-1 | 1 | Indicativo de pensão alimentícia para fins de retenção de FGTS. Valores válidos: 0 - Não existe pensão alimentícia 1 - Percentual de pensão alimentícia 2 - Valor de pensão alimentícia 3 - Percentual e valor de pensão alimentícia Validação: Preenchimento obrigatório e exclusivo se o vínculo for celetista o campo "Tipo de regime trabalhista" (tpRegTrab) = [1]. Se o campo "Data da senteça" (dtSent) ou "Data da conciliação" (dtCCP) < [2024-01-22], o preenchimento é opcional. |
| Percentual a ser destinado a pensão alimentícia | percAliment | N | 0-1 | 1-5 | Percentual a ser destinado a pensão alimentícia. Validação: Deve ser maior que 0 (zero) e menor ou igual a 100 (cem). Informação obrigatória e exclusiva se "Percentual a ser destinado a pensão alimentícia" = [1, 3]. |
| Valor da pensão alimentícia | vrAlim | N | 0-1 | 14,2 | Valor da pensão alimentícia. Validação: Deve ser maior que 0 (zero). Informação obrigatória e exclusiva se "Percentual a ser destinado a pensão alimentícia" = [2, 3]. |
| Observações do contrato de trabalho. Os campos abaixo pertencem ao grupo **observacoes**, cujo preenchimento é opcional. | | | | | |
| Observação | observacao | C | 1 | 1-255 | Observação relacionada ao contrato de trabalho. |
