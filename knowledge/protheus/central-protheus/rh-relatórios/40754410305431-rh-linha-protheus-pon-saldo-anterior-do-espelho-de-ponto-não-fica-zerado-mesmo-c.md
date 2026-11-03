---
article_id: 40754410305431
category: RH - Relatórios
content_hash: 6a9e20813f3766a15b72309a35c64423ce6a36eb2e0a6075390b24e7e1407e3e
fetched_at: '2026-06-28T22:44:43.615716+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Saldo anterior do Espelho de Ponto não fica zerado
  mesmo com todo o Banco de Horas baixado e zerado
type: support-article
updated_at: '2026-05-27T18:41:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40754410305431-RH-Linha-Protheus-PON-Saldo-anterior-do-Espelho-de-Ponto-n%C3%A3o-fica-zerado-mesmo-com-todo-o-Banco-de-Horas-baixado-e-zerado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40754371544727) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Por qual motivo o **Saldo anterior** do **Espelho de Ponto** **não fica zerado** mesmo com todo o **Banco de Horas baixado** e zerado?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
  
**Solução**  
O espelho de ponto é o reflexo do período vigente.   
Neste caso, o saldo anterior apresentado no espelho de ponto gerado do período de apontamento com data em 21/04 a 20/05, refere-se ao período de 21/03 à 20/04, se para este período o banco de horas ainda estava aberto, neste espelho de ponto permanecerá demonstrando o saldo.  
 O saldo só será zerado a partir do período fechado, se foi o período de 21/04 a 20/05, só refletirá no saldo anterior referente ao espelho de ponto do período 21/05 a 20/06. Por este motivo não se deve validar fechamento do banco de horas apenas como base o espelho de ponto e sim deve conferir pelos relatórios de banco de horas e extrato do BH.   
  
Veja mais abaixo sobre os relatórios:  
[RH - Linha Protheus - PON - Como funciona o Relatório de Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015845991-RH-Linha-Protheus-PON-Como-funciona-o-Relat%C3%B3rio-de-Banco-de-Horas?source=search)  
[RH - Linha Protheus - PON - Como exibir as horas valorizadas no extrato de banco de horas ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028737751-RH-Linha-Protheus-PON-Como-exibir-as-horas-valorizadas-no-extrato-de-banco-de-horas-?source=search)

**Saiba mais**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
