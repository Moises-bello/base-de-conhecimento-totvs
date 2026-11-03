---
content_hash: 9ac4f123fc7ef24bcaed76544a7f654de456bfc575998f2c3741b0717bb0a15f
fetched_at: '2026-06-29T00:09:20.111006+00:00'
page_id: '422545668'
product: rm
source: tdn-rm
title: Declaração de Operações Tributáveis - DOT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545668
version: 13
---

De acordo com RICMS, [Art. 762 a 768, aprovado pelo Decreto nº 1.090-R, de 25/10/2002](http://www.sefa.es.gov.br/arquivos/ricms/ricms_1090R.pdf), é obrigado a apresentar a Declaração de Operações Tributáveis - DOT todos os estabelecimentos inscritos no cadastro de contribuintes do imposto, exceto os contribuintes optantes pelo Simples Nacional.

A TAG de que abre o arquivo de importação é <IMPORTAR\_DOTS></IMPORTAR\_DOTS> dentro dela ficará as declarações que serão importadas.   
As informações da declaração ficarão dentro da TAG <DECLARACAO></DECLARACAO>, inclusive os detalhamentos quando houver.   
Já o detalhamento ficará dentro da TAG <DETALHAMENTOS></DETALHAMENTOS> e as informações de cada município ficará dentro da TAG <DETALHAMENTO></DETALHAMENTO>.

**Formato XML do Arquivo:**   
  <?xml version="1.0" encoding="ISO-8859-1"?>   
 <IMPORTAR\_DOTS>   
 <DECLARACAO>   
   ...   
   <DETALHAMENTOS>   
     <DETALHAMENTO>   
         ...   
 </DETALHAMENTO>   
 </DETALHAMENTOS>   
 </DECLARACAO>   
 </IMPORTAR\_DOTS>

---

Embasamento Legal

[Manual de Orientação para Preenchimento da Declaração de Operações Tributáveis - DOT](ftp://ftp.sefaz.es.gov.br/DOT/2015_02_19_manualdeinstrucaoparaopreenchimentodadot_comcfpo.pdf)
