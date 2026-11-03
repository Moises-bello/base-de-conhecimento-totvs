---
article_id: 8102582437655
category: RH - Definições de Cálculo
content_hash: ed924394b8226e37dc635e3051b56fa788b5304d89def04848b0cb9f7865dc0e
fetched_at: '2026-06-28T22:43:22.483699+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Mnemônico P_MULTV necessário estar ativo para cálculos
type: support-article
updated_at: '2025-09-12T16:55:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8102582437655-RH-Linha-Protheus-GPE-Mnem%C3%B4nico-P-MULTV-necess%C3%A1rio-estar-ativo-para-c%C3%A1lculos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32700187662103) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No módulo gestão de pessoal, ao tentar realizar alguns cálculos, é gerado o log abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8101595812119)  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.27  
  
**Causa**Esse incidente ocorre pois o mnemônico P\_MULTV no sistema está desativado.  
  
**Solução**A partir da versão 12.1.27 verificamos que ao deixar o mnemônico desativado estava ocorrendo erro ao enviar eventos para o eSocial. Para solucionar essa ocorrência, alteraram a validação nos fontes, sendo necessário ativar o Mnemônico P\_MULTV para os cálculos.

Para ativar, realize o procedimento abaixo:  
1. Acesse o módulo SIGAGPE - Gestão de pessoal;

2.  Acesse **Atualizações - Definição de Cálculo - Mnemônico:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8101827015959)  
3. Pesquise o **Mnemônico P\_MULTV:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8101834783383)

4. Altere o conteúdo do Mnemônico para **.T.** e clique em Confirmar:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8101890423319)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8101950172695)

5. Após a ativação do Mnemônico P\_MULTV, realize os cálculos, abaixo exemplo de férias:![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8102324196631)

**Saiba Mais**[Manual do Cálculo de Múltiplos Vínculos](https://tdn.totvs.com/pages/viewpage.action?pageId=552575179)
