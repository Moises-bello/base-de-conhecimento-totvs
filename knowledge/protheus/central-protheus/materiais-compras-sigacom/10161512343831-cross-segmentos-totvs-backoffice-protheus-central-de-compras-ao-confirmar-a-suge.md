---
article_id: 10161512343831
category: Materiais - Compras (SIGACOM)
content_hash: fd090825652f5b33f96af42b5472857369daf65e240e63d4bcc983829adb0d6d
fetched_at: '2026-06-28T22:41:12.856657+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - Central de Compras - Ao Confirmar
  a Sugestão de Compra o Pedido é Gerado para Fornecedor Aleatório
type: support-article
updated_at: '2022-11-11T13:48:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10161512343831-Cross-Segmentos-Totvs-Backoffice-Protheus-Central-de-Compras-Ao-Confirmar-a-Sugest%C3%A3o-de-Compra-o-Pedido-%C3%A9-Gerado-para-Fornecedor-Aleat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03 min****Ocorrência**

1. Ao realizar alteração do cadastro de Fornecedor e efetivar a sugestão de compra, sistema apresenta mensagem de que o cadastro está bloqueado e não efetiva a sugestão de compra.
2. Sistema não atualiza condição de pagamento ao fazer alteração do código de Fornecedor.
3. Após efetivação da sugestão de compra, sistema não apresenta o número do documento gerado na grid Documento.
4. Sistema permite que ao realizar alteração da sugestão de compra, o campo Doc. Compra (**DBI\_DOCOMP**) seja alterado.
5. Campo Fornecedor (**DBI\_FORNEC**) não possui consulta padrão (F3), para busca do Cadastro de Fornecedores.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12

**Solução**

1. Tratamento para que o sistema considere o código do Fornecedor gravado na tabela DBI (**DBI\_FORNEC**) e não realize a validação do Fornecedor através da amarração produto x fornecedor ou pelos campos Forn. padrão (**B1\_PROC**) e Loja padrão (**B1\_LOJPROC**).
2. Feito ajuste para que a condição de pagamento seja gravada de acordo com o código do Fornecedor.
3. Realizado tratamento para que seja apresentado o número do documento gerado após a gravação do documento.
4. Realizado ajuste para não permitir alteração do campo Doc. Compra(**DBI\_DOCOMP**).
5. Inclusão da consulta padrão do campo Fornecedor (**DBI\_FORNEC**).

**Demais informações :**

* **Referente ao item 5**, o ajuste docampo DBI\_FORNEC estará disponível automaticamente a partir do**release12.1.2310,**porém poderá ser feito manualmente ou através da aplicação da expedição contínua de compras (data superior26/09/2022)
* [Pacote de atualização - Compras](https://tdn.totvs.com/pages/viewpage.action?pageId=522011099)

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
