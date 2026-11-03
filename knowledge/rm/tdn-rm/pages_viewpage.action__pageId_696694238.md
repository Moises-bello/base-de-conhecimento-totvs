---
content_hash: c3615a4370199b3b3d63277daeef563b363652e64adfe4abc17add8ffe6222fb
fetched_at: '2026-06-29T00:11:21.528150+00:00'
page_id: '696694238'
product: rm
source: tdn-rm
title: Nota Técnica nº 05/2022 - Leiaute S-1.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=696694238
version: 36
---

false

**A partir dos patches:**

* 12.1.33.289
* 12.1.34.189
* 12.1.2205.127
* e Superiores.

Objetivo:

Em 15/06/2022 foi disponibilizado a [Nota Técnica](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-0-05-2022.pdf) apontando ajustes no leiaute S-1.0 do eSocial.

1Seguem orientações referente ao produto TOTVS Folha de Pagamento, para atender essa alteração:1AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

2ParametrizaçãoParametrização

Atualizado a descrição da versão no Parametrizador.

true3AlteraçõesAlterações11TabelasTabelas

1) Tabela "18-Motivos de Afastamentos" incluídos os códigos abaixo:

| Código | Descrição |
| --- | --- |
| 41 | Qualificação - Afastamento por suspensão do contrato de acordo com o art. 17 da MP 1.116/2022 |
| 42 | Qualificação - Afastamento por suspensão do contrato de acordo com o art. 19 da MP 1.116/2022 |

Estes códigos foram disponibilizados no Parametrizador | eSocial | De/Para de Afastamento que serão utilizados no evento S-2230.

2) Tabela "01 – Rubrica" foi incluído código abaixo:

| Código | Descrição |
| --- | --- |
| 906 | Beneficiário do Programa Nacional de Prestação de Serviço Civil Voluntário |

Disponibilizado no cadastro de categoria do trabalhador:

3) Tabela "19 – Motivos de Desligamento" ajustada a descrição do código abaixo:

| Código | Descrição Atual |
| --- | --- |
| 29 | Redistribuição ou Reforma Administrativa |

Ajustado no Parametrizador | eSocial | De/Para de Desligamento:

4) Tabela "24 - Agentes Nocivos e Atividades - Aposentadoria Especial" alterada a descrição dos códigos abaixo: 

Ajustada a descrição em RH | Segurança e Saúde Ocupacional | PPRA | PGR | Tipos de Agentes:

| Código | Descrição |
| --- | --- |
| 01.09.003 | Bis (cloro metil) éter, clorometileter, (éter bis (clorometílico) ou éter metílico de clorometila), bisclorometil |
| 01.19.008 | Aminobifenila (4-aminodifenil) |

5) Tabela "28 - Treinamentos, Capacitações, Exercícios Simulados e Outras Anotações" excluídos os códigos []  permanecendo apenas os códigos abaixo:

| Código | Descrição |
| --- | --- |
| 1006 | Autorização para trabalhar em instalações elétricas |
| 1207 | Operação e realização de intervenções em máquinas |

Ajuste realizado em RH | Gestão de Pessoas | Desenvolvimento | Cursos:

2S-2200S-2200

1) S-2200 Campo {tpAdmissao} – incluído valor [7] Transferência quando a empresa sucedida é considerada inapta por inexistência de fato.

2) Evento S-2200 alterada a condição do grupo {sucessaoVinc}:

| De | Para |
| --- | --- |
| O (se tpAdmissao = [2, 3, 4] ou tpProv = [5, 8]); N (nos demais casos) | O (se tpAdmissao = [2, 3, 4, **7**] ou tpProv = [5, 8]); N (nos demais casos) |

Tratativa para gerar o grupo {sucessaoVinc} também quando for o tipo de admissão "7"(PFUNC.TIPOADMISSAO seja "T - Ent Transf sem ônus p/ Cedente" e PFUNC.MOTIVOTRANSFERENCIA seja 5 ).

3) S-2200 Campo {tpProv} – incluído valor [11] e alteradas descrição do valor [5] e validação

           11 - Estabilizados - Art. 19 do ADCT

| De | Para |
| --- | --- |
| 5 - Redistribuição | 5 - Redistribuição ou Reforma Administrativa |

           Validação: Os valores [3, 5, 6, 7, 8, 9] só são permitidos se a natureza jurídica do declarante for Administração Pública (grupo [1]). Se codCateg = [302], deve ser preenchido com [2, 5, 8,10].

1S-2299S-2299

S-2299:

* Criação do motivo de rescisão 43 - Transferência de empregado de empresa considerada inapta por inexistência de fato.
* Grupo {sucessaoVinc} – alterada condição

| De | Para |
| --- | --- |
| O (se mtvDeslig = [11, 12, 13, 28, 29, 30, 37]); N (nos demais casos). | O (se mtvDeslig = [11, 12, 13, 28, 29, 30, 37, \{\*}43{\*}]); N (nos demais casos) |

* Grupo {verbasResc} – alterada condição

| De | Para |
| --- | --- |
| N (se mtvDeslig = [11, 12, 13, 25, 28, 29, 30, 34, 36] OU dtDeslig for anterior ao início de obrigatoriedade dos eventos periódicos para o empregador OU tpRegTrab em S-2200 = [2]); OC (nos demais casos). | N (se mtvDeslig = [11, 12, 13, 25, 28, 29, 30, 34, 36, **43**] OU dtDeslig for anterior ao início de obrigatoriedade dos eventos periódicos para o empregador OU tpRegTrab em S-2200 = [2]); OC (nos demais casos). |

1S-2210S-2210

S-2210: Alterada validações

* Campo {hrAcid} – alterada validação

| De | Para |
| --- | --- |
| Hora do acidente, no formato HHMM. Validação: Preenchimento obrigatório e exclusivo se tpAcid = [1, 3]. Se informada, deve estar no intervalo entre [0000] e [2359], criticando inclusive a segunda parte do número, que indica os minutos, que deve ser menor ou igual a 59. Se tpCat = [2, 3], deve ser informado valor igual ao preenchido no evento de CAT anterior, quando informado em nrRecCatOrig. | Hora do acidente, no formato HHMM. Validação: Preenchimento obrigatório se tpAcid = [1] ou se (tpAcid = [3] e dtAcid >= [2022-01-26]). Não informar se tpAcid = [2]. Se preenchida, deve estar no intervalo entre [0000] e [2359], criticando inclusive a segunda parte do número, que indica os minutos, que deve ser menor ou igual a 59. Se tpCat = [2, 3], deve ser informado valor igual ao preenchido no evento de CAT anterior, quando informado em nrRecCatOrig. |

* Campo {hrsTrabAntesAcid} – alterada validação

| De | Para |
| --- | --- |
| Horas trabalhadas antes da ocorrência do acidente, no formato HHMM. Validação: Preenchimento obrigatório e exclusivo se tpAcid = [1]. Se informada, deve estar no intervalo entre [0000] e [9959], criticando inclusive a segunda parte do número, que indica os minutos, que deve ser menor ou igual a 59. | Horas trabalhadas antes da ocorrência do acidente, no formato HHMM. Validação: Preenchimento obrigatório se tpAcid = [1] ou se (tpAcid = [3] e dtAcid >= [2022-07-20]). Não informar se tpAcid = [2]. Se preenchida, deve estar no intervalo entre [0000] e [9959], criticando inclusive a segunda parte do número, que indica os minutos, que deve ser menor ou igual a 59. |

1S-2300 / S-2306S-2300 / S-2306

 S-2300 e S-2306:

* Grupo {cargoFuncao} – alterada condição

| De | Para |
| --- | --- |
| OC (se codCateg = [901, 903, 904]); O (nos demais casos) | OC (se codCateg = [901, 903, 904, 906]); O (nos demais casos) |

* Grupo {remuneracao} – alterada condição

| De | Para |
| --- | --- |
| O (se codCateg = [721, 722, 771]); OC (nos demais casos) | O (se codCateg = [721, 722, 771, 906]); OC (nos demais casos) |

* Grupo {infoEstagiario} – alteradas condição e descrição

| De | Para |
| --- | --- |
| O (se codCateg = [901]); | O (se codCateg = [901, 906]); |

* Grupo {ageIntegracao} – alterada condição

| De | Para |
| --- | --- |
| OC | OC (se o código de categoria for igual a [901]); N (nos demais casos) |

* Grupo {supervisorEstagio} – alterada condição

| De | Para |
| --- | --- |
| OC | OC (se o código de categoria for igual a [901]); N (nos demais casos) |

* Campo {natEstagio} – alterada descrição e incluída validação.

| De | Para |
| --- | --- |
| Natureza do estágio. Valores válidos: O - Obrigatório N - Não obrigatório | Natureza do estágio ou da prestação de serviço civil voluntário. Valores válidos: O - Obrigatório N               Não obrigatório Validação: Se o código de categoria for igual a [906], deve ser preenchido com [N] |

* Campo {nivEstagio} – alteradas ocorrência e descrição, e incluída validação

| De | Para |
| --- | --- |
| Ocorrência 1 Informar o nível do estágio. Valores válidos: 1 - Fundamental 2 - Médio 3 - Formação profissional 4 - Superior 8 - Especial 9 - Mãe social (Lei 7.644/1987) | Ocorrência 0-1 Informar o nível do estágio ou da prestação de serviço civil voluntário. Valores válidos: 1 - Fundamental 2 - Médio 3 - Formação profissional 4 - Superior 8 - Especial 9 - Mãe social (Lei 7.644/1987) Validação: Preenchimento obrigatório se o código de categoria for igual a [901]. Se o código de categoria for igual a [906], não pode ser informado [9]. |

S-2300

S-2306

1S-2240S-2240

S-2240:

* Campo {ideOC} – alterada ocorrência e incluída validação.

| De | Para |
| --- | --- |
| 1 | 0-1 Validação: Preenchimento obrigatório se codAgNoc for diferente de [09.01.001]. |

* Campo {nrOC} – alterada ocorrência e incluída validação.

| De | Para |
| --- | --- |
| 1 | 0-1 Validação: Preenchimento obrigatório se codAgNoc for diferente de [09.01.001]. |

* Campo {ufOC} – alterada ocorrência e incluída validação.

| De | Para |
| --- | --- |
| 1 | 0-1 Validação: Preenchimento obrigatório se codAgNoc for diferente de [09.01.001]. |
