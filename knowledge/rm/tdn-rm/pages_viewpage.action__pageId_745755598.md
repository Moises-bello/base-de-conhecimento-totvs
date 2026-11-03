---
content_hash: cfdcdfd874844e820aa41bc65c31d0088a9b3a2b80aab1d9c2f6fe4d571b7abb
fetched_at: '2026-06-29T00:11:32.288619+00:00'
page_id: '745755598'
product: rm
source: tdn-rm
title: Nota Técnica V. S-1.1 01/2023
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745755598
version: 27
---

false

**A partir das Versões:**

* 12.1.2205.248
* 12.1.2209.197
* 12.1.2302.121
* e Superiores.

# Objetivo:

---

Em 09/02/2023 foi disponibilizado pelo eSocial a [Nota Técnica 01/2023](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-1-01-2023.pdf)[,](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-1-01-2023.pdf) apontando ajustes no Layout S-1.1, com isso se fez necessárias algumas adequações no produto TOTVS Folha de Pagamento.

11AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

true3Alterações Alterações 

Seguem orientações referente ao produto TOTVS Folha de Pagamento, para atender essa alteração:

1) Criado o parâmetro da Nota Técnica (**S-1.1 NT 01/2023**) em Configurações | Parametrizador | Folha de Pagamento | eSocial | Configurações Gerais conforme demonstrado abaixo:

**Observação: as mudanças relacionadas aos processos trabalhistas da NT 02/2023 serão contemplas nesse leiaute.**

2) Eventos S-1200, S-1202, S-1207, S-2299 e S-2399

* Excluída a validação do campo {indRRA}, conforme print abaixo:

3) Eventos S-1200, S-2299 e S-5001

* Incluído no campo {tpAcConv} o tipo de acordo "I - Sentença judicial (exceto reclamatória trabalhista)".

No produto esse tipo de acordo é visualizado em  RH | Folha de Pagamento | eSocial | Acordo Coletivo / Reajuste por Lei.

  

4) Evento S-2230 - Afastamento

* Alterada a validação do campo {dtInicio}, conforme abaixo:

5) Tabela 18 -  Motivos de Afastamento

* Alterada a descrição dos códigos de motivo de afastamento [41, 42], conforme abaixo:

De:

Para:

No produto esse ajuste encontra-se em RH | Folha de Pagamento | configurações | Parametrizador | 06.07 - eSocial | 06.07.02 - De/Para. Etapa 1: De/Para de Afastamento.

6) Tabela 19 - Motivos de Desligamento

* Alterada a descrição do código de motivo de desligamento 40, conforme abaixo:

De:

Para:

No produto esse ajuste encontra-se em RH | Folha de Pagamento | configurações | Parametrizador | 06.07 - eSocial | 06.07.02 - De/Para. Etapa 4: De/Para de Desligamento.

7) Tabela 24 - Agentes Nocivos e Atividades - Aposentadoria Especial

No produto esse ajuste encontra-se em RH | Segurança e saúde ocupacional | PPRA / PGR | Tipos de agentes.

* Alterada a descrição do código 02.01.014, conforme abaixo:

De:

Para:

8) Tabela 25 - Tipos de Benefícios

* Incluído o código "0605 - Pensão por morte - Plano próprio".

No produto esse ajuste encontra-se em RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Dados do Benefício.

9) Tabela 27 - Procedimentos Diagnósticos 

* Excluídos os códigos: [0353, 0628, 0829].

No produto esse ajuste encontra-se em RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Anexos | Segurança e Medicina | Consultas Médicas.

Dentro de exames temos as tabelas exemplificadas abaixo:

* Códigos Incluídos.

| Código | Procedimento |
| --- | --- |
| 1433 | Arsênico sanguíneo |
| 1434 | Berílio sanguíneo |
| 1435 | Cálcio sanguíneo |
| 1436 | Cálcio urinário |
| 1437 | Citopatologia |
| 1438 | Ferro urinário |
| 1439 | Formaldeído sanguíneo |
| 1440 | Formaldeído urinário |
| 1441 | Glicose urinária |
| 1442 | Magnésio sanguíneo |
| 1443 | Magnésio urinário |
| 1444 | Mamografia |
| 1445 | Mapeamento de retina (oftalmoscopia indireta) |
| 1446 | Níquel sanguíneo |
| 1447 | Procedimento diagnóstico em citopatologia cérvico-vaginal oncótica |
| 1448 | Radiografia de tórax em duas incidências |
| 1449 | Videolaringoscopia |

* Descrições Alteradas.

De:

| Código | Procedimento |
| --- | --- |
| 0095 | Ácido delta aminolevulínico |
| 0613 | Ferro sérico |
| 1393 | Zinco |

Para:

| Código | Procedimento |
| --- | --- |
| 0095 | Ácido delta aminolevulínico (ALA-U) |
| 0613 | Ferro sérico (sangue) |
| 1393 | Zinco sanguíneo |

10) Evento S-2500 - Processo Trabalhista

* Alterada a condição do grupo {dependente}, conforme abaixo:

De:

Para:

* Alterada a condição do grupo {mudCategAtiv}, conforme abaixo:

De:

Para:

* Alterada a condição do grupo {idePeriodo}, conforme abaixo:

De:

Para:

11) Evento S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador

* Alterada a descrição do campo {tpRegPrev}, conforme abaixo:

De:

Para:

No produto esse ajuste encontra-se em RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Edite o cadastro do funcionário e clique na aba Situação:

* Alterada a descrição do valor 3 do campo {tpProv}, conforme abaixo:

De:

Para:

No produto esse ajuste encontra-se em: RH | Folha de Pagamento | Administração de Pessoal | Funcionários

Edite o cadastro do funcionário e clique na aba Situação:

12) Evento S-2206 - Alteração de Contrato de Trabalho/Relação Estatutária

* Alterada a condição do Grupo {infoRegimeTrab}, conforme abaixo:

De:

Para:

13) Eventos S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início e  S-2306 - Trabalhador Sem Vínculo de Emprego/Estatutário - Alteração Contratual

* Alterada a descrição do campo {infoDirigenteSindical/tpRegPrev}, conforme abaixo:

No produto esse ajuste encontra-se em RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Edite o cadastro do funcionário e clique na aba Dados do Sindicato:

* Alterada a descrição do campo {infoTrabCedido/tpRegPrev}, conforme abaixo:

No produto esse ajuste encontra-se em RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Edite o cadastro do funcionário e clique na aba Registro.

* Alterada a descrição do campo {infoMandElet/tpRegPrev}, conforme abaixo:

No produto esse ajuste encontra-se em RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Edite o cadastro do funcionário e clique na aba Registro.

14) Tabela 03 - Natureza das Rubricas da Folha de Pagamento

* Incluído os códigos: [1016, 1017, 1018, 1019]
* Alterada a descrição do código: [1004]
* Inserido término de validade para os códigos: [1020, 1021].

* Incluído os códigos:

| Código | Nome da Natureza da Rubrica |
| --- | --- |
| 1016 | Férias |
| 1017 | Terço constitucional de férias |
| 1018 | Férias - Abono ou gratificação de férias superior a 20 dias |
| 1019 | Terço constitucional de férias - Abono ou gratificação de férias superior a 20 dias |

* Alterada a descrição do código

De:

| Código | Nome da Natureza da Rubrica |
| --- | --- |
| 1004 | Horas extraordinárias - Indenização de banco de horas |

Para:

| Código | Nome da Natureza da Rubrica |
| --- | --- |
| 1004 | Horas extraordinárias - Banco de horas |

No produto esse ajuste encontra-se em RH | Folha de Pagamento | Administração de Pessoal | Eventos | Eventos | Edite o cadastro do evento:

* **Códigos Excluídos:**

Para os códigos excluídos [1020, 1021], ao inserir um evento/verba, estas naturezas de rubricas não ficarão disponíveis no cadastro.

Ao alterar um evento e colocar estas naturezas de rubricas será exibida uma mensagem de erro informando que estas rubricas se encontram expiradas.

No produto esse ajuste encontra-se em RH | Folha de Pagamento | Administração de Pessoal | Eventos | Eventos.

Edite o cadastro do evento

15) Tabela 07 - Tipos de Dependente

* Excluído o tipo "4 - Filho(a) ou enteado(a), universitário(a) ou cursando escola técnica de 2º grau".

No produto esse ajuste encontra-se em RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Dependentes.

Ao cadastrar com a parametrização abaixo o xml era gerado com o tipo 4 - Filho(a) ou enteado(a), universitário(a) ou cursando escola técnica de 2º grau, com a implementação da nota tecnica passa a ser gerado com o Tipo 3 - Filho(a) ou enteado(a).

De:

Para:

16) Tabela 18 - Motivos de Afastamento

* Alterada a descrição dos códigos: [05, 10].

De:

| Código | Decrição |
| --- | --- |
| 05 | Afastamento/licença de servidor público prevista em estatuto, sem remuneração |
| 10 | Afastamento/licença de servidor público prevista em estatuto, com remuneração |

Para:

| Código | Decrição |
| --- | --- |
| 05 | Afastamento/licença de servidor público ou militar prevista em estatuto, sem remuneração |
| 10 | Afastamento/licença de servidor público ou militar prevista em estatuto, com remuneração |

No produto esse ajuste encontra-se em RH | Folha de Pagamento | configurações | Parametrizador | 06.07 - eSocial | 06.07.02 - De/Para. Etapa 1: De/Para de Afastamento.
