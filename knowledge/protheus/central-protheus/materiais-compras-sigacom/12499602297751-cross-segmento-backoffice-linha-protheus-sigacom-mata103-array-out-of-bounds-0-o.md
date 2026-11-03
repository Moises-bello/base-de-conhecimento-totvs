---
article_id: 12499602297751
category: Materiais - Compras (SIGACOM)
content_hash: 24c1bc824fcf18738a3f823b22e0b1cb87f23d65f9f5924e4c04eb5af3e56363
fetched_at: '2026-06-28T22:41:10.613260+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - MATA103 - array out
  of bounds ( 0 of 241 )  on A103FKW(MATA103REINF.PRW)
type: support-article
updated_at: '2024-09-26T14:03:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12499602297751-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-MATA103-array-out-of-bounds-0-of-241-on-A103FKW-MATA103REINF-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25945290503959) Tempo aproximado para leitura: **03:00:00 min****Ocorrência**Ao incluir o documento de entrada com natureza de rendimento ocorre o error.log abaixo:

array out of bounds ( 0 of 241 ) on A103FKW(MATA103REINF.PRW)

**Importante:** O número do cabeçalho do erro ( 0 of **241** )  pode variar de acordo com o dicionario de dados.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.33.  
  
**Causa**Quando o erro "array out of bounds" inicia-se com zero ( **0** of 241 ) geralmente o campo utilizado pelo sistema estar inativo na base de dados. Um dos fatores é devido o campo não estar marcado como **USADO** no configurador, ou existe alguma validação naquele campo que está tornando-o nulo   
  
**Solução**Para solucionar essa ocorrência, solicitamos que acesse o **Configurador** > **Base de Dados** > **Dicionario** > **Base de Dados**:

**Passo 1:** Selecione a empresa que ocorre o erro > Clique em **Dicionario de Dados** > **Clique** na Lupa de pesquisa conforme imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12499225220503)

**Passo 2:** Busque pela tabela SD1 > Clique em Alterar:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12499300820375)

**Passo 3:** Localize os campos descritos abaixo > Clique em **Alterar** > Vá aba "**Uso**" > Marque os campos como "**Usado**":

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12499396859031)

Campos que devem estar marcados como "Usado" e com o nível do campo = "1"  para correção deste erro:

* D1\_VALIRR
* D1\_VALPIS
* D1\_VALCOF
* D1\_VALCSL
* D1\_VALIPI
* D1\_TOTAL
* D1\_BASEIRR
* D1\_BASEPIS
* D1\_BASECOF
* D1\_BASECSL
* D1\_BASEIPI

**Passo 4:** Após marcar todos os campos acima como USADO, clique no **Disquete** para **salvar:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12499524762135)

**IMPORTANTE**:

**1-)** Caso algum dos campos apontados acima **NÃO** exista, solicitamos que atualize os pacotes dos dicionários Completo ( SDS.bra ) e o diferencial completo ( SDF.bra ) disponíveis em nosso portal de download.

**2-)** Se por acaso um dos campos acima não estiver marcado como Usado e, no momento de marcar ao salvar o sistema apresenta o help abaixo :

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12628724394647)

Se o **tamanho** do campo for **14** com **2** **decimais**, **altere** a picture para **@E 99,999,999,999.99** e **salve** a **alteração**.

**OBS.:** Essa validação de picture começou a ocorrer por conta da evolução da LIB que passou a validar o formato ( picture ) dos campos.

**3-)** Lembrando que por padrão, o nível desses campos não pode ser alterado via configurador.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26642670183703)

**Exemplo de uma query executada para verificação e validação dos campos envolvidos nesse erro, considerando a SX3 da empresa 99 ( teste ).**

SELECT X3\_CAMPO, X3\_TIPO, X3\_USADO,X3\_NIVEL FROM SX3990  
WHERE X3\_CAMPO IN ('D1\_VALIRR','D1\_VALPIS','D1\_VALCOF','D1\_VALCSL','D1\_VALIPI','D1\_TOTAL','D1\_BASEIRR','D1\_BASEPIS','D1\_BASECOF','D1\_BASECSL','D1\_BASEIPI'). O resultado obtido nas configurações padrão do sistema, é o abaixo :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26642686834839)
