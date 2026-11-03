---
article_id: 360051313514
category: RH - Definições de Cálculo
content_hash: 43a12cf4be9685c543833c8a8f48a2dff659fa5ca844a48129aedf3914666311
fetched_at: '2026-06-28T22:43:22.475537+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: 'RH - Linha Protheus - GPE - Geração período padrão mostra mensagem: Não foi
  informada a data inicial para a criação do período'
type: support-article
updated_at: '2025-10-02T13:55:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051313514-RH-Linha-Protheus-GPE-Gera%C3%A7%C3%A3o-per%C3%ADodo-padr%C3%A3o-mostra-mensagem-N%C3%A3o-foi-informada-a-data-inicial-para-a-cria%C3%A7%C3%A3o-do-per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32865937526551) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Ao executar a rotina GPEA490 - Geração de Período padrão, gera mensagem: **Não foi informada a data inicial para a criação do período, na rotina de verbas pro processo**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**Faça o seguinte procedimento:  
  
**1-** Acessar em **Atualizações> Definições de Cálculo> Padrão Período - GPEA500** e clique em incluir, faça a inclusão do período padrão considerando:

- O **campo código e descrição** fica a critério da empresa

- O **campo Ref. Período** deverá ser informado o mês

- O **campo Num. Pagto** deverá ser informado o número de pagamento no caso 01

- O **campo Dias Período** deverá ser informado a quantidade de dias do mês, exatamente como no calendário

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081669693)

**Saiba Mais**[RH - Linha Protheus - GPE - Como Criar Períodos Automaticamente pela Rotina Geração Período Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010729592-RH-Linha-Protheus-GPE-Como-Criar-Per%C3%ADodos-Automaticamente-pela-Rotina-Gera%C3%A7%C3%A3o-Per%C3%ADodo-Padr%C3%A3o?source=search)[RH - Linha Protheus - GPE - Ao tentar gerar um período padrão aparece a mensagem: A geração será possível somente para roteiros por processo que utilizam padrão de períodos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010841388-RH-Linha-Protheus-GPE-Ao-tentar-gerar-um-per%C3%ADodo-padr%C3%A3o-aparece-a-mensagem-A-gera%C3%A7%C3%A3o-ser%C3%A1-poss%C3%ADvel-somente-para-roteiros-por-processo-que-utilizam-padr%C3%A3o-de-per%C3%ADodos?source=search)
