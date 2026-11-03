---
article_id: 360029258471
category: RH - Férias
content_hash: c99ea036a3f74105bb6c841c8e6f558902c0c9af0b0fd1881b8eb8ce8886fee0
fetched_at: '2026-06-28T22:43:58.356926+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Pensão Alimentícia de 13º Salário no cálculo das
  Férias com valor Dobrado
type: support-article
updated_at: '2025-09-02T17:48:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029258471-RH-Linha-Protheus-GPE-Pens%C3%A3o-Aliment%C3%ADcia-de-13%C2%BA-Sal%C3%A1rio-no-c%C3%A1lculo-das-F%C3%A9rias-com-valor-Dobrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26668185183767) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Ao imprimir o Recibo da 1ª Parcela do 13º salário recebido nas férias, o sistema apresenta o valor dobrado de desconto da Pensão do Adiantamento do 13º .  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O erro ocorre quando a verba de desconto de Pensão tem o campo **Id de Cálculo preenchido.**  
Após a criação da rotina "Beneficiários", onde o funcionário pode ter mais de um beneficiário, o cálculo da Pensão passou a validar as informações inseridas na rotina GPEA280, e o **uso do Id não é mais necessário**, porém quando preenchido, pode acarretar erros como este.   
Os Ids permanecem na versão 12 somente como legado.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse: **Atualizações / Definições de Cálculo / Verbas** e localize a verba de Pensão Alimentícia e apague o conteúdo do campo **Id de Cálculo (RV\_CODFOL)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26668185192215)

2. Acesse: **Miscelânea / Cálculos / Férias / Outras ações / Impressão** e imprima o Recibo da 1ª parcela do 13º salário novamente.

Calculo de férias 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26668185197719)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26668185205399)

**Saiba Mais**[RH - Férias](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597291-RH-F%C3%A9rias)  
[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[Manual de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=941247504)
