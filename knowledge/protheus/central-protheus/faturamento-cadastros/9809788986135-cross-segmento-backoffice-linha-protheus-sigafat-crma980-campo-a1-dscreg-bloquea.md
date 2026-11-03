---
article_id: 9809788986135
category: Faturamento - Cadastros
content_hash: 0fb9674a6ea6ff39decce8ff0089319cc43ad5f7d369a09cd8b43b77a0c1882a
fetched_at: '2026-06-28T22:38:35.223946+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAFAT- CRMA980 - Campo A1_DSCREG
  bloqueado para alteração de tamanho
type: support-article
updated_at: '2022-10-26T19:05:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9809788986135-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFAT-CRMA980-Campo-A1-DSCREG-bloqueado-para-altera%C3%A7%C3%A3o-de-tamanho
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min**

**Duvida:**

Como editar o tamanho do campo **A1\_DSCREG** quando ele estiver bloqueado para alteração?

**Ambiente:**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Até a Versão 12.1.33

**Solução:**

Realizado o ajuste no Dicionário de Dados para permitir a alteração do tamanho do campo referente a descrição da região.

Para solucionar essa dúvida, realize os seguintes passos:

**1. Aplicar o pacote de Expedição Contínua do CRM que se encontra no link abaixo;**

<https://tdn.totvs.com/pages/viewpage.action?pageId=521997496>

**2. Rodar o UPDDISTR;**

**![upddistr.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/9811531038359)**

**3. Seguir o passo a passo da documentação abaixo para alterar o tamanho do campo;**

3.1 **-** Acessar o módulo Configurador (SIGACFG);

**![imag_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9811597567639)**

3.2 - Acessar o menu *Dicionário*→*Base de Dados;*

***![ima_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/9811637621271)***

3.3 - Pesquise pela tabela SA1 e em seguida clique na lupa para *Pesquisar;*

***![ima_3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/9811644450583)***

*3.4 - Após pesquisar selecione a tabela SA1 e clique em Editar, selecione a pasta Campos;*

***![ima_4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/9811646689175)***

*3.5 - Pesquise pelo campo A1\_DSCREG e clique em editar;*

***![ima_5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/9811694892695)***

*3.6 - Altere o tamanho do campo A1\_DSCREG, conforme a necessidade e clique em Salvar;*

***![ima_6.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/9811650913303)***

*3.7 - Clique em Confirmar;*

***![ima_7.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/9811668946199)***

*3.8 - Para finalizar clique em Salvar.*

***![ima_8.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/9811670929431)***
