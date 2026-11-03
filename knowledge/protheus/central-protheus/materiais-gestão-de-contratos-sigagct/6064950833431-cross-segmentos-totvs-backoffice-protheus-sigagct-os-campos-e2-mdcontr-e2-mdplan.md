---
article_id: 6064950833431
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 1963017b8e4795d1a351c4c7935a61bc682d61e16265bf9883bac75599cc374e
fetched_at: '2026-06-28T22:37:23.991184+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Os campos E2_MDCONTR,
  E2_MDPLANI e E2_PARCE são gravados em quais situações no SIGAGCT ?
type: support-article
updated_at: '2026-05-19T14:44:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6064950833431-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Os-campos-E2-MDCONTR-E2-MDPLANI-e-E2-PARCE-s%C3%A3o-gravados-em-quais-situa%C3%A7%C3%B5es-no-SIGAGCT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40582936951447) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Qual o Conceito de gravação dos campos E2\_MDCONTR, E2\_MDPLANI e E2\_PARCE no Gestão de Contratos ?

**Ambiente**

Protheus - Gestão de Contratos -  A partir da versão 12.1.17.

**Solução**

No padrão do Gestão de Contratos, os campos E2\_MDCONTR, E2\_MDPLANI e E2\_PARCE são gravados no título a pagar (Financeiro), tabela SE2:

* Somente para os títulos provisórios, Tipo = PR, que são gerados na inclusão do contrato ao torná-lo "Vigente" (baseado no cronograma financeiro), e estando ativada a configuração do parâmetro MV\_CNPROVI;
* E também no título gerado no Encerramento de uma medição caso o campo: "**Nota/Título =** **Título",** conforme print abaixo, ou seja, quando o título é gerado dirertamente pelo SIGAGCT.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6065658042391)

No caso, de contratos/Medições que o campo: "**Nota/Título =** **Nota Fiscal",** não serão gravados na tabela SE2 que posteriormente é gerado pela NF do Pedido que foi gerado na medição, pois os respectivos campos não existem nas tabelas SD1 - Itens da Nota fiscal de entrada e na tabela SF1 - Cabeçalho da Nota fiscal de entrada.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6065889181207)  
   
E conforme o conceito do módulo estas informações são gravados apenas no documento que é gerado diretamente pelo Gestão de Contratos, ou seja, apenas no Pedido gerado no encerramento da medição.

***Saiba Mais:***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como desativar a geração de títulos provisórios na mudança de situação do contrato ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018381871-MP-GCT-Como-desativar-a-gera%C3%A7%C3%A3o-de-t%C3%ADtulos-provis%C3%B3rios-na-mudan%C3%A7a-de-situa%C3%A7%C3%A3o-do-contrato)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-MP-SIGAGCT-Pontos-de-entrada-para-rotinas-de-Medi%C3%A7%C3%A3o)
* [Nova Medição - CNTA121 - Gestão de Contratos - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=353284981)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
