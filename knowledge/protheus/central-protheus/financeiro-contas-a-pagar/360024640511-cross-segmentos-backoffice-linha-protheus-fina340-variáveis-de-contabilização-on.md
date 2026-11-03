---
article_id: 360024640511
category: Financeiro - Contas a Pagar
content_hash: 3e90c30131ad46ded06b87ce8e7bfccf4e9f56824dbcf033ee27acf7f37b74e6
fetched_at: '2026-06-28T22:38:07.039148+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA340 - Variáveis de contabilização
  (online e offline) da Compensação de Contas à Pagar
type: support-article
updated_at: '2026-06-03T20:22:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024640511-Cross-Segmentos-Backoffice-Linha-Protheus-FINA340-Vari%C3%A1veis-de-contabiliza%C3%A7%C3%A3o-online-e-offline-da-Compensa%C3%A7%C3%A3o-de-Contas-%C3%A0-Pagar
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20882423152023)**Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Quais são as variáveis de contabilização (online e offline) da Compensação de Contas a Pagar?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Solução**

A seguir, apresenta-se a lista de variáveis que podem ser utilizadas na configuração do **Lançamento Padrão 597 (Compensação CP)** para a **contabilização on-line** da Compensação CP (**FINA340**):

**VALOR** - Armazena o valor compensado.  
**VALOR2** - Valor de Acréscimo.  
**VALOR3** - Valor de Decréscimo.  
**VALOR4** - Variação da correção monetária.  
**VLRINSTR** - Armazena o valor compensado.  
**nSldReal** - armazena o valor compensado na moeda correspondente do título.  
**ABATIMENTO** - Valores de abatimentos.  
**REGVALOR** - Recno do registro atual.  
**STRLCTPAD** - Chave do título principal+número do documento.

**Contabilização Online**

Na contabilização **online**, quando o lançamento padrão **597** estiver configurado com o campo **CT5\_VLR01** utilizando a variável **VALOR**, o sistema gerará um único lançamento contábil com o valor total compensado da operação.

Esse comportamento é nativo do processo de compensação com contabilização online e **não está relacionado** ao parâmetro **"Aglutina Lançamentos?"** da rotina **FINA340**.

Por outro lado, quando o campo **CT5\_VLR01** estiver configurado com o conteúdo **SE5->E5\_VALOR**, o sistema gerará um lançamento contábil individual para cada nota fiscal vinculada à compensação.

A seguir, apresenta-se a lista de variáveis que podem ser utilizadas na configuração do **Lançamento Padrão 597 (Compensação CP)** para a **contabilização off-line** da Compensação CP (**FINA340**):

**VALOR** - Armazena o valor compensado.  
**VALOR2** - Valor de Acréscimo.  
**VALOR3** - Valor de Decréscimo.  
**REGVALOR** - Recno do registro atual.  
**STRLCTPAD** - Chave do título principal+número do documento.  
**VARIACAO** - Valor da variação monetária. (Deverá utilizar a função ABS() para deixar positivo.)

**Contabilização Offline**

Na contabilização **offline**, independentemente de o campo **CT5\_VLR01** do lançamento padrão **597** estar configurado com a variável **VALOR** ou com **SE5->E5\_VALOR**, o sistema gerará um lançamento contábil individual para cada nota fiscal vinculada à compensação.

Dessa forma, recomenda-se validar se essa configuração atende às necessidades do seu processo, uma vez que o comportamento da variável **VALOR** na contabilização offline (**CTBAFIN**) difere do comportamento observado na contabilização online (**FINA340**) para esse mesmo cenário.

**Importante**

A contabilização da compensação será sempre feita com base nos dados da Nota fiscal.

Caso seja de extrema necessidade o posicionamento no PA, o desenvolvedor da empresa pode criar uma função utilizando o comando **"Posicione"**. Vale ressaltar que o Suporte Padrão TOTVS não auxilia no processo de criação de customizações; havendo dificuldades na implementação, deverá ser acionada uma equipe de consultoria ou especialista em ADVPL.

**Saiba mais**

[597 Compensação Contas a Pagar](https://tdn.totvs.com/pages/releaseview.action?pageId=556885546)
