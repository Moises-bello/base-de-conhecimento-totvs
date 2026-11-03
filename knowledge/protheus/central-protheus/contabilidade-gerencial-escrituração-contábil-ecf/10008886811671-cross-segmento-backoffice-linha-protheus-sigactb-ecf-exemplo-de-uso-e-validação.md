---
article_id: 10008886811671
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: fc6cd392aa6310cfb63ac16ebcd9c8686e7df274f2140d89495893f9bdb1c969
fetched_at: '2026-06-28T22:40:47.362670+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - Exemplo de uso
  e validação da função SaldoConta | Bloco L210
type: support-article
updated_at: '2022-11-04T17:19:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10008886811671-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Exemplo-de-uso-e-valida%C3%A7%C3%A3o-da-fun%C3%A7%C3%A3o-SaldoConta-Bloco-L210
---

**Ocorrência**

Exemplo de uso e validação da função SaldoConta | Bloco L210

Apresentar o saldo estoque  no inicio  do período de apuração

   
**Ambiente**Cross Segmento - TOTVS Backoffice  - TOTVS Contabilidade Gerencial  - Todas as versões  
  
  
**Solução**

**Para este caso será necessário utilizar o  [função SaldoConta | Bloco L210](https://tdn.totvs.com/pages/viewpage.action?pageId=6068544)**

Exemplo:

* **[Arquivo modelo visão gerencial L210](http://tdn.totvs.com/pages/releaseview.action?pageId=189314312)**
* **[Necessário Amarração Visão Gerencial ao Livro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)**

CTBA161 Configuração da Visão gerencial

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10008336621079)

Exemplo utilização [função saldoconta](https://tdn.totvs.com/pages/viewpage.action?pageId=6068544)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10008432216855)

CTBA102 - Lançamento contabil :

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10008302330135)

Emitir o relatório DRE com a visão gerencial configurada com a formula

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10008375659415)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10008376474647)

* Verifique como o  parâmetro  abaixo foi preenchido

***![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078399533/mceclip5.png)***

***![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077269674/mceclip6.png)***

***![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077269714/mceclip7.png)***

* Solicito que verifique as***[Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)***

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077271714/mceclip14.png)

**Para conciliação dos saldos**

* Verifique a amarração da visão , veja se ao emitir relatório com a visão gerencial (CTBR500,CTBR040) o saldo é gerado correto , caso  o sistema apresente no relatório também o saldo errado ,  será necessário avaliar a configuração da visão gerencial

* Verifique a tabela CSD os registros foram gerados

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10008739969943)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10008793016599)

* Através do gerenciado de integração veja se dados foram gerados

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10008795750295)

* Através da tabelas TAFST1 e TAFST2 verifique se o T088AC foi gerado
* Com base na [estrutura do Layout](https://tdn.totvs.com/pages/releaseview.action?pageId=498722271) verifique a do Bloco T088AB e T088AC.  
  -Verifique se a tabela TAFST1 foi alimentada :  
  - no registro da conta verifique T088  
   \*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração  
      \* Editar > Alterar -  Verifique  se a conta referencial está sendo apresentada  
    Ex:

|T088|20220101|20221231|A00|

|T088AB|1|

|T088AC|1|500|

|T088AC|2|500|

|T088AA|1|1.01.01.09.10|500|1|13500|1|13000|0|

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10008801777047)

Com base na [estrutura do Layout](https://tdn.totvs.com/pages/releaseview.action?pageId=498722271)  verifique se a estrutura gerada está correta

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078401353/mceclip13.png)

Acesse as rotinas abaixo para verificar se os registros foram alimentados:

**Registro L200 - Método de Avaliação do Estoque Final**

* Tabela - CAR (Método Avaliação Estoque Final)
* Registro do Layout TOTVS - **T088AB**
* Rotina - [**TAFA361**](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512) (Bloco L - Lucro Líquido)

**Registro L210 - Informativo da Composição de Custos**

* Tabela - CAS (Informativo da Comp. de Custos)
* Registro do Layout TOTVS - **T088AC**
* Rotina - [**TAFA361**](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512) (Bloco L - Lucro Líquido)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10008836506391)

*Ao* gerar o arquivo o sistema gerou o L210

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10008839413783)
