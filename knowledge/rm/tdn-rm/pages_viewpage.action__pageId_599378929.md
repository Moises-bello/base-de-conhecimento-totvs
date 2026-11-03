---
content_hash: f9e011cf3adcc1d76adba337fd170b47f62cb1a123735ede6b713b5d6f40350d
fetched_at: '2026-06-29T00:10:57.776287+00:00'
page_id: '599378929'
product: rm
source: tdn-rm
title: Alterações S-2200
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=599378929
version: 25
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2200 para o leiaute do eSocial Versão S-1.0.

---

| **GRUPO/CAMPO/ITEM** | **DE** | **PARA** |
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
| Grupos {endereco}  Alterada ocorrência e condição | Ocorrência :1-1 Condição: O | Ocorrência: 0-1  Condição: O (se grupo desligamento não estiver preenchido); F (nos demais casos) |
| Grupos {trabImig}: Grupo adicionado |  | OC (se paisNac for diferente de [105]); N (nos demais casos) |
| Grupos {trabImig}: Campo {tmpResid} adicionado. |  | Tempo de residência do trabalhador imigrante. Valores válidos: 1 - Prazo indeterminado 2 - Prazo determinado Validação: Preenchimento obrigatório quando houver trabalhador com (dtAdm ou dtExercicio ou dtInicio) no Registro de Eventos Trabalhistas - RET >= [2021-05-10]. |
| Grupos {trabImig}: Campo {condIng} adicionado. |  | Condição de ingresso do trabalhador imigrante. Valores válidos: 1 - Refugiado 2 - Solicitante de refúgio 3 - Permanência no Brasil em razão de reunião familiar 4 - Beneficiado pelo acordo entre países do Mercosul 5 - Dependente de agente diplomático e/ou consular de países que mantêm acordo de reciprocidade para o exercício de atividade remunerada no Brasil 6 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre a República Federativa do Brasil e a República Portuguesa 7 - Outra condição Validação: Se tmpResid = [1], não pode ser informado [2, 5]. Se tmpResid = [2], não pode ser informado [1]. |
| Grupos {contato}: Campo {foneAlternat},{emailAlternat} excluído. |  |  |
| Grupos {exterior}-alteradas condição e descrição no registro do evento | DE: O (se não informado o grupo {brasil}) N (nos demais casos) | PARA: O (se não informados os grupos brasil e desligamento);  N (se grupo brasil estiver preenchido);  F (nos demais casos) |
| Grupos {exterior}:Campo{nmCid}- Alterado  Tamanho | Tamanho: 50 | Tamanho: 2-50 |
| Grupos {exterior}:Campo{codPostal}-Alterado  Tamanho | Tamanho: 12 | Tamanho:4-12 |
| Grupos {trabEstrangeiro}:Excluído o grupo {trabEstrangeiro} e respectivos campos  Campos excluídos: dtChegada, classTrabEstrang, casadoBr e filhosBr |  |  |
| Grupos {infoDeficiencia}: alterada condição | condição:OC | Condição:OC (se grupo desligamento não estiver preenchido);  F (nos demais casos) |
| Grupos {infoDeficiencia}: Campo{infoCota}-alterada ocorrência e incluída validação | Ocorrência: 1-1   Informar se o trabalhador preenche cota de pessoas com deficiência habilitadas ou de beneficiários reabilitados | Ocorrência: 0-1    Informar se o trabalhador preenche cota de pessoas com deficiência habilitadas ou de beneficiários reabilitados. Preenchimento obrigatório e exclusivo se tpRegTrab = [1]. |
| Grupos {dependente}: Campo{NmDep} Alterado tamanho | Tamanho: 70 PARA: 2-70 | Tamanho:2-70 |
| Grupos {dependente}: Campo{dtNascto} Alterado validação | Deve ser maior ou igual que 01/01/1890 e menor que a data atual. | Deve ser maior ou igual que 01/01/1890 e menor ou igual à data atual. |
| Grupos {dependente}: Campo{sexoDep}   Criado o campo sexo do dependente |  | Valores válidos: M - Masculino F - Feminino Validação: Preenchimento obrigatório se tpRegPrev = [2] e cadIni = [N]. Não informar se tpRegPrev for diferente de [2] |
| Grupos {aposentadoria}  Excluído o grupo {aposentadoria} e respectivo campo.  Campo excluído: trabAposent |  |  |
| Grupos {Vinculo}: campo{tpRegTrab}  – alterada descrição do valor [2] | Tipo de regime trabalhista  1 - CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas;  2 - Estatutário. | Tipo de regime trabalhista  1 - CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas  2 - Estatutário/legislações específicas (servidor temporário, militar, agente político, etc.) |
| Grupos {Vinculo}: campo{tpRegPrev}  – alterada descrição | DE: Tipo de regime previdenciário conforme opções abaixo: 1 - Regime Geral da Previdência Social - RGPS; 2 - Regime Próprio de Previdência Social - RPPS; 3 - Regime de Previdência Social no Exterior. | Tipo de regime previdenciário (ou Sistema de Proteção Social dos Militares) 1 - Regime Geral de Previdência Social - RGPS 2 - Regime Próprio de Previdência Social - RPPS ou Sistema de Proteção Social dos Militares 3 - Regime de Previdência Social no exterior |
| Grupos {Vinculo}: campo{nrRecInfPrelim} - Campo excluido |  |  |
| Grupos {infoCelestista}: campo{nrProcTrab} |  | Criado o campo número que identifica o processo trabalhista, quando a admissão se der por decisão judicial |
| Grupos {FGTS}: campo{FGTS}-alterada condição | Condição: F (se {cadIni} = [N] e {tpAdmissao} = [1, 6]); O (nas demais situações) | Condição: N (se tpAdmissao = [6] OU (se codCateg for diferente de [104] e dtAdm >= [1988-10-05]) OU (se codCateg = [104] e dtAdm >= [2015-10-01])); O (nos demais casos) |
| Grupos {FGTS}: campo{opcFGTS}-excluido |  |  |
| Grupos {FGTS}: campo{dtopcFGTS}-alterada ocorrência e excluida validação | Ocorrência: 0-1 Validação:Preenchimento obrigatório em caso de trabalhador optante pelo FGTS. | Ocorrencia 1:  Sem validação |
| Grupos {trabTemporario}: alterada condição | Condição: O (Se {codCateg} = [106]); N (Nas demais situações) | Condição:N (se codCateg for diferente de [106]); O (se codCateg = [106] e se grupo desligamento não estiver preenchido); F (nos demais casos) |
| Grupos {trabTemporario}:campo{tpInclContr} Campo excluido |  |  |
| Grupos {ideTomadorServ}:campos excluidos {itpInsc},{nrInsc} |  |  |
| Grupos {ideEstabVinc}: campo {nrInsc} alterados tamanho, descrição e validação | Tamanho DE: 15    Informar o número de inscrição do contratante de serviços, de acordo com o tipo de inscrição informado em {tpInsc}.   Validação: Se {tpInsc} for igual a [1], deve ser um CNPJ válido. Se {tpInsc} for igual a [2], deve ser um CPF válido. Se for um CNPJ deve ter a mesma Raiz/Base de oito posições informada em {ideTomadorServ/nrInsc}. | Tamanho:11 ou 14 descrição  Informar o número de inscrição do contratante de serviços, de acordo com o tipo de inscrição informado em ideEstabVinc/tpInsc  Validação:Se ideEstabVinc/tpInsc for igual a [1], deve ser um CNPJ válido, com 14 (catorze) algarismos. Se ideEstabVinc/tpInsc for igual a [2], deve ser um CPF válido. |
| Grupo {aprend} – alterada condição | Condição:OC (se {codCateg} = [103]); N (nas demais situações). | Condição:N (se codCateg for diferente de [103]); OC (se codCateg = [103] e se grupo desligamento não estiver preenchido); F (nos demais casos) |
| Grupo {aprend}: Campo{nrInsc}   alterados tamanho, descrição e validação | Tamanho: 15   Descrição:Informar o número de inscrição do empregador para o qual a contratação de aprendiz foi efetivada, de acordo com o tipo de inscrição indicado no campo {tpInsc}.  Validação: Se {tpInsc} for igual a [1], deve ser um número de CNPJ válido. Se {tpInsc} for igual a [2], deve ser um CPF válido. | Tamanho:11 ou 14  Descrição:Informar o número de inscrição do estabelecimento para o qual a contratação de aprendiz foi efetivada, de acordo com o tipo de inscrição indicado no campo aprend/tpInsc  Validação:Deve ser um identificador válido e: a) Se aprend/tpInsc = [1], deve ser informado com 14 (catorze) algarismos. Se o empregador for pessoa jurídica, a raiz do CNPJ informado deve ser diferente de ideEmpregador/nrInsc. b) Se aprend/tpInsc = [2], deve ser diferente do CPF do empregado. Se o empregador for pessoa física, também deve ser diferente do CPF do empregador. |
| Grupo {infoContrato}: Campo{codFuncao}   Campo excluido |  |  |
| Grupo {infoContrato}: Campo{nmFuncao }   Campo Novo |  | Informar o nome do cargo. Validação: O preenchimento é obrigatório, exceto se for relativo a servidor nomeado em cargo em comissão (tpRegTrab = [2] e tpProv = [2]). |
| Grupo {infoContrato}: Campo{CBOFuncao } |  | Informar a Classificação Brasileira de Ocupações - CBO relativa ao cargo. Validação: Informação obrigatória e exclusiva se nmCargo for preenchido. Se informado, deve ser um código válido e existente na tabela de CBO, com 6 (seis) posições. |
| Grupo {infoContrato}: Campo{codFunção} |  |  |
| Grupo {remuneração}:   Alterada ocorrência e Condição | Ocorrência: 1-1  Condição DE: O | Ocorrencia:0-1  Condição: N (se tpRegTrab = [2]); O (se tpRegTrab = [1] e se grupo desligamento não estiver preenchido); F (nos demais casos) |
| Grupo {remuneracao}: Campo{dscSalVar}  Alterado Tamanho | Tamanho:255 | Tamanho:1-999 |
| Grupo {duracao}  Alteradas ocorrência e condição | Ocorrência: 1-1  Condição: O | Ocorrência:0-1  Condição: N (se tpRegTrab = [2]); O (se tpRegTrab = [1] e se grupo desligamento não estiver preenchido); F (nos demais casos) |
| Grupo {duracao}: Campo{dtTerm}  Alteradas descrição e validação | Descrição: Data do Término. | Descrição:Data do término do contrato por prazo determinado |
| Grupo {localtrabalho}:Alteradas ocorrência e condição | Ocorrência: 1-1  Condição : O | Ocorrência:0-1  Condição: O (se grupo desligamento não estiver preenchido); F (nos demais casos) |
| Grupo {localTrabGeral}: Campo{nrInsc}  Alterados tamanho, descrição e validação | Tamanho: 15   Descrição : Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo {tpInsc}   Validação: A inscrição informada deve ser compatível com {tpInsc} e constar na tabela S-1005 | Tamanho:PARA: 12 ou 14  Descrição: Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo localTrabGeral/tpInsc  Validação:Deve ser um número de inscrição válido e existente na Tabela de Estabelecimentos (S-1005), bem como compatível com localTrabGeral/tpInsc |
| Grupo {localTrabDom}:Excluído o grupo {localTrabDom} e respectivos campos |  | Campos excluídos: tpLograd, dscLograd, nrLograd, complemento, bairro, cep, codMunic e uf |
| Grupo {localTrabDom} Alteração da descrição para {localTempDom} |  |  |
| Grupo {horContratual}- Alteradas condição e descrição no registro do evento | Descrição  Informações do Horário Contratual do Trabalhador. O preenchimento é obrigatório se {tpRegJor} = [1] PARA: Informações do horário contratual do trabalhador Condição DE: O (se {tpRegJor} = [1]); OC (nos demais casos) | O (se tpRegJor = [1] e se grupo desligamento não estiver preenchido); OC (se tpRegJor for diferente de [1] e se grupo desligamento não estiver preenchido); F (nos demais casos) |
| Grupo {horContratual}-Campo{tpJornada}  Incluídos valores [4, 5, 6, 7] e excluído valor [1] | Preencher com uma das opções:  1 - Jornada com horário diário e folga fixos;  2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso);  3 - Jornada com horário diário fixo e folga variável;  9 - Demais tipos de jornada | Valores válidos:  2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso)  3 - Jornada com horário diário fixo e folga variável  4 - Jornada com horário diário fixo e folga fixa (no domingo) 5 - Jornada com horário diário fixo e folga fixa (exceto no domingo)  6 - Jornada com horário diário fixo e folga fixa (em outro dia da semana), com folga adicional periódica no domingo  7 - Turno ininterrupto de revezamento  9 - Demais tipos de jornada |
| Grupo {horContratual}-Campo{dscTpJorn}  Campo {dscTpJorn} – excluído |  |  |
| Grupo {horContratual}-Campo{horNoturno}  Criado o campo {horNoturno} – Indica se a jornada semanal possui horário noturno (no todo ou em parte) |  | Valores válidos:  S - Sim  N - Não |
| Grupo {horContratual}-Campo{dscpJorn}  Criado o campo {dscJorn} – Descrição da jornada semanal contratual |  | Descrição da jornada semanal contratual, contendo os dias da semana e os respectivos horários contratuais (entrada, saída e intervalos) |
| Grupo {horario}  Excluído o grupo {horario}   Campos excluídos: dia e codHorContrat |  |  |
| Grupo {filiacaoSindical}  Excluído o grupo {filiacaoSindical} Campo excluído: cnpjSindTrab |  |  |
| Grupo {alvaraJudicial}   Alterada condição | Condição:OC | Condição:  OC (se grupo desligamento não estiver preenchido); F (nos demais casos) |
| Grupo {observacoes}  Alterada condição | Condição: OC PARA: OC (se grupo desligamento não estiver preenchido); F (nos demais casos) | Condição: OC (se grupo desligamento não estiver preenchido); F (nos demais casos) |
| Grupo {treiCap}  Criado o grupo {treiCap} |  |  |
| Grupo {treiCap}-Campo{codTreicap}  Criado o campo {codTreiCap} – código do treinamento, capacitação, exercício simulado ou outra anotação |  | Validação: Deve ser um código válido e existente na  Tabela 28. |
| Grupo {sucessaoVinc}-alterada condição e descrição | Descrição: Grupo de informações da sucessão de vínculo trabalhista   Condição: O (se {tpAdmissao} for igual [2, 3, 4]); N (nos demais casos) | Descrição: Grupo de informações da sucessão de vínculo trabalhista/estatutário    Condição: O (se tpAdmissao = [2, 3, 4] ou tpProv = [5, 8]); N (nos demais casos) |
| Grupo {sucessaoVinc}-Campo{tpInscAnt}  Campo excluido |  |  |
| Grupo {sucessaoVinc}-Campo{tpInsc}  Criado o campo {tpInsc} – código correspondente ao tipo de inscrição, conforme Tabela 05 |  | Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.  Valores válidos:  1 - CNPJ  2 - CPF  5 - CGC  6 - CEI  Validação: Somente é possível informar [5] se dtTransf for igual ou anterior a [1999-06-30]. Somente é possível informar [6] se dtTransf for igual ou anterior a [2011-12-31]. |
| Grupo {sucessaoVinc}-Campo{nrInsc} |  | Informar o número de inscrição do empregador anterior, de acordo com o tipo de inscrição indicado no campo sucessaoVinc/tpInsc.  Validação: Deve ser um número de inscrição válido e diferente da inscrição do declarante, considerando as particularidades aplicadas à informação de CNPJ de órgão público em S-1000. Se sucessaoVinc/tpInsc = [1], deve possuir 14 (catorze) algarismos e ser diferente do CNPJ base do empregador (exceto se ideEmpregador/nrInsc tiver 14 (catorze) algarismos) e dos estabelecimentos informados através do evento S-1005. Se sucessaoVinc/tpInsc = [2], deve possuir 11 (onze) algarismos. Se sucessaoVinc/tpInsc = [5], deve possuir somente algarismos. Se sucessaoVinc/tpInsc = [6], deve possuir 12 (doze) algarismos. |
| Grupo {mudancaCPF}-Campo{nrInsc}  Alterada condição | Condição: O (se {tpAdmissao} = [6]); N (nos demais casos) | Condição :O (se tpAdmissao = [6] ou tpProv = [10]); N (nos demais casos) |
| Grupo {afastamento}-Campo{dtIniafast} |  | Data de início do afastamento.  Validação: Devem ser observadas as seguintes regras: a) Deve ser igual ou posterior à data de admissão/exercício do trabalhador; b) Se cadIni = [S], deve ser anterior à data de início da obrigatoriedade dos eventos não periódicos para o empregador; c) Se cadIni = [N], deve ser anterior à data da transferência ou alteração do CPF do empregado (sucessaoVinc/dtTransf, transfDom/dtTransf ou dtAltCPF). Não informar se tpAdmissao = [1] ou se tpProv for diferente de [5, 8, 10]. |
| Grupo {afastamento}-Campo{codMotAfast}  Alterada validação |  | Preencher com o código do motivo de afastamento temporário.  Validação: Deve ser um código válido e existente na Tabela 18. Se a natureza jurídica do declarante for Administração Pública (grupo [1]), não pode ser informado [14]. |
| Grupo {desligamento}-alterada a condição | N (se grupo {afastamento} estiver preenchido OU se {tpAdmissao} = [6]); OC (nos demais casos) | N (se (grupo afastamento ou cessao estiver preenchido) ou (se tpAdmissao = [6] ou tpProv = [10])); OC (nos demais casos) |
| Grupo {desligamento}-Campo{dtDeslig}  Alterada validação da alínea c) | c) Se {cadIni} = [N], deve ser anterior à data da transferência do empregado ({sucessaoVinc/dtTransf} ou {transfDom/dtTransf}). Não informar se {tpAdmissao} = [1] | c) Se cadIni = [N], deve ser anterior à data da transferência do empregado (sucessaoVinc/dtTransf ou transfDom/dtTransf).  Não informar se tpAdmissao = [1] ou se tpProv for diferente de [5, 8] |
| Grupo {desligamento}-Campo{dtDeslig} |  |  |
| Grupo {cessao} -Campo{dtIniCessao}  Criado o campo {dtIniCessao} – Data de início da cessão/exercício em outro órgão | . | Data de início da cessão/exercício em outro órgão. Validação: Devem ser observadas as seguintes regras:  a) Deve ser igual ou posterior à data de admissão/exercício do trabalhador;   b) Se cadIni = [S], deve ser anterior à data de início da obrigatoriedade dos eventos não periódicos para o ente público e a natureza jurídica do declarante deve ser Administração Pública (grupo [1]);  c) Se cadIni = [N], deve ser anterior à data da transferência ou alteração do CPF do empregado (sucessaoVinc/dtTransf ou dtAltCPF) e igual ou posterior a [2021-05-10]. Não informar se tpAdmissao = [1] ou se tpProv for diferente de [5, 8, 10]. |

**Observação:**

Foi criado um De/Para no campo "Classificação da condição no Brasil" Tag (condIng) para que fosse possível obter as informações nas duas versões do leiaute, sem que o usuario precisasse fazer alterações.

**Tabela com DE/PARA**

|  |  |
| --- | --- |
| 1 - Visto permanente 2 - Visto temporário 3 - Asilado 6 - Residente fora do Brasil 7 - Deficiente físico e com mais de 51 anos 8 - Com residência provisória e anistiado, em situação irregular | 7 - Outra condição |
| 4 - Refugiado | 1 - Refugiado |
| 5 - Solicitante de Refúgio | 2 - Solicitante de refúgio |
| 9 - Permanência no Brasil em razão de filhos ou cônjuge brasileiros | 3 - Permanência no Brasil em razão de reunião familiar |
| 10 - Beneficiado pelo acordo entre países do Mercosul | 4 - Beneficiado pelo acordo entre países do Mercosul |
| 11 - Dependente de agente diplomático e/ou consular de países que mantém convênio de reciprocidade para o exercício de atividade remunerada no Brasil | 5 - Dependente de agente diplomático e/ou consular de países que mantêm acordo de reciprocidade para o exercício de atividade remunerada no Brasil |
| 12 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre a República Federativa do Brasil e a República Portuguesa. | 6 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre a República Federativa do Brasil e a República Portuguesa |

 Campos criados no cadastro do funcionário:

**Atenção:**

Informações para geração do **Grupo treiCap:**

Criado o grupo **treiCap** (Informação de treinamentos, capacitações do trabalhador) no registro {**infoContrato**}.

As informações dos cursos/capacitações são oriundas do sistema de Gestão de Pessoas e para sua devida configuração, os seguintes passos devem ser realizados:

 

* Criar/modificar um curso e configurá-lo como "curso esocial", além de fazer a correspondência com o código de treinamento específico (Tabela 28)

* Criar/modificar uma turma na qual o curso definido anteriormente será ministrado. No caso da criação da turma, desmarcar a opção "Exibir somente entidades que ministrem o curso"

           para facilitar a inclusão.

* No cadastro de turmas, acessar anexos >> Participantes e adicionar o funcionário para o qual será gerado o S-2200

 Ainda no cadastro de turmas, acessar anexos >> Avaliação de Conhecimento. Posteriormente, será necessário clicar na avaliação de desempenho e executar o processo "Fechar avaliação de conhecimento". Caso o sistema não tenha gerado a avaliação de desempenho automaticamente, basta inserir a mesma manualmente.

* Ainda no cadastro de turmas, acessar anexos >> Avaliação de Conhecimento.  Caso o sistema não tenha gerado a avaliação de conhecimento automaticamente, basta inserir a mesma manualmente.

* Depois da criação da avaliação de conhecimento, será necessário adicionar os avaliados. Acessar anexos da avaliação recém-criada>> avaliados

**Observação importante**: somente é permitido adicionar avaliados dentre os participantes definidos para aquela turma.

* Somente após esse processo, o curso constará como realizado pelo funcionário. Para fins de negócio, o sistema de gestão de pessoas só considera que um curso já foi concluído, após o fechamento da avaliação de conhecimento daquela turma referente ao curso.
