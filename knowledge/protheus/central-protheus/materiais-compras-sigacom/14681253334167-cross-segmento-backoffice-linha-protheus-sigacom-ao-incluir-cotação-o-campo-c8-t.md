---
article_id: 14681253334167
category: Materiais - Compras (SIGACOM)
content_hash: 1e1a7e4bfc6648c7d330d6c942aa80958a99216805b90107e44daccf5e060e9b
fetched_at: '2026-06-28T22:41:10.496533+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Ao Incluir Cotação
  o campo C8_TES não é preenchido
type: support-article
updated_at: '2023-05-18T15:28:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14681253334167-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Ao-Incluir-Cota%C3%A7%C3%A3o-o-campo-C8-TES-n%C3%A3o-%C3%A9-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00** **Dúvida**

Ao incluir uma Cotação o campo C8\_TES não é preenchido.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Compras - Versão 12

**Solução**

Para que o conteúdo do campo B1\_TE seja gravado na cotação, será necessário realizar a seguinte configuração:

1. Informar uma TES no campo B1\_TE;

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14680820557463)

2. Gerar Cotação;

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14681038984599)

3. Em Atualiza Cotação, Pressione "F12" rotina "Atualizar Cotações" (MATA150) e habilite a pergunta: "Sugere TE Padrão" para "Sim";

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14681091532695)

4. Ao realizar essa configuração o conteúdo do campo B1\_TE será apresentando na tela de "Atualizar Cotações" para ser gravado.;

![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14681140849431)

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
