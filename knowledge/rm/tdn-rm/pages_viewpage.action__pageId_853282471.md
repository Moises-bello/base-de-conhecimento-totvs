---
content_hash: 00594b7f945c2010bcf7658fc342f7d7abb50f12a7e89ca6ed9416a8cba6ddff
fetched_at: '2026-06-29T00:11:54.048868+00:00'
page_id: '853282471'
product: rm
source: tdn-rm
title: Pré-Processamento Apuração Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=853282471
version: 96
---

AVISO

Esta funcionalidade está em desenvolvimento e será disponibilizada em breve.

# Conteúdo

Conteúdo

# 1. Visão Geral

O **Pré-Processamento Apuração Fiscal** é um processo de preparação dos dados fiscais que otimiza a performance na jornada fiscal do usuário, principalmente em etapas como Apuração e obrigações acessórias. Ele realiza uma série de validações e cálculos sobre os dados fiscais de origem, preparando-os para o uso nas próximas etapas, o que reduz o tempo de resposta e o esforço computacional nos momentos de geração dessas rotinas.

O Pré-Processamento Apuração Fiscal utiliza o [Fracionamento de Job](https://tdn.totvs.com/pages/viewpage.action?pageId=547231277), permitindo que o processo seja dividido em etapas, agendado e distribuído entre servidores para maior eficiência e estabilidade na execução. Com isso, ao gerar as rotinas fiscais, o sistema acessa diretamente os dados já pré-processados, proporcionando agilidade e precisão. Os dados pré-processados podem ser visualizados em uma tela específica, de acordo com as permissões e o perfil de cada usuário, possibilitando o acompanhamento e revisão conforme necessário.

# 2. Configurações iniciais

Para utilizar o Pré-Processamento é necessário realizar algumas configurações iniciais conforme abaixo:

ConfigleftPermissões por usuário

## Permissões por usuário:

Acesse o perfil vinculado ao usuário, do módulo Gestão Fiscal, em acesso aos menus, em obrigações acessórias, configuração de campos, permitir acesso ao item "[03.01.03] Pré-Processamento Apuração Fiscal".

Configuração do processo (job)

## Configuração do processo (job)

É possível configurar o processo utilizando recurso de agendamento e fracionamento de jobs, quando parametrizado em N camadas, neste caso basta executar o processo normalmente, após a tela de parâmetros será apresentado a tela de configuração do job.

Parametrizações de rotina

## Parametrizações de rotina

O processo está disponível à partir da versão 12.1.2402. Os campos do anexo dos Parâmetros da Rotina precisam ser preenchidos para que o pré-processamento possa ser executado. Neste caso, siga os passos abaixo para correta execução do processo:

Deck ParametrizaçãoPasso\_01Passo 01Passo 01

Acesse Obrigações Acessórias, Rotinas Fiscal, inclua a rotina desejada, (neste primeiro momento apenas a rotina EFD Contribuições está implementada no processo).

Passo\_02Passo 02Passo 02

Execute o processo: Processo Parâmetros da Rotina.

Passo\_03Passo 03Passo 03

Informe o layout e os parâmetros da rotina. (para a rotina EFD Contribuições é necessário inserir os parâmetros APURACAO\_PIS e APURACAO\_COFINS manualmente para que seja possível identificar qual o tributo principal utilizado pelo usuário.

# 3. Processo do Pré-Processamento

O Processo do Pré-Processamento tem como objetivo preparar os dados fiscais para etapas subsequentes, como a **apuração da EFD-Contribuições**. Durante a execução, o sistema realiza uma busca nos lançamentos fiscais com base nos parâmetros de Data Inicial, Data Final e Rotina Fiscal, armazenando os resultados na tabela de Pré-Processamento.

Imagem

Essa tabela permite que outros processos do sistema acessem os dados pré-processados de forma mais eficiente, reduzindo o tempo de processamento e aumentando a performance geral do sistema.

Para realizar o Pré-Processamento, é necessário fazer o preenchimento dos campos nos Parâmetros da Rotina. Para isso basta executar o processo Rotinas Fiscais > Processos Parâmetros da Rotina. 

Parâmetros da Rotina Fiscal

Também é possível executar o processo de Pré-Processamento utilizando o serviço de agendamento ou fracionamento de jobs. Para mais informações acesse a documentação: "[Ambiente 3 Camadas](https://tdn.totvs.com/display/LRM/Ambiente+3+Camadas)".

Agendamento do ProcessoFracionamento de Jobs

Ao [Encerrar Períodos](https://tdn.totvs.com/pages/viewpage.action?pageId=421388803) do PIS/COFINS será executado o processo do Pré-Processamento automaticamente.

Encerramento de Períodos com execução do Pré-Processamento

### Regras Específicas

* Para [Encerramento do Período](https://tdn.totvs.com/pages/viewpage.action?pageId=421388803) de PIS/COFINS é necessário realizar o cadastro e configurações dentro de [Rotinas Fiscais/Anexo Parâmetros de Rotina](https://tdn.totvs.com/pages/viewpage.action?pageId=842699260).
* Ao encerrar os períodos PIS/COFINS, será executado o processo do Pré-Processamento automaticamente que e irá persistir o(s) lançamento(s) para apuração.
* No encerramento será verificado se os lançamentos não foram pré-processdos e irá executa-los, caso contrario esse processo não acontecerá no encerramento do período.
* O Encerramento de Múltiplos Períodos também vai executar o Pré-Processamento automaticamente.

Exemplo de Encerramento do PeríodoExemplo de Encerramento de Múltiplos Períodos

# 4. Processos de Expurgo de Dados do Pré-Processamento Apuração Fiscal

Os dados gerados no Pré-Processamento Apuração Fiscal são utilizados exclusivamente nas etapas de Apuração e na geração da **EFD-Contribuições**. Após a execução desses processos, os dados armazenados podem ser excluídos sem qualquer prejuízo às funcionalidades ou à integridade do sistema.

Caso os dados sejam apagados e haja necessidade de reutilizá-los, o Pré-Processamento pode ser executado novamente, recriando todas as informações necessárias para suportar as etapas seguintes da jornada fiscal. Essa possibilidade torna o expurgo de dados uma operação segura, permitindo a otimização do uso de espaço no banco de dados sem comprometer a continuidade das operações fiscais.

O expurgo pode ser realizado de duas formas: manualmente, com critérios definidos pelo usuário, ou automaticamente, seguindo parâmetros previamente configurados no sistema. Ambas as opções são descritas detalhadamente nos tópicos a seguir.

## 4.1 Expurgo Manual de Dados do Pré-Processamento Apuração Fiscal

O expurgo manual permite ao usuário selecionar e excluir registros antigos do Pré-Processamento Apuração Fiscal de forma personalizada. Para realizar o expurgo, é necessário criar um filtro com os critérios desejados, como período, filial ou outros campos disponíveis na tabela do Pré-Processamento. Após a definição do filtro, basta executar o processo para que os registros correspondentes sejam removidos da base de dados.

Este processo exige uma permissão específica configurada no perfil do usuário, garantindo que somente pessoas autorizadas possam realizar a exclusão dos dados.

Ao final da execução, o sistema apresenta um log detalhado com as informações do expurgo, incluindo a quantidade de registros excluídos, o período selecionado e as filiais impactadas, assegurando total rastreabilidade da operação.

## 4.2 Expurgo Automático de Dados do Pré-Processamento Apuração Fiscal

O expurgo automático ocorre durante a execução do processo de Pré-Processamento Apuração Fiscal, seguindo as configurações do parâmetro **MESES\_PARA\_MANTER\_HISTORICO**. Esse parâmetro determina o período de meses que os dados históricos devem ser mantidos na tabela de registros do Pré-Processamento. Caso o parâmetro não esteja configurado, o sistema utiliza o valor padrão de 6 meses.

Durante a execução, o sistema calcula automaticamente a data limite com base no período configurado e remove os registros anteriores a essa data, garantindo que apenas os dados mais recentes sejam mantidos. Esse processo é integrado ao fluxo do Pré-Processamento, eliminando a necessidade de intervenção manual para a limpeza dos dados.

As informações sobre o expurgo são registradas no log do Pré-Processamento Apuração Fiscal, incluindo a quantidade de dados excluídos e o período correspondente ao expurgo. Isso assegura transparência e rastreabilidade do processo, permitindo ao usuário monitorar as operações realizadas de forma automática.

Rotina Fiscal > Parâmetros da Rotina

**Exemplo de Expurgo automático**

### **Exemplo 1**

* **Configuração do parâmetro:** 3 meses.
* **Período processado pelo Pré-Processamento:** 01/01/2024 a 31/01/2024.
* **Cálculo do expurgo:** O sistema subtrai 3 meses da data final do período processado (31/01/2024 - 3 meses = 01/10/2023).
* **Resultado:** Todos os registros anteriores a 01/10/2023 são excluídos automaticamente, e o sistema mantém apenas os dados a partir dessa data.

### **Exemplo 2**

* **Configuração padrão (sem parâmetro):** 6 meses.
* **Período processado pelo Pré-Processamento:** 01/01/2024 a 31/01/2024.
* **Cálculo do expurgo:** O sistema subtrai 6 meses da data final do período processado (31/01/2024 - 6 meses = 01/07/2023).
* **Resultado:** Todos os registros anteriores a 01/07/2023 são excluídos automaticamente, e o sistema mantém apenas os dados a partir dessa data.

# 5. Outras Informações

## 5.1 Edição/exclusão de lançamentos pré-processados

É possível editar lançamentos que já passaram pelo pré-processamento. Isto é útil caso seja necessário realizar alguma alteração para corrigir alguma informação, ou até mesmo cancelar um lançamento. Entretanto, **qualquer alteração em um lançamento fiscal que já foi pré-processado acarretará em sua exclusão automática do pré-processamento**, sendo necessário executar o pré-processamento novamente para que ele volte a considerar o lançamento editado, caso seja necessário. Navegue pelas abas abaixo para visualizar exemplos de todas as situações em que um lançamento será excluído do pré-processamento:

ExemplosEdicaoExclusaoEdicaoDoLancamentoEdição do Lançamento

Suponhamos que temos um lançamento que foi pré-processado em 11/2024, cujo ID é 3489. Este lançamento possui duas parcelas:

Este lançamento, por acaso, foi salvo com a observação do item errada (ficou escrito "cmoercial" ao invés de "comercial"), e a pessoa que identificou o erro o corrigiu.

Neste caso, ao salvar o lançamento, será realizada uma edição nele. Isso automaticamente irá excluí-lo da tabela de pré-processamento.

ExclusaoDoLancamentoExclusão do Lançamento

Como o lançamento deixa de existir no sistema, ele também será excluído do pré-processamento.

CancelarOLancamentoCancelar o Lançamento

Como houve alteração do status do lançamento fiscal, será contabilizado como edição. Logo, ele será excluído do pré-processamento.  
Importante ressaltar que o pré-processamento aceita lançamentos cancelados. Caso seja necessário considerar o lançamento novamente, basta executar o pré-processamento após cancelá-lo.

FecharOPeriodoFiscalFechar o Período Fiscal

Os lançamentos serão apagados do sistema e guardados em tabelas de histórico. Logo, eles também serão excluídos do pré-processamento. Ao abrir um período fiscal, será possível realizar o pré-processamento com os lançamentos novamente.

EstornoDeEscrituracaoEstorno de Escrituração

Os lançamentos são excluídos no estorno, então também serão excluídos do pré-processamento.
