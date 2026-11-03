---
article_id: 360059124694
category: RH - Folha de Pagamento
content_hash: aa29dc96870617fd7cae0dff1468aceadf35446d4477fcb58cf5b8325f7d2d90
fetched_at: '2026-06-28T22:44:15.060641+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Mensagem no log de calculo "Registros Não Processados"
type: support-article
updated_at: '2025-08-11T21:07:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059124694-RH-Linha-Protheus-GPE-Mensagem-no-log-de-calculo-Registros-N%C3%A3o-Processados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26337424188951) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**Sistema apresenta log de calculo com a seguinte mensagem: "Registros Não Processados".  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Se existirem demissões na competência (Período) em aberto, no calculo da folha será exibido o log com a seguinte mensagem: "**Registros Não Processados**"  
  
**Solução**Não se trata de um erro, e sim de uma mudança no sistema, que passou a não calcular a folha para funcionário Demitidos, ou seja, o **Roteiro FOL** apenas irá transportar os lançamentos da **RGB** (**Lançamento Por Funcionários**) para a tabela **SRC** (**Movimento do Período**), a mudança foi necessária para evitar lançamentos na Folha diferentes da Rescisão. 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099634974)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
