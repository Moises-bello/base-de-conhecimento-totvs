---
article_id: 360025738254
category: Cálculo
content_hash: ab7f89d8781f9d640d80ba12d8036ec28837059ddbad243d4a828fdd716137e3
fetched_at: '2026-06-28T22:46:29.210344+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Calcular faltas por suspensão em evento separado do evento
  de faltas
type: support-article
updated_at: '2025-09-22T15:06:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025738254-RH-RM-PTO-Calcular-faltas-por-suspens%C3%A3o-em-evento-separado-do-evento-de-faltas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17200623505815) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Como calcular as faltas por suspensão em evento separado do evento de faltas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 11.80  
  
**Solução**Para calcular as faltas por suspensão em evento separado do evento de faltas, siga os passos abaixo.

1. Acesse o módulo de **Automação de Ponto**, na guia **Configurações** e crie uma nova ocorrência customizada em **Tipos de Ocorrência**.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35112168022039)
2. Crie um evento de código de cálculo **0043** no menu **Eventos** e associe a ocorrência customizada que foi criada a este evento.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35112161516439)
3. No sindicato associado ao funcionário, insira o evento de código de cálculo 0043 criado no passo anterior.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35112168029335)
4. Para os dias da falta por suspensão do funcionário, é necessário realizar uma modificação de ocorrências, passando a ocorrência do tipo **F - Falta** para o tipo customizado que foi criado e após realize o recálculo e o evento será calculado no movimento do funcionário.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35112161524759)

**Saiba Mais**Para mais informações sobre os procedimentos realizados acima, consulte os seguintes artigos:  
[RH - RM - PTO - Modificação de ocorrência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000929287)  
[RH - RM - PTO - Cadastrar eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025095672-TOTVS-RH-Linha-RM-PTO-Como-cadastrar-eventos)

[RH - RM - PTO - Cadastrar eventos por tipo de ocorrência (código de cálculo 0043)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019943891-RH-RM-PTO-Cadastrar-eventos-por-tipo-de-ocorr%C3%AAncia-c%C3%B3digo-de-c%C3%A1lculo-0043)
