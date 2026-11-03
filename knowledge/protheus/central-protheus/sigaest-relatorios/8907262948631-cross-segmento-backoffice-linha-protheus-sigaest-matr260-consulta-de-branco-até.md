---
article_id: 8907262948631
category: SIGAEST - RELATORIOS
content_hash: d6be273745b6e633ccd97a5034021f34509b675d48e29d978a94e699b7a128b6
fetched_at: '2026-06-28T22:39:06.067806+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR260 - Consulta
  de "branco" até "Z" ou até "ZZZZZZ" não retorna produtos iniciados com a letra Z
type: support-article
updated_at: '2022-09-16T14:36:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8907262948631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR260-Consulta-de-branco-at%C3%A9-Z-ou-at%C3%A9-ZZZZZZ-n%C3%A3o-retorna-produtos-iniciados-com-a-letra-Z
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Consulta de "branco" até "Z"  ou até "ZZZZZZ" não retorna produtos iniciados com a letra Z no relatório MATR260. O que pode estar causando isso?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Geralmente este problema no relatório está relacionado a configuração do **Collation** do Banco de Dados.

Para o Protheus, são homologados os seguintes Collations abaixo:

**MSSQL:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8906930314775/mceclip2.png)

**Oracle:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8906918636439/mceclip1.png)**

**PostgreSQL:**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8906985056919/mceclip3.png)**

[Clique aqui para verificar documentação completa dos bancos de dados homologados para o Protheus.](https://tdn.totvs.com/display/public/PROT/Banco+de+dados+homologados)

Ao utilizar um Collation não homologado, pode acarretar em erros como esse no MATR260, fora outros problemas ainda não mapeados.

**Importante:**A configuração do Collation homologado, deve ser realizada com auxílio do DBA da empresa. (Tanto para configuração inicial, quanto para a correção do Collation após implantação). A correção não está relacionada apenas a alteração do Collation, existe toda uma tratativa a ser realizada nas tabelas já existentes.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Relatórios do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)*
