---
article_id: 4412575742871
category: Materiais - Compras (SIGACOM)
content_hash: c63655ead2118db06fab83fa40d784d964a98c7dd8562f2641115fa8eecfcdab
fetched_at: '2026-06-28T22:41:11.794588+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Retorno
  de Venda com a mesma taxa de Faturamento
type: support-article
updated_at: '2024-12-11T13:34:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412575742871-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Compras-Retorno-de-Venda-com-a-mesma-taxa-de-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28443739070231) Tempo aproximado para leitura: **00:04 min** **Dúvida**

Como realizar o retorno de venda com a mesma taxa de Faturamento?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Versão 12

**Solução**

Foi realizado tratamento no programa de geração de notas fiscais de saída para gravar a informação da pergunta 'Dt. Ref. Conversão' no campo F2\_DTTXREF, e realizado tratamento no programa de geração de notas fiscais de entrada para checar se este campo está preenchido e retornar a taxa da moeda utilizando esta data no retorno de uma venda, quando o parâmetro MV\_MOEDTIT estiver configurado com S.

Para as notas que já estão faturadas, onde o campo F2\_DTTXREF estará em branco, foi realizado tratamento para habilitar a edição do campo Taxa da Moeda no documento de entrada de devolução, para que seja possível informar a taxa de devolução correta. O campo somente ficará habilitado nas notas de devolução quando o parâmetro MV\_TXMOENC estiver configurado com conteúdo 1, e quando o valor faturado constante no campo F2\_VALFAT, estiver diferente da duplicata que foi calculada pelo sistema com a taxa encontrada.

***Obs**:*

O checkbox "Taxa Negociada" que aparece na aba de Duplicatas é somente informativo, não sendo gravado em nenhum campo do sistema.  
Ele aparecerá marcado para informar que a taxa da moeda difere da taxa cadastrada para o dia corrente.  
A taxa somente será considerada como negociada se diferir da taxa do dia da emissão do título (E2\_EMISSAO). Se a taxa do dia estiver zerada, a taxa do título não será considerada como negociada.  
Não é considerado para notas de devolução.

Mais infomrações: [Conversão Moeda Devolução de Venda](https://tdn.totvs.com/x/V0MZE)

***Saiba Mais :***

[Conversão Moeda Devolução de Venda](https://tdn.totvs.com/x/V0MZE)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
