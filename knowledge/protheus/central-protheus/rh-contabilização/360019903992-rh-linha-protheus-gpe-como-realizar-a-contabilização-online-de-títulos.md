---
article_id: 360019903992
category: RH - Contabilização
content_hash: aca24b7aa44b26a381b8f0e36e23c74ecc02043d532bab420767b5250283db44
fetched_at: '2026-06-28T22:43:45.852022+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar a contabilização online de títulos
type: support-article
updated_at: '2025-07-23T20:12:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019903992-RH-Linha-Protheus-GPE-Como-realizar-a-contabiliza%C3%A7%C3%A3o-online-de-t%C3%ADtulos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33671830845591) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como realizar a contabilização online de títulos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**  
Para que seja possível realizar a contabilização online, realize os passos abaixo:

**ATENÇÃO:** as configurações mostradas nos prints abaixo servem apenas para ilustrar o processo. Realize a configuração de acordo com a regra de negócio da sua empresa.   
  
No **Módulo Contábil** (SIGACTB 34):  
**1.** Cadastre as moedas contábeis em **Atualizações > Cadastros > Moedas Contábeis**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015893151)  
  
**2.** Cadastre o Calendário Contábil em **Atualizações > Cadastros > Calendário Contábil**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015844932)  
  
**3.** Realize a amarração da moeda com o calendário contábil em **Atualizações > Cadastros > Amarração Moedas X Calendário**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015844972)  
  
No **Módulo Financeiro** (SIGAFIN 06)  
**1.** Realize o cadastro do lançamento padrão em **Atualizações > Cadastros > Lançamento Padrão**  
Caso seja apresentada a tela abaixo ao acessar a rotina, selecione o F12 do teclado e altere a pergunta Visão Por Processo para NÃO. Dê o OK, saia da rotina retornando ao menu principal e acesse novamente a rotina   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015845172)  
  
**2.** Será mostrada a tela abaixo (não será estes registros que serão mostrados na tela, uma vez que os registros devem ser incluídos manualmente):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015845472)  
  
**3.** Inclua um lançamento com o código do lançamento padrão 510 (as demais configurações devem ser utilizadas apenas de exemplo. Configure os demais campos do lançamento padrão de acordo com sua regra de negócio)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015893891)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015845792)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015893931)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015845912)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015845992)  
  
No **Módulo Gestão de Pessoal** (SIGAGPE 07)  
**4.** Após gerar o título, realize a integração com a pergunta **Contabiliza Online= SIM**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015846072)  
  
**5.** Será aberta a tela mostrando que a contabilização do título foi realizada  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015846032)

**Saber Mais:**

[RH - Linha Protheus - GPE - Como gerar o arquivo em formato de texto da Contabilização com o código do Lançamento Padrão do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008995401-RH-Linha-Protheus-GPE-Como-gerar-o-arquivo-em-formato-de-texto-da-Contabiliza%C3%A7%C3%A3o-com-o-c%C3%B3digo-do-Lan%C3%A7amento-Padr%C3%A3o-do-Protheus)

[RH - Linha Protheus - GPE - Como realizar a contabilização de provisão de férias rateada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13053142707991-RH-Linha-Protheus-GPE-Como-realizar-a-contabiliza%C3%A7%C3%A3o-de-provis%C3%A3o-de-f%C3%A9rias-rateada)

[RH - Linha Protheus - GPE - Como utilizar o ponto de entrada GP110APP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6140879458455-RH-Linha-Protheus-GPE-Como-utilizar-o-ponto-de-entrada-GP110APP)
