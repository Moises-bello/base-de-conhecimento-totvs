---
content_hash: 4752cd7c49cf704487d08b6af7cb31f615770a8ddd24d5a1cb90e7936079222f
fetched_at: '2026-06-29T00:09:04.247759+00:00'
page_id: '382562913'
product: rm
source: tdn-rm
title: 3390181 FISCAL01-5737 DT NFS-e - Regime Especial de Tributação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382562913
version: 2
---

# NFS-e - Regime Especial de Tributação

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Envio - NFS-e |
| **Situação/Requisito:** | O RM está gerando o campo RegimeEspecialTributacao como 50. Ao tentar enviar a nota para  Prefeitura de Guarulhos ocorre a mensagem abaixo: Enviar NFS-e: Erro no envio da NFS-e TSS - Erro na validação desta nota. Element ' <http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd> RegimeEspecialTributacao': Conteúdo do campo não obedece ao Esquema da NFS-e. O valor '50' não é  aceito pelo padrão estabelecido pela SEFAZ: '1|2|3|4|5|6'. |
| **Solução/Implementação:** | Ajustada a Tratativa da tag "RegimeEspecialTributacao" Layout antigo para que quando o Regime Especial de Tributação for "Nenhum" a tag não seja gerada assim como ja e feito no Layout Único. Incluído o Município de Guarulhos no Layout Único. |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Tickets relacionados:** | Não se Aplica |
| **Requisito:** | Não se Aplica |
| **Documento de Referência:** | Não se Aplica |
