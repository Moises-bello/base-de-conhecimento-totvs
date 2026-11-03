---
content_hash: edd48deefa8246d8b993efeaf26c1feb33239d754d27bff2280b50b2e3dea7ae
fetched_at: '2026-06-29T00:08:24.694931+00:00'
page_id: '270900298'
product: rm
source: tdn-rm
title: Configuração de permissão RELVIEWER
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270900298
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | RM |
| **Versões:** | 11.80 / 12.1.XX |
| **Ocorrência:** | Permissão RMRELVIEWER |
| **Ambiente:** | Gerador de relatórios Delphi/Framework |
| **Passo a passo:** | A mensagem “Failed to set data for”,    Apresentada ao gerar qualquer relatório do gerador de relatórios Delphi através de algum processo, como por exemplo Impressão de documentos do TOTVS Gestão de Estoque, Compras e Faturamentos, se refere a privilégios que devem ser concedidos a aplicação RM\_REL\_Viewer.exe assim que a mesma é executada. Para alterar o nível de privilégio da aplicação siga os passos abaixo:  Localização do arquivo: o arquivo se encontra na seguinte pasta: **\totvs\CorporeRM\RMRelViewer\ RM\_REL\_Viewer.exe**  1)      Acesse as propriedades do aplicativo e na aba “Compatibilidade” marque a opção “Executar este programa como administrador” conforme abaixo:        2)   Clique no botão “Alterar configurações de todos os usuários” e também marque a opção “Executar este programa como administrador” conforme abaixo:            Ao realizar esse procedimento, o erro não será apresentado ao gerar o relatório através da visão. |
| **Observações:** |  |

**Configuração RELVIEWER**
