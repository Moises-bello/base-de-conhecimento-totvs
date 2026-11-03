---
article_id: 360023201671
category: MDFe - Manifesto de Carga
content_hash: d7cd11474b30139f0648c2bab223032edc947af41dd99ef300c6fe9499bd29a7
fetched_at: '2026-06-28T22:40:08.138746+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE -  634 Rejeição:
  A data do evento não pode ser menor que a data de emissão do MDF-e'
type: support-article
updated_at: '2025-06-17T18:43:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023201671-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-634-Rejei%C3%A7%C3%A3o-A-data-do-evento-n%C3%A3o-pode-ser-menor-que-a-data-de-emiss%C3%A3o-do-MDF-e
---

**Dúvida**Como corrigir a rejeição 634 : A data do evento não pode ser menor que a data de emissão do MDF-e  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**1 - Clique em **Outras ações -> Parâmetros;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410708308631)

2- Configure **Horário de Verão -> Sim ou Não e Horário de acordo com a UF** de transmissão de nota;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410700668695)

3- **+ Administrador: salvar as configurações** (apenas administrador tem acesso);

4- No configurador altere o **parâmetro conforme abaixo MV\_HVERAO;**

.F. = Sem horário de Verão

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410700775575)

.T. = Com horário de Verão

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410708475287)

5- No **appserver.ini do TSS** deverá incluir esse parâmetro se não houver de acordo com o horário de verão que o mesmo está instalado: **SPED\_HVERAO=1(horario de verao = SIM) ou = 2 (horario de verao = NAO).**

* **Exemplo:**

[Environment]  
SPED\_HVERAO=1

OBS: Após alterar o ini do TSS o mesmo deverá ser reiniciado.

6- Após isso, exclua o **MDF-e e gere novamente.**
