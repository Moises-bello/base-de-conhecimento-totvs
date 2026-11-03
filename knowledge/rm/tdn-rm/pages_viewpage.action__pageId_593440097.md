---
content_hash: 3ae39233581a87479269ef9b19956f50acb1b7d4ce13fecbb1568d3d7f0075f1
fetched_at: '2026-06-29T00:10:56.914341+00:00'
page_id: '593440097'
product: rm
source: tdn-rm
title: Alterações S-2300
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593440097
version: 10
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2300 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {trabalhador}: Campo {nisTrab} excluído. |  |  |
| Grupos {nascimento}: Campos{codMunic}, {uf}, {paisNascto}, {nmMae }, {nmPai} excluído. |  |  |
| Grupos {documentos}: Excluido |  |  |
| Grupos {CTPS}: Campo {nrCtps},{serieCtps }, {ufCtps}, excluído. |  |  |
| Grupos {RIC}: Campo {nrRic},{orgaoEmissor }, {dtExped}, excluído. |  |  |
| Grupos {RG}: Campo {nrRg},{orgaoEmissor }, {dtExped}, excluído. |  |  |
| Grupos {RNE}: Campo {nrRne},{orgaoEmissor }, {dtExped} excluído. |  |  |
| Grupos {OC}: Campo {nrOc},{orgaoEmissor }, {dtExped},{dtValid} excluído. |  |  |
| Grupos {CNH}: Campo {nrRegCnh},{dtExped}, {ufCnh},{dtValid}, {dtPriHab}, {categoriaCnh} excluído. |  |  |
| Grupos {trabImig}: Grupo adicionado |  | OC (se paisNac for diferente de [105]); N (nos demais casos) |
| Grupos {trabImig}: Campo {tmpResid} adicionado. |  | Tempo de residência do trabalhador imigrante. Valores válidos: 1 - Prazo indeterminado 2 - Prazo determinado Validação: Preenchimento obrigatório quando houver trabalhador com (dtAdm ou dtExercicio ou dtInicio) no Registro de Eventos Trabalhistas - RET >= [2021-05-10]. |
| Grupos {trabImig}: Campo {condIng} adicionado. |  | Condição de ingresso do trabalhador imigrante. Valores válidos: 1 - Refugiado 2 - Solicitante de refúgio 3 - Permanência no Brasil em razão de reunião familiar 4 - Beneficiado pelo acordo entre países do Mercosul 5 - Dependente de agente diplomático e/ou consular de países que mantêm acordo de reciprocidade para o exercício de atividade remunerada no Brasil 6 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre a República Federativa do Brasil e a República Portuguesa 7 - Outra condição Validação: Se tmpResid = [1], não pode ser informado [2, 5]. Se tmpResid = [2], não pode ser informado [1]. |
| Grupos {trabEstrangeiro}: Campo {dtChegada},{classTrabEstrang}, {casadoBr}, {filhosBr} excluído. |  |  |
| Grupos {contato}: Campo {foneAlternat},{emailAlternat} excluído. |  |  |
| Grupos {infoTSVInicio}: Campo {matricula} adicionado. |  | Matrícula atribuída ao trabalhador pela empresa. Validação: Preenchimento obrigatório se indRetif = [1]. No caso de retificação (indRetif = [2]), a matrícula deve ser preenchida caso tenha sido informada no evento original. O valor informado não pode conter a expressão 'eSocial' nas 7 (sete) primeiras posições. Regra de validação: REGRA\_CARACTERE\_ESPECIAL |
| Grupos {infoTSVInicio}: Campo {dtInicio} condição alterada. | Data de início, que pode ser: a) Para o Cooperado, a data de ingresso na cooperativa; b) Para o Diretor Não Empregado, a data de posse no cargo; c) Para o Dirigente Sindical, a data de início do mandato no sindicato; d) Para o Estagiário, a data de início do estágio; e) Para o trabalhador avulso, a data de ingresso no ogmo ou no Sindicato; f) Para os demais trabalhadores, a data de início das atividades no empregador. Validação: Devem ser observadas as seguintes regras: a) Deve ser posterior à data de nascimento do trabalhador;. b) Se {cadIni} = [S], deve ser anterior à data de início da obrigatoriedade dos eventos não periódicos para o empregador no eSocial; c) Se {cadIni} = [N], deve ser igual ou posterior à data de início da obrigatoriedade dos eventos não periódicos para o empregador no eSocial. | Data de início, que pode ser: a) Para o cooperado, a data de ingresso na cooperativa; b) Para o diretor não empregado, a data de posse no cargo; c) Para o dirigente sindical, a data de início do mandato no sindicato; d) Para o estagiário, a data de início do estágio; e) Para o trabalhador avulso, a data de ingresso no Órgão Gestor de Mão de Obra - OGMO ou no sindicato; f) Para o servidor público exercente de cargo eletivo, a data de início do mandato; g) Para os demais trabalhadores, a data de início das atividades. Validação: Devem ser observadas as seguintes regras: a) Deve ser posterior à data de nascimento do trabalhador e não pode ser posterior a 30 (trinta) dias da data atual; b) Se cadIni = [S], deve ser anterior à data de início da obrigatoriedade dos eventos não periódicos para o empregador no eSocial; c) Se cadIni = [N], deve ser igual ou posterior à data de início da obrigatoriedade dos eventos não periódicos para o empregador no eSocial. |
| Grupos {infoTSVInicio}: Campo {nrProcTrab} adicionado. |  | Ocorrencia: 0 - 1  Tamanho: 20  Número que identifica o processo trabalhista,  quando o início de TSVE se der por decisão judicial.  Validação:  Se preenchido, deve ser um processo  judicial válido, com 20 (vinte) algarismos. |
| Grupos {infoTSVInicio}: Campo {natAtividade} condição alterada. | Natureza da atividade, conforme opções abaixo: 1 - Trabalho Urbano; 2 - Trabalho Rural. Validação: Preenchimento obrigatório para as categorias de avulso, cooperado e dirigente sindical. Não deve ser preenchido para as categorias Diretor não empregado, servidor público indicado a conselho, membro de conselho tutelar e estagiário. Valores Válidos: 1,2. | Natureza da atividade. Valores válidos: 1 - Trabalho urbano 2 - Trabalho rural Validação: Preenchimento obrigatório se codCateg = [201, 202, 401, 731, 734, 738]. Não deve ser preenchido se codCateg = [721, 722, 771, 901]. |
| Grupos {cargoFuncao}:  condição alterada. | OC (Se {codCateg} = [901, 903, 904, 905]); O (Nas demais situações) | OC (se o código de categoria no RET for igual a [901, 903, 904]); O (nos demais casos) |
| Grupos {cargoFuncao}: Campos {codFuncao},{codCargo} excluído. |  |  |
| Grupos {cargoFuncao}: Campo {nmCargo} adicionado. |  | Informar o nome do cargo. Validação: Preenchimento obrigatório se o código de categoria no RET for diferente de [410]. |
| Grupos {cargoFuncao}: Campo {nmFuncao} adicionado. |  | Informar o nome da função de confiança. Validação: Preenchimento obrigatório se o código de categoria no RET for igual a [410] e não houver informação de nmCargo. |
| Grupos {cargoFuncao}: Campo {CBOCargo} adicionado. |  | Ocorrencia: 0 - 1  Tamanho: 6  Informar a Classificação Brasileira de  Ocupações CBO relativa ao cargo.  Validação:  Informação obrigatória e exclusiva  se nmCargo for preenchido.  Se informado, deve ser um código  válido e existente na tabela de CBO,  com 6 (seis) posições. |
| Grupos {cargoFuncao}: Campo {CBOFuncao} adicionado. |  | Ocorrencia: 0 - 1  Tamanho: 6  Informar a CBO relativa à função de confiança/cargo  em comissão. Validação: Informação obrigatória  e exclusiva se nmFuncao for preenchido.  Se informado, deve ser um código válido  e existente na tabela de CBO,  com 6 (seis) posições. |
| Grupos {renumeracao}:  condição alterada. | O (se categoria igual a diretor não empregado, servidor público indicado a conselho ou membro de Conselho Tutelar) OC (nas demais situações). | O (se codCateg = [721, 722, 771]); OC (nos demais casos) |
| Grupos {fgts}: Campos {opcFGTS} excluído. |  |  |
| Grupos {FGTS}: Grupo adicionado. |  | O (se codCateg = [721]); N (nos demais casos) |
| Grupos {FGTS}: Campo {dtOpcFGTS} adicionado e alterado ocorrência. | Ocorrência de 0-1 | Ocorrência 1 |
| Grupos {infoDirigenteSindical}: Campo {tpInsc} adicionado. |  | Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05. Valores válidos: 1 - CNPJ 2 - CPF Validação: O preenchimento é obrigatório e exclusivo se infoDirigenteSindical/categOrig corresponder a "Empregado", "Agente Público", "Avulso" ou for igual a [721]. |
| Grupos {infoDirigenteSindical}: Campo {cnpjOrigem} Excluído. |  |  |
| Grupos {infoDirigenteSindical}: Campo {dtAdmOrig} alterada validação e descrição. | Preencher com a data de admissão ou data de início do dirigente sindical na empresa de origem. Validação: O preenchimento é obrigatório se a categoria de origem do trabalhador corresponder a "empregado" ou "avulso". | Preencher com a data de admissão (ou de início) do dirigente sindical na empresa de origem. Validação: O preenchimento é obrigatório se infoDirigenteSindical/categOrig corresponder a "Empregado", "Agente Público", "Avulso" ou for igual a [721]. |
| Grupos {infoDirigenteSindical}: Campo {matricOrig} alterada validação e descrição. | Preencher com a matrícula do trabalhador na empresa de origem. Validação: Preenchimento obrigatório se a categoria de origem do trabalhador corresponder a "empregado". | Preencher com a matrícula do trabalhador na empresa de origem. Validação: Preenchimento obrigatório se infoDirigenteSindical/categOrig corresponder a "Empregado" ou "Agente Público". |
| Grupos {infoDirigenteSindical}: Campo {tpRegTrab} adicionado. |  | Tipo de regime trabalhista. Valores válidos: 1 - CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas 2 - Estatutário/legislações específicas (servidor temporário, militar, agente político, etc.)  Validação: O preenchimento é obrigatório e exclusivo se infoDirigenteSindical/categOrig corresponder a "Empregado" ou "Agente Público". |
| Grupos {infoDirigenteSindical}: Campo {tpRegPrev} adicionado. |  | Tipo de regime previdenciário (ou Sistema de Proteção Social dos Militares). Valores válidos: 1 - Regime Geral de Previdência Social - RGPS 2 - Regime Próprio de Previdência Social - RPPS ou Sistema de Proteção Social dos Militares 3 - Regime de Previdência Social no exterior Validação: Se infoDirigenteSindical/categOrig for relativa a "Empregado", não pode ser preenchido com [2]. |
| Grupos {infoTrabCedido}:  condição alterada. | O (se categoria do trabalhador = trabalhador cedido) N (nas demais situações) | O (se codCateg = [410]); N (nos demais casos) |
| Grupos {infoTrabCedido}: Campo {tpRegTrab} alterada descrição. | 2 - Estatutário. | 2 - Estatutário/legislações específicas (servidor temporário, militar, agente político, etc.) |
| Grupos {infoTrabCedido}: Campo {tpRegPrev} alterada descrição e validação. | Tipo de regime previdenciário conforme opções abaixo: 1 - Regime Geral da Previdência Social - RGPS; 2 - Regime Próprio de Previdência Social - RPPS; 3 - Regime de Previdência Social no Exterior. Validação: Se {categOrig} for relativa a Empregado, não pode ser preenchido  com [2]. Valores Válidos: 1, 2, 3. | Tipo de regime trabalhista. Valores válidos: 1 - CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas 2 - Estatutário/legislações específicas (servidor temporário, militar, agente político, etc.)  Validação: O preenchimento é obrigatório e exclusivo se infoDirigenteSindical/categOrig corresponder a "Empregado" ou "Agente Público". |
| Grupos {infoTrabCedido}: Campo {infOnus} excluído. |  |  |
| Grupos {infoEstagiario}: Campo {areaAtuacao} alterado tamanho. | 50 | 1-100 |
| Grupos {instEnsino}: Campo {nmRazao} incluída validação e alterada ocorrência. | Informar a razão social.  1-1 | Informar a razão social. Validação: Preenchimento obrigatório e exclusivo se o campo cnpjInstEnsino não estiver preenchido.  0-1 |
| Grupos {instEnsino}: Campo {dscLograd} incluída validação. | Descrição do logradouro. | Descrição do logradouro.  Validação: Preenchimento obrigatório e exclusivo se o campo cnpjInstEnsino não estiver preenchido. |
| Grupos {instEnsino}: Campo {nrLograd} alterada descrição e incluída validação. | Número do logradouro. Se não houver número a ser informado, preencher com "S/N". | Número do logradouro. Se não houver número a ser informado, preencher com "S/N". Validação: Preenchimento obrigatório e exclusivo se o campo cnpjInstEnsino não estiver preenchido. |
| Grupos {instEnsino}: Campo {bairro} incluída validação. | Nome do bairro/distrito | Nome do bairro/distrito. Validação: Preenchimento obrigatório e exclusivo se o campo cnpjInstEnsino não estiver preenchido. |
| Grupos {instEnsino}: Campo {cep} alterada validação. | Código de Endereçamento Postal - CEP. Validação: Deve ser preenchido apenas com números. Deve ser um CEP válido. | Código de Endereçamento Postal - CEP. Validação: Não informar se o campo cnpjInstEnsino estiver preenchido. Se informado, deve ser preenchido apenas com números, com 8 (oito) posições. |
| Grupos {instEnsino}: Campo {codMunic} alterada validação. | Preencher com o código do município, conforme tabela do IBGE. Validação: Se informado, deve ser um código existente na tabela do IBGE. | Preencher com o código do município, conforme tabela do IBGE. Validação: Não informar se o campo cnpjInstEnsino estiver preenchido. Se informado, deve ser um código válido e existente na tabela do IBGE. |
| Grupos {instEnsino}: Campo {uf} alterada validação. | Preencher com a sigla da Unidade da Federação. Validação: Deve ser uma UF válida. | Preencher com a sigla da Unidade da Federação - UF. Valores válidos: AC, AL, AP, AM, BA, CE, DF, ES, GO, MA, MT, MS, MG, PA, PB, PR, PE, PI, RJ, RN, RS, RO, RR, SC, SP, SE, TO Validação: Não informar se o campo cnpjInstEnsino estiver preenchido |
| Grupos {ageIntegracao}: Campos {nmRazao}, {dscLograd}, {nrLograd}, {bairro},{cep},{codMunic},{uf} excluídos. |  |  |
| Grupos {supervisorEstagio}: Campo {nmSuperv} excluído. |  |  |
| Grupos {mudancaCPF}: Campo {matricAnt} adicionado. |  | Preencher com a matrícula anterior do trabalhador. |

Criação de campos no cadastro do funcionário.

Acesse**RH | Folha de Pagamento | Administração de Pessoal | Funcionários**

Criado os campos Tipo de regime trabalhista e tipo de regime previdenciário (ou sistema de proteção social dos militares).  Para atender ao preenchimento das tag’s <tpRegTrab> e <tpRegPrev> do grupo <infoDiregenteSindical> que se refere a informações relativas ao dirigente sindical.
