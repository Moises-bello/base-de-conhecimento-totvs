---
article_id: 1500012682362
category: SIGAEST - LEGAIS
content_hash: fb16009baa1f93f2f425877c2c1347a2628688a9b67808f38fa64aa9ddb0e1a2
fetched_at: '2026-06-28T22:38:51.914278+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -MATR949 - Error.log
  "THREAD ERROR - Sintaxe incorreta perto da palavra-chave 'FROM'"
type: support-article
updated_at: '2021-05-31T14:45:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012682362-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR949-Error-log-THREAD-ERROR-Sintaxe-incorreta-perto-da-palavra-chave-FROM
---

**Dúvida**Ao emitir o relatório MATR949 - Mapa Demonstrativo de Entradas e Saídas de Produtos Controlados - Comando Militar (Exército) - Ocorre o seguinte error.log:

"*THREAD ERROR - Error : 156 (42000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Sintaxe incorreta perto da palavra-chave 'FROM'.*  
*( From tMSSQLConnection::GetQueryFile )*  
*SELECT SB5.B5\_COD,SB5.B5\_PRODEX,SB5. FROM SB5070 SB5 WHERE SB5.B5\_FILIAL=' ' AND SB5.B5\_COD='MP1013080005 ' AND SB5.B5\_PRODEX='S' AND SB5.D\_E\_L\_E\_T\_ = ' ' ORDER BY B5\_FILIAL,B5\_COD on PROCREL(MATR949.PRW)*"

Como corrigir este problema?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Para resolver este problema, basta preencher (ou criar) o parâmetro **MV\_MTR949D** com conteúdo = **B5\_DESC**, conforme a imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019986201/mceclip0.png)

Após isso, basta acessar novamente o relatório para que ele seja emitido e impresso na tela com sucesso.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
