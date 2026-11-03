---
article_id: 360015767412
category: RH - Banco De Horas
content_hash: c6c79a0007f77e0cfca44e00a6a7e38baa0faf7cca5437813f516a63098fcc97
fetched_at: '2026-06-28T22:44:54.230711+00:00'
product: protheus
section_id: 32405029751063
source: central-protheus
title: RH - Linha Protheus - PON - Como realizar a apuração parcial de um evento,
  levando parte para Folha e parte para Banco de Horas no mesmo dia de apontamento
type: support-article
updated_at: '2025-11-17T11:54:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015767412-RH-Linha-Protheus-PON-Como-realizar-a-apura%C3%A7%C3%A3o-parcial-de-um-evento-levando-parte-para-Folha-e-parte-para-Banco-de-Horas-no-mesmo-dia-de-apontamento
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34211467384983) Tempo aproximado para leitura: 00:01:30 min******Dúvida**Como realizar a apuração parcial de um evento, levando parte para Folha e parte para Banco de Horas no mesmo dia de apontamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**A apuração parcial do evento será configurada pelo cadastro de cada evento que será apontado.  
Esta configuração é realizada no **cadastro de evento** e, mais especificamente, na aba **Banco de Horas**.  
  
Para realizar o cadastro de evento ou a alteração de um evento já criado, acesse o módulo **16-SIGAPON**, em **Atualizações → Cadastro do ponto → Eventos**. Crie um novo evento ou altere algum já existente.  
Abaixo, seguem dois prints de como deverão estar cadastrados cada evento para termos a apuração parcial:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31986871329559)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31986871332119)  
  
A configuração acima fará com que o sistema apure metade do evento apontado — no exemplo, é o de **Atraso** — para Folha e metade para o Banco de Horas.  
Todos os eventos que desejarem ter essa configuração deverão ser cadastrados desta forma.  
  
Ao efetuar a **Leitura e Apontamentos**, em **Miscelânea → Cálculos → Leitura/Apontamento**, segue como ficaram os apontamentos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31986856347031)  
  
Ao realizar o **Cálculo Mensal**, em **Miscelanea - Cálculos - Calculo Mensal**, metade da apuração foi para Banco de Horas e a outra metade para Folha de Pagamento.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31986871334295)  
  
**Lançamento de Banco de Horas:**  
Veja que foi apurado metade de cada evento para o **Banco de Horas**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31986856352919)  
  
**Lançamentos de Resultados:**  
Da mesma forma, foi apurado metade de cada evento nos **Resultados** para integrar com a **folha de pagamento**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31986871344279)  
  
**Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373) **[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)**[RH - Linha Protheus - PON - Como utilizar o cadastro de evento do ponto eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407450836887-RH-Linha-Protheus-PON-Como-utilizar-o-cadastro-de-evento-do-ponto-eletr%C3%B4nico)[RH - Linha Protheus - PON - Como fazer e qual a finalidade do Cálculo Mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051550453-RH-Linha-Protheus-PON-Como-fazer-e-qual-a-finalidade-do-C%C3%A1lculo-Mensal)
