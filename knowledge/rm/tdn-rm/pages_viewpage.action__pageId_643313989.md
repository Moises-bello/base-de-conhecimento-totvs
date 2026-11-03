---
content_hash: 2dab47ba0016a81d32b18fa85410a8d5ba890bd9178dc198f0b7212fd0f12184
fetched_at: '2026-06-29T00:11:10.311653+00:00'
page_id: '643313989'
product: rm
source: tdn-rm
title: S-2206 - Alteração de Contrato de Trabalho / Relação Estatutária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=643313989
version: 16
---

false

**A partir das Versões:**

* 12.1.33.259
* 12.1.34.158
* 12.1.2205.103
* e Superiores

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2206 para atender ao leiaute do eSocial, versão S-1.0, para o grupo 4.

---

11AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

2S-2206 - AlteraçõesS-2206 - Alterações

1) Em Funcionários | Aba Registro e Funcionários | Anexo Histórico de Função, foi criado o parâmetro "**Considerar como Função /Emprego/ Cargo Acumulável**", para a situação onde o funcionário possui cargo, emprego ou função acumulável, conforme solicitado no grupo de Informações do contrato de trabalho do leiaute.

**ATENÇÃO:**

Este parâmetro somente será considerado se a Natureza Jurídica do declarante for igual a 1XX-X ,201-1 ou 203-8.

3S-2206 - XMLS-2206 - XML

Foram necessárias algumas alterações na geração do XML para atender os clientes do grupo 4, sendo elas:

1) Tag <**nmCargo**>: Implementada a validação: Preenchimento obrigatório, exceto se for relativo a servidor nomeado em cargo em comissão (tpRegTrab = [2] e tpProv = [2]);

2) Tag <**nmFuncao>**: Implementada a validação: Preenchimento obrigatório se for relativo a servidor nomeado em cargo em comissão (tpRegTrab = [2] e tpProv = [2]);

3) No grupo infoCeletist implementada a validação: O (se tpRegTrab = [1]); N (nos demais casos);

4) Criado o grupo infoEstatutario (O (se tpRegTrab = [2])). Veja mais detalhes na próxima aba "Estatutário".

4EstatutárioEstatutário11Tipo de funcionário EstatutarioTipo de funcionário Estatutario

Acessar o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Registro

1) Preencher com as informações necessárias para geração do grupo <infoEstatutario> do leiaute:

**ATENÇÃO:**

Esta aba somente ficará visível quando o funcionário for do tipo Estatutário e possuir uma das categorias: 301, 302, 303, 306, 307, 309, 310 ou 312.

2) Após o preenchimento dos dados, o XML será gerado com as informações do grupo <InfoEstatutário>.

2Tipo de regime trabalhista EstatutarioTipo de regime trabalhista Estatutario

Acessar o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Registro

1) Preencher com as informações necessárias para geração do grupo <infoEstatutario> do leiaute:

**ATENÇÃO:**

Esta aba somente ficará visível quando o funcionário for do tipo de regime trabalhista Estatutário/legislações específicas e possuir uma das categorias: 301, 302, 303, 306, 307, 309, 310 ou 312.

2) Após o preenchimento dos dados, o XML será gerado com as informações do grupo <InfoEstatutário>.
