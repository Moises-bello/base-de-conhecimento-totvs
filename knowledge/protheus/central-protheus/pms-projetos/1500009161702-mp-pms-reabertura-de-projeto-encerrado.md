---
article_id: 1500009161702
category: PMS - Projetos
content_hash: e692d73604cd6abe5eadbef66aa92a4ba94d38e5c1b87977b3cbfee402c91538
fetched_at: '2026-06-28T22:37:16.004076+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: MP - PMS - Reabertura de Projeto Encerrado
type: support-article
updated_at: '2021-05-04T17:00:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009161702-MP-PMS-Reabertura-de-Projeto-Encerrado
---

**Ocorrência**É possível reabrir um projeto encerrado?  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Projetos - Todas as versões   
  
**Causa**O projeto é encerrado ao utilizar uma fase de projeto com a opção **Permite Encerrar = Sim**, desta forma, o sistema grava essa informação no campo **AF8\_ENCPRJ**.

**Solução**

Por padrão de sistema, ao encerrar o projeto, ele grava o campo **AF8\_ENCPRJ = 1** e  assim, não permite mais reabertura.

Veja a mensagem apresentada no momento da alteração da fase no projeto, antes de confirmar para encerrado:  
***"a alteração de fase não é permitido após encerramento do projeto"***

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014103742/mceclip0.png)**

**Observação:**Aconselhamos que só utilize a fase com a opção encerramento de projeto, se realmente o projeto está em fase final para fechamento e já foi validado por completo, pois uma vez encerrado não será possível reverter.
