---
article_id: 1500000461062
category: Escrita Fiscal - Error.log
content_hash: bd185bae08e1dea91e297db7c46e83d9f68f4fa4c067645866f3ee12426a9231
fetched_at: '2026-06-28T22:39:32.921048+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: 'MP - FIS - Error.log Data width error - Field: S1_MARGEM Value: 121.000000
  on GRVHISTFIS(FISXFUN.PRX)'
type: support-article
updated_at: '2021-04-28T19:01:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000461062-MP-FIS-Error-log-Data-width-error-Field-S1-MARGEM-Value-121-000000-on-GRVHISTFIS-FISXFUN-PRX
---

**Dúvida**  
Ao tentar informar um valor de MVA no campo Margem de Lucro (F7\_MARGEM) é apresentado error.log referenciando o campo S1\_MARGEM:  
  
Data width error - Field: S1\_MARGEM Value: 121.000000 on GRVHISTFIS(FISXFUN.PRX)  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**  
O error.log acima é apresentado por motivo do campo S1\_MARGEM ter o tamanho diferente do campo  F7\_MARGEM.

Para correção do erro, será necessário acessar o configurador e alterar o tamanho e decimal do campo S1\_MARGEM (Tabela SS1) e deixando igual o campo F7\_MARGEM (Tabela SF7).  
  
Após executar o procedimento acima, salve as alterações, acesse o sistema e efetue o testes na rotina de Exceção Fiscal (MATA540) incluindo o a margem de lucro no campo "Margem de Lucro (F7\_MARGEM)".

Caso o campo S1\_MARGEM estiver bloqueado para alteração, foi disponibilizado na versão 12.1.17 a correção contendo dicionário de dados com tratamento para que o campo S1\_MARGEM fique habilitado para alteração.  
  
Abaixo documento técnico e link contendo a correção :  
  
Documento Técnico:   
<https://tdn.totvs.com/pages/releaseview.action?pageId=327329379>  
  
Correção Contendo Dicionário na Release 12.1.17:  
  
12.1.17: <https://suporte.totvs.com/portal/p/10098/download?e=657413>  
  
Sendo confirmado que o campo S1\_MARGEM está bloqueado para uso, basta executar o dicionário de dados mencionado acima e, em seguida alterar o tamanho e decimal do campo S1\_MARGEM conforme instruído acima.
