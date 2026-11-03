---
content_hash: d696ad3aed060e60945ea47e85de9568bf03e71017ce6bec452c30cd9682e015
fetched_at: '2026-06-29T00:08:49.373009+00:00'
page_id: '330140380'
product: rm
source: tdn-rm
title: DT eSocial - Leiaute 2.4.01
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+eSocial+-+Leiaute+2.4.01
version: 7
---

**Releases: 12.1.17.215 , 12.1.18.143 e 12.1.19.101, ou acima.**

**ATENÇÃO:**

Para liberação da adequação ao leiaute 2.4.01 do eSocial foram criados campos em alguns cadastros da Folha de Pagamento, com isso, a partir destes patchs 12.1.17 e 12.1.18 será OBRIGATÓRIO a execução do Atualizador para acessar o módulo de Folha de Pagamento.

Observação: Favor executar primeiramente em base de **Homologação.**

Segue Link do TDN, caso tenha dúvidas sobre a execução desse Script via RM.Atualizador: <http://tdn.totvs.com/pages/releaseview.action?pageId=322143046>

A partir dessa versão o sistema passa verificar o parâmetro “Data de obrigatoriedade / Adesão ao eSocial” existente **no Parametrizador | eSocial** nos seguintes processos:

* **Fila de Eventos**
* **Gerar XML**
* **Integrar com o TAF**

Veja detalhes no help: <http://wikihelp.totvs.com.br/WikiHelp/FOP/Fop.ConfiguracoesGerais1.aspx>

**Aviso Prévio e Aviso Prévio Coletivo**

Implementado o tipo de demissão “V - Comum acordo”.

Veja detalhes em <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.AvisoPrevio.aspx>

**eSocial | Preencher Categoria eSocial**

Implementado o processo.

Veja mais detalhes em: <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.PreencherCategoriaeSocial.aspx>

**eSocial | Carga Inicial Funcionários Demitidos**

Implementado o processo carga inicial para funcionários demitidos.

Veja detalhes em <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.CargaInicialFuncionariosDemitidos.aspx>

**eSocial | Informações do Empregador**

Implementado CPF do Empregador e Data de encerramento da empresa.

Veja detalhes em: [http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.InformaçaoEmpregador.aspx](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.Informa%C3%A7aoEmpregador.aspx)

**eSocial | Outros Processos | Encerrar Atividades da Empresa**

Implementado o processo para encerramento da atividade da empresa junto ao eSocial.

Veja detalhes em: <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.EncerrarAtividadeEmpresa.aspx>

**eSocial | Gerar Gatilhos Eventos Iniciais**

O processo será divido em duas fases conforme definição do eSocial.

Veja detalhes em: <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.GerarGatilhosIniciais.aspx>

**eSocial | Integração com o TAF**

Veja mais detalhes em: <http://wikihelp.totvs.com.br/WikiHelp/FOP/Fop.IntegracaoTAF.aspx>

**eSocial | Validador da Base de Dados**

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.ValidadordaBasedeDados.aspx>

**Parametrizador | eSocial**

A aba “Configurações Gerais” foi desmembrada em duas abas: “Configurações Gerais 1/2” e “Configurações Gerais 2/2”. E foram implementado/alterado os parâmetros abaixo:

Data da Obrigatoriedade/Adesão ao eSocial

Desmembrada a data conforme faseamento do eSocial.

Gerar Gatilhos Iniciais por Evento

Implementada a possibilidade de gerar carga inicial selecionando o evento desejado.

Não gerar aviso para registro não obrigatório quando desconsiderado no XML

Gerar erro de preenchimento para registro não obrigatório quando tiver algum campo preenchido

Prefixo eventos de Tabelas

Veja detalhes destas implementações em:

<http://wikihelp.totvs.com.br/WikiHelp/FOP/Fop.ConfiguracoesGerais1.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/Fop.ConfiguracoesGerais2.aspx>

Seções a Desconsiderar

Possibilidade de informar as seções que serão desconsideradas na geração dos eventos: “[S-1005 - Tabela de Estabelecimentos e Obras](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S1020.aspx) e [S-1020 - Tabela de Lotações Tributárias](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S1020.aspx)”.

<http://wikihelp.totvs.com.br/WikiHelp/FOP/Fop.SecoesDesconsiderar.aspx>

Eventos de Tabelas

Todos os eventos de tabela do eSocial possuem um atributo de vigência ou "Período de validade das informações".

Veja detalhes em: <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.EventosDeTabelas.aspx>

Filiais (RM x TAF)

Implementado a possibilidade do usuário mapear as filiais com RM com as filiais do TAF.

Veja detalhes em: <http://wikihelp.totvs.com.br/WikiHelp/FOP/Fop.FiliaisRMxTAF.aspx>

**Adequação e Inclusão na importação do Labore**

Veja mais detalhes em:

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.LayoutsImportacao.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.LayoutFuncDadosCad.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.LayoutSecoes.aspx>

**Ajustes nos mapeamentos dos eventos abaixo:**

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S1005.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S1010.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S1020.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S1070.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S1200.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S1210.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S1299.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2200.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2205.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2206.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2210.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2230.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2250.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2299.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2300.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2306.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2399.aspx>
