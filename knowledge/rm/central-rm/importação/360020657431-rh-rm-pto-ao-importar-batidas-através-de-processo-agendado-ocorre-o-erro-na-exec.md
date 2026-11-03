---
article_id: 360020657431
category: Importação
content_hash: 4254701a842e25782272ca7952e13f0b1ae1d12c316ca7e68cae1950fbfc1b49
fetched_at: '2026-06-28T22:46:33.731007+00:00'
product: rm
section_id: 6045469428631
source: central-rm
title: RH - RM - PTO - Ao importar batidas através de processo agendado ocorre o "Erro
  na execução do processo de batida:"
type: support-article
updated_at: '2025-10-20T14:29:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020657431-RH-RM-PTO-Ao-importar-batidas-atrav%C3%A9s-de-processo-agendado-ocorre-o-Erro-na-execu%C3%A7%C3%A3o-do-processo-de-batida
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16503145099671) Tempo aproximado para leitura: 00:01:10 min****Ocorrência**Ao agendar o processo (jobs) de importação de batidas, para que ocorra de maneira automática aparece a seguinte mensagem: "Erro na execução do processo de batida:"  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21925423969559)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1.22  
  
**Causa**   
Esse incidente pode ocorrer se a pasta em que o arquivo de importação está localizado não for compartilhada em rede ou se o usuário de rede ao qual o processo está sendo "chamado" não tiver permissão para acessar a pasta.  
  
**Solução**Aqui está o vídeo com os passos para corrigir o incidente: **Parte 1 - Simulação do erro:**

**Parte 2 - Conferência e das permissões de acesso a pasta:**

Aqui está o passo a passo dos cadastros que precisam ser avaliados:

* Para garantir que tudo esteja correto, verifique se o caminho inserido no campo de importação corresponde à sintaxe correta:   
  **\\IP do servidor\nome da pasta\nome do arquivo de importação.txt  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21925423980183)**
* Certifique-se de que a pasta onde o arquivo de importação está localizado esteja em rede e compartilhada com o usuário de rede NetworkService, com os usuários que executam o processo e com o servidor onde o processo será executado. É importante aplicar as permissões de leitura e gravação ao usuário e ao servidor. Para conferir, clique com o botão direito do mouse sobre o nome da pasta e selecione a opção "Propriedades".  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21925423990679)
* Na aba "Segurança", verifique se o usuário de rede NetworkService, os usuários que executarão o processo e o servidor onde o processo será executado estão adicionados na seção "Nome de grupo ou de usuários".      
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21925419180567)
* Se não estiverem adicionados, clique em "Editar":     
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21925999612439)
* Na janela de segurança, clique em "Adicionar":  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21925999638167)
* Na janela de seleção de usuários, computadores, contas de serviço ou grupos, clique em "Tipos de objeto" e marque as opções "entidade de segurança interna", "computadores", "grupos" e "usuários", e clique em "OK".  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21925424058263)![](https://centraldeatendimento.totvs.com/hc/article_attachments/21925424074007)
* Ao retornar à janela anterior, no campo "Digite o nome do objeto a ser selecionado", insira os usuários e o servidor onde o processo será executado e clique em "Verificar nomes". Após a verificação, clique em "OK".  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21925424087447)
* Após adicionar, verifique na guia "Segurança" se as permissões de leitura e gravação estão ativas e clique em "OK".  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21925999661079)

Após revisar os cadastros e permissões, caso tenha feito algum ajuste, exclua os processos agendados anteriormente e programe um novo agendamento.

**Importante**

* O arquivo .txt que contém as marcações, utilizado para a importação deverá estar disponibilizado no próprio servidor que executa o processo de importação.
* Ao selecionar o arquivo de importação, na tela de importação, o caminho do arquivo **não** deverá ser utilizado mapeamento.
* Antivírus e Firewall podem impactar no bloqueio do processo, portanto atente-se nas liberações de ambos para permitir a execução do processo corretamente.
* O tamanho do caminho do arquivo **não deve** ultrapassar 150 caracteres.

**Saiba mais**

[RH - RM - PTO - Como agendar o processo para importar as batidas de forma automática](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014195451)

[RH - RM - PTO - Como importar as batidas para o Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000486068)
