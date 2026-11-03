---
article_id: 23136608500759
category: Financeiro - Contas a Pagar - Comunicação Bancária Online
content_hash: 9cbb939f73a529e9c3b2d46ee500f8d6273c37158dc95d8c5d3470e554a91ae7
fetched_at: '2026-06-28T22:37:49.929892+00:00'
product: protheus
section_id: 26656222001687
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA718 - Banco do
  Brasil - Configurar retorno via API para baixar títulos a pagar de forma automática
type: support-article
updated_at: '2025-10-07T21:26:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23136608500759-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA718-Banco-do-Brasil-Configurar-retorno-via-API-para-baixar-t%C3%ADtulos-a-pagar-de-forma-autom%C3%A1tica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23136577343127) Tempo aproximado para leitura: **00:05:00min****Dúvida**Como habilitar o retorno via API para baixar títulos a pagar de forma automática?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - A partir da release 33  
  
**Solução**  
1. Na **Configurações de Conta** do **Novo Gestor Financeiro**, posicione no banco utilizado para realizar o envio do **título a Pagar**, clique nos três pontinhos e depois '**Editar**':  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23136608449687)  
  
2. Depois disso, clique em '**Outras Ações**' e selecione a opção '**Baixa títulos(Retorno)**':  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23136577352599)  
  
3. Por fim, selecione a opção **'Utiliza Retorno Bancário**', deixando marcado como '**Sim**':  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23136577357207)   
Além dos pontos mencionado acima, se faz necessário também configurar o *job* da **FINA718** no **Configurador**, na rotina '**Schedule**'.  
  
4. Acessar o Schedule e depois '**Agendamentos**'  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23136608457879)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23136608460183)

5. Configurar o **JOB da FINA718**, nomeando com **FINA718('01')** - 01 seria o **grupo da empresa**, então, preencher de acordo com seu grupo. Depois disso, configurar selecionando somente um **grupo** e uma **filial** deste grupo. Dessa forma, o **JOB** funcionará para todas as filiais deste mesmo grupo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23136577365271)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23136577367575)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23136608466455)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23136577371415)

**Saiba mais:**[Job de retorno dos pagamentos - FINA718](https://tdn.totvs.com.br/display/public/PROT/Job+de+retorno+dos+pagamentos+-+FINA718)
