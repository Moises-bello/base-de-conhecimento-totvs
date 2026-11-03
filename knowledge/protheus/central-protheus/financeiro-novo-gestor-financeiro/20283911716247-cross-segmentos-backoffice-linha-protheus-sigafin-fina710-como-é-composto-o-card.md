---
article_id: 20283911716247
category: Financeiro - Novo Gestor Financeiro
content_hash: 752940427b0085ac7a029ebab0a7c441c0859e7c3b01af616ac4bfc45a443aed
fetched_at: '2026-06-28T22:37:41.515063+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 Como é composto
  o Card formato Pizza "Entradas a vencer" e "Entradas vencidas" que fica FINA710
  Novo Painel Gestor > Movimentos > Abas Entrada ou Saída?
type: support-article
updated_at: '2026-01-07T18:30:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20283911716247-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Como-%C3%A9-composto-o-Card-formato-Pizza-Entradas-a-vencer-e-Entradas-vencidas-que-fica-FINA710-Novo-Painel-Gestor-Movimentos-Abas-Entrada-ou-Sa%C3%ADda
---

**Dúvida**  
Como é composto o Card formato Pizza "Entradas a vencer" e "Entradas vencidas" que fica FINA710 Novo Painel Gestor > Movimentos > Abas Entrada ou Saída?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -  Financeiro - FINA710 - A partir da versão 12.1.33  
  
**Solução**

Este exemplo a minha data corrente é 03/01/2024 (data do dia)

Temos 5 títulos, sendo que temos os títulos  
A001 possui vencimento no dia 20/12/2023 e está com o campo E1\_FLUXO = SIM  (Vencido há 14 dias)

A002 possui vencimento no dia 20/12/2023 e está com o campo E1\_FLUXO = NÃO  (Vencido há 14 dias)

A003 possui vencimento no dia 02/05/2023 e está com o campo E1\_FLUXO = SIM  (Vencido há 246 dias)

A004 possui vencimento no dia 02/05/2023 e está com o campo E1\_FLUXO = NÃO  (Vencido há 246 dias)

A004 possui vencimento no dia 01/02/2024 e está com o campo E1\_FLUXO = SIM (título não vencido)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20283918528535)](https://centraldeatendimento.totvs.com/hc/article_attachments/20283918528535)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20283918529943)](https://centraldeatendimento.totvs.com/hc/article_attachments/20283918529943)

- Veja como será exibido o gráfico

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20283918531607)](https://centraldeatendimento.totvs.com/hc/article_attachments/20283918531607)

Caso por algum motivo, exemplo Job desligado, os títulos não foram gravados na tabela  "F75 - Saldos de títulos", veja que o gráfico ou faltará informações ou não terá dados.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20283918532759)](https://centraldeatendimento.totvs.com/hc/article_attachments/20283918532759)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20283918533015)](https://centraldeatendimento.totvs.com/hc/article_attachments/20283918533015)

Caso o seu gráfico esteja com diferença ou zerado ao comparar com os títulos, o ideal seria verificar se o registro foi gravado corretamente na tabela "F75 - Saldos de títulos"  
  
Caso identifique que 1 ou 2 títulos não foram gravados na tabelas "F75 - Saldos de títulos" gerando dados inconsistentes no gráfico de pizza

Segue uma sugestão de processo paliativo de acertar:

Alterar uma característica do título que não gravou a tabela "F75 - Saldos de títulos"

Exemplo:

Alterar o vencimento do título, depois executar o job FINA711 que irá gravar na tabela F75 porém com o vencimento alterado, e depois retornar o vencimento original e executar o job novamente, e  sistema irá deletar o registro da tabela F75  e gravar novamente com o vencimento original

Isso ocorre pois ao alterar uma característica do registro, no caso um título a receber, automaticamente é gravado um novo conteúdo no campo S\_T\_A\_M\_P\_ da tabela SE1,  e o sistema entende que esse registro deve ser alterado na tabela F75

**Saiba Mais**  
<https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=622668231>
