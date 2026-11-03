---
content_hash: 5379611574eb00dbca3512a175163ca2e110f69aad2d618082da1a711cda4e1c
fetched_at: '2026-06-29T00:10:37.194858+00:00'
page_id: '536721262'
product: rm
source: tdn-rm
title: Middleware - Relatório de Conferência de INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=536721262
version: 79
---

## **Visão Geral do Programa**

Esta funcionalidade têm por objetivo apoiar na identificação de possíveis divergências entre os valores de INSS existentes no envelope de pagamento com o valores retornados do RET, auxiliando também na conferência de valores (Segurados, Deduções Salário Família e Maternidade) da Guia de INSS.

Os dados apresentados são originados da comparação dos valores de INSS integrados do RH (S-1200, S-2299 e S-2399) contra os valores retornados do Governo pelo evento S-5001.

Parametrização

## **Parametrização**

1) Realize a configuração do DefaultDB no config do Host. Informações em: [Configurando DefaultDB](https://tdn.totvs.com/display/LRM/Configurando+DefaultDB).

2) Para utilização dos relatórios de conferência, é necessário informar o servidor e porta que serão utilizados para execução desses serviços. Acesse o menu Configurações | Parametrizador | eSocial | Configurações Gerais | Integração com Middleware | Outros parâmetros:

**Servidor/Porta API**: Servidor e porta onde o serviço de API"s RM está sendo executado. (**APiPort** do Host RM. No caso onde a ApiPort não foi discriminada nas configurações do Host, utilizar a HttpPort).   
**Servidor/Porta APP:** Servidor e porta onde o aplicativo THF está sendo executado. (Caso o servidor seja o Host RM, informar a **HttpPort**).

Para maiores informações sobre a configuração da **HttpPort** e **ApiPort**, acesse: [O que é e como configurar a HttpPort e ApiPort](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633-RM-Integra%C3%A7%C3%B5es-O-que-%C3%A9-e-como-configurar-a-HttpPort-e-ApiPort-).

**OBSERVAÇÃO: Se estiver executando o RM.Host.exe o mesmo deve ser executado com administrador.**

ImportanteNas versões e patches iguais e superiores a 12.1.28.147, 12.1.27.237 e 12.1.26.255 é imprescindível a execução do sistema RM.Atualizador.exe para a criação da tabela PESOCIALTOTALIZADORESAUTONOMOS, que será utilizada no relatório de conferência de INSS para comparação dos autônomos cadastrados no TOTVS Gestão Financeira ou autônomos externos. A partir da 12.1.29 não é necessário executar o RM.Atualizador.exe.Menu eSocial | Conferência INSS/FGTS/IRRF

## **Menu eSocial | Conferência INSS/FGTS/IRRF**

##### **Filtros**

Ao selecionar no menu a opção "Relatório de Conferência (INSS)" será apresentado o Painel de Conferência do INSS:

Lista de campos apresentados na tela para utilização como filtro das informações a ser processadas:

| Campo | Obrigatoriedade | Descrição |
| --- | --- | --- |
| **Período** | Obrigatório | Ano/Mês no formato AAAA/MM, ou apenas Ano no formato AAAA, para ser considerado no processamento das informações do painel. Competência da Folha de Pagamento que foi integrada com o governo. |
| **Estabelecimento** | Opcional | Lista de estabelecimentos de acordo com os enviados no evento S-1005. Podem ser selecionados mais de um estabelecimento. |
| **Somente Divergências** | Opcional | Parâmetro que permite listar somente os casos que apresentaram alguma divergência de valores entre as colunas RH x Governo, ou listar todos os colaboradores que possuam valor de INSS em sua remuneração, independente de divergência ou não. Opções:  * + **Sim**= lista somente colaboradores com divergência de valores nas colunas de valor.   + **Não**= lista informações de todos os colaboradores que possuam valor de INSS em sua remuneração. |

ImportanteO painel conta com filtro adicional que pode ser encontrado clicando no botão "Busca Avançada". Os filtros podem ser aplicados em ambas as telas ( Principal e Busca Avançada ).

Lista de campos apresentados na tela de Busca Avançada:

| Campo | Obrigatoriedade | Descrição |
| --- | --- | --- |
| **Estabelecimento** | Opcional | Lista de estabelecimentos de acordo com os enviados no evento S-1005. Podem ser selecionados mais de um estabelecimento. |
| **Lotação** | Opcional | Lista de lotações de acordo com as enviadas no S-1020. Podem ser selecionadas mais de uma lotação. |
| **Período** | Obrigatório | Ano/Mês no formato AAAA/MM, ou apenas Ano no formato AAAA, para ser considerado no processamento das informações do painel. Competência da Folha de Pagamento que foi enviado ao RET. |
| **Somente Divergências** | Opcional | Parâmetro que permite listar somente os casos que apresentaram alguma divergência de valores entre as colunas RH x Governo, ou listar todos os colaboradores que possuam valor de INSS em sua remuneração, independente de divergência ou não. Opções:  * **Sim**= lista somente colaboradores com divergência de valores nas colunas de valor. * **Não**= lista informações de todos os colaboradores que possuam valor de INSS em sua remuneração. |
| **Matrícula** | Opcional | Matricula do colaborador o qual se deseja buscar os valores de INSS. |
| **Categoria** | Opcional | Categoria do colaborador o qual se deseja buscar os valores de INSS. |
| **CPF** | Opcional | CPF do colaborador o qual se deseja buscar os valores de INSS. |

Todos os filtros selecionados são exibidos no container abaixo da barra de campos de filtros. Também é possível remover um ou mais filtros, clicando no "X" à direita de cada ícone, ou por meio do botão "Remover todos":

Processamento

## **Processamento**

Após selecionar os filtros desejados, é possível utilizar o botão "Aplicar Filtros" para iniciar a coleta e processamentos das informações para apresentação no painel. Durante esta operação, uma barra de progresso é exibida abaixo do container de filtros:

Ao final do processamento, são apresentados os valores sintéticos de Recolhimento de INSS e uma tabela com os valores analíticos por colaborador:

Apresentação das Informações

## **Apresentação das Informações**

Cards Totalizadores da Consulta: Estes cards totalizam os valores encontrados nas fontes de informação (**RH** e **Governo**), desta forma, já é possível identificar se existem divergências nos valores de desconto de INSS.

Importante!Os detalhamentos dos valores sintéticos dos Cards deixaram de ser apresentados em tela e passaram a serem visualizados através do detalhamento de funcionários e, além disso, com a nova funcionalidade de extração dos dados, o usuário poderá também trabalhar esses valores conforme necessidade.Pesquisa por CPF ou Nome

## **Pesquisa por CPF ou Nome**

O campo apresentado com um ícone de lupa permite pesquisar entre os dados carregados na tela. A pesquisa é aplicada apenas para o CPF e Nome do colaborador:

Tabela Analítica por Pagamento a Colaborador

## **Tabela Analítica por Pagamento a Colaborador**

A tabela apresentada exibe os valores de forma analítica por pagamento a colaborador. Caso o colaborador possua mais de um vínculo, e consequentemente, mais de um pagamento recebido, a tabela apresentará os dados somados deste colaborador.

Nesta tabela, é apresentado apenas o Valor de Recolhimento de INSS:

É possível acessar o detalhamento de mais valores analíticos de cada colaborador ao clicar no link encontrado no conteúdo da coluna CPF ou Nome:

Nesta tela, além do Valor de Recolhimento do INSS, também são apresentados na **aba Contribuições Sociais** os valores de Base de INSS, Base de INSS 13º Salário, Valor de Recolhimento de INSS 13º Salário, Salário Família, Salário Maternidade e Salário Maternidade 13º Salário para cada fonte de informação (RH e Governo ):

**ATENÇÃO:** Caso possua múltiplos vínculos, será apresentada a descrição dos valores para cada vinculo, conforme demonstrado abaixo:

Na **aba PIS/PASEP**é apresentados os valores de base de PIS/PASEP, sendo que os valores são identificados por filial.

A tabela é apresentada com 30 colaboradores (podendo ser editado em Busca avançada opção **Funcionários por página**), para não carregar informações desnecessárias na tela e prejudicar a performance de navegação. Para carregar mais resultados, é possível clicar no botão "Carregar mais resultados".

  
  
Exportar Relatório

## **Exportar Relatório**

Clicando no botão **Exportar** é possível salvar os dados Analíticos e Sintéticos gerados em .XLS.

**Sintético**: Exporta os valores sintéticos apresentados na primeira tela.

**Analítico:** Exporta os valores analíticos apresentados ao clicar no detalhamento de cada funcionário.

**Considerações importantes para o correto funcionamento do Painel de Conferência de INSS:**

Importante

**Os grupos de colunas relativas a valores possuem as seguintes indicações:**

* **RH: Valores de INSS existentes no envelope de pagamento, provenientes do sistema de Folha de Pagamento.**
* **Governo: Dados interceptados no momento da consulta de retorno do governo do evento S-5001. Esses eventos ficam gravados na fila de eventos, juntamente com os eventos de pagamento.**

* Embora a coluna "**Valor INSS - Descontado do Colaborador em folha (Enviado)**" esteja presente neste relatório, ela não é utilizada para retornar valores. Portanto, se preferir não visualizá-la, basta ocultá-la clicando na engrenagem.  
  É importante destacar que a coluna não foi removida do relatório, pois compartilhamos a mesma estrutura do TAF Full, onde essa coluna é utilizada para informar o valor do INSS no momento da transmissão no TAF, o cliente pode ter alterado algo direto no TAF e ficar com um valor divergente do que está no ERP.

* O Relatório de Conferência de INSS passou por algumas mudanças recentemente. Para verificar os detalhes sobre as mudanças ocorridas, acesse:

[Middleware - Mudanças no Relatório de Conferência - INSS](https://tdn.totvs.com/pages/viewpage.action?pageId=639179085)

Observações

## **Observações**

Os grupos de colunas relativas a valores possuem as seguintes indicações:

* **RH:** Valores de INSS existentes no envelope de pagamento, provenientes do sistema de Folha de Pagamento.
* **Governo**: Dados interceptados no momento da consulta de retorno do governo do evento S-5001. Esses eventos ficam gravados na fila de eventos, juntamente com os eventos de pagamento.
Sugestões de Análises

## **Sugestões de Análises**

Apresentando divergência de valores, estas devem ser analisadas e identificadas as causas, que podem ser:

* Rubricas com incidências incorretas que geram bases e valores diferentes no Governo.
* Inclusões, exclusões ou alterações nas bases e/ou valores operados diretamente no Portal eSocial.
Detalhamento dos Campos

## **Detalhamento dos Campos**

O **retorno do evento S-5001** (Informações de Contribuições Sociais por Trabalhador) **não detalha os valores calculados por matrícula**, mas sim por **CPF** (Cadastro de Pessoa Física) do trabalhador.

Os campos abaixo, utilizados na totalização do eSocial, mapeiam os valores de retenção de INSS (Instituto Nacional do Seguro Social) conforme o **indicativo de apuração (indApuracao)** existente no retorno do evento

S-5001 - Informações das contribuições sociais consolidadas por trabalhador:

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo** | **Descrição no relatório** | **Tag no evento S-5001** | **Indicativo de 13° salário** |
| PESOCIALTOTALIZADORES.VALORINSSRET | Valor INSS | valor (tipo tpValor = 21) no grupo infoBaseCS | ind13 =0 (Mensal) |
| PESOCIALTOTALIZADORESCPF.VALORINSSRET | Valor INSS - Calculado pelo eSocial (Valor da DCTFWEB) | vrCpSeg no grupo infoCpCalc | ind13 =0 (Mensal) |
| PESOCIALTOTALIZADORES.VALORINSS13RET | Valor INSS 13° | valor (tipo tpValor = 21) no grupo infoBaseCS | ind13 =1 (13º) |
| PESOCIALTOTALIZADORESCPF.VALORINSS13RET | Valor INSS 13° Salário - Calculado pelo eSocial (Valor da DCTFWEB) | vrCpSeg no grupo infoCpCalc | ind13 =1 (13º) |

**Exemplo:**  
Realizado o envio de um funcionário com múltiplos vínculos, em que, na folha de pagamento, foi desmarcada uma incidência sem que a rubrica correspondente fosse atualizada no RET, ocasionando divergências de valores.

**Envelope:** 1

**Envelope:** 2

**Retorno do eSocial:** Evento S-5001

**Relatório de Conferência de INSS:** Apresentou divergência somente na tela inicial

Divergência no Relatório

## **Divergência no Relatório**

Devido ao cálculo e retorno serem unificados por CPF, o seguinte cenário pode ocorrer na geração do relatório de conferência:

* **Visão Sintética do Relatório:** É apresentada sempre a divergência, pois essa visão é por CPF.
* **Visão Analítica do Relatório:** A divergência **somente deverá ocorrer** se houver **alteração na folha de pagamento** após o envio original do evento S-1200. Sem uma alteração posterior, o valor comparado retornado pelo RET por matricula é o mesmo enviado.
Tabelas Utilizadas

## **Tabelas Utilizadas**

* PESOCIALTOTALIZADORES
* PESOCIALTOTALIZADORESCPF
* PESOCIALTOTAISLOTACAO
* PESOCIALTOTALIZADORESAUTONOMOS
