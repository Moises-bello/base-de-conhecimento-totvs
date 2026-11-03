---
content_hash: c97f614c888024cf80b5498210bbbb0b7b759b1a13611f104a7f6dd154be5e19
fetched_at: '2026-06-29T00:06:27.964577+00:00'
page_id: '233741565'
product: rm
source: tdn-rm
title: TUDCK9 ER Regerar Saldos e Custos - Melhoria de Performance
type: documentation
url: https://tdn.totvs.com/display/LRM/TUDCK9+ER+Regerar+Saldos+e+Custos+-+Melhoria+de+Performance
version: 148
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque,Compras e Faturamento | **Módulo** | Estoque |
| **Segmento Executor** | Construção e Projetos | | |
| **Chamado** | TUDCK9 | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   

## 

## Objetivo

O objetivo desta melhoria é implementar a partir das versões 11.82.43 e 12.1.10 do TOTVS Gestão de Estoque, Compras e Faturamento uma considerável melhoria de performance no processo *"Regerar Saldos e Custos"*.

Anteriormente este processo trabalhava apenas de forma sequencial, ou seja, era regerado um produto de cada vez não importando qual era a capacidade do servidor de aplicação e do banco de dados.

A partir de agora a execução deste processo poderá ser paralelizada, ou seja, poderão ser regerados N produtos de uma só vez e o seu tempo de cálculo estará diretamente relacionado ao poder de processamento do ambiente onde o mesmo está sendo executado, ou seja, quanto mais processadores e memória possuir o servidor de aplicação, mais produtos serão calculados simultaneamente e consequentemente muito menos tempo levará o processo. Entretanto, é importante salientar que a execução em paralelo irá exigir mais do servidor de banco de dados, já que cada cálculo abre uma conexão.

Assim, caso o ambiente não esteja dimensionado adequadamente é possível que ao executar o cálculo de forma paralela sejam exibidas mensagens de "timeout" se o Banco de Dados estiver sobrecarregado, ou de "timeout no connection pool" no Oracle se o número de conexões simultâneas ultrapassar o pré-estabelecido. Deverão ser observados ainda, outros gargalos como o tráfego de rede e outros processos concorrentes, principalmente em bases Oracle, onde por padrão existe um número limitado de conexões simultâneas.

Recomendamos que antes que o processo seja executado, o seu servidor de banco de dados seja analisado e dimensionado corretamente para absorver todas as requisições paralelas e poder utilizar o ganho de performance proporcionado por este recurso.

## 

## Definição da Regra de Negócio

Após a atualização da versão 11.82.43 ou da versão 12.1.10, ao ser acessado o TOTVS Gestão de Estoque, Compras e Faturamento por um usuário que seja Supervisor, o sistema apresentará a mensagem abaixo, informando sobre a existência da nova forma de execução do processo *"Regerar Saldos e Custos":*

Para executar este processo com paralelismo vá em *"Estoque > Processos > Regerar Saldos e Custos".*

Na primeira tela clique em "Avançar".

Na tela de*"Seleção de Produtos"* informe os dados dos produtos cujos saldos e custos serão regerados e clique em "Avançar".

Na tela de *"Parâmetros Gerais"* do processo marque o campo 'Execução Paralela', além dos demais parâmetros habitualmente utilizados por sua empresa na Regeração de Saldos e Custos.

Ao passar o mouse sobre o checkbox do campo o sistema apresentará ao usuário uma dica acerca da função do campo e sobre o seu consumo de recursos:

Ao ser selecionada a Execução Paralela o sistema habilitará um símbolo de alerta.

Passando o mouse sobre o alerta o sistema irá informar o usuário sobre o maior consumo de recursos do banco de dados que a Execução Paralela exige.

Dica

A Execução Paralela também pode ser utilizada caso o processo *"Regerar Saldos e Custos"* seja executado através de agendamento.

Otimize seu ambiente e configure o seu SGDB para que sua empresa esteja apta a realizar a Regeração de Saldos e Custos de forma paralela e possa desfrutar do enorme ganho de performance que é proporcionado por esse recurso.

Otimização do Banco de Dados

* Dimensionar o pool de conexões do banco para suportar várias conexões simultâneas de forma que outros processos não sejam prejudicados. Por padrão, são liberadas apenas 100 conexões simultâneas com a base de dados para cada aplicação. Isso pode ser muito pouco dependendo do porte da base, mas não existe um número ideal para todos, é necessário acompanhar o uso através de performance counters por exemplo se necessário e dimensionar o valor mínimo conforme o uso cotidiano e o valor máximo considerando uma contingência para casos especiais. Para alterar o tamanho do pool na aplicação utilize a tag abaixo no arquivo de configuração do host (RM.Host.Service.exe.config):

*<add key="DBSConnStrExtensions" value=";Min Pool Size=5;Max Pool Size=30;" />*

Onde o min pool size deve ser aumentado de forma a comportar o uso regular, e o Max pool size deve ser aumentado de forma a contemplar situações de uso elevado. O valor a ser colocado no parâmetro deve ser determinado preferencialmente por alguém da T.I. em conjunto com o DBA da empresa.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Regerar Saldos e Custos | Alteração | Estoque > Processos > Regerar Saldos e Custos | Conforme definições constantes deste documento |

## Tabelas Utilizadas:

* TRELSLD - Ficha Física Financeira.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
