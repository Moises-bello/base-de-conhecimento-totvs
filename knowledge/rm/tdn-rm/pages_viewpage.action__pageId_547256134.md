---
content_hash: a446d7ac3930dfa2637f4e0b898c276656a090bae1a68aa35d45b3a24c154c2d
fetched_at: '2026-06-29T00:10:42.730193+00:00'
page_id: '547256134'
product: rm
source: tdn-rm
title: Reajuste Revitalizado / Processo de Reajuste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547256134
version: 35
---

Com o reajuste revitalizado o processo pode ser executado e agendado de três formas, são elas:

CardstrueContrato1- Contratos de Venda |

Novo processo de reajuste na visão de vendas permitirá maior dinamismo para o usuário,

Através da tela de Cadastro de **Contratos de Venda**: Selecione o contrato desejado vá em **Processos>> Reajuste>> Reajustar Venda**.

Parâmetros do processo:

* Data do Reajuste;
* Reajustar Até o Dia de Vencimento da Parcela;
* Reajustar no último dia do mês;
* Vendas Distratadas;
* Contabilizar o reajuste sempre no mês atual;
* Contabilizar o reajuste no último dia do mês;
* Reajustar Somente Parcelas com Vencimento no Mês de Reajuste;
* Enviar o reajuste mês a mês para o Financeiro/Contábil;
* Apagar o Log do Reajuste Anterior Antes de Iniciar o Novo Reajuste (Se houver alteração de parâmetro que impacta o reajuste, o usuário deverá reajustar toda a base e marcar essa a opção).

Importante

Quando marcar esse parâmetro o sistema deixará de voltar o reajuste para o início do contrato e passa usar a data base do último reajuste aplicado na base.  Caso haja mudança de parâmetros ou índices que impactam o reajustes já executados, o mesmo deve ser executado novamente e marcado a opção de apagar o data base para o sistema utilizar a nova parametrização

***[Para maiores informações sobre os Parâmetros acima, CLIQUE AQUI !!](https://tdn.totvs.com/pages/viewpage.action?pageId=552575670)***

* **Apagar o Log do Reajuste Anterior Antes de Iniciar o Novo Reajuste**

             Apaga o log dos Reajustes anteriores antes de iniciar o novo Reajuste.

**Os parâmetros poderão vir marcados/desmarcados por default de acordo com a parametrização realizada nos .**

**Importante!**

Caso durante a execução deste processo o sistema exiba a mensagem abaixo, é preciso habilitar o [***controle de histórico de alterações***](https://tdn.totvs.com/pages/viewpage.action?pageId=421388636) no módulo financeiro, para dar continuidade ao reajuste das vendas.

*Para executar o processo, o parâmetro [Habilitação do Controle de Histórico de Alterações de Lançamentos/Extratos de Caixa] deve estar configurado como [Habilita controle para todos os módulos] ou [Habilita controle somente para Totvs Incorporação].*

*O caminho para acessar e ajustar este parâmetro é:*  
*Módulo BackOffice > Gestão Financeira > Utilitários > Habilitação Histórico de Alterações*

Esta ação é necessária para garantir a consistência das informações no sistema.

Global2- Reajuste Global |

Menu **Venda>> Reajuste**.

Parâmetros do processo:

  

* Empreendimentos;
* Data do Reajuste;
* Reajustar Até o Dia de Vencimento da Parcela;
* Reajustar no último dia do mês;
* Reajustar Somente Parcelas com Vencimento no Mês de Reajuste;
* Vendas Distratadas;
* Contabilizar o reajuste sempre no mês atual;
* Contabilizar o reajuste no último dia do mês;
* Enviar o reajuste mês a mês para o Financeiro/Contábil;
* Apagar o Log do Reajuste Anterior Antes de Iniciar o Novo Reajuste (Se houver alteração de parâmetro que impacta o reajuste, o usuário deverá reajustar toda a base e marcar essa a opção).

Filtros:

Os filtros serão utilizados para demonstrar os contratos de venda na tela do reajuste, são eles: **Data Inicio/Data Fim e****Nro Venda**. Após aplicar os filtros os contratos de venda deverão ser selecionados para que o processo seja executado.

Utilizando o botão **Reajustes Pendentes** é possível acessar a tela que demonstra todos os reajustes pendentes de execução.

Os parâmetros poderão vir marcados/desmarcados por default de acordo com a parametrização realizada nos [Parâmetros Gerais](https://tdn.totvs.com/pages/viewpage.action?pageId=552575670).

O processo pode também pode ser chamado através do botão **Executar** a direita do sistema buscando por **Reajuste Global de Vendas**.

 Está disponível também a tela de visualização de reajustes já executados, um log no novo reajuste que mostra ao cliente de uma forma simples, quais foram os reajustes que deram erro e precisam ser revistos.

Agendamento3- Agendamento

O processo de agendamento do reajuste global de vendas é executado por empreendimento, sendo assim pode ser criado um agendamento para cada empreendimento especifico e cada agendamento com sua devida parametrização.

Os parâmetros desta tela são:

* Reajustar Até o Dia de Vencimento da Parcela;
* Reajustar no último dia do mês;
* Contabilizar o reajuste sempre no mês atual;
* Contabilizar o reajuste no último dia do mês;
* Vendas Distratadas;
* Enviar o reajuste mês a mês para o Financeiro/Contábil;
* Reajusta Somente Contratos Pendentes de Reajuste para o Mês Selecionado;
* Apagar o Log do Reajuste Anterior Antes de Iniciar o Novo Reajuste (Se houver alteração de parâmetro que impacta o reajuste, o usuário deverá reajustar toda a base e marcar essa a opção).

Parâmetros de data:

* Mês Corrente;
* Próximo Mês;
* Data Específica (o usuário terá que informar uma data).

Atenção!

**Para que o processo de agendamento funcione é necessário que o ambiente RM esteja parametrizado como N camadas.**

**Para maiores informações acesse: [Configuração N Camadas](https://tdn.totvs.com/pages/viewpage.action?pageId=236432384).**

Foram criados novas permissões para gerenciar os novos parâmetros de reajuste
