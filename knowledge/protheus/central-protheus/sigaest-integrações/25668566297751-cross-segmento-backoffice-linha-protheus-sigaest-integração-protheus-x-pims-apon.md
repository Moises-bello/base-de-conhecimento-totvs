---
article_id: 25668566297751
category: SIGAEST - INTEGRAÇÕES
content_hash: 7901a8fe792d28c622b207a48d0674e5f03e422b182f751ccae8ada24a235004
fetched_at: '2026-06-28T22:38:46.232642+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Integração Protheus
  x PIMS Apontamento Agrícola  O Tipo de movimentação não foi cadastrado nos parâmetros
  MV_MTI241E | MV_MTI241S
type: support-article
updated_at: '2024-08-15T16:54:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25668566297751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Integra%C3%A7%C3%A3o-Protheus-x-PIMS-Apontamento-Agr%C3%ADcola-O-Tipo-de-movimenta%C3%A7%C3%A3o-n%C3%A3o-foi-cadastrado-nos-par%C3%A2metros-MV-MTI241E-MV-MTI241S
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25668566265751) Tempo aproximado para leitura: **00:01:45 min****Ocorrência**Ao realizar o Apontamento Agrícola, é apresentado a mensagem: " O Tipo de movimentação não foi cadastrado nos parâmetros MV\_MTI241E | MV\_MTI241S ou o tipo de movimentação: 2.1.30 não foi cadastrado."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25668566271895)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**Esse erro ocorre por falta de configuração do tipo de movimento para que a integração ocorra normalmente.

**Solução**

A integração se trata de uma via de mão dupla, sendo assim para que ela funcione adequadamente é necessário realizar as configurações tanto no Protheus, como no PIMS:

Dessa maneira para que a Integração funcione adequadamente no Protheus precisamos confirmar se os parâmetros estão configurados corretamente:

Acesse o Configurador (SIGACFG) > Ambiente > Cadastros > Parâmetros, e Localize os parâmetros MV\_MTI241E e MV\_MTI241S:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25668566274455)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25668538653463)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25668566275863)

Além disso, deve ser avaliado se o tipo de movimento informado nos parâmetros existem no sistema, esses registros ficam gravados na tabela SF5, ou pode ser visto na rotina MATA230:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25668538657431)

**Importante:** Caso toda a configuração na parte do Protheus esteja de acordo, é necessário avaliar no PIMS se os tipos cadastrados estão informados:

Acesse o PIMS Connector > Administração > Configurações PIMS > Tipo de Movimento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25668566283287)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25668538663319)

Nesse caminho deve ter as configurações de Apontamento Agrícola apontando para os mesmos tipos de movimentos.

Caso tenha dúvidas nessa configuração, recomendamos entrar em contato com o Suporte do PIMS Agroindústria para orientações nessa configuração.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Integrações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)*
