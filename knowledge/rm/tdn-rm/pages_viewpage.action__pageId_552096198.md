---
content_hash: 413867682d2ef8916af6d028d91b7f257ea3af4d7dc2be51bd8a79246ec40ad7
fetched_at: '2026-06-29T00:10:44.041026+00:00'
page_id: '552096198'
product: rm
source: tdn-rm
title: Migração Software Terceiros para RM Middleware
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=552096198
version: 10
---

# Objetivo

Prover informações para clientes que estejam iniciando a utilização da Folha de Pagamento RM, e que já tenham enviado informações para o ambiente do eSocial utilizando softwares de folha de pagamento de terceiros, possam continuar a enviar os dados para o eSocial através da fila de eventos do RM Middleware.

# Etapas da migração:

# Etapa 1 - Ativação do Middleware

A primeira etapa para a migração do eSocial consiste em ativar o middleware. As informações sobre como realizar essa importação podem ser obtidas no link abaixo:

# Etapa 2 - Parametrização do eSocial no RM

A segunda etapa consiste em acessar o parametrizador do RM (Configurações | Parametrizador | eSocial) e configurar os dados do eSocial.

Nesta etapa deve ser prestada atenção especial aos seguintes parâmetros:

* **Máscara para Matrícula do Trabalhador:**  

  Deve ser criada uma máscara que garanta que o código de matrícula sequencial gerado automaticamente pelo RM nunca seja igual a um código gerado no sistema anterior.

  Para garantir essa unicidade da matrícula pode ser utilizado o recurso de prefixo na máscara, que pode ser parametrizado em “Parametrizador | eSocial | Configurações Gerais 2/6”.  
    
  **Observação:**

  Durante o processo de migração de dados do cadastro de funcionários do software de terceiros para o RM deve-se atentar para que as matrículas dos funcionários que foram enviados para o eSocial no sistema anterior sejam mantidas, isso é fundamental para o governo continuar recepcionando os eventos de funcionários enviados pelo RM aos funcionários já enviados pelo software anterior.
* **Prefixo para Eventos de Tabelas:**

  Para que não exista conflito entre os códigos dos registros do RM e códigos dos registros gerados pelo sistema anterior deve ser utilizado o recurso de Prefixo para Eventos de Tabelas, que pode ser parametrizado em “Parametrizador | eSocial | Configurações Gerais 2/6”.

* **De/Para de período:**

  Para a entrada em produção nos casos de trabalho com o mês caixa, será necessário utilizar o processo de De/Para de período localizado em "Parametrizador | eSocial | De/Para | De/Para de Período" para realizar a alteração do período da folha de pagamento para o período utilizado no sistema terceiro.

# As etapas 3 e 4 são para os casos em que os códigos de tabelas não permaneceram os mesmos utilizados pelo sistema de terceiros:

# Etapa 3 - Carga das tabelas do RM

A terceira etapa consiste em realizar a carga das tabelas do RM para o governo. Para isso podem ser utilizados os módulos abaixo:

* Validador da Base de Dados: Para validar se os dados migrados para o RM estão atendendo as regras de validação do leiaute do eSocial.
* Gerar Gatilhos Eventos Iniciais de Tabela: A execução desse módulo insere um gatilho na fila de eventos para cada registro das tabelas selecionadas na parametrização do processo.
* Gerar XML: Nesse módulo são gerados os xml’s para cada um dos gatilhos inseridos na execução do item anterior.
* Integrar com o Governo.

# Etapa 4 - Geração de evento S-2206 Alteração de Contrato de Trabalho

A empresa pode optar por enviar eventos "S-2206 Alteração de Contrato de Trabalho" para os trabalhadores, a geração desse evento garantirá que o cadastro dos trabalhadores existente no ambiente do governo estará atualizado considerando os novos códigos das tabelas geradas no item anterior, além de garantir que os demais campos do cadastro estarão com as informações compatíveis com o cadastro dos funcionários no RM.

Para a execução dessa tarefa pode ser utilizado o menu Gerar Gatilhos em Lote, selecionando os funcionários não demitidos e marcando para gerar o evento S-2206.

# Considerações finais

1) Retificações de eventos que foram enviados pelo sistema de terceiro poderá seguir umas das opções abaixo:

1. Retificar pelo próprio sistema de terceiro;
2. Alimentar a fila de eventos do RM somente com os eventos a serem retificados, não é necessário trazer para o RM todos os dados da fila de eventos do sistema de terceiros;
3. Editar o XML de retificação e informar o número de recibo.

**Observação:**

Caso deseje alimentar a fila de eventos do RM poderá utilizar a importação via TBC.  Veja mais informações em  ou utilizar o novo processo **.**

2) É imprescindível que na migração dos funcionários mantenha a mesma matricula eSocial do produto de terceiros.
