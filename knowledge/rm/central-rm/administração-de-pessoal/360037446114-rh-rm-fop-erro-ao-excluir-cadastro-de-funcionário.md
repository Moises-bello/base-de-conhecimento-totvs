---
article_id: 360037446114
category: Administração de Pessoal
content_hash: 82dd93f21ae783049d93da63a91a1ebb7366e669b3dbcbd966e3d412c45ae162
fetched_at: '2026-06-28T22:47:02.231707+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Erro ao excluir cadastro de funcionário
type: support-article
updated_at: '2025-03-12T13:39:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037446114-RH-RM-FOP-Erro-ao-excluir-cadastro-de-funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:04:15 min****Ocorrência**Ao tentar excluir o cadastro de funcionário, são apresentadas mensagens que reportam erro ao excluir registros de tabelas como PFUNC, APARFUN, entre outras. Segue abaixo alguns exemplos de erros que podem ser apresentados:  
  
Erro ao excluir os registros da tabela PFUNC.  
Verifique as tabelas relacionadas.  
FKPFITEMLAN\_PFUNC

Erro ao excluir os registros da tabela PFUNC.  
Verifique as tabelas relacionadas.  
FKVCONSULTASPRONT\_PFUNC

Erro ao excluir os registros da tabela PFUNC.  
Verifique as tabelas relacionadas.  
FKPPFUNCPRESTSERVTERCEIROS\_PFU

Erro ao excluir os registros da tabela PFUNC.  
Verifique as tabelas relacionadas.  
FKPGPSLOGCALCDETALHE\_PFUNC

Erro ao excluir os registros da tabela APARFUN.  
Verifique as tabelas relacionadas.  
FKAPERFUN\_APARFUN  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Este tipo de incidente ocorre pois, após o cadastro do funcionário, houveram movimentações para o funcionário, como lançamento de folha, recálculos, lançamentos de certas informações que alimentam tabelas do módulo de Folha de Pagamento, bem como de outros módulos, como: Automação de Ponto, Gestão Financeira, etc.  
  
**Solução**A rotina exclusão de funcionário foi criada para excluir um funcionário **somente** quando for criado no mês de competência atual e não ter tido **nenhuma** movimentação ou processo executado para o mesmo. Porém caso o usuário já tenha realizado qualquer movimentação para esse funcionário, será apresentado erro ao executar a rotina de exclusão. Na mensagem, será apresentado qual foi a **tabela envolvida**, portanto, será necessário acionar o DBA da própria empresa para realizar a limpeza via Banco de Dados nas tabelas apresentadas. Essa intervenção via Banco de Dados é de responsabilidade da própria empresa. O erro na exclusão do funcionário é uma segurança do produto, pois foi detectado a execução de processos para o funcionário, não permitindo a exclusão.  
  
**Importante**Caso seja de preferência da empresa, também temos o setor de Consultoria tarifada. Neste serviço, um Consultor TOTVS poderá realizar os procedimentos necessários diretamente na Base de Dados do cliente.  
  
**Saiba mais**[TOTVS RH - Linha RM - PTO - Como realizar a exclusão de funcionários admitidos no período atual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012517431)[RH - RM - FOP - Exclusão de funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416040659479-RH-RM-FOP-Exclus%C3%A3o-de-funcion%C3%A1rio)
