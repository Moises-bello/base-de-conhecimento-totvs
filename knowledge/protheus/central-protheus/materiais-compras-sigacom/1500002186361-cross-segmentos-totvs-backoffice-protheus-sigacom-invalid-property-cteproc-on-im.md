---
article_id: 1500002186361
category: Materiais - Compras (SIGACOM)
content_hash: 7cd45519487bc0ed72975b0834cc0a64efabb856205bd79897b7ac2a590d54c9
fetched_at: '2026-06-28T22:41:20.011132+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - invalid property _CTEPROC
  on IMPORTCOL(COMXCOL.PRW) ao executar o SCHEDCOMCOL
type: support-article
updated_at: '2024-06-13T17:20:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002186361-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-invalid-property-CTEPROC-on-IMPORTCOL-COMXCOL-PRW-ao-executar-o-SCHEDCOMCOL
---

**Ocorrência**Erro invalid property \_CTEPROC on IMPORTCOL(COMXCOL.PRW) ao executar o SCHEDCOMCOL  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as Versões

**Causa**

Ao executar as rotina SCHEDOCOMCOL após o registro na tabela CKOCOL o erro é exibido:

![](https://p23.zdusercontent.com/attachment/888110/hYGSCo5Mga90Iee6GHt1XxrKi?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..IvMkyuyWHro1WPgy7AuhTw.kq_YK19eIdSqegm5gYqS3YDqvL0Awx0WghfWQQAJPya0bUjkf7LeB8pa-B9KFV5qw01YhjBITFralyN8D7CWUyVjtbsO358ZPO1sK_z8F5x3WnaFXq-8xOT_aCaf-DTwMhxr8Z3kTROGZqoV_pxJsbcf9avm6Qun2KL09_48wg80Rry2k6G_GmuZx8m3VBHzd1hEiaTrMKrcHfsDOVpHsKMkGb1KRpsdp20gmjN3KL7micfCMsJYDHjBWrRFKtC0EfA9QgVhOtOTovoTBAmIbOpFn-dBAyLt_j1dUWwZU18.VB07j71_13TSiOtXvf-sug)

**Solução**

O erro ocorre devido a existência de algum registro divergente na tabela CKOCOL.  
  
Alguns registros na tabela CKOCOL com o campo CKO\_FLAG = "0" pode estar direcionado a um XML divergente, com isso o erro é exibido.

Procedimento para Ajuste:

Deve-se parar o serviço do importador/colaboração, criar um Backup da tabela CKOCOL, e após realizar este processo, recriar a tabela CKOCOL, inclua os arquivos um de cada vez executando o processo.

***Obs:***

Caso efetuar o append o erro voltará a ser exibido, por isso deve incluir apenas os arquivos XML's pontuais para importação.

***Saiba Mais:***

* [Pontos de Entrada disponíveis nas funções](http://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)
* [Parâmetros Envolvidos](http://tdn.totvs.com/pages/releaseview.action?pageId=485869217)
* [Tabelas e rotinas](http://tdn.totvs.com/pages/releaseview.action?pageId=485869224)
* [Códigos de Erros](http://tdn.totvs.com/pages/releaseview.action?pageId=485869227)
* [Diferenças TOTVS Colaboração e Importador XML](http://tdn.totvs.com/pages/releaseview.action?pageId=501478281)
* [Importador XML ou Totvs Colaboração: Como executar as funções de carga SEM utilizar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-MP-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-schedule)
* [Pontos de Entrada](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
