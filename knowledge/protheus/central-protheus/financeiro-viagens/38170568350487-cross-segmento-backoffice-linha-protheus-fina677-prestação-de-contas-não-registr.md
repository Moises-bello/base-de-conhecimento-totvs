---
article_id: 38170568350487
category: Financeiro - Viagens
content_hash: 0cdf66eff0a31a714c4726e52cccaeef5ced8d22eafa2a2c7733740d15035728
fetched_at: '2026-06-28T22:38:21.205621+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA677 - Prestação de contas
  não registra reembolso
type: support-article
updated_at: '2026-02-04T20:10:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38170568350487-Cross-Segmento-Backoffice-Linha-Protheus-FINA677-Presta%C3%A7%C3%A3o-de-contas-n%C3%A3o-registra-reembolso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38170579863191) Tempo aproximado para leitura: **00:05 min**  
  
**Ocorrência**  
Ao utilizar despesa com limite diário, a prestação de contas não registra o reembolso.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FINA677 - Todas as Versões.  
  
**Causa**  
A causa provável reside na configuração do **Tipo de Despesa** na rotina **Tipos de Despesa (FINA679)**. Para garantir que o sistema considere o limite individualmente por dia, é necessário verificar e reajustar a parametrização de vigência dessa despesa, focando nos campos de limite.

**Solução**  
Acesse o módulo Financeiro e execute a rotina **Tipos de Despesa** **(FINA679)**.

1. **Editar a Despesa:** Edite o código da despesa e verifique a aba de **Vigências**.
2. **Confirmar o Tipo Limite:** O campo **Tipo Limite** deve estar como **1 - Limite Diário**.
3. **Ajustar os limites de vigência:**

   * Confirme se o valor está corretamente inserido nos campos de limite da vigência (Lim. Sem Perm. ou Limite Perm.). O cálculo incorreto pode estar sendo causado por uma leitura errada do limite diário ao tentar somar as despesas.![Screenshot_7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38170568343575)
4. **Recálculo na Prestação de Contas:**
   * Após qualquer ajuste, acesse a rotina **Prestação de Contas** **(FINA677)**.
   * No documento que está com o erro, utilize a opção de **Recalcular** o limite de despesas (disponível em **Outras Ações** ou funcionalidade semelhante) para forçar o sistema a reprocessar os limites com a nova configuração.

**Saiba Mais**

[Central de Atendimento TOTVS - Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA679 - Cadastro de Despesas e Despesas X Localização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033699394-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA679-Cadastro-de-Despesas-e-Despesas-X-Localiza%C3%A7%C3%A3o)

[Central de Atendimento TOTVS - Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA677 - Como recalcular o limite de despesas da Viagem](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15821139916567-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA677-Como-recalcular-o-limite-de-despesas-da-Viagem)

[Central de Atendimento TOTVS - Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA679 - HELP: Tipo Limite ao tentar alterar o campo tipo limite](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33637701216279-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA679-HELP-Tipo-Limite-ao-tentar-alterar-o-campo-tipo-limite)
