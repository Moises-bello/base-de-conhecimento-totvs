---
article_id: 360013258331
category: Requisições
content_hash: 9ae80fede5c96c3642ba563e14b03955c8910d5a47e43cd50b3858c0de107541
fetched_at: '2026-06-28T22:47:25.380329+00:00'
product: rm
section_id: 1500000861382
source: central-rm
title: RH - RM - RHU - Campo salário não disponível nas requisições de transferência
  com alteração de dados funcionais
type: support-article
updated_at: '2025-04-28T14:36:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013258331-RH-RM-RHU-Campo-sal%C3%A1rio-n%C3%A3o-dispon%C3%ADvel-nas-requisi%C3%A7%C3%B5es-de-transfer%C3%AAncia-com-altera%C3%A7%C3%A3o-de-dados-funcionais
---

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27002704114327)Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**O campo salário não está disponível na abertura das requisições de transferência com alteração de dados funcionais, o que fazer?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Totvs Gestão de Pessoas - Todas as versões  
  
**Solução**A regra de negócio da requisição de Transferência com alterações de dados funcionais é permitir a definição salarial ao chefe de destino e não ao chefe de origem da requisição, pois são os chefes de níveis mais altos ou das seções que irão receber o funcionário que, em tese, tem o controle/gerência de verbas do seu centro de custo e etc. Desta forma, os requisitantes não terão acesso ao campo.  
  
No caso dos aprovadores seguintes editarem/visualizarem ou não o campo, não dependerá necessariamente se estes pertencem a área que efetua as movimentações.  
  
Com base no comportamento do produto, assim que a Requisição for encaminhada para o próximo aprovador, a edição/visualização do campo por estes gestores poderá ser gerenciada por meio das permissões de acesso a campos do Perfil vinculado ao seu Usuário, onde poderão definir se o Usuário verá ou não o campo salário (VLRSALARIO) da tabela VREQTRANSPROMOCAO.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27002704124055)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27002704130839)

**Saiba Mais**

Para maiores informações, acesse:

- [Requisição de Transferência com Alteração de Dados Funcionais](https://tdn.totvs.com/pages/releaseview.action?pageId=452719580)
