---
article_id: 29030020163351
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 88d64eb8f5e724b919e7317c71971ee7e726535f8d408867061bb0e7707611d3
fetched_at: '2026-06-28T22:39:09.724917+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais tabelas são
  relacionadas ao modulo SIGAEST?
type: support-article
updated_at: '2025-03-12T11:39:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29030020163351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-tabelas-s%C3%A3o-relacionadas-ao-modulo-SIGAEST
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29030020158999) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**  
Quais são as tabelas relacionadas ao modulo SIGAEST, Estoque/Custos/ACD? Como consultar as tabelas do modulo?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Você pode efetuar uma relação das tabelas do modulo, através de uma consulta de dados, sob a tabela **SX2 Tabelas do sistema.**

Cada modulo tem um numero, o modulo de Estoque Custos, é o modulo 04, conforme exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29030000828183)

Para que você possa verificar, quais tabelas estão relacionadas a esse modulo, solicite ao seu analista de TI, que faça a consulta de dados, pode ser via APSDU ou via Banco de dados.

**Exemplo via banco de dados SQL:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29030020159895)

**Exemplo via APSDU:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29030020160279)

---

Dessa forma, as tabelas serão apresentadas conforme o módulo desejado. Ressalta-se que essa relação pode variar entre releases ou ambientes, dependendo de fatores como integrações e customizações específicas.

Caso você esteja buscando algo específico, é necessário abrir um ticket direcionado ao suporte do módulo desejado, detalhando o motivo pelo qual necessita da relação solicitada. Essas informações permitirão que a equipe de suporte compreenda melhor a necessidade apresentada e forneça a assistência adequada.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
