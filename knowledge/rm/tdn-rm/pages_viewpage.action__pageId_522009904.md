---
content_hash: cecef78ce3ef3b383ec1725e40f4356366226ab4b7bfd1c8b00544c5df1297d4
fetched_at: '2026-06-29T00:10:31.872012+00:00'
page_id: '522009904'
product: rm
source: tdn-rm
title: Solicitação de Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=522009904
version: 43
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Telas utilizadas**
3. **Considerações**
4. **Prioridade do exame**
5. **Atualização V.2506**
6. **Tempo de alerta de exame**
7. **Fluxo de solicitação de exames via prescrição médica**
   1. **Impressão automática da solicitação de exames ao liberar a prescrição**
   2. **Impressão da solicitação de exames: configuração do relatório**

Solicitação de examesVisão Geral

## **01. VISÃO GERAL**

Esta tela tem como objetivo registrar a solicitação de exames do paciente.

Telas utilizadas 

## **02. TELAS UTILIZADAS**

* Ao acessar o menu "Solicitação de exames" uma listagem com o histórico de solicitações será exibida. Para iniciar uma nova solicitação clique no botão "+ Novo".

Ao iniciar uma nova solicitação, o sistema apresenta o formulário com todos os campos desbloqueados, permitindo o preenchimento manual dos dados ou a utilização de de modelos previamente salvos. Durante a edição, é possível excluir o rascunho criado, salvar o formulário como modelo, finalizar ou finalizar e imprimir.

**Ações dos botões:**

* **Excluir rascunho:** o botão fica disponível para uso enquanto a solicitação de exames ainda não é finalizada. Após a conclusão do documento, não será mais possível excluí-lo como rascunho.
* **Usar modelo:** busca os modelos de solicitações de exames salvos previamente.
* **Salvar modelo**: salvará informações da tela para usar como modelo em futuras solicitações de exames.
* **Finalizar:** finaliza a solicitação de exames. Para finalizar a solicitação de exames é necessário preencher todos os campos obrigatórios. Após a finalização, o documento não poderá mais ser alterado ou editado.
* **Finalizar e imprimir:** finaliza e também gera o relatório da solicitação. Para finalizar a solicitação de exames é necessário preencher todos os campos obrigatórios. Após a finalização, o documento não poderá mais ser alterado ou editado.
* **Impressão TISS:** o botão "Impressão TISS" é habilitado após a finalização da solicitação.

**Comportamento da tela**

* Após preencher qualquer campo as informações são salvas automaticamente, [saiba mais sobre salvamento automático](http://tdn.totvs.com/pages/viewpage.action?pageId=496017290).
* Os campos de texto utilizam o editor de texto, saiba mais sobre o editor de texto.

## 

* Para adicionar um ou mais exames, selecione um ou mais exames na caixa de seleção "Adicionar exames" e clique no botão "Adicionar".

* Para adicionar um ou mais grupos de exames, selecione o grupo na caixa de seleção "Adicionar grupo exames" e clique no botão "Adicionar".

* Para excluir um exame da lista de exames da solicitação, basta clicar na lixeira ao lado do campo de quantidade no exame.

* A partir da versão 12.1.2602, um novo checkbox "Obs" foi implementado para adicionar observações individualmente para cada exame adicionado. O novo campo tem um limite de 2000 caracteres.
* As observações inseridas nesse campo também serão exibidas no RM.

Ao finalizar solicitação, o usuário poderá informar se os exames serão realizados internamente ou externamente. Se a opção "Interno" for selecionada, a solicitação será enviada para a unidade de diagnósticos no RM. Após finalizar solicitação, a timeline de solicitações de exames será exibida. 

As observações inseridas no novo campo utilizando o checkbox "Obs" poderão ser visualizadas no RM através da tela de "Pedidos de exame".

Nas configurações da unidade de atendimento no RM, na aba "Prontuário Eletrônico" e "Solicitação de exames", são utilizados dois parâmetros:

1. Habilitar modal para seleção de realização dos exames?  
  1.1. Se sim: Sempre que o usuário clicar em finalizar ou finalizar e imprimir, deverá ser aberta a modal onde o usuário poderá selecionar quais exames que serão realizados internamente e quais exames serão realizados externamente.  
  1.2. Se não: O sistema deverá considerar o comportamento padrão.

2. Definir padrão de exames na solicitação:  
  2.1. Se Interno: Caso o usuário não aponte uma definição para o item 1.1. , os itens deverão sempre seguir o mesmo fluxo dos exames solicitados na prescrição médica. Caso o usuário aponte o parâmetro do item 1.1. , a modal deverá já ser habilitada com todos os itens marcados como Interno.   
  2.2. Se externo: Caso o usuário não aponte um definição para o item 1.2. , não deverá ocorrer nenhum lançamento/validação pelo sistema. Apenas realizar a finalização ou finalização/impressão do registro. Caso o usuário aponte o parâmetro do item 1.1. , a modal deverá já ser habilitada com todos os itens marcados como externo.

**CONFIGURAÇÃO DO HORÁRIO DE ROTINA:**

Para exames de rotina, a hora de execução para os pedidos de exame na Unidade de diagnóstico são classificadas de acordo com o horário de rotina cadastrado na unidade de atendimento que realiza o respectivo exame.

O horário de rotina pode ser cadastrado nas configurações da unidade de atendimento:

**Unidade de Atendimento > Prontuário Eletrônico > Solicitação de Exames > Horário rotina**

Os horários programados dos pedidos de exames com a opção ROTINA marcada, deverão vir de acordo com o horário de rotina da unidade de atendimento do exame

Considerações

## **03. Considerações**

Listamos algumas mensagens que podem ocorrer durante a utilização da rotina.

1. **Mensagem:** Não foi possível realizar a solicitação.   
   **Detalhe**: O atendimento selecionado é do tipo externo e possui mais de 48 horas de lançamento e não foi possível realizar a solicitação.   
   **Possíveis causas:** atendimento interno com data de saída ou atendimento externo com mais de 48 horas aberto. Atendimento com status diferente de "Em Elaboração". Parcial liberada, Finalizada ou Cancelada.

**ATENÇÃO**:

**Caso** **alguma mensagem de alerta de horário inválida for apresentada, verifique se os campos de horário de rotina estão corretamente configurados na unidade.**

Exemplo da mensagem de erro:

Prioridade do exame

## **04. Prioridade do Exame**

A página de solicitação de exames do PEP passou por atualização visual e foram adicionadas novas funções, como as opções de definir a prioridade do exame, data e hora:

* Ao escolher a prioridade "Programado", os campos de data e hora permanecem habilitados para seleção. No RM, na aba de "Exames", o tipo de exame ficará marcado como "Normal" e será exibido a data e hora selecionadas no PEP.
* Ao escolher a prioridade "Rotina", apenas o campo de data permanece habilitado para seleção. No RM, na aba de "Exames", o tipo de exame ficará marcado como "Normal" e será exibido apenas a data selecionada no PEP.
* Ao escolher a prioridade "Imediato", os campos de data e hora ficarão desabilitados para seleção. No RM, na aba de "Exames", o tipo de exame ficará marcado como "Emergência", sem a data e hora.

Foi disponibilizado um novo parâmetro no sistema que permite definir a prioridade padrão para solicitações de exames por unidade de atendimento, a **partir da versão 2602.**

Essa configuração tem como objetivo agilizar o processo de lançamento de exames, reduzindo a necessidade de seleção manual da prioridade a cada inclusão.

Na aba **Exames** foram incluídos os campos “**Prioridade padrão para solicitação de exames**” e “**Prioridade padrão para exames na prescrição**”, que permitem definir um valor padrão entre Programado, Rotina ou Imediato. Quando configurada para uma unidade de atendimento, essa prioridade será automaticamente atribuída aos exames no momento de sua inclusão na tela de solicitação, podendo ainda ser ajustada manualmente, se necessário.

Atualização V.2506

## **05. Atualização V.2506**

##### **Funcionalidade disponível a partir da versão 12.1.2506.**

A partir da versão 12.1.2506, o campo "Material" foi incluído no formulário de solicitação de exames. 

* Ao clicar no campo "Material", uma lista de materiais disponíveis para o respectivo exame será exibida.
Tempo de alerta de exame

## **06.** **Tempo de alerta de exame**

##### **Funcionalidade disponível a partir da versão 12.1.2602.**

Para garantir a segurança do paciente e evitar solicitações duplicadas, o alerta de último exame solicitado passa a ser persistente nas telas de Prescrição Médica e Solicitação de Exames.

1. **Persistência:** O alerta não desaparece automaticamente após alguns segundos. Ele permanece visível na tela por até 24 horas ou até que o profissional de saúde interaja com ele.
2. **Ação Obrigatória:** Para fechar a notificação, o usuário deve clicar manualmente no ícone "X" ou no botão "Fechar".

Nota de Configuração: A regra pode ser consultada ou parametrizada em:  
RM -> Cadastro -> Cuidado com o Paciente -> Cadastro Alerta Exame.

Fluxo de Solicitação de Exames via Prescrição Médica 

## **07.** **Fluxo de solicitação de exames via prescrição médica**

O fluxo de Solicitação de Exames via Prescrição Médica permite que os exames prescritos pelo profissional assistencial sejam automaticamente registrados na funcionalidade de Solicitação de Exames após a liberação da prescrição médica.

Nesses casos, não é permitido incluir novos exames, editar, excluir ou suspender exames diretamente na tela de Solicitação de Exames.

Todas as alterações devem ser realizadas na própria prescrição médica. Na impressão da prescrição os exames vão sair impressos como pertencentes a prescrição porém, se pelo fluxo da instituição é necessário a impressão da solicitação de exames a ação deve ser feita na funcionalidade pertinentes (Solicitação de Exames e Procedimentos)

As informações inseridas nos exames poderão ser visualizadas no RM através da tela de pedidos de exame.

Na funcionalidade de Solicitação de Exames, será permitido apenas visualizar as informações registradas e realizar a impressão do relatório.

Essa restrição assegura conformidade com o fluxo assistencial, evita inconsistências entre prescrição e solicitação e garante maior segurança no controle das informações.

## **7.a Impressão automática da solicitação de exames ao liberar a prescrição**

##### **Funcionalidade disponível a partir da versão 12.1.2510.**

Agora será possível configurar por meio de parâmetro, a impressão automática do relatório da solicitações de exame quando houver exames vinculados à liberação da prescrição.  
Com essa configuração habilitada em uma unidade de atendimento que não utiliza aprazamento e checagem, o relatório de solicitações de exames será gerado automaticamente ao **liberar a prescrição** ou ao **imprimir a liberação da prescrição** na tabela lateral de "Prescrições anteriores", desde que existam exames associados.

Na tabela lateral de "Prescrições anteriores", será impressa apenas a solicitação de exames referente à liberação selecionada.Ao clicar em imprimir no ícone da prescrição completa, o relatório individual da solicitação de exames não será gerado junto ao relatório principal com todos os itens da prescrição. Essa mesma regra também se aplica ao botão “Imprimir” localizado ao final da tela, que também realiza a impressão da prescrição completa e não gera o relatório individual da solicitação de exames.

Para unidades que utilizam aprazamento e checagem, a liberação da prescrição não dispara automaticamente a geração do relatório de exames. Esse fluxo é condicionado àliberação do aprazamento, etapa necessária para a consolidação da data e hora da realização do exame. Portanto, o relatório estará disponível somente após a efetivação do aprazamento.

## **7.b Impressão da solicitação de exames: configuração do relatório**

O relatório da Solicitação de Exames apresenta todas as informações registradas em tela, contemplando os exames exatamente conforme cadastrados na prescrição médica.

Quando a instituição possuir assinatura digital habilitada, o relatório poderá conter a assinatura digital do profissional prescritor, conforme configuração vigente.

Para melhor organização do documento impresso, os exames são apresentados de forma segmentada: os exames laboratoriais são exibidos em uma página e os exames de imagem em página distinta. Essa separação proporciona maior clareza na leitura e melhor aderência aos fluxos operacionais dos setores executantes.

RM > Aba Gestão> RM Reports> Selecione o relatório > SubDetalhe2> Grade de propriedade> Quebra de Página.

O relatório comtempla as informações de dados do paciente, dados do solicitante, indicação clínica, orientações, prioridade, data/hora, quantidade, material e observação dos exames.
