---
content_hash: f589adf7b48b315594a7bb45866a3da6740fa90cfab6096ea3afa72e8cd2dd50
fetched_at: '2026-06-29T00:10:35.538785+00:00'
page_id: '531013034'
product: rm
source: tdn-rm
title: Agenda de Cirurgia
type: documentation
url: https://tdn.totvs.com/display/LRM/Agenda+de+Cirurgia
version: 27
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Registro de informação de cirurgias**
4. **Procedimentos**
5. **Status**
6. **Observação**
7. **OPME**
8. **Passo a passo das telas utilizadas**
9. **Controle de permissão de troca de atendimento**
10. **Anexo de documentos**

itensVisão Geral

## **01. VISÃO GERAL**

Nesta tela você poderá incluir e visualizar as cirurgias marcadas e canceladas.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Dentro do Menu Processos o sistema surge com as seguintes funcionalidades:  
Fechar Agenda de Cirurgia, Abrir Agenda Cirurgia , Reagendar Cirurgia, Cancelar Agenda de Cirurgia, e o Log da Agenda de Cirurgias.  
A inserção de paciente na Agenda pode ser através de:  
**Um paciente externo** - paciente nunca foi atendido.  
**Paciente interno** - já existe na base algum atendimento, a pesquisa trará os campos preenchidos dentro da tela da Agenda, as seguintes funcionalidades:  
Identificação, Procedimentos e Recursos ficam em edição.  
As informações preenchidas na Agenda vão ser utilizadas no Registro de Informações de Cirurgias ao associar Atendimento Dentro da tela de Registro.

O preenchimento de data inicio e fim do agendamento são preenchidas automaticamente com a data e hora atual.

Registro de informação de cirurgias 

## **03. REGISTRO DE INFORMAÇÕES DE CIRURGIA**

Está função será utilizada para o registro de informações sobre cirurgias, dentro do sistema.

Procedimentos 

## **04. PROCEDIMENTOS**

Na aba procedimentos, são exibidas as Equipes Médicas e Procedimentos realizados na cirurgia.

Caso o procedimento tenha alguma Órtese/Prótese vinculada, ao adicionar o procedimento na agenda, automaticamente na será adicionado todos os OPME relacionados. 

Ao adicionar um procedimento, o sistema verifica se o período de tempo do agendamento comporta o tempo estimado de duração do(s) procedimento(s) e em caso da duração deste(s) exceder o tempo do agendamento, a aplicação questionará o usuário pra que o processo ajuste o tempo do agendamento.

Status

## **05. STATUS**

Ao realizar o vínculo da agenda com um atendimento com parcial **Em elaboração** ou **Em aberto**, o status será  **Agendado.** A alteração dos status poderá ser realizada através do campo Status da agenda. 

As agendas com o status "**Cancelada**" não podem ser alteradas.

Observação

## **06. OBSERVAÇÃO**

Os recursos tem de estar previamente cadastrados em Recursos para Cirurgias, localizado em Cadastro | Cuidados com o Paciente | Cirurgias | Recursos para Cirurgias Anestesia  
Na aba Anestesia, você irá registrar as Anestesias da cirurgia  
Exemplo:  
Alguns tipos de ASA :  
ASA I - Paciente com boa saúde.  
ASA II – Paciente com doença sistêmica leve  
ASA III – Paciente com doença sistêmica grave  
ASA IV – Paciente com doença sistêmica grave com risco constante de morte  
ASA V – Paciente moribundo que não se presume que sobreviva caso não se submeta a cirurgia  
ASA VI – Paciente com morte cerebral confirmada cujos órgãos serão retirados para doação.  
Agentes Anestésicos  
Na aba Agentes Anestésicos, você irá registrar os Agentes da cirurgia, a quantidade e a Unidade de cada um (Miligrama, Grama ou Mililitro)  
Folhas de Sala  
Na aba Folha de Sala, será permitido associar uma ou mais Folhas de Sala do paciente a uma cirurgia.  
Observação:  
Esta funcionalidade servirá apenas como informação gerencial (podendo ser lida em relatórios feitos no Gerador de Relatórios)

OPME

## **07. OPME**

Ao cadastrar o procedimento, caso o mesmo possui OPME vinculado ele será automaticamente cadastrado e exibido na aba de OPME.

Na aba serão listados todos os OPME que foram vinculados a cirurgia, no grid exibiremos o nome do OPME, quantidade e qual o procedimento que está vinculado ao OPME, só será exibido procedimento e cirurgião para os OPME vinculados ao procedimento.

Na tela de adicionar OPME o usuário poderá selecionar qual OPME deseja vincular a cirurgia e qual a quantidade que será utilizada.

Para vincular OPME a um determinado procedimento acessar: Menu > Cadastro > Cuidados com o Paciente > Cirurgias > Procedimento para agenda de cirurgias

Passo a passo das telas utilizadas 

## **08. PASSO A PASSO DAS TELAS UTILIZADAS**

Acesse:

* A tela de Cadastro

* Cuidados com Paciente

* Cirurgias

Nesta etapa fazemos todo o cadastro de Cirurgias.

* Na tela de Processo identificamos o paciente e incluímos o procedimento, recursos, anestesia, órtese/prótese e campos complementar
* Na aba de processos temos a opção de fechar a agenda cirúrgica abrir, Reagendar, cancela, o log e a justificativa de Atraso.

## **Bloqueio de salas do bloco Cirúrgico**

Nesta função cadastramos todos os Bloqueios de Salas de Bloco Cirúrgicos no Hospital.

Estes bloqueios refletirão na Agenda de Cirurgias. Caso o usuário tente agendar um compromisso em uma sala que esteja bloqueada, o Sistema impede o agendamento, alertando o usuário que a mesma encontra-se em estado de bloqueio.

Está função será utilizada para o registro de informações sobre cirurgias, dentro do sistema.

Controle de permissão de troca de atendimento

## **09. CONTROLE DE PERMISSÃO DE TROCA DE ATENDIMENTO**

O RM possui um controle de acesso de troca de conta para que as agendas com itens de cirurgias já lançados não gerem inconsistências no processo de faturamento.

As agendas já finalizadas não é possível alterar a conta, porém agendas em andamento com itens já confirmados é possível alterar apenas a conta. 

Anexo de documentos

## **10. ANEXO DE DOCUMENTOS**

Acessando a Agenda de Cirurgias:

* + Navegue até a seção de Agenda de Cirurgias no sistema.
  + Selecione a cirurgia desejada na lista.

Abrindo o Controle de Documentos:

* + Clique na seta ao lado direito da opção **"**Anexos**"**.
  + Selecione "Controle de Documentos". Uma nova aba será aberta com o título "Controle de Documentos", conforme ilustrado na imagem abaixo:

Visualizando, Editando e Deletando Documentos:

* + Na aba"Controle de Documentos", você poderá:
    - Visualizar todos os documentos anexados à cirurgia selecionada.
    - Editar informações dos documentos, se necessário.
    - Deletar documentos que não são mais relevantes.

Adicionando Novos Documentos:

* + Para anexar novos documentos à cirurgia, clique no botão **"+"**.
  + Preencha os campos obrigatórios no formulário que será exibido.
  + Clique em "Anexos" e, em seguida, em "Arquivos".
  + Complete os campos necessários e, em seguida, clique no ícone de imagem para selecionar o arquivo desejado do seu dispositivo.

Observação: Para adicionar documentos à cirurgia, é necessário que o tipo de documento seja classificado como 'Cirurgia'.

No “Tipo de Documento” igual a “Cirurgia” será desabilitados todos os Processos e também o anexo “Pendências da Conta” do controle de documentos. Ao editar a tela, os seguintes campos ficarão desabilitados: Outros, Convenio, Fatura. Não permitido selecionar outro atendimento ou parcial.

Finalizando o Processo:

* + Após selecionar o arquivo, certifique-se de revisar todas as informações preenchidas.
  + Clique em**"Salvar"** para concluir o processo de anexação do documento.

Manter a documentação organizada e acessível é fundamental para a eficiência e segurança dos procedimentos cirúrgicos. Utilize o Controle de Documentos para garantir que todas as informações relevantes estejam sempre à mão.
