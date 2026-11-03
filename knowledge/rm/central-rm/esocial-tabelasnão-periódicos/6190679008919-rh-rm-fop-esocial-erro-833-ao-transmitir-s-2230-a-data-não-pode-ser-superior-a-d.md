---
article_id: 6190679008919
category: eSocial - Tabelas/Não Periódicos
content_hash: 38e166470fed07d7b351d69d835ac17854cffb7780f78450611673a90892845f
fetched_at: '2026-06-28T22:47:10.340970+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 833 ao transmitir S-2230: A data não pode ser
  superior a data atual'
type: support-article
updated_at: '2025-07-02T20:49:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6190679008919-RH-RM-FOP-eSocial-Erro-833-ao-transmitir-S-2230-A-data-n%C3%A3o-pode-ser-superior-a-data-atual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência** Ao transmitir o evento S-2230 é apresentada a mensagem **Código do erro: 883 Descrição: Data de Início do Afastamento inválida. Ação Sugerida: A data não pode ser superior a data atual, exceto se o motivo do afastamento for férias, situação em que pode ser ate 60 dias superior a data atual ou se o motivo do afastamento for licença maternidade, situação em que pode ser até 120 dias superior a data atual.**

![883.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/6190695217943/883.PNG)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre quando o afastamento está sendo enviado em data anterior superior a quantidade de dias permitido a data de inicio do afastamento.

**Manual de Orientação eSocial pág. 171**

![33.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/6190860678807/33.PNG)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o cadastro do afastamento do funcionário em **Anexos | Históricos | Histórico de Afastamentos** e localize o afastamento em questão;
2. Consulte a data de início do afastamento e verifique se a data de envio é **igual ou anterior à data atual**;
3. Para corrigir este de fato, será preciso **aguardar até que a data esteja dentro dos requisitos do eSocial**;
4. Após aguardar a data correta, acesse a **Fila de Eventos** e envie o registro ao eSocial.

**Importante**  
No caso de férias, o sistema permite que seja configurado para que o envio para o TAF não ocorra antes do período permitido pelo governo. Basta acessar o menu **Configurações | Parametrizador | eSocial** e, na etapa **Configurações Gerais 4/7**, preencher o parâmetro abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6219207530263/mceclip0.png)
