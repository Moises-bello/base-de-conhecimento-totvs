---
article_id: 360022027712
category: RH - Folha de Pagamento
content_hash: b987d7389057f7d8356374f7015e5d251b2350fc1093a41e02ffa00f0abf3c5b
fetched_at: '2026-06-28T22:44:12.068407+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de hora extra com salário incorporado por
  verbas com números de códigos superiores
type: support-article
updated_at: '2025-10-08T16:58:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022027712-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-hora-extra-com-sal%C3%A1rio-incorporado-por-verbas-com-n%C3%BAmeros-de-c%C3%B3digos-superiores
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19207878920343) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como configurar corretamente uma **verba** sem **identificador de cálculo** para ser incorporada ao salário e ser base para cálculo das **horas extras**, independente da ordem em que as **verbas** estejam gravadas na tabela **SRV**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que o sistema considere **verbas** do cliente para incorporar ao salário e ser base para outros cálculos, é necessário seguir a ordem abaixo:  
  
**1.** Atualizar o sistema com o pacote do link a seguir: **[Pacote Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)**

**2.** Acesse **Atualizações / Definições de Cálculo / Verbas (GPEA040)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19207878931863)

**3.** Configurar a verba **que irá incorporar o salário**, por exemplo Comissão, preenchendo o campo **Incorp. Sal. como sim** e o campo **Hora Extra como Não;**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019077371)  
 **4.** Configurar as verbas de **hora extra** que **irão usar a nova base para cálculo**, com o campo **Base Cálculo como Salário Incorporado** e com o campo **Hora Extra como Sim;**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019077491)

**Saiba Mais:**

[RH - Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010838314-RH-Verbas-) [-](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010838314-RH-Verbas-) [Verbas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010838314-RH-Verbas-)
