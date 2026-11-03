---
content_hash: 733d0fb226ae25d2f0ac7f1ff1a5a915d52c92e065b4f6d93b4b56f6c8c48cab
fetched_at: '2026-06-29T00:08:31.690300+00:00'
page_id: '273305890'
product: rm
source: tdn-rm
title: Alteração da página principal do Portal Web
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273305890
version: 3
---

# Alterar a página principal do portal web

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.XX ; 12.XX |
| **Ocorrência:** | Alterar a página principal do Portal Web |
| **Ambiente:** | Portal WEB - Gestão de Conteúdos |
| **Passo a passo:** | É possível alterar a página principal do Portal Web, porém qualquer alteração efetuada nos códigos será de total responsabilidade do cliente.  Recomendamos neste caso, um programador web para efetuar as alterações e / ou customizações necessárias  Página Inicial:    As imagens estão localizadas nos seguintes diretórios:  C:\totvs\CorporeRM\Corpore.Net\Images\login  C:\totvs\CorporeRM\Corpore.Net\Images\  Para alterar via código, deverá ter conhecimento nas extensões css.  Como exemplo, para alterar ou redirecionar o “**moresocialmorebusiness”** localize o arquivo style.css (C:\totvs\CorporeRM\Corpore.Net\Styles).  Neste arquivo terá as informações das imagens e redirecionamento das mesmas.   xmlstyle.csstrue   Para eliminar / retirar os links Currículo, Cotação On-line, Executor web e etc, será através do arquivo web.config (C:\totvs\CorporeRM\Corpore.Net) para as tags: Valor falso irá retirar o link do portal  \*\*Este procedimento continua o mesmo das versões anteriores   xmlweb.configtrue                                                                                                                                                                                                                                                                                                                                                                                                ]]>     Para retirar os itens como Perfil, segurança, Mobilidade e etc, será através do arquivo login.aspx (C:\totvs\CorporeRM\Corpore.Net) através do código.  Ex:   xmllogin.aspxtrue Perfil  Segurança  Mobilidade  Produtividade  Integração  Rede de empresas  Quer saber mais sobre                           ]]>   Alterar a cor da fonte dos menus da tela de login do RM Portal. Segue abaixo um exemplo, onde foi alterada a cor da fonte de azul para vermelho.  Acesse o caminho C:\totvs\CorporeRM\Corpore.Net\Styles  Edite o arquivo style.css, no bloco "box-formulario-login", alterando a cor de azul para vermelho:    **Conteúdo original:**   xmlstyle.csstrue       **Conteúdo alterado:**   xmlstyle.csstrue       Para alterar a cor do fundo do RM Portal, poderá alterar a imagem fwstd\_bg.png (C:\totvs\CorporeRM\Corpore.Net\Images\login), conforme exemplo abaixo:  Tela login default:    Tela Login alterada: |
| **Observações:** | Não prestamos suporte à customizações no RM Portal**.**  Alertamos novamente que os exemplos e / ou caminhos citados acima podem ser alterados, onde a total responsabilidade é do cliente, onde recomendamos um programador web ou TI da sua empresa.  Qualquer erro apresentado nesta tela devido à alteração, o suporte irá solicitar a reinstalação do produto sem a obrigatoriedade de localizar ou acertar os códigos alterados. |
