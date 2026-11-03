---
article_id: 25983075808151
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: ccc79afb44688a445299be711a84263cfd48eb6ca18c1737c1bf7f6395c0b85e
fetched_at: '2026-06-28T22:39:08.293584+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Locais de estoque
  sem armazem preenchido
type: support-article
updated_at: '2025-03-12T12:17:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25983075808151-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Locais-de-estoque-sem-armazem-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25983043412503) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Avaliando alguns dados, nota-se locais de estoque, onde o campo de ARMAZEM esta em branco, como corrigir esse problema aparente?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões

**Solução**

O Protheus, em suas rotinas padrões, não permite a inserção de cadastros de produtos, notas fiscais, movimentos internos e outras operações que envolvam saldos de estoque sem o preenchimento do campo de armazém/local. Este campo é obrigatório e indispensável para a integridade das operações.

Caso seja identificado um cenário em que exista alguma tabela sem o preenchimento do campo armazém/local, é provável que isso seja resultado de uma customização específica, seja ela atual ou histórica, no ambiente em questão.

**Mas como corrigir esse problema?**

Recomendamos que a validação e correção desse tipo de inconsistência sejam realizadas com a assistência de um **consultor especializado em estoque e custos**. O consultor deverá realizar uma análise detalhada do ambiente para identificar as origens e corrigir as inconsistências nas tabelas de movimentação.

Alternativamente, a equipe  de infraestrutura do cliente pode realizar uma varredura completa nas tabelas de movimentações para identificar registros que possuam movimentações sem o devido preenchimento do campo armazém/local. Após essa identificação, será necessário corrigir esses dados, visto que não é possível existir movimentações ou saldos corretos sem que o campo armazém/local esteja devidamente preenchido.

Ressaltamos que este processo **é de caráter interno** e que o suporte padrão não abrange esse tipo de intervenção. Portanto, é imprescindível a atuação de um consultor qualificado junto ao cliente para a efetivação das correções necessárias.

**Saiba mais:**  
*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
