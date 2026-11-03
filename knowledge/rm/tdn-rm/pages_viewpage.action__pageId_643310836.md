---
content_hash: a78b96700e95b377d6f020ddc149fb8cc838b0436ffa24cea80355b2046eb473
fetched_at: '2026-06-29T00:11:10.303741+00:00'
page_id: '643310836'
product: rm
source: tdn-rm
title: S-2200 - Cadastro inicial do Vinculo e Admissão/ingresso e Trabalhador - Órgão
  Público
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=643310836
version: 46
---

false

**A partir das Versões:**

* 12.1.33.259
* 12.1.34.158
* 12.1.2205.103
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2200 para atender ao leiaute do eSocial, versão S-1.0, para o grupo 4.

---

11AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

2S-2200 - CadastroS-2200 - Cadastro

1) Em Funcionários | Aba Registro e Funcionários | Anexo Histórico de Função, foi criado o parâmetro "**Considerar como Função /Emprego/ Cargo Acumulável**", para a situação onde o funcionário possui cargo, emprego ou função acumulável, conforme solicitado no grupo de Informações do contrato de trabalho do leiaute.

**ATENÇÃO:**

Este parâmetro somente será considerado se a Natureza Jurídica do declarante for igual a 1XX-X ,201-1 ou 203-8.

3S-2200 - XMLS-2200 - XML

Foram necessárias algumas alterações na geração do XML para atender os clientes do grupo 4, sendo elas:

1) Tag <**tpRegTrab**>: Implementado a opção 2 para estatutário. Ao incluir um funcionário com o tipo estatutário (PFUNC.CODTIPO = E) este campo será levado com o valor 2. Caso contrário será levado o valor 1;

2) Tag <**infoCota**>: Implementada a validação: Preenchimento obrigatório e exclusivo se tpRegTrab = [1];

3) Tag <**nmCargo**>: Implementada a validação: Preenchimento obrigatório, exceto se for relativo a servidor nomeado em cargo em comissão (tpRegTrab = [2] e tpProv = [2]);

4) Tag <**nmFuncao>**: Implementada a validação: Preenchimento obrigatório se for relativo a servidor nomeado em cargo em comissão (tpRegTrab = [2] e tpProv = [2]);

5) Implementado a tag <**dtIngrCargo**> no grupo infoContrato que buscará o valor do campo "Data de Mudança" do Histórico de Função;

6) No grupo infoCeletist implementada a validação: O (se tpRegTrab = [1]); N (nos demais casos);

7) Criado o grupo infoEstatutario (O (se tpRegTrab = [2])). Veja mais detalhes na próxima aba "Estatutário".

8) Tag <**dtIniAfast**>: Implementada a validação: Não informar se tpAdmissao = [1] ou se tpProv for diferente de [5, 8, 10].

4EstatutárioEstatutário11Tipo de funcionário EstatutarioTipo de funcionário Estatutario

Acessar o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Registro

1) Preencher com as informações necessárias para geração do grupo <infoEstatutario> do leiaute:

**ATENÇÃO:**

Esta aba somente ficará visível quando o funcionário for do tipo Estatutário e possuir uma das categorias: 301, 302, 303, 306, 307, 309, 310 ou 312.

2) Após o preenchimento dos dados, o XML será gerado com as informações do grupo <InfoEstatutário>.

2Tipo de regime trabalhista EstatutarioTipo de regime trabalhista Estatutario

Acessar o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Registro

1) Preencher com as informações necessárias para geração do grupo <infoEstatutario> do leiaute:

**ATENÇÃO:**

Esta aba somente ficará visível quando o funcionário for do tipo de regime trabalhista Estatutário/legislações específicas e possuir uma das categorias: 301, 302, 303, 306, 307, 309, 310 ou 312.

2) Após o preenchimento dos dados, o XML será gerado com as informações do grupo <InfoEstatutário>.

3-2Carga InicialCarga Inicial

Acessar o menu RH | Folha de Pagamento | eSocial | Gerar Gatilhos Eventos Iniciais

Deverá selecionar a "2a. Fase" e selecionar o evento "S-2200".

**ATENÇÃO:**

Para gerar o gatilho com status carga inicial o sistema irá verificar se a data de admissão do funcionário é anterior a data dos "Não Periódicos" ou caso o campo "Economia Mista" esteja marcado o sistema irá considerar a data do campo "Não Periódicos" da economia mista, existem no Parametrizador.
