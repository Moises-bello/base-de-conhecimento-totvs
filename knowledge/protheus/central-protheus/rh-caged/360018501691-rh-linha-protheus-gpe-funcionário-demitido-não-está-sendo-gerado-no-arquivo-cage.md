---
article_id: 360018501691
category: RH - CAGED
content_hash: fcfa795d286b2e2f70a9183d37ea9144e4d4564f121139e27aff7b513daf6101
fetched_at: '2026-06-28T22:43:33.029903+00:00'
product: protheus
section_id: 360010781674
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionário demitido não está sendo gerado no Arquivo
  CAGED
type: support-article
updated_at: '2025-08-27T19:59:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018501691-RH-Linha-Protheus-GPE-Funcion%C3%A1rio-demitido-n%C3%A3o-est%C3%A1-sendo-gerado-no-Arquivo-CAGED
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29401189147415) Tempo aproximado para leitura: 00:03:00 min***

**Ocorrência**Funcionário demitido não está sendo gerado no Arquivo CAGED.   
Nos parâmetros, se definirmos somente a matrícula em questão, é gerado o alerta: "Não foram incluídos registros no arquivo do Caged".  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Esse incidente ocorre, pois há uma incompatibilidade entre os campos **RA\_VIN.EMP. RAIS**  e  **RA\_RESCRAI.** Os códigos devem ser compatíveis entre si e devem existir no Manual da RAIS.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

Verificar os campos no cadastro do funcionário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013805352)

**Obs.** No campo **VIN.EMP.RAIS** estará o código do tipo de vínculo empregatício ou relação de emprego, que foi definido na admissão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013805772)

No campo **Cod.Resc. RAIS** estará vinculado o tipo de rescisão de acordo com o que foi escolhido no momento da RESCISÃO. Se estiverem incompatíveis, não será gerado no **CAGED.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013805912)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013805912)  
  
**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)

[MP - GPE0860 - Caged Acerto](http://tdn.totvs.com/display/PROT/MP+-+GPE0860+-+Caged+Acerto)

Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento:   
<https://www.youtube.com/watch?v=T7b4zMlphTI>
