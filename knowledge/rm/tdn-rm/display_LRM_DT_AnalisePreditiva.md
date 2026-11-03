---
content_hash: 81233139338adb56fa9367b2899ec1793385a7bf095f1c49288cf21615f5c9d7
fetched_at: '2026-06-29T00:08:23.433756+00:00'
page_id: '270087127'
product: rm
source: tdn-rm
title: DT_AnalisePreditiva
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_AnalisePreditiva
version: 116
---

# ANÁLISE PREDITIVA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Framework* |
| **Módulo:** | *Análise Preditiva* |
| **Requisito:** | *Informe o requisito relacionado (Issue).* |
| **País(es):** | *BRA* |

## Descrição

Análise Preditiva avalia regras predeterminadas para sugerir funcionalidades e ajuda para o usuário do sistema, bem como ofertas de consultoria que venham a ser publicadas pela equipe TOTVS.

A mensagem é exibida quando o usuário acessa a funcionalidade associada.

A exibição das mensagens pode ser desabilitada para o usuário atual do sistema ou para todos os usuários, por um administrador do sistema que possua permissão apropriada.

A funcionalidade já vem **ATIVADA** por padrão.

Existem dois jobs referentes à funcionalidade: um job de sincronismo que tenta se conectar à base TOTVS para pegar as regras e ofertas mais recentes e um job de processamento de mensagens, que valida as regras na base do cliente para povoar a fila de mensagens dos usuários.

A cada novo release, o sistema virá com 3 arquivos contendo informações atualizadas: uainferences.xml; uaoffers.xml; uaparameters.xml; Ao abrir o sistema, os dados dos XML serão importados para a base e os arquivos serão removidos.

## Procedimento para Utilização

       1.            Ao acessar qualquer funcionalidade do sistema, se houver uma mensagem associada ela pode ser exibida para o usuário. A mensagem será exibida no canto inferior direito.

        

       2.            Ao clicar no ícone de "engrenagens", serão exibidas duas opções: 1) desativar exibição de mensagens para o usuário atual do sistema. 2) cancelar a exibição da mensagem atual; essa mesma mensagem não será exibida novamente para esse usuário.

        

       3.            Para reativar a exibição das mensagens ou limpar a lista de mensagens bloqueadas, basta acessar a aba de "Análise de Usuário" nos parâmetros globais do sistema.

* + 1) "Ativar notificações" permite ativar ou desativar a funcionalidade para o usuário atual do sistema
  + 2) "Habilitar Análise Preditiva no Sistema" é visível apenas para usuários que sejam supervisores e tenham permissão. Essa opção permite habilitar ou desabilitar a funcionalidade para todos os usuários do sistema.
  + 3) "Limpar lista de mensagens bloqueadas (ao fechar essa tela)": ao marcar essa checkbox e clicar em OK ou Salvar, todas as mensagens que haviam sido previamente bloqueadas pelo usuário serão limpas e voltarão a serem exibidas. Caso o usuário não tenha bloqueado nenhuma mensagem, nada acontecerá.

        

## Parâmetros do Sistema

Existem alguns parâmetros no sistema que são controlados pela TOTVS. Não é possível alterá-los no sistema. São eles:

|  |  |  |
| --- | --- | --- |
| Nome do Parâmetro | Descrição | Valor Padrão |
| DAYSBETWEENSAMEMSG | Dias a esperar antes de exibir uma mensagem novamente para o usuário | 7 |
| HOURSBETWEENEXHIBIT | Horas entre exibição de mensagem para o usuário no sistema (evitar spam de mensagens) | 2 |
| INTERVALJOBMESSAGEQUEUE | Intervalo (em horas) a ser executado o job de processamento da fila de mensagens | 2 |
| INTERVALJOBSYNC | Intervalo (em horas) a ser executado o job de sincronismo com a base TOTVS | 24 |

divs
