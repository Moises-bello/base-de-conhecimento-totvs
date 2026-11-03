---
article_id: 360028569572
category: Materiais - Compras (SIGACOM)
content_hash: 21bc100269c5e5b390591afbe40f0ce06286f779f145ab706bd7c2947457b62e
fetched_at: '2026-06-28T22:41:18.934072+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help MSDOCOPEN - Não
  foi possível abrir o objeto o preview do banco de conhecimento no Windows 10
type: support-article
updated_at: '2022-05-18T21:01:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028569572-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-MSDOCOPEN-N%C3%A3o-foi-poss%C3%ADvel-abrir-o-objeto-o-preview-do-banco-de-conhecimento-no-Windows-10
---

**Dúvida**

Help MSDOCOPEN - Não foi possível abrir o objeto o preview do banco de conhecimento no Windows 10

**Ambiente**Protheus – Compras – A partir da versão 12.1.7]  
  
**Solução**

Como utilizar o preview do banco de conhecimento no Windows 10?

(Inconsistência "MSDOCOPEN - Não foi possível abrir o objeto" quando não executado como administrador)

O botão Preview do Banco de Conhecimento (FATA340) do Protheus utiliza a classe "TOleContainer" para apresentação do preview do documentos dentro do Protheus. Segundo documentação desta, para solução do problema, pode-se utilizar um usuário administrador do computador para a instalação do TOleContainerInstaller no diretório de instalação do binário smartclient utilizado:

"A partir da build 7.00.131227A - 13.2.3.25 um usuário com permissão de administrador poderá executar o instalador TOleContainerInstaller (disponível na mesma pasta do binário SmartClient) que fará o registro da dependência (DLL) do componente TOleContainer. Uma vez instalado, o componente não mais necessitará da permissão de Administrador, podendo ser executado por qualquer usuário."

A classe "TOleContainer" possui observações específicas sobre a aplicação:

![](http://tdn.totvs.com/download/attachments/344473822/image2018-3-13_15-58-41.png?version=1&modificationDate=1520967917000&api=v2)

Link com vídeo demonstrativo:

<http://tdn.totvs.com/pages/releaseview.action?pageId=344473822&preview=/344473822/344473862/Teste%20TOleContainer.zip>

***Saiba Mais :***

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
