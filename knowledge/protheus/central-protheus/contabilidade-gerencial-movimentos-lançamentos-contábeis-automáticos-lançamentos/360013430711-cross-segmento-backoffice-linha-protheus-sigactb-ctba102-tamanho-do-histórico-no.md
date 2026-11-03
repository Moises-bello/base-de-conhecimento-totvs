---
article_id: 360013430711
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: c03bf5e241317fc4a8a3d3a8fa72262c6c2d9ff87a6133b856eb0f6eeeb69546
fetched_at: '2026-06-28T22:40:32.338475+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 Tamanho do histórico
  no lançamento contábil
type: support-article
updated_at: '2024-10-25T19:37:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013430711-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Tamanho-do-hist%C3%B3rico-no-lan%C3%A7amento-cont%C3%A1bil
---

**Dúvida**É possível alterar o tamanho dos campos CT2\_HIST?  
  
**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - A partir da versão 11.80 **Solução** É possível modificar a quantidade de caracteres dos campos **CT2\_HIST, CTK\_HIST e CV3\_HIST**, porém não é aconselhável essa alteração, pois algumas rotinas em que estes campos são utilizados, estão limitadas a 40 caracteres, caso exista uma alteração, somente são exibidos **40 caracteres**, porém é permitido aumentar caso seja necessário, para no máximo 240 caracteres, tendo no Lançamento Normal (débito, crédito e partida dobrada) com 40 caracteres na **CT2\_HIST** e 5 linhas no campo **Cont. Hist**.

Para isto é necessário configurar o parâmetro [**MV\_CT5HIST**](https://tdn.totvs.com/pages/releaseview.action?pageId=606649086) - **Histórico de lançamento padrão** com o conteúdo em **.T.** Atualmente o sistema está padronizado para aceitar 240 caracteres no cadastro de histórico.

Alterar o parâmetro **MV\_AGLHIST** para .T. para que compreenda que precisa aglutinar as informações.

**Limite do campo CT2\_HIST:**<http://tdn.totvs.com/pages/releaseview.action?pageId=203761229>

Saiba mais:

[GERAÇÃO DOS RAZÃO CONTÁBIL COM O HISTORICO EM UMA LINHA UNICA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16693352223127-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR400-GERA%C3%87%C3%83O-DOS-RAZ%C3%83O-CONT%C3%81BIL-COM-O-HISTORICO-EM-UMA-LINHA-UNICA?source=search)
