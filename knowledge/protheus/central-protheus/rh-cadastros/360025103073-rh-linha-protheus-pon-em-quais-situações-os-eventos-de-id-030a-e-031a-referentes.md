---
article_id: 360025103073
category: RH - Cadastros
content_hash: 2c8ad6fd4bb3563982e0905186fb35ac7d88efe343391493d0db362a9bc5a120
fetched_at: '2026-06-28T22:44:53.142265+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH – Linha Protheus – PON – Em quais situações os eventos de ID 030A e 031A,
  referentes ao intervalo, são apontados para o funcionário?
type: support-article
updated_at: '2025-12-22T13:57:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103073-RH-Linha-Protheus-PON-Em-quais-situa%C3%A7%C3%B5es-os-eventos-de-ID-030A-e-031A-referentes-ao-intervalo-s%C3%A3o-apontados-para-o-funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29772389884567) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Em quais situações os eventos de ID 030A e 031A, referentes ao intervalo, são apontados para o funcionário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Será gerado o ID 030A ou 031A nos apontamentos, quando o campo **Saída Interv** na Tabela de Horário Padrão estiver com **Sim.**   
  
Primeiramente cadastre o evento atribuindo ao **ID 030A-HORAS DE INTERVALO** ou **031A-HORAS DE INTERVALO NOTURNO.**  
  
Veja a documentação sobre cadastro de evento: [RH - Linha Protheus - PON - Como utilizar o cadastro de evento do ponto eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407450836887-RH-Linha-Protheus-PON-Como-utilizar-o-cadastro-de-evento-do-ponto-eletr%C3%B4nico)  
  
Exemplo do cadastro de evento:  
**Obs.:** O código para folha será informado somente se quiser que suba os eventos apontados aos resultados para integração com a folha, ok. No exemplo o evento só será informativo no ponto das horas apontadas de intervalo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29772389891223)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29772389895959)  
  
  
No exemplo abaixo o horário misto iniciando no noturno das 22:00 e finalizando no diurno as 07:30, com intervalo das 01:30 as 02:30. Neste caso a **1a Saída** trata-se de inicio do intervalo e com isso o campo **1a S.Interv** deverá ficar com Sim para ser considerado intervalo. Exemplo prático no print abaixo:  
  
Para configuração acessar a rotina **Atualizações > Cadastro do Ponto > Tabela de Horário Padrão**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29772389900183)

Em **Atualizações > Cadastro do Ponto > Regra de Apontamento,** os campos **Pg. Hrs. Norm.** e **Hr. Norm.Fol** estiver marcado com Sim e **Pg. Intervalo** estiver marcado com os intervalos à serem pagos. Exemplo: No campo **Pg. Intervalo** selecione a posição do **intervalo** que deseja que seja gerado as **horas de intervalo** conforme a **tabela de horário padrão.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29772389905047)**  
  
  
Após utilizado este processo ao realizar o apontamento, o sistema apontará de acordo com o evento atribuído ao cadastro do **ID 031A-HORAS DE INTERVALO NOTURNO.** Neste caso, é o **evento de horas noturnas,** veja exemplo:  
  
Em **Atualizações > Lançamentos > Integrados**, filtrei o funcionário atribuído a tabela de horário e regra configurada e veja como ficou os apontamentos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29772389910039)

**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
