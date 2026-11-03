---
article_id: 21056972490647
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 5ea02c9680fd80d10fbcca458d732cac4ea11b523a047754d0cd203f9fd143c6
fetched_at: '2026-06-28T22:42:09.161409+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - CONV115/CAT79
  - Erro de validação "MEST 196/MEST 197"
type: support-article
updated_at: '2024-02-02T16:37:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21056972490647-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-CONV115-CAT79-Erro-de-valida%C3%A7%C3%A3o-MEST-196-MEST-197
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21056975237271) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao importar os arquivos magnéticos **CONV115** ou **CAT79**, ocorre os erros de validação:  
*MEST 196-Data de Início da Prestação do Serviço: ano menor que 2003, ou é inválida*  
*MEST 197-Data de Término da Prestação do Serviço: ano menor que 2003, ou incompatív*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21056975238295)  
**Ambiente**Cross Segmentos- TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**Falta de atualização e complementos da NF não preenchidos   
  
**Solução**Para corrigir o erro deve preencher os campos de data nos complementos das NFs (ativas e canceladas) conforme documentação abaixo:  
  
A informação sobre as datas deverá ser fornecida através da rotina de complementos fiscais, conforme a tela abaixo:

![](https://tdn.totvs.com/download/attachments/747325406/image2023-3-30_18-59-43.png?version=1&modificationDate=1680213584187&api=v2)  
![](https://tdn.totvs.com/download/attachments/747325406/image2023-3-30_19-1-18.png?version=1&modificationDate=1680213678507&api=v2)  
 

Para as notas modelo 21 (NTSC) e 22 (NTST):

Ao preencher o campo Ini.pst.serv**(FX\_DTINI)** será alimentado o campo 30(Data de leitura anterior) do arquivo mestre da CAT79 e CONV115.  
Ao preencher o campo Fin.pst.ser**(FX\_DTFIM)** será alimentado o campo 31 (Data de leitura atual) do arquivo mestre da CAT79 e CONV115.

![](https://tdn.totvs.com/download/attachments/747325406/image2023-3-31_9-36-18.png?version=1&modificationDate=1680266178953&api=v2)  
![](https://tdn.totvs.com/download/attachments/747325406/image2023-3-31_9-35-29.png?version=1&modificationDate=1680266130670&api=v2)

È preciso também que o ambiente esteja atualizado com os pacotes abaixo:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049615333-Cross-Segmentos-Backoffice-Protheus-FIS-Atualiza%C3%A7%C3%A3o-do-Ambiente-Fiscal-M%C3%B3dulo-09-Livros-Fiscais?source=search>

Documentação:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=756460574>
