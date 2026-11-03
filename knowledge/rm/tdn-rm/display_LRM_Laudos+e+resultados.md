---
content_hash: b39880b20944d51d133422a3f28a78c4da5dafad4ede848db9aea45064888cab
fetched_at: '2026-06-29T00:10:20.244304+00:00'
page_id: '490323941'
product: rm
source: tdn-rm
title: Laudos e resultados
type: documentation
url: https://tdn.totvs.com/display/LRM/Laudos+e+resultados
version: 62
---

## **ÍNDICE**

1. **Visão Geral**
2. **Anexos**
3. **Processos**
4. **Preenchimento do Laudo**
5. **Status Pedido Exame**
6. **Tabelas utilizadas**

sumarioVisão Geral

## **01. VISÃO GERAL**

Esta funcionalidade exibe os exames dos pedidos realizados pelo RM, de acordo com filtro utilizado. Nela você consegue realizar algumas ações para um ou diversos exames ao mesmo tempo.

Anexos:

* Pedido de Exame
* Arquivos
* Exibe todos os exames de pedido selecionado
* Controle de Documentos
* Histórico de alterações de Laudos
* Integração
* Geração de Exceção
* Log de alterações

Processos:

* Entrega de Material Pendente
* Executar ação desejada(Múltiplos Registros)
* Reemitir etiquetas
* Reemitir pedido de exame
* Link Laudos
* Triagem amostras
* Recoletar amostras
* Troca de informações com a Matrix
* Verificar Pendências  
    
  ícone correspondente à tela de Controle de Pedido de Exames:

* Na visão a coluna Unidade Atendimento irá exibir:   
  -   para atendimento externo: a unidade de atendimento do exame    
  - para atendimento interno:  a unidade de atendimento do leito.
Anexos

## **02. ANEXOS**

* **Pedido de Exame:** Exibe todos os Pedidos de Exame do atendimento do exame selecionado. Você pode acessar este anexo também pelo ícone .

Abaixo segue a permissão para a ação:

 

* **Geração de Exceção:** Gera exceções Impeditivas e Restritivas para os exames. Exceções Impeditivas impedem a liberação do exame e exceções Restritivas liberam exames mediante a confirmação do usuário. Habilitado de acordo com a configuração do perfil do usuário, menu "Perfis > Anexos > Parâmetros RM Saúde > Aba Unidade Diagnóstico > Perfil gera exceções". Pode ser acessada pelo anexo ou pelo ícone . Pelo ícone permite incluir exceção para múltiplos registros ao mesmo tempo.

**Campos:**

Tipo Exceção: Tipo da exceção cadastrado em "Cadastros > Unidade Diagnóstico > Tipos de Exceções".

Tipo Impedimento: Permite informar se a exceção é para a Amostra, Pedido de Exame e Exame.

Tipo de Restrição: Permite informar se o usuário quer que a exceção seja Impeditiva para o processo de liberação ou Restritiva mediante a confirmação do usuário.

Ação Restritiva:

Responsável: Usuário que está fazendo o cadastro da exceção.

Data: Horário de inclusão da exceção.

Processos

## **03. PROCESSOS**

* **Entrega de Material Pendente:** Este processo permite o usuário informar para o RM que o material do exame foi entregue. Para utiliza-lo basta selecionar um exame na visão, acessar o processo Entrega de Material Pendente ou clicar no ícone . Irá abrir a tela com os exames que estão com material pendente, para realizar a entrega do material basta clicar no checkbox do exame, caso desmarque este checkbox será removida a entrega do material. Para imprimir um relatório de todos os exame do pedido basta clicar no botão Imprime Pedido.

* **Link Laudos:**Esse processo é utilizado para criar um link entre os exames selecionados e não é permitido selecionar vários exames. Ao selecionar o processo de Link Laudos, será exibida a tela com os exames disponíveis para realizar o Link entre laudos. Ao selecionar um dos exames e clicar no botão **Relacionar**será questionado  se é você deseja informar uma nova descrição para exame, caso essa opção seja confirmada, será exibida um janela para que seja informada essa nova descrição. É possível remover um link, para isso basta selecionar um Pedido exame com Código de Link e clicar no botão **Remover,**com isso o link será removido. Abaixo temos algumas imagens que exemplifica o processo acima.

* **Reemitir etiquetas:** Esse processo permite reemitir as etiquetas e atualizar o status do pedido do exame para como “Saiu para coleta" se o parâmetro “Utiliza Fluxo com Triagem de Amostras” estiver configurado e o status do pedido for Inicial ou Recoleta.

       

* **Triagem amostras:**Este processo permite triar as amostras dos exames. Ao realizar o processamento da tela, as amostras selecionadas irão receber o agente de coleta selecionado e, caso o Parâmetro Geral > Aba Unidade Diagnóstico II > Aba Laboratoriais > Utiliza Fluxo com Triagem de Amostras estiver marcado, os exames da amostra irão para o status Triado Laboratório(S).

**Campos:**

No. Pedido: Número do pedido a ser pesquisado.

Departamento: Departamento da amostra.(Tabela SZLABDEPARTAMENTO)

Exibir amostras já coletadas: Indica se a pesquisa deverá trazer amostras que já tenham Agente de Coleta.

Agente de Coleta: Este campo indica qual será o agente de coleta das amostras selecionadas para serem processadas.

Grid Amostras: Exibe as amostras retornadas de acordo com o filtro selecionado. Só exibirá as amostras que não foram descastadas.

Grid Histórico da Amostra: Ao selecionar uma amostra na grid acima, este grid é carregada com o histórico da amostra.

**Botões:**

Pesquisa: Realiza a pesquisa.

Seleção através de código de barras:

           Tela de Seleção de amostras. Pode ser por leitura de código de Amostra ou digitação manual.

**Campos**

           Amostra: Número da amostra. Este campo é editável e deve possuir mais de 12 números. A amostra digitada/lida deve estar                     vinculada ao mesmo departamento que o pedido selecionado na tela anterior.

           Pedido: Número do pedido de exame.

           Paciente: Nome do paciente que esta solicitando o exame.

           Data da Amostra: Data da amostra digitada/leitura de código de barras.

           Exames da Amostra: Os exames que a amostra selecionada faz parte.

           Departamento: Nome do departamento responsável pela amostra.

           Unidade: Nome da unidade responsável pela amostra.

           Ao selecionar OK, a lista de amostras que foram lidas, será atualizada na grid da tela de Triagem/Recoleta.

Executar: Executa o processamento das amostras selecionadas.

Ao processar as amostras selecionadas, o campo agente de coleta deve estar selecionado, para que seja vinculado as amostras.

Caso este campo não esteja selecionado uma mensagem deve avisar o usuário. Estes registros de amostras, não devem aparecer na grid de amostras da tela de Triagem, somente na tela de Recoletar amostras.

* **Recoletar amostras:**Este processo permite recoletar as amostras dos exames. Ao realizar o processamento da tela ela pode ter dois comportamento de acordo com o Parâmetro Geral > Aba Unidade Diagnóstico II > Aba Laboratoriais > Utiliza Fluxo com Triagem de Amostras. Caso ele esteja marcado, as amostras selecionadas serão descartadas, os exames das amostras vão para o status Recoleta(N) e é feito o recalculo de amostras dos exames. Caso o Parâmetro Geral estiver desmarcado, as amostras selecionadas irão receber o agente de coleta selecionado. Antes de realizar o processamento, quando o Parâmetro Geral Utiliza Fluxo com Triagem de Amostras estiver marcado, será obrigatório o preenchimento da justificativa da recoleta.

**Campos:**

No. Pedido: Número do pedido a ser pesquisado.

Departamento: Departamento da amostra.(Tabela SZLABDEPARTAMENTO)

Agente de Coleta: Este campo indica qual será o agente de coleta das amostras selecionadas para serem processadas.

Grid Amostras: Exibe as amostras retornadas de acordo com o filtro selecionado.

Grid Histórico da Amostra: Ao selecionar uma amostra na grid acima, este grid é carregada com o histórico da amostra.

**Botões:**

Pesquisa: Realiza a pesquisa.

Seleção através de código de barras:

Executar: Executa o processamento das amostras selecionadas.

Na execução da tela de Recoleta de amostras, é realizado o vinculo com o novo agente selecionado e deve ser inserida uma justificativa para esta troca.

* **Verifica Pendências:**Este processo exibe todos os exames do pedido selecionado.

**Campos:**

Data 1ª Coleta: Exibe a data da primeira coleta do pedido. Caso nenhuma coleta ainda tenha sido realizada, irá exibir "Nenhuma coleta realizada".

Pendência: Para verificar se a pendência está expirada ou não, é utilizado o Parâmetro Geral > Aba Unidade Diagnóstico > Número máximo de DIAS para coletar / entrega de material pendente. Se a diferença de dias entre a primeira coleta e a data atual for igual ao parâmetro geral, então irá exibir EXPIRANDO HOJE, se for maior irá exibir EXPIRADA, se não irá exibir NÃO EXPIRADA.

**Colunas:**

Preenchido: Indica se o exame já passou pelos status Conclusão(C), Retorno(R), Liberação(L), Emissão(E) ou Entrega(F).

Liberado: Indica se o exame já passou pelos status Liberação(L), Emissão(E) ou Entrega(F).

Impresso: Indica se o exame já passou pelos status Emissão(E) ou Entrega(F).

Mat. Pendente: Indica se já foi coletado o material do exame.

preenchimento do laudo

## **04. PREENCHIMENTO DO LAUDO**

Essa funcionalidade permite efetuar o preenchimento do laudo de um exame de imagem. Pode ser acessado clicando duas vezes no exame ou no botão de editar 

         

         **Campos:**

N° Pedido: Exibe o número do pedido do exame selecionado.

         Cód. Atend: Exibe o código de atendimento do exame.

         Leito Atual: Exibe leito atual, se paciente estiver internado.

         Cód. Exame: Exibe o código do exame selecionado.

         Exame: Exibe o exame selecionado.

         Idade: Exibe a idade do paciente.

         Cód Paciente: Exibe o código do paciente.

         Paciente: Exibe o nome do paciente.

         Nome Social: Exibe o nome social se o paciente possuir cadastrado no registro de atendimento.

         Dt. Nasc: Exibe a data de nascimento do paciente.

         Dt. Pedido: Exibe a data do pedido do exame.

         N° Películas: Campo para preenchimento do número de películas utilizadas no exame.

         Auto Texto para Laudo: Permite selecionar um auto texto cadastrado utilizando o mnemônico.

**Botões:**

         Auto Texto para Laudo: Exibe nova janela com uma lista de todos os autotextos cadastrados para laudo de imagem.

         Substituir: Insere o texto de substituição no laudo.

         Modelo: Exibe nova janela com uma lista de todos o modelos de resultados disponíveis para este exame.

         Conclusão: Exibe nova janela para inserir observações.

          Tela exibida quando selecionado botão de Auto texto.

           Tela exibida quando selecionado o botão de Modelo

          Procedimento para efetuar uma inclusão, alteração e exclusão de algum auto texto para laudo de imagem.

## **05. STATUS DOS PEDIDOS DE EXAMES**

## **06. TABELAS UTILIZADAS**

* SZPEDEXAME
* SZPEDEXAMEITEM
* SZLABMATERIALEXAME
* SZAMOSTRAS
* SZATENDIMENTO
* SZPACIENTE
* SZLABDEPARTAMENTO

Use esse box para destacar informações relevantes e/ou de destaque.IMPORTANTE!

]]>
