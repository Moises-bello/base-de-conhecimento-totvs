---
article_id: 360004970391
category: RH - Cadastros
content_hash: 4340bd4f0ae8458ae1c71b30e806e43c9707950dada87d0ee4595014e499df29
fetched_at: '2026-06-28T22:44:52.850061+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como efetuar o desconto do DSR no Ponto Eletrônico
  quando existe Falta, Atraso ou Saída Antecipada
type: support-article
updated_at: '2026-02-03T17:56:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004970391-RH-Linha-Protheus-PON-Como-efetuar-o-desconto-do-DSR-no-Ponto-Eletr%C3%B4nico-quando-existe-Falta-Atraso-ou-Sa%C3%ADda-Antecipada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31780455710743)** **Tempo aproximado para leitura:****00:01:30 min**  
  
**Dúvida**  
Como efetuar o desconto do DSR no Ponto Eletrônico quando existe Falta, Atraso ou Saída Antecipada?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O objetivo do **desconto de DSR** (Descanso Semanal Remunerado) é descontar as horas referentes aos dias de **DSR** e **Feriados** para funcionários que **não cumpriram integralmente a carga horária** estabelecida para o período de apuração.  
  
Para a realização desse desconto, devem ser realizados alguns procedimentos:  
  
1 - Verifique via **Configurador** (SIGACFG), os **parâmetros** que controlam o desconto de DSR [nesta documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018605091-RH-Linha-Protheus-PON-Par%C3%A2metros-que-controlam-o-DSR-no-m%C3%B3dulo-SIGAPON)   
Os parâmetros são configurações **obrigatórias** e devem estar preenchidos de acordo com a regra necessária para atender a necessidade de sua empresa.   
  
2 - No cadastro dos **Eventos** que terão **desconto de DSR**, é necessário deixar o campo **Desc. DSR** como **Sim**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100820733)  
  
3 - Na **Regra de Apontamento**, aba de **Apontamento,** se o campo **Desconta DSR** estiver como **SIM**, o evento utilizado para prosseguir com o desconto será o que possui o **ID de Ponto 018A.** Se estiver como **NÃO**, o **ID será o 017N**. Lembrando que este campo **não determina** se haverá ou não desconto e sim qual evento será apontado.  
O cadastro do evento que será responsável pelo desconto do DSR deve estar conforme exemplo abaixo:![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098584974)  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100821673)  
  
Na **Regra de Apontamento**, aba de **Apuração**, definimos a **periodicidade** da Apuração. Por padrão, deixamos como **Semanal** (um DSR por semana):  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098584154)  
  
Na aba de **Tolerância** da **Regra de Apontamento**, por padrão, deixamos o campo **Nro. Oc. N. DSR** em **branco**. Este campo serve como **tolerância para descontar ou não o DSR**, logo, se estiver preenchido com 1 por exemplo, só será descontado do funcionário caso ele tenha ao menos 2 descontos de DSR no período.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11987429396503)  
  
5 - Na rotina de **Arredondamentos**, deve ser cadastrado o arredondamento de **DSR**. A quantidade de horas a ser descontada é definida pelo cliente:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100821353)  
  
6 - Após ter ajustado todos os cadastros e ter feito o apontamento dos eventos, deve ser processado o **Cálculo Mensal** do período, esta rotina será a responsável em fazer a análise dos apontamentos gerados e quais deles possuem configuração para desconto do DSR em Folha. Ao término do processamento, as verbas serão geradas na rotina de **Lançamentos - Resultados** para posterior **integração com a Folha**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31780460123671)  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
