---
content_hash: 7d2586e3c5ae1ff5624b64c95d6fd08fea62f85c07d978f7830f89c30e5569b9
fetched_at: '2026-06-29T00:06:11.822755+00:00'
page_id: '203770902'
product: rm
source: tdn-rm
title: eSocial - S2210 (Comunicação de Acidente de Trabalho)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203770902
version: 85
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** | CONSTRUÇÃO E PROJETOS | | |
| **Projeto1** | (A definir) | **IRM1** | (A definir) |
| **Requisito1** | (A definir) | **Subtarefa1** | (A definir) |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** |  |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

# Objetivo

Este documento descreve um conjunto de modificações que serão implementadas no **TOTVS Segurança e Medicina do Trabalho** para que este módulo recupere todas as informações necessárias para integração com o **e-Social**, referentes ao leiaute **S-2210 (Comunicação de Acidente do Trabalho)**.

# **O que é e-Social**

O e-Social é um projeto do Governo Federal que inaugura um sistema eletrônico de coleta de informações trabalhistas, previdenciárias e fiscais de empregadores, que substituirá o atual procedimento de captura dessas informações, realizado atualmente por meios físicos (declarações, formulários, dentre outros). A documentação completa pode ser acessada no site oficial do projeto, no endereço: <https://www.esocial.gov.br/>.

Neste processo, caberá aos empregadores enviar os dados por meio de consumo de **web-services** disponibilizados pelo Governo Federal. Esses serviços são classificados por tipos específicos, denominados eventos, que representam fatos típicos gerados pela relação empregador x empregado. Para cada evento, existe um leiaute que define o esquema XML a ser preenchido pelo empregador com suas respectivas informações. Nesta especificação, trataremos unicamente do evento S-2210, destinado ao envio dos dados referentes à **CAT** (Comunicação de Acidente de Trabalho).

## Atenção

Conforme destacado inicialmente, esta especificação **NÃO** tratará de detalhes relativos ao mecanismo destinado a trocar informações com os web-services do Governo Federal, mas abordará somente as informações a serem recuperadas para o preenchimento do XML referente ao leiaute S-2210 (CAT), indicando quais campos serão modificados ou criados para que todos os dados deste evento possam ser obtidos.

# Definição da Regra de Negócio

| Rotina | Tipo de Operação | Opção de Menu | Regra de Negócio |
| --- | --- | --- | --- |
| Comunicação de Acidente de Trabalho | Alteração | RH > Segurança e Medicina do Trabalho > CAT > Ocorrências Acidente Trabalho | Implementações descritas abaixo, nos itens:   * 1.1. evtCAT * 1.1.2. ideRegistrador * 1.1.5. cat * 1.1.5.2. parteAtingida * 1.1.5.3. agenteCausador |
| Classe:  RM.Smt.Cadastros.SmtOcorrenciaData | Alteração | Não se aplica | Implementações descritas abaixo, no item:   * 1.1.1. evtCAT |
| Classe:  RM.Fop.Dominio.Relatorio.eSocial.Eventos.EventoS2210 | Criação | Não se aplica | Implementações descritas abaixo, no item:   * 1.1.1. evtCAT |
| Tipo Emitente CAT | Criação | RH > Segurança e Medicina do Trabalho > CAT > Tipo Emitente | Implementações descritas abaixo, no item:   * 1.1.5. cat |
| Tipo CAT | Criação | RH > Segurança e Medicina do Trabalho > CAT > Tipo de CAT | Implementações descritas abaixo, no item:   * 1.1.2. ideRegistrador |
| Fontes Geradoras | Alteração | RH > Segurança e Medicina do Trabalho > PPRA > Fontes Geradoras | Implementações descritas abaixo, no item:   * + 1.1.2. ideRegistrador   + 1.1.5.3 agenteCausador |
| Natureza Médica | Alteração | RH > Segurança e Medicina do Trabalho > CAT > Natureza Médica | Implementações descritas abaixo, no item:   * 1.1.5.4. atestado |

As informações do leiaute S-2210, são distribuídas de forma hierárquica por meio dos seguintes grupos:

| Nível | Nome | Descrição | Condição | Ocorrência |
| --- | --- | --- | --- | --- |
| 1. | eSocial | Agrupador Geral | Obrigatório | Somente 1 registro |
| 1.1. | evtCAT | Evento de Comunicação de Acidente de Trabalho | Obrigatório | Somente 1 registro |
| 1.1.1. | ideEvento | Informações de Identificação do Evento | Obrigatório | Somente 1 registro |
| 1.1.2. | ideRegistrador | Informações de Identificação do registrador da CAT | Obrigatório | Somente 1 registro |
| 1.1.3. | ideEmpregador | Informações de Identificação do empregador | Obrigatório | Somente 1 registro |
| 1.1.4. | ideTrabalhador | Informações de Identificação do Trabalhador | Obrigatório | Somente 1 registro |
| 1.1.5. | cat | Comunicação de Acidente de Trabalho | Obrigatório | Somente 1 registro |
| 1.1.5.1. | localAcidente | Local do Acidente | Obrigatório | Somente 1 registro |
| 1.1.5.2. | parteAtingida | Parte do Corpo Atingida | Obrigatório | No mínimo 1 registro e no máximo 99 registros |
| 1.1.5.3. | agenteCausador | Agente Causador | Obrigatório | No mínimo 1 registro e no máximo 99 registros |
| 1.1.5.4. | atestado | Atestado Médico | Opcional | Nenhum ou no máximo 1 registro |
| 1.1.5.4.1. | emitente | Médico/Dentista que emitiu o atestado | Obrigatório | Somente 1 registro |
| 1.1.5.5 | catOrigem | CAT de origem | Opcional | Nenhum ou no máximo 1 registro |

## 1. eSocial

Presente em todo evento do e-Social, o agrupador geral constitui um grupo base, que identifica o evento que trata o arquivo XML. Todas as demais informações do evento ficam localizadas dentro deste grupo. Em relação a este, nenhuma implementação será realizada, haja vista que ele é criado automaticamente pela rotina responsável pela geração do XML.

*<eSocial xmlns="[http://www.esocial.gov.br/schema/evt/evtCAT/v02\_01\_00](http://www.esocial.gov.br/schema/evt/evtAdmissao/v02_01_00)">*

```
</eSocial>
```

## 1.1. evtCAT

O grupo de informações **evtCAT** reúne todas as informações relativas à **CAT**. Essas informações são aquelas apresentadas no cadastro de Ocorrências e Acidentes de Trabalho, acessível pelo menu **RH > Segurança e Medicina do Trabalho > CAT > Ocorrências Acidente Trabalho**, e alimenta principalmente a tabela **VOCORRENCIA**.

Toda atualização de dados por meio desta tela, seja inclusão, alteração ou exclusão, irá gerar um evento **S-2210** a ser enviado ao e-Social. Para que isso ocorra, será implementado um **gatilho**, que irá disparar automaticamente essa informação para a ferramenta responsável pela comunicação com o e-Social.

---

*Nota técnica para implementação*

Para que um determinado cadastro dispare o gatilho de um evento para o e-Social, o programador deve substituir a classe ancestral do respectivo data server. Ao invés da classe data ser herança da classe **RMSDataServer**, ela deve ser herança da classe **FopESocialDataServer**.

Após substituir a classe ancestral, o programador deve, ainda, implementar o método: **protected override List<ParametrosGatilhoEsocial> PreencheListaColunasEsocial(DataSet dataSet)**.

No caso da CAT, a classe a ser modificada será a **SmtOcorrenciaData**.

Esse gatilho agendará uma tarefa para a geração do arquivos XML do respectivo evento. Para cada evento, existirá uma classe responsável por recuperar os dados para a geração do arquivo. No caso da CAT, será implementada a classe **RM.Fop.Dominio.Relatorio.eSocial.Eventos.EventoS2210**.

---

Este grupo possui um único campo:

| Id. Leiaute | Nome | Tipo | Tamanho | Ocorrência | Descrição e-Social | Regra de Negócio |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | Id | String | 36 | Obrigatório | Identificação única do evento | VOCORRENCIA.CODCOLIGADA + VOCORRENCIA.CODOCORRENCIA |

E possui 11 grupos de informação (**ideEvento, ideRegistrador, ideEmpregador, ideTrabalhador, cat, localAcidente, parteAtingida, agenteCausador, atestado, emitente, catOrigem**), descritos adiante.

## 1.1.1. ideEvento

Os dados deste grupo são calculados automaticamente pela ferramenta responsável pela geração dos arquivos XML. Possui os seguintes campos:

| Id. Leiaute | Nome | Tipo | Tamanho | Ocorrência | Descrição e-Social | Regra de Negócio |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | indRetif | Numérico | 1 | Obrigatório | Valores (Tipo de arquivo):  1: Arquivo original  2: Arquivo de retificação | Não se aplica. |
| 6 | nrRecibo | String | 40 | Opcional | Número de recibo do arquivo a ser retificado (se indRetif = 2) | Não se aplica. |
| 7 | tpAmb | Numérico | 1 | Obrigatório | Valores (Tipo de ambiente):  1: Produção  2: Pré-produção (dados reais)  3: Pré-produção (dados fictícios) | Não se aplica. |
| 8 | procEmi | Numérico | 1 | Obrigatório | Valor (Tipo de emissão):  1: Emitido pelo aplicativo do empregador | Não se aplica. |
| 9 | verProc | String | 20 | Obrigatório | Versão do aplicativo do empregador | Não se aplica. |

## 1.1.2. ideRegistrador

Os dados deste grupo são originados na tabela **VOCORRENCIA**, manipulada pelo formulário de cadastro de CAT, sendo distribuídos nos seguintes campos:

| Id. Leiaute | Nome | Tipo | Tamanho | Ocorrência | Descrição e-Social | Regra de Negócio |
| --- | --- | --- | --- | --- | --- | --- |
| 11 | tpRegistrador | Numérico | 2 | Obrigatório | Valores (Responsável pelo registro da CAT):  1: Empregador  2: Cooperativa  3: Sindicato de trabalhadores avulsos  4: Órgão Gestor de Mão de Obra  5: Empregado  6: Dependente de empregado  7: Entidade Sindical  8: Médico Assistente  9: Autoridade Pública | VOCORRENCIAEMITENTEESOCIAL.CODIGO (Convertido para inteiro, vide nota técnica a seguir) |
| 12 | tpInsc | Numérico | 1 | Opcional | Se tpRegistrador for diferente de "1", indica o tipo de inscrição:  1: CNPJ  2: CPF | VOCORRENCIA.EMITENTETIPOINSCRICAO (vide nota técnica a seguir) |
| 13 | nrInsc | String | 15 | Opcional | Se tpInsc foi informado, contém o CPF ou CNPJ do responsável pelo registro da CAT | VOCORRENCIA.EMITENTECPFCNPJ (vide nota técnica a seguir) |

---

*Nota técnica para implementação*

O campo **Emitente** atualmente realiza uma pesquisa de itens existentes em uma lista fixa (Tabela Dinâmica: **GCONSIST**). A partir desta implementação esta pesquisa será realizada em uma nova tabela **VOCORRENCIAEMITENTE**.

Esta nova tabela **VOCORRENCIAEMITENTE** conterá os seguintes campos:

* Código [**CODIGO**, varchar(10), obrigatório, chave primária, auto incremental]
* Descrição [**DESCRICAO**, varchar(70), obrigatório, único]
* ESocial [**ESOCIAL** varchar(10), obrigatório, lookup (vide descrição abaixo)]

O campo **VOCORRENCIAEMITENTE.ESOCIAL** corresponderá a um relacionamento (lookup) com um campo de uma outra nova tabela a ser criada, **VOCORRENCIAEMITENTEESOCIAL.CODIGO**. A estrutura desta nova tabela **VOCORRENCIAEMITENTEESOCIAL** será descrita adiante.

Para a tabela **VOCORRENCIAEMITENTE** será disponibilizada uma tela de cadastro (**CRUD**) no menu **RH > Segurança e Medicina do Trabalho > CAT > Tipo Emitente** e será controlado pela seguinte diretiva de segurança **RH > Serviços Globais > Segurança > Perfis > Sistema: Segurança e Medicina do Trabalho > Acesso a Menus > Segurança e Medicina do Trabalho > [05] CAT > [05.01] Acidente de Trabalho > [05.01.05] Tipo Emitente**.

A tabela **VOCORRENCIAEMITENTE** conterá os seguintes valores iniciais para **BASE VAZIA** (nova instalação):

| Código | Descrição | eSocial |
| --- | --- | --- |
| 00001 | Empregador | 00001 |
| 00002 | Cooperativa | 00002 |
| 00003 | Sindicato de trabalhadores avulsos não portuários | 00003 |
| 00004 | Órgão Gestor de Mão de Obra | 00004 |
| 00005 | Empregado | 00005 |
| 00006 | Dependente do empregado | 00006 |
| 00007 | Entidade Sindical competente | 00007 |
| 00008 | Médico assistente | 00008 |
| 00009 | Autoridade Pública | 00009 |

Para base que já esteja em produção a tabela **VOCORRENCIAEMITENTE** receberá os valores correspondentes aos que constar na tabela dinâmica **GCONSIST** onde **GCONSIST.CODTABELA = "CATEMITE"**, sendo:

* **VOCORRENCIAEMITENTE.CODIGO = GCONSIST.CODCLIENTE**
* **VOCORRENCIAEMITENTE.DESCRICAO = GCONSIST.DESCRICAO**
* **VOCORRENCIAEMITENTE.ESOCIAL = NULL**

A nova tabela **VOCORRENCIAEMITENTEESOCIAL** possuirá os seguintes campos:

* Código [**CODIGO**, varchar(10), obrigatório, chave primária, auto incremental]
* Descrição [**DESCRICAO**, varchar(70), obrigatório, único]

A tabela **VOCORRENCIAEMITENTEESOCIAL** conterá os seguintes valores fixos:

| Código | Descrição |
| --- | --- |
| 00001 | Empregador |
| 00002 | Cooperativa |
| 00003 | Sindicato de trabalhadores avulsos não portuários |
| 00004 | Órgão Gestor de Mão de Obra |
| 00005 | Empregado |
| 00006 | Dependente de empregado |
| 00007 | Entidade Sindical competente |
| 00008 | Médico assistente |
| 00009 | Autoridade Pública |

À tabela **VOCORRENCIA** ainda serão adicionados dois campos:

* **VOCORRENCIA.EMITENTETIPOINSCRICAO** (Tipo de inscrição do Emitente): Indica se o emitente é Pessoa Física ou Jurídica.
* **VOCORRENCIA.EMITENTECPFCNPJ** (CPF ou CNPJ do Emitente)

Estes dois novos campos não serão de preenchimento obrigatório no banco de dados e serão adicionados no cadastro de CAT na aba **Emitente**. No formulário esses dois campos serão de preenchimento obrigatório caso o usuário, no campo **Emitente**, selecione qualquer opção diferente de **Empregador**. Essa validação será adicionada no evento **Salvar** do formulário:

"Você informou para esta CAT um emitente que não é o Empregador. Assim, é necessário preencher também os campos: Tipo de inscrição e CPF/CNPJ do Emitente!"

Por fim, a legenda atual do campo **Emitente** será modificada para **Tipo Emitente**.

Veja o posicionamento sugerido para os campos no Protótipo 1.

---

## 1.1.3. ideEmpregador

Os dados deste grupo são originados na tabela **GCOLIGADA**, a partir da seleção da coligada da CAT (**GCOLIGADA.CODCOLIGADA = VOCORRENCIA.CODCOLIGADA**), sendo distribuídos nos seguintes campos:

| Id. Leiaute | Nome | Tipo | Tamanho | Ocorrência | Descrição e-Social | Regra de Negócio |
| --- | --- | --- | --- | --- | --- | --- |
| 15 | tpInsc | Númerico | 1 | Obrigatório | Valores (Tipo de Empregador):  1: Pessoa Jurídica  2: Pessoa Física | Valor fixo: 1  Obs.: O sistema não possibilita o cadastro de empregadores do tipo Pessoa Física. |
| 16 | nrInsc | String | 15 | Obrigatório |  | GCOLIGADA.CGC |

## 1.1.4. ideTrabalhador

Os dados deste grupo são originados na tabela **PFUNC**, a partir do acidentado da CAT (**PFUNC.CHAPA = VOCORRENCIA.CHAPA**), e também da tabela **PPESSOA**, a partir do código da pessoa (**PPESSOA.CODIGO = PFUNC.CODPESSOA**), sendo distribuídos nos seguintes campos:

| Id. Leiaute | Nome | Tipo | Tamanho | Ocorrência | Descrição e-Social | Regra de Negócio |
| --- | --- | --- | --- | --- | --- | --- |
| 18 | cpfTrab | String | 11 | Obrigatório | Número do CPF | PPESSOA.CPF |
| 19 | nisTrab | String | 11 | Opcional | Código do NIS (PIS ou PASEP ou NIT) | PFUNC.PISPASEP  Obrigatório, se o empregado não for estagiário. |

## 1.1.5. cat

Os dados deste grupo referem-se especificamente às informações do acidente, sendo originados das tabelas **VOCORRENCIA** e **VTIPOOCORRENCIA**, sendo distribuídos nos seguintes campos e grupos:

| Id. Leiaute | Nome | Tipo | Tamanho | Ocorrência | Descrição e-Social | Regra de Negócio |
| --- | --- | --- | --- | --- | --- | --- |
| 21 | dtAcid | Data | 10 | Obrigatório | Data do acidente | VOCORRENCIA.DATAHORA  Formato: AAAA-MM-DD |
| 22 | tpAcid | Numérico | 1 | Obrigatório | Valores (Tipo de Acidente):  1: Típico  2: Doença  3: Trajeto para o local do trabalho ou entre local de trabalho e a residência do empregado | Para VTIPOOCORRENCIA.TIPOACIDENTE:   * Diferente de "2" e diferente de "3", então "1" (Típico) * Igual a "2", então "2" (Doença) * Igual a "3", então "3" (Trajeto) |
| 23 | hrAcid | String | 4 | Opcional | Hora do acidente | VOCORRENCIA.DATAHORA  Formato: HHMM  Preenchimento obrigatório se tpAcid for diferente de "2" (Doença). |
| 24 | hrsTrabAntesAcid | String | 4 | Opcional | Horas trabalhadas antes do acidente | VOCORRENCIA.HORASTRAB  Formato: HHMM  Preenchimento obrigatório se tpAcid for diferente de "2" (Doença). |
| 25 | tpCat | Numérico | 1 | Obrigatório | Valores (Tipo de CAT):  1: Inicial  2: Reabertura  3: Comunicação de Óbito | VOCORRENCIATIPOESOCIAL.CODIGO (Convertido para inteiro, vide nota técnica a seguir) |
| 26 | indCatObito | String | 1 | Obrigatório | Valores (Houve óbito):  S: Sim  N: Não | Para VOCORRENCIA.MORTE:   * Igual a "1", então "S" * Diferente de "1", então "N" |
| 27 | indComunPolicia | String | 1 | Obrigatório | Valores (Houve comunicação à autoridade policial?):  S: Sim  N: Não | Para VOCORRENCIA.REGPOLICIAL:   * Igual a "1", então "S" * Diferente de "1", então "N"   Se tpCat for igual a "3" (Trajeto), este campo será preenchido sempre com "S". |
| 28 | codSitGeradora | Numérico | 9 | Opcional | Valores pré-definidos na Tabela 16 do e-Social | VFONTEGERADORA.CODCLIENTE (Convertido para inteiro, vide nota técnica a seguir) |
| 29 | iniciatCAT | Numérico | 1 | Opcional | Valores (A CAT foi emitida por):  1: Iniciativa do empregador  2: Ordem Judicial  3: Determinação do Órgão Fiscalizador | VOCORRENCIAINICIATIVAESOCIAL.CODIGO (Convertido para inteiro, vide nota técnica a seguir)  Não pode ser preenchido se tpRegistrador for diferente de "1". |
| 30 | observacao | String | 255 | Opcional | Observações | VOCORRENCIA.DESCRICAO  Se o conteúdo superar 255 caracteres, será cortado na posição 252, sendo acrescentado três pontos (...) ao final. |

---

*Nota técnica para implementação*

**1. Tipo CAT**

O campo **Tipo CAT** atualmente realiza uma pesquisa de itens existentes em uma lista fixa (Tabela Dinâmica: **GCONSIST**). A partir desta implementação, esta pesquisa será realizada em uma nova tabela **VOCORRENCIATIPO**.

Esta nova tabela **VOCORRENCIATIPO** conterá os seguintes campos:

* Código [**CODIGO**, varchar(10), obrigatório, chave primária, auto incremental]
* Descrição [**DESCRICAO**, varchar(70), obrigatório, único]
* ESocial [**ESOCIAL** varchar(10), obrigatório, lookup (vide descrição abaixo)]

O campo **VOCORRENCIATIPO.ESOCIAL** corresponderá a um relacionamento (lookup) com um campo de uma outra nova tabela a ser criada, **VOCORRENCIATIPOESOCIAL.CODIGO**. A estrutura desta nova tabela **VOCORRENCIATIPOESOCIAL** será descrita adiante.

Para a tabela **VOCORRENCIATIPO** será disponibilizada uma tela de cadastro (CRUD) no menu **RH > Segurança e Medicina do Trabalho > CAT > Tipo de CAT** e será controlado pela seguinte diretiva de segurança **RH > Serviços Globais > Segurança > Perfis > Sistema: Segurança e Medicina do Trabalho > Acesso a Menus > Segurança e Medicina do Trabalho > [05] CAT > [05.01] Acidente de Trabalho > [05.01.06] Tipo CAT**.

A tabela **VOCORRENCIATIPO** conterá os seguintes valores iniciais para **BASE VAZIA** (nova instalação):

| Código | Descrição | eSocial |
| --- | --- | --- |
| 00001 | Iniciativa do empregador | 00001 |
| 00002 | Ordem judicial | 00002 |
| 00003 | Determinação de órgão fiscalizador | 00003 |

Para base que já esteja em produção, a tabela **VOCORRENCIATIPO** receberá os valores correspondentes aos que constar na tabela dinâmica **GCONSIST** onde **GCONSIST.CODTABELA = "CATTIPO"**, sendo:

* **VOCORRENCIATIPO.CODIGO = GCONSIST.CODCLIENTE**
* **VOCORRENCIATIPO.DESCRICAO = GCONSIST.DESCRICAO**
* **VOCORRENCIATIPO.ESOCIAL = NULL**

A nova tabela **VOCORRENCIATIPOESOCIAL** possuirá os seguintes campos:

* Código [**CODIGO**, varchar(10), obrigatório, chave primária, auto incremental]
* Descrição [**DESCRICAO**, varchar(70), obrigatório, único]

A tabela **VOCORRENCIATIPOESOCIAL** conterá os seguintes valores fixos:

| Codigo | Descrição |
| --- | --- |
| 00001 | Inicial |
| 00002 | Reabertura |
| 00003 | Comunicação de óbito |

**2. Situação Geradora**

O campo **VOCORRENCIA.CODSITUACAOGERA** realiza uma pesquisa na tabela **VPPRAFONTGERA** (mantido pelo cadastro **RH > Segurança e Medicina do Trabalho > PPRA > Fontes Geradoras**), selecionando apenas os itens **VPPRAFONTGERA.TIPO = 2** (**Situação Geradora**). A tabela **VPPRAFONTGERA**, por sua vez, possui o campo **VPPRAFONTGERA.CODESOCIAL**que relaciona com a campo **VFONTEGERADORA.CODCLIENTE**. A tabela **VFONTEGERADORA**representa os dados da chamada **Tabela 16 - Situação Geradora do Acidente de Trabalho** (Pesquisar arquivo "**MOS 2.1 - Anexo III - Tabelas do eSocial.pdf**", na página 42) do eSocial. Para **BASE VAZIA**, serão criados:

* Script para adicionar automaticamente todos os dados da **Tabela 16 do eSocial** na tabela **VFONTEGERADORA**.
* Script para adicionar na tabela **VPPRAFONTGERA** todos registros da **Tabela 16 do eSocial**, relacionando-os com a tabela **VFONTEGERADORA**, com **VPPRAFONTGERA.TIPO = 2**.

Por questões de consistência com possíveis scripts criados anteriormente para manipular estas tabelas, antes de adicionar os registros o script apagará todos os registros existentes na tabela **VPPRAFONTGERA**, que sejam **VPPRAFONTGERA.TIPO = 2**, bem como os existentes na tabela **VFONTEGERADORA**, respectivamente.

**3. Iniciativa**

Será criado o campo **VOCORRENCIA.TIPOINICIATIVA** (Legenda: **Iniciativa,** varchar(10)), que possuirá um relacionamento com uma nova tabela que será criada, **VOCORRENCIAINICIATIVAESOCIAL**. Assim, o usuário deverá, neste campo, escolher um dos valores existentes na tabela **VOCORRENCIAINICIATIVAESOCIAL**, que já será criada com os seguintes valores:

* Código [**CODIGO**, varchar(10), obrigatório, chave primária, auto incremental]
* Descrição [**DESCRICAO**, varchar(70), obrigatório, único]

| Código | Descrição |
| --- | --- |
| 00001 | Iniciativa do empregador |
| 00002 | Ordem Judicial |
| 00003 | Determinação do Órgão Fiscalizador |

---

## 1.1.5.1. localAcidente

Os dados deste grupo são originados na tabela **VOCORRENCIA**, manipulada pelo formulário de cadastro de CAT, sendo distribuídos nos seguintes campos:

| Id. Leiaute | Nome | Tipo | Tamanho | Ocorrência | Descrição e-Social | Regra de Negócio |
| --- | --- | --- | --- | --- | --- | --- |
| 32 | tpLocal | Numérico | 1 | Obrigatório | Valores (Tipo do Local do Acidente):   * 1: Estabelecimento do empregador * 2: Empresa onde o empregado presta serviços * 3: Via pública * 4: Área Rural * 5: Embarcação * 9: Outros | VOCORRENCIALOCALESOCIAL.CODIGO (vide nota técnica a seguir) |
| 33 | dscLocal | String | 80 | Opcional | Especificação do local do acidente (pátio, rampa de acesso, posto de trabalho, etc.) | VOCORRENCIA.LOCALACIDENTE |
| 34 | dscLograd | String | 80 | Opcional | Descrição do logradouro | VOCORRENCIA.LOGRADOUROACIDENTE  Se o conteúdo superar 80 caracteres, será cortado na posição 77, sendo acrescentado três pontos (...) ao final. |
| 35 | nrLograd | String | 10 | Opcional | Número do logradouro | VOCORRENCIA.NUMEROACIDENTE |
| 36 | codMunic | Numérico | 7 | Opcional | Código do Município (IBGE) | (Código da UF) + VOCORRENCIA.CODMUNICIPIOACIDENTE  Código da UF corresponde a lista do IBGE, descrita na nota técnica a seguir) |
| 37 | uf | String | 2 | Opcional | Unidade da Federação | VOCORRENCIA.UFLOCALACIDENTE  Exemplo: MG, RJ, SP... |
| 38 | cnpjLocalAcid | String | 14 | Opcional | CNPJ do local onde ocorreu o acidente ou doença ocupacional | VOCORRENCIA.CNPJLOCALACIDENTE  Será extraído somente os números, sem pontos, traços e barras. |

---

*Nota técnica para implementação*

O campo **Local do Acidente (INSS)** atualmente realiza uma pesquisa de itens existentes em uma lista fixa (Tabela Dinâmica: **GCONSIST**). A partir desta implementação, esta pesquisa será realizada em uma nova tabela, **VOCORRENCIALOCAL**.

Esta nova tabela, **VOCORRENCIALOCAL**, conterá os seguintes campos:

* Código [**CODIGO**, varchar(10), obrigatório, chave primária, auto incremental]
* Descrição [**DESCRICAO**, varchar(70), obrigatório, único]
* ESocial [**ESOCIAL** varchar(10), obrigatório, lookup (vide descrição abaixo)]

O campo **VOCORRENCIALOCAL.ESOCIAL** corresponderá a um relacionamento (lookup) com um campo de uma outra nova tabela a ser criada, **VOCORRENCIALOCALESOCIAL.CODIGO**. A estrutura desta nova tabela **VOCORRENCIALOCALSOCIAL** será descrita adiante.

Para a tabela **VOCORRENCIALOCAL** será disponibilizada uma tela de cadastro (**CRUD**), no menu **RH > Segurança e Medicina do Trabalho > CAT > Tipo Local Acidente** e será controlado pela seguinte diretiva de segurança **RH > Serviços Globais > Segurança > Perfis > Sistema: Segurança e Medicina do Trabalho > Acesso a Menus > Segurança e Medicina do Trabalho > [05] CAT > [05.01] Acidente de Trabalho > [05.01.07] Tipo Local Acidente**.

A tabela **VOCORRENCIALOCAL**, conterá os seguintes valores iniciais para **BASE VAZIA** (nova instalação):

| Código | Descrição | eSocial |
| --- | --- | --- |
| 00001 | Estabelecimento do empregador | 00001 |
| 00002 | Empresa onde o empregado presta serviço | 00002 |
| 00003 | Via pública | 00003 |
| 00004 | Área rural | 00004 |
| 00005 | Embarcação | 00005 |
| 00009 | Outros | 00009 |

Para base que já esteja em produção, a tabela **VOCORRENCIALOCAL** receberá os valores correspondentes aos que constar na tabela dinâmica **GCONSIST** onde **GCONSIST.CODTABELA = "CATTIPOLOC"**, sendo:

* **VOCORRENCIALOCAL.CODIGO** = **GCONSIST.CODCLIENTE**
* **VOCORRENCIALOCAL.DESCRICAO** = **GCONSIST.DESCRICAO**
* **VOCORRENCIALOCAL.ESOCIAL** = **NULL**

A nova tabela **VOCORRENCIALOCALESOCIAL**, possuirá os seguintes campos:

* Código [**CODIGO**, varchar(10), obrigatório, chave primária, auto incremental]
* Descrição [**DESCRICAO**, varchar(70), obrigatório, único]

A tabela **VOCORRENCIALOCALESOCIAL** conterá os seguintes valores fixos:

| Código | Local |
| --- | --- |
| 00001 | Estabelecimento do empregador |
| 00002 | Empresa onde o empregado presta serviço |
| 00003 | Via pública |
| 00004 | Área rural |
| 00005 | Embarcação |
| 00006 | Outros |

**Observação sobre o campo codMunic**

O valor do campo "**codMunic**" deve conter o valor do campo código do município (**VOCORRENCIA.CODMUNICIPIOACIDENTE**), porém deve ser precedido pelo código da UF, utilizado pelo IBGE. Por exemplo: Belo Horizonte = **31**06200 (Consulta: <http://www.ibge.gov.br/home/geociencias/areaterritorial/area.php?nome=BELO+HORIZONTE&codigo=&submit.x=33&submit.y=5>).

Lista de UF do IBGE (<http://www.ibge.gov.br/home/geociencias/areaterritorial/principal.shtm>):

| Código | UF |
| --- | --- |
| 11 | Rondônia |
| 12 | Acre |
| 13 | Amazonas |
| 14 | Roraima |
| 15 | Pará |
| 16 | Amapá |
| 17 | Tocantins |
| 21 | Maranhão |
| 22 | Piauí |
| 23 | Ceará |
| 24 | Rio Grande do Norte |
| 25 | Paraíba |
| 26 | Pernambuco |
| 27 | Alagoas |
| 28 | Sergipe |
| 29 | Bahia |
| 31 | Minas Gerais |
| 32 | Espírito Santo |
| 33 | Rio de Janeiro |
| 35 | São Paulo |
| 41 | Paraná |
| 42 | Santa Catarina |
| 43 | Rio Grande do Sul |
| 50 | Mato Grosso do Sul |
| 51 | Mato Grosso |
| 52 | Goiás |
| 53 | Distrito Federal |

---

## 1.1.5.2. parteAtingida

Os dados deste grupo são originados na tabela **VOCORRENCIAPARTEATINGIDA** (**VOCORRENCIA****.CODCOLIGADA = **VOCORRENCIAPARTEATINGIDA**.CODCOLIGADA AND **VOCORRENCIA**.CODOCORRENCIA = **VOCORRENCIAPARTEATINGIDA**.CODOCORRENCIA**), sendo distribuídos nos seguintes campos:

| Id. Leiaute | Nome | Tipo | Tamanho | Ocorrência | Descrição e-Social | Regra de Negócio |
| --- | --- | --- | --- | --- | --- | --- |
| 40 | codParteAting | Numérico | 9 | Obrigatório | Código da Parte Atingida  Valores pré-definidos na Tabela 16 do e-Social | VOCORRENCIAPARTEATINGIDA.CODNATUREZA |
| 41 | lateralidade | Numérico | 1 | Obrigatório | Valores:   * Não aplicável * Esquerda * Direita * Ambas | VOCORRENCIAPARTEATINGIDA.LATERALIDADE (vide nota técnica a seguir) |

---

*Nota técnica para implementação*

Será criado o campo **VOCORRENCIAPARTEATINGIDA.LATERALIDADE** e será alterado, no cadastro da CAT, o detalhe "**Parte(s) do corpo atingida(s)**", que deixará de ser um componente "LookupMultiRecords" sendo colocado no seu lugar um "grid editável" com três campos:

* Código da Parte do Corpo: **VOCORRENCIA.CODNATUREZA**. Lookup para pesquisa na action SmtNaturezaAction (Tabela: **VOCORRENCIAPARTEATINGIDA**).
* Descrição: **VNATUREZA.NATUREZA** (**VOCORRENCIA.CODNATUREZA = VNATUREZA.CODNATUREZA**). Somente leitura.
* Lateralidade: **VOCORRENCIAPARTEATINGIDA.LATERALIDADE**. Combobox com as opções:
  + Não aplicável
  + Esquerda
  + Direita
  + Ambas

---

## 1.1.5.3. agenteCausador

Os dados deste grupo são originados da tabela **VOCORRENCIAAGENTECAUSADOR** (**VOCORRENCIA.CODCOLIGADA = VOCORRENCIAAGENTECAUSADOR.CODCOLIGADA AND VOCORRENCIA.CODOCORRENCIA = VOCORRENCIAAGENTECAUSADOR.CODOCORRENCIA**), sendo distribuídos nos seguintes campos:

| Id. Leiaute | Nome | Tipo | Tamanho | Ocorrência | Descrição e-Social | Regra de Negócio |
| --- | --- | --- | --- | --- | --- | --- |
| 43 | codAgntCausador | Numérico | 9 | Obrigatório | Valores pré-definidos nas tabela 14 e 15 do e-Social | VAGENTECAUSADOR.CODCLIENTE (vide nota técnica a seguir) |

---

*Nota técnica para implementação*

O campo **VOCORRENCIAAGENTECAUSADOR****.CODFONTEGERA** realiza uma pesquisa na tabela **VPPRAFONTGERA** (mantido pelo cadastro **RH > Segurança e Medicina do Trabalho > PPRA > Fontes Geradoras**), selecionando apenas os itens **VPPRAFONTGERA.TIPO = 1** (**Agente Causador**). A tabela **VPPRAFONTGERA**, por sua vez, possui o campo **VPPRAFONTGERA.CODESOCIAL** que relaciona com a campo **VAGENTECAUSADOR.CODCLIENTE**. A tabela **VAGENTECAUSADOR**representa os dados das chamadas **Tabela 14 - Agente causador do Acidente de Trabalho** e **Tabela 15 - Agente Causador / Situação Geradora de Doença Profissional** (Pesquisar arquivo **MOS 2.1 - Anexo III - Tabelas do eSocial.pdf**, nas páginas 34 e 40 respectivamente) do eSocial. Para **BASE VAZIA**, serão criados:

* Script para adicionar automaticamente todos os dados da **Tabela 14 e da Tabela 15 do eSocial** na tabela **VAGENTECAUSADOR**.
* Script para adicionar na tabela **VPPRAFONTGERA** todos registros da **Tabela 14 e da Tabela 15 do eSocial**, relacionando-os com a tabela **VAGENTECAUSADOR**, com **VPPRAFONTGERA.TIPO = 1**.

Por questões de consistência com possíveis scripts criados anteriormente para manipular estas tabelas, antes de adicionar os registros o script apagará todos os registros existentes na tabela **VPPRAFONTGERA**, que sejam **VPPRAFONTGERA.TIPO = 1**, bem como os existentes na tabela **VAGENTECAUSADOR**, respectivamente.

---

## 1.1.5.4. atestado

Os dados deste grupo são originados nas tabelas **VOCORRENCIA**, **VOCORRENCIANATUREZAMEDICA** e **VNATUREZACAT** (**VOCORRENCIA.CODCOLIGADA = VOCORRENCIANATUREZAMEDICA.CODCOLIGADA AND VOCORRENCIA.COOCORRENCIA = VOCORRENCIANATUREZAMEDICA.COOCORRENCIA AND VOCORRENCIANATUREZAMEDICA.CODNATUREZA = VNATUREZACAT.CODNATUREZA**), manipulada pelo formulário de cadastro de CAT "**aba Atestado**", sendo distribuídos nos seguintes campos:

| Id. Leiaute | Nome | Tipo | Tamanho | Ocorrência | Descrição e-Social | Regra de Negócio |
| --- | --- | --- | --- | --- | --- | --- |
| 45 | codCNES | String | 7 | Opcional | Código da Unidade de Atendimento  (Cadastro Nacional de Estabelecimentos de Saúde do Ministério da Saúde) | VOCORRENCIA.CNES |
| 46 | dtAtendimento | Data | 10 | Obrigatório | Data do Atendimento | VOCORRENCIA.DATAMEDICA  Formato: AAAA-MM-DD |
| 47 | hrAtendimento | String | 4 | Obrigatório | Hora do Atendimento | VOCORRENCIA.DATAMEDICA  Formato: HHMM |
| 48 | indInternacao | String | 1 | Obrigatório | Valores (Foi internado?):  S: Sim  N: Não | Para: VOCORRENCIA.INTERNACAO:   * Igual a "1", então "S" * Diferente de "1", então "N" |
| 49 | durTrat | Numérico | 4 | Obrigatório | Duração do tratamento em quantidade de dias | VOCORRENCIA.DURACAOTRATAMENTO |
| 50 | indAfast | String | 1 | Obrigatório | Valores (Ocorreu afastamento do trabalho?):  S: Sim  N: Não | Para: VOCORRENCIA.AFASTAMENTOTRATAMENTO:   * Igual a "1", então "S" * Diferente de "1", então "N" |
| 51 | dscLesao | Numérico | 9 | Opcional | Valores pré-definidos na Tabela 17 do e-Social | VNATUREZACATESOCIAL.CODIGO (Campo vide nota técnica a seguir) |
| 52 | dscCompLesao | String | 200 | Opcional | Descrição complementar da lesão | VNATUREZACAT.DESCRICAO  Se o conteúdo superar 200 caracteres, será cortado na posição 197, sendo acrescentado três pontos (...) ao final. |
| 53 | diagProvavel | String | 100 | Opcional | Descrição de diagnóstico provável | VOCORRENCIA.DIAGNOSTICO |
| 54 | codCID | String | 5 | Obrigatório | Código da Classificação Internacional de Doenças | VOCORRENCIA.CID |
| 55 | observacao | String | 255 | Opcional | Observação | VOCORRENCIA.OBSERVACAOMEDICA  Se o conteúdo superar 255 caracteres, será cortado na posição 252, sendo acrescentado três pontos (...) ao final. |

---

*Nota técnica para implementação*

**1. Natureza Médica**

No cadastro de Natureza Médica (**RH > Segurança e Medicina do Trabalho > CAT > Natureza Médica**) será adicionado o campo ESocial (**VNATUREZACAT.ESOCIAL**). Este campo irá se relacionar com um campo de uma nova tabela que será criada **VNATUREZACATESOCIAL.CODIGO**.

A nova tabela **VNATUREZACATESOCIAL**, possuirá os seguintes campos:

* Código [**CODIGO**, varchar(10), obrigatório, chave primária, auto incremental]
* Descrição [**DESCRICAO**, varchar(70), obrigatório, único]

A tabela **VNATUREZACATESOCIAL**será criada já contendo os registros equivalentes aos da **Tabela 17 - Descrição da Natureza da Lesão do eSocial**(pesquisar **versão 2.1** da documentação do e-Social, no arquivo "**MOS 2.1 - Anexo III - Tabelas do eSocial.pdf**", na página 44)

**2. Usar eSocial (Lesões)**

Será criado o campo **VOCORRENCIANATUREZAMEDICA.USARESOCIAL** (Boolean) e será alterado no cadastro da CAT na aba "**Atestado Médico**" o detalhe "**Lesão**", que deixará de ser um componente "LookupMultiRecords" sendo colocado no seu lugar um "grid editável" com três campos: 

* Código da Lesão: **VOCORRENCIANATUREZAMEDICA.CODNATUREZA**. Lookup para pesquisa na action **SmtNaturezaCATAction** (Tabela: **VNATUREZACAT**).
* Descrição: **VNATUREZACAT.NATUREZA** (**VOCORRENCIANATUREZAMEDICA.CODNATUREZA = VNATUREZACAT.CODNATUREZA**). Somente leitura.
* Lateralidade: **VOCORRENCIANATUREZAMEDICA.USARESOCIAL**. Combobox com as opções "Sim" e "Não".

Será adicionada uma validação no cadastro de CAT, na aba "Atestado Médico", no detalhe "**Lesão**", impedindo que em uma mesma CAT exista mais de uma lesão e-Social adicionada com o valor do campo "**VOCORRENCIANATUREZAMEDICA.USARESOCIAL = S**", pois somente uma das lesões adicionadas à CAT poderá representar a informação a ser utilizada no e-Social. O usuário será alertado por meio da seguinte mensagem:

"Você já selecionou uma lesão para ser utilizada no e-Social. Para modificar a lesão selecionada para o e-Social você deve primeiramente desfazer a seleção atual!"

---

## 1.1.5.4.1. emitente

Os dados deste grupo são originados da tabela **VOCORRENCIA** e **VPROFISSIONALSAUDE** (**VOCORRENCIA.CODMEDICO = VPROFISSIONALSAUDE.CODIGO**) manipulada pelo formulário de cadastro de CAT "**aba Atestado**", sendo distribuídos nos seguintes campos:

| Id. Leiaute | Nome | Tipo | Tamanho | Ocorrência | Descrição e-Social | Regra de Negócio |
| --- | --- | --- | --- | --- | --- | --- |
| 57 | nmEmit | String | 60 | Obrigatório | Nome do Médico ou Dentista | VPROFISSIONALSAUDE.NOMEPROFISSIONAL |
| 58 | ideOC | Numérico | 1 | Obrigatório | Valores (Órgão de Classe):  1: CRM (Conselho Regional de Medicina)  2: CRO (Conselho Regional de Odontologia) | Para VPROFISSIONALSAUDE.CODORGAOCLASSE:   * Igual a "CRM", então "1" * Igual a "CRO", então "2" |
| 59 | nrOc | String | 14 | Obrigatório | Número de inscrição no órgão de classe | VPROFISSIONALSAUDE.NUMEROREGISTRO |
| 60 | ufOC | String | 2 | Opcional | Sigla da UF do órgão de classe | VPROFISSIONALSAUDE.CODUFREGISTRO |

## 1.1.5.5. catOrigem

Os dados deste grupo são originados da tabela **VOCORRENCIA** manipulada pelo formulário de cadastro de CAT, sendo distribuídos nos seguintes campos:

| Id. Leiaute | Nome | Tipo | Tamanho | Ocorrência | Descrição e-Social | Regra de Negócio |
| --- | --- | --- | --- | --- | --- | --- |
| 62 | dtCatOrig | Data | 10 | Obrigatório | Data da CAT de origem | VOCORRENCIA.DTCATORIGEM  Formato: AAAA-MM-DD |
| 63 | nrCatOrig | String | 40 | Opcional | Número da CAT de origem | VOCORRENCIA.NROCATORIGEM (Modificações a serem implementadas, vide nota técnica a seguir)  O preenchimento deste campo é obrigatório se a data da CAT original for posterior à data de vigência do e-Social. Se informado, deve corresponder número de recibo da CAT do arquivo gerado para a CAT de origem. |

Obs.: Esses dados são gerados somente quando o "**tpCat**" (Tipo de CAT) for igual a "2" (**Reabertura**) ou igual a "3" (**Comunicação de óbito**).

 

---

*Nota técnica para implementação*

Atualmente, na tela do cadastro de CAT (**RH > Segurança e Medicina do Trabalho > CAT > Ocorrências Acidente Trabalho**), quando o usuário seleciona o valor do campo "**Tipo**" igual a "**Reabertura**", dois campos são exibidos na tela para preenchimento: "Data de Cat de Origem" (**DTCATORIGEM**) e Número Cat Origem (**NROCATORIGEM**). A partir desta implementação, um terceiro campo aparecerá seguindo a mesma regra. Será gerado script para criar este novo campo, a ser denominado "**CAT de origem**", que será adicionado à tela conforme sugestão de layout abaixo (Protótipo 1). O campo "CAT de origem" será um lookup do próprio cadastro de CAT, mas somente poderá exibir registros de CAT que **NÃO** sejam do Tipo "**Reabertura**", nem que corresponda ao próprio registro em edição.

As legendas dos dois campos já existentes atualmente para esta regra (**DTCATORIGEM** e **NROCATORIGEM**) serão ajustadas para: "**Data da CAT de origem**" e "**Número do recibo da CAT de origem**", respectivamente. Ainda, estes dois campos passarão a estar desabilitados para edição e seus respectivos valores serão atribuídos automaticamente a partir do registro da CAT selecionada no campo "**CAT de origem**". O valor do campo **NROCARORIGEM** será obtido a partir dos dados de log do mecanismo de gerenciamento do eSocial.

---

# Protótipo

## 1. Tela de Cadastro da CAT **(locais a serem alterados no layout)**

## 2. Tela de Cadastro de Tipo de Lesão (Natureza Médica)

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
