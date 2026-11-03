---
article_id: 1500012007521
category: SIGAEST - CUSTOS
content_hash: 6d5eac49ae54037e9c8aca18464deb8f97854bc320d9029824ff8279b3925882
fetched_at: '2026-06-28T22:39:02.187196+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Movimentos
  Internos zerados após o Recálculo do Custo Médio
type: support-article
updated_at: '2021-05-24T18:18:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012007521-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Movimentos-Internos-zerados-ap%C3%B3s-o-Rec%C3%A1lculo-do-Custo-M%C3%A9dio
---

**Ocorrência**Após o Recálculo do Custo Médio com a pergunta "gerar estrutura pela movimentação?" = "Não", alguns movimentos internos de devolução foram zerados.

**Causa**

No cenário onde ocorre produção em mais de uma filial e também transferências entre filiais o sistema está ordenando o RE1 da filial origem antes da produção da filial destino, por um problema de tratamento da ordenação.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.25  
  
**Solução**

Para corrigir este problema, aplique o pacote abaixo conforme a sua release:

**MATA330 12.1.23: [Clique aqui](https://r.totvs.io/p/1022869) | MATA330 12.1.25: [Clique aqui](https://r.totvs.io/p/1022870) | MATA330 12.1.27: [Clique aqui](https://r.totvs.io/p/1022896)**

Observação: Sempre aplicar atualizações primeiramente em ambiente de homologação.

Após aplicar, basta efetuar o Recálculo do Custo Médio novamente para que o tratamento da ordenação dos movimentos seja feito corretamente.

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA190 - Valor do Custo diminuindo após o Refaz Custo de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010690241)*

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
