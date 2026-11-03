---
content_hash: 3c5875190157c8824315d6346be21c7936279f809430b93d15396dc61fc92cbd
fetched_at: '2026-06-29T00:10:15.920647+00:00'
page_id: '465385372'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-4434 DT Fracionamento do processo de contabilização / estorno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465385372
version: 28
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Gestão Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Contabilização / estorno por competência |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUINTEGRACOES-4434 DEDUINTEGRACOES-4744 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a contabilização / estorno por competência do TOTVS Educacional para um grande volume de contratos, necessita-se que seja reduzido o tempo total de execução deste processo e que seja melhor aproveitado a estrutura dos servidores.

## **03. SOLUÇÃO**

Vislumbrou-se o fracionamento do processo de contabilização / estorno por competência, como forma de reduzir o tempo total de execução, assim como aproveitar melhor a capacidade de processamento do servidores.

## **DESCRIÇÃO**

Com o objetivo de fracionar os processos de contabilização / estorno por competência, foi desenvolvida funcionalidade intrínseca ao processo de contabilização / estorno por competência, que  particiona de forma automática os contratos selecionados, criando novos processos e os colocando em execução. O sistema grava no banco de dados os identificadores dos subprocessos gerados e permite o acompanhamento das execuções, através de um tela de monitoramento.  
O sistema decidirá se o fracionamento será realizado a partir dos parâmetros preenchidos para fracionamento e da quantidade de contratos a ser processada.  
Ao se fracionar é criado um processo pai o qual será responsável por disparar a execução dos processos filhos.

## **GERAÇÃO DA CONTABILIZAÇÃO / ESTORNO**

Na tela de geração de contabilização / estorno, assim que for disparada a execução, o sistema fará uma carga de todos os contratos, conforme selecionado ou definido nos filtros ordenando os mesmos por matriz aplicada.

Após a carga dos contratos, o sistema consultará os parâmetros de fracionamento abaixo para saber se utilizará o fracionamento de processos bem como qual será o número de contratos por fracionamento e o número máximo de processos.

* "Utiliza fracionamento de processos: Indica se o fracionamento de processos (jobs) está habilitado. Caso esteja marcado, o sistema passará a subdividir os processos a serem executados de acordo com o número de contratos parametrizados por fracionamento. Caso não esteja marcado, o sistema se comportará conforme comportamento atual, ou seja, a framework do RM continuará gerenciando os processos conforme configuração do sistema.
* "N° de contratos por fracionamento: Indica o número limite de contratos que o sistema considerará por fracionamento. Se o número limite de contratos não for atingido o sistema não fracionará, ou seja, será criado apenas um processo que será responsável pela contabilização / estorno de todos os contratos. O número de contratos por fracionamento só ficará habilitado se o parâmetro de utilização de fracionamento estiver marcado. O número default para o tamanho do pacote é de **1500** contratos, ou seja, se o usuário somente marcar a opção de utilização de fracionamento, o sistema assumirá esse tamanho a partir do qual os jobs são fracionados. Caso o fracionamento esteja habilitado, o sistema não permitirá um valor menor ou igual a zero.
* Nº máximo de processos por contexto: Número limite de processos a serem gerados pelo fracionamento, ou seja, o sistema somente criará processos até o número máximo especificado por esse parâmetro.   
  Se a quantidade de contratos dividida pelo número de contratos por fracionamento (arredondando sempre para o próximo número inteiro) for maior do que o número máximo de processos, o sistema ajustará o número de contratos por fracionamento na execução do processo corrente de forma que a quantidade de processos gerados não exceda o número de processos informado. Caso o fracionamento esteja habilitado, o sistema não permitirá um valor menor ou igual a zero.  
    
  **Exemplo:**  
  Sistema está parametrizado para "Utilizar fracionamento de processos"  
  Nº de contratos por fracionamento: 100  
  Nº máximo de processos por contexto: 5  
  Total de contratos a serem processados: 1000  
    
  Com essa parametrização, inicialmente, o sistema tentará quebrar o total de contratos (1000) em 10 processos com 100 contratos cada.   
  Como o número máximo de processos gerados é 5, o sistema recalculará o número de contratos por processo da seguinte forma:   
    
  **Nº de contratos por fracionamento** = Total de contratos a serem processados / Nº máximo de processos por contexto = (1000 / 5) = **200**  
  **Observação:** Se esse número de contratos por fracionamento calculado não for um número inteiro, o sistema arredondará para o número inteiro posterior mais próximo. Ex.: 200,05 => 201

Utilização de multicontexto

Caso o usuário queira processar a contabilização / estorno por competência de contratos utilizando a opção de multi contexto, a mesma só estará disponível se o fracionamento de processos estiver habilitado.

O fracionamento de processos será efetuado para cada contexto a ser processado.

Conheça mais a opção de multi contexto [<<clicando aqui>>](http://tdn.totvs.com/pages/viewpage.action?pageId=466323952)!

## **TELAS DO PROCESSO**

A tela abaixo mostra a tela do processo de contabilização / estorno antes da execução ser iniciada.

Se o fracionamento de processos estiver habilitado, será mostrado o ícone e um texto os quais terão um hint explicativo indicando o número de contratos parametrizado para o fracionamento bem como o número máximo de processos por contexto.

Se o ambiente não for 3 camadas e o fracionamento de jobs estiver habilitado, ao clicar em executar, será exibida a seguinte mensagem para o usuário alertando do uso de recursos e processamento da máquina:

Caso o usuário esteja ciente e não queira que a mensagem apareça novamente, poderá ser marcada a opção "Não exibir novamente".

Ao clicar em "Sim", o processo será executado. Se clicar em "Não", a execução do mesmo será abortada.

Se a lista de processos retornada for igual a um, o sistema se comportará como se o fracionamento estivesse desabilitado (comportamento padrão de execução de processos do RM).

Se o fracionamento tiver sido realizado, isto é, caso o sistema tenha quebrado o processamento em mais de um processo filho, o sistema habilitará o botão "Monitorar processos em execução" que, ao ser clicado, fechará o formulário de contabilização / estorno e exibirá uma tela de acompanhamento da contabilização / estorno.

Tela de acompanhamento de contabilizações:

Caso o fracionamento não tenha sido realizado, o sistema exibirá a tela de processo com um botão para acessar o log das contabilizações realizadas.

Dica

Conheça mais a funcionalidade de Log de contabilizações [<<clicando aqui>>](http://tdn.totvs.com/pages/viewpage.action?pageId=465381685)!

Podemos acessar o acompanhamento da execução das contabilizações através do menu "Financeiro / Contábil → Contabilidade → Acompanhar execução das contabilizações".

O acompanhamento poderá ter os status abaixo os quais serão mostrados na coluna "Job" e no texto explicativo ao passar o mouse sobre a respectiva linha de fracionamento (acompanhamento).

1. **Aguardando execução:** Caso o processamento do fracionamento não tenha iniciado, o sistema exibirá a linha conforme abaixo:
2. **Executando**: Caso o fracionamento esteja sendo executado, o sistema exibirá a linha conforme abaixo:
3. **Executado com sucesso:** Caso o fracionamento tenha sido executado sem erros, o sistema exibirá a linha conforme abaixo:
4. **Executado com erros**: Caso o fracionamento da contabilização / estorno tenha sido executado com erros, o sistema exibirá a linha de execução

Interromper execução do processo

Caso seja necessário a execução do processo poderá ser interrompida para isso basta selecionar o processo desejado e depois clicar no ícone “Interrompe a execução do processo”, após o processo ser interrompido o mesmo poderá ser excluído.

Acessando os processos no gerenciador de jobs

Clicando no respectivo ícone de status ou dando duplo clique na linha de fracionamento, o sistema exibirá o processo no gerenciador de jobs, conforme abaixo:

Acessando o log de contabilização

De modo semelhante ao acesso de execução do job, clicando no ícone da coluna Log, será aberta a tela de Log detalhado da contabilização / estorno.

Uma vez clicado no ícone do Log, a tela de Log detalhado da contabilização / estorno será exibida. Esta por sua vez, permite avaliar o status de contabilização / estorno de cada contrato, pertencente  ao processamento em questão, conforme ilustra a imagem abaixo.

Contabilização

Estorno

**AMBIENTE TRÊS CAMADAS**

No processo executado em ambiente Três Camadas com Agendamento ao informar dados para contabilização e agendar a data e hora, a tela de contabilização será fechada e é possível acompanhar o inicio da execução das contabilizações através do menu "Financeiro / Contábil → Contabilidade → Acompanhar execução das contabilizações".

Na tela do acompanhamento o processo pai fica visível com a Data Programada e Status, após o inicio do processo o pai e concluído e são criados os processos filhos com o inicio da execução das contabilizações.

Caso seja necessário desabilitar a execução do processo não iniciado foi criado um ícone "Desabilita a execução do Processo" que poderá ser habilitado novamente no ícone "Habilita a execução do Processo".  
Para habilitar novamente o processo a data e hora que está sendo habilitado deverá ser anterior a data programada, caso seja superior o processo será automaticamente cancelado.

**1. Processo pai agendado, aguardando execução.**

**2. Processo pai concluído**

**3. Processos filhos iniciados**

**4. Processos desabilitado**

IMPORTANTE

O agendamento de execução de processos, no caso do fracionamento, agendará a execução do processo pai que, ao ser executado, criará e executará os processos filhos.
