---
article_id: 360060589393
category: RH - Lançamentos
content_hash: 66c0099e390086766673e8d8ade364718ad28a5d37fee6345e321c8952a0ed23
fetched_at: '2026-06-28T22:44:46.839914+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Como visualizar as marcações de períodos já fechados
type: support-article
updated_at: '2025-06-13T14:11:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060589393-RH-Linha-Protheus-PON-Como-visualizar-as-marca%C3%A7%C3%B5es-de-per%C3%ADodos-j%C3%A1-fechados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29755439326871) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como verificar as marcações de um período que já foi fechado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para visualizar as marcações de períodos fechados deverá acessar no módulo do Ponto Eletrônico em **Atualizações -> Acumulados -> Marcações**.

Lembrando que essa rotina verifica diretamente a tabela SPG (tabela das marcações dos períodos fechados).  
  
A rotina valida o período de apontamento que consta no campo PG\_PAPONTA (período de apontamento que foi fechado) com o período de apontamento cadastrado na tabela SPO (responsável pelo fechamento do ponto), exemplo período fechado via rotina de apontamento em **Atualizações> Cadastro do Ponto> Períodos de Apontamentos**, é possível visualizar o período fechado na tela inicial da rotina:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29755446204695)

Validado que na PG\_PAPONTA (na tabela SPG) e o período de apontamento na SPO iguais com o campo PO\_RESPONS (na tabela SPO) com S, o sistema vai gerar as marcações acumuladas na rotina **Atualizações -> Acumulados -> Marcações:**

Clicar em **Outras Ações > Períodos** e selecionar o período a ser impresso:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29755446209303)

Será apresentado a tela abaixo, selecionar o período e clicar em "OK":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29755439335703)

Após, selecionar a matricula e clicar em visualizar, será gerado as marcações do período:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29755439342487)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29755439345175)

**Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)
