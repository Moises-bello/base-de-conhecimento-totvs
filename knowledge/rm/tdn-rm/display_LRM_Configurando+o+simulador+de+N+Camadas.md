---
content_hash: d0778d78f64fa05fb3cef0753e27bfe0996dc2ccef8237840ccb2ee9b94d92ea
fetched_at: '2026-06-29T00:11:11.006453+00:00'
page_id: '644724461'
product: rm
source: tdn-rm
title: Configurando o simulador de N Camadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Configurando+o+simulador+de+N+Camadas
version: 7
---

## Para habilitar instruções que possibilita o simulador de N camadas, será necessário, executar as orientações abaixo, veja:

false

Inicie alterando os  arquivos "Configs" na instalação padrão do TOTVS, no caminho:

*C:\TOTVS\CorporeRM\RM.Net*

Dentro dos configs, informe se o ambiente será ou não em 3 camadas.

* RM.exe.config
* RM.Host.exe.config
* RM.Host.Service.exe.config

**<add key="JobServer3Camadas" value="true" />**

Além de alterar para 3 camadas, é necessário incluir em todos os configs acima qual o servidor de host que será responsável pela execução dos jobs.

*Lembre* de alterar “NOMEDAMÁQUINA” para o nome da **sua** máquina, ou seja, o nome da máquina que é seu servidor host.

**<add key="Host" value="NOMEDAMÁQUINA" />**

Após as alterações acima, é necessário apagar o arquivo \_Broker e iniciar o serviço para entrar no RM.exe.

Em seguida, acesse a opção de programação de agendamento desejada e execute, então, na última tela será apresentado uma visão do ambiente de três camadas, onde poderá escolher se o processo será executado na hora selecionando a opção "Agora" ou se será agendado para outro momento clicando em "Executar em" e definindo o período desejado, conforme imagem abaixo:

  

No menu *Ambientes/Gerenciamento* de Jobs, será onde consultará o status de execução.

E após o período agendado, será possível certificar se aconteceu a execução do job, veja:

 *Lembrando* que este processo além de ganho de performance permite-se trabalhar normalmente, sem precisar aguardar o restante da execução.
