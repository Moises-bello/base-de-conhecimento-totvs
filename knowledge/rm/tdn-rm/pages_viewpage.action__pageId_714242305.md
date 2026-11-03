---
content_hash: fd64818f954cb83aa5996038e7d7270d5a659127825daaf05c820b65be6b94d0
fetched_at: '2026-06-29T00:11:25.666014+00:00'
page_id: '714242305'
product: rm
source: tdn-rm
title: Relatório de Conferência INSS Patronal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=714242305
version: 53
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Esta funcionalidade têm como objetivo apoiar na identificação de possíveis divergências entre os valores de INSS calculados utilizando as incidências dos eventos/verbas existentes no envelope de pagamento com o valores retornados do RET através do evento S-5011, auxiliando também na conferência dos valores de: Segurados, Deduções Salário Família e Maternidade da DARF de INSS.

Os dados apresentados são originados da comparação dos valores de INSS encontrados na Folha de pagamento contra os valores retornados pelo Governo através do evento S-5011-Informações das Contribuições Sociais Consolidadas por Contribuinte.

## **02. EXEMPLO DE UTILIZAÇÃO**

11Parametrização TAF FULLParametrização TAF FULL

**1)** Acesse o menu Configurações | Parametrizador | eSocial | Configurações Gerais | Integração com TAF | Outros parâmetros

Informe o servidor e porta que serão utilizados para execução desses serviços

**Servidor/Porta API**: Servidor e porta onde o serviço de API"s RM está sendo executado. (**APiPort** do Host RM. No caso onde a ApiPort não foi discriminada nas configurações do Host, utilizar a HttpPort).   
**Servidor/Porta APP:** Servidor e porta onde o aplicativo THF está sendo executado. (Caso o servidor seja o Host RM, informar a **HttpPort**).

Verique a configuração do **DefaultDB**. Informações em : [Configurando DefaultDB](https://tdn.totvs.com/display/LRM/Configurando+DefaultDB)

Para maiores informações sobre a configuração da **HttpPort** e **ApiPort**, acesse: [O que é e como configurar a HttpPort e ApiPort](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633-RM-Integra%C3%A7%C3%B5es-O-que-%C3%A9-e-como-configurar-a-HttpPort-e-ApiPort-).

**OBSERVAÇÃO: Se estiver executando o RM.Host.exe, o mesmo deve ser executado com administrador.**

  

**2)** Acesse o menu Serviços Globais| Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em Acesso a Menus e permita o acesso 09.06.02 - Conferência INSS DCTFWEB

**3)** Acesse o menu Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Encargos Sociais

Marque os parâmetros "Habilita Histórico de INSS no Cadastro de Seção" e "Discriminar Percentual de Terceiros":

**4)**Acesse o menu Serviços Globais | Segurança | Perfis | Folha de Pagamento

Edite o perfil desejado, vá em **Acesso a Menus** e permita o acesso aos seguintes itens:

* **01.01.113.07.01 - Histórico de Percentuais para INSS: Executar**
* **01.01.113.07.02 - Histórico de Percentuais para INSS: Incluir**
* **01.01.113.07.03 - Histórico de Percentuais para INSS: Excluir**
* **01.01.113.07.04 - Histórico de Percentuais para INSS: Editar**

 

**5)** Acesse o menu Administração de Pessoal | Seções

Selecione a seção centralizadora e abra o anexo "Histórico de Percentuais de INSS" e edite o cadastro, conforme demonstrado abaixo:

Nesta tela cadastre os dados dos percentuais, conforme demonstrado abaixo:

Acesse aba "Percentuais de Terceiros" e cadastre os valores discriminados conforme cada código da receita. Esses códigos são conforme descrito na tabelas códigos de receita do manual da DCTFWEB.

falseATENÇÃO!

A partir das versões citadas no [documento técnico](https://tdn.totvs.com/pages/viewpage.action?pageId=842272518), é possível realizar o cadastro de **percentuais de terceiros** considerando a quebra de FPAS informada em Parametrizador | eSocial | Lotação Tributária.

Para que o relatório funcione adequadamente, é essencial realizar a atualização da versão do TAF. Isso permitirá a obtenção dos totalizadores após o encerramento do processo. Importante ressaltar que essa atualização não afetará a visualização do evento S-1299 na fila de eventos, pois o retorno correspondente será automaticamente registrado no banco de dados.IMPORTANTE!

2Parametrização MiddlewareParametrização Middleware

**1)** Acesse o menu Configurações | Parametrizador | eSocial | Configurações Gerais | Integração com Middleware | Outros parâmetros

Informe o servidor e porta que serão utilizados para execução desses serviços.

**Servidor/Porta API**: Servidor e porta onde o serviço de API"s RM está sendo executado. (**APiPort** do Host RM. No caso onde a ApiPort não foi discriminada nas configurações do Host, utilizar a HttpPort).   
**Servidor/Porta APP:** Servidor e porta onde o aplicativo THF está sendo executado. (Caso o servidor seja o Host RM, informar a **HttpPort**).

Para maiores informações sobre a configuração da **HttpPort** e **ApiPort**, acesse: [O que é e como configurar a HttpPort e ApiPort](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633-RM-Integra%C3%A7%C3%B5es-O-que-%C3%A9-e-como-configurar-a-HttpPort-e-ApiPort-).

**OBSERVAÇÃO: Se estiver executando o RM.Host.exe, o mesmo deve ser executado com administrador.**

**2)** Acesse o menu Serviços Globais| Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em Acesso a Menus e permita o acesso 09.06.02 - Conferência INSS DCTFWEB

**3)** Acesse o menu Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Encargos Sociais

Marque os parâmetros "Habilita Histórico de INSS no Cadastro de Seção" e "Discriminar Percentual de Terceiros":

**4)** Acesse o menu Serviços Globais | Segurança | Perfis | Sistema Folha de Pagamento

Edite o perfil desejado, vá em **Acesso a Menus** e permita o acesso aos seguintes itens:

* **01.01.113.07.01 - Histórico de Percentuais para INSS: Executar**
* **01.01.113.07.02 - Histórico de Percentuais para INSS: Incluir**
* **01.01.113.07.03- Histórico de Percentuais para INSS: Excluir**
* **01.01.113.07.04 - Histórico de Percentuais para INSS: Editar**

**5)** Acesse o menu Administração de Pessoal | Seções

Selecione a seção centralizadora e abra o anexo "Histórico de Percentuais de INSS" edite o cadastro, conforme demonstrado abaixo:

Nesta tela cadastre os dados do percentuais patronais e acidente de trabalho

Acesse aba "Percentuais de Terceiros" e cadastre os valores discriminados conforme cada código da receita. Esses códigos são conforme descrito na tabelas códigos de receita do manual da DCTFWEB.

falseATENÇÃO!

A partir das versões citadas no [documento técnico](https://tdn.totvs.com/pages/viewpage.action?pageId=842272518), é possível realizar o cadastro de **percentuais de terceiros** considerando a quebra de FPAS informada em Parametrizador | eSocial | Lotação Tributária.

true3Relatório de Conferência INSS PatronalRelatório de Conferência INSS DCTFWEB

Acesse o menu eSocial | Conferência de Conferência de INSS Patronal, para que seja apresentada a tela com os campos para a geração do relatório:

| Campo | Obrigatoriedade | Descrição |
| --- | --- | --- |
| **Período** | Obrigatório | Informar a competência que deseja gerar o relatório. Preencher no formato AAAA/MM ou apenas Ano no formato AAAA para competência anual. |
| **Estabelecimento** | Opcional | Serão listados os estabelecimentos de acordo com o envio do evento S-1005. Poderá selecionar mais de um estabelecimento.  Caso não selecione nenhum estabelecimento, será considerada todos. |
| **Somente Divergências** | Opcional | Este parâmetro permite gerar o relatório apenas para os casos que apresentaram alguma divergência de valores entre as colunas **Folha** e **RET.**  Opções:   * + - **Sim**= lista somente estabelecimentos com divergência de valores.     - **Não**= lista informações de todos os estabelecimentos, independente de haver divergência ou não. |
| **Exibir Valores já Calculados** | Opcional | Sempre que este parâmetro estiver desmarcado o sistema irá buscar os valores de INSS com base no envelope de pagamento com o valores retornados do RET (S-5011), caso contrário será utilizados os valores retornados na ultima geração do relatório.  Ou seja, o parâmetro somente deve ser marcado em casos de re-geração do relatório onde não houve alteração de dados.  É importante ressaltar, que caso o usuário tenha realizado alguma modificação em dados que impactam os cálculos, é imprescindível que o parâmetro esteja desmarcado, para o sistema trazer a informação atualizada.  Exemplo quando utilizar o parâmetro marcado:  O usuário gerou o relatório com o parâmetro desmarcado, não fez nenhuma alteração em dados que impactam os cálculos e deseja apenas gerar novamente o relatório. |

Todos os filtros selecionados são exibidos no container abaixo da barra de campos de filtros. Também é possível remover um ou mais filtros, clicando no "X" à direita de cada ícone, ou por meio do botão "Remover todos":

## Processamento

Após selecionar os filtros desejados, é possível utilizar o botão "Aplicar Filtros" para iniciar a coleta e processamentos das informações para apresentação no painel.

Durante esta operação, uma barra de progresso é exibida abaixo do container de filtros:

Ao final do processamento, são apresentados os valores sintéticos de Recolhimento de INSS e uma tabela com os valores analíticos por estabelecimentos:

### Apresentação das Informações

#### Cards Totalizadores da Consulta

Estes cards totalizam os valores encontrados nas fontes de informação (Folha e Governo), desta forma, já é possível identificar se existem divergências nos valores de INSS.

Para o detalhamento basta clicar nos card's.

É possível acessar o detalhamento por código da receita de cada estabelecimento ao clicar na seta :

Os codigos de receita 164601 (CP PATRONAL - GILRAT AJUSTADO)  e 114101 (CP PATRONAL - ADICIONAL GILRAT)  são somados no código 164601(CP PATRONAL - GILRAT AJUSTADO).IMPORTANTE!

É possível acessar o detalhamento das bases de cada estabelecimento ao clicar no link encontrado no conteúdo da coluna CNPJ:

Ao selecionar a opção **Lotações**, as bases de cálculo de contribuição correspondem à estrutura de lotação.

Ao selecionar a opção **PIS/PASEP**, as bases para o cálculo doPIS/PASEP correspondem à estrutura de filial.

# **Observações**

Os grupos de colunas relativas a valores possuem as seguintes indicações:

* **RH:** Valores de INSS existentes no envelope de pagamento, provenientes do sistema de Folha de Pagamento.
* **Governo**: Dados interceptados no momento da consulta de retorno do governo do evento S-5011. Esses eventos ficam gravados na fila de eventos, juntamente com os eventos de pagamento.

# **Sugestões de Análises**

Caso haja divergência de valores, é necessário analisar e identificar as possíveis causas, que podem ser:

* **Rubricas com incidências incorretas,** resultando em bases e valores diferentes no Governo.
* **Inclusões, exclusões ou alterações** realizadas diretamente no Portal eSocial, impactando as bases e valores enviados.

4Exportação dos TotalizadoresExportação dos Totalizadores

Para realizar a exportação do relatório basta clicar em "Exportar CSV" após o cálculos dos valores.

Após clique em abrir arquivo

Será gerado um arquivo em .CSV com as abas disponíveis dos totalizadores:

* **Total Empresa:** Traz os valores dos Card's totalizadores.
* **Estabelecimentos:** Retorna os valores analíticos da parte de estabelecimentos do relatório.

* **Valores Estabelecimentos:** Retorna os valores por códigos de receitas detalhados por estabelecimento.

* **Lotações:** Retorna os valores analíticos da parte de lotações do relatório.

* **Valores Lotações:** Retorna os valores das bases detalhados por lotação.

## **03. TABELAS UTILIZADAS**

* PESOCIALINSSPATRONAL, PESOCIALINSSESTABELECIMENTO, PESOCIALINSSTOTALESTAB, PESOCIALINSSLOTACAO, PESOCIALINSSTOTALLOTACAO.

## **04. DOCUMENTAÇÃO**
