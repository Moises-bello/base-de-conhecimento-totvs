---
content_hash: fd870b66454117134f68f429f097e5652b9cb2cd15f4b622574b33973bc86c14
fetched_at: '2026-06-29T00:08:37.671280+00:00'
page_id: '284880328'
product: rm
source: tdn-rm
title: Customização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284880328
version: 7
---

O novo Portal do Aluno, permite que a instituição realizar a customização das páginas para que o portal fique a cara da instituição. Estão disponíveis, através da parametrização, dois tipos de customização:

* **Customização básica:** envolve a customização de arquivos do CSS global, HTML e imagens;
* **Customização avançada:** envolve a customização de arquivos de Javascript (.js).

Foram criadas variáveis que servem para verificar se o portal irá utilizar a configuração padrão ou páginas customizadas. Essa variáveis estão salvas nos arquivo de configuração "**edu-contantes.global.config.js**" que está disponível através do caminho: "**C:\totvs\CorporeRM\FrameHTML\Web\app\Edu\PortalEducacional\js**". Dentro deste arquivo existe variáveis para cada página do portal. As variáveis por padrão, estarão com o valor **false**, ou seja, o Portal do Aluno irá utilizar as páginas criadas pela TOTVS. Para realizar a customização, primeiramente, devemos alterar o valor das variáveis referente a página que será customizada para **true**. Após a alteração da variável que indica a customização, será necessário a criação de uma pasta com o nome "**custom**", na raiz do caminho da página a ser customizada.

IMPORTANTE 

1. Os arquivos que serão customizados que ficarão contidos nas pastas "**custom**" devem ter o mesmo nome do arquivo original.
2. Alterações nos arquivos da pasta "custom" não são de responsabilidade da TOTVS, pois estão ligadas à customização realizada pelo cliente.

creation
