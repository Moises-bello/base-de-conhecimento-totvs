---
article_id: 35813677592087
category: Materiais - Compras (SIGACOM)
content_hash: 0cd750ba4a985bcc81debb6074e1b07b00a1c797aa0970398567198b2eb89797
fetched_at: '2026-06-28T22:41:21.869055+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - O que fazer quando
  Rotina do Novo Fluxo de Compras ficar congelada
type: support-article
updated_at: '2025-11-07T15:02:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35813677592087-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-O-que-fazer-quando-Rotina-do-Novo-Fluxo-de-Compras-ficar-congelada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35813677566615) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Ao abrir a rotina do Novo Fluxo de Compras, o sistema carrega a tela inicial mas nenhum botão do menu esquerdo funciona, ficando impossibilitada sua utilização. Além disso pode ocorrer de gerar uma validação "javascript" no canto inferior esquerdo da tela. Como solucionar? O que fazer quando ao entrar na rotina fica carregando e não mostra nenhuma informação?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35813672278039)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35991928191383)  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310  
  
**Solução**  
Para solução da ocorrência reportada, realize os dois passos abaixo.

**1º Passo**

Por gentileza realize teste em ambiente de Homologação com as atualizações a seguir:

- [Acumulado Compras conforme sua versão](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)  
- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168735)  
- [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/) - [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1112215) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168420)

- Smartclient - [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1112221)

- Smartclient WebApp - [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168455)

- DBAccess - [MP - FRAME - Atualização do DBAccess](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033789713-MP-FRAME-Atualiza%C3%A7%C3%A3o-do-DBAccess?source=search)

***Obs: Recomendamos backup e validação primeiramente em ambiente teste.***

**2º Passo**

Renomeie a pasta **HTTP\_ROOT** que fica dentro do diretório **Protheus\_Data.** Após isso **reinicie os serviços** do APPSERVER e realize novo teste.

***Observação***

Caso a rotina seja aberta corretamente, porém o sistema apresente lentidão ao listar as cotações na tela de Cotações, poderá ser seguida a mesma tratativa abordada nesta documentação.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
