---
content_hash: cd1616ba383a0c45c8c32cfe2f875808f3408581246d5403bd146e2cca99d29a
fetched_at: '2026-06-29T00:08:37.878907+00:00'
page_id: '284884343'
product: rm
source: tdn-rm
title: Customização Avançada.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284884343
version: 9
---

Após Instalar o TOTVS RM Portal deverá ser realizado os passos abaixo:

Dica

Esse passo a passo é válido para customizar as páginas, o CSS global e as imagens, porém cada um dos arquivos serão encontrados em suas respectivas pastas com já citado anteriormente.

Informação

Para as views que possuem arquivos (.html) diferentes entre os níveis de ensino Básico e Superior, existem variáveis específicas para definir qual nível de ensino será customizado. As variáveis que terminam com \_EB representam o nível de ensino básico.

No exemplo abaixo, vamos customizar a página de Login.

**1º-**Edite o arquivo "edups-constantes.global.config.js" com algum editor de sua preferência e altere o valor da variável referente ao Login para **true**.

**2º -** O template default se encontra no caminho: "C:\totvs\CorporeRM\FrameHTML\Web\app\Edu\PortalProcessoSeletivo\js\templates". Crie uma pasta com o nome "custom" e faça uma cópia do template referente a página que será customizada para a pasta criada.

Avisos Importantes

1. Os arquivos que serão customizados que ficarão contidos nas pastas CUSTOM devem ter o mesmo nome do arquivo original.
2. Alterações nos arquivos da pasta CUSTOM não são de responsabilidade da TOTVS, pois estão ligadas à customização realizada pelo cliente.

Cada variável está relacionada à um ou mais arquivos, de acordo com a lista a seguir:

* EDUPS\_CONST\_GLOBAL\_CUSTOM\_VIEW\_PORTAL\_CANDIDATO
  + centralcandidato-eb-list.view.html
  + centralcandidato-es-list.view.html
* EDUPS\_CONST\_GLOBAL\_CUSTOM\_VIEW\_INFORMACOES
  + informacoes-eb-list.view.html
  + informacoes-es-list.view.html
* EDUPS\_CONST\_GLOBAL\_CUSTOM\_VIEW\_RESULTADOS
  + resultados-eb-list.view.html
  + resultados-es-list.view.html
* EDUPS\_CONST\_GLOBAL\_CUSTOM\_VIEW\_INSCRICOES  
  + inscricoes-eb-comprovante.view.html
  + inscricoes-eb-confirmacao-list.view.html
  + inscricoes-eb-edit.view.html         (até a versão 12.1.23)
  + inscricoes-eb-list.view.html           (até a versão 12.1.17)
  + inscricoes-eb-wizard.view.html     (a partir da versão 12.1.24)
  + inscricoes-es-comprovante.view.html
  + inscricoes-es-confirmacao-list.view.html
  + inscricoes-es-edit.view.html          (até a versão 12.1.23)
  + inscricoes-es-list.view.html            (até a versão 12.1.17)
  + inscricoes-es-wizard.view.html      (a partir da versão 12.1.24)
* EDUPS\_CONST\_GLOBAL\_CUSTOM\_VIEW\_LOGIN

  + login.edit.view.html
  + loginautomatico.edit.view.html

Sendo assim, ao alterar alguma variável para "true", todos os arquivos relacionados a ela, sendo mesmo nível de ensino, devem ser movidos para a pasta "custom", e não apenas o arquivo editado.

**3º -** Edite o arquivo na pasta CUSTOM e realize as alterações de acordo com a sua preferência. Este arquivo está em linguagem HTML.

**Tela Original:**

**Tela Customizada:**

Dica Importante

Ao desinstalar o Portal RM de sua máquina, as pastas 'custom' que foram criadas NÃO serão apagadas do seu diretório, ou seja, seus arquivos customizados continuaram salvos no diretório.
