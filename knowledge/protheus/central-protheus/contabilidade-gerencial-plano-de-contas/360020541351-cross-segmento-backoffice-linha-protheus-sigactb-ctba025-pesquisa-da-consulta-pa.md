---
article_id: 360020541351
category: Contabilidade Gerencial - Plano de Contas
content_hash: 02f41314e53014ea56250f5047d8c26b66b7d1704ad5499934f39a436756b6ab
fetched_at: '2026-06-28T22:40:33.316513+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA025 Pesquisa da
  consulta padrão do Plano Referencial não funciona
type: support-article
updated_at: '2022-06-13T12:06:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020541351-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA025-Pesquisa-da-consulta-padr%C3%A3o-do-Plano-Referencial-n%C3%A3o-funciona
---

**Ocorrência**Não está sendo possível realizar consulta pelo código da **Conta Referencial via Consulta Padrão**.

**Ambiente**Protheus - Contabilidade Gerencial - 12.1.17

**Causa**Este ocorrido pode ser apresentado por questão de configuração de **índice(SIX)** no ambiente utilizado.

**Solução**Para sanar a questão, verifique se:

-No ambiente, os **índices(tabela SIX) da CVN(Planos de Contas de Referencia)** encontram-se conforme a imagem:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016432811/mceclip0.png)

**OBS:** Caso não estejam iguais, recomendamos que rode o Compatibilizador(UPDDISTR) com os últimos dicionários Diferencial e Completo para os devidos ajustes.

-Após efetuar a verificação dos índices devemos agora configurar o sistema para que faça a busca pela ordem desejada, no caso a 6 que pesquisa pela Conta Referencial.   
Para isso, entre na rotina que irá fazer a busca da Conta Referencial, abra a sua **Consulta Padrão**e selecione a opção de **configuração da consulta**, assim como na imagem:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016381412/mceclip1.png)

-Clique em Consulta Padrão:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016433231/mceclip2.png)

-Selecione o **índice 6 e salve as alterações**, assim será possível efetuar a pesquisa pela conta referencial desejada:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016433491/mceclip4.png)

-Para que a ocorrência seja sanada, também é necessário verificar se o campo **CVD\_CTAREF** está com a configuração correta, para isso veja a nossa documentação: [MP - SIGACTB - VINCULO DO PLANO DE CONTAS REFERENCIAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007012691-MP-SIGACTB-VINCULO-DO-PLANO-DE-CONTAS-REFERENCIAL?source=search)

**Saiba mais:** [MP - SIGACTB - CVD\_CODPLA - PLANO DE CONTAS REFERENCIAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007357911-MP-SIGACTB-CVD-CODPLA-PLANO-DE-CONTAS-REFERENCIAL-?source=search)
