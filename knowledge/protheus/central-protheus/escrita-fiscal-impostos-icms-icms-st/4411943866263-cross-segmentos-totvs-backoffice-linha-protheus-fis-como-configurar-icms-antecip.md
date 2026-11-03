---
article_id: 4411943866263
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 1abad5f7697272b50a89c49525529a255b540138c6f51db1354d3cc0e8141c59
fetched_at: '2026-06-28T22:39:20.400676+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar ICMS
  antecipado operações internas PE?
type: support-article
updated_at: '2021-11-01T13:39:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411943866263-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-ICMS-antecipado-opera%C3%A7%C3%B5es-internas-PE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:05:00**min** **Dúvida**MP - FIS Como configurar ICMS antecipado operações internas PE?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões

**Solução**

Seguir as configurações abaixo:

MV\_ESTADO = PE  
Fornecedor = PE  
  
  
UFxUF no módulo Livros Fiscal em Atualizações > Sped > UFxUF (FISA080).  
  
![](https://totvssuporte.zendesk.com/attachments/token/08hYb4v2gP5vQIdClX1SW23fm/?name=inline-966573079.png)​  
  
b. Rotina Exceções Fiscais no módulo Livros Fiscal em Atualizações > Cadastros > Exceções Fiscais (MATA540).  
![](https://totvssuporte.zendesk.com/attachments/token/BK2m3bAOaZAtRmLjNQVxFcCk3/?name=inline2103039099.png)​  
Cadastro de produtos o grupo amarrado  
![](https://totvssuporte.zendesk.com/attachments/token/hIVDJHnhlsKvXPl3HtCypouKC/?name=inline860369951.png)​  
  
3. Configuração da TES no módulo Livros Fiscal em Atualizações > Cadastro > Tipos de Entrada e Saída (MATA080).  
a. Alterar campo da antecipação de ICMS na Aba Outros > campo F4\_ANTICMS = 1 - Sim.  
b. Amarração TES X Lançamento da Apuração, vincular o código da apuração de acordo com sua necessidade.  
  
TES  
![](https://totvssuporte.zendesk.com/attachments/token/bRjBhTND3dNAhBP1SaRZox5kd/?name=inline-1159370984.png)​  
  
Código de reflexo  
![](https://totvssuporte.zendesk.com/attachments/token/rGpS8CfHrKjisfcyhfwXnTwVI/?name=inline-734308176.png)​  
  
Ao lançar a nota fiscal de entradas o valor na aba de apuração do icms está correto  
  
valor da mercadoria = 1100,00  
![](https://totvssuporte.zendesk.com/attachments/token/NVBzif1NUqj9A4fkxhXgxtYmN/?name=inline-1567390545.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/UzdBiPbglbo5SGeqvkSaUBLMX/?name=inline-1368504672.png)​  
  
Os valores nos campos FT\_VALANTI e F3\_VALANTI. somente serão gravados se o fornecedor não for do simples nacional.

Boletim

<https://tdn.totvs.com/pages/releaseview.action?pageId=516199161>
