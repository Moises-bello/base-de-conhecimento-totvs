---
article_id: 4413927848983
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 8961920d5d0be623fced98424a7a48378d0cd2296013edc0a97f6be94ea16011
fetched_at: '2026-06-28T22:37:21.437904+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como alterar a situação
  de um Contrato para Paralisado" ?
type: support-article
updated_at: '2022-02-14T11:31:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413927848983-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-alterar-a-situa%C3%A7%C3%A3o-de-um-Contrato-para-Paralisado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Com mudar a situação de um Contrato para Paralisado ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões  
  
**Solução**Das situações em que um contrato no módulo Gestão de Contratos pode estar, a situação ou legenda de "Paralisado" é realizada através de uma revisão de contrato.

Para tornar um contrato *"Paralisado"* deve-se cadastrar e utilizar a revisão do Tipo "5 - Paralisação".

E para retornar o contrato para *"Vigente"* deve-se cadastrar e utilizar a revisão do Tipo "6 - Reinicio".

Abaixo informações sobre estes Tipos de Revisões:

**5 - PARALISAÇÃO**

É utilizado para bloquear o contrato por um período. No momento em que este tipo de revisão for selecionado, é necessário informar o Motivo e a Data de Termino da Paralisação na Aba "Parâmetros/Revisão" e, automaticamente, é gerada uma revisão contratual e o bloqueio do contrato.

A escolha desta opção não habilita o preenchimento dos campos **Modo** e **Espécie**.

**Exemplo:**

O fornecedor não satisfaz a qualidade exigida pelas cláusulas do contrato. Neste caso, o contrato é paralisado até que o fornecedor melhore a qualidade de seu produto ou serviço.

***Obs.:***

Os Motivos de Paralisação podem ser cadastrados na rotina "Paralisações" em Gestão de Contratos->Cadastros->Tipos->Paralisações" (CNTA030)

**6 - REINÍCIO**

Este recurso é utilizado para desbloquear o contrato paralisado. Desta forma, toda e qualquer mudança no cronograma financeiro pode ser realizada normalmente neste tipo de revisão.  
No momento do reinício do contrato, de forma similar a um aditivo, o sistema realiza a validação e a atualização dos prazos de vigência e saldos existentes. Por fim, são apresentados os cronogramas financeiros para possível adequação das parcelas de acordo com a situação atual.

A escolha desta opção não habilita o preenchimento dos campos **Modo** e **Espécie**.

***Saiba Mais:***

[Tipos de Revisões de Contrato - CNTA010 - Gestão de Contratos - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=224447795)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
