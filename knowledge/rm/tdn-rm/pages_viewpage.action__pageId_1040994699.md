---
content_hash: 8e66859ef03321c1e7d93b077e4c9fa50155d085d45e30371fcbfc304e47c3b7
fetched_at: '2026-06-29T00:05:49.778924+00:00'
page_id: '1040994699'
product: rm
source: tdn-rm
title: Middleware - Relatório de Conferência IRRF S-5002 - MAPEAMENTO e ORIENTAÇÕES
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1040994699
version: 207
---

## **01. VISÃO GERAL**

Este documento tem como objetivo apresentar omapeamento dos campos exibidos no **Relatório de Conferência de IRRF – S-5002**, com a finalidade de facilitar a conferência das informações. Para isso, demonstraremos a origem de cada dado, tanto no produto TOTVS Folha de Pagamento quanto no eSocial, evento S-5002.

O documento apresenta também orientações sobre conferências e análises que devem ser realizadas quando forem identificadas divergências de valores, auxiliando na identificação da possível causa do problema.

## **02. MAPEAMENTO | ORIENTAÇÕES**

1true1MapeamentoMapeamento

Disponibilizamos abaixo o mapeamento dos campos, organizado conforme as abas do XML gerado pelo Relatório de Conferência de IRRF – S-5002, com as respectivas explicações de cada campo.

Ressaltamos que, na coluna “ORIGEM GOVERNO”, será apresentada a tag utilizada no evento S-5002.

## ⚠️ ATENÇÃO – Regra para composição de deduções (IRRF)

A regra abaixo **define se uma verba será considerada** para compor valores de **dedução de dependentes, pensão alimentícia, previdência complementar ou processos**.

---

### Verbas **candidatas** a compor deduções

Uma verba **será candidata** a compor valores de dedução **somente quando**:

* + - * `PFFINANC.VALOR ≠ 0`, **e**
      * **uma** das condições abaixo for atendida.

**PRIMEIRA CONDIÇÃO:** O campo `codIncIRRF` deve:

* + - * + Ser **um dos valores**: **46, 47, 48, 61, 62, 63, 64, 65, 66**, **ou**
        + **Iniciar com “9”**.

**SEGUNDA CONDIÇÃO:** O campo `codIncIRRF` deve ser **um dos valores**:: **31, 32, 33, 34, 35, 51, 52, 53, 54, 55, 81, 82, 83**

**E, adicionalmente**, o campo `PEVENTO.CODIGOCALCULO` **não pode ser**: 030, 107, 113, 387, 388, 417, 428, 429, 430, 431, 432, 433, 434 e 435.

---

### ❌ Regra de exclusão

Caso **nenhuma** das condições acima seja atendida, a verba **não será considerada** para compor:

* + - * Dedução de dependentes
      * Pensão alimentícia
      * Previdência complementar
      * Informações de Processos

Mapeamentotrue2-1Dedução de DependenteDedução de Dependente

**1. DEDUÇÃO DE DEPENDENTE**

| CAMPO DO S-5002 | CAMPO RELATÓRIO | ORIGEM FOLHA | ORIGEM GOVERNO | OBSERVAÇÃO |
| --- | --- | --- | --- | --- |
| Não se Aplica | Nome | PPESSOA.NOME |  | Menu Administração de Pessoal | Funcionários | Documentação | campo Nome |
| AAAA-MM | Período | Informado na tela | <ideEvento><perApur> |  |
| CPF Beneficiário | CPF | PPESSOA.CPF | <ideTrabalhador><cpfBenef> | Menu Administração de Pessoal | Funcionários | Documentação | campo CPF |
| Código de Receita | Código de Receita | Veja detalhes na aba "**Códigos da Receita**". | <infoIRComplem><infoIRCR><tpCR> |  |
| CPF do Dependente | CPF do Dependente | PFDEPEND.CPF | <infoIRComplem><infoIRCR><dedDepen><cpfDep> | Menu Administração de Pessoal | Funcionários | Folha de Pagamento | Dependentes | campo CPF |
| Tipo de Valores Relativos ao IRRF | Tipo de Rendimento | Classificação exibida no relatório conforme o código de incidência tributária da rubrica (`codIncIRRF`):   * Quando o **`codIncIRRF`** do evento for **31**, o relatório exibirá **11**. * Quando o **`codIncIRRF`** do evento for **32**, o relatório exibirá **12**. * Quando o **`codIncIRRF`** do evento for **33**, o relatório exibirá **13**. | <infoIRComplem><infoIRCR><dedDepen><tpRend> | Menu Administração de Pessoal | Eventos | Identificação | campo Código de Cálculo    Regras para definição do `codIncIRRF` conforme o código de cálculo do evento:   * Para que o **`codIncIRRF`** seja **31**, o evento (**`PEVENTO.CODIGOCALCULO`**) deve possuir um dos seguintes códigos de cálculo: 4, 84, 122, 207 ou 346.      * Para que o **`codIncIRRF`** seja **32**, o evento (**`PEVENTO.CODIGOCALCULO`**) deve possuir um dos seguintes códigos de cálculo: 49, 52, 106, 215, 340 ou 347.      * Para que o **`codIncIRRF`** seja **33**, o evento (**`PEVENTO.CODIGOCALCULO`**) deve possuir um dos seguintes códigos de cálculo: 30, 61, 107, 211 ou 348. |
| Valor da Dedução | Valor da Dedução Mensal | Somatório da dedução de dependentes PFDEPIRRFDED.VALOR no período informado na tela de acordo com o código de incidência tributária da rubrica para o IRRF | <infoIRComplem><infoIRCR><dedDepen><vlrDedDep> | Menu Administração de Pessoal | Funcionários | Folha de Pagamento | Dependentes | Anexos | Valor Dedução do Rendimento Tributável | campo Valor |

2-2Pensão AlimentíciaPensão Alimentícia

**2. PENSÃO ALIMENTÍCIA**

| CAMPO DO S-5002 | CAMPO RELATÓRIO | ORIGEM FOLHA | ORIGEM GOVERNO | OBSERVAÇÃO |
| --- | --- | --- | --- | --- |
| Não se Aplica | Nome | PPESSOA.NOME |  | Menu Administração de Pessoal | Funcionários | Documentação | campo Nome |
| AAAA-MM | Período | Informado na tela | <ideEvento><perApur> |  |
| CPF Beneficiário | CPF | PPESSOA.CPF | <ideTrabalhador><cpfBenef> | Menu Administração de Pessoal | Funcionários | Documentação | campo CPF |
| Código de Receita | Código de Receita | Veja detalhes na aba "**Códigos da Receita**". | <infoIRComplem><infoIRCR><tpCR> |  |
| Não se Aplica | Nome do Titular / Dependente | PFDEPEND.NOME |  | Menu Administração de Pessoal | Funcionários | Folha de Pagamento | Dependentes | campo Nome |
| Tipo de Valores Relativos ao IRRF | Tipo do Rendimento | Classificação exibida no relatório conforme o código de incidência tributária da rubrica (`codIncIRRF`) e a existência de eventos de RRA:   * Quando o **`codIncIRRF`** for **51**:    + Com eventos de RRA (códigos de cálculo 206 ou 394), o relatório exibirá **18**.   + Sem eventos de RRA, o relatório exibirá **11**. * Quando o **`codIncIRRF`** for **52**:    + Com eventos de RRA (códigos de cálculo 214 ou 395), o relatório exibirá **18**.   + Sem eventos de RRA, o relatório exibirá **12**. * Quando o **`codIncIRRF`** for **53**:    + Com eventos de RRA (códigos de cálculo 210, 396 ou 397), o relatório exibirá **18**.   + Sem eventos de RRA, o relatório exibirá **13**. * Quando o **`codIncIRRF`** for **54**, o relatório exibirá **14**. | <infoIRComplem><infoIRCR><penAlim><tpRend> | Menu Administração de Pessoal | Eventos | Identificação | campo Código de Cálculo Menu Administração de Pessoal | Eventos | Inc. Descontos | campo Dedutível IRRF Menu Administração de Pessoal | Eventos | Inc. Descontos | campo Estorna IRRF Menu Administração de Pessoal | Eventos | Inc. Descontos | campo Dedutível IRRF 13º Menu Administração de Pessoal | Eventos | Inc. Descontos | campo Estorna IRRF 13º Menu Administração de Pessoal | Eventos | Inc. Descontos | campo Dedutível IRRF Férias Menu Administração de Pessoal | Eventos | Inc. Descontos | campo Estorna IRRF de Férias    Regras para definição do `codIncIRRF` conforme o código de cálculo e indicadores do evento:   * Para que o **`codIncIRRF`** seja **51**, o evento (`PEVENTO.``CODIGOCALCULO`) deve possuir um dos seguintes códigos de cálculo: 13, 53, 195, 206, 386 ou 394, e o campo `PEVENTO.DEDUTIVELIRRF` ou `PEVENTO.ESTIRRF` deve estar VERDADEIRO.      * Para que o **`codIncIRRF`** seja **52**, o evento (**`PE`**`VENTO.CODIGOCALCULO`) deve possuir um dos seguintes códigos de cálculo: 54, 120, 196, 214, 395 ou 407, e o campo `PEVENTO.DEDUTIVELIRRF13` ou `PEVENTO.ESTIRRF13` deve estar VERDADEIRO.      * Para que o **`codIncIRRF`** seja **53**, o evento (`PEVENTO.CODIGOCALCULO`) deve possuir um dos seguintes códigos de cálculo: 113, 197, 210, 319, 320, 326, 396, 397 ou 4068, e o campo `PEVENTO.DEDUTIVELIRRFFERIAS` ou `PEVENTO.ESTIRRFFERIAS` deve estar VERDADEIRO.      * Para que o **`codIncIRRF`** seja **54**, o evento (`PEVENTO.CODIGOCALCULO`) deve possuir um dos seguintes códigos de cálculo: 121, 321 ou 408. |
| CPF do Dependente | CPF Dependente | PFDEPEND.CPF | <infoIRComplem><infoIRCR><penAlim><cpfDep> | Menu Administração de Pessoal | Funcionários | Folha de Pagamento | Dependentes | campo CPF |
| Valor da Dedução Pagamento de Pensão Alimentícia | Valor Dedução Mensal | Corresponde ao somatório dos valores de pensão alimentícia do beneficiário (campo PFDEPMOV.VALOR), considerando o período informado na tela e respeitando o código de incidência tributária da rubrica para o IRRF. | <infoIRComplem><infoIRCR><penAlim><vlrDedPenAlim> | Menu Administração de Pessoal | Funcionários | Folha de Pagamento | Dependentes | Movimentação da Pensão de Dependentes | campo Valor |

2-3Previdência ComplementarPrevidência Complementar

**3. PREVIDÊNCIA COMPLEMENTAR**

| CAMPO DO S-5002 | CAMPO RELATÓRIO | ORIGEM FOLHA | ORIGEM GOVERNO | OBSERVAÇÃO |
| --- | --- | --- | --- | --- |
| Não se Aplica | Nome | PPESSOA.NOME |  | Menu Administração de Pessoal | Funcionários | Documentação | campo Nome |
| AAAA-MM | Período | Informado na tela | <ideEvento><perApur> |  |
| CPF Beneficiário | CPF | PPESSOA.CPF | <ideTrabalhador><cpfBenef> | Menu Administração de Pessoal | Funcionários | Documentação | campo CPF |
| Código de Receita | Código de Receita | Veja detalhes na aba "**Códigos da Receita**". | <infoIRComplem><infoIRCR><tpCR> |  |
| Não se Aplica | Nome do Titular / Dependente | PFDEPEND.NOME |  | Menu Administração de Pessoal | Funcionários | Folha de Pagamento | Dependentes | campo Nome |
| Tipo de Previdência Complementar | Tipo da Previdência | Classificação exibida no relatório conforme o código de incidência tributária da rubrica (`codIncIRRF`):   * Quando o `codIncIRRF` do evento for **46, 47 ou 48**, o relatório exibirá **1**. * Quando o `codIncIRRF` do evento for **61, 62 ou 66**, o relatório exibirá **2**. * Quando o `codIncIRRF` do evento for **63, 64 ou 65**, o relatório exibirá **3**. | <infoIRComplem><infoIRCR><previdCompl><tpPrev> | Menu Administração de Pessoal | Eventos | Inc. Proventos | campo Tipo de Previdência Complementar    Para que o **`codIncIRRF`** seja **46, 47, 48, 61, 62, 63, 64, 65 ou 66**, o campo **`PEVENTO.TIPOPREVIDENCIACOMPLEMENTAR`** deve estar preenchido com uma das opções válidas de previdência complementar. |
| Número de Inscrição da Entidade de Previdência Complementar | CNPJ - Entidade de Previdência Complementar | PPREVIDENCIACOMPLEMENTAR.CNPJ | <infoIRComplem><infoIRCR><previdCompl><cnpjEntidPC> | Menu eSocial | Previdência Complementar | Cadastro Previdência Complementar | campo CNPJ |
| Valor da Dedução Relativa a Previdência Complementar | Valor | Somatório do valor dos eventos de previdência complementar lançados na ficha financeira, no período informado na tela, cujo `codIncIRRF` seja igual a 46, 47, 48, 61, 62, 63, 64, 65 ou 66, e com o campo “Décimo Terceiro” desmarcado no cadastro dos eventos de previdência complementar. | <infoIRComplem><infoIRCR><previdCompl><vlrDedPC> | Menu eSocial | Previdência Complementar | Cadastro Previdência Complementar | Eventos da Previdência Complementar | campo Evento |
| Valor da Dedução 13° Salário Relativa a Previdência Complementar | Valor 13° Salário | Somatório do valor dos eventos de previdência complementar lançados na ficha financeira, no período informado na tela, cujo `codIncIRRF` seja igual a 46, 47, 48, 61, 62, 63, 64, 65 ou 66, e com o campo “Décimo Terceiro” marcado no cadastro dos eventos de previdência complementar. | <infoIRComplem><infoIRCR><previdCompl><vlrDedPC13> | Menu eSocial | Previdência Complementar | Cadastro Previdência Complementar | Eventos da Previdência Complementar | campo Evento e campo Décimo Terceiro |
| Valor da Contribuição Mensal do Ente Público Funpresp | Valor de Servidor Público | Não mapeado |  |  |
| Valor da Contribuição  13° Salário do Ente Público Funpresp | Valor de Servidor Público 13° Salário | Não mapeado |  |  |

2-4Informações de ProcessosInformações de Processos

**4. INFORMAÇÕES DE PROCESSOS**

| CAMPO DO S-5002 | CAMPO RELATÓRIO | ORIGEM FOLHA | ORIGEM GOVERNO | OBSERVAÇÃO |
| --- | --- | --- | --- | --- |
| Não se Aplica | Nome | PPESSOA.NOME |  | Menu Administração de Pessoal | Funcionários | Documentação | campo Nome |
| AAAA-MM | Período | Informado na tela | <ideEvento><perApur> |  |
| CPF Beneficiário | CPF | PPESSOA.CPF | <ideTrabalhador><cpfBenef> | Menu Administração de Pessoal | Funcionários | Documentação | campo CPF |
| Código de Receita | Código de Receita | Veja detalhes na aba "**Códigos da Receita**". | <infoIRComplem><infoIRCR><tpCR> |  |
| Número do Processo Administrativo/Judicial | Nr. Processos | PPROCSUSPENSAOINC.NRPROCESSO | <infoIRComplem><infoIRCR><infoProcRet><nrProcRet> | Menu Administração de Pessoal | Eventos | Eventos | Processo de Suspensão de Incidência | campo Nº do Processo |
| Tipo Processo | Tp. Processo | PPROCSUSPENSAOINC.TPPROCESSO | <infoIRComplem><infoIRCR><infoProcRet><tpProcRet> | Menu Administração de Pessoal | Eventos | Eventos | Processo de Suspensão de Incidência | campo Tipo do Processo |
| Código do Indicativo da Suspensão | Cod. Susp | PPROCSUSPENSAOINC.CODINCSUSP | <infoIRComplem><infoIRCR><infoProcRet><codSusp> | Menu Administração de Pessoal | Eventos | Eventos | Processo de Suspensão de Incidência | campo Código do Indicativo da Suspensão |
| Indicativo Período Apuração | Ind. Per. Fiscal | PESOCIALFOLHAMENSAL.INDAPURACAO | <infoIRComplem><infoIRCR><infoProcRet><infoValores><indApuracao> | Menu eSocial | Período de Apuração | campo Indicativo de Período de Apuração |
| Valor da Retenção que deixou de ser efetuada em função do processo administrativo / Judicial | Vlr. Rent. Jud/adm | Somatório do valor dos eventos da ficha financeira cujo codIncIRRF em S-1010 = [9XXX] (exceto [9067]). | <infoIRComplem><infoIRCR><infoProcRet><infoValores><vlrNRetido> | Menu Administração de Pessoal | Eventos | Inc. Proventos | Incidência(s) suspensa(s) em decorrência de decisão judicial | campo Incidência IRRF                                                   Menu Administração de Pessoal | Eventos | Inc. Descontos | Incidência(s) suspensa(s) em decorrência de decisão judicial | campo Incidência IRRF    Para codIncIRRF ser 9XXX o campo PEVENTO.INCIRRFSUSPENSAO deve estar preenchido. |
| Valor do Deposito Judicial em função do processo Administrativo / Judicial | Vlr. Depo. Adm/Jud | Não mapeado |  |  |
| Valor Compensação Relativa ao Ano Calendário em Função de Processo Judicial | Vlr. Comp. Jud. | Não mapeado |  |  |
| Valor Compensação Relativa ao Ano Anteriores em Função de Processo Judicial | Vlr. Comp. Retro. Jud. | Não mapeado |  |  |
| Valor do Rendimento com Exigibilidade Suspensa | Vlr. Rend. Exig. Susp. | Não mapeado |  |  |
| Indicativo Tipo Dedução | Ind. Tp. Dedução | Não mapeado |  |  |
| Valor Dedução da Base Cálculo do IRRF com Exigibilidade Suspensa | Vlr. Ded. Imp. | Não mapeado |  |  |
| Número de Inscrição da Entidade de Previdência Complementar | CNPJ da entidade | Não mapeado |  |  |
| Valor da Contribuição do Ente Funpresp | Vlr. Contrib. Fun. - TAF | Não mapeado |  |  |
| CPF do Dependente | CPF do Dependente | Não mapeado |  |  |
| Valor da Dedução Relativa a Dependente ou a Pensão Alimentícia com Exigibilidade Suspensa | Vlr. Ded ou pen. Alim. | Não mapeado |  |  |

2-5Plano de SaúdePlano de Saúde

**5. PLANO DE SÁÚDE**

| CAMPO DO S-5002 | CAMPO RELATÓRIO | ORIGEM FOLHA | ORIGEM GOVERNO | OBSERVAÇÃO |
| --- | --- | --- | --- | --- |
| Não se Aplica | Nome | PPESSOA.NOME |  | Menu Administração de Pessoal | Funcionários | Documentação | campo Nome |
| AAAA-MM | Período | Informado na tela | <ideEvento><perApur> |  |
| CPF Beneficiário | CPF | PPESSOA.CPF | <ideTrabalhador><cpfBenef> | Menu Administração de Pessoal | Funcionários | Documentação | campo CPF |
| CNPJ da Operadora de Plano Privado Coletivo Empresarial de Assistência a Saúde | CNPJ Operadora | VOPERADORASAUDE.CNPJ | <infoIRComplem><planSaude><cnpjOper> | Menu eSocial | Operadora Saúde | Cadastro Operadoras de Saúde | campo CNPJ |
| Registro na Agência Nacional de Saúde | Registro ANS | VOPERADORASAUDE.REGISTROANS | <infoIRComplem><planSaude>   <regANS> | Menu eSocial | Operadora Saúde | Cadastro Operadoras de Saúde | campo Registro ANS |
| Não se Aplica | CPF Benef. | PPESSOA.CPF Exibido no relatório somente quando o valor de assistência saúde se refere ao titular. |  | Menu Administração de Pessoal | Funcionários | Documentação | campo CPF |
| Valor Relativo a Dedução do Rendimento Tributável Correspondente a Pagamento a Plano de Saúde do Titular | Vlr. Titular | Valor do titular PFHSTASSMED.VALOR informado no histórico de assistência saúde desde que o evento informado no cadastro de operadoras de saúde esteja lançado na ficha financeira no período informado na tela. | <infoIRComplem><planSaude><vlrSaudeTit> | Menu eSocial | Operadora Saúde | Cadastro Operadoras de Saúde | Eventos da Operadora | campo Evento  Menu Administração de Pessoal | Funcionários | Históricos | Histórico Assistência Saúde | campo Valor |
| CPF do Dependente do Plano de Saúde | CPF Dep. | PFDEPEND.CPF Exibido no relatório somente quando o valor de assistência saúde se refere ao dependente. | <infoIRComplem><planSaude><infoDepSau>  <cpfDep> | Menu Administração de Pessoal | Funcionários | Folha de Pagamento | Dependentes | campo CPF |
| Valor Relativo a Dedução do Rendimento Tributável Correspondente a Pagamento a Plano de Saúde do Dependente | Vlr.Dep | Valor do dependente PFHSTASSMED.VALOR informado no histórico de assistência saúde com o campo beneficiário PFHSTASSMED.NRODEPEND preenchido com o dependente,  e o evento informado no cadastro de operadoras de saúde lançado na ficha financeira no período informado na tela. | <infoIRComplem><planSaude><infoDepSau>  <vlrSaudeDep> | Menu eSocial | Operadora Saúde | Cadastro Operadoras de Saúde | Eventos da Operadora | campo Evento  Menu Administração de Pessoal | Funcionários | Históricos | Histórico Assistência Saúde | campo Beneficiário  Menu Administração de Pessoal | Funcionários | Históricos | Histórico Assistência Saúde | campo Valor |

2-6Reembolso MédicoReembolso Médico

**6. REEMBOLSO MÉDICO**

| CAMPO DO S-5002 | CAMPO RELATÓRIO | ORIGEM FOLHA | ORIGEM GOVERNO | OBSERVAÇÃO |
| --- | --- | --- | --- | --- |
| Não se Aplica | Nome | PPESSOA.NOME |  | Menu Administração de Pessoal | Funcionários | Documentação | campo Nome |
| AAAA-MM | Período | Informado na tela | <ideEvento><perApur> |  |
| CPF Beneficiário | CPF | PPESSOA.CPF | <ideTrabalhador><cpfBenef> | Menu Administração de Pessoal | Funcionários | Documentação | campo CPF |
| Registro na Agência Nacional de Saúde | Código ANS | VOPERADORASAUDE.REGISTROANS | <infoIRComplem><infoReembMed><regANS> | Menu Anuais | Dirf | Reembolso da Operadora de Assistência à Saúde | campo Operadora |
| Indicativo da Origem do Reembolso | Origem Reemb. | PFREEMBOLSOOPERADORA.INDICATIVOORIGEMREEMBOLSO | <infoIRComplem><infoReembMed><indOrgReemb> | Menu Anuais | Dirf | Reembolso da Operadora de Assistência à Saúde | campo Indicativo da Origem do Reembolso |
| CNPJ da Operadora do Plano de Saúde | Nr. Inscr. | VOPERADORASAUDE.CNPJ | <infoIRComplem><infoReembMed><cnpjOper> | Menu Anuais | Dirf | Reembolso da Operadora de Assistência à Saúde | campo Operadora |
| Não se Aplica | Benef. CPF | PPESSOA.CPF Exibido no relatório somente quando o valor de reembolso se refere ao titular PFREEMBOLSOOPERADORA.CHAPA |  | Menu Anuais | Dirf | Reembolso da Operadora de Assistência à Saúde | campo Chapa  Menu Administração de Pessoal | Funcionários | Documentação | campo CPF |
| Número e Inscrição do Prestador de Serviço de Assistência Médica | Benef. Inscr. | VENTIDADES.CGCCPF | infoIRComplem><infoReembMed><detReembTit>   <nrInsc> | Menu Anuais | Dirf | Reembolso da Operadora de Assistência à Saúde | campo Entidade(Prestador de Serviço) |
| Tipo de Inscrição do Prestador de Serviço de Assistência Médica | Benf. Tp. Inscr. | Relatório exibe 1 ou 2 de acordo com o campo VENTIDADES.CGCCPF | <infoIRComplem><infoReembMed><detReembTit>  <tpInsc> | Menu Anuais | Dirf | Reembolso da Operadora de Assistência à Saúde | campo Entidade(Prestador de Serviço) |
| Valor do Reembolso Relativo ao Ano do Período Indicado em perApur | Vlr Total | PFREEMBOLSOOPERADORAMENSAL.VALORATUAL | <infoIRComplem><infoReembMed><detReembTit><vlrReemb> | Menu Anuais | Dirf | Reembolso da Operadora de Assistência à Saúde | campo Valor Ano Atual |
| Valor do Reembolso Relativo a Anos Anteriores | Não implementado |  | <vlrReembAnt> |  |
| CPF do Dependente do Reembolso do Plano de Saúde | Dep. CPF | PFDEPEND.CPF Exibido no relatório somente quando o valor de reembolso se refere ao dependente PFREEMBOLSOOPERADORA.NRODEPEND | <infoIRComplem><infoReembMed><infoReembDep><cpfBenef> | Menu Anuais | Dirf | Reembolso da Operadora de Assistência à Saúde | campo Dependente  Menu Administração de Pessoal | Funcionários | Folha de Pagamento | Dependentes | campo CPF |
| Número e Inscrição do Prestador de Serviço de Assistência Médica | Dep. Inscr. | VENTIDADES.CGCCPF | <infoIRComplem><infoReembMed><infoReembDep><detReembDep><nrInsc> | Menu Anuais | Dirf | Reembolso da Operadora de Assistência à Saúde | campo Entidade(Prestador de Serviço) |
| Tipo de Inscrição do Prestador de Serviço de Assistência Médica | Dep.Tipo Inscr. | Relatório exibe 1 ou 2 de acordo com o campo VENTIDADES.CGCCPF | <infoIRComplem><infoReembMed><infoReembDep><detReembDep><tpInsc> | Menu Anuais | Dirf | Reembolso da Operadora de Assistência à Saúde | campo Entidade(Prestador de Serviço) |
| Valor do Reembolso Relativo ao Ano do Período Indicado em perApur | Dep. Vlr Atual | PFREEMBOLSOOPERADORAMENSAL.VALORATUAL | <infoIRComplem><infoReembMed><infoReembDep><detReembDep><vlrReemb> | Menu Anuais | Dirf | Reembolso da Operadora de Assistência à Saúde | campo Valor Ano Atual |
| Valor do Reembolso Relativo a Anos Anteriores | Dep. Vlr Aterior | PFREEMBOLSOOPERADORAMENSAL.VALORANTERIOR | <infoIRComplem><infoReembMed><infoReembDep><detReembDep><vlrReembAnt> | Menu Anuais | Dirf | Reembolso da Operadora de Assistência à Saúde | campo Valor Ano Atual |

2-78Totalizador MensalTotalizador Mensal

**8. TOTALIZADOR**

Uma verba **realizará estorno ou dedução** quando **pelo menos um** dos campos abaixo estiver com valor **VERDADEIRO**:

* `ESTIRRF`
* `ESTIRRFFERIAS`
* `ESTIRRF13`
* `DEDUTIVELIRRF`
* `DEDUTIVELIRRFFERIAS`
* `DEDUTIVELIRRF13`

Caso **todos** os campos acima estejam com valor **FALSO**, a verba **não será considerada** para estorno ou dedução de IRRF.

**Atenção:** O grupo utilizado do S-5002 para buscar as informações de totalização é o **<totInfoIR>**.

| CAMPO DO S-5002 | CAMPO RELATÓRIO | ORIGEM FOLHA | ORIGEM GOVERNO | OBSERVAÇÃO |
| --- | --- | --- | --- | --- |
| Não se Aplica | Nome | PPESSOA.NOME |  | Menu Administração de Pessoal | Funcionários | Documentação | campo Nome |
| AAAA-MM | Período | Informado na tela | <ideEvento><perApur> |  |
| CPF Beneficiário | CPF | PPESSOA.CPF | <ideTrabalhador><cpfBenef> | Menu Administração de Pessoal | Funcionários | Documentação | campo CPF |
| Código de Receita | Código de Receita | Veja detalhes na aba "**Códigos da Receita**". |  |  |
| Valor Relativo ao Rendimento Tributável Mensal e Férias | Rend. Tributavel | **Regras para definição do `codIncIRRF` (11 ou 13):**  Para retornar na tag **`codIncIRRF`** o valor **11**, o evento (PEVENTO) deve atender uma das seguintes condições:   * **`INCIRRF`** = **VERDADEIRO** * **`INCIRRFSUSPENSA`** = **VERDADEIRO** * **DEDUTIVELIRRF =** **VERDADEIRO** * **`CODIGOCALCULO`** = **204**     Para retornar na tag **`codIncIRRF`** o valor **13,** o evento (PEVENTO) deve atender uma das seguintes condições:   * **`INCIRRFFERIAS`** = **VERDADEIRO** * **`INCIRRFSUSPENSA`** = **VERDADEIRO** * **`DEDUTIVELIRRFFERIAS`**= **VERDADEIRO** * **`CODIGOCALCULO`** ∈ **{208, 381}** | <vlrRendTrib> |  |
| Valor Relativo ao Rendimento do 13° Salário | Rend. Tributavel 13° | **Regra para definição do `codIncIRRF` = 12**  Para que o **`codIncIRRF`** retorne o valor **12**, o evento (PEVENTO) deve atender uma das  seguintes condições:   * **INCIRRF13**= **VERDADEIRO** * **`INCIRRFSUSPENSA`** = **VERDADEIRO** * **DEDUTIVELIRRF13** = **VERDADEIRO** * **`CODIGOCALCULO`** = **212** | <vlrRendTrib13> |  |
| Valor Relativo a Previdência Oficial sobre Rendimentos do Trabalho, Mensal e Férias | Prev. Oficial | **Regras para definição do `codIncIRRF` (41 ou 43):**    Para retornar na tag **`codIncIRRF`** o valor **41**, o evento (PEVENTO) deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **FALSO** * **`TIPOPREVIDENCIACOMPLEMENTAR`** = **NULO** * **`INCIRRFSUSPENSAO`** = **NULO** * **`RENDNAOTRIBACORDOINTERNAC`** = **FALSO** * **`CODIGOCALCULO`** ∈ **{003, 068, 085, 092}**     Para retornar na tag **`codIncIRRF`** o valor **43**:   * Se **`PEVENTO.CODIGO`** for igual a **`ESOCIALEVENTOINSSANTECIPFERIAS`** (quando preenchido), o evento será enquadrado com **`codIncIRRF = 43`**. * Quando `ESOCIALEVENTOINSSANTECIPFERIAS` não estiver preenchido, o evento (PEVENTO) deve atender simultaneamente às seguintes condições:    + **`FORCARINCIRRF`** = **FALSO**   + **`ISENTOIRRF`** = **FALSO**   + **`TIPOPREVIDENCIACOMPLEMENTAR`** = **NULO**   + **`INCIRRFSUSPENSAO`** = **NULO**   + **`RENDNAOTRIBACORDOINTERNAC`** = **FALSO**   + **`CODIGOCALCULO`** ∈ **{082, 110, 130, 132, 141, 349}** | <vlrPrevOficial> |  |
| Valor Relativo a Previdência Oficial 13° Salário | Prev. Oficial 13° | **Regra para definição do `codIncIRRF` = 42**  Para que o **`codIncIRRF`** retorne o valor **42**, o evento (PEVENTO) deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **FALSO** * **`TIPOPREVIDENCIACOMPLEMENTAR`** = **NULO** * **`INCIRRFSUSPENSAO`** = **NULO** * **`RENDNAOTRIBACORDOINTERNAC`** = **FALSO** * **`CODIGOCALCULO`** ∈ **{011, 103, 108, 153, 171}** | <vlrPrevOficial13> |  |
| Valor Relativo ao Imposto sobre a Renda Retido na Fonte sobre Rendimento do Trabalho, Mensal e Férias | IR Retido | **Regras para definição do `codIncIRRF` (31 ou 33):**    Para retornar na tag `cod``IncIRRF` o valor **31**, o evento (PEVENTO) deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **FALSO** * **`TIPOPREVIDENCIACOMPLEMENTAR`** = **NULO** * **`INCIRRFSUSPENSAO`** = **NULO** * **`RENDNAOTRIBACORDOINTERNAC`** = **FALSO** * **`CODIGOCALCULO`** ∈ **{004, 084, 346, 122, 207}**   Para retornar na tag `codIncIRRF` o valor **33**, o evento (PEVENTO) deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF` = FALSO** * **`ISENTOIRRF` = FALSO** * **`TIPOPREVIDENCIACOMPLEMENTAR` = NULO** * **`INCIRRFSUSPENSAO` = NULO** * **`RENDNAOTRIBACORDOINTERNAC` = FALSO** * **`CODIGOCALCULO`** ∈ **{030, 061, 107, 348, 215}** | <vlrCRMen> |  |
| Valor Relativo ao Imposto sobre a Renda Retido na Fonte sobre Rendimento do Trabalho, 13° Salário | IR Retido 13° | **Regra para definição do `codIncIRRF` = 32:**  Para retornar na tag **`codIncIRRF`** o valor **32**, o evento (PEVENTO) deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **FALSO** * **`TIPOPREVIDENCIACOMPLEMENTAR`** = **NULO** * **`INCIRRFSUSPENSAO`** = **NULO** * **`RENDNAOTRIBACORDOINTERNAC`** = **FALSO** * **`CODIGOCALCULO` ∈ {049, 106, 340, 347, 052, 211}** | <vlrCR13Men> |  |
| Valor Relativo a Parcela Isenta de Proventos de Aposentadoria, Reserva Remunerada, Reforma e Pensão de Beneficiário com 65 anos ou mais | Parc. Inse. 65 | O PEVENTO deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **VERDADEIRO** * **`INCIRRFISENCAO`** = **70** | <vlrParcIsenta65> |  |
| Valor Relativo a Parcela Isenta de Proventos de Aposentadoria, Reserva Remunerada, Reforma e Pensão de Beneficiário com 65 anos ou mais sobre o 13° Salário | Parc. Inse. 65 13 | O PEVENTO deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **VERDADEIRO** * **`INCIRRFISENCAO`** = **71** | <vlrParcIsenta65Dec> |  |
| Valor Relativo a Diárias | Diárias | O PEVENTO deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **VERDADEIRO** * **`INCIRRFISENCAO`** = **72** | <vlrDiarias> |  |
| Valor Relativo a Ajuda de Custo | Ajuda Custo | O PEVENTO deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **VERDADEIRO** * **`INCIRRFISENCAO`** = **73** | <vlrAjudaCusto> |  |
| Valor Relativo a Indenização e Rescisão de Contrato, inclusive a título de PDV e Acidente de Trabalho | Inde. Resc. Contrato | Para que o **`codIncIRRF`** retorne o valor **74**, o evento (PEVENTO) deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **FALSO** * **`TIPOPREVIDENCIACOMPLEMENTAR`** = **NULO** * **`INCIRRFSUSPENSAO`** = **NULO** * **`RENDNAOTRIBACORDOINTERNAC`** = **FALSO** * **`CODIGOCALCULO`** ∈ **{062, 099}** * **`INCIRRF`** = **FALSO** | <vlrIndResContrato> |  |
| Valor Relativo ao Abono Pecuniário | Abono Pec. | Para que o **`codIncIRRF`** retorne o valor **75**, o evento (PEVENTO) deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **FALSO** * **`TIPOPREVIDENCIACOMPLEMENTAR`** = **NULO** * **`INCIRRFSUSPENSAO`** = **NULO** * **`RENDNAOTRIBACORDOINTERNAC`** = **FALSO** * **`CODIGOCALCULO`** ∈ **{039, 047, 056, 059, 176, 311, 312, 398}** * **`INCIRRFFERIAS`** = **FALSO** * **`INCIRRF`** = **FALSO** * **`INCIRRF13`** = **FALSO** | <vlrAbonoPec> |  |
| Valor Relativo ao Rendimento de Beneficiário com Moléstia Grave ou Acidente em Serviço - Remuneração Mensal | Moléstia grave | O PEVENTO deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **VERDADEIRO** * **`INCIRRFISENCAO`** = **76** | <vlrRendMoleGrave> |  |
| Valor Relativo ao Rendimento de Beneficiário com Moléstia Grave ou Acidente em Serviço - 13° Salário | Moléstia grave 13° | O PEVENTO deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **VERDADEIRO** * **`INCIRRFISENCAO`** = **77** | <vlrRendMoleGrave13> |  |
| Valor Relativo a Auxilio Moradia | Aux. Moradia | O **PEVENTO** deve atender **simultaneamente** às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **VERDADEIRO** * **`INCIRRFISENCAO`** = **700** | <vlrAuxMoradia> |  |
| Valor Relativo a Bolsa Médico Residentes, Mensal | Bolsa Médico | O PEVENTO deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **VERDADEIRO** * **`INCIRRFISENCAO`** = **702** | <vlrBolsaMedico> |  |
| Valor Relativo a bolsa Médico Residentes, 13° Salário | Bolsa Médico 13° | O PEVENTO deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **VERDADEIRO** * **`INCIRRFISENCAO`** = **703** | <vlrBolsaMedico13> |  |
| Valor relativo ao juros de mora Recebidos, Devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função. | JurosMoradia | O PEVENTO deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **VERDADEIRO** * **`INCIRRFISENCAO`** = **704** | <vlrJurosMora> |  |
| Valor relativo aos rendimentos isentos - outros | Isentos - Outros | O PEVENTO deve atender simultaneamente às seguintes condições:   * **`FORCARINCIRRF`** = **FALSO** * **`ISENTOIRRF`** = **VERDADEIRO** * **`INCIRRFISENCAO`** = **79** | <vlrIsenOutros> |  |
| Descrição do rendimento não tributável ou isento do IRRF. | Não implementado |  | <descRendimento> |  |

2-7Códigos de ReceitaCódigos de Receita

**7. CÓDIGO DE RECEITA**

Uma verba é avaliada com base em um conjunto ordenado de regras para determinar em qual código de receita ela se enquadra.  
A ordem de avaliação dos códigos de receita está definida na tabela abaixo.

A avaliação ocorre de formasequencial e excludente:  
assim que a verba atender às condições de um determinado código de receita, a avaliação é encerrada, e a verba é vinculada a esse código.

Caso a verba não atenda às condições de nenhum dos códigos de receita avaliados, ela não será considerada no relatório.

**Exemplo 1:**  
Uma verba foi enquadrada no código de receita **188901**.  
Antes disso, ela foi avaliada como candidata ao código **047301**, porém **não atendeu às suas condições**.  
Dessa forma, a **pré-condição** para o enquadramento no código **188901** é que a verba **não se enquadre no código 047301**, e assim sucessivamente, respeitando a ordem definida até o último código de receita.

**Exemplo 2:**  
Uma verba atendeu às condições do código de receita **353301**.  
Isso implica que ela **não se enquadrou** nos códigos de receita **047301**, **188901** e **056111**, que são avaliados anteriormente na ordem de priorização.

| CÓDIGOS DE RECEITA | DESCRIÇÃO | OBSERVAÇÃO |
| --- | --- | --- |
| 047301 | IRRF - Residentes no exterior, para fins fiscais | Para que uma verba seja considerada no código de receita `047301`, devem ser atendidas simultaneamente as seguintes condições::   * A **chapa do funcionário** deve estar cadastrada na tabela **`PFDADOSRESIDEXTERIOR`**, caracterizando **residente no exterior**; * O campo **`PESOCIALEMPREGADOR.CLASSTRIB`** **não** deve ser igual a **22**; * O evento (**`PEVENTO`**) deve atender a **uma** das condições abaixo:    + **`PEVENTO.CODIGOCALCULO`** ∈ **{004, 084, 346, 030, 061, 107, 348, 049, 106, 340, 347, 013, 053, 195, 386, 113, 197, 319, 320, 326, 406, 054, 120, 196, 407}**; **ou**   + O **tipo de rendimento** deve **iniciar com 2 ou 4**. |
| 188901 | Rendimentos Recebidos Acumuladamente - RRA | Uma verba será considerada no código de receita `188901` quando não se enquadrar nas regras do código de receita `047301` e, adicionalmente, atender simultaneamente às seguintes condições:   * A **chapa do funcionário** **não** deve estar cadastrada na tabela **`PFDADOSRESIDEXTERIOR`**, caracterizando **não residente no exterior**; * O **tipo de rendimento** deve ser **diferente de 0**; * O **`CODIGOCALCULO`** do evento deve ser **um dos seguintes**: **{207, 211, 215, 206, 394, 214, 395, 210, 396, 397}**. |
| 056111 | IRRF - Empregado/Trabalhador rural - Segurado especial | Para que uma verba seja considerada no código de receita `056111`, ela não deve se enquadrar nos códigos de receita `047301` e `188901` e deve atender simultaneamente às seguintes condições:   * **`PESOCIALEMPREGADOR.CLASSTRIB`** = **22**; * **`PFUNC.CODCATEGORIAESOCIAL`** ∈ **{101, 102, 103, 105, 106, 107, 108, 111}**; * A **chapa do funcionário** **não** deve estar cadastrada na tabela **`PFDADOSRESIDEXTERIOR`**, caracterizando **não residente no exterior**; * **Tipo de Rendimento** = **11**.   **Regras adicionais para Tipo de Rendimento = 11:**   * O **`codIncIRRF`** deve ser **51**; * O **`PEVENTO.CODIGOCALCULO`** deve ser **diferente de 206 e 394**. |
| 353301 | Proventos de aposentadoria, reserva, reforma ou pensão pagos por previdência pública | Para que uma verba seja considerada no código de receita `353301`, ela não deve se enquadrar nos códigos de receita `047301`, `188901` e `056111`, e deve atender simultaneamente às seguintes condições:   * **Tipo de Pagamento** = **5**.  ---   **Regras para Tipo de Pagamento = 5:**  O **Tipo de Pagamento = 5** será considerado quando ocorrer **uma das situações abaixo**:   * **Contém pagamento de 13º salário**, **não** é **regime próprio** e **possui pagamento de benefício**; **ou** * **Não contém pagamento de 13º salário** e **possui pagamento de benefício**.  ---   **Critério para conter pagamento de 13º salário:**  Considera-se que **há pagamento de 13º salário** quando existir, no período filtrado, **algum evento** com:   * **`PEVENTO.CODIGOCALCULO`** ∈ **{102, 343, 371}**; * **`PFPERFF.RETIFICACAO`** = **2**;   considerando a associação entre **PFUNC**, **PFPERFF**, **PFFINANC** e **PEVENTO**.   ---   **Critério para funcionário em regime próprio:**  O funcionário será considerado **regime próprio** quando:   * **`PFPERFF.NUMEROBENEFICIO`** = **NULO**, * **e** atender a **pelo menos uma** das condições abaixo:   **1ª condição:**   * **`CODIGOCATEGORIAESOCIAL`** ∈ **{301, 302, 303, 304, 306, 307, 309, 310, 312, 314}**, * **e** **`PFUNC.TPREGIMEPREV`** = **2** ou **NULO**.   **2ª condição:**   * **`CODIGOCATEGORIAESOCIAL`** ∈ **{308, 311, 313}**.   **3ª condição:**   * **`CODIGOCATEGORIAESOCIAL`** = **305**, * **e** o **primeiro dia do período filtrado do relatório** ≥ **01/08/2022**.   **4ª condição:**   * **`CODIGOCATEGORIAESOCIAL`** ∈ **{401, 410}**, * **e** **`PFUNC.TPREGIMEPREV`** = **2**.  ---   **Critério para funcionário com pagamento de benefício:**  Considera-se que o funcionário **possui pagamento de benefício** quando:   * **`PFPERFF.NUMEROBENEFICIO`** ≠ **NULO**. |
| 056112 | IRRF - Empregado/Trabalhador rural - Segurado especial 13° salário | Uma verba será considerada no código de receita 056112 quando todas as condições abaixo forem atendidas: 1. Regra de exclusão A verba **não deve se enquadrar** em nenhum dos seguintes códigos de receita:   * 047301 * 188901 * 056111 * 353301  ---  2. Primeira condição Devem ser atendidos **simultaneamente** os seguintes critérios:   * A chapa do funcionário **não** deve estar contida na tabela `PFDADOSRESIDEXTERIOR` (não residente no exterior); * `PESOCIALEMPREGADOR.CLASSTRIB` **igual a 22**; * **Tipo de rendimento igual a 12**.  Para o Tipo de Rendimento ser **12**:  * `codIncIRRF` deve ser **52**; **e** * `PEVENTO.CODIGOCALCULO` **diferente** de **214** e **395**.  ---  3. Segunda condição Deve ser atendida **uma** das opções abaixo:   * `PFUNC.CODCATEGORIAESOCIAL` **igual a** (101, 102, 103, 105, 106, 107, 108, 111); **ou** * A chapa do funcionário **não conter eventos de 13º salário**.  ---  4. Terceira condição  * `PEVENTO.CODIGOCALCULO` deve ser **um dos seguintes valores**: **049, 106, 340, 347, 054, 120, 196, 407**. |
| 056113 | IRRF - Empregado/Trabalhador rural - Segurado especial 13° salário rescisório | Uma verba será considerada no código de receita 056113 quando todas as condições abaixo forem atendidas: 1. Regra de exclusão A verba **não deve se enquadrar** em nenhum dos seguintes códigos de receita:   * 047301 * 188901 * 056111 * 353301 * 056112  ---  2. Primeira condição Devem ser atendidos **simultaneamente** os seguintes critérios:   * A chapa do funcionário **não** deve estar contida na tabela `PFDADOSRESIDEXTERIOR` (não residente no exterior); * `PESOCIALEMPREGADOR.CLASSTRIB` **igual a 22**; * **Tipo de rendimento igual a 12**.  Para o Tipo de Rendimento ser **12**:  * `codIncIRRF` deve ser **52**; **e** * `PEVENTO.CODIGOCALCULO` **diferente** de **214** e **395**.  ---  3. Segunda condição Deve ser atendida **uma** das opções abaixo:   * `PFUNC.CODCATEGORIAESOCIAL` **igual a** (101, 102, 103, 105, 106, 107, 108, 111); **ou** * A chapa do funcionário **não conter eventos de 13º salário na rescisão**.  ---  4. Terceira condição  * `PEVENTO.CODIGOCALCULO` deve ser **um dos seguintes valores**: **049, 106, 340, 347, 054, 120, 196, 407**. |
| 058806 | IRRF sobre rendimento do trabalho sem vínculo empregatício | Uma verba será considerada no código de receita 058806 quando todas as condições abaixo forem atendidas: 1. Regra de exclusão A verba **não deve se enquadrar** em nenhum dos seguintes códigos de receita:   * 047301 * 188901 * 056111 * 353301 * 056112 * 056113  2. Condição obrigatória Deve existir **registro correspondente** na tabela:   * `PPAGTOAUTONOMOEXT` |
| 056107 | IRRF mensal, 13° salário e férias sobre trabalho assalariado no país ou ausente no exterior a serviço do país, exceto se contratado por empregador doméstico ou por segurado especial sujeito a recolhimento unificado | Uma verba será considerada no código de receita 056107 quando todas as regras abaixo forem observadas. 1. Regra de exclusão A verba **não deve se enquadrar** em nenhum dos seguintes códigos de receita:   * 047301 * 188901 * 056111 * 353301 * 056112 * 056113 * 058806  ---  2. Regras de enquadramento A verba poderá ser considerada no código **056107** conforme as regras abaixo, **dependendo do valor de `PESOCIALEMPREGADOR.CLASSTRIB`**.   ---  2.1 Quando `PESOCIALEMPREGADOR.CLASSTRIB = 22` Devem ser atendidas **todas** as condições a seguir: 2.1.1 Código de cálculo `PEVENTO.CODIGOCALCULO` deve:   * Estar **entre** (004, 084, 346, 030, 061, 107, 348), **ou** * Estar **entre** (013, 053, 195, 386, 113, 197, 319, 320, 326, 406), **ou** * **Não** estar entre (049, 106, 340, 347, 054, 120, 196, 407).  ---  2.1.2 Tipo de rendimento  * **Tipo de rendimento deve iniciar com 2**; * O funcionário **não deve possuir**:    + evento de **13º salário**, nem   + evento de **13º salário na rescisão**.   Para Tipo de Rendimento iniciar com **2**:   * `codIncIRRF` deve ser **32**; * Caso contrário, `codIncIRRF` deve obedecer à correspondência abaixo:    + **Tipo Rendimento 21** → `codIncIRRF` = 46, 47 ou 48   + **Tipo Rendimento 22** → `codIncIRRF` = 61, 62 ou 66   + **Tipo Rendimento 23** → `codIncIRRF` = 63, 64 ou 65  ---  2.2 Quando `PESOCIALEMPREGADOR.CLASSTRIB ≠ 22` Neste cenário, **todas as condições abaixo devem ser atendidas**.   ---  2.2.1 Primeira condição Deve ser atendida **uma** das opções abaixo:   * `PEVENTO.CODIGOCALCULO` **igual a** (004, 084, 346, 030, 061, 107, 348, 013, 053, 195, 386, 113, 197, 319, 320, 326, 406, 049, 106, 340, 347, 054, 120, 196, 407); **ou** * **Tipo de rendimento iniciar com 2 ou 4**; **ou** * **Tipo de rendimento igual a 0** **e** `PFUNC.CODCATEGORIAESOCIAL` **igual a**: (101, 102, 103, 105, 106, 107, 108, 111, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 401, 410, 501, 721, 722, 723, 761, 901, 902, 903, 904, 906).   Para Tipo de Rendimento iniciar com **4**:   * `codIncIRRF` deve **iniciar com 9**.  ---  2.2.2 Segunda condição  * A chapa do funcionário **não** deve estar contida na tabela `PFDADOSRESIDEXTERIOR` (não residente no exterior).  ---  2.2.3 Terceira condição  * `PFUNC.CODCATEGORIAESOCIAL` **não deve conter** nenhum dos seguintes valores: (201, 202, 701, 711, 712, 731, 734, 738, 741, 751, 761, 771, 781). |
| 356201 | IRRF sobre participação dos trabalhadores em lucros ou resultados - PLR | Uma verba será considerada no código de receita 356201 somente se todas as condições abaixo forem atendidas: 1. Regras de exclusão (obrigatórias) A verba **NÃO** pode se enquadrar em **nenhum** dos códigos de receita abaixo:   * 047301 * 188901 * 056111 * 353301 * 056112 * 056113 * 058806 * 056107      ---  2. Categoria do trabalhador O funcionário deve possuir:   * `PFUNC.CODCATEGORIAESOCIAL` ∈ **(101, 102, 103, 105, 106, 107, 108, 111)**  ---  3. Regras condicionais (mínimo de 1 condição atendida) Além das regras acima, **pelo menos uma** das condições abaixo deve ser verdadeira: 🔹 Condição 1  * `PEVENTO.CODIGOCALCULO = 127`  ---  🔹 Condição 2  * `PFUNC.CODCATEGORIAESOCIAL` **inicia com 1** * `PEVENTO.CODIGOCALCULO` ∈ **(321, 121, 408)** |

2OrientaçõesOrientações

**1 – O que fazer quando houver divergência de valores de verbas entre Folha e Governo?**

Resposta: É importante verificar se a verba em questão possui as mesmas parametrizações na folha de pagamento e no eSocial.

Exemplo:  
A verba XXXX pode estar com a opção “Força codIncIRRF eSocial” marcada e com o valor “09” no sistema. Entretanto, no retorno do governo, o codIncIRRF pode estar como “14”.

Nessa situação, para correção do relatório, é necessário desmarcar a opção “Força codIncIRRF eSocial” e gerar o relatório novamente.

**2 – O que fazer quando a coluna “Total IRRF da Folha” não está sendo alimentada, enquanto o retorno do governo está correto?**

**Resposta:** Quando a coluna “Total IRRF da Folha” não é alimentada, uma possível causa está relacionada à parametrização da tabela de verbas (PEVENTO), menu Administração de Pessoal | Eventos | Eventos.

Para realizar a conferência e o ajuste, siga as orientações abaixo:

1. Verifique no menu Administração de Pessoal | Eventos | Eventos se o campo "Incidência(s) suspensa(s) em decorrência de decisão judicial" (PEVENTO.INCIRRFSUSPENSAO) está preenchida com o valor “0”.
2. Ajuste os eventos que estejam com valor incorreto, informando um valor válido conforme a regra do produto.
3. Após a correção, gere novamente o relatório para validar se o Total IRRF da Folha passou a ser apresentado corretamente.

**3 – Estou com divergência no campo “Isento – Outros” entre o valor apresentado pelo Governo e o da Folha. O valor do Governo está correto e o da Folha não. O que devo conferir?**

**Resposta:** Nesse cenário, é necessário conferir os códigos de receita associados aos valores isentos, especialmente aqueles cujo código se inicia com o dígito 7. Esses códigos impactam diretamente a composição do campo “Isento – Outros” e podem gerar divergências entre os valores da Folha e os apurados pelo Governo.

**4 – Como ajustar o Abono Pecuniário de Férias quando o valor está sendo considerado no campo “Isento – Outros”, gerando divergência entre o valor apresentado pelo Governo e o da Folha?  
*Considerar o valor somente no campo Abono de Férias.*  
Resposta:**Para que o Abono Pecuniário de Férias seja considerado corretamente apenas no campo Abono de Férias, siga os passos abaixo:

1. Acesse o menu: Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais (6/7).
2. No campo **“Evento Abono de Férias Envelope”**, informe um evento com o **código de cálculo 39**.

   > Caso necessário, crie um evento do tipo **provento**, sem incidências, utilizando o código de cálculo **39**.
3. Após realizar o ajuste, envie o evento **S-1010** ao eSocial com **data de início de validade retroativa a 01/01/2025**.
4. Após o envio do **S-1010**, remova o código de cálculo **39** do evento informado no parametrizador.
5. Na sequência:
   * Exclua o evento **S-1210**;
   * Realize a **retificação do evento S-1200**;
   * Reenvie o **S-1210** para as competências em que ocorreram as inconsistências.

**5 – O evento de 1ª parcela de 13º salário /  Adiantamento Salarial estão sendo demonstrados como “Isentos – Outros”, porém entendo que eles não deveriam constar no Relatório de Conferência de IRRF (S-5002).**

**Resposta:**  
É necessário verificar a configuração de incidência de IRRF no cadastro do evento/verba.

Acesse o menu Administração de Pessoal | Eventos | Eventos e valide o preenchimento dos campos:

Se o campo **“Isento de IRRF”** estiver configurado com o código **“79 - Outras isenções (o nome da rubrica deve ser claro para identificação da natureza dos valores)”**, será necessário:

* + Desmarcar o campo **“Isento de IRRF”**;
  + Marcar o parâmetro **“Forçar codIncIRRF eSocial”**;
  + Selecionar o código **“09 - Outras verbas não consideradas como base de cálculo ou rendimento”**.

Após realizar o ajuste, envie o evento S-1010 com competência retroativa a janeiro/2025.

Após o ajuste, o evento deixará de ser considerado como rendimento isento e não deverá compor o relatório como “Isentos – Outros”.

**Atenção:** O mesmo ajuste deverá ser realizado para o evento informado no menu: Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais (7/7), no campo **“Evento Antecipação Primeira Parcela 13º nas Férias (Provento)”**.

**6 – Esta ocorrendo divergência no relatório quando possui verba Licença Remunerada no envelope do funcionário. O que devo fazer?**

**Resposta:**Provavelmente a verba **Licença Remunerada** está com o campo **PFFINANC.VERBAFERIAS** igual a **1**, quando o correto seria **0**.

O relatório utiliza a flag **VERBAFERIAS** para identificar as verbas que devem ser desconsideradas da Ficha Financeira, por se tratarem de férias, uma vez que essas informações já são demonstradas no recibo. Ou seja, quando o campo está com valor **1**, a verba não é considerada no relatório. Por esse motivo, pode estar ocorrendo a divergência apontada.

Essa situação indica uma possível inconsistência na base de dados atual.

Como o campo **PFFINANC.VERBAFERIAS** não é editável pela interface do sistema, orientamos realizar o seguinte procedimento:

* Exportar a Ficha Financeira utilizando o leiaute disponível no sistema: **9.004.004 – Exportação da Ficha Financeira.RRM**;
* Ajustar, no arquivo exportado, o campo **PFFINANC.VERBAFERIAS** colocando **0,** conforme a regra correta para as verbas de férias;
* Importar novamente a Ficha Financeira com a informação corrigida.

Após o ajuste, recomenda-se realizar nova conferência para validar se a divergência foi sanada.

**7 – Está ocorrendo divergência no relatório no campo "Valor Titular" no grupo "Plano de Saúde". O que devo fazer?**

**Resposta:**  
Uma possível causa para essa divergência é a duplicidade no cadastro de dependentes, ou seja, a existência de mais de um registro utilizando o mesmo CPF, vinculados ao histórico de assistência médica.

Para verificação, acesse o menu Administração de Pessoal | Cadastros | Funcionários | Dependentes e valide se há dependentes cadastrados com o mesmo CPF.

Caso identificado, recomendamos ajustar o cadastro para eliminar a duplicidade, garantindo a correta apuração dos valores no relatório.

**8 - O valor de 1/3 de Abono deve aparecer no campo “Abono Pecuniário”?**

**Resposta:** Não. O evento **“1/3 de Abono Férias”** possui incidência de **IRRF** e, por isso, é classificado como **rendimento tributável de férias** (*codIncIRRF 13*).

Dessa forma, o valor **não será exibido no campo “Abono Pecuniário”** do relatório — que apresenta apenas valores com *codIncIRRF 75* — sendo demonstrado no campo **“Rendimento Tributável”**.

**9 - Por que o valor de 1/3 de Abono está duplicado no campo “Rendimento Tributável”?**

**Resposta:** A duplicidade ocorre, geralmente, quando o evento **CC381 – Base de IRRF Férias Envelope** não está sendo considerado corretamente no envio ao eSocial.

Esse evento tem a função de estornar os valores que incidem em IRRF sobre férias no envelope de pagamento, evitando que haja duplicidade na composição do rendimento tributável.

Uma possível causa, seria o evento **CC381** não está sendo levado no XML do evento **S-1200**, o que impede o estorno correto dos valores.

Verifique os seguintes pontos:

* Se o evento **CC381** foi incluído no parametrizador como **“Eventos a Desconsiderar”**  
  → Caso esteja, é necessário removê-lo dessa configuração;
* Caso a coligada utilize Tomador de Serviços:
  + Verificar se o evento está com o parâmetro **“Segue rateio de tomador”** marcado;
  + Confirmar se adistribuição de tomador foi realizada corretamente para essa verba.

**10 - Por que o valor de adiantamento salarial está sendo apresentado indevidamente no campo “Rendimento Tributável”?**

**Resposta:** Esse comportamento ocorre quando o evento de adiantamento (código de cálculo **19 – Desconto**) está configurado como **“Dedutível IRRF”** na pasta *“Inc.Descontos”*.

Quando marcado dessa forma, o sistema passa a considerar o valor no cálculo do Rendimento Tributável, resultando em um valor maior do que o esperado.

Para corrigir o comportamento:

* Acessar a configuração do evento (**CC19 – Desconto**);
* Na pasta *“Inc.Descontos”*, alterar a parametrização de: **“Dedutível IRRF”** para **“Estorna IRRF”**.

Com essa configuração:

* O evento de **pagamento do adiantamento salarial** (realizado em caixa diferente da folha) continuará com incidência de IRRF;
* O evento de desconto (**CC19**) passará a **estornar corretamente o valor**, evitando que ele seja considerado indevidamente no campo **“Rendimento Tributável”**.

**11 - Por que o campo *“Rendimento Tributável”* está apresentando valor a maior no governo devido ao evento de Pensão Alimentícia de Férias?**

**Resposta:** Esse comportamento ocorre quando o evento de **pensão alimentícia de férias** está configurado com a flag **“Estorna IRRF”** ou **“Estorna IRRF de Férias”**.

Nessa situação, o evento passa a compor o cálculo do **Código de Cálculo 381 – Base de IRRF Férias (Envelope)**, reduzindo indevidamente a base de IRRF das férias no envelope de pagamento. Como consequência, ocorre divergência e o valor enviado ao governo fica maior do que o esperado no campo *“Rendimento Tributável”*.

Para corrigir o problema:

* Acessar o cadastro do evento de pensão alimentícia de férias;
* Alterar a parametrização de: **“Estorna IRRF” / “Estorna IRRF de Férias”** para **“Dedutível IRRF de Férias”**;
* Ajustar manualmente o valor do **Código de Cálculo 381 – Base de IRRF Férias (Envelope)**;
* Realizar o reprocessamento dos eventos no eSocial:
  + Excluir o evento **S-1210** por meio do **S-3000**;
  + Retificar o evento **S-1200**;
  + Enviar novamente o evento **S-1210**.

Com essa configuração:

* A pensão alimentícia será tratada corretamente como **dedução**;
* A base de IRRF de férias será apurada de forma adequada;
* O valor apresentado no campo **“Rendimento Tributável”** ficará consistente com o esperado pelo eSocial.
* [Código de Cálculo 381 - Base de IRRF Férias Envelope](https://tdn.totvs.com/pages/releaseview.action?pageId=452719713)

**12 - Por que os campos "Previdência Oficial" e/ou "Previdência Oficial 13º" estão sendo apresentados com valor zerado na Folha?**

**Resposta:** Esse comportamento ocorre quando os eventos de INSS (Folha, Férias e 13º), inclusive os eventos de diferença, estão configurados com o parâmetro **"Dedutível IRRF"** marcado na aba **"Inc. Descontos"**.

Com essa configuração, o sistema gera a tag **codIncIRRF** de forma incorreta, fazendo com que os valores desses eventos não sejam considerados na composição dos campos **"Previdência Oficial"** e **"Previdência Oficial 13º"**.

Para corrigir, é necessário desmarcar o parâmetro **"Dedutível IRRF"** desses eventos, garantindo assim a correta apuração dos valores na Folha.

**13 -  Por que os campos "Previdência Oficial" e/ou "Previdência Oficial 13º" estão sendo apresentados com valor zerado para o Governo?**

**Resposta:** Esse cenário geralmente ocorre devido à configuração incorreta das tags ***codIncIRRF***, o que impacta a correta apuração dos valores enviados ao Governo.

Para orientar a correção, consulte o documento: [Divergência de Previdência Oficial do Relatório de Conferência IRRF S-5002](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37856390101783)

**14 - Por que o campo "Valor da Dedução Mensal" está sendo apresentado zerado na Folha?**

**Resposta:** Esse comportamento pode ocorrer quando não há informações preenchidas corretamente para os dependentes do funcionário.

Para validação, acesse o caminho: Administração de Pessoal | Funcionários | Anexo: Folha de Pagamento | Dependentes.

Ao editar o dependente, verifique o anexo **"Valor Dedução do Rendimento Tributável"** e confirme se o campo **"Valor"** está devidamente preenchido conforme oano caixa e mês caixa correspondente.

Além disso, é importante garantir que o ambiente esteja atualizado com o patch mais recente da release, pois já foram realizados ajustes de não conformidade relacionados a esse item.

Para mais detalhes, consulte o material: [Middleware - Relatório de Conferência IRRF S-5002 - MAPEAMENTO e ORIENTAÇÕES](https://tdn.totvs.com/pages/releaseview.action?pageId=1040994699) (aba **"Mapeamento | Dedução de Dependente"**).

**15 - Como é realizada a tratativa de autônomos no Relatório de Conferência IRRF S-5002?**

**Resposta:** O relatório contempla a tratativa dos autônomos Externos, Internos e da Folha de Pagamento, permitindo a correta conciliação entre as bases de cálculo e os valores de IRRF registrados no sistema TOTVS Folha de Pagamento e as informações apuradas pelo Governo por meio do evento S-5002 do eSocial.

Essa tratativa garante maior assertividade na conferência dos dados complementares de IRRF, possibilitando identificar e ajustar eventuais divergências entre o sistema e o retorno governamental.

Para mais detalhes sobre regras, validações e orientações, consulte o documento: [DT - Relatório de Conferência IRRF S-5002 - Tratativa para Autônomos](https://tdn.totvs.com/pages/releaseview.action?pageId=1046422261)

## **03. DEMAIS INFORMAÇÕES**

* [Middleware - Relatório de Conferência IRRF S-5002](https://tdn.totvs.com/pages/viewpage.action?pageId=1028947938)
* [Webinar DIRF Mensal - FAQ](https://tdn.totvs.com/display/LRM/Webinar+DIRF+Mensal+-+FAQ)
