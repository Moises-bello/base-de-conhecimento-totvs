---
article_id: 360050629453
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: a9a8a4c5545c2182e7ed7acbca3f0ef1073a3d7d788f9570b9384fb884e750c4
fetched_at: '2026-06-28T22:39:57.487351+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Implantação
  de NFTS via Webservice
type: support-article
updated_at: '2025-05-29T12:21:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050629453-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Implanta%C3%A7%C3%A3o-de-NFTS-via-Webservice
---

**Dúvida**Orientação e documentação para implantação de NFTS via webservice no Protheus.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**

**1.** É importante verificar se o município está homologado para transmissão de NFTS via webservice:  
- [Municípios Homologados NFTS](https://tdn.totvs.com/pages/releaseview.action?pageId=172300900)

**2.** É imprescindível que o TSS esteja atualizado de acordo com a última versão disponível no portal do cliente:  
- [TSS - Atualização do Appserver (binário) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062416694-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Appserver-bin%C3%A1rio-do-TSS?source=search)  
- [TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)  
- [TSS - Atualização das URLs do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025394911-TSS-Atualiza%C3%A7%C3%A3o-das-URLs-do-TSS)  
- [TSS - Atualização de SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)

**3.** Deve ser utilizado os RDMAKES NFSEXMLENV e NFSEXML102 disponíveis no portal do cliente, que é o responsável pela geração do XML no Protheus. É necessário alterar o parâmetro MV\_NFSEMOD deixando-o como .T., segue abaixo o link para download dos RDMAKES para NFSE do Protheus 12.  
-[Rdmake NFSEXMLENV](https://suporte.totvs.com/portal/p/10098/download#detail/1083728)

**4.** O documento de entrada deve ser gerado com espécie NFS;  
É importante verificar se a emissão do documento gerou as tabelas CD2, SF3 e SFT;

**5.** Sugerimos a emissão do documento de entrada com formulário próprio=SIM, pois dessa forma, se houver a necessidade de cancelar a nota, não encontrará problemas na transmissão conforme detalhamos no link abaixo:

**-**[Cancelamento de NFTS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018405192-TSS-NFSE-Cancelamento-de-NFTS)

**6.** Configure o parâmetro MV\_NFTOMSE:  
- [MV\_NFTOMSE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028760652-MP-NFSE-Configura%C3%A7%C3%A3o-do-MV-NFTOMSE)

**7.** Utilize a rotina FISA022 para transmissão da NFTS.  
Selecione o Tipo de NFS-e = 2-Entrada:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076533353)

**Artigos relacionados:**

**-**[Nenhuma Nota Transmitida - NFTS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047528993-MP-NFSE-Nenhuma-Nota-foi-Transmitida-Entrada-)  
**-**[Cancelamento de NFTS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018405192-TSS-NFSE-Cancelamento-de-NFTS)
