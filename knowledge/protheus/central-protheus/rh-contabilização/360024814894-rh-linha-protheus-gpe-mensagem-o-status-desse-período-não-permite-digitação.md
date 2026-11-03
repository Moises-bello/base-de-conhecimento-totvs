---
article_id: 360024814894
category: RH - Contabilização
content_hash: aaa255767933b92a15fce2ac45f46ef125683e2b77b10fc8787e57e7896e0966
fetched_at: '2026-06-28T22:43:45.990072+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: 'RH - Linha Protheus - GPE - Mensagem: O status desse período não permite digitação'
type: support-article
updated_at: '2025-07-30T20:48:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024814894-RH-Linha-Protheus-GPE-Mensagem-O-status-desse-per%C3%ADodo-n%C3%A3o-permite-digita%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33832493590039)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como corrigir a mensagem: **O status desse período não permite digitação.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Será apresentada a mensagem de solução: **Verifique o status do calendário para essa data.**  
A mensagem ocorre por ausência de calendário para o período de contabilização. Siga o seguinte procedimento:  
  
1. Acesse o módulo 34 - Contabilidade Gerencial: **Atualizações -> Cadastros -> Calendário Contábil.**Em sua tela será apresentada a opção de incluir o calendário. No exemplo abaixo já possuímos um calendário referente ao ano de 2018 e incluiremos um novo calendário referente ao ano de 2019.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039093873)**

2. Será necessário que exista uma moeda contábil cadastrada (Atualizações -> Cadastros -> Moedas Contábeis) . ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039094213)  
3. Acesse: **Atualizações -> Cadastros -> Moedas x Calendários**  
***Importante:***Para um mesmo calendário, pode haver mais de uma moeda amarrada. Porém, devem ser evitados conflitos entre calendários e moedas, isto é, para uma mesma moeda não deve ser utilizado mais de um calendário com exercício contábil similar.![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038259154)

4. Após amarração Moedas x Calendários, acesse **Miscelânea -> Fechamentos -> Contabilização** e refaça o processo de contabilização.   
Obs: A data apresentada no cabeçalho estará compreendida no calendário cadastrado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039396353)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como configurar Lançamento Padrão para Folha de Pagamento do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-RH-Linha-Protheus-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-do-Protheus-)
