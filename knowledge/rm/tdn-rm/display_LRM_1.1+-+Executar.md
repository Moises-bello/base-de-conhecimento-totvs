---
content_hash: 6a52a2ce5063890163563a3fb67781352cdf52cdb3ece4cc7121e72805734465
fetched_at: '2026-06-29T00:11:55.611516+00:00'
page_id: '862598235'
product: rm
source: tdn-rm
title: 1.1 - Executar
type: documentation
url: https://tdn.totvs.com/display/LRM/1.1+-+Executar
version: 26
---

## O que é?

O **Menu Executar** é uma funcionalidade essencial para iniciar e gerenciar a execução de atividades no TOTVS Automação de Testes. É aqui que você pode iniciar a execução de fato do seu teste em um servidor.

## Para que serve?

Ele é responsável por iniciar a execução de uma ou mais atividades, além de permitir a visualização e o gerenciamento da lista de atividades em execução em um determinado servidor, garantindo controle sobre os processos em execução.

## Exemplo de Uso

Como cadastrarComo realizar uma execução

A execução de uma atividade envolve a interação entre a atividade, um servidor que realizará a execução, e o ambiente do RM onde os testes serão realizados. Para isso, é necessário configurar previamente um servidor e um ambiente relacionado à versão do RM hospedada no servidor em questão. Saiba mais como realizar a criação desses pré-requisitos em: [Servidores](https://tdn.totvs.com/display/LRM/5.+Servidores) e [Ambientes](https://tdn.totvs.com/display/LRM/4+-+Ambientes).

**Pré-condições:** Antes de executar qualquer atividade, certifique-se de que o Agent do servidor responsável por essa execução está rodando como Administrador.

1. Conferir se o servidor que irá executar a atividade está Online;
2. Selecionar a(s) atividade(s) de interesse;
3. Navegar para o seguinte menu: **TOTVS Automação de Testes → Gestão de Execução → Executar**;
4. Será apresentado no rodapé do navegador a tela de execução;
5. Selecionar o Servidor que irá executar o teste;
6. Selecionar o Ambiente de execução;
7. **Atividades C#:** Caso necessite **debugar** o código dessa atividade, clique em **Depurar**. Com isso, será aberto o Visual Studio com o debugger ativo no código dessa atividade.
8. **Atividade Cypress:** Caso seja necessário **debugar**, clique em **Depurar**. Assim, a atividade será executada no modo visual (*headed*), permitindo acompanhar em tempo real todas as ações realizadas durante a execução do teste.
9. Clicar em Play .

Em caso de sucesso, uma mensagem de confirmação em um box verde indicará que a execução foi iniciada corretamente. Se essa mensagem não aparecer, verifique se o Agent está, de fato, em execução no servidor.

Gerenciamento Macro da Execução

As execuções podem ser gerenciadas de forma macro da seguinte forma:

* + **Start** : Inicia a execução de uma Atividade.
  + **Remoção da Fila**: Remove todas as Atividades da fila de execução.

Além disso, quando uma Atividade está em execução, é possível acompanhar seu progresso em tempo real. Essa visualização permite extrair as seguintes informações:

1. **Atividade em Execução:** Identifica qual atividade está sendo executada no momento. No caso de um projeto de teste, exibe o nó específico do projeto que está em execução.
2. **Progresso da Execução:** A barra de progresso azul indica a porcentagem concluída da atividade como um todo.
3. **Status da Atividade:** Após o nome da atividade, é exibido seu status atual, como "Aguardando" ou "Executando".

Como visualizar a fila de execuções

A fila de execução pode ser visualizada clicando na seguinte opção:

Com isso, serão apresentadas as seguintes opções:

* + Fechar;
  + Exibir acima;
  + Detalhes da Fila.

Fechar

Fecha o componente de execução.

Exibir acima

Move o componente de execução para a parte superior da tela. **Observação:** Quando o componente está na parte superior, você também pode movê-lo de volta para a parte inferior

Detalhes da Fila

Ao clicar nessa opção, o usuário consegue visualizar:

* **Atividade Atual**: Identificar qual atividade está sendo executado no momento.
* **Status da Atividade**: Verificar o status atual da execução, se está aguardando ou em andamento.
  + *Aguardando:* A atividade ainda não foi executada, está aguardando a finalização de outra na fila de execução.
  + *Executando:* A atividade está sendo executado naquele momento no servidor em questão.
* **Progresso da Execução**: Acompanhar o progresso percentual da atividade, facilitando o monitoramento.
* **Usuário Responsável**: Saber quem iniciou a execução da atividade, ajudando na rastreabilidade e comunicação.

As execuções podem ser gerenciadas da seguinte forma:

* + **Cancelamento**: Possibilidade de cancelar uma Atividade que está em andamento.
  + **Remoção da Fila**: Capacidade de remover uma Atividade da fila de execução, se necessário.

*Exemplo de Situação:*

A fila de execução abaixo possui atualmente dois projetos. O primeiro projeto está em andamento, com metade de sua execução já concluída.

Enquanto isso, o segundo projeto está aguardando sua vez na fila, esperando que o primeiro termine completamente para iniciar sua execução.

Ao final da execução de uma Atividade, é possível visualizar o **Log de Execução** da mesma.

Caso o fundo do Log de Execução for vermelho, a execução da sua atividade **NÃO** foi realizada com sucesso.

Caso o fundo do Log de Execução for verde, a execução da sua atividade **FOI** realizada com sucesso.

---

# Saiba mais

Para verificar se o Agent está operacional no seu servidor, consulte a coluna **Online** na tabela de servidores.

É possível executar várias atividades simultaneamente em um servidor.

Um ambiente é necessário para indicar o diretório onde o RM está localizado no servidor em questão.

Sempre verifique se uma atividade está realmente pronta para ser executada.

# FAQ

**P: O que acontece se minha atividade não for executada com sucesso?**  
R: Após a execução, será exibido o log final com o status da execução (Sucesso ou Falha). Clique nele para verificar o log gerado do erro, isso poderá te ajudar a tirar conclusões sobre a causa raiz. Certifique-se de que o ambiente do RM apontado realmente existe na sua máquina.

**P: O que devo fazer se o servidor não estiver acessível?**  
R: Verifique a conexão de rede do servidor e garanta que ele esteja configurado para permitir acesso na rede onde o TOTVS Automação de Testes está operando. Certifique-se também de que não há bloqueios de firewall ou problemas de configuração de rede que possam impedir a comunicação.

**P:  Como verifico se o meu servidor está Ativo?**  
R: Na tabela de servidores, a coluna "Online" indica o status do servidor. Se o ícone estiver ativo, isso significa que o servidor está operacional e disponível para execução de tarefas.
