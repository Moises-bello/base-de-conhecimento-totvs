---
article_id: 360018607411
category: PMS - Projetos
content_hash: 9084aeffac7e296d2f634dd0a38dccbdedf8cf53b45c9dd97baa2a9f6e09eca3
fetched_at: '2026-06-28T22:37:16.000619+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: MP - PMS - Projetos Compartilhados com Movimentos Exclusivos
type: support-article
updated_at: '2021-04-29T21:13:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018607411-MP-PMS-Projetos-Compartilhados-com-Movimentos-Exclusivos
---

**Dúvida**

Qual a configuração para projetos compartilhados e movimentos exclusivos ?

**Ambiente**

Protheus - PMS – A partir da versão 11.80  
  
   
**Solução**

Os procedimentos deverão ser seguidos para apuração correta do custo realizado do projeto:

As tabelas de apontamentos e do gerenciamento de execução, tais como, SF1/SD1-Nota Fiscal de Entrada, SE2-Contas a Pagar, SC1-Solicitação de Compras etc, mesmo estando em modo exclusivo, podem ser visualizadas no escopo do projeto, desde que as tabelas de projetos (família AE/AF/AJ) estejam em modo compartilhado e as tabelas de amarrações entre projeto x apontamento ou projetos x tabelas do gerenciamento de execução contenha o campo '<ALIAS>\_MSFIL' com a filial de origem com exceção da tabela de empenhos do projeto(TABELA AFJ).

Para tanto, siga os procedimentos com detalhes em :

<http://tdn.totvs.com/display/PROT/PMS0024_Projetos_Compartilhados_Com_Movimentos_Exclusivos>
