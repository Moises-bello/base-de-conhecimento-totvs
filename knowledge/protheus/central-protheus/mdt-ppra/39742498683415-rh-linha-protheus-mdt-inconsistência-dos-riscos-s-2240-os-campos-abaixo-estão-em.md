---
article_id: 39742498683415
category: MDT - PPRA
content_hash: 97cb4eeb85fbc2e7703932d4145e8345d2c8fdf89e19edf9da4c7e74dccdc595
fetched_at: '2026-06-28T22:44:27.337315+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: 'RH - Linha Protheus - MDT - Inconsistência dos riscos (S-2240): Os campos
  abaixo estão em branco ou possuem inconsistência com relação ao formato padrão do
  esocial'
type: support-article
updated_at: '2026-04-14T17:19:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39742498683415-RH-Linha-Protheus-MDT-Inconsist%C3%AAncia-dos-riscos-S-2240-Os-campos-abaixo-est%C3%A3o-em-branco-ou-possuem-inconsist%C3%AAncia-com-rela%C3%A7%C3%A3o-ao-formato-padr%C3%A3o-do-esocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39742472537111) Tempo aproximado para leitura: **02:30:00 min**  
  
**Ocorrência**  
Ao executar qualquer rotina que gere o evento S-2240 no módulo de Medicina e Segurança do Trabalho, o sistema apresenta o seguinte erro:

Inconsistência dos riscos (S-2240): Os campos abaixo estão em branco ou apresentam inconsistências em relação ao formato padrão do eSocial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39742472538263)  
**Ambiente**  
TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**  
Este erro está relacionado às datas utilizadas para a geração do evento S-2240.  
  
**Solução**  
1. Caso a rotina utilizada inclua datas, certifique-se de que a data informada seja igual ou posterior à data de admissão do colaborador.

2. Verifique se no módulo do TAF existe um evento S-2240 com a data de início da exposição igual à data informada no log. No exemplo citado, a data é 01/12/2026.

3. A data base do sistema também deve ser validada. A data base informada precisa ser igual ou posterior à data de admissão do colaborador.

4. O parâmetro MV\_NG2DTES deve estar configurado para uma data igual ou anterior à data de admissão do colaborador.

Saiba mais  
[Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
