---
content_hash: ac6e4ae1a6dcb7364300d498578598f2d2c97adb4d84fdf2356e46bcedd153de
fetched_at: '2026-06-29T00:08:31.759739+00:00'
page_id: '273308508'
product: rm
source: tdn-rm
title: Reinstalação ou instalação do LICENSE SERVER com HARDLOCK
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273308508
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.XX; 12.01.XX |
| **Ocorrência:** | **Orientações para reinstalação/instalação - Hard Lock** |
| **Ambiente:** | License Server - Hard Lock |
| **Passo a passo:** | Baixe o instalador do License Server do link abaixo:  <https://suporte.totvs.com/portal/p/10098/download-license-publico>       1 - Acessar a máquina antiga ou atual no diretório UNIDADE:\TOTVSLicense\BIN e fazer o backup dos arquivos de licenças totvslic.key e applylic.key;     2 - Se for na mesma maquina, Remover o License Server pelo painel de controle do Windows; (senão for a mesmo maquina execute item 8)     3 - Remover o diretório UNIDADE:\TOTVSLicense     4 - Excluir os serviços do DEP ( appserver e totvsappserver) tópico  1.8 do manual     5 - Reinicializar a máquina. (Verifique se os serviços foram excluídos, senão refaça passo 4)     6 - Proceder novamente com a instalação do License Server seguindo as instruções contidas no manual de instalação em anexo ao chamado.     <http://tdn.totvs.com/pages/releaseview.action?pageId=59900121>     7 - Após aplicação dos arquivos de licenças, você deverá iniciar o serviço .TOTVS LICENSE SERVER.          8 - Proceda com a instalação conforme manual no link abaixo:     <http://tdn.totvs.com/pages/releaseview.action?pageId=59900121> |
| **Observações:** | Este procedimento já está com link correto para baixar o instalador. |
