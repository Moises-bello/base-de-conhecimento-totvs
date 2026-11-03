---
article_id: 360058809993
category: SIGAEST - PODER DE TERCEIROS
content_hash: f9cf1e635eacede90603b50a1bc41be1968167c53ecd6e8a87122778ea93f11a
fetched_at: '2026-06-28T22:39:03.227598+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Na devolução de Poder
  de Terceiros foi inserido um TES incorreto. Como ajustar o saldo?
type: support-article
updated_at: '2026-06-02T14:42:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058809993-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Na-devolu%C3%A7%C3%A3o-de-Poder-de-Terceiros-foi-inserido-um-TES-incorreto-Como-ajustar-o-saldo
---

**Dúvida**  
Quais os passos para dar baixa no saldo DE/EM terceiros, quando ao efetuar a devolução **não** for utilizada TES com o campo "Poder de Terceiros" (F4\_PODER3) = Devolução ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Toda nota de entrada ou saída que utilizou a TES configurada com o campo **Poder de Terceiros (F4\_PODER3) = Devolução**, indica que iniciou o controle do Saldo de Terceiros, essas movimentações, geram registros na tabela SB6, que para baixa-los devem estar amarrados às Notas Fiscais devolvendo o saldo utilizando o campo **Poder de Terceiros (F4\_PODER3) = Devolução**.

Porém quando na devolução **não** **foi** **utilizada a TES com o campo F4\_PODER3 = Devolução,** no padrão é possível ajustar através de uma forma:

* Estornar a nota que foi emitida com a TES sem controle de poder de terceiro igual à Devolução, e classificar novamente com a TES correta. Esse cenário ocorre quando é identificado a tempo que possa estornar a classificação da nota.

**Caso não seja possível estornar a classificação da nota a tempo, cabe validar internamente ao setor fiscal da empresa, a possibilidade de gerar a nota com a TES correta sem a necessidade de transmissão, apenas com finalidade de ajuste nos saldos em estoque.**

**Observações:** Não existe no padrão uma funcionalidade para ajuste de poder de terceiros por inventário ou outras rotinas de ajustes.

**Saiba mais:**

[*MP - FAT - Poder de terceiros Correta configuração do cadastro de TES*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004201467-MP-FAT-Poder-de-terceiros-Correta-configura%C3%A7%C3%A3o-do-cadastro-de-TES)

[*Clique aqui e veja mais artigos sobre Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)
