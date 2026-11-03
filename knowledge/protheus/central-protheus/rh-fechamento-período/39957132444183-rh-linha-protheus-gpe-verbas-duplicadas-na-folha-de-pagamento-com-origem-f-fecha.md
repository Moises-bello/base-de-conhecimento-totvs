---
article_id: 39957132444183
category: RH - Fechamento Período
content_hash: b2c43e0a1a7c468b86260dfa45885549de806cc7043ae56f27e7b40d9301d83a
fetched_at: '2026-06-28T22:43:24.516030+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - Verbas duplicadas na folha de pagamento com origem
  F - Fechamento
type: support-article
updated_at: '2026-04-23T14:09:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39957132444183-RH-Linha-Protheus-GPE-Verbas-duplicadas-na-folha-de-pagamento-com-origem-F-Fechamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39957132406807) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao calcular a folha de pagamento, o sistema apresenta verbas duplicadas, sendo elas com Origem **F- fechamento**. O problema ocorre após o fechamento do período anterior.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**  
Isso acontece quando há uma configuração no cadastro de verbas vinculando o evento a uma **Verba Mês Seguinte**, forçando o sistema a carregar o valor novamente ou quando o período da folha do mês anterior foi **reaberto** por algum motivo.  
  
**Solução**  
Para resolver a situação no período atual, é necessário **remover** os registros duplicados diretamente na tabela de movimentos (RGB), uma vez que a interface de lançamentos por funcionário **bloqueia** a exclusão de verbas com origem **F**. Para evitar novas ocorrências, o cadastro de verbas deve ser **corrigido**, caso haja configuração de verba mês seguinte indevida, ou em caso de reabertura de período, ter sempre o **apoio** de um **analista** ***in loco*** **TOTVS**.

**Passos**

1. Acesse o módulo **Gestão de Pessoal (SIGAGPE)**.
2. Vá em **Atualizações > Definições Cálculo > Verbas**.
3. Localize as verbas que estão duplicando.
4. Verifique o campo **Verba Próximo Mês** (ou Verba Mês Seguinte) e certifique-se de que não há um apontamento indevido para si mesma ou para outra verba que gere o conflito. Caso exista, remova a configuração.
5. Limpe o movimento atual na tabela **RGB** os registros com origem **F** que estão em duplicidade.
6. Recalcule a folha de pagamento e valide os resultados.

**Saiba Mais**

[RH - Linha Protheus - GPE - Quais os parâmetros utilizados para o fechamento do período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9070502632343-RH-Linha-Protheus-GPE-Quais-os-par%C3%A2metros-utilizados-para-o-fechamento-do-per%C3%ADodo)

[RH - Fechamento Período - Central de Atendimento TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909793-RH-Fechamento-Per%C3%ADodo)
