---
article_id: 360036131394
category: Financeiro - Contas a Pagar
content_hash: 4d16126da04aa7666cf7d00b85b94746c5baab9e0095dc8a5a89368789b709e5
fetched_at: '2026-06-28T22:38:07.171208+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus -SIGAFIN - Como contabilizar o
  Pagamento Antecipado (PA)
type: support-article
updated_at: '2026-06-12T17:37:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036131394-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-contabilizar-o-Pagamento-Antecipado-PA
---

**Duvida**  
Como contabilizar o Pagamento Antecipado (PA)?  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus todas as versões   
  
**Solução**  
Para contabilizar o pagamento antecipado (PA), deve utilizar o **Lançamento Padrão** **(LP) 513.**  
do sistema está posicionado no registro do título a pagar (TIPO = PA) na tabela **SE2** e no Movimento Bancário correspondente (TIPODOC = PA) na tabela **SE5**, podendo ser utilizados os campos da própria tabela, exemplo **E2\_VALOR** ou **E5\_VALOR**.

No momento da contabilização será tratado o parâmetro **MV\_CTMOVPA** que indica se a Contabilização do **Lançamento Padrão** (LP) 513 ocorrerá pelo Título na tabela **SE2** ou **Movimento Bancário** na tabela **SE5** do **Pagamento Antecipado** (PA). 1="**SE2**" / 2="**SE5**"

**Exemplo 1:**  
Emissão 17/08/2019 do TITA no valor 500,00 e o TITB no valor de 1000,00, ao realizar uma conciliação bancária do movimento destes títulos para alteração da data de disponibilidade para 18/08/2019.

**MV\_CTMOVPA = 1 (Default)**  
Contabilização ocorrerá pelo processo databela **SE2,** trata a data da emissão do registro.  
TITA+TITB no dia 17/08/2019 no valor de 1500,00

**MV\_CTMOVPA = 2**  
Contabilização ocorrerá pelo processo da tabela **SE5,** trata a data de disponibilidade do movimento.  
TITA+TITB no dia 18/08/2019 no valor de 1500,00

Portando o parâmetro **MV\_CTBAIXA** influenciará, depende do conteúdo: Se está **A ou B**,

Tipo de Contabilização da Baixa (**Contas a Pagar**) (B)aixa, na geração do (C)heque ou em (A)mbos os casos.

**Exemplo 2:**  
MV\_CTBAIXA = C  
MV\_CTMOVPA = 2 (SE5) ou MV\_CTMOVPA = 1 (SE2)

Com o **LP 513** configurado com a sintaxe SE2->E2\_VALOR

Contabiliza online = SIM

Mostra lançamento contábil = SIM

Gera cheque para adiantamento = NÃO

Movimenta banco sem cheque = **NÃO**

FINA050 - Inclusão de título a pagar, incluindo um tipo:PA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25947893994391)

Veja que o tipo:PA não gerou linha de movimentação bancária, **e não será contabilizado pelo LP 513 no momento da inclusão**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25947893996183)

Ao efetuar um retorno de CNAB pela rotina **FINA430** ou realizar a baixa automática pela rotina **FINA090,** neste momento será gerado a **movimentação bancária a pagar** para o tipo:PA ,  e será contabilizado pelo **LP 513.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25947894001815)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25947837833623)

Será exibido a mensagem ao efetuar a baixa pela rotina **FINA090 - Baixa Automática a pagar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25947894012311)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25947894017175)

Como ficará a posição de titulo a pagar

E que agora o tipo:PA gerou uma movimentação bancária a pagar (saída)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25947894023319)**

Caso realize novamente a baixa do tipo:PA pela rotina "**FINA080 - Baixas Manual a pagar**"

Será contabilizado pelo "**LP 530** - Baixas manual a pagar" onde o tipo:PA fará uma movimentação a receber (devolução do valor do tipo:PA novamente para o banco.)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25947837848599)

Podemos ver que que na imagem acima (posição do titulo a pagar)

O Tipo:PA gerou uma movimentação a pagar (saída) de cor cinza, e gerou uma movimentação a receber (entrada) cor verde.

**Exemplo 3:**

MV\_CTBAIXA = C  
MV\_CTMOVPA = 2 (SE5)

Com o **LP 513** configurado com a sintaxe SE2->E2\_VALOR

Contabiliza online = SIM

Mostra lançamento contábil = SIM

Gera cheque para adiantamento = NÃO

Movimenta banco sem cheque = **SIM**

FINA050 - Inclusão de título a pagar, incluindo um tipo:PA

Será chamado o **LP 513** no momento da inclusão

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25947837852823)

Podemos observar na imagem abaixo, que na inclusão do tipo:PA já foi realizado uma movimentação a pagar (saída)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25947894033687)**

**FINA080 - Baixas Manual a pagar**

Ao baixar o título tipo:PA

Será contabilizado pelo "**LP 530** - Baixas manual a pagar" onde o tipo:PA fará uma movimentação a receber (devolução do valor do tipo:PA novamente para o banco.)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25947894035991)**

**Importante:**

Funcionalidade presente na contabilização Online e Offline através da rotina **CTBAFIN**.

**Saiba mais**

<https://tdn.totvs.com/display/PROT/MV_CTMOVPA>
