---
article_id: 4411589623063
category: RH - Provisão
content_hash: a79d8507ff7810889ff18e633746cfb5fe423d00f990e69fb727838f3aaa91d7
fetched_at: '2026-06-28T22:43:55.974194+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de entrada  GP070BIF - Baixa de Férias -
  INSS FGTS
type: support-article
updated_at: '2026-03-23T18:07:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411589623063-RH-Linha-Protheus-GPE-Ponto-de-entrada-GP070BIF-Baixa-de-F%C3%A9rias-INSS-FGTS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17874047593751) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Utilização do ponto de entrada  GP070BIF.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**  
**1. Visão Geral**

Ponto de entrada para alterar os valores de Inss e Fgts das Baixas das férias proporcionais na provisão.

**Programa Fonte**  
GPEM070.PRX  
  
**Sintaxe**

GP070BIF - Baixa de Férias - INSS/FGTS ( )

Retorno()

**2. Exemplos de utilização**

User Function GP070BIF()  
nBx\_Inss := 100  
nBx\_FGTS := 200  
Return()

**3. Variáveis**  
**Outras Ações / Ações relacionadas**

| Nome | Tipo | Escopo | Pode Alterar | Descrição |
| --- | --- | --- | --- | --- |
| nBx\_Inss | Numérico | Privado | Sim |  |
| nBx\_Fgts | Numérico | Privado | Sim |  |

![GP070BIF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17874047600279)

**Importante:**  
A baixa de férias que é tratada no ponto de entrada refere-se ao pagamento de férias por ocasião de gozo de férias e não em caso de rescisão.   
A baixa será realizada nos identificadores de cálculo 0234 e 0235 no cálculo das provisões de férias, não será gerada nenhuma informação adicional na folha.

**Saiba Mais**  
[Documentação Técnica](https://tdn.totvs.com/pages/viewpage.action?pageId=642631194)
