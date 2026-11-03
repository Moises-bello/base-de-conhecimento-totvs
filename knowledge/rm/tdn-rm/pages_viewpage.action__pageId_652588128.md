---
content_hash: 922560d00ac2e43beb02ca45699caa2b1405db4a9477f5f6251e72a3117f2748
fetched_at: '2026-06-29T00:11:12.423003+00:00'
page_id: '652588128'
product: rm
source: tdn-rm
title: Análise de prescrição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=652588128
version: 91
---

AnáliseVisão Geral

## **01. VISÃO GERAL**

## 

A tela pode ser acessada através de Menu > Farmácia > Farmácia Clínica > Análise de prescrições

Ao acessar a tela de análise de prescrições, será exibida a tela com todas as prescrições liberadas pelo corpo clínico.

Serão exibidas as prescrições que possuem itens com o status "Pendente" e/ou prescrições que já possuem alguma análise iniciada ou concluída.

Campos da grid:

**Data** → Data em que o médico realizou a prescrição.

**Status** → Corresponde ao status da prescrição, possíveis valores: Pendente, Em Análise e Analisada.

**Situação da análise** → Está relacionada a vigência da prescrição médica com uma tolerância de 12hs para a validação. As prescrições Vencidas não poderão ser analisadas.

**Nome** → Nome do paciente.

**Leito** → Número do leito onde está o paciente.

**Situação** → É exibido o nível de urgência da prescrição, esse cálculo é realizado com base nos itens da prescrição, valores possíveis: Urgente, Atenção e Em Tempo.

O cadastro dos níveis de urgência é realizado em: Menu > Cadastro > Cadastros de estoque > Níveis de urgência.

**Prescritor** → Nome do médico responsável pela prescrição.

**Tipo da Prescrição** → Se a prescrição é médica ou oncológica.

**Unidade de atendimento** → Unidade foi realizado o atendimento do paciente.

**Responsável pela análise** → Funcionário que realizou a análise da prescrição.

## **02. Configuração para utilização da análise farmacêutica**

A configuração para utilização da análise de prescrições deverá ser realizada por Unidade de Atendimento.

Para isso, o usuário deve acessar: Menu > Cadastro > Uso Geral > Unidade de atendimento:

Na tela de unidade de atendimento, acessar a aba PEP RM > Prescrição médica

Caso o usuário deixe marcado a opção acima, todas as prescrições que forem criadas pelo médico, nessa unidade de atendimento, serão enviadas para a análise farmacêutica. 

## **03. Regra para iniciar análise da prescrição**

Para iniciar análise da prescrição o usuário deve realizar um duplo clique no registro, ou então, clicar no botão de edição na barra de ferramentas.

O usuário poderá analisar as prescrições que estejam com o status "pendente" ou "em análise".

Para as prescrições com o status em análise, quando o usuário tentar acessar será exibida a seguinte mensagem, que tem o objetivo de barrar a concorrência de tela:

No caso de clicar em "Não", ele será retornado para a tela de visão.

No caso de clicar em "Sim", todas as alterações que foram ou que estiverem sendo realizadas pelo outro usuário serão descartadas. O usuário que está acessando terá que iniciar a análise da prescrição do início. 

Analisar prescrição

## **01.****Analisar Prescrição**

## 

Para iniciar a análise da prescrição o usuário tem duas opções, na tela de visão da análise de prescrição realizar um duplo clique na prescrição que deseja analisar, ou selecionar uma prescrição e clicar no ícone de edição da barra de ferramentas.

Após selecionar a prescrição será exibida a tela de análise para farmacêutico realizar a validação, vide imagem abaixo da tela.

A tela é composta por:

1. Cabeçalho, nele deve constar as informações pessoais e do atendimento do paciente.
   1. Botão Prontuário, ao clicar será aberto o prontuário do paciente no PEP RM no browser padrão configurado na estação de trabalho.
   2. Classificação protocolo TEV - reflete a classificação do paciente no protocolo TEV no PEPRM (Alto, Médio ou Baixo risco e Não Classificado)
2. Informações de Peso, Altura e superfície corporal - extraídos da anamnese no PEPRM.
3. Grid Itens da Prescrição, onde serão exibidos todos os itens que foram prescritos para o paciente
4. No lado direito da tela, serão exibidas as informações do item que foi selecionado no grid Itens da Prescrição.
   1. Atalho para a calculadora do RM
   2. Parte superior serão exibidas as informações básicas do medicamento/material prescrito.
   3. Grid que exibirá os itens que estão associados ao medicamento.
   4. Botão "+ Informações" que exibe a prescrição completa do item selecionado.
   5. Campo de observação caso o farmacêutico deseje enviar alguma informação sobre o item.
   6. Nome do usuário e data/hora em que a análise foi realizada.
5. Botões de recusar, liberar c/ ressalva e liberar item.
6. Botão Desfazer, para reverter a ação atribuída ao item, caso a análise ainda não tenha sido finalizada.
7. Botões de liberar sem validar e finalizar análise.

Quando o medicamento for prescrito se necessário ou acm os associados serão exibidos sem que seja realizada o cálculo das configurações de consiste e múltipla, visto que, um item se necessário ou acm não possui horário definido.

## **02.** **Mais Informações**

Ao clicar no botão **+ Informações**, será exibida uma tela com dados adicionais sobre o "medicamento", "inalações" e "soros e componentes" além de alguns parâmetros clínicos referentes à prescrição.

MaisInformacoesMedicamentosSoros e componentesInalações

## **02.1.** **Parâmetros**

Na aba **Parâmetros**, estão disponíveis informações farmacêuticas que têm como objetivo fornecer uma **pré-visualização dos itens prescritos**, oferecendo ao farmacêutico insumos complementares que auxiliam em uma **análise mais precisa e assertiva**.

Esses parâmetros permitem personalizar o comportamento da tela de análise, destacando características importantes dos medicamentos, como classificações específicas (ex.: alta vigilância, vesicante), além de outras informações relevantes para a segurança e efetividade do atendimento clínico.

Para cada item haverá uma situação que pode ser: **Ok** ou **Alerta** (representado pelo ícone '!'), além de um campo descritivo:

Os parâmetros clínicos exibidos são:

* Alergia Medicamentosa;
* Interação Medicamentosa Grave;
* Faixa Terapêutica;
* Medicamento de alta vigilância;
* Medicamento Vesicante;
* Medicamento Irritante.

ParametrosAlergia Medicamentosa

A definição de alergia será relacionada ao paciente e por essa razão é classificada de acordo com a informação inserida no **Prontuário do Paciente**. Siga os passos abaixo:

1. **Acesse o prontuário do paciente:**
2. **Clicar em "+Alergias, Alertas, Isolamentos, Riscos e Problemas":**

    3.  **Aba "Alergias". Realizar o cadastro da alergia do paciente.**

4. **Caso o medicamento cadastrado seja prescrito para este paciente o parâmetro será marcado como alerta.**

Interação Medicamentosa Grave

Para definir uma **Interação Medicamentosa Grave**, siga os passos abaixo:

1. **Acesse o cadastro de interações medicamentosa:**  
   Menu → Cadastros → Cuidados com o Paciente → Prescrição Médica → Interação Medicamentosa
2. **Criar um resgistro de interação medicamentosa:**  
   Na tela que será aberta o usuário deve:

   1. Selecionar o tipo de interação Princípio Ativo x Princípio Ativo.
   2. Definir os dois princípios ativos que possui interação.
   3. Definir a classificação de risco com "Grave".
3. **Salve as alterações:**  
   Após marcar a opção, clique em **Salvar** para registrar a configuração.

Observação

A exibição do parâmetro como alerta ocorre somente quando a classificação de risco da interação medicamentosa estiver configurada como 'Grave'.

Faixa Terapêutica

Para configurar a **Faixa Terapêutica** do item, siga os passos abaixo:

1. **Acesse o cadastro de produtos:**  
   Menu → Cadastro → Estoque → Produtos
2. **Localize o produto desejado:**  
   Utilize os filtros disponíveis para buscar o item que será classificado.
3. **Abra o anexo 'Informação TOTVS Saúde':**  
   Com o produto selecionado, clique no botão **Anexos** e escolha **Informação TOTVS Saúde**.
4. **Abra o anexo 'Doses máximas e mínimas':**  
   Com o produto selecionado, clique no botão **Anexos** e escolha **Doses máximas e mínimas**.
5. **Configure a dose máxima e mínima do produto:**  
   Nessa tela que será aberta o usuário poderá selecionar a unidade de medida, e definir a dose máxima e mínima.
6. **Salve as alterações:**  
   Após marcar a opção, clique em **Salvar** para registrar a configuração.
Medicamento de alta vigilância

Para classificar um item como medicamento de **Alta Vigilância**, siga os passos abaixo:

1. **Acesse o cadastro de produtos:**  
   Menu → Cadastro → Estoque → Produtos
2. **Localize o produto desejado:**  
   Utilize os filtros disponíveis para buscar o item que será classificado.
3. **Abra o anexo 'Informação TOTVS Saúde':**  
   Com o produto selecionado, clique no botão **Anexos** e escolha **Informação TOTVS Saúde**.
4. **Vá até a aba 'Identificação II':**  
   Navegue até a aba **Identificação II**, onde estão localizadas as opções de classificação.
5. **Marque a opção 'Medicamento de alta vigilância':**  
   Ative o checkbox correspondente à classificação **Alta Vigilância**.
6. **Salve as alterações:**  
   Após marcar a opção, clique em **Salvar** para registrar a configuração.

Observação

A opção **Medicamento de alta vigilância** somente estará disponível se o tipo do item estiver definido como Medicamento.

Medicamento Vesicante

Para classificar um item como medicamento de **Vesicante**, siga os passos abaixo:

1. **Acesse o cadastro de produtos:**  
   Menu → Cadastro → Estoque → Produtos
2. **Localize o produto desejado:**  
   Utilize os filtros disponíveis para buscar o item que será classificado.
3. **Abra o anexo 'Informação TOTVS Saúde':**  
   Com o produto selecionado, clique no botão **Anexos** e escolha **Informação TOTVS Saúde**.
4. **Vá até a aba 'Identificação II':**  
   Navegue até a aba **Identificação II**, onde estão localizadas as opções de classificação.
5. **Marque a opção 'Medicamento Vesicante':**  
   Ative o checkbox correspondente à classificação **Vesicante**.
6. **Salve as alterações:**  
   Após marcar a opção, clique em **Salvar** para registrar a configuração.

Observação

A opção **Medicamento Vesicante** somente estará disponível se o tipo do item estiver definido como Medicamento.

Medicamento Vesicante

Para classificar um item como medicamento de **Irritante**, siga os passos abaixo:

1. **Acesse o cadastro de produtos:**  
   Menu → Cadastro → Estoque → Produtos
2. **Localize o produto desejado:**  
   Utilize os filtros disponíveis para buscar o item que será classificado.
3. **Abra o anexo 'Informação TOTVS Saúde':**  
   Com o produto selecionado, clique no botão **Anexos** e escolha **Informação TOTVS Saúde**.
4. **Vá até a aba 'Identificação II':**  
   Navegue até a aba **Identificação II**, onde estão localizadas as opções de classificação.
5. **Marque a opção 'Medicamento Irritante':**  
   Ative o checkbox correspondente à classificação **Irritante**.
6. **Salve as alterações:**  
   Após marcar a opção, clique em **Salvar** para registrar a configuração.

Observação

A opção **Medicamento Irritante** somente estará disponível se o tipo do item estiver definido como Medicamento.

Liberar

## **01.** **Liberar**

## 

Para liberar o item o farmacêutico deve selecionar o(s) item(s) no grid Itens da Prescrição e clicar no botão "Liberar".

Após clicar no botão liberar, o item será marcado como liberado e no grid será exibido será exibido o novo status:

Para confirmar a liberação do item é necessário finalizar a análise.

Liberar com ressalva

## **01.** **Liberar com ressalva**

## 

Para liberar o item com ressalva o farmacêutico deve selecionar um item no grid da esquerda e clicar no botão "Lib. C/Ressalva".

Após clicar no botão será aberto a tela para o farmacêutico definir o motivo pelo qual está liberando o item com ressalva e acrescentar uma observação/justificativa, caso julgue necessário. Essas informações serão enviadas ao médico prescritor.

Após o preenchimento das informações é necessário clicar no botão confirmar.

Após clicar no botão confirmar, o farmacêutico retornará para a tela de análise, no grid será exibido o status liberado com ressalva:

Para confirmar a liberação do item com ressalva é necessário finalizar a análise.

Recusar item

## **01.****Recusar item**

Para realizar a recusa do item o farmacêutico deve selecionar um item no grid da esquerda e clicar no botão "Recusar".

Após clicar no botão recusar será aberto a tela para o farmacêutico definir o motivo pelo qual está recusando o item e escrever alguma observação ou justificativa, caso necessário. Essas informações serão enviadas ao médico prescritor.

Após o preenchimento das informações é necessário clicar no botão confirmar.

Após clicar no botão confirmar, o farmacêutico retornará para a tela de análise, no grid será exibido o status recusado:

Após recusar o item ele será exibido no PEPRM com o status Item Recusado.

Para confirmar a recusa de um item é necessário finalizar a análise.

Desfazer análise do item

## **01.****Desfazer análise do item**

## 

Para desfazer uma análise que ainda não foi finalizada, o farmacêutico deve selecionar um item no grid de Itens da prescrição e clicar no botão "Desfazer".

Após clicar no botão desfazer será aberto um popup para o farmacêutico confirmar a ação.

Caso clique no botão NÃO, nada será feito e retornará para a tela de análise.

Caso clique em SIM, irá retornar para a tela de análise de prescrição e o status do item que foi selecionado retornará para o status de "Pendente".

Os itens que já tiveram a análise confirmada não poderão retornar para o status de pendente.

Finalizar análise

## **01. Finalizar análise**

## 

Após a análise do farmacêutico, e atribuição de ações para os itens o usuário poderá clicar em "Finalizar Análise" - *nota*: *não é necessário que toda a prescrição seja avaliada para que a análise da prescrição seja finalizada, importante ressaltar que a análise pode ser realizada item a item*, nesse momento o sistema irá fazer uma validação e verificar se durante a análise do farmacêutico foi alterado algo na prescrição pelo médico.

Caso tenha sido alterado algo na prescrição será exibida uma mensagem para o usuário, com as seguintes opções:

Caso SIM, a tela será atualizada com as novas informações e o que foi analisado será descartado.

Caso NÃO, seguirá a finalização da análise, como descrito nos trechos abaixo.

Ao clicar no botão **Finalizar análise** será exibida uma mensagem de confirmação, caso não tenha alteração pelo médico como descrito acima:

Clicando no botão **Sim** a prescrição será finalizada e seu status passará a ser **Analisada**, caso todos os itens tenham sido analisados ou somente. Se ainda houverem itens não suspensos que necessitem de avaliação, o status da prescrição segue como Pendente.

O status dos itens serão atualizados de acordo com a avaliação que foi realizada pelo farmacêutico.

Clicando no botão **Não** nenhuma ação será realizada.

Rastreabilidade das movimentações

## **01. Rastreabilidade das movimentações**

A função de rastreabilidade das movimentações exibe os itens da prescrição, o seu status final, o usuário que realizou a análise e em qual horário.

Essa função está nos anexos, ela pode ser acessada via tela de visão das prescrição ou na tela que onde se realiza a análise da prescrição:

Após selecionar uma prescrição e em seguida "Rastreabilidade das Movimentações", será aberta uma aba onde o usuário poderá validar todas as informações relacionada aos itens da prescrição, conforme imagem abaixo.

Na aba será exibido, nome do medicamento, status do item referente a análise da prescrição, responsável pela análise e Data/horário da análise.

Quando um item estiver ainda com o status pendente, não será exibido o responsável pela análise e Data/Horário da análise.

Relatório de validação farmacêutica

## **01. Relatório de validação farmacêutica**

O relatório de validação farmacêutica exibe o tempo que o usuário levou para executar os passos da análise de prescrição. Ele é acessado através do processo indicado abaixo.

Será exibida uma tela para informar o tipo do relatório e as datas de início e fim que serão consideradas.

Os tipo de exibição podem ser:

1 - **Por paciente**: lista cada prescrição a abaixo todos os usuários e o tempo para a análise.

2 - **Por usuário**: lista cada usuário e abaixo todas as prescrições e o tempo para a análise.

O usuário deve ter permissão para acessar esse processo.

Os relatórios SAUREL0040 e SAUREL0041 devem estar importados no ambiente do RM.

Assinatura digital

## **01. Visão Geral**

Caso o RM esteja devidamente configurado ao final da análise da prescrição o farmacêutico poderá assinar digitalmente a análise realizada. O processo é automático e o usuário deverá apenas estar autenticado no TAE. A assinatura está restrita apenas a assinatura digital da Totvs através do TAE ( Totvs Assinatura Digital ), para mais informações acessar o link   
Caso esteja parcialmente configurado ou o usuário não autentique o processo continuará sem bloqueio e o usuário deverá em outro momento assinar a análise da prescrição.

## **02. Configuração RM Saúde**

Para habilitar o processo, além da configuração do TAE deverá ser realizada a configuração por unidade de atendimento. Deverá ser informados o modelo da assinatura e o relatório para submeter a assinatura. O RM dispõe de um relatório padrão ( SAUREL0045 ).

**Configuração Unidade de atendimento**

**Modelo Relatório padrão**

**Modelo documento assinado**

Ao final de todos os documentos assinados no padrão TAE - assinatura digital será acrescentada uma página com as informações similares a imagem abaixo.

Ao finalizar a análise será exibido ao usuário um formulário de login para que sejam informadas as credenciais do sistema TAE para que seja validada a assinatura digital, o prazo de login  é de 12h, após esse período ou caso o usuário efetue logoff serão solicitadas novamente as credenciais do TAE.

Notificação ao médico prescritor

## **01. Visão geral**

Ao finalizar uma análise que possua itens analisados com os status Recusado e/ou Liberado com ressalva (via parâmetro ). A notificação será no PEPRM por prescrição, no painel de "Prescrições Anteriores" onde o médico prescritor precisa ser notificado para que possa reavaliar a prescrição e realizar os ajustes, caso necessário.

Será exibido um alerta correspondente à um círculo vermelho com uma exclamação.

## **02. Notificação por item**

O médico ao abrir a tela de edição do item no PEP RM irá visualizar uma faixa com cores variadas de acordo a finalização da análise. Vermelho para os itens recusados, azul para itens liberados com ressalva e verde para os itens liberados.

## **02.01. Medicamento Liberado**

Ao liberar o item na análise farmacêutica, os mesmos serão exibidos conforme imagem abaixo no PEPRM.

Itens liberados apresentarão a faixa da análise para registro de informações. Esse status não gera nenhum tipo de notificação ao médico. 

## **02.02. Medicamento Liberado com ressalva**

Ao liberar o item com ressalvas na análise farmacêutica, os mesmos serão exibidos conforme imagem abaixo no PEPRM.

## **02.03. Medicamento Recusado**

Ao recusar o item na análise farmacêutica, os mesmos serão exibidos conforme imagem abaixo no PEPRM.

## **03. Ações do prescritor após análise farmacêutica**

## **03.01. Visão geral**

Após a análise da prescrição pela farmácia o médico é notificado podendo seguir com o item com ou sem alterações. Essas ações são as mesmas para medicamentos, inalações e soros e componentes. Os processos de suspensão e atualização do item são os mesmo que já possuem no fluxo do PEPRM.

## **03.02. Suspensão**

A qualquer instante o médico prescritor pode suspender os itens dentro do período de validade da prescrição, para os itens analisados com o status recusado ou liberado com ressalva ao realizar a suspensão, os alertas associados ao item deixarão de ser exibidos. Importante salientar que a faixa com o resumo da análise sempre será exibida.

## **03.03. Reenvio do mesmo item**

Para itens recusados, caso o médico prescritor opte por seguir com a mesma prescrição com ou sem alteração deverá abrir o item e informar uma justificativa. Essa informação é obrigatória, e após atualizar as informações ele deverá liberar o item novamente.

## **03.04. Ciente da ressalva**

Os itens liberados com ressalva serão exibidos ao médico prescritor e o mesmo poderá suspender ou alterar conforme descrito nos passos anteriores. Poderá apenas informar que está ciente da ressalva e desativar os alertas associados ao item. Após a confirmação a mensagem a seguir é exibida: Você marcou ciente da ressalva. Não será exibida mais a notificação para este item.

## **03.05. Obrigar Ciente da Ressalva ao Liberar ou Copiar prescrições**

Parâmetro Unidade de atendimento  > Prescrição Médica > **Obriga Aceite Médico para itens Liberado com Ressalva.**

Com o parâmetro ativo, caso exista na prescrição algum item com status **“Liberado com Ressalva”** pela Farmácia Clínica, será exibida uma mensagem de bloqueio, impedindo o médico de liberar novas prescrições ou copiar o item liberado com ressalva.

A mensagem deixará de ser exibida após o médico acessar o item e registrar a ciência da ressalva.

Prescrições de Oncologia

## **01. Visão Geral**

Também é possível realizar usar o RM para realizar análise de prescrições de oncologia.

## **02.****Configuração para utilização da análise farmacêutica de prescrições de oncologia**

A configuração para utilização da análise de prescrições de oncologia deverá ser realizada por Unidade de Atendimento.

Para isso, o usuário deve acessar: Menu > Cadastro > Uso Geral > Unidade de atendimento. Na tela de edição acessar a aba Prontuário Eletrônico > Prescrição médica

Ativar a caixa de seleção: Utiliza análise farmacêutica de prescrições de oncologia.

## 

## **03.** **Informações da** **prescrição de oncologia na****análise farmacêutica**

Na análise farmacêutica são exibidas as seguintes informações referente a prescrições de oncologia

* Protocolo
* Finalidade
* Fase 1
* Ciclo
* Dia

Também são exibidos os seguintes campos referente aos itens da prescrição oncológica

* Dose/AUC alvo
* Categoria
* Administração
* Tempo de administração
* Redução da dose
