---
article_id: 360021518871
category: RH - Relatórios
content_hash: e47df8e040d5047458f9db602e81431d92f3eacf066ae07653945cd1f9478de0
fetched_at: '2026-06-28T22:44:43.527508+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Espelho de Ponto em Duplicidade
type: support-article
updated_at: '2025-12-22T17:29:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021518871-RH-Linha-Protheus-PON-Espelho-de-Ponto-em-Duplicidade
---

**Dúvida**Ao emitir espelho de ponto de um período em aberto, o sistema gera em duplicidade.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**No Ponto Eletrônico, o processo padrão é realizar o **fechamento mensal do período (PONM090)**, com isso, o sistema cria de forma automática um novo período de apontamento, que pode ser consultado dentro da rotina de **Atualizações> Cadastro do Ponto>Períodos de Apontamento> Modificar Período de Apontamento> Apenas Visualizar> Salvar.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35468442633111)**  
Quando é criada uma linha nesta rotina manualmente (legenda verde), o sistema entende que o período em questão está fechado, porém também constará em aberto no parâmetro **MV\_PONMES**, **emitindo duas folhas idênticas de espelho de ponto.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35468442635287)**Ou seja, gerará em duplicidade quando o mesmo período estiver cadastrado na primeira tela da rotina PONA290 e, aberto pelos parâmetros MV\_PAPONTA e MV\_PONMES.  
  
**Para correção**, é necessário a exclusão desta linha criada manualmente na rotina de Período de Apontamento, através de **Outras Ações>Excluir** e após isso emita o espelho novamente.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35468442638615)  
  
Outra possibilidade de gerar um espelho de ponto em duplicidade é a pergunta **Número de Cópias**, nos parâmetros de geração do espelho. Orientamos a deixar essa pergunta com o **conteúdo 0**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35468470225815)  
  
**Saiba mais:  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)**[RH - Linha Protheus - PON - Como imprimir o Espelho de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004253171-RH-Linha-Protheus-PON-Como-imprimir-o-Espelho-de-Ponto?source=search)
