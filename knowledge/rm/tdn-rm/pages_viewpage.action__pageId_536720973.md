---
content_hash: 11f6f73380d56c3843d8fcedba61aa5ce2c022278f21dcd51d36f84a875e1509
fetched_at: '2026-06-29T00:10:37.175874+00:00'
page_id: '536720973'
product: rm
source: tdn-rm
title: Middleware - Relatório de Conferência de FGTS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=536720973
version: 39
---

# Visão Geral do Programa

Esta funcionalidade tem como objetivoir além de um simples relatório, servindo como uma ferramenta prática, simples e intuitiva para consulta das Bases e Valores de Depósito do FGTS registrados no sistema de Folha de Pagamento e no evento Totalizador S-5003, enviado ao governo.

A funcionalidade é composta pelas informações extraídas dos eventos enviados ao eSocial: **S-1200, S-2299 e S-2399**.

A abaixo, iremos apresentar e explicar os significados de **cada valor exibido no painel**, além das instruções sobre como **utilizar os recursos disponíveis dentro do TOTVS Folha de Pagamento**.

1true1ParametrizaçãoParametrização

Acesse o menu Configurações | Parametrizador | eSocial | Configurações Gerais | Integração com Middleware | Outros parâmetros.

Para utilização dos relatórios de conferência, é necessário informar o servidor e porta que serão utilizados para execução desses serviços.

**Servidor/Porta API**: Servidor e porta onde o serviço de API"s RM está sendo executado. (**APiPort** do Host RM. No caso onde a ApiPort não foi discriminada nas configurações do Host, utilizar a HttpPort)  
**Servidor/Porta APP:** Servidor e porta onde o aplicativo THF está sendo executado. (Caso o servidor seja o Host RM, informar a **HttpPort**).

Para maiores informações sobre a configuração da **HttpPort** e **ApiPort**, acesse: [O que é e como configurar a HttpPort e ApiPort](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633-RM-Integra%C3%A7%C3%B5es-O-que-%C3%A9-e-como-configurar-a-HttpPort-e-ApiPort-).

2Relatório de Conferência de FGTSRelatório de Conferência de FGTS

Acesse o menu eSocial |Conferência INSS/IRRF/FGTS, e clique em "Relatório de Conferência (FGTS)".

### 1) Filtros

Lista de campos apresentados na tela para utilização como filtro das informações a ser processadas:

| Campo | Obrigatoriedade | Descrição |
| --- | --- | --- |
| **Período** | Obrigatório | Ano/Mês no formato AAAA/MM, ou apenas Ano no formato AAAA, para ser considerado no processamento das informações do painel. Competência da Folha de Pagamento que foi integrada ao RET. |
| **CPF** | Opcional | CPF do colaborador o qual se deseja buscar os valores de FGTS. |
| **Matrícula** | Opcional | Matricula do colaborador o qual se deseja buscar os valores de FGTS. |
| **Somente Divergências** | Opcional | Parâmetro que permite listar somente os casos que apresentaram alguma divergência de valores entre as colunas RH x Governo, ou listar todos os colaboradores que possuam valor de FGTS em sua remuneração, independente de divergência ou não.  Opções:   * **Sim**= lista somente colaboradores com divergência de valores nas colunas de valor. * **Não**= lista informações de todos os colaboradores que possuam valor de FGTS em sua remuneração. |
| **Categoria** | Opcional | Categoria do colaborador o qual se deseja buscar os valores de FGTS. |

IMPORTANTE:

O painel conta com filtro adicional que pode ser encontrado clicando no botão "Busca Avançada". Trata-se do filtro de categoria do colaborador, um filtro muito útil para o caso de funcionários que possuem múltiplos vínculos e no qual se deseja consultar os valores de Depósito e Bases do FGTS de forma individual. Estes filtros podem ser aplicados em ambas as telas ( Principal e Busca Avançada ).

### 2) Apresentação das Informações

#### 

Os cards totalizam os valores encontrados nas duas fontes de informação ( RH e Governo ) e demonstra de forma sintética os resultados, desta forma, já é possível identificar se existem divergências nos valores. Na tela principal é apresentado apenas o Valor de Depósito de FGTS:

Além disso, estes cards são interativos, sendo possível acessar o detalhamento de mais valores sintéticos ao clicar no espaço ocupado por qualquer um dos cards.

Além do Valor de Depósito de FGTS, também são apresentados os valores de Valor de Depósito de FGTS 13º Salário, Valor de Depósito de FGTS Rescisório, Base de FGTS, Base de FGTS 13º Salário e Base de FGTS Rescisório para cada fonte de informação ( RH e Governo ):

### 3) Pesquisa por CPF ou Nome

O campo apresentado com um ícone de lupa permite pesquisar entre os dados carregados na tela. A pesquisa é aplicada apenas para o CPF e Nome do colaborador e pode ser utilizado com valor parcial ou total. Será apresentado uma lista com os colaboradores encontrados na pesquisa executada e que representam o resultado analítico dos valores exibidos:

### 4) Tabela Analítica por Pagamento a Colaborador

É possível acessar o detalhamento de mais valores analíticos de cada colaborador ao clicar no link encontrado no conteúdo da coluna Nome:

### 5) Exportar Relatório

Clicando no botão Exportar é possível salvar os dados gerados em .XLS.

3ConsideraçõesConsiderações

Abaixo listamos algumas considerações importantes para o correto funcionamento do Relatório de Conferência de FGTS.

Os grupos das colunas relativas a valores possuem as seguintes indicações:

* **RH**: Dados interceptados no momento da integração com o governo dos arquivos xml de eventos do eSocial, provenientes do sistema de Folha de Pagamento.
* **Governo**: Dados interceptados no momento da consulta de retorno do governo do evento S-5003. Esse evento fica registrado também na fila de eventos junto com o evento de pagamento enviado.
* **FGTS valor governo:** o valor retornado neste campo é o valor da tag <dpsFGTS> do evento S-5003.
* **FGTS valor RH:** o valor retornado neste campo é calculado utilizando a base de FGTS do envelope de pagamento (PFFINANC) e aplicando o percentual conforme tipo do funcionário.
  + O percentual é aplicado nas bases conforme o agrupamento no eSocial, sendo:

| Código | Descrição | Código | Descrição |
| --- | --- | --- | --- |
| 11 | FGTS mensal | 23 | FGTS aviso prévio indenizado |
| 12 | FGTS 13° salário | 24 | FGTS (período anterior) mês da rescisão |
| 13 | FGTS (período anterior) mensal | 25 | FGTS (período anterior) 13º salário rescisório |
| 14 | FGTS (período anterior) 13º salário | 26 | FGTS (período anterior) aviso prévio indenizado |
| 15 | FGTS mensal - Aprendiz/Contrato Verde e Amarelo | 27 | FGTS mês da rescisão - Aprendiz/Contrato Verde e Amarelo |
| 16 | FGTS 13° salário - Aprendiz/Contrato Verde e Amarelo | 28 | FGTS 13° salário rescisório - Aprendiz/Contrato Verde e Amarelo |
| 17 | FGTS (período anterior) mensal - Aprendiz/Contrato Verde e Amarelo | 29 | FGTS aviso prévio indenizado - Aprendiz/Contrato Verde e Amarelo |
| 18 | FGTS (período anterior) 13º salário - Aprendiz/Contrato Verde e Amarelo | 30 | FGTS (período anterior) mês da rescisão - Aprendiz/Contrato Verde e Amarelo |
| 21 | FGTS mês da rescisão | 31 | FGTS (período anterior) 13° salário rescisório - Aprendiz/Contrato Verde e Amarelo |
| 22 | FGTS 13° salário rescisório | 32 | FGTS (período anterior) aviso prévio indenizado - Aprendiz/Contrato Verde e Amarelo |

**Exemplo: Quando o funcionário é demitido, o processo é o seguinte:**

**1)** Na rescisão do funcionário são utilizadas as bases:

* + - 21 - FGTS mês da rescisão;
    - 22 - FGTS 13° salário rescisório;
    - 23 - FGTS aviso prévio indenizado.

 

**2)** No retorno do RET é apresentado:

**3)**No relatório, os valores são apresentados conforme os dados do eSocial, com os devidos cálculos de FGTS aplicados sobre as bases informadas. Veja o exemplo abaixo:

* **21 – FGTS mês da rescisão:** Base: R$1.136,12 × 8% = **R$90,89**
* **22 – FGTS 13º salário rescisório:** Base: R$196,57 × 8% = **R$15,72**
* **23 – FGTS aviso prévio indenizado:** Base: R$1.398,46 × 8% = **R$111,88**

**Total:** 90,89 + 15,72 + 111,88 = **R$218,49**

Este valor total (**R$218,49**) é apresentado tanto na coluna **"VALOR RH"** quanto na coluna **"VALOR GOVERNO"**, permitindo a conferência entre o que foi processado internamente no sistema de folha e o que foi reconhecido pelo governo por meio do evento **S-5003**.

**4)**No envelope de pagamento, são apresentadas as bases somadas conforme as incidências aplicadas.

**Exemplo:**

* + **Folha:** R$1.436,30 × 8% = **R$114,90**
  + **13º Salário:** R$294,85 × 8% = **R$23,59**

**ATENÇÃO:**

1. 1. * Como demonstrado nos cálculos acima, pode haver ocasionalmente uma diferença de um centavo.
      * Para calcular os valores na coluna "RH", o sistema extrai as informações da ficha financeira (PFFINANC) e realiza o cálculo conforme demonstrado anteriormente. É importante observar que os valores sempre serão truncados.

4Sugestão de AnáliseSugestão de Análise

Apresentando divergência de valores, estas devem ser analisadas e identificadas as causas, que podem ser:

* Rubricas com incidências incorretas que geram bases e valores diferentes no Governo.
* Inclusões, exclusões ou alterações nas bases e/ou valores operados diretamente no Portal eSocial.

# Tabelas utilizadas

PESOCIALTOTALIZADORES, PESOCIALTOTALIZADORESCPF, PESOCIALTOTAISLOTACAO e PESOCIALTOTALIZADORESAUTONOMOS.
