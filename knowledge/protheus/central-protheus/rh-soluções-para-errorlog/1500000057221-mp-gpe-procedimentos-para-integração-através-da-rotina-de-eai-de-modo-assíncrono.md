---
article_id: 1500000057221
category: RH - Soluções para error.log
content_hash: 78f25bbd7d0dda6be427afa035dca1128cdf823d03779b20ca783e92272f4a5f
fetched_at: '2026-06-28T22:44:09.013611+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: MP - GPE - Procedimentos para integração através da rotina de EAI de modo Assíncrono
type: support-article
updated_at: '2021-01-29T16:35:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000057221-MP-GPE-Procedimentos-para-integra%C3%A7%C3%A3o-atrav%C3%A9s-da-rotina-de-EAI-de-modo-Ass%C3%ADncrono
---

**Dúvida**Procedimentos para efetuar **integração** através da rotina de **EAI** de modo **Assíncrono****Ambiente**Protheus - Gestão de Pessoal - à partir da versão 12.1.17  
  
**Solução**Envio de mensagens **Assíncronas:**Quando um evento de integração é disparado no **Protheus**, o ***adapter*** cadastrado é chamado para executar o envio da mensagem. A rotina de processamento gera o *XML* de integração e esta mensagem é gravada na tabela **XX3** (a fila de mensagens do **EAI Protheus**).  
De acordo com a recorrência cadastrada para a rotina de transmissão das mensagens do **EAI** esta fila é lida e os registros que se encontram em condições de envio são enviados para o sistema receptor. Um registro está em condições de envio se respeitar as condições a seguir:  
-> A mensagem seja do tipo **assíncrona** e o número de tentativas de envio para o sistema receptor seja menor que 4;  
-> A Mensagem esteja com o *status* de 'Aguardando execução', 'Falhou' ,'Não entregue' ou 'Recusada'.  
  
Para que o envio das mensagens **assíncronas** seja realizado, é necessário que seja realizado o cadastro no ***Schedule* Protheus,** da rotina **FWEAI**. Esta rotina é responsável pelo envio e recebimentos das mensagens na fila do **EAI**. Caso necessário, pode ser realizado o agendamento da rotina **FWEAISEND**. Esta rotina é exclusiva para o envio das mensagens da fila do **EAI**. O agendamento desta rotina é realizado por **Empresa/Grupo de Empresas** cadastrado no sistema. No envio da mensagem, um canal de comunicação é aberto com o *webservice* do produto integrado e esta comunicação é encerrada após o recebimento da mensagem de retorno (no caso das Mensagens Únicas **TOTVS**, após o recebimento da *ReceiptMessage*, indicando que o processo ocorreu corretamente) ou por *timeout* (mensagem com status de falha).  
Posteriormente, o outro sistema integrado poderá gerar uma outra mensagem de resposta (no caso das Mensagens Única Totvs, será gerada uma *ResponseMessage)* após o processamento da mensagem.

**1. Exemplo de configuração da rotina FWEAI:**Em ambiente>*schedule*>*schedule*, é necessário efetuar o cadastro da rotina, conforme abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000224441/mceclip0.png)  
  
**2. Exemplo de configuração de *ADAPTERS* de modo Assíncrono:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099091914/mceclip1.png)  
  
  
  
**Saiba mais**Documentação EAI:<https://tdn.totvs.com/display/framework/A+camada+do+EAI>  
  
Configuração de schedule:  
<https://tdn.totvs.com/pages/viewpage.action?pageId=271167961>
