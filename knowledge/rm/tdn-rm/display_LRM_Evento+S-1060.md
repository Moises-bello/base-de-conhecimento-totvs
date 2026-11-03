---
content_hash: 1941192c93e656b74cff208b83aa54e10f51aa0570d8cb719d56337c7117d666
fetched_at: '2026-06-29T00:08:56.093238+00:00'
page_id: '351376171'
product: rm
source: tdn-rm
title: Evento S-1060
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1060
version: 6
---

Leiautestrue2Leiaute 2.5.00

Mapeamento dos campos para o leiaute 2.5.00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro\_eSocial** | **Campo\_eSocial** | **Tabela\_RM** | **Coluna\_RM** | **Informações\_do\_calculo** |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideAmbiente | codAmb | VAMBIENTETRABALHO | CODIGO |  |
| ideAmbiente | iniValid |  |  | Se o tipo da operação for Carga Inicial, retorna a data de obrigatoriedade parametrizada, caso contrário, retorna a competência atual. |
| ideAmbiente | fimValid |  |  |  |
| dadosAmbiente | nmAmb | VAMBIENTETRABALHO | NOMEAMBIENTE |  |
| dadosAmbiente | dscAmb | VAMBIENTETRABALHO | DESCRICAO |  |
| dadosAmbiente | localAmb |  |  | Valores válidos:   1 - Estabelecimento do próprio empregador;   2 - Estabelecimento de Terceiros;   3 - Prestação de Serviço Externo; |
| dadosAmbiente | tpInsc |  |  | Caso VAMBIENTETRABALHO.TIPO seja "Prestação de Serviço", o valor do campo será originado do preenchimento do campo Tipo inscrição na aba "Dados eSocial Terceiros". Caso VAMBIENTETRABALHO.TIPO seja "Posto de Trabalho" ou "Local de Trabalho", considera a SEÇÃO centralizadora da filial selecionada no cadastro do "Posto de Trabalho" ou "Local de Trabalho" (VPOSTOTRABALHO.CODFILIAL ou VLOCALTRABALHO.CODFILIAL);  Caso VAMBIENTETRABALHO.TIPO seja "Seção" ou "Lotação", considera a própria SEÇÃO selecionada (VAMBIENTETRABALHO.CODSECAO);    Com a SEÇÃO encontrada então:    Caso PSECAO.CAEPF esteja preenchido retorna "3 - CAEPF (Cadastro de Atividade Econômica   de Pessoa Física)";  Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ". |
| dadosAmbiente | nrInsc |  |  | Caso VAMBIENTETRABALHO.TIPO seja "Prestação de Serviço", o valor do campo será originado do preenchimento do campo Número Inscrição na aba "Dados eSocial Terceiros". Caso VAMBIENTETRABALHO.TIPO seja "Posto de Trabalho" ou "Local de Trabalho", considera a SEÇÃO centralizadora da filial selecionada no cadastro do "Posto de Trabalho" ou "Local de Trabalho" (VPOSTOTRABALHO.CODFILIAL ou VLOCALTRABALHO.CODFILIAL);  Caso VAMBIENTETRABALHO.TIPO seja "Seção" ou "Lotação", considera a própria SEÇÃO selecionada (VAMBIENTETRABALHO.CODSECAO);    Com a SEÇÃO encontrada então:    Caso tpInsc seja 1: retorna valor do campo PSECAO.CGC;  Caso tpInsc seja 3: retorna valor do campo PSECAO.CAEPF. |
| dadosAmbiente | codLotacao | VAMBIENTETRABALHO | CODLOTACAOTRIBUTARIA |  |
| novaValidade | iniValid |  |  |  |
| novaValidade | fimValid |  |  | Campo será preenchido com a data de encerramento informada ao executar o processo de Encerrar Atividades da Empresa. |
