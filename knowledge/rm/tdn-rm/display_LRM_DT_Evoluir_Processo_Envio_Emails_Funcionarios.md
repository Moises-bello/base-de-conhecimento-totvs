---
content_hash: c46db4c49df16cd5bc6bd0c73960d991ad2ad256e8faa07a540386e450985246
fetched_at: '2026-06-29T00:06:09.288603+00:00'
page_id: '203752251'
product: rm
source: tdn-rm
title: DT_Evoluir_Processo_Envio_Emails_Funcionarios
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Evoluir_Processo_Envio_Emails_Funcionarios
version: 13
---

# ENVIO DE E-MAIL PARA GESTORES/SUPERVISORES

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Automação de Ponto TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotinas** | **Nome Técnico** | | *› Processos › Caminho* | *Envio de e-mail para o funcionário* | |
| **Versões/Release:** | *12.1.6* |

## Descrição

A evolução deste processo permite o envio automático de relatórios, como por exemplo, ''Dados da minha equipe'' para os gestores/supervisores através do Totvs Automação de Ponto.

## Procedimento para Utilização

O processo “Enviar e-mails para Funcionários” está no módulo Folha de Pagamento, dentro do Menu “Configurações”.  
  
  
  
O processo “Enviar e-mails para Funcionários” está no módulo Automação de Ponto, dentro do Menu “Processos / Utilitários”.

    
  
 Os relatórios são filtrados pela aplicação do contexto selecionado;  
 O processo considera os funcionários selecionados na visão. Ele está evoluído para que seja possível executá-lo também por fora. Para isso são disponibilizados novas opções de filtros para seleção dos destinatários, através dos seguintes controles:  
   
 • Filtrar por opções de envio:

 • Filtrar por grupo de funcionários:  
  
   
  
 Caso o relatório selecionado seja do tipo “DADOS DA MINHA EQUIPE”,  são filtrados somente os chefes/supervisores, que receberão o relatório da sua respectiva equipe em anexo por e-mail;  
 É disponibilizado o perfil de parâmetros para salvar as configurações do envio de e-mail.

    
  
 O agendamento e a recorrência deverão ser configurados pelo agendador de Jobs dos processos.  
 

» O envio de emails deve respeitar o filtro de funcionários. Caso a configuração de filtro não retorne nenhum destinatário, não será possível avançar para a próxima etapa;  
» Caso o tipo de relatório seja “DADOS DA MINHA EQUIPE”, deverá enviar somente para os chefes/supervisores. Caso o filtro de seleção filtre somente funcionários subordinados, não será possível avançar para a próxima etapa, solicitando a verificação do filtro;  
» Os gestores devem receber somente os relatórios com as informações da sua equipe. Não pode acontecer de receberem relatórios de outros gestores;  
» O perfil deve salvar a configuração de todos os controles do processo, exceto os anexos do e-mail por mensagem livre;  
»  Para o envio de mensagens livres, o processo irá criar lotes de até 30 destinatários, incluindo os que estiverem em cópia. Isso foi necessário pois os servidores SMTP possuem limites de destinatários pré-definidos. Caso o limite seja menor que 30 destinatários, o usuário deverá configurar o filtro para considerar a quantidade máxima do servidor.

 O processo para enviar emails está em **Automação de Ponto / Processos / Utilitários**ou no módulo Folha de Pagamento dentro do Menu **Configurações / Comunicação**.
