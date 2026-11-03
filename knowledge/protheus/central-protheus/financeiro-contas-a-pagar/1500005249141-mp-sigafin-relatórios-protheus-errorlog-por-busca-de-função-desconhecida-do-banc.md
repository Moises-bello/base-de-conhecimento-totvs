---
article_id: 1500005249141
category: Financeiro - Contas a Pagar
content_hash: 99bd986a1b9a770881a03247e608b64bcf5e2334875390d20de8957242475b3b
fetched_at: '2026-06-28T22:38:09.954748+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - Relatórios Protheus - Error.log por busca de Função Desconhecida
  do Banco de dados
type: support-article
updated_at: '2021-04-28T15:17:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005249141-MP-SIGAFIN-Relat%C3%B3rios-Protheus-Error-log-por-busca-de-Fun%C3%A7%C3%A3o-Desconhecida-do-Banco-de-dados
---

**Ocorrência**No módulo Financeiro, ao tentar realizar a impressão de relatórios nossos FINR's o sistema apresenta error.log:

***" : Error : 195 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]***

***'RPAD' não é um nome da função incorporada reconhecido."***

**Ambiente**Microsiga Protheus - a  partir 12.1.17

**Causa**Ocorre que nossos relatórios verificam o **TOPDatabase** do banco de dados, no caso o sistema pode estar ajustado para **MSSQL7** por exemplo e ao realizar a tentava de execução do relatório ao chamar a FUNÇÃO **RPAD** o sistema exibe error.log pois, essa função não deve existir nas bibliotecas dessa versão de banco de dados. 

**Solução**Para solucionar essa ocorrência, realize o seguinte passo:

- Alterar no AppServer para **MSSQL** realizar testes para a execução dos relatórios. 

**Mais informações: <https://tdn.totvs.com/display/public/PROT/Banco+de+dados+homologados>**
