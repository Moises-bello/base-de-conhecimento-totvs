---
content_hash: aeefac77d88a20f627c466de8f72556da3e5432c9dbe11cfc9dc081df8475d17
fetched_at: '2026-06-29T00:10:21.942655+00:00'
page_id: '494975180'
product: rm
source: tdn-rm
title: MATESTCNTFTOF01-5609 Atualização de entidade e source code
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=494975180
version: 4
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | BackOffice |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** | Integração EAI 1.0 |
| **Situação/Requisito:** | Necessidade de atualização da entidade, do source code ou de ambos. |
| **Solução/Implementação:** | Informe a solução/implementação. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |

## Atualização de entidades do EAI 1.0

Após configurar integração “Mensagem Única” EAI 1.0 - e o mapeamento das entidades utilizadas, pode ser necessário atualizar a versão da entidade, do source code utilizado pela entidade ou mesmo a versão da entidade e do source code.

## Passo-a-passo para atualização de um source code

1. Acessar o módulo integrações:

2. Acessar grupo “**Integração**” => Menu “**Mensagem Unica**” => Item de menu “**Integrações**”

Vai ser exibido a visão de menagem única com as integrações configuradas, observe filtro aplicado

3. Na visão da mensagem única acesse “**Anexos**” => “**Mapeamento de Entidades**”

As entidades configuradas serão exibidas no anexo junto a sua versão, edite a entidade que deseja atualizar o Source Code.

4. Na imagem abaixo temos a entidade “REQUEST” e em Eventos o Source Code, clique sobre “Request\_1\_009” para editar o source code.

5. Ao abrir a janela “Cadastro de códigos fontes” clique em excluir para remover o source code.

6. Com o source code removido execute novamente o configurador, a última versão do source code vai ser criada e vinculado novamente a entidade.

As novas versões são liberadas junto com as bibliotecas atualizadas de “Biblioteca RM”, então lembre de estar com a versão atualizada para ter acesso ao source code atualizado.

## Passo-a-passo para atualização de uma entidade

Seguir os mesmos passos para atualização do source code.

* Se o source code é customizado e não deseja atualizar o source code, após o passo 4 ao invés de acessar o source code e excluir deve-se apenas apagar o código do source code, no campo “Eventos”  da entidade.

+ Após atualização da entidade vai ser necessário informar novamente o código do evento.

* Se a atualização pode ser completa, segui os passos da atualização do source code até o passo 5.

Após desvincular ou apagar o source code, apagar também a entidade.

**Observação:** Indicado que também sejam apagadas as Mensagens de Transformação da Entidade excluída.

Executar o configurador para criar a entidade novamente em sua versão atualizada.

Sobre executar o configurador, ver link abaixo, passo 3 que é um exemplo de execução do configurador:

Observação: Substituir a integração do exemplo para a integração de seu uso.

<http://tdn.totvs.com/pages/releaseview.action?pageId=463822922>
