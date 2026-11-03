---
article_id: 360019196651
category: MDFe - Manifesto de Carga
content_hash: ef5939089e3fdbb8007909d74cad5ebf91b7bd0179dbe209931f43683a05564c
fetched_at: '2026-06-28T22:40:08.328849+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - Rejeição:
  212 Data/hora de emissão MDF-e posterior a data/hora de recebimento'
type: support-article
updated_at: '2025-06-17T18:49:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019196651-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Rejei%C3%A7%C3%A3o-212-Data-hora-de-emiss%C3%A3o-MDF-e-posterior-a-data-hora-de-recebimento
---

**Dúvida**Como solucionar a rejeição abaixo ?

212 Data/hora de emissão MDF-e posterior a data/hora de recebimento  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

**Na rotina de transmissão de MDFe: Acesse como Administrador > Ações Relacionadas ou Outras ações > Parâmetros > Horário de Verão = SIM Ou NÃO (de acordo com a UF da filial).**

![](http://tdn.totvs.com/download/attachments/307823452/image2017-10-16_9-18-53.png?version=1&modificationDate=1508153078000&api=v2)

**+ Administrador: salvar as configurações (apenas administrador tem acesso).**

* Após alterar na rotina conferir a gravação na tabela SPED000 do TSS nos parametros:

MV\_HRVMDFE - 1 = Está em horário de verão; 2 = Não está em horário de verão

MV\_HRMDFE  - 1 = Fernando de Noronha; 2 = Brasília; 3 = Manaus

* Acessar no configurador (de acordo com Estado do servidor da empresa):

MV\_HVERAO (X6\_VAR)  
Tipo Lógico (X6\_TIPO)

Define se o local físico do servidor está em Horário de Verão que o **ERP** está instalado.  
Valor Padrão .F.(sem) ou .T.(com)

* No ini do TSS deverá incluir esse parâmetro se não houver de acordo com o horário de verão que o mesmo está instalado: SPED\_HVERAO=1(horario de verao = SIM) ou = 2 (horario de verao = NAO).

Exemplo:

[Environment]  
SPED\_HVERAO=1

OBS: Após alterar o ini do TSS o mesmo deverá ser reiniciado
