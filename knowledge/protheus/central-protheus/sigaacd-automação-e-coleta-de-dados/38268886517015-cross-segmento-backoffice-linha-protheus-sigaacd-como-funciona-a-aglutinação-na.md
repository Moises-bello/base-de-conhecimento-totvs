---
article_id: 38268886517015
category: SIGAACD - Automação e Coleta de Dados
content_hash: f89a9aba0a98b6a20a095a4dff2c05804e5eaebf264c286899f08d16898401b4
fetched_at: '2026-06-28T22:39:11.130690+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD -  Como funciona a aglutinação
  na rotina ACDV120
type: support-article
updated_at: '2026-02-09T16:41:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38268886517015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-funciona-a-aglutina%C3%A7%C3%A3o-na-rotina-ACDV120
---

A aglutinação de itens na rotina ACDV120 do TOTVS Protheus ocorre quando registros na tabela SD1 são idênticos em todos os campos comparáveis, desconsiderando alguns campos específicos. Não há aglutinação se o parâmetro MV\_INTWMS estiver habilitado ou em importações via XML pelo TOTVS Colaboração.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38268930449559) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Em quais situações ocorre a aglutinação na conferência da rotina **ACDV120**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Em quais situações ocorre a aglutinação na conferência da rotina **ACDV120**?

A **aglutinação de itens** na rotina **ACDV120** ocorre no momento da conferência sempre que existirem registros na tabela **SD1** que sejam **idênticos em todos os campos comparáveis**.

Durante essa validação, **alguns campos são desconsiderados na comparação**. Ou seja, mesmo que esses campos possuam valores diferentes, os itens ainda poderão ser aglutinados.

### Campos desconsiderados na comparação:

* + `D1_QUANT`
  + `D1_QTDCONF`
  + `D1_TOTAL`
  + `D1_ITEM`
  + `D1_DTVALID`
  + `D1_LOTECTL`
  + `D1_QTSEGUM`
  + `D1_MSUIDT`

Se **todos os demais campos** estiverem exatamente iguais entre os registros, a rotina realizará a **aglutinação dos itens** durante a conferência.

## **Observações importantes sobre a não aglutinação de itens**

Existem cenários específicos em que a **aglutinação de itens não ocorre** na rotina **ACDV120**.

### 1. Parâmetro **MV\_INTWMS** habilitado

Quando o parâmetro **MV\_INTWMS** estiver habilitado no momento da geração do **Pré-Documento de Entrada**, por meio da rotina **MATA140**, o campo `D1_NUMSEQ` é automaticamente preenchido.

Como cada item passa a possuir um **número de sequência diferente**, os registros deixam de ser considerados idênticos, impedindo assim a **aglutinação dos itens** durante a conferência.

### 2. Importação de notas via XML (TOTVS Colaboração)

A aglutinação também **não ocorre** quando a nota fiscal é importada através do **TOTVS Colaboração**, utilizando arquivos **XML**.

### Exemplo de conferência com aglutinação

A seguir, é apresentada uma demonstração de uma conferência na qual os itens atendem aos critérios acima e, por isso, são aglutinados pela rotina **ACDV120**.

Geração do **Pré-Documento de Entrada**, Rotina **MATA140**:

![](https://tdn.totvs.com/download/attachments/1040980003/Pedido_01.png?version=1&modificationDate=1770298935787&api=v2)

![](https://tdn.totvs.com/download/attachments/1040980003/Pedido_02.png?version=1&modificationDate=1770299034200&api=v2)

Processo de conferencia na rotina **ACDV120** :

![](https://tdn.totvs.com/download/attachments/1040980003/ACDV120_01.png?version=1&modificationDate=1770300438723&api=v2)

![](https://tdn.totvs.com/download/attachments/1040980003/ACDV120_02.png?version=1&modificationDate=1770300467887&api=v2)

![](https://tdn.totvs.com/download/attachments/1040980003/ACDV120_03.png?version=1&modificationDate=1770300492387&api=v2)

![](https://tdn.totvs.com/download/attachments/1040980003/ACDV120_04.png?version=1&modificationDate=1770300566017&api=v2)

![](https://tdn.totvs.com/download/attachments/1040980003/ACDV120_05.png?version=1&modificationDate=1770300703007&api=v2)

![](https://tdn.totvs.com/download/attachments/1040980003/ACDV120_06.png?version=1&modificationDate=1770300741023&api=v2)

![](https://tdn.totvs.com/download/attachments/1040980003/ACDV120_07.png?version=1&modificationDate=1770300759723&api=v2)

Após confirmação da conferencia, acessar novamente a rotina **MATA140**, para verificar se ocorreu a aglutinação:

![](https://tdn.totvs.com/download/attachments/1040980003/Pedido_03.png?version=1&modificationDate=1770300990717&api=v2)

**Saiba mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[PACD0041 - Como funciona a aglutinação na rotina ACDV120](https://tdn.totvs.com/pages/viewpage.action?pageId=1040980003)
