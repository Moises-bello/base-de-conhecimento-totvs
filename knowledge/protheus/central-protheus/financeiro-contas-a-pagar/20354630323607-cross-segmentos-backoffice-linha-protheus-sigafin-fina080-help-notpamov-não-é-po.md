---
article_id: 20354630323607
category: Financeiro - Contas a Pagar
content_hash: 5fe45cd0ebcb015541071f51ed2363971f48faf8deeaf9b7dd57260cdf61a339
fetched_at: '2026-06-28T22:38:09.582670+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA080 - HELP NOTPAMOV
  - Não é possível realizar a baixa de pagamento antecipado sem movimentação bancária
type: support-article
updated_at: '2025-09-04T15:17:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20354630323607-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA080-HELP-NOTPAMOV-N%C3%A3o-%C3%A9-poss%C3%ADvel-realizar-a-baixa-de-pagamento-antecipado-sem-movimenta%C3%A7%C3%A3o-banc%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20354630295319) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**No módulo Financeiro, ao tentar baixar um título de pagamento antecipado é apresentado a mensagem

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20354622698903)

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o pagamento antecipado foi gerado sem movimentação bancária ou alteração nas propriedades do motivo de baixa padrão.

Ao efetuar alteração nas propriedades dos motivos de baixa padrão do sistema, podem gerar riscos no sistema.

As alterações efetuadas nos motivos de baixa padrão do sistema devem ser realizados com muita cautela pois o sistema os utiliza para diversas operações internas.

Considere uma movimentação relacionada a um motivo (DEB - Débito CC) que num determinado momento atende a carteira - Contas a Pagar.

Uma alteração de carteira, de Pagar para Receber, poderá fazer com que as operações anteriores não sejam reconhecidas. Por exemplo: Uma baixa realizada com um motivo o qual venha a sofrer uma alteração de carteira ou sigla e que mais adiante se necessite efetuar o Cancelamento daquela Baixa. O sistema poderá não reconhecer o movimento anterior se o motivo de baixa fizer parte do critério de localização.

Portanto, podemos classificar os riscos de irregularidade da seguinte forma:

Alto - Mudanças de Carteira, de Sigla e exclusões de motivos;  
Médio - Mudanças nas propriedades: Mov. Bancária, Comissão, Cheque e Espécie;  
Baixo/Muito Baixo - Mudanças na Descrição.

**IMPORTANTE: Opte sempre por criar novos registros e mantenha os motivos padrão.**

**Solução 1**Só é possível baixar um título de pagamento antecipado que tenha movimento bancário. Para gerar a movimentação bancária deste título, realize os seguintes passos:  
1. Acesse a rotina **Baixa Automática** e preencha com um motivo de baixa que movimente banco;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20354630302743)  
2. Selecione o título do **pagamento antecipado** sem a movimentação e clique em **Salvar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20354622700567)  
3. Neste momento, o sistema fará uma **movimentação bancária** do título de **pagamento antecipado**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20354622701719)

Após este processo, o título ficará disponível para baixa.

Outro cenário é quando altera o motivo de baixa **FINA490** **'NOR'** somente para a uma carteira receber

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21182028069783)

Se não deixar como Carteira **'Ambos'**ou criar um baixa **NOR** para a carteira à pagar o help será apresentado.

Veja que ao criar o **PA** o motivo da primeira movimentação é criando como **NOR** e para que consiga realizar a baixa o motivo precisa está como **'Ambos'**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21181986475671)

**Solução 2**

**Exemplo de risco de alteração do motivo de baixa padrão onde irá gerar colateral no ERP.**

FINA080 - Ao baixar um título tipo:PA poderá apresentar a mensagem :

"Help: NOTPAMOV   
Problema:  Atenção. Não é possível realizar a baixa de pagamento antecipado sem movimentação bancária. Verifique se os motivos de baixa padrão encontram-se disponíveis - FINA490"

**Motivo:**

Alteração das propriedades do motivo de baixa "**NOR**", onde o campo foi alterado para  "**Mov. Bancária = Não**" com isso o sistema irá apresentar o **HELP** NOTPAMOV

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34698467585175)

Sugerimos que não altere os motivos de baixa padrões do sistema, e crie sempre novos motivos.

**Saiba Mais:**

<https://tdn.totvs.com/display/public/PROT/Baixas+Pagar+Manual+-+FINA080+-+Financeiro+-+P12>  
[FIN0082\_Tabela de motivos de baixa - Contas a Pagar e Receber](https://tdn.totvs.com/display/public/PROT/FIN0082_Tabela+de+motivos+de+baixa+-+Contas+a+Pagar+e+Receber)
