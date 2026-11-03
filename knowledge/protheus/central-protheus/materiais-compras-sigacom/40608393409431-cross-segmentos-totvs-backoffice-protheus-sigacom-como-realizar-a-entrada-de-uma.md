---
article_id: 40608393409431
category: Materiais - Compras (SIGACOM)
content_hash: f8bc9ccf895a50a81755484028cf19b6ad0cd49e4d260e6d59a22c7748f3d40f
fetched_at: '2026-06-28T22:41:16.012294+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar a entrada
  de uma NFSe Nacional via Documento de entrada
type: support-article
updated_at: '2026-05-20T13:24:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40608393409431-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-entrada-de-uma-NFSe-Nacional-via-Documento-de-entrada
---

⏱ Tempo aproximado para leitura: 00:05:00 min

**Dúvida**  
Como realizar a Implementação para dar entrada em uma NFSe Nacional via Documento de Entrada (MATA103) (Tamanho documento até 15 caracteres)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - 12.1.2510

**Solução**  
  
**Importante:**

Aplicar expedição continua para atualização de dicionário: [Pacotes de Atualização](https://tdn.totvs.com/pages/viewpage.action?pageId=522011099)

Habilitar o parâmetro **MV\_NFSNAUT**  
  
No **Documento de Entrada (MATA103)**, ao inserir um novo documento e informar a espécie NFS, o usuário será questionado se a numeração do documento é maior que 9 caracteres (Default - Padrão Protheus).  
  
Se informar **"Sim"**, a numeração do documento **(F1\_DOC)**, fica desabilitada para edição, pois ao confirmar a geração do documento será gerada uma nova numeração com "T" + Contador (Ex: T00000001) e a numeração que estava no campo **"Numero da NFSe" na DANFSe** deve-se informar no campo **"Numero NF Eletr" (F1\_NFELETR).**  
  
![](https://tdn.totvs.com/download/attachments/897308139/image-2024-12-13_16-26-55.png?version=1&modificationDate=1734118015320&api=v2)

Informou "Sim", campo **"Numero (F1\_DOC)"** desabilitado.  
  
![](https://tdn.totvs.com/download/attachments/897308139/image-2024-12-13_13-48-50.png?version=1&modificationDate=1734108530940&api=v2)  
  
 Deve-se preencher o campo **"Numero NF Eletr (F1\_NFELETR)"**  
  
**![](https://tdn.totvs.com/download/attachments/897308139/image-2026-1-27_11-39-10.png?version=1&modificationDate=1769524750390&api=v2)**  
  
Ao confirmar geração do documento, sera apresentada nova numeração gerada.  
  
![](https://tdn.totvs.com/download/attachments/897308139/image-2024-12-13_13-50-27.png?version=1&modificationDate=1734108627077&api=v2)  
  
**Observação:**Caso não respeite essas regras, usuário será alertado, para preencher corretamente. Ou então informe a espécie novamente "NFS" e selecione a opção **"Não"**, assim deixando o campo (F1\_DOC) disponível para preencher com a numeração desejada pelo usuário.  
  
![](https://tdn.totvs.com/download/attachments/897308139/image-2024-12-13_16-27-43.png?version=1&modificationDate=1734118063713&api=v2)  
  
Se informar **"Não",** a numeração do documento (F1\_DOC), fica habilitada para edição e deve ser a mesma numeração do campo **"Numero da NFSe" na DANFSe.**

Sem informar a série, pois a nota da prefeitura **NÃO**tem série.  
  
![](https://tdn.totvs.com/download/attachments/897308139/image-2026-1-27_11-47-3.png?version=1&modificationDate=1769525223493&api=v2)  
  
Para incluir numeração de prestador de serviço basta preencher o campo F1\_NUMRPS que deve ser informada na **aba "Nota Fiscal Eletrônica".**  
  
**![](https://tdn.totvs.com/download/attachments/897308139/image-2026-1-27_11-59-36.png?version=1&modificationDate=1769525976323&api=v2)**  
  
Para incluir a Data da competência, deve ser informada na **aba "Informações Adicionais"**.  
  
![](https://tdn.totvs.com/download/attachments/897308139/image-2026-1-27_12-2-9.png?version=1&modificationDate=1769526129973&api=v2)  
  
Chave documento **(NFSe Nacional),**deve ser informada na **aba "Nota Fiscal Eletrônica".**

![](https://tdn.totvs.com/download/attachments/897308139/image-2026-1-27_12-3-16.png?version=1&modificationDate=1769526196663&api=v2)  
  
  
***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)  
  
[PCOM12088 - NFSe Nacional - Implementação via Importador XML e/ou Documento de Entrada](https://tdn.totvs.com/pages/viewpage.action?pageId=897308139)  
  
[NFSE ambiente nacional](https://tdn.totvs.com/display/PROT/26021862+DMANMAT02-55252+DT+MATA103+%7C+NFSE+ambiente+nacional)
