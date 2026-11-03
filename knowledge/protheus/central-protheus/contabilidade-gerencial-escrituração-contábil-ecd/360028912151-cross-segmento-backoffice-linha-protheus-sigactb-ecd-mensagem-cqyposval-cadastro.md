---
article_id: 360028912151
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 006a29c915644c43947c52daf0568ced3e148a9b671403fe14fddfaab6aade86
fetched_at: '2026-06-28T22:40:44.786109+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB ECD - Mensagem CQYPOSVAL
  cadastro K300
type: support-article
updated_at: '2023-11-13T15:44:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028912151-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-Mensagem-CQYPOSVAL-cadastro-K300
---

**Ocorrência**A soma dos valores a eliminar no *Grid*dos Itens*(*campo **Valor Elim.***),*mesmo possuindo o mesmo valor informado no campo**Valor Elimin** do cabeçalho, apresenta a mensagem **CQYPOSVAL**("O valor absoluto das eliminações (K300 - campo "**Valor Elimin**") e a soma das parcelas do valor eliminado total (painel K310), devem ser iguais.").

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047254993)**

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 12.1.17  
   
  
 **Solução**Este problema ocorre devido a uma condição interna do servidor de aplicação do **Protheus**, em sua base de **32 bits**, para valores numéricos com muitas casas decimais. Para trabalhar com uma precisão mais apurada de tais valores numéricos é imprescindível habilitar o parâmetro "*FloatingPointPrecise"*(deixando com o valor igual a 1). Este parâmetro deverá ser informado no arquivo de configurações do sistema (**appserver.ini**) dentro do grupo **[General]**.

[5902279 DSERCTR1-21354 DT Mensagem CQYPOSVAL cadastro K300](https://tdn.totvs.com/display/public/PROT/5902279+DSERCTR1-21354+DT+Mensagem+CQYPOSVAL+cadastro+K300)
