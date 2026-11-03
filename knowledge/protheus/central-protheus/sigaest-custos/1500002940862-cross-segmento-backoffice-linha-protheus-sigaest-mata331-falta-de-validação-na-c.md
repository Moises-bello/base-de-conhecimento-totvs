---
article_id: 1500002940862
category: SIGAEST - CUSTOS
content_hash: f5e617b8eb114dd894c95e3de511c40819d67580b157d1bd20bddef45967e4b4
fetched_at: '2026-06-28T22:39:02.243063+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA331 - Falta de
  validação na contabilização do Custo
type: support-article
updated_at: '2026-04-06T18:16:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002940862-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA331-Falta-de-valida%C3%A7%C3%A3o-na-contabiliza%C3%A7%C3%A3o-do-Custo
---

Ao contabilizar o Custo Médio off-line no TOTVS Protheus, o sistema não valida ausências obrigatórias como Centro de Custo, Item Contábil ou Classe de Valor, impedindo a confirmação dos lançamentos. Para habilitar essa validação, é necessário configurar os parâmetros MV\_CT105MS e MV\_ALTLCTO com "S" no módulo Configurador (SIGACFG). Assim, mensagens de erro orientam o usuário a corrigir inconsistências antes de prosseguir.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30504020304279)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**

Ao efetuar a Contabilização do Custo Médio de forma off-line, o sistema não apresenta validação quando há ausência de informações obrigatórias, como Centro de Custo, Item Contábil ou Classe de Valor. Desta forma, os lançamentos são apresentados em tela e o usuário não consegue clicar em confirmar para seguir com o procedimento.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque - Todas as versões

**Solução**

Esta situação refere-se a uma configuração padrão do produto e ocorre porque o parâmetro responsável por acionar a mensagem de validação está desabilitado ou em branco no ambiente. O sistema permite definir se, em caso de inconsistência nas contabilizações, será exibida uma mensagem orientando sobre o que deve ser corrigido.

**Para resolver a questão e habilitar a validação em tela:**

1. Acesse o módulo **Configurador (SIGACFG)** e direcione-se à rotina de Parâmetros.
2. Localize o parâmetro [**MV\_CT105MS**](https://tdn.totvs.com/x/EgpeIg)e preencha o seu conteúdo com **S**.
3. Localize o parâmetro [**MV\_ALTLCTO**](https://tdn.totvs.com/x/EgpeIg)e certifique-se de que o seu conteúdo também esteja preenchido como **S**.

Após o preenchimento, sempre que faltar alguma informação durante a exibição dos lançamentos em tela, uma mensagem referente ao problema será demonstrada para que o usuário realize o ajuste.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)
