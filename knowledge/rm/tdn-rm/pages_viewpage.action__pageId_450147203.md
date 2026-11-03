---
content_hash: d714a8ad76dfa856ebd4399f89e1494ac906425b309790f89ce0675dac01ac80
fetched_at: '2026-06-29T00:09:55.738506+00:00'
page_id: '450147203'
product: rm
source: tdn-rm
title: Migração Software Terceiros para RM e TAF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450147203
version: 8
---

# Objetivo

Prover informações para clientes que estejam iniciando a utilização da Folha de Pagamento RM, e que já tenham enviado informações para o ambiente do eSocial utilizando softwares de folha de pagamento de terceiros, possam continuar a enviar os dados para o eSocial através da fila de eventos do RM.

# Etapas da migração:

# Etapa 1 - Importação dos xml's no TAF

A primeira etapa para a migração do eSocial consiste em importar no TAF os xml's enviados para o governo através do software de terceiros.

Devem ser importados todos os xml's já enviados para o eSocial:

* Informações do Empregador
* Tabelas
* Não Periódicos
* Periódicos

as informações sobre como realizar essa importação podem ser obtidas no link abaixo:

# Etapa 2 - Parametrização do eSocial no RM

A segunda etapa consiste em acessar o parametrizador do RM (Configurações | Parametrizador | eSocial) e configurar os dados do eSocial.

Nesta etapa deve ser prestada atenção especial aos seguintes parâmetros:

* **Máscara para Matrícula do Trabalhador:**  

  Deve ser criada uma máscara que garanta que o código de matrícula sequencial gerado automaticamente pelo RM nunca seja igual a um código gerado no sistema anterior.

  Para garantir essa unicidade da matrícula pode ser utilizado o recurso de prefixo na máscara, que pode ser parametrizado em “Parametrizador | eSocial | Configurações Gerais 2/6”.  
    
  Obs: Durante o processo de migração de dados do cadastro de funcionários do software de terceiros para o RM deve-se atentar para que as matrículas dos funcionários que foram enviados para o eSocial no sistema anterior sejam mantidas, isso é fundamental para o governo continuar recepcionando os eventos de funcionários enviados pelo RM aos funcionários já enviados pelo software anterior.
* **Prefixo para Eventos de Tabelas:**

  Para que não exista conflito entre os códigos dos registros do RM e códigos dos registros gerados pelo sistema anterior deve ser utilizado o recurso de Prefixo para Eventos de Tabelas, que pode ser parametrizado em “Parametrizador | eSocial | Configurações Gerais 2/6”.

# Etapa 3 - Carga das tabelas do RM

A terceira etapa consiste em realizar a carga das tabelas do RM para o TAF e posteriormente para o governo, para isso podem ser utilizados os módulos abaixo:

* Validador da Base de Dados: Para validar se os dados migrados para o RM estão atendendo as regras de validação do leiaute do eSocial.
* Gerar Gatilhos Eventos Iniciais: A execução desse módulo insere um gatilho na fila de eventos para cada registro das tabelas selecionadas na parametrização do processo.
* Gerar XML: Nesse módulo são gerados os xml’s para cada um dos gatilhos inseridos na execução do item anterior.
* Integrar com o TAF: Nessse módulo os eventos gerados no item anterior são transmitidos para o TAF.

# Etapa 4 - Geração de evento S-2206 Alteração de Contrato de Trabalho

A empresa pode optar por enviar eventos "S-2206 Alteração de Contrato de Trabalho" para os trabalhadores, a geração desse evento garantirá que o cadastro dos trabalhadores existente no ambiente do governo estará atualizado considerando os novos códigos das tabelas geradas no item anterior, além de garantir que os demais campos do cadastro estarão com as informações compatíveis com o cadastro dos funcionários no RM.

Para a execução dessa tarefa pode ser utilizado o menu Gerar Gatilhos em Lote, selecionando os funcionários não demitidos e marcando para gerar o evento S-2206.

# Considerações finais

Após a execução das etapas anteriores, o TAF terá em seus cadastros as informações dos eventos de tabela enviados para o governo pelo sistema anterior e também dos eventos de tabela integrados pelo RM.  
De forma semelhante, o TAF terá o histórico dos eventos periódicos e não periódicos enviados para o governo pelo sistema anterior e continuará recepcionando os novos eventos periódicos e não periódicos integrados à partir do RM.

Retificações de eventos enviados pelo sistema anterior podem ser realizadas pelo TAF, desde que a importação dos xmls enviado para o governo e retornado pelo governo tenham sido realizadas com sucesso.
