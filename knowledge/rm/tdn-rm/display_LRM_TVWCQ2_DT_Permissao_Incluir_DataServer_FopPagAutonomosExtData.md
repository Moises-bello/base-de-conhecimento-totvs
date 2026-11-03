---
content_hash: bf551aa77e5680baaeae8491a93307df4ee92d6a27d9c1a3594e9103c8661cf2
fetched_at: '2026-06-29T00:08:18.914187+00:00'
page_id: '266976752'
product: rm
source: tdn-rm
title: TVWCQ2_DT_Permissao_Incluir_DataServer_FopPagAutonomosExtData
type: documentation
url: https://tdn.totvs.com/display/LRM/TVWCQ2_DT_Permissao_Incluir_DataServer_FopPagAutonomosExtData
version: 116
---

# WEBSERVICE AUTÔNOMOS EXTERNOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *WebService Autônomos Externos* |
| **Situação/Requisito:** | Cliente realiza a Integração do BackOffice SAP com o RM, portanto o Cliente utiliza o WebService FopPagAutonomosExtData para inserir dados na tabela PPAGTOAUTONOMOEXT onde será levado na SEFIP os dados dos Autônomos Externo.  Porém ao executar o SaveRecord via SOAP UI no DataServer FopPagAutonomosExtData, é retornado a mensagem Você não está autorizado a alterar registros! Mesmo o usuário já tendo permissão em todos Perfis. |
| **Solução/Implementação:** | *Alterado a segurança do dataServer FopPagAutonomosExtData para permitir incluir/remover/editar.* |
| **Chamados relacionados:** | *TVWCQ2* |

divs
