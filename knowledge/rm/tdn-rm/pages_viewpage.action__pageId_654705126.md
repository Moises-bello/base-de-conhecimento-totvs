---
content_hash: 5a017590a0804d78af5adadbf56ba3837423ed254889118c6ad7e0f96e0f597b
fetched_at: '2026-06-29T00:11:12.541293+00:00'
page_id: '654705126'
product: rm
source: tdn-rm
title: Integração RM x SmartLink Behavior Sharing
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=654705126
version: 35
---

## **01. Apresentação**

Este documento tem por objetivo auxiliar as equipes dos segmentos no entendimento do mecanismo de integração do RM com a plataforma de mensagens do SmartLink.

## **02. SmartLink**

O SmartLink é o mediador das mensagens entre a plataforma TOTVS Apps (*cloud*) e ERPs (*on premise*), e por sua vez é formado por dois componentes: SmartLink Client (*on premise*), e SmartLink Server (*cloud*).

Esta arquitetura somente pode ser utilizada na comunicação entre aplicativos hospedados na plataforma TOTVS Apps (ex: TPD) com os ERPs. Ou seja, não será possível utilizar essa comunicação entre os ERPs do grupo.

Nesse caso, deve ser utilizado o EAI para a comunicação entre ERPs.

Como exemplo, a integração entre o ERP RM com o TPD (TOTVS Privacidade de Dados) ocorre através da plataforma SmartLink.

**Exemplo de uso:**

1. 1. 1. Aplicativo TPD publica uma mensagem no "SmartLink Server" solicitando uma anonimização de dados. Nesse momento a solicitação fica com o status de "Em Processamento".
      2. ERP RM (SmartLink Client) consome essa mensagem em um momento posterior, providenciando a anonimização dos dados em seu banco de dados;
      3. ERP RM (SmartLink Client) envia as respostas para o o SmartLink Server;
      4. Aplicativo TPD consome as respostas enviadas pelo RM providenciando a mudança do status original da solicitação para "Processada".

A plataforma Smart Link somente poderá ser usada pelos segmentos se o evento de negócio em questão possuir a natureza "assíncrona", ou seja, o publicador da mensagem não precisará de uma resposta imediata para prosseguir com seu processamento.

Essa comunicação entre os aplicativos hospedados na plataforma TOTVS Apps com o ERP RM ocorrerá através da troca de mensagens entre o componente SmartLink Server com o componente SmartLink Client (localizado na framework RM).

A intenção é que os clientes possuam em sua infraestrutura apenas o **SmartLink Client**, uma vez que o Smart Link Server será mantido pela TOTVS na nuvem.

## **03. Log de execução da integração RM x SmartLink**

Todos os logs de execução das mensagens Smart Link Client são gravados na tabela GTotvsLinkLog. Essa tabela contém os seguinte atributos:

| Coluna | Descrição |
| --- | --- |
| ID | Chave primária da tabela. Identificador único do Log. |
| IDMENSAGEM | Identificador único da mensagem relacionada a mensagem gravada em "GTotvsLInkMessage.ID". É através desse campo  que o usuário poderá filtrar todos os logs de uma determinada mensagem. |
| LOGTYPE | 0 - Mensagem de informação  1 - Mensagem de aviso  2 - Mensagem de erro |
| LOGMENSAGEM | Texto contendo o log |
| LOGDATE | Data de geração do Log |
| DATADEBUG | Informações extras do log |

## **04. Modelo de dados do RM SmartLink client**

| Tabela |  |
| --- | --- |
| GTOTVSLINKMESSAGE | Tabela utilizada para armazenar todas as mensagens geradas e enviadas para execução pelo Smart Link Client.  Sempre que uma mensagem é executa com sucesso, a linha referente a mensagem é excluída  dessa tabela , deixando essa tabela sempre leve. Esse procedimento melhora a performance do processo,  visto que vários "updates" são realizados nessa tabela. Quanto menor o volume de uma tabela, mais rápido  serão as operações do update e detele. |
| GTOTVSLINKMESSAGEEXEC | Tabela contendo todos os dados de execução de uma determinada mensagem. O conteúdo dessa tabela nunca será excluído,  ficando portanto como um histórico de execução. Porém, essa tabela poderá ter um volume muito grande.  Sendo assim, seria importante de tanto em tanto tempo mensagens muito antigas serem excluídas dessa tabela. |
| GTOTVSLINKLOG | Tabela contendo todos os logs de execução de uma mensagem. O conteúdo dessa tabela nunca será excluído, ficando portanto como um histórico de log de execução. Porém, essa tabela poderá ter um volume muito grande.  Sendo assim, seria importante de tanto em tanto tempo logs muito antigos serem excluídos dessa tabela. |
