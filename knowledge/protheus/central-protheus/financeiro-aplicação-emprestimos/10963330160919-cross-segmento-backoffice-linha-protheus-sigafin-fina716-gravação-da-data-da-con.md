---
article_id: 10963330160919
category: Financeiro - Aplicação / Emprestimos
content_hash: aba7bf40bbbc73c950482a87df7cb7295f7a871e46a0a951a93006511888ac61
fetched_at: '2026-06-28T22:37:59.289472+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmento - Backoffice linha Protheus -  SIGAFIN  - FINA716  - Gravação
  da data da contabilização de uma apropriação no contábil
type: support-article
updated_at: '2026-01-07T19:19:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10963330160919-Cross-Segmento-Backoffice-linha-Protheus-SIGAFIN-FINA716-Grava%C3%A7%C3%A3o-da-data-da-contabiliza%C3%A7%C3%A3o-de-uma-apropria%C3%A7%C3%A3o-no-cont%C3%A1bil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17822145839895) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
FINA716 – Na contabilização da apropriação, qual a data que será levada para o contábil (CT2)?  
  
**Exemplo:**  
Considere uma aplicação em **CDI** realizada em **01/11**. O usuário acessa o sistema com a **database** ajustada para **15/12**.

Ao efetuar o processo de apropriação, é informada no campo **“Data da Apropriação?”** a data **30/11**, e a contabilização é realizada de forma online.

Diante desse cenário, questiona-se: qual data será considerada no envio das informações ao módulo contábil?

Será utilizada a database **do sistema** (data em que o usuário está logado) ou a **data informada no parâmetro** “Data da Apropriação?”  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da versão 11  
  
**Solução**  
A data gravada no contábil (tabela CT2) será a database (data em que estava logado no sistema), porém os valores são calculados e gravados na SEI com base na data que foi inserida no conteúdo da pergunta "Data da Apropriação? ”

Caso tenha necessidade de levar uma data diferente para o contábil, utilizar o ponto de entrada **ALTDATAL.**

[ALTDATAL](https://tdn.totvs.com/display/public/PROT/PE+ALTDATAL)

**Importante**

Todas as rotinas do financeiro levam para a contabilidade sempre a database logada do sistema em uma contabilização on-line.  
  
**Documentação de Referência:**  
[Aplicações e Empréstimos - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=392500138)
