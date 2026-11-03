---
content_hash: 9ccd0e0b7c1fc2f1d90a48ed87e6d7fc6250db84a9d23eff31b2b83d4044940b
fetched_at: '2026-06-29T00:11:06.935706+00:00'
page_id: '636964346'
product: rm
source: tdn-rm
title: Versão 12.1.34
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=636964346
version: 101
---

**PERT Web**

* **PERT Web (Beta)** - Disponibilizada a versão Beta do PERT Web, com nova interface que irá substituir o PERT atual a partir de versões futuras. O **PERT** **Web** é uma nova forma de acompanhar o planejamento e a evolução da obra com uma interface muito mais intuitiva e usual, estando disponível tanto no sistema como na web.

  Proporciona ao usuário o acesso rápido e eficiente ao andamento das atividades, bem como aos caminhos críticos do projeto, permitindo replanejamentos e trazendo o foco necessário para que não ocorram atrasos na Obra.

**Minhas Inspeções**

* **Plano de Criação de Inspeções**- Através do Plano de criação de Inspeções é possível definir regras para que as inspeções possam ser criadas automaticamente. [Saiba mais](https://tdn.totvs.com.br/pages/viewpage.action?pageId=622512467#DeckPlano-PlanoCadastro)
* **Criação de Workflow para as Inspeções de Qualidade**- Disponibilizada a criação de workflows para as Inspeções de Qualidade, nos quais serão definidos os fluxos pelos quais a inspeção irá passar e os critérios de aprovação/reprovação da mesma. [Saiba mais](https://tdn.totvs.com.br/pages/viewpage.action?pageId=622512467)
* **Visualização em Lista** - Foi criada, na tela de resposta da inspeção, a opção de visualização em lista, sendo possível responder fora da ordem sequencial. Além disso, nessa visão é possível exibir somente as perguntas que não foram preenchidas em cada inspeção. [Saiba mais](https://tdn.totvs.com.br/pages/viewpage.action?pageId=622512467&draft=true)

**Workflows de Aprovação do TCOP integrado ao TAA (RM Agilis)**

* **Pedido Extra** - Implementado o processo para geração de workflows de aprovação do TCOP integrado com o TAA (TOTVS Aprovações e Atendimento) para o Pedido Extra, possibilitando a aprovação através do APP Minhas Aprovações.  [Saiba mai](https://tdn.totvs.com/pages/viewpage.action?pageId=577914914)s

* **Contrato** - No processo para geração de workflows de aprovação do TCOP integrado com o TAA (TOTVS Aprovações e Atendimento) foi implementada a possibilidade de parametrizar para quais tipos de contrato (a pagar, a receber ou ambos) serão gerados os workflows de aprovação de Associação de itens do Contrato, Associação de Itens do Aditivo, Liberação de períodos do Contrato e Liberação do Adiantamento.  [Saiba mai](https://tdn.totvs.com/pages/viewpage.action?pageId=421385430)s

**Melhorias de Performance nas seguintes Funcionalidades:**

* **Cálculo do Projeto;**
* **Curva S;**
* **Comparador de Projetos;**
* **Tarefas - Atualização Múltiplas de Registros;**
* **Cópia de Calendário de Atividades;**
* **Alteração Geral de Composições;**
* **Contrato - Processo de Dedução de Produto no Faturamento Direto;**
* **Cronograma de Desembolso;**
* **Cronograma como Planilha.**

**Contratos**

* **Faturamento Direto - Alerta de Controle do Saldo no Contrato** - Disponibilizados campos na edição do contrato informando o valor total de faturamento direto solicitado, o total deduzido e o saldo ainda a deduzir no contrato. Além dessas informações, também passamos a emitir um alerta nas telas de Liberação de Período e Geração de Movimento, informando que o total de medições mais o total de faturamento direto está superior ao saldo do contrato, sendo assim necessário deduzir valores para não estourar o saldo contratual. [Saiba mais](https://tdn.totvs.com/display/LRM/Faturamento+Direto#1-3)

**Vínculo da Planilha de Atividades x Planilha de Serviços**

* Agora é possível através de parâmetro de projeto selecionar se a Associação de Serviço a Atividades será feita pela Quantidade ou por Percentual. Além disso, a associação entre Serviços e Atividades passa a ser realizada de N x N, isto é, um Serviço com várias Atividades ou uma Atividade com vários Serviços. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=421385088&draft=true)

**Saldo para Fluxo de Desembolso**

* Disponibilizada a opção de Rastreamento de movimentos, na etapa de cálculo de consumo de pedidos do Saldo para Fluxo de Desembolso, possibilitando a visualização de de toda a árvore de movimentos. [Saiba mais](https://tdn.totvs.com/display/LRM/Discriminar+Valores+-+Saldo+para+Fluxo+de+Desembolso+RM)

**App Minha Obra**

* **Ciclo de Transporte - Compartilhamento e Impressão dos Comprovantes de Carga e Descarga** - Implementada a geração, compartilhamento com o motorista (via bluetooth, whatsapp, e-mail, etc.) e/ou impressão de QR Code contendo os dados da carga, bem como a leitura do mesmo no ponto de descarga, alimentando os dados do apontamento sem a necessidade de inclusão manual dos dados e consequentemente proporcionando maior segurança à rotina. Implementados também o compartilhamento e emissão dos comprovantes da descarga. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=607612064#tudo-sobre-funcionalidades-interfaces)
* **Ciclo de Transporte**- Implementado o ciclo de transporte do tipo Distância Percorrida no processo de carga e descarga. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=607612064#tudo-sobre-funcionalidades-interfaces)
* **Informações do Aplicativo** - A partir de agora o ícone de Informações do App Minha Obra passa a ter um sinalizador, que estará ativo sempre que houverem apontamentos não sincronizados no coletor. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=607612064#tudo-sobre-instalacao)

**Mobilidade**

* **Ciclo de Transporte - Conciliar apontamentos** - Os apontamentos de descarga realizados através da leitura do QR Code são automaticamente vinculados ao seu apontamento de carga, eliminando, assim, a necessidade de conciliação manual dos mesmos. Estes apontamentos estarão conciliados logo após o seu sincronismo. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=607612064#tudo-sobre-funcionalidades-interfaces)
* **Ciclo de Transporte**- Implementado o ciclo de transporte do tipo Distância Percorrida no cadastro do Ciclo de transporte. [Saiba mais.](https://tdn.totvs.com/display/LRM/Cadastro+de+Ciclos+de+Transporte)
* **Ciclo de Transporte** - Adicionada a informação do tipo de ciclo no relatório de Ciclos de Transporte (TOPREL0029).

**Composição**

* **Alteração Geral de Composição** - A funcionalidade "Alteração Geral de Composições" passa a permitir ao usuário aplicar um Fator a Quantidade utilizando Fórmula. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=421385136)

**Integração**

* **Integração TCOP X Prevision** - Sabemos que o planejamento é uma informação muito importante para a obra e que se relaciona com diversas áreas como suprimentos e mão de obra, desta forma, fora implementado uma integração entre os sistemas Prevision e TOTVS Construção Obras e Projetos com o intuito de descomplicar o compartilhamento de informações entre os Cronogramas de forma rápida. [Saiba mais](https://tdn.totvs.com.br/pages/viewpage.action?pageId=661593488)
