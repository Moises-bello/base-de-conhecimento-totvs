---
article_id: 360051337553
category: RH - Rescisão
content_hash: a10a1fa26bd157eb42a6d8f2411ed2826eac2c900ffcd7dbe0be9383ad04d599
fetched_at: '2026-06-28T22:43:48.316562+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - Como proporcionalizar o DSR no cálculo da rescisão, com
  data de admissão e demissão no mesmo mês
type: support-article
updated_at: '2025-06-12T12:33:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051337553-RH-Linha-Protheus-Como-proporcionalizar-o-DSR-no-c%C3%A1lculo-da-rescis%C3%A3o-com-data-de-admiss%C3%A3o-e-demiss%C3%A3o-no-mesmo-m%C3%AAs
---

**Dúvida**Como proporcionalizar o DSR no cálculo da rescisão, com data de admissão e demissão no mesmo mês?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**O sistema considera dois mnemônicos para cálculo de DSR na rescisão, o **P\_CPROPDSR**  e o **P\_LPROPDSR**, temos as opções abaixo de configuração:

**P\_CPROPDSR** - PROPORCIONALIZA DSR HE:0=NAO/1-ADM /2-DEM /3-AFAST /4-FÉRIAS.  
**P\_LPROPDSR** - PROPORCIONALIZA DSR DE HE NA ADMISSAO, DEMISSAO E AFAST.

Configure, conforme abaixo para que o sistema proporcionalize o DSR no cálculo da rescisão:  
**P\_CPROPDSR** - "12"  
**P\_LPROPDSR** - .T.   
  
**Observação.:** O sistema só acata a proporcionalização do DSR na rescisão se o cadastro de calendário do período for analítico (parâmetro MV\_TPCALEN=1), caso contrário o sistema não tem de onde buscar um DSR proporcional uma vez que não há o calendário analítico.
