---
content_hash: 5541e2037ab092dca648a2bd3ed2c4745d29bb89aa146d09061b694743d44220
fetched_at: '2026-06-29T00:09:21.801756+00:00'
page_id: '422545913'
product: rm
source: tdn-rm
title: Atualização de Municípios Homologados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545913
version: 16
---

Através deste processo é possível inserir na base de dados atualizados dos municípios homologados para emissão de NFS-e através da integração do TSS.

Para executar o processo, acesse a visão das NFS-e, e nos processos escolha a opção Atualização de Municípios Homologados.

Imagem

Tela aberta apresenta no quadro da esquerda os municípios gravados na base de dados e no quadro da direita os municípios homologados. Não é necessário selecionar nenhum município. Clique somente no botão executar que os municípios já existentes serão sobrepostos e nos novos gravados.

Imagem

Para que este processo funcione é necessária a configuração da .

Máscara Código Federal

Foi incluído o campo **Máscara Código Federal** por município, que passa a ser sincronizado com a base de dados através do serviço de Mashup, comportamento que não existia anteriormente.

Para sincronizar os dados basta executar o processo de Atualização de Municípios Homologados e as informações serão atualizadas na base.

Este novo campo deve ser parametrizado da seguinte forma:

Opções de Preenchimento da Máscara:

* # - Preenchimento obrigatório do dígito
* Q - Preenchimento do dígito apenas se for maior 0 (Deve ser utilizado somente no primeiro dígito da máscara)

Exemplo das opções de Máscara:

| Código Cadastro do Serviço | Máscara definida na DMUNICIPIONFSE | Valor no XML |
| --- | --- | --- |
| 1.05 | ##.## | 01.05 |
| 1.05 | Q#.## | 1.05 |
| 1.05 | #### | 0105 |
| 1.05 | Q### | 105 |
| 12.05 | ##.## | 12.05 |
| 12.05 | Q#.## | 12.05 |
| 12.05 | #### | 1205 |
| 12.05 | Q### | 1205 |

É necessário que a tabela DMUNICIPIONFSE possua a coluna MASCARACODFEDERAL, ou seja, a base deve estar atualizada.

Disponível a partir da biblioteca 12.1.28

noneAtualização de Município Homologados para NFS-e

648432
