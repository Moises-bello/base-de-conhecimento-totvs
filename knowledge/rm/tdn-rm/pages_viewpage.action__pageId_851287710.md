---
content_hash: fad2c2ea771a480fef99c252efe5e0732cf6d8cf6da2bc2658236b3e8f5688be
fetched_at: '2026-06-29T00:11:53.742762+00:00'
page_id: '851287710'
product: rm
source: tdn-rm
title: Servidores.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=851287710
version: 22
---

# O que são?

Os servidores são as plataformas onde os testes automatizados são executados. Isto permite centralizar o processamento e garantir que os recursos necessários para execução de uma determinada atividade estejam disponíveis no ambiente.

# Para que servem?

Além de executar os projetos, os servidores auxiliam na realização do monitoramento e gerenciamento da fila de execução de atividades. Com ele, também possível cancelar execuções em andamento ou remover atividades na fila.

# Como configurar um Servidor para uso com o TOTVS Automação de Testes

Para que uma máquina opere como Servidor no TOTVS Automação de Testes, é necessário que ela atenda aos seguintes requisitos:

* **Instalação do Agent:** O Agent deve estar sendo executado nessa máquina, para que os projetos possam rodar na mesma. Confira [aqui](https://tdn.totvs.com/display/LRM/13+-+Download+-+Agent), para mais informações sobre o Agent.
* **Ambiente RM (se aplicável):** Para testes que envolvam o ambiente RM, este deve estar corretamente instalado e funcionando na versão necessária no servidor.

# Exemplo de Uso

Criação de um grupoComo Cadastrar

1. Navegue no menu do TOTVS Automação de Testes e clique em **Servidores.**
2. Na tabela que será mostrada, clique no botão verde em destaque.

Preencha o cabeçalho do servidor:

1. 1. **Nome:** Informe o nome do servidor, pode ser tanto o endereço de IP, quanto o Hostname do mesmo.
   2. **Descrição:** Defina uma descrição para o servidor. Por exemplo: De quem pertence esse servidor ou para qual o uso do mesmo.

*Usando o endereço de IP do Servidor:*

*Usando o Hostname do Servidor:*

4. Defina o Grupo o qual o Servidor pertence. Saiba mais sobre o que são os [Grupos](https://tdn.totvs.com/display/LRM/6+-+Grupos) no TOTVS Automação de Testes.

5. Para finalizar a criação, clique em Salvar. Após isso, o servidor será criado e listado na tabela de servidores.

Ícones da TabelaColuna Online

A coluna **Online** na tabela de Servidores serve para indicar o status de conexão do servidor. Ela mostra se o TOTVS Automação de Testes conseguiu se conectar corretamente ao servidor específico. Para que essa conexão seja bem-sucedida, o **Agent** deve estar em execução na máquina.

Essa funcionalidade permite um monitoramento contínuo e eficaz do estado dos servidores, garantindo que qualquer problema de conectividade seja identificado e resolvido rapidamente.

Ao clicar no ícone em destaque da coluna **Online**, você pode ver dois possíveis status:

1. **Status Online**:

   * **Descrição**: O servidor está ativo e pronto para executar automações.
   * **Requisito**: O **Agent** está funcionando corretamente na máquina e a máquina está devidamente conectada na rede.
   * **Ação**: Projetos e atividades podem ser executados sem restrições neste servidor.
2. **Status Offline**:

   * **Descrição**: O servidor não está disponível para execução de automações.
   * **Possíveis Causas**:
     + O **Agent** não está em execução ou foi interrompido.
     + Falta de liberações de rede impedem o TOTVS Automação de Testes de se conectar ao servidor.
   * **Ação**: Verifique se o **Agent** está rodando e se a máquina está com as liberações de rede devidamente feitas.

Coluna Ações

## Edição

O botão de editar permite que os usuários autorizados modifiquem as configurações de um servidor específico.

## Deletar

O botão de deletar permite que os usuários autorizados removam permanentemente um servidor específico do sistema. Uma vez deletado, não será mais possível executar automações, projetos ou atividades nesse servidor, pois ele não estará mais disponível na lista de servidores operacionais.

## Status de Execução

O ícone de status de execução permite visualizar e gerenciar a lista de execução de atividades em um determinado servidor, garantindo flexibilidade e controle sobre os processos em execução.

Com isso, o usuário consegue visualizar:

* **Atividade Atual**: Identificar qual atividade ou projeto está sendo executado no momento.
* **Status da Atividade**: Verificar o status atual da execução, se está aguardando ou em andamento.
  + *Aguardando:* O projeto ainda não foi executado, está aguardando a finalização de outro na fila de execução.
  + *Executando:* O projeto está sendo executado naquele momento no servidor em questão.
* **Progresso da Execução**: Acompanhar o progresso percentual da atividade, facilitando o monitoramento.
* **Usuário Responsável**: Saber quem iniciou a execução da atividade, ajudando na rastreabilidade e comunicação.

As execuções podem ser gerenciadas da seguinte forma:

* + **Cancelamento** : Possibilidade de cancelar Projetos/Atividades que estão em andamento.
  + **Remoção da Fila** : Capacidade de remover Projetos/Atividades da fila de execução se necessário.

*Exemplo de Situação:*

O servidor abaixo possui atualmente dois projetos na fila de execução. O primeiro projeto está em andamento, com metade de sua execução já concluída.

Enquanto isso, o segundo projeto está aguardando sua vez na fila, esperando que o primeiro termine completamente para iniciar sua execução.

Ao final da Execução de uma atividade, é possível visualizar o Log de Execução do mesmo

Exemplo Prático

Imagine que a equipe do Educacional, realizou uma série de implementações e melhorias em várias versões do RM. Essas mudanças impactam diversas funcionalidades do produto e, para garantir a qualidade e a estabilidade do software antes do lançamento, a equipe de QA precisa realizar testes automatizados abrangentes em diferentes ambientes de RM.

### Objetivo

O objetivo é garantir que todas as novas versões do RM sejam rigorosamente testadas em seus respectivos ambientes para assegurar que funcionem corretamente e atendam às expectativas dos usuários.

### Como fazer isso?

1. **Configuração dos Servidores**:

   * **Identificação de Ambientes**:

     + A equipe de QA identifica e define diferentes servidores para cada versão específica do RM.
     + Por exemplo, um servidor é configurado para a versão RM 12.1.2402, outro para RM 12.1.2406, e assim por diante.
   * **Preparação dos Servidores**:

     + **Criação e Configuração**:
       - Adicione e configure cada servidor no TOTVS Automação de Testes através da tabela de **Servidores**.
       - Garanta que o **Agent** esteja instalado e rodando com privilégios de administrador em cada servidor.
       - Assegure que o ambiente do RM na versão necessária esteja corretamente instalado e operacional em cada servidor.
     + **Validação da Configuração**:
       - Verifique se cada servidor está configurado corretamente com a versão específica do RM.
       - Certifique-se de que os servidores são capazes de comunicar-se com o TOTVS Automação de Testes, permitindo a execução dos testes.
2. **Verificação da Disponibilidade dos Servidores**:

   * **Monitoramento do Status**:
     + Na interface do TOTVS Automação de Testes, utilize a coluna **Online** para verificar a disponibilidade de cada servidor.
     + O status **Online** indica que o servidor está pronto para executar os testes.
     + Se um servidor estiver **Offline**, verifique se o **Agent** está em execução e se a conectividade de rede está adequada.
3. **Execução dos Testes Automatizados**:

   * **Início da Execução**:

     + Com todos os servidores verificados e online, inicie a execução dos testes automatizados.
     + Cada servidor executará os testes específicos para a versão do RM para a qual está configurado.
     + Por exemplo, no servidor configurado para RM 12.1.2402, execute todos os testes referentes a essa versão específica.
   * **Paralelização e Gerenciamento de Fila**:

     + Inicie os testes simultaneamente em cada servidor para diferentes versões do RM.
     + O TOTVS Automação de Testes gerencia a fila de execução e a ordem dos testes, assegurando que cada ambiente seja testado de maneira ordenada e eficiente.
     + Utilize a interface para monitorar o progresso e gerenciar a execução, incluindo a possibilidade de cancelar ou reordenar os testes conforme necessário.
4. **Análise e Relatório de Resultados**:

   * **Monitoramento em Tempo Real**:

     + Acompanhe a execução dos testes em tempo real, verificando o progresso e status diretamente na interface do TOTVS Automação de Testes.
     + Identifique rapidamente quaisquer falhas ou problemas nos testes para uma ação imediata.

---

# Saiba mais

Antes de rodar qualquer automação em um servidor, confira se o mesmo está Online.

O ambiente do RM, se for o objetivo do teste, deve estar instalado e operante no seu servidor na versão que necessita executar seus projetos.

O servidor deve estar acessível na rede em que o TOTVS Automação de Testes esteja executando.

Para que o servidor consiga executar os projetos, o Agent deve estar executando em modo **Administrador**.

# FAQ

**P: O que é o Agent do TOTVS Automação de Testes e por que ele é necessário?**  
R: O Agent é uma porta de comunicação entre o TOTVS Automação de Testes e a máquina de automação. Ele precisa estar instalado e executando com privilégios de administrador para garantir que o servidor possa executar os Projetos/Atividades corretamente e responder às requisições do sistema.

**P: Posso cancelar uma Atividade em execução em andamento?**  
R: Sim. Isso pode ser feito acessando a fila de execução e selecionando a opção de cancelamento.

**P:  Como verifico se o meu servidor está Ativo?**  
R: Na tabela de servidores, a coluna "Online" indica o status do servidor. Se o ícone estiver ativo, isso significa que o servidor está operacional e disponível para execução de tarefas.

**P: O que devo fazer se o servidor não estiver acessível?**  
R: Verifique a conexão de rede do servidor e garanta que ele esteja configurado para permitir acesso na rede onde o TOTVS Automação de Testes está operando. Certifique-se também de que não há bloqueios de firewall ou problemas de configuração de rede que possam impedir a comunicação.

**P: Posso remover uma Atividade da fila de execução?**  
R: Sim. Isso pode ser feito acessando a fila de execução e selecionando a opção de remoção.
