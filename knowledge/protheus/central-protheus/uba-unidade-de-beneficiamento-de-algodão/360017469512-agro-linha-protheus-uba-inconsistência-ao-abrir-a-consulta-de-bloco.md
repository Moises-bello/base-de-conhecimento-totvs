---
article_id: 360017469512
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: eee0be0cb02a5674b4aa5e5071ea0a1054f65143f0c5e0d6162a1c160534eacc
fetched_at: '2026-06-28T22:45:35.612666+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Inconsistência ao abrir a consulta de bloco
type: support-article
updated_at: '2025-06-18T20:04:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017469512-Agro-Linha-Protheus-UBA-Inconsist%C3%AAncia-ao-abrir-a-consulta-de-bloco
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21881422894359)**Tempo aproximado para leitura: **00:00:55 min  
  
Ocorrência**No módulo **Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão**, ao acessar a rotina **UBAC008 -****Consulta de Bloco**, ocorre o erro **Alias does not exist: on UBAC0082P**.  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - Versão 12  
  
 **Causa**Este incidente ocorre porque o conteúdo da coluna **X1\_VALID**, pergunta de ordem **4**, referente ao arquivo **SX1**, da rotina **UBAC008**, está inconsistente.  
  
 **Solução**Para solucionar essa ocorrência realize os seguintes passos:

**1.** Acesse o arquivo **SX1**, via **APSDU**, e filtre pela rotina **UBAC008**;

**2.** Procure pela pergunta de ordem **4 - Fazenda**;

**3.** Navegue até a coluna **X1\_VALID** e insira o conteúdo: **VAZIO()  .OR. EXISTCPO("NN2",mv\_par02+mv\_par03,3)**.
