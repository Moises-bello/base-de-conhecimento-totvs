---
article_id: 360055460753
category: RH - Períodos de Apontamento
content_hash: 4eb199dd9733fa82f6a0581e37e14cb9de368fddf14995ab24c458d870047ab4
fetched_at: '2026-06-28T22:44:45.088281+00:00'
product: protheus
section_id: 32419304439959
source: central-protheus
title: RH - Linha Protheus - PON  - Como evitar a gravação de marcações com período
  de apontamento incorreto
type: support-article
updated_at: '2025-12-02T17:16:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055460753-RH-Linha-Protheus-PON-Como-evitar-a-grava%C3%A7%C3%A3o-de-marca%C3%A7%C3%B5es-com-per%C3%ADodo-de-apontamento-incorreto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34204732176407)****Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Ao executar a leitura/apontamentos o sistema busca **marcações do ultimo dia do período passado para o primeiro dia do período atual**, deixando as marcações com período de apontamento incorreto. **Como evitar a gravação de marcações com período de apontamento incorreto**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
**1.** Na [**Tabela de Horário Padrão**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o), os dias **Compensados**, **Não Trabalhados** e **DSR** devem conter horários preenchidos, para que o sistema possua um horário como base caso ocorram marcações nesses dias:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4968183890839)  
  
**2.** Os campos de [**Limite Inferior e Superior**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002754861-RH-Linha-Protheus-PON-Funcionalidades-dos-campos-de-Limite-inferior-e-Limite-superior-na-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o) somados com a carga horária do dia não devem ultrapassar 23h59, pois com base nos limites o sistema irá reconhecer marcações correspondentes ao dia correto:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4968233003287)  
  
**3.** No momento em que for realizar a Leitura/Apontamento, a **data base do sistema** sempre deve estar no **último dia do Período de Apontamento:**   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32038805688087)

Temos os parâmetros **MV\_GETDIAA** e **MV\_GETDIAP** que controlam os **limites adicionais** de datas estabelecidas na **leitura/apontamento**. No caso de **turnos noturnos,** o conteúdo de ambos deve ser de no **mínimo 1** e no **máximo 7**.  
  
**Exemplo:**  
Se na Leitura/Apontamento for informada uma **data final** de leitura no dia **20**, porém, o funcionário finalizou o expediente apenas no dia **21**, o **MV\_GETDIAAP** precisa estar no **mínimo** com **conteúdo 1**, para que o sistema consiga **validar as marcações após às 00h do dia 21** e entender como **término da jornada iniciada no dia 20**.  
  
**Saiba Mais**  
[**Manual do Ponto Eletrônico**](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[**Pacote de Expedição Contínua Acumulado de RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[**RH - Linha Protheus - PON - Período do ponto desconfigurado como ajustar os parâmetros MV\_PAPONTA e MV\_PONMES**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015809548-MP-PON-Per%C3%ADodo-de-apontamento-desconfigurado-Como-configurar-MV-PAPONTA-e-MV-PONMES?source=search)  
[RH - Linha Protheus - PON - Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-MP-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o-?source=search)
