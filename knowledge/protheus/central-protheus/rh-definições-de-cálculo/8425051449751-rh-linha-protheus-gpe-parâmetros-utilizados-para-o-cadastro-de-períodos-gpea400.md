---
article_id: 8425051449751
category: RH - Definições de Cálculo
content_hash: bf79750bbafe457ad86794c6c1af7c09ff7fbbd74b706d330cdf8ed04952815e
fetched_at: '2026-06-28T22:43:22.495705+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Parâmetros utilizados para o Cadastro de Períodos
  - GPEA400
type: support-article
updated_at: '2025-11-27T21:40:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8425051449751-RH-Linha-Protheus-GPE-Par%C3%A2metros-utilizados-para-o-Cadastro-de-Per%C3%ADodos-GPEA400
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32853389627799) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Quais são os parâmetros utilizados para o Cadastro de Períodos da Folha de Pagamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução:**  
Os parâmetros relacionados ao Cadastro de Período, são:  
  
**• MV\_DIASPER** – Define a quantidade de dias do período para cálculo.  
**1** = Utiliza a quantidade de dias do mês do período  
**2** = Utiliza sempre 30 dias como divisor  
  
**• MV\_MODFOL** – Indica a versão da folha de pagamento utilizada.  
**1** = Modelo padrão  
**2** = Modelo 2  
  
**• MV\_OPESOC** – Define se será utilizado o **Controle de Beneficiário – Órgão Público**. Quando habilitado, permite a integração de eventos não periódicos para beneficiários de órgãos públicos.  
**.T.** = Habilitado  
**.F.** = Desabilitado (padrão)

**Atenção:** Ao habilitar o parâmetro MV\_OPESOC o sistema gera os eventos próprios de entes públicos como o S-2400 / S-2405.   
  
**• MV\_PERMOD2** – Habilita o cadastro de períodos simplificado para a Folha Modelo 2.  
**.F.** = Não utiliza (padrão)  
**.T.** = Utiliza  
  
**• MV\_SIGAGFP** – Define a utilização do módulo SIGAGFP (Gestão de Folha Pública).  
**1** = Não utiliza  
**2** = Folha Pública  
**3** = Folha Mista  
  
**• MV\_TPCALEN** – Determina o tipo de calendário utilizado no Cadastro de Períodos:  
**1** = Analítico (padrão): o sistema monta o calendário do mês dia a dia, permitindo ajustes no tipo de cada dia (trabalhado, não trabalhado, DSR), além de controlar se haverá ou não desconto de benefícios como VT e VR  
**2** = Sintético: o sistema **não** monta o calendário de períodos.

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como efetuar o cadastro de período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052262653-RH-Linha-Protheus-GPE-Como-efetuar-o-cadastro-de-per%C3%ADodo)  
[RH - Linha Protheus - GPE - Como Criar Períodos Automaticamente pela Rotina Geração Período Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010729592-RH-Linha-Protheus-GPE-Como-Criar-Per%C3%ADodos-Automaticamente-pela-Rotina-Gera%C3%A7%C3%A3o-Per%C3%ADodo-Padr%C3%A3o)  
[RH - Linha Protheus - GPE - Como criar processo e período de cálculo diferente do padrão já existente no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045247114-RH-Linha-Protheus-GPE-Como-criar-processo-e-per%C3%ADodo-de-c%C3%A1lculo-diferente-do-padr%C3%A3o-j%C3%A1-existente-no-sistema)
