---
content_hash: c552d2e500a8d23f58b584a78d2c3d2da07df1d4d902cb484b7d2db8381283e3
fetched_at: '2026-06-29T00:10:59.131369+00:00'
page_id: '611308887'
product: rm
source: tdn-rm
title: Alterações S-2240 - Condições Ambientais do Trabalho - Agentes Nocivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=611308887
version: 10
---

false

**A partir das Versões:**

* 12.1.28.281
* 12.1.29.239
* 12.1.31.142

* e Superiores.
falseImportante!

Conforme orientação do governo, é necessário gerar uma carga do evento S-2240 no mês de inicio da obrigatoriedade. Para isso deverá acessar o menu " " e executar o processo selecionando o evento S-2240..

Lembrando que, funcionários com a data de admissão anterior ao inicio da obrigatoriedade do envio do evento terão a tag <dtIniCondicao> preenchida com a data do inicio da obrigatoriedade cadastrada nos parametros do eSocial.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2240 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {evtExpRisco }: alterada descrição | Evento Condições Ambientais do Trabalho -  Fatores de Risco | Evento Condições Ambientais do Trabalho - Agentes Nocivos |
| Grupos {infoAmb}: alterada ocorrência | 1-99 | 1 |
| Grupos {ativPericInsal}: e campo {codAtiv} excluído. |  |  |
| Grupos {fatRisco}: Campos {codFatRis,dscFatRisc, tpAval,intConc, limTol, unMed, tecMedicao, insalubridade, periculosidade, aposentEsp} excluídos. |  |  |
| Grupos {agNoc} e Campos {codAgNoc, dscAgNoc,tpAval,intConc, limTol, unMed, tecMedicao} incluídos. |  | Agente(s) nocivo(s) ao(s) qual(is) o trabalhador está exposto. |
| Grupos {agNoc}: Campos {epcEpi} vinculado a novo grupo | Grupo anterior {fatRisco} |  |
| Grupos {epi}: alterada a chave | caEPI, dscEPI | docAval, dscEPI |
| Grupos {epiCompl} e campos {medProtecao, condFuncto, usoInint, przValid, periodicTroca, higienizacao} incluídos. |  | Ocorrência: 0-1 Condição: O (se utilizEPI = [2]);  N (nos demais casos) Descrição: Requisitos das NR-06 e NR-09 pelo(s) EPI(s) informado(s) |
| Grupos {grupoinfoExpRisco}: Campos {dtIniCondicao} alterada validação. | Informar a data em que o trabalhador iniciou as atividades  nas condições descritas ou a data de início da obrigatoriedade deste evento para o empregador no eSocial, a que for mais recente. Validação: Deve ser uma data válida, igual ou anterior à data atual  e igual ou posterior à data de admissão do vínculo a que se refere. Não pode ser anterior à data de início da obrigatoriedade deste  evento para o empregador no eSocial. | Informar a data em que o trabalhador iniciou as atividades nas condições descritas ou a data de início da obrigatoriedade deste  evento para o empregador no eSocial, a que for mais recente.  Validação: Deve ser uma data válida, igual ou posterior à data de admissão do vínculo a que se refere. Não pode ser anterior à data  de início da obrigatoriedade deste evento para o empregador no eSocial, nem pode ser posterior a 30 (trinta) dias da data atual. |
| Grupos {infoAmb}: Campo {codAmb} excluído. |  |  |
| Grupos {infoAmb}: Campo {localAmb} incluído. |  | Tipo: N Ocorrência: 1 tamanho: 1 Descrição: Informar o tipo de estabelecimento do ambiente de  trabalho. Valores válidos:  1 - Estabelecimento do próprio empregador  2 - Estabelecimento de terceiros |
| Grupos {infoAmb}: Campo {dscSetor} incluído. |  | Tipo: C Ocorrência: 1 tamanho: 1-100 Descrição: Descrição do lugar administrativo, na estrutura organizacional da empresa, onde o trabalhador exerce suas atividades laborais. |
| Grupos {infoAmb}: Campo {nrInsc} incluído. |  | Tipo: N Ocorrência: 1 tamanho: 1 Descrição: Preencher com o código correspondente ao  tipo de inscrição, conforme Tabela 05.  Valores válidos: 1 - CNPJ 3 - CAEPF 4 - CNO |
| Grupos {infoAmb}: Campo {tpInsc} incluído. |  | Tipo: C Ocorrência: 1 tamanho: 12-14 Descrição: Número de inscrição onde está localizado o ambiente. Validação: Deve ser um identificador válido, compatível  com o conteúdo do campo infoAmb/tpInsc e:  a) Se localAmb = [1], deve ser válido e existente na  Tabela de Estabelecimentos (S-1005); b) Se localAmb = [2], deve ser diferente dos  estabelecimentos informados na Tabela S-1005 e, se  infoAmb/tpInsc = [1] e o empregador for pessoa jurídica, a raiz do CNPJ informado deve ser diferente da constante  em S-1000. |
| Grupos {agNoc}: Campo {codAgNoc} incluído. |  | Tipo: C Ocorrência: 1 Tamanho: 9 Descrição: Informar o código do agente nocivo ao qual o trabalhador está exposto. Preencher com números e pontos. Caso não haja exposição,  informar o código [09.01.001] (Ausência de  agente nocivo ou de atividades previstas no  Anexo IV do Decreto 3.048/1999).  Validação: Deve ser um código válido e existente na Tabela 24. Não é possível informar nenhum outro código de agente nocivo quando houver o código [09.01.001]. |
| Grupos {agNoc}: Campo {dscAgNoc} incluído. |  | Tipo: C Ocorrência: 0-1 Tamanho: 1-999 Descrição: Descrição do agente nocivo.  Validação: Preenchimento obrigatório se  codAgNoc = [01.01.001, 01.02.001,  01.03.001, 01.04.001, 01.05.001, 01.06.001,  01.07.001, 01.08.001, 01.09.001, 01.10.001, 01.12.001, 01.13.001, 01.14.001, 01.15.001,  01.16.001, 01.17.001, 01.18.001, 05.01.001]. |
| Grupos {agNoc}: Campo {tpAval} alterados grupo pai e descrição. | Grupo anterior {fatRisco}  Tipo de avaliação do fator de risco: 1 - Critério quantitativo; 2 - Critério qualitativo. Valores Válidos: 1, 2. | Tipo: N Ocorrência: 1 Tamanho: 1 Descrição: Tipo de avaliação do agente nocivo.  Valores válidos:  1 - Critério quantitativo  2 - Critério qualitativo |
| Grupos {agNoc}: Campo {intConc} alterados grupo pai e descrição. | Grupo anterior {fatRisco}  Intensidade, concentração ou dose da exposição do trabalhador ao fator de risco cujo critério de avaliação seja quantitativo. Validação: Preenchimento obrigatório se {tpAval} = [1]. Não informar se {tpAval} = [2]. | Tipo: N Ocorrência: 0-1 Tamanho: 1-10 DEC: 4 Descrição: Intensidade, concentração ou dose da exposição  do trabalhador ao agente nocivo cujo critério de  avaliação seja quantitativo.  Validação: Preenchimento obrigatório e exclusivo  se tpAval = [1]. |
| Grupos {agNoc}: Campo {limTol} alterados grupo pai e descrição. | Grupo anterior {fatRisco}  Limite de tolerância calculado para agentes específicos, conforme técnica de medição exigida na legislação. Validação: Preenchimento obrigatório se {tpAval} = [1] e {codFatRis} = [01.01.014, 01.01.018, 02.01.687, 02.01.788]. Não informar nos demais casos. | Tipo: N Ocorrência: 0-1 Tamanho: 1-10 DEC: 4 Descrição: Limite de tolerância calculado para agentes específicos, conforme técnica de medição  exigida na legislação. Validação: Preenchimento obrigatório e exclusivo se tpAval = [1] e codAgNoc = [01.18.001,  02.01.014]. |
| Grupos {agNoc}: Campo {unMed} alterados grupo pai e descrição. | Grupo anterior {fatRisco}  Dose ou unidade de medida da intensidade ou concentração do agente: 1 - dose diária de ruído; 2 - decibel linear (dB (linear)); 3 - decibel (C) (dB(C)); 4 - decibel (A) (dB(A)); 9 - metro por segundo ao quadrado (m/s2); 10 - metro por segundo elevado a 1,75 (m/s1,75); 11 - parte de vapor ou gás por milhão de partes de ar contaminado (ppm); 12 - miligrama por metro cúbico de ar (mg/m3); 13 - fibra por centímetro cúbico (f/cm3); 14 - grau Celsius (ºC); 15 - metro por segundo (m/s); 16 - porcentual; 17 - lux (lx); 18 - unidade formadora de colônias por metro cúbico (ufc/m3); 19 - dose diária; 20 - dose mensal; 21 - dose trimestral; 22 - dose anual; 26 - watt por metro quadrado (W/m2); 27 - ampère por metro (A/m); 28 - militesla (mT); 29 - microtesla (µT); 30 - miliampère (mA); 31 - quilovolt por metro (kV/m); 32 - volt por metro (V/m); 35 - joule por metro quadrado (J/m2); 36 - milijoule por centímetro quadrado (mJ/cm2); 37 - milisievert (mSv); 39 - milhão de partículas por decímetro cúbico (mppdc); 43 - umidade relativa do ar (UR (%)). Validação: Preenchimento obrigatório se {tpAval} = [1]. Não informar se {tpAval} = [2]. Valores Válidos:1,2,3,4,9,10,11,12,13,14,15,16,17,18,19,20,21,22,26,27,28,29,30,31,32,35,36,37,39,43. | Tipo: N Ocorrência: 0-1 Tamanho: 1-2 Descrição: Dose ou unidade de medida da intensidade ou concentração do agente.  Valores válidos: 1 - dose diária de ruído  2 - decibel linear (dB (linear))  3 - decibel (C) (dB(C))  4 - decibel (A) (dB(A)) 5 - metro por segundo ao quadrado (m/s2) 6 - metro por segundo elevado a 1,75 (m/s1,75)  7 - parte de vapor ou gás por milhão de partes de ar contaminado (ppm)  8 - miligrama por metro cúbico de ar (mg/m3)  9 - fibra por centímetro cúbico (f/cm3)  10 - grau Celsius (ºC)  11 - metro por segundo (m/s)  12 - porcentual  13 - lux (lx)  14 - unidade formadora de colônias por metro cúbico (ufc/m3)  15 - dose diária  16 - dose mensal  17 - dose trimestral  18 - dose anual 19 - watt por metro quadrado (W/m2)  20 - ampère por metro (A/m)  21 - militesla (mT)  22 - microtesla (μT) 23 - miliampère (mA)  24 - quilovolt por metro (kV/m)  25 - volt por metro (V/m)  26 - joule por metro quadrado (J/m2)  27 - milijoule por centímetro quadrado (mJ/cm2)  28 - milisievert (mSv)  29 - milhão de partículas por decímetro cúbico (mppdc) 30 - umidade relativa do ar (UR (%)) Validação: Preenchimento obrigatório e exclusivo se tpAval = [1]. |
| Grupos {agNoc}: Campo {tecMedicao} alterados grupo pai e descrição. | Grupo anterior {fatRisco}  Técnica utilizada para medição da intensidade ou concentração. Validação: Preenchimento obrigatório se {tpAval} = [1]. Não informar se {tpAval} = [2]. | Tipo: C Ocorrência: 0-1 Tamanho: 1-40 Descrição: Técnica utilizada para medição da intensidade ou concentração.  Validação: Preenchimento obrigatório e exclusivo se tpAval = [1]. |
| Grupos {agNoc}: Campo {epcEpi} alterados grupo pai. | fatRisco | agNoc |
| Grupos {ativPericInsal} e campo {codAtiv} excluído. |  |  |
| Grupos {fatRisco} e campos {codFatRis, dscFatRisc, tpAval, intConc, limTotal, unMed, tecMedicao, insalubridade, periculosidade, aposentEsp} excluído. |  |  |
| Grupos {epi} e campo {caEPI, medProtecao, condFuncto, usoInint, przValid, periodicTroca, higienizacao, } excluído. |  |  |
| Grupos {epi} e campo {docAval} incluído. |  | Certificado de Aprovação - CA ou documento de avaliação do EPI. |
| Grupos {epiCompl}: Campo {medProtecao} incluído. |  | Tipo: C Ocorrência: 1 Tamanho: 1 Descrição: Foi tentada a implementação de medidas de  proteção coletiva, de caráter administrativo  ou de organização, optando-se pelo EPI por inviabilidade técnica, insuficiência ou interinidade , ou ainda em caráter complementar ou  emergencial? Valores válidos: S - Sim N - Não |
| Grupos {epiCompl}: Campo {condFuncto} incluído. |  | Tipo: C Ocorrência: 1 Tamanho: 1 Descrição: Foram observadas as condições de funcionamento  do EPI ao longo do tempo, conforme especificação técnica do fabricante nacional ou importador,  ajustadas às condições de campo?  Valores válidos: S - Sim N - Não |
| Grupos {epiCompl}: Campo {usoInint} incluído. |  | Tipo: C Ocorrência: 1 Tamanho: 1 Descrição: Foi observado o uso ininterrupto do EPI ao longo do tempo, conforme especificação técnica do  fabricante nacional ou importador, ajustadas às condições de campo? Valores válidos: S - Sim N - Não |
| Grupos {epiCompl}: Campo {przValid} incluído. |  | Tipo: C Ocorrência: 1 Tamanho: 1 Descrição: Foi observado o prazo de validade do CA no momento  da compra do EPI?  Valores válidos: S - Sim N - Não |
| Grupos {epiCompl}: Campo {periodicTroca} incluído. |  | Tipo: C Ocorrência: 1 Tamanho: 1 Descrição:  É observada a periodicidade de troca definida pelo  fabricante nacional ou importador e/ou programas  ambientais, comprovada mediante recibo assinado  pelo usuário em época própria?  Valores válidos: S - Sim N - Não |
| Grupos {epiCompl}: Campo {higienizacao} incluído. |  | Tipo: C Ocorrência: 1 Tamanho: 1 Descrição:  É observada a higienização conforme orientação  do fabricante nacional ou importador?  Valores válidos: S - Sim N - Não |
| Grupos {epiCompl}: Campos {nisResp, nmResp} excluídos. |  |  |
| Grupos {obs}: Campo {metErg} excluído. |  |  |
| Grupos {obs}: Campo {obsCompl} excluída validação. | Observação(ões) complementar(es) referente(s) a registros ambientais.  Validação: Preenchimento obrigatório se {metErg}  não for informado. | Observação(ões) complementar(es) referente(s) a  registros ambientais. |

Informações complementares:
