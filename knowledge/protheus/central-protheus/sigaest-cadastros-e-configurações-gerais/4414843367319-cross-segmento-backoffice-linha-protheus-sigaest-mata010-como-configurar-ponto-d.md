---
article_id: 4414843367319
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 40b843df1faed20a8a9c8c2c6d2eb9770650978fb965064ff9a7955da0bd9471
fetched_at: '2026-06-28T22:39:09.453303+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Como configurar
  Ponto de Pedido?
type: support-article
updated_at: '2021-12-03T12:17:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414843367319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-configurar-Ponto-de-Pedido
---

**Dúvida**Como configurar o Ponto de Pedido no Protheus?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Ponto de Pedido é a quantidade em estoque que uma vez atingida, pode iniciar o processo de compra a partir da **Geração de Solicitações de Compras por ponto de pedido.**

Toda vez que o Sistema detectar a falta de um material, somando saldo em estoque, pedidos e solicitações de compras em aberto e esta for menor que o Ponto de Pedido definido em seu cadastro de Produto é gerado uma **Solicitação de Compras**.

**Como configurar do Ponto de Pedido no cadastro de Produto?**

**![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008595311/Sem_t_tulo.png)**

Os campos "Ponto de Pedido" (B1\_EMIN) e  "Estoque de Segurança" (B1\_ESTSEG) definirão sua configuração para Ponto de Pedido.

O campo B1\_EMIN define a quantidade mínima pré-estabelecida que, uma vez atingida, ao processar a rotina de Solicitações por Ponto de Pedido, gera emissão de uma solicitação de compras.

Já o campo B1\_ESTSEG irá definir a quantidade mínima do produto em estoque para evitar a falta do mesmo entre a solicitação de compra e o seu recebimento.

**Como gerar a Reposição de Estoque quando o produto entrar no Estoque de Segurança?**

Para maiores informações sobre como gerar a Reposição do Estoque a partir do Estoque de Segurança, veja o boletim abaixo:

*[Cross Segmento - Backoffice Protheus - SIGACOM - Como gerar Solicitação de Compras/Pedido de Compras por ponto de pedido ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011967491-MP-SIGACOM-Como-gerar-Solicita%C3%A7%C3%A3o-de-Compras-Pedido-de-Compras-por-ponto-de-pedido-)*

**Saiba mais:**

*[Como gerar o Cálculo do Ponto de Pedido, Estoque de Segurança e Lote Econômico](https://tdn.totvs.com/pages/releaseview.action?pageId=347442943#:~:text=O%20lote%20econ%C3%B4mico%20informa%20a,produtos%20classificados%20pela%20curva%20ABC.&text=Exemplo%3A,cada%2030%20Dias%20(%201%20m%C3%AAs%20))*

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
