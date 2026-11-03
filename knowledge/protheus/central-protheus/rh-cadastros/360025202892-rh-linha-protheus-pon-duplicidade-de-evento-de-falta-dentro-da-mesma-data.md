---
article_id: 360025202892
category: RH - Cadastros
content_hash: 437745ed7d609b3b7f09be26bb0b5c0b02f33eb9334afee621ed2ba55fefbd26
fetched_at: '2026-06-28T22:44:52.975121+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Duplicidade de evento de falta dentro da mesma
  data
type: support-article
updated_at: '2025-12-29T12:17:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025202892-RH-Linha-Protheus-PON-Duplicidade-de-evento-de-falta-dentro-da-mesma-data
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34296067407767) Tempo aproximado para leitura:00:01:00 min**  
  
**Dúvida**  
O que fazer quando o sistema gera dois eventos de falta para a mesma data dentro da rotina de marcações?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Na rotina de marcações em **Atualizações> Lançamentos> Marcações** ao reapontar, o sistema gera evento de falta integral antes do intervalo e após o intervalo, dividindo o evento em 2 apontamentos, e no espelho de ponto essa informação também será apresentada duas vezes.

Veja como fica o apontamento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34296099661079)  
  
  
**Configurações a serem observadas**:

O evento é gerado dessa forma por conta de configuração do campo **R6\_APTPMAR** que está configurado com **SIM** na rotina de Turnos de Trabalho em **Atualizações > Cadastros Gerais > Turnos de Trabalho.**

Para correção é necessário realizar manutenção no cadastro do Turno de Trabalho ajustado o campo **R6\_APTPMAR** para **Não** no Turno atrelado ao colaborador. Dessa forma o sistema irá gerar o evento uma única vez e integralmente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34296067409175)  
  
  
Segue abaixo o evento gerado após ajuste na configuração:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34296067410711)  
  
  
  
  
**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como cadastrar um Turno de Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410322419095-RH-Linha-Protheus-PON-Como-cadastrar-um-Turno-de-Trabalho)  
[RH - Linha Protheus - PON - Como fazer o apontamento considerando o Tipo de marcação - Apontamento por marcação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024756513-RH-Linha-Protheus-PON-Como-fazer-o-apontamento-considerando-o-Tipo-de-marca%C3%A7%C3%A3o-Apontamento-por-marca%C3%A7%C3%A3o)
