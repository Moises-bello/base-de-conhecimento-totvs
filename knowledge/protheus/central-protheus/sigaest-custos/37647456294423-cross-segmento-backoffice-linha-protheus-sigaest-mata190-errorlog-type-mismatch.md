---
article_id: 37647456294423
category: SIGAEST - CUSTOS
content_hash: 00d8f0e4357b2e702cb2b794cf400dd7a79abdc83f5c9f1251e9ce9d0830b2e5
fetched_at: '2026-06-28T22:39:00.363346+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA190 - errorlog:
  type mismatch in array subscriptor - expected N->C on BACKOFFICE.STOCK.CALCULATIONCOST.CALCULATIONNFETRBGEN
  (BACKOFFICE.STOCK.CALCULATIONCOST.TLPP)'
type: support-article
updated_at: '2026-06-17T15:33:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37647456294423-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA190-errorlog-type-mismatch-in-array-subscriptor-expected-N-C-on-BACKOFFICE-STOCK-CALCULATIONCOST-CALCULATIONNFETRBGEN-BACKOFFICE-STOCK-CALCULATIONCOST-TLPP
---

O erro "type mismatch in array subscriptor" ocorre na rotina Refaz Custo de entrada devido a inconsistências na regra tributária da Substituição Tributária (ST) da nota fiscal de entrada. Isso pode ser causado por regra inexistente, parâmetro incorreto ou divergência em campos tributários. A solução envolve gerar o errorlog, identificar o ID do configurador de tributo (CIDTRIB), localizar a nota fiscal envolvida, validar a regra tributária e corrigir a configuração para refazer a nota fiscal corretamente.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37647456269207) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**

Ao executar a rotina Refaz Custo de entrada é gerado o errorlog: **"type mismatch in array subscriptor - expected N->C on BACKOFFICE.STOCK.CALCULATIONCOST.CALCULATIONNFETRBGEN(BACKOFFICE.STOCK.CALCULATIONCOST.TLPP)"**, como posso identificar e corrigir?   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**

Esse incidente ocorre quando há **inconsistência na regra tributária utilizada no cálculo da Substituição Tributária (ST) da nota fiscal de entrada**.

O erro “type mismatch in array subscriptor – expected N->C” indica que, durante o processamento do cálculo de custo, o sistema tentou acessar uma posição do array relacionada ao **CIDTRIB (ID do configurador de tributo)** com um tipo diferente do esperado (numérico vs caracter).  
Isso geralmente ocorre devido a:

* Regra de cálculo **inexistente** ou **excluída** da base;
* Parâmetro tributário **incorreto ou incompleto** no configurador de tributos;
* Divergência entre **D1\_IDTRIB**, **F2D\_IDREL** e o campo **F2D\_TRIB**, causando falha ao gerar a estrutura de cálculo usada na rotina de custo.

**Solução**

**1. Gerar o errorlog completo:**

Quando o erro aparecer em tela, salve o conteúdo exibido em um bloco de notas para análise.

**2. Localizar o STACK do processo:**  
No arquivo errorlog, procure pelo trecho:  “**BACKOFFICE.STOCK.CALCULATIONCOST.CALCULATIONNFETRBGEN**”. Nesse ponto será possível identificar o ID do configurador de tributo (CIDTRIB) que não foi carregado corretamente durante o cálculo do custo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37647456270359)

**3. Identificar a nota fiscal envolvida:**  
Localize o campo D1\_DOC no errorlog para descobrir qual é a NF de entrada associada ao CIDTRIB que gerou a falha.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37647465072407)

**4. Validar a regra tributária utilizada na NF:**  
De posse do número da nota, consulte o campo **D1\_IDTRIB** e verifique o relacionamento com o campo **F2D\_IDREL**, conforme documentação:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como identificar impostos do Configurador de Tributos nas Notas Fiscais?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37535417591319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-identificar-impostos-do-Configurador-de-Tributos-nas-Notas-Fiscais)

**5. Verificar a configuração no F2D:**  
No registro **F2D** correspondente, valide o campo **F2D\_TRIB**, confirmando se a regra tributária está ativa, íntegra e corretamente configurada.  
→ Caso a regra esteja incorreta, incompleta ou inexistente na base, ou registros **DELETADOS**, o errorlog pode ser gerado.

**6. Corrigir e refazer a nota:**  
Após identificar o problema na regra tributária, ajuste o configurador conforme necessário. ***Em seguida, cancele e refaça a NF de entrada para permitir o cálculo correto do custo.***

Em caso de validação pontual, da inexistencia dos fatos apresentados acima, e ainda a ocorrencia do problema, onde o erro pode ocorrer devido a inconsistencia de dados na base, é sugestivel o acompanhamento de um analista in loco.

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGAEST - Como configurar o custo de entrada com impostos na TES?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19509172274455-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-configurar-o-custo-de-entrada-com-impostos-na-TES)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como identificar impostos do Configurador de Tributos nas Notas Fiscais?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37535417591319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-identificar-impostos-do-Configurador-de-Tributos-nas-Notas-Fiscais)
