---
article_id: 4415235211799
category: TAF - REINF
content_hash: b62f07e9237069b6a5777b1e2b9182938411cb4d09b83d61102d27558aee8342
fetched_at: '2026-06-28T22:41:34.612174+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Configuração Painel Reinf
  utilizando MPP - Porta Multiprotocolo
type: support-article
updated_at: '2023-10-09T17:23:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415235211799-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Configura%C3%A7%C3%A3o-Painel-Reinf-utilizando-MPP-Porta-Multiprotocolo
---

**Dúvida**Como configurar o Painel Reinf (TAF do Futuro) utilizando porta Multiprotocolo?  
  
**Ambiente**A partir de 12.1.33  
  
**Solução**

**A TOTVS recomenda que seja utilizada a Porta Multiprotocolo** para uso do TAF do Futuro, dessa forma apenas com uma atualização simples é possível ter acesso as rotinas novas disponibilizadas no produto.

Nesta configuração, **não é utilizado** nem REST, nem HTTP, nem os parâmetros MV\_BACKEND e MV\_GCTPURL, parâmetros devem ficar vazio!

1º - Dentro do TAF, pressione as teclas "SHIFT+F6", será aberta uma interface conforme abaixo.

Valide se a versão do "Appserver version" é igual a superior a **19.3.0.X**, no exemplo abaixo a versão do servidor de aplicação do TAF  é a "19.3.1.7":

![](https://tdn.totvs.com/download/attachments/528452172/image2021-11-26_16-4-37.png?version=1&modificationDate=1637955981427&api=v2)

Caso a sua versão do item acima esteja desatualizada é necessário realizar a atualização do binário e também do TAF:

**Binário**:

AppServer: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/appserver>

Smartclient: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/smartclient>

[Procedimento para atualizar o binário do Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=224123650)

**TAF**:

[MP - TAF - REINF - Atualização Completa REINF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026673572-MP-TAF-REINF-Atualiza%C3%A7%C3%A3o-Completa-REINF?source=search)

2º - Após as atualizações acima, será necessário acessar o appserver.ini da aplicação (ou seja, o appserver.ini onde o Smartclient é iniciado) e incluir as seguintes chaves nas seções:

Em ambiente com broker ou balanceamento a configuração deve ser realizada em todos appserver.ini

Chave **app\_environment** contendo o nome do seu ambiente, no exemplo abaixo, no ambiente com o nome TAF:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415230402327)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415251722391)

OBS: Caso as chaves acima sejam configuradas em um appserver.ini separado (onde não é acessado o Smartclient), poderão ocorrer erros.

Seguindo exatamente os passos acima o seu ambiente do Automação Fiscal já estará apto a acessar os novos painéis em PO UI.

Exemplo de um arquivo appserver.ini do Automação Fiscal utilizando a porta MPP na release 33**, este arquivo deve ser utilizado apenas como consulta e nunca deve ser utilizado para substituir o "appserver.ini" vigente de seu ambiente:**

![](https://tdn.totvs.com/download/attachments/528452172/image2021-11-26_16-40-53.png?version=1&modificationDate=1637955981507&api=v2)

**Importante**:

* Não pode haver mais de um ambiente na chave app\_environment, se houver a necessidade de configurar mais de um ambiente deve ser utilizando REST e HTTP contido no link: [TAF – REINF - Configuração Painel Reinf - Appserver](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409133202199-TAF-REINF-Configura%C3%A7%C3%A3o-Painel-Reinf-Appserver?source=search)
* Quando o acesso ao ambiente com porta multiprotocolo habilitado é feito fora do servidor de aplicação é necessário que as estações que irão acessar esse ambiente (smartclients) possuam um certificado TOTVS instalado. O certificado TOTVS precisa ser gerado dentro do servidor, conforme o passo a passo descrito nessa documentação: [Porta Multiprotocolo - Geração de Certificado](https://tdn.totvs.com/pages/viewpage.action?pageId=548376390), utilizando o executável totvs\_certificates.exe.
* Após essa geração, os certificados gerados devem ser copiados tanto para os appservers dentro do servidor e também para a pasta do smartclient que vai acessar o ambiente e aí sim, efetuar a instalação do certificado (somente nas estações, no servidor não é necessário instalar), conforme link a seguir [Porta Multiprotocolo - Geração de Certificado.](https://tdn.totvs.com/pages/viewpage.action?pageId=548376390) Caso essa configuração não seja efetuada, será apresentado o erro ao iniciar o painel reinf ou o ambiente como "não foi possível acessar esse site - err\_cert\_common\_invalid"

Para mais informações, acesse:

<https://tdn.totvs.com/pages/releaseview.action?pageId=528452172>

<https://tdn.totvs.com/pages/releaseview.action?pageId=641441402>
