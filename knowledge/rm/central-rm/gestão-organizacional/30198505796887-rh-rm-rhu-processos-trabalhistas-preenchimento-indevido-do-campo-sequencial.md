---
article_id: 30198505796887
category: Gestão organizacional
content_hash: 731d894438a79d387b4fcd180cf4bf24dca12946847839ea978c7a0868e03c09
fetched_at: '2026-06-28T22:47:22.231801+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - Processos Trabalhistas: Preenchimento indevido do campo ''Sequencial'''
type: support-article
updated_at: '2025-03-21T19:49:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30198505796887-RH-RM-RHU-Processos-Trabalhistas-Preenchimento-indevido-do-campo-Sequencial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30198505770519) Tempo aproximado para leitura: **00:02:03 min** **Dúvida**O evento **S-2501 - Informações dos Tributos Decorrentes de Processo Trabalhista** foi devidamente cadastrado e enviado, constando no RM com o status **10 - Aceito RET**, mas a guia para pagamento **não foi gerada no Portal e-CAC**. Acessei o site do Governo e a Informação dos Tributos Decorrentes de Processo Trabalhista é exibida com o botão 'Consolidar'. O que fazer?   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30198475478807)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.2402.245**, **12.1.2406.185**, **12.1.2410.121** e **superiores**.  
  
**Solução**Este comportamento é apresentado quando o evento **S-2501 - Informação dos Tributos Decorrentes de Processo Trabalhista** é enviado com o campo **Sequencial** preenchido:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30198475481239)  
  
Este campo deverá ser preenchido somente quando se tratar de um processo trabalhista que possui mais de um reclamante ou quando é necessário enviar o evento S-2501 mais de uma vez, pois o campo está diretamente ligado ao evento **S-2555 - Solicitação de Consolidação das Informações de Tributos Decorrentes de Processo Trabalhista**.  
  
Quando preenchido indevidamente, ou seja, em um processo que possui apenas um reclamante ou será pago em parcela única, terá o mesmo comportamento: aguardar que o usuário acesse o site do Governo e realize a consolidação para que a guia de pagamento seja devidamente gerada no Portal e-CAC.  
  
Para orientá-los quanto ao cenário, consultamos o Suporte do eSocial - Governo e obtivemos o seguinte retorno:

*O contribuinte poderá excluir o evento S-2501 ou consolidar o evento S-2555. Não será possível retificar o campo Sequencial no evento S-2501 aceito, pois é um campo chave.*  
  
*Neste caso, deverá ser realizado o que for causar menos problemas operacionais ao contribuinte.*

Portanto, considerando as opções supracitadas, deverá ser realizado o ajuste que melhor se adequar à sua necessidade.  
  
Para maiores orientações, é possível acionar diretamente o Suporte do eSocial - Governo através dos canais de atendimento listados no link abaixo:  
  
[RH - RM - FOP - eSocial - Contato com o Governo para dúvidas sobre os eventos do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004050432)  
  
**Importante**  
O ato de 'Consolidação' disponível no site do Governo é suficiente para que a guia seja devidamente gerada no Portal e-CAC.  
  
**Saiba Mais**Para maiores informações sobre o preenchimento do campo em questão, acesse:  
[‭RH - RM - RHU - Processos Trabalhistas: Dúvidas quanto ao preenchimento do campo 'Sequencial'‬](%E2%80%ADRH%20-%20RM%20-%20RHU%20-%20Processos%20Trabalhistas:%20D%C3%BAvidas%20quanto%20ao%20preenchimento%20do%20campo%20'Sequencial'%E2%80%AC)
