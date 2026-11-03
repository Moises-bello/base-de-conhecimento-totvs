---
article_id: 360047676454
category: Financeiro - Contas a Receber
content_hash: b92b31ef5bc2e02565bd614b749dfcf0d196a42bec66c5dc38389476499049a1
fetched_at: '2026-06-28T22:38:14.257228+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN -  FINA350 - Contabilização do Estorno da Variação Monetária a
  Receber
type: support-article
updated_at: '2026-03-24T14:17:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047676454-MP-SIGAFIN-FINA350-Contabiliza%C3%A7%C3%A3o-do-Estorno-da-Varia%C3%A7%C3%A3o-Monet%C3%A1ria-a-Receber
---

**Dúvida**  
Como realizar a contabilização do estorno da variação monetária a receber?  
  
**Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 12  
  
**Solução**  
Foi disponibilizado na rotina Contas a Receber (**FINA040**) o lançamento padrão **59A**, que tem como finalidade fazer a contabilização do estorno da variação monetária a receber.

Procedimentos para Utilização

Pré-requisito:

1. No **Financeiro (SIGAFIN)**acesse a opção **Atualizações / Cadastros / Lançamento Padrão.**

Corrigir o lançamento padrão 59A.

2. Acesse a opção **Atualizações / Cadastros / Moedas.**

Incluir a moeda 2 em duas datas diferentes.

3. Acesse a opção **Atualizações / Contas a Receber / Receber.**

Incluir um título com a moeda 2 e fazer a contabilização on-line.

4. Acesse a opção **Miscelânea / Contab. Var Monet.**

Faça a contabilização da variação monetária.

5. Acesse a opção **Atualizações / Contas a Receber / Receber.**

Faça a exclusão do titulo a receber

6. Após a exclusão do título, é efetuada a contabilização da exclusão do título e da variação monetária.

**Importante:**  
Não existe uma rotina de estorno para os lançamentos pela rotina **FINA350**, apenas a exclusão do título, sendo assim, não será possível estorná-lo Deve ser feita uma nova variação no dia em questão, colocando a taxa correta, o sistema irá ajustar para o valor desejado. Somente poderá contabilizar o estorno da variação monetária a receber.

**Saiba mais:**  
[Lançamento padrão para variação contábil](https://tdn.totvs.com/pages/releaseview.action?pageId=244934660)
