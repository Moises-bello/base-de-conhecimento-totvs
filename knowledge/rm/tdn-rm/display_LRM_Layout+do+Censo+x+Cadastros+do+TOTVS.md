---
content_hash: 146d68a881e32ce1df1cdcb9214556f2375971529f887cac32c06d9a3671c2fe
fetched_at: '2026-06-29T00:10:59.013650+00:00'
page_id: '608391631'
product: rm
source: tdn-rm
title: Layout do Censo x Cadastros do TOTVS
type: documentation
url: https://tdn.totvs.com/display/LRM/Layout+do+Censo+x+Cadastros+do+TOTVS
version: 76
---

# **Registro 41 - Alunos**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo - layout INEP** | **Cadastro Totvs Educacional** | **Caminho do cadastro** | **Imagem** | **Regra** |
| Tipo de registro | Não possui | - | - | - |
| ID do aluno no INEP | Cadastro do aluno | Currículo e oferta | aluno | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Nome | Cadastro do aluno | Currículo e oferta | aluno | guia: identificação |  | Sem regra |
| CPF | Cadastro do aluno | Currículo e oferta | aluno | guia: documentos | subguia: pessoais |  | Sem regra |
| Documento de estrangeiro ou passaporte | Cadastro do aluno | Currículo e oferta | aluno | guia: documentos | subguia: complementares |  | Sem regra |
| Data de nascimento | Cadastro do aluno | Currículo e oferta | aluno | guia: identificação |  | Sem regra |
| Cor/raça | Cadastro do aluno | Currículo e oferta | aluno | guia: identificação | subguia: informações adicionais |  | Sem regra |
| Nacionalidade | Cadastro do aluno | Currículo e oferta | aluno | guia: identificação |  | Sem regra |
| UF de nascimento | Cadastro do aluno | Currículo e oferta | aluno | guia: identificação |  | Sem regra |
| Município de nascimento | Cadastro do aluno | Currículo e oferta | aluno | guia: identificação |  | Sem regra |
| Pais de origem | Cadastro do aluno | Currículo e oferta | aluno | guia: identificação |  | Sem regra |
| Aluno com Deficiência, Transtorno do espectro autista (TEA), altas habilidades ou superdotação | Cadastro do aluno | Currículo e oferta | aluno | anexos | dados para o censo escolar e SISTEC |  | Aceita apenas 0, 1 e 2. Quando preenchido com 1, dos campos 13 a 21, no mínimo um dos campos também deve estar preenchido com 1. Quando preenchido com 0 ou 2, os campos 13 a 21, devem estar preenchidos com 0. |
| Tipos de deficiência. Campos 13 a 22. | Cadastro do aluno e relação de deficiências | Currículo e oferta | aluno | guia: documentos | subguia: pessoas com necessidades educacionais especiais |  | Verificar regra anterior |
| Tipo de escola que o aluno concluiu o ensino médio | Cadastro do aluno | Currículo e oferta | aluno | guia: diversos | instituição do ensino básico | editar | tipo da instituição |  | Sem regra |

# **Registro 42 - Cursos dos Alunos**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo - layout INEP** | **Cadastro Totvs Educacional** | **Caminho do cadastro** | **Imagem** | **Regra** |
| Tipo de registro | Não possui | - | - | - |
| ID na IES | Cadastro do aluno | Currículo e oferta | aluno | guia: identificação. RA do aluno |  | Sem regra |
| Semestre de referencia | Cadastro de curso/habilitação | Currículo e oferta | aluno | anexos | curso/habilitações | guia: ingresso | data de ingresso no curso |  | Somente deve ser preenchido quando a instituição for federal |
| Código do curso | Cadastro de curso do MEC | Configurações | Instituição do MEC | Anexo | Curso do MEC |  | Sem regra |
| Código do polo ou curso a distancia | Cadastro de curso | Currículo e oferta | estrutura curricular | cursos | Modalidade |  | Somente deve ser preenchido quando o curso for a distância |
| Turno do aluno | Cadastro da matricula no período letivo | Currículo e oferta | aluno | anexos | matricula no período letivo | guia: identificação | turno |  | Sem regra |
| Situação de vínculo do aluno ao curso | Cadastro da situação de matrícula | Matrícula e Avaliação | Matriculas |  | Situação do aluno no curso período de coleta do Censo.  Valores possíveis:  2 – Cursando 3 – Matrícula trancada 4 – Desvinculado do curso 5 - Transferência Interna 6 – Formado 7 – Falecido |
| Curso origem | Cadastro de curso/habilitação | Currículo e oferta | aluno | anexos | curso/habilitações | anexos | transferência |  | Somente é informado para alunos que passaram por transferência interna. |
| Semestre de conclusão do curso | Cadastro da matricula no período letivo | Currículo e oferta | aluno | anexos | matricula no período letivo | guia: identificação | resultado |  | Somente é informado, quando a situação de vínculo/matricula é "formado" |
| Aluno PARFOR | Cadastro de curso/habilitação | Currículo e oferta | aluno | anexos | curso/habilitações | anexos | dados do censo escolar |  | Somente é preenchido quando a forma de ingresso é: PARFOR. Somente pode ser preenchido quando o grau acadêmico do curso for: licenciatura |
| Segunda licenciatura/formação pedagógica | Cadastro de curso/habilitação | Currículo e oferta | aluno | anexos | curso/habilitações | anexos | dados do censo escolar |  | Sem regra |
| Tipo segunda licenciatura/formação pedagógica | Cadastro de curso/habilitação | Currículo e oferta | aluno | anexos | curso/habilitações | anexos | dados do censo escolar |  | Sem regra |
| Semestre de ingresso no curso | Cadastro de curso/habilitação | Currículo e oferta | aluno | anexos | curso/habilitações | guia: ingresso | data de ingresso no curso |  | Sem regra |
| Forma de ingresso. Campos: 14 a 23. | Cadastro de curso/habilitação | Currículo e oferta | aluno | anexos | curso/habilitações | guia: ingresso | tipo de ingresso |  | Sem regra |
| Mobilidade acadêmica | Cadastro da matricula no período letivo | Currículo e oferta | aluno | anexos | matricula no período letivo | anexos | dados para o censo e sistec |  | Sem regra |
| Tipo de mobilidade acadêmica | Cadastro da matricula no período letivo | Currículo e oferta | aluno | anexos | matricula no período letivo | anexos | dados para o censo e sistec |  | Sem regra |
| Mobilidade acadêmica - Nacional | Cadastro da matricula no período letivo | Currículo e oferta | aluno | anexos | matricula no período letivo | anexos | dados para o censo e sistec |  | Somente pode ser preenchido a mobilidade nacional, para instituições federais e estaduais |
| Mobilidade acadêmica - Internacional | Cadastro da matricula no período letivo | Currículo e oferta | aluno | anexos | matricula no período letivo | anexos | dados para o censo e sistec |  | Sem regra |
| Financiamento estudantil. Campos: 28 a 39. | Cadastro de bolsas | Financeiro/contábil | formação de preços | bolsas | anexo | dados da bolsa para o censo escolar |  | Sem regra |
| Apoio social. Campos: 40 a 46. | Cadastro de curso/habilitação | Currículo e oferta | aluno | anexos | curso/habilitações | anexos | dados do censo escolar |  | Sem regra |
| Atividade extracurricular. Campos 47 a 55. | Cadastro de curso/habilitação | Currículo e oferta | aluno | anexos | curso/habilitações | anexos | dados do censo escolar |  | Sem regra |
| Carga horária total do curso por aluno | Cadastro de matriz curricular | Currículo e oferta | estrutura curricular | matrizes curriculares | carga horária |  | Sem regra |
| Ingressou por política de ação afirmativa ou por programa diferenciado de destinação de vagas? Campos 58 a 59. | Cadastro de curso/habilitação | Currículo e oferta | aluno | anexos | curso/habilitações | anexos | dados do censo escolar |  | Sem regra |
| Tipo de Ação Afirmativa - Lei de Cotas (Lei nº 12.711 de 2012 e Lei nº 14.723 de 2023) | Cadastro de curso/habilitação | Currículo e oferta | aluno | anexos | curso/habilitações | anexos | dados do censo escolar |  | Para as opções 1, 2, 3, 4, 5, 6, 7 e 8 é obrigatório ter preenchido o campo  Tipo de escola que concluiu o Ensino Médio com a opção escola pública '1 - Escola Pública'.  Para as opções 1 e 5 é obrigatório ter preenchido no campo cor/raça com uma das opções "2 -Preto", "3 - Pardo" ou "5 - Indígena".  Para as opções 3 e 7 é obrigatório ter preenchido no campo Aluno com Deficiência, Transtorno do espectro autista (TEA), altas habilidades ou superdotação como "1 - Sim", exceto a marcação exclusiva da opção "Tipo de deficiência - Altas habilidades ou superdotação".  Se qualquer uma das opções for informada e a IES não for uma instituição pública federal, deverá apresentar a mensagem: A opção "Lei de Cotas" não pode ser selecionada caso a IES não seja uma instituição pública federal. |
| Outras reservas de vagas OU Programa diferenciado de destinação de vagas - Preto, Pardo e Indígena (PPI). Campos 61 a72 | Cadastro de curso/habilitação | Currículo e oferta | aluno | anexos | curso/habilitações | anexos | dados do censo escolar |  | Sem regra |
| Carga horária integralizada pelo aluno | Cadastro de disciplinas | Currículo e oferta | estrutura curricular | disciplinas | carga horária |  | São somadas todas as cargas horárias das disciplinas onde o aluno possui resultado final de aprovado e também atividades ofertadas finalizadas. |
| Justificativa | Cadastro da matricula no período letivo | Currículo e oferta | aluno | anexos | matricula no período letivo | anexos | dados para o censo e sistec |  | Sem regra |

# **Registro 31 - Docentes**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo - layout INEP** | **Cadastro Totvs Educacional** | **Caminho do cadastro** | **Imagem** | **Regra** |
| Tipo de registro | Não possui | - | - | - |
| ID do docente na IES | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Nome do Docente | Cadastro do professor | Currículo e oferta | professor | guia: identificação |  | Sem regra |
| CPF | Cadastro do professor | Currículo e oferta | professor | guia: documentos | subguia: pessoais |  | Sem regra |
| Documento estrangeiro | Cadastro do professor | Currículo e oferta | professor | guia: documentos | subguia: complementares |  | Sem regra |
| Data de Nascimento | Cadastro do professor | Currículo e oferta | professor | guia: identificação |  | Sem regra |
| Cor/Raça | Cadastro do professor | Currículo e oferta | professor | guia: identificação | subguia: informações adicionais |  | Sem regra |
| Nacionalidade | Cadastro do professor | Currículo e oferta | professor | guia: identificação |  | Sem regra |
| País de origem | Cadastro do professor | Currículo e oferta | professor | guia: identificação |  | Sem regra |
| UF de nascimento | Cadastro do professor | Currículo e oferta | professor | guia: identificação |  | Sem regra |
| Município de Nascimento | Cadastro do professor | Currículo e oferta | professor | guia: identificação |  | Sem regra |
| Deficiência, Transtorno do espectro autista (TEA), altas habilidades ou superdotação | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Aceita apenas 0, 1 e 2. Quando preenchido com 1, dos campos 13 a 21, no mínimo um dos campos também deve estar preenchido com 1. Quando preenchido com 0 ou 2, os campos 13 a 21, devem estar preenchidos com 0. |
| Tipos de deficiência. Campos 13 a 22. | Cadastro do professor | Currículo e oferta | professor | guia: documentos | subguia: pessoas com necessidades educacionais especiais |  | Verificar regra anterior |
| Atuação do Docente Campos 23 a 26. | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Se esse campo for informado com a opção "sim", e o docente não tem curso vinculado com a opção "Docente Regente" ou "Docente Conteudista" então apresentar mensagem: "O docente deve ser vinculado a pelo menos um curso com a opção "Docente - Regente" ou "Docente - Conteudista" selecionada" |
| Bolsa Pesquisa Campos 27 a 28. | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Escolaridade | Cadastro do professor | Currículo e Oferta | Professores | Editar | guia: identificação | sub guia: informações adicionais | grau de instrução |  |  |
| Tipo de vínculo | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Tipo de consórcio, acordo ou programa de cooperação do docente sem vínculo contratual com a IES | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| A função de conteudista é exercida em contrato específico (distinto do contrato de regência e/ou função de gestão)? | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Tipo de vínculo - Exclusivo conteudista | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Tipo de consórcio, acordo ou programa de cooperação do docente sem vínculo contratual com a IES - Exclusivo conteudista | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Regime de trabalho | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Carga horária semanal do docente | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Docente foi admitido ou iniciou suas atividades no ano de referência do Censo? | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| O docente esteve afastado durante o ano de referência do Censo? | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Docente substituto | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Docente Visitante | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Docente em exercício em 31/12 do ano do censo | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |

# **Registro 32 - Cursos dos Docentes**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo - layout INEP** | **Cadastro Totvs Educacional** | **Caminho do cadastro** | **Imagem** | **Regra** |
| Tipo de registro | Não possui | - | - | - |
| Código do curso no INEP | Instituição do MEC | Configurações | Instituição do MEC | anexos | curso do MEC |  | Sem regra |
| Docente Regente | Turma/Disciplina | Currículo e oferta | turma/disciplina | anexos | professores |  guia: dados do censo |  | Sem regra |
| Docente Conteudista | Turma/Disciplina | Currículo e oferta | turma/disciplina | anexos | professores |  guia: dados do censo |  | Sem regra |
| Docente Coordenador | Turma/Disciplina | Currículo e oferta | turma/disciplina | anexos | professores |  guia: dados do censo |  | Sem regra |

# **Registro 91 - Mediadores**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo - layout INEP** | **Cadastro Totvs Educacional** | **Caminho do cadastro** | **Imagem** | **Regra** |
| Tipo de registro | Não possui | - | - | - |
| ID do mediador na IES | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC | [Código INEP.jpg](https://tdn.totvs.com/download/attachments/608391631/ID%20do%20docente%20na%20IES.jpg?version=1&modificationDate=1772712593020&api=v2) | Sem regra |
| Nome do mediador | Cadastro do professor | Currículo e oferta | professor | guia: identificação | [Nome.jpg](https://tdn.totvs.com/download/attachments/608391631/Nome%20Professor.jpg?version=1&modificationDate=1772713529000&api=v2) | Sem regra |
| CPF | Cadastro do professor | Currículo e oferta | professor | guia: documentos | subguia: pessoais | [CPF.jpg](https://tdn.totvs.com/download/attachments/608391631/CPF%20Professor.jpg?version=1&modificationDate=1772713329323&api=v2) | Sem regra |
| Documento estrangeiro | Cadastro do professor | Currículo e oferta | professor | guia: documentos | subguia: complementares | [Passaporte.jpg](https://tdn.totvs.com/download/attachments/608391631/Passaporte%20Professor.jpg?version=1&modificationDate=1772713868870&api=v2) | Sem regra |
| Data de Nascimento | Cadastro do professor | Currículo e oferta | professor | guia: identificação | [Data de nascimento.jpg](https://tdn.totvs.com/download/attachments/608391631/Data%20de%20nascimento%20professor.jpg?version=1&modificationDate=1772714068733&api=v2) | Sem regra |
| Cor/Raça | Cadastro do professor | Currículo e oferta | professor | guia: identificação | subguia: informações adicionais | [Cor/Raça.jpg](https://tdn.totvs.com/download/attachments/608391631/Cor%20Ra%C3%A7a%20Professor.jpg?version=1&modificationDate=1772714264730&api=v2) | Sem regra |
| Nacionalidade | Cadastro do professor | Currículo e oferta | professor | guia: identificação | [Nacionalidade.jpg](https://tdn.totvs.com/download/attachments/608391631/Nacionalidade%20professor.jpg?version=1&modificationDate=1772714448787&api=v2) | Sem regra |
| País de origem | Cadastro do professor | Currículo e oferta | professor | guia: identificação | [País de origem.jpg](https://tdn.totvs.com/download/attachments/608391631/Pa%C3%ADs%20de%20origem%20Professor.jpg?version=1&modificationDate=1772714588663&api=v2) | Sem regra |
| UF de nascimento | Cadastro do professor | Currículo e oferta | professor | guia: identificação | [UF de nascimento.jpg](https://tdn.totvs.com/download/attachments/608391631/UF%20de%20nascimento%20Professor.jpg?version=1&modificationDate=1772714746170&api=v2) | Sem regra |
| Município de Nascimento | Cadastro do professor | Currículo e oferta | professor | guia: identificação | [Município de nascimento.jpg](https://tdn.totvs.com/download/attachments/608391631/Munic%C3%ADpio%20de%20Nascimento%20Professor.jpg?version=1&modificationDate=1772714955447&api=v2) | Sem regra |
| Deficiência, Transtorno do espectro autista (TEA), altas habilidades ou superdotação | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC | [Deficiência, Transtorno do espectro autista (TEA), altas habilidades ou superdotação.jpg](https://tdn.totvs.com/download/attachments/608391631/Professor%20com%20defici%C3%AAncia.jpg?version=1&modificationDate=1772715282683&api=v2) | Aceita apenas 0, 1 e 2. Quando preenchido com 1, dos campos 13 a 21, no mínimo um dos campos também deve estar preenchido com 1. Quando preenchido com 0 ou 2, os campos 13 a 21, devem estar preenchidos com 0. |
| Tipos de deficiência. Campos 13 a 22. | Cadastro do professor | Currículo e oferta | professor | guia: documentos | subguia: pessoas com necessidades educacionais especiais | [Tipos de deficiência. Campos 13 a 22.jpg](https://tdn.totvs.com/download/attachments/608391631/Professor%20com%20defici%C3%AAncia.jpg?version=1&modificationDate=1772715282683&api=v2) | Verificar regra anterior |
| Escolaridade | Cadastro do professor | Currículo e Oferta | Professores | Editar | guia: identificação | sub guia: informações adicionais | grau de instrução | [Escolaridade.jpg](https://tdn.totvs.com/download/attachments/608391631/Escolaridade.jpg?version=1&modificationDate=1772738665190&api=v2) | [As informações cadastradas ficarão da seguinte forma.jpg](https://tdn.totvs.com/download/attachments/608391631/As%20informa%C3%A7%C3%B5es%20cadastradas%20ficar%C3%A3o%20da%20seguinte%20forma.jpg?version=1&modificationDate=1772739670067&api=v2) |
| Tipo de vínculo | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Carga horária semanal do mediador | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Mediador foi admitido ou iniciou suas atividades no ano de referência do Censo? | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Mediador foi desligado ou encerrou suas atividades no ano de referência do Censo? | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| O mediador esteve afastado durante o ano de referência do Censo? | Cadastro do professor | Currículo e oferta | professor | anexos | dados para o censo escolar e SISTEC |  | Sem regra |
| Atuação do Mediador. Campos 29 a 39. | Turma/Disciplina | Currículo e oferta | turma/disciplina | anexos | professores |  guia: dados do censo |  | Sem regra |

# **Registro 92 - Cursos dos Mediadores**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo - layout INEP** | **Cadastro Totvs Educacional** | **Caminho do cadastro** | **Imagem** | **Regra** |
| Tipo de registro | Não possui | - | - | - |
| Código do curso no INEP | Instituição do MEC | Configurações | Instituição do MEC | anexos | curso do MEC |  | Sem regra |
