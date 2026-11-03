---
article_id: 360006652632
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 67b679385ad681e3e7e008cb6e01f93d20fcbd40bd14f0807d66221d1927b774
fetched_at: '2026-06-28T22:39:57.482061+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - IMPLANTAÇÃO
  DE NFSE
type: support-article
updated_at: '2026-05-15T18:11:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006652632-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-IMPLANTA%C3%87%C3%83O-DE-NFSE
---

**Dúvida**  
Orientação e documentação para implantação de NFSe no Protheus.

**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões  
  
**Solução**  
**1.** Para as transmissões de NFSE, é necessário verificar se o município da filial que fará as transmissões está homologado no TSS, é possível verificar a relação dos municípios homologados através do link abaixo:  
- [Municípios Homologados](http://tdn.totvs.com/pages/releaseview.action?pageId=4814340)  
  
**2.** É imprescindível que o TSS esteja atualizado de acordo com a última versão disponível no portal do cliente.

- [TSS - Atualização do Appserver (binário) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062416694-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Appserver-bin%C3%A1rio-do-TSS?source=search)  
- [TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)  
- [TSS - Atualização das URLs do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025394911-TSS-Atualiza%C3%A7%C3%A3o-das-URLs-do-TSS)  
- [TSS - Atualização de SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)  
- [TSS - Atualização do TssNewNfse](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16784834285847-Cross-Segmentos-Backoffice-Protheus-TSS-NFSe-Configura%C3%A7%C3%A3o-do-NewNfse)  
  
**3.** Deve ser utilizado o RDMAKE NFSEXMLENV disponível no portal do cliente, que é o responsável pela geração do XML no Protheus. Para a utilização do mesmo é necessário alterar o parâmetro MV\_NFSEMOD deixando-o como .T., segue abaixo o link para download do RDMAKE para NFSE do Protheus 12.  
- 12.1.2410: <https://r.totvs.io/p/1248782> ou 12.1.2510: <https://r.totvs.io/p/1248780>  
  
Para as transmissões, por padrão deverá ser utilizada a rotina **FISA022.**  
  
**4.** Ao acessar a rotina e realizar a configuração do Wizard, o campo versão deve ser preenchido de acordo com a versão do layout do Município, esta informação pode ser consultada na relação de municípios homologados:  
- [Versão Homologada](http://tdn.totvs.com/pages/releaseview.action?pageId=4814340)

Poderá definir o ambiente entre produção e homologação (Tela 4):  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe -Wizard. Config rotina FISA022](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026788652-MP-NFSE-Wizard-Config-rotina-FISA022)

O campo SIAFI, deve ser preenchido o código do município de acordo com o modelo SIAFI, ele pode ser consultado no link abaixo:  
- [Código do Município SIAFI](https://www.cnm.org.br/cms/images/stories/Links/16062014_Codigo_SIAFI_municipio.pdf)

No link abaixo, realize o download do arquivo NOTASELETRONICAS\_Help.rar, esse documento servirá de apoio para implantação.  
- [NOTASELETRONICAS\_Help.rar](http://tdn.totvs.com/pages/viewpage.action?pageId=126191127)

**Seguem abaixo as funcionalidades dentro da rotina FISA022 para NFSE:**  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Transmissão de NFSE (Web Service)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027852711-MP-NFSE-Transmiss%C3%A3o-de-NFSE?source=search)  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Transmissão de NFSE (TXT/XML)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027700172-MP-NFSE-Transmiss%C3%A3o-TXT-XML)  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Substituição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015759732-MP-NFSE-Substitui%C3%A7%C3%A3o?source=search)  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Consulta RPS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015681772-MP-NFSE-Consulta-RPS-?source=search)  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Cancelamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004979372-TSS-NFSE-Cancelamento?source=search)

***IMPORTANTE***  
*Caso durante implantação surjam dúvidas ou erros, solicitamos que realize a abertura de um novo chamado para cada incidente.*

*Conforme nosso Guia de Atendimento, deverá ser registrado apenas UM incidente por chamado, visando agilidade no suporte e histórico do mesmo.*
