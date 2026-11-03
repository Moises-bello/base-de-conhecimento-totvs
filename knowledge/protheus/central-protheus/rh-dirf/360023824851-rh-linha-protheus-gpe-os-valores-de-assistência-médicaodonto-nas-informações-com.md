---
article_id: 360023824851
category: RH – DIRF
content_hash: 74f66a1e9c1f7307cc13cea436d47b8f5a8d37eb504716f07409f9abedd8ee48
fetched_at: '2026-06-28T22:44:07.090821+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Os valores de assistência médica/odonto nas informações
  complementares estão divergentes, como corrigir
type: support-article
updated_at: '2025-08-19T17:34:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023824851-RH-Linha-Protheus-GPE-Os-valores-de-assist%C3%AAncia-m%C3%A9dica-odonto-nas-informa%C3%A7%C3%B5es-complementares-est%C3%A3o-divergentes-como-corrigir
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34296073177623)*** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Os valores apresentados nas informações complementares estão divergentes, como corrigir?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que os valores sejam demonstrados corretamente em **Informações Complementares da DIRF** (Miscelânea >DIRF >Manutenção do Arquivo >Outras Ações >Ações Complementares), é necessário que as informações estejam no Histórico de Planos de Saúde (tabela RHS) para valores de mensalidade de assistência médica/odonto e no Histórico de Coparticipação (tabela RHP) para os casos de coparticipação/reembolso.   
Estas informações podem ser acessadas por meio da rotina **Acumulado de Plano de Saúde (GPER014)** no módulo SIGAGPE ([Saiba como incluir a rotina GPER014 aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420942003351)).  
  
As verbas relacionadas ao plano de saúde/odonto, coparticipação e reembolso devem estar com **incidência R para DIRF** (Caminho rotina **verbas >Atualizações >Definições de cálculos >Verbas**).  
  
Mas, quando os valores são **lançados manualmente** ou **importados** diretamente na folha de pagamento, os dados não serão carregados corretamente para Informações Complementares da DIRF, pois na folha de pagamento não existe a informação de fornecedor, CNPJ e registro ANS.  
Dessa maneira **os valores para DIRF, devem ser lançados também manualmente**.   
Para isso siga o passo a passo do *link* a seguir: [Como informar o plano de saúde manualmente em Informações Complementares na DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021563052)   
  
E quando foi utilizada as rotinas padrões do sistema, porém os valores estão incorretos ou não foram carregados para as informações complementares?  
  
Nesses casos devemos analisar as seguintes situações para os valores descontados **mensalmente**:  
- Verifique se os valores estão na tabela de histórico de plano de saúde (tabela RHS);  
- Verifique se no Histórico de Planos de Saúde (tabela RHS) consta data de pagamento para todos os valores referentes ao ano calendário em questão;  
\* Caso não tenha data de pagamento, execute a rotina **GPEM004** ([Clique aqui e saiba como incluir no menu e utilizar a rotina](https://tdn.totvs.com/pages/releaseview.action?pageId=341214116))  
  
Para os casos de **coparticipação e reembolso**:  
- Verifique se os valores constam no Histórico de Coparticipação (tabela RHP)   
- Verifique se a data de pagamento está preenchida na tabela RHP referente ao ano calendário em questão;  
\* Caso não tenha data de pagamento ou não exista o dado na tabela RHP, execute a rotina **GPEM004** ([Clique aqui e saiba como incluir no menu e utilizar a rotina](https://tdn.totvs.com/pages/releaseview.action?pageId=341214116)).  
  
Após ajustes, execute novamente a rotina Gerar Arquivo [GPEM550](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437012).  
  
**IMPORTANTE:** Se os valores não estiverem nas tabelas, deverá ser feito o lançamento manual.  
  
  
**Saiba Mais**  
[Página centralizadora Protheus - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
