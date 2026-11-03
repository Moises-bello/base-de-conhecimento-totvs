---
article_id: 6908969616791
category: Materiais - Compras (SIGACOM)
content_hash: 2e5f3c5e5e9a22126d0d5a66ae7d5fc1f651099d5b0d3d21da13374ce10d5899
fetched_at: '2026-06-28T22:41:11.568429+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Ao lançar uma
  Nota com TES que Atualize Ativo, é gerada a mensagem "Gerando fichas de Ativo Imobilizado" '
type: support-article
updated_at: '2024-04-15T15:04:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6908969616791-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Ao-lan%C3%A7ar-uma-Nota-com-TES-que-Atualize-Ativo-%C3%A9-gerada-a-mensagem-Gerando-fichas-de-Ativo-Imobilizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22814492541079) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao lançar uma Nota com TES que Atualize Ativo, é gerada a mensagem Gerando fichas de Ativo Imobilizado

![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6908650206359)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12

**Solução**Verifique se no cadastro do TES o campo F4\_BENSATF está igual a Sim, em caso positivo quando for lançado um item com quantidade 1000, por exemlplo na Nota de Entrada, serão gerados 1000 itens com quantidade igual a 1 no módulo do Ativo Fixo ( tabelas SN1 e SN3 ), e a mensagem Gerando fichas de Ativo Imobilizado será apresentada, até que todos os itens sejam gerados.

![ativo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/6908805737367)

Caso não se deseje essa geração de Itens separados, então deixe o campo F4\_BENSATF da TES igual a Não, assim a Nota será inclusa gerando apenas 1 item com quantidade igual a 1000.

**Obs**: Esse parâmetro/campo da TES só tem efeito se o campo F4\_ATUATF estiver igual a Sim.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [MV\_A12DTHR para inclusão de ativos com desmembramento](https://tdn.totvs.com/pages/releaseview.action?pageId=665275186)
