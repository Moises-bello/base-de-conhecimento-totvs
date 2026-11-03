---
content_hash: 8ae6e5429d5db679174395260244b0d2125a8f5fa6a4e7f257f1f50efdd30b27
fetched_at: '2026-06-29T00:08:18.583831+00:00'
page_id: '265782235'
product: rm
source: tdn-rm
title: TVU958_DT_Erro_Log_Sefip
type: documentation
url: https://tdn.totvs.com/display/LRM/TVU958_DT_Erro_Log_Sefip
version: 113
---

# GERAÇÃO SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Cosntruções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração de Sefip* |
| **Situação/Requisito:** | * Com a base prametrizada para trabalhar com o tomador do tipo Cessão Mão de Obra. Mesmo após o sistema retornar a mensagem que as linhas do arquivo selecionado, após marcar o flag Importar valores de retenção de outro Sistema (Lei 9711/98), foram importadas com sucesso, ao editar o arquivo SEFIP.RE o valor não é apresentado no Registro 20 na posição 243 a 257. Mesmo que no arquivo importado exista uma linha que o tomador é o mesmo que esta sendo recolhido em uma das chapas selecionadas, o valor não é apresentado no arquivo. * No logo do sistema totaliza um número maior de funcionários gerados. |
| **Solução/Implementação:** | * *O arquivo informado não está seguindo a regra para importação. O mesmo encontra-se com o tomador igual ao do funcionário, mas o CNPJ diferente, impossibilitando a importação. O arquivo de importação deve conter o CNPJ e o TOMADOR igual ao de pelo menos um dos funcionários selecionados para ser possível efetuar a retenção.* * *Foi ajustado o contador de funcionários para SEFIP geradas por Tomador.* |
| **Chamados relacionados:** | *TVU958, TVVZBS* |

divs
