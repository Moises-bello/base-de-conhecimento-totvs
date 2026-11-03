---
article_id: 1500001544821
category: SIGAEST - LEGAIS
content_hash: 5693595db55b6f9dfc72a3e983cd72cd263c784ec1036a5a48346ecbc97764c5
fetched_at: '2026-06-28T22:38:51.608057+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K - Erro: SQL
  Server: Sintaxe incorreta próxima a '',''.'
type: support-article
updated_at: '2021-05-03T19:04:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001544821-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-Erro-SQL-Server-Sintaxe-incorreta-pr%C3%B3xima-a
---

**Duvida**

Ao gerar o SPED Fiscal com Gera Bloco K = Sim é apresentado o seguinte error.log: *"THREAD ERROR [14632]*  
*: Error : 102 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Sintaxe incorreta próxima a ','".* O que fazer para resolver este problema?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17

**Solução**

Para solução do problema, siga os passos abaixo.

**1° - Certifique-se de que seu ambiente está atualizado**

Para isso, atualize o pacote acumulado do módulo de Estoque.

***Pacotes acumulados Estoque/Custos:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571) **|** 12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640) **|** 12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/748747)

**Observação:**Atualizar primeiramente em ambiente de testes.

**2° - Validar existência de cadastro de parâmetro sem aspas simples**

Nos parâmetros MV\_BLKTP00 ao MV\_BLKTP10, seu conteúdo deve conter aspas simples antes e depois da descrição.

Exemplo correto MV\_BLKTP00 = 'PA'

Exemplo incorreto: MV\_BLKTP00 = PA

Se estiver sem aspas simples, basta ajustar e gerar novamente o SPED.

**3° - Execute o SPED com o ambiente sem Customizações/Pontos de Entrada**

Se a sua base possuir Ponto de Entrada ou Customizações, em sua tabela XX7, altere o campo XX7\_STATUS de todas as linhas de 1 para 2. Com isso, o sistema desabilitará todos os P.Es e Customizações.

Se mesmo com os três passos acima persistir o problema, acione ao nosso time de Suporte Técnico do módulo de Estoque/Custos com as devidas evidências para uma melhor análise.

**Saiba mais:**

[MP - SIGAEST - Bloco H - Error.log THREAD ERROR - Cannot resolve the collation conflict between "Latin1\_General\_BIN" and "SQL\_Latin1\_General\_CP1\_CI\_AS" in the equal to operation.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060156814-MP-SIGAEST-Bloco-H-Error-log-THREAD-ERROR-Cannot-resolve-the-collation-conflict-between-Latin1-General-BIN-and-SQL-Latin1-General-CP1-CI-AS-in-the-equal-to-operation-)

[MP - SIGAEST - Bloco H - Error.log "THREAD ERROR ([14620], Error : 1222 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Lock request time out period exceeded."](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060155834-MP-SIGAEST-Bloco-H-Error-log-THREAD-ERROR-14620-Error-1222-37000-RC-1-Microsoft-SQL-Server-Native-Client-11-0-SQL-Server-Lock-request-time-out-period-exceeded-)

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
