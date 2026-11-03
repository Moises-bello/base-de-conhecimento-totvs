---
article_id: 31749069079191
category: SIGAEST - RELATORIOS
content_hash: 37beb8406fdec6a309a702485f6fe3dddd007ce58f0cc753de27f7720483791d
fetched_at: '2026-06-28T22:39:06.128946+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR282 - Error.log
  [SQL Server Native Client 11.0][SQL Server]Nome de coluna 'TRK_FILIAL' inválido.
type: support-article
updated_at: '2025-04-29T18:19:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31749069079191-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Error-log-SQL-Server-Native-Client-11-0-SQL-Server-Nome-de-coluna-TRK-FILIAL-inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31749112412183) Tempo aproximado para leitura: **00:02:17 min****Ocorrência**Ao gerar o relatório MATR282 ocorre o erro: [Microsoft][SQL Server Native Client 11.0][SQL Server]Nome de coluna 'TRK\_FILIAL' inválido.  
SELECT SUM(BK\_QINI) BK\_QINI FROM TRK990\_SP WHERE (BK\_FILIAL = '01' AND BK\_COD = 'ACD001 ' AND BK\_LOCAL = '01' AND D\_E\_L\_E\_T\_ = ' ') AND ((ISNULL(TRK\_FILIAL,'01') = '01')) on MTR282IMP(MATR282.PRX)   
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**Esse incidente ocorre pois o usuário logado está com algumas permissões faltantes para exibição do relatório

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse ao Configurador. Entre no menu Usuário -> Senhas -> Usuário  
2. Altere o usuário que ao gerar o relatório enfrenta o error.log  
3. Clique em "Restrições de Acesso" na parte superior, após isso clique na aba "Acessos"

4. Certifique-se de que este usuário esteja com as permissões 169, 190, 196, 197 e 198. Elas são imprescindíveis para este erro ser sanado.

Com isso o problema não ocorrerá mais.

**Saiba mais:**

[*MP - Relação dos acessos de usuários do ambiente Configurador*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115012706728-MP-Rela%C3%A7%C3%A3o-dos-acessos-de-usu%C3%A1rios-do-ambiente-Configurador)

*[Clique aqui e veja mais artigos sobre Relatórios no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)*
