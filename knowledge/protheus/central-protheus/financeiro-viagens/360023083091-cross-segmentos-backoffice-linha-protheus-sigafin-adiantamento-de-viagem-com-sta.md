---
article_id: 360023083091
category: Financeiro - Viagens
content_hash: 1bb39b426f8342a7c8bc4d3db4dc36c6a03c0ae66c6a532497eaa3d6af2379cb
fetched_at: '2026-06-28T22:38:21.222476+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  Adiantamento de viagem
  com status bloqueado '
type: support-article
updated_at: '2023-12-15T16:47:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023083091-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Adiantamento-de-viagem-com-status-bloqueado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**No módulo Financeiro, na rotina de Adiantamentos de viagens, existem adiantamentos com status bloqueado, impedindo sua liberação ou qualquer tipo de ação.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**   
Esse incidente ocorre, pois existe uma ou mais prestação de contas em atraso aberta para o mesmo participante do adiantamento.  
  
**Solução**  
Para solucionar essa ocorrência, será necessário finalizar a prestação de contas em atraso.  
1. Acesse a rotina **FINA677 - Prestação de contas** e identifique a prestação de contas em atraso;  
2. Verifique se a prestação já possui suas despesas cadastradas, caso contrário cadastre-as através da opção alterar;  
3. Após o preenchimento das **despesas**, em outras ações, encaminhe para **conferência**;  
4. Confira e aprove a **conferência** gerada;  
5. Encaminhe a **prestação de contas** para aprovação do gestor;  
6. O gestor deve aprovar a **prestação de contas**;  
7. Ainda na rotina de **prestação de contas**, em outras ações, selecione a opção **Liberar financeiro**. Neste momento será criado um **título a pagar**;  
8. Através da rotina **FINA080 - Baixas a pagar manual**, efetue a baixa do título criado.  
9. Após estes procedimentos, será possível desbloquear o **adiantamento**.  
10. Acesse a rotina de **Adiantamentos de viagens** e em outras ações, selecione as opções Aprovar ou **aprovar por lote**. Neste momento o adiantamento terá seu status **alterado** para **aprovado**.

**Observação:** No item 2, caso não tenha despesas, é possível reprovar a **prestação de contas** em questão, encaminhando para **conferência** e conferindo. Deste modo a prestação ficará com o status **reprovado**.

**Importante:**Algumas opções descritas acima, somente é possível caso o usuário logado no sistema seja o aprovador deste participante. Exemplo: Aprovação da prestação de contas e aprovação do adiantamento.
