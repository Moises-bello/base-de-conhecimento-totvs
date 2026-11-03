---
article_id: 8582346381079
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: cecb6c4820d48b6338052fc265b45a1c7414d74588e23867466023790acbe5c0
fetched_at: '2026-06-28T22:42:08.882865+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS -   Arq. Magnéticos -  Como informar
  o IVA na CAT207?
type: support-article
updated_at: '2022-09-01T17:19:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8582346381079-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-informar-o-IVA-na-CAT207
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como informar o **IVA** na **CAT207**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**O **IVA - Índice de Valor Acrescido** é estabelecido de acordo com o **CNAE**  da empresa e  deve ser informado no **Protheus** de acordo com as informações disponibilizadas pela **SEFAZ.**  
   
![](https://totvssuporte.zendesk.com/attachments/token/mpGQ1seiwewafYmio2ioK5QQ1/?name=image.png)  
   
Ou seja, a própria **SEFAZ** disponibiliza uma tabela informando qual deve ser o **IVA**, quando o utilizado na empresa for menor que o da tabela.   
   
Abaixo, *link* com  um exemplo da tabela, (lembrando que se trata apenas de um exemplo, ficando o contribuinte responsável por verificar se há versão mais atualizada da tabela) na qual o fiscal da empresa deve avaliar qual **IVA** se encaixa em suas atividades.  
   
[ttps://legislacao.fazenda.sp.gov.br/Paginas/ccat082010.aspx](https://legislacao.fazenda.sp.gov.br/Paginas/ccat082010.aspx)  
   
Após identificar essa informação, é possível informá-la de duas formas no **Protheus:**  
 

**1**. **Campo  IVA Utilizado (F4\_IVAUTIL)** no qual  é possível informar o percentual.

   
O campo **IVA Utilizado - F4\_IVAUTIL** conterá o Índice de valor acrescido considerado no cálculo do custo estimado da operação ou prestação geradora. 

Informando o **IVA** no cadastro de **TES**, o percentual será gerado nos registros com base nas operações que utilizarem o cadastro de **TES** em questão.  
  
**2. Parâmetro MV\_IVAUTIL**

Esse parâmetro foi criado para os casos em que a empresa gerar a **CAT207** para mais de uma filial e para as quais cada uma possuir um **CNAE** diferente e consequentemente **IVAs distintos** sendo o cadastro de **TES compartilhado entre as filiais.**

Assim, informando o conteúdo no parâmetro não é necessário criar vários cadastros de **TES**: um para cada operação, conforme descrito no *link* abaixo:

 <https://tdn.totvs.com/pages/releaseview.action?pageId=645477505>  
   
**Importante**:

Fica a critério do cliente avaliar se a informação será preenchida no **campo** ou no **parâmetro** de acordo com o cenário.  
   
Havendo informação tanto no **campo** quanto no **parâmetro**, será  utilizado o conteúdo do **parâmetro** para geração da **CAT207**.
