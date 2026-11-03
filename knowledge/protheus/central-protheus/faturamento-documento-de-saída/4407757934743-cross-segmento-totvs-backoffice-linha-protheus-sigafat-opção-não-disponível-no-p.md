---
article_id: 4407757934743
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 19af1a2b1bf4b0471ed77119b33ce9320011a449ee0f107f213c8cb50496d3f1
fetched_at: '2026-06-28T22:38:43.950885+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Opção não disponível
  no Protheus Função fa050penc
type: support-article
updated_at: '2021-09-03T14:48:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407757934743-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-fa050penc
---

![time.png](https://totvssuporte.zendesk.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao tentar utilizar excluir uma nota de saída, é informado o help : **Opção não disponível no Protheus Função fa050penc**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Causa**

O erro ocorre por a rotina que está requisitando a função **FA050PENC** está desatualizada.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do pacote de expedição contínua do Financeiro, conforme sua release: **[SIGAFIN](https://tdn.totvs.com/x/HrCmHw)**

2. Aplique o pacote de atualização via VS-Code no ambiente.  
3. Reinicie o Smartclient e efetue o procedimento novamente.

**Observação: O procedimento de atualização deve ser efetuado por um analista com conhecimento de Vs-code, em caso dúvida procure o atendimento da equipe de ADVPL para orientação.**
