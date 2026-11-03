---
article_id: 360022630231
category: SIGAEST - LEGAIS
content_hash: bf27c973ea4af8972a4ddc02cf67deaa053a3c5c0f3b1dc20e256ad7823f4e48
fetched_at: '2026-06-28T22:38:51.449335+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K - Processo
  para geração do registro K270
type: support-article
updated_at: '2021-09-03T14:06:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022630231-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-Processo-para-gera%C3%A7%C3%A3o-do-registro-K270
---

**Dúvida**Qual o processo para geração do Registro K270 no *Protheus*?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O Registro K270 tem o objetivo de escriturar correção de apontamento de período de apuração anterior, relativo ao "registro-pai", por tipo de registro e por período de apuração em que o apontamento será corrigido. Caso ocorra correção de apontamento apenas do "registro-filho", este Registro deverá ser informado com os campos de quantidade zerados

**Quais movimentos do Protheus o Registro K270 (Correção de Apontamento) leva em consideração?**

As rotinas de movimentação de estoque do Protheus consideradas para este registro são:

* MATA240 - Transferência de produtos
  + - Ocorre através da opção **estorno**
* MATA242 - Desmontagem
  + - Ocorre através da opção **estorno**
* MATA103 - Documento de Entrada
  + - Apontamento de produção em terceiros
      * Ocorre através da opção **excluir**
    - Apontamento de produção conjunta em terceiros
      * Ocorre através da opção **excluir**
* MATA650/MATA650 - Ordem e Apontamento de Produção
  + - Apontamento de Produção
      * Ocorre através da opção **estornar**

Para ilustrarmos, vamos mostrar como um Apontamento de Produção e o seu estorno e como esses movimentos aparecem no Registro K270:

**1 - Validar como está o parâmetro MV\_TMPAD (por padrão vem como 010)**

**![image2018-10-19_17-0-32.png](https://tdn.totvs.com/download/attachments/259560564/image2018-10-19_17-0-32.png?version=1&modificationDate=1540998665250&api=v2)**

**2 - Cadastrar um Armazém (AGRA045).**

**![image2018-10-22_13-56-45.png](https://tdn.totvs.com/download/attachments/259560564/image2018-10-22_13-56-45.png?version=1&modificationDate=1540998754790&api=v2)**

**3 - Cadastrar um produto PA e seu(s) MP(s)  (MATA010).**

**![image2018-10-31_11-20-52.png](https://tdn.totvs.com/download/attachments/259560564/image2018-10-31_11-20-52.png?version=1&modificationDate=1540999253060&api=v2)**

**3. Criar uma Estrutura do PA para os MPs (MATA200).**

**![image2018-10-31_13-47-26.png](https://tdn.totvs.com/download/attachments/259560564/image2018-10-31_13-47-26.png?version=1&modificationDate=1541008046323&api=v2)**

**4 - Criar uma OP para o PA (MATA650).**

**![image2018-11-1_8-40-41.png](https://tdn.totvs.com/download/attachments/259560564/image2018-11-1_8-40-41.png?version=1&modificationDate=1541076041643&api=v2)**

**![image2018-10-31_13-55-18.png](https://tdn.totvs.com/download/attachments/259560564/image2018-10-31_13-55-18.png?version=1&modificationDate=1541008519777&api=v2)**

**![image2018-11-1_8-41-24.png](https://tdn.totvs.com/download/attachments/259560564/image2018-11-1_8-41-24.png?version=1&modificationDate=1541076084277&api=v2)**

**5 - Apontar a Produção (MATA250).**

**![image2018-11-1_8-42-58.png](https://tdn.totvs.com/download/attachments/259560564/image2018-11-1_8-42-58.png?version=1&modificationDate=1541076178263&api=v2)**

**6 - Gerar o SPED para o mês A com a pergunta "Gera Bloco K?" = Sim. (SPEDFISCAL)**

**![image2018-10-31_14-12-18.png](https://tdn.totvs.com/download/attachments/259560564/image2018-10-31_14-12-18.png?version=1&modificationDate=1541009538877&api=v2)**

**7 - Estornar a OP (MATA250)**

**![image2018-11-1_9-22-21.png](https://tdn.totvs.com/download/attachments/259560564/image2018-11-1_9-22-21.png?version=1&modificationDate=1541078542177&api=v2)**

**8 - Gerar o SPED do mês A+1 com a pergunta "Gera Bloco K?" = Sim. (SPEDFISCAL)**

**![image2018-10-31_14-12-18.png](https://tdn.totvs.com/download/attachments/259560564/image2018-10-31_14-12-18.png?version=1&modificationDate=1541009538877&api=v2)**

**9 - Gerar o MATR241 do mês da apuração do SPED (como vamos nos atentar apenas ao K270, deixar as 3 perguntas do relatório como "Não")**

**![image2018-11-1_9-14-15.png](https://tdn.totvs.com/download/attachments/259560564/image2018-11-1_9-14-15.png?version=1&modificationDate=1541078055467&api=v2)**

**Saiba mais:**

*[Documentação completa do Registro K270 - Protheus](http://tdn.totvs.com/pages/viewpage.action?pageId=259560564)*

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
