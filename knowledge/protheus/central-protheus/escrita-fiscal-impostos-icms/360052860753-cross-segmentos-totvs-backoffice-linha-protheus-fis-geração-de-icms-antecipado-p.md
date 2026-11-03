---
article_id: 360052860753
category: Escrita Fiscal - Impostos - ICMS
content_hash: e270ef50e102052f378b374efee1f4c4ef9640f63b8a37598d43b0e3e6357260
fetched_at: '2026-06-28T22:39:25.935284+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Geração de ICMS Antecipado
  por documento de entrada
type: support-article
updated_at: '2021-07-28T14:06:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052860753-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gera%C3%A7%C3%A3o-de-ICMS-Antecipado-por-documento-de-entrada
---

**Dúvida**Como gerar **Titulo**, **Guia** de **ICMS Antecipado**?  
   
 **Ambiente**Microsiga Protheus – Fiscal – A partir da versão 11.80  
   
**Solução**Para gerar **Titulo**, **Guia** de **ICMS Antecipado**, realize os seguintes passos;

1. Na rotina **MATA103** "documento de entrada", acesse o grupo de perguntas via **F12**, configure as perguntas abaixo;

**Pergunta 18 –** **Gera Titulo ICMS Antecipado** = Sim;

**Pergunta 19 – Guia Recolhimento ICMS Atec.** = Sim;

**Pergunta 26 – Gera ICMS Antecip Separado** = Sim;

2. No lançamento do documento de entrada, deverá ser usado o **TES** que possua as seguintes configurações;

**Est Var/Atac (F4\_VARATAC):** 1= Varejista, 2 = Atacadista;

**Antecip.ICMS (F4\_ANTICMS):** = Sim;

3. Verificar a configuração do parâmetro abaixo caso queira que a **Guia de Recolhimento** seja apresentada na tela, ao confirmar a inclusão do documento;

**MV\_GNRENF** - Habilitar o parâmetro para que não seja gerada a tela **GNRE** quando a opção **Guia** de **Recolhimento** = Sim;
