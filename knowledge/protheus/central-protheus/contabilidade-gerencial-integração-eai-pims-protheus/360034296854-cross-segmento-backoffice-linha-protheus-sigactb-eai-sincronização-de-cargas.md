---
article_id: 360034296854
category: Contabilidade Gerencial - Integração EAI PIMS Protheus
content_hash: 810e8371194965f98fff7d429e66b64675aff8b88b29cd7308f610fd1f897095
fetched_at: '2026-06-28T22:40:54.165661+00:00'
product: protheus
section_id: 1500001537541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB  EAI - Sincronização de
  Cargas
type: support-article
updated_at: '2025-10-10T19:30:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034296854-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-EAI-Sincroniza%C3%A7%C3%A3o-de-Cargas
---

**Dúvida**Para que serve e como usar a rotina**APCFG020A**(Sinc. Carga Inicial Protheus)?

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - A partir da 12.1.17

**Solução**A rotina de Sincronização e Carga Inicial Protheus EAI tem como objetivo realizar o cadastro dos dados que estão no Protheus e devem ser utilizados também nas outras marcas da TOTVS (Ex: PIMS e RM).

Segue os passos de utilização abaixo:

1- Antes de realizar a Sincronização, o cliente deverá verificar se a comunicação via do Protheus e outras marcas está funcionando através do **WebService**.

2- Será necessário que esteja configurado o **cadastro de empresa/filial da mensagem única**, neste cadastro é necessário realizar o De/Para das filiais contidas no Protheus e outras marcas, para a acessar a rotina, logue no sistema pelo **Módulo Configurador > Ambiente > Schedule > Emp. Filial Mensagem Única(APCFG050)**.

3- Agora será necessário cadastrar o **Adapter** da mensagem envolvida na Sincronização/Carga Inicial, esta rotina tem como objetivo definir a forma que a integração entre os produtos será realizada, para acessar, entre no sistema pelo módulo **Configurador > Ambiente Schedule > Adapter eai,** veja a documentação da funcionalidade: [Adapter Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=312157611)

4- Para utilizar a rotina de **Sincronização e Carga inicial do Protheus (APCFG020A),** acesse o módulo de **Configurador > Ambiente > Schedule > Sinc. Carga Inicial Eai**, nela deverá selecionar o **Adapter** do cadastro desejado e clicar em inicializar sincronização:

![](https://totvssuporte.zendesk.com/attachments/token/jrkS5GpTgVEDi4RnkTLAA15yE/?name=inline767435866.png)

A partir desse momento será apresentado um Wizard com a quantidade de processos, basta confirmar e esperar para que a carga inicial seja feita. Se desejar verificar os detalhes do processo, selecione o botão de Log de Sincronização que fica ao lado da opção de inicio de sincronização.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Help_buttonImportante:  |  |  | | --- | --- | | • | Não há controle de registro existente, ou não, na outra base. |  |  |  | | --- | --- | | • | É possível determinar a quantidade de processos a serem executados, no mínimo 1 e máximo 9. |  |  |  | | --- | --- | | • | É possível reprocessar caso tenha alguma mensagem de erro. |  |  |  | | --- | --- | | • | Caso tenha processos com erro a sincronizar, os demais adapters não são sincronizados. | |

Outra documentação da rotina: [Sincronização](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/apcfg020a.htm)
