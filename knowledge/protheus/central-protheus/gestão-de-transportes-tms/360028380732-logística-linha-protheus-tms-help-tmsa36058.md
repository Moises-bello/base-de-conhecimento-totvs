---
article_id: 360028380732
category: Gestão de Transportes (TMS)
content_hash: cf31ccbb4dedcb5e339f6e4f5785d765d6f2c53805452d1ddb77d1066edbf620
fetched_at: '2026-06-28T22:45:29.287959+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - HELP TMSA36058
type: support-article
updated_at: '2022-06-20T17:33:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028380732-Log%C3%ADstica-Linha-Protheus-TMS-HELP-TMSA36058
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como resolver o *help***TMSA36058** ao estornar uma ocorrência?   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões

**Solução**O *help***TMSA36058** **- Só será permitido o estorno de solicitação diferente de Documento Informado** é exibido ao tentar estornar uma ocorrência da viagem de coleta em que a coleta já tenha sido utilizada para gerar um documento. Sendo esse o caso, esse documento deve ser estornado.  
  
Segue procedimento:  
  
*Help***TMSA36058** foi exibido.

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360029101671/Capturar.PNG)

Deve-se visualizar a viagem de coleta a qual deseja estornar a ocorrência e visualizar a coleta vinculada. **Anote a filial do documento e número do documento** para que seja possa buscar um documento vinculado a esta coleta.

![Capturar1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360029101691/Capturar1.PNG)

Na rotina **TMSA050 - Entrada Documentos Cliente**, encontrada no menu **Atualizações/Recebimento/Entrada Documentos Cliente**, deve utilizar a barra de busca para buscar algum documento vinculado a coleta. Utilize o índice de **Filial Origem + Número da solicitação da coleta**, conforme destacado na imagem.

![Capturar2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360029101731/Capturar2.jpg)

Efetue a busca e, para confirmar, visualize o documento e veja se a coleta em questão é a mesma que está no campo **Número da Solicitação de Coleta**.

![Capturar3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360029099652/Capturar3.PNG)

Com o documento devidamente identificado, deve-se efetuar o estorno do cálculo do documento em **Outras Ações/Cálculo Frete/Estornar**, efetuar a transmissão do Cancelamento para a **SEFAZ - Secretaria de Estado da Fazenda**, caso tenha sido transmitido o envio, e estornar o documento em **Outras Ações/Estornar**.  
  
Com o documento estornado, o sistema permite efetuar o estorno da ocorrência.

![Capturar4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360029099672/Capturar4.PNG)

![Capturar5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360029101751/Capturar5.PNG)

**Importante**Caso esse documento tenha sido vinculado à uma viagem de entrega, deve-se efetuar o estorno de todo o processo da viagem de entrega.
