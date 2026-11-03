---
article_id: 4410196516887
category: Materiais - Compras (SIGACOM)
content_hash: 80c9a63cb2531275110edfc1bd258b0e77dfc438e3d57e2b8945ba04d65c7e47
fetched_at: '2026-06-28T22:41:17.615586+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Erro ao aplicar patch
  no VS Code: " Duplicated function ISPJOUPF (found in OMSM011.PRW) "'
type: support-article
updated_at: '2022-05-16T22:57:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410196516887-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Erro-ao-aplicar-patch-no-VS-Code-Duplicated-function-ISPJOUPF-found-in-OMSM011-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ao realizar a aplicação de um patch de Issue no VS Code ocorre o erro / mensagem:

*Patch (xnptacbd\_tttp120\_lg.ptm) could not be applied.*  
*Server returned: Duplicated function ISPJOUPF() on GFEM011.PRW line:2737. found in OMSM011.PRW*

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões

**Solução**Para informação, houve uma troca de algumas funções em fontes. E para corrigir essa mensagem de duplicidade, deve-se primeiramente realizar a aplicação do pacote do módulo SIGAGFE que consta no link abaixo:

[Pacote de Atualização - TOTVS Logística Frete Embarcador (SIGAGFE) - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=547876421)

E posteriormente realizar a aplicação do pacote que se deseja aplicar.

***Obs.:***

Mesmo que no ambiente em questão, não seja utilizado o módulo de Frete Embarcador (SIGAGFE), para a correção da mensagem de função duplicada deve ser aplicado o pacote referido para atualização dos fontes no RPO.

***Saiba Mais :***

[Pacote de Atualização - TOTVS Logística Frete Embarcador (SIGAGFE) - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=547876421)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
