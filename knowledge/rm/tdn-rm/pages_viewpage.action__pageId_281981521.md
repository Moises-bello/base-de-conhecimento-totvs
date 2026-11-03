---
content_hash: 082250f81b47e053c8da01575935bdcda3f02cb91cd8e3591723ded0bb1ffd57
fetched_at: '2026-06-29T00:08:35.549274+00:00'
page_id: '281981521'
product: rm
source: tdn-rm
title: 868098 RHU01-763 Erro ao salvar funcionário estagiário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=281981521
version: 105
---

# Visualizar nomes dos campos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Pessoas |
| **Função:** | Cadastro de funcionário. |
| **Situação/Requisito:** | Ao editar os dados do estágio de um funcionário estagiário, o sistema apresentava a seguinte mensagem de erro : Violação de concorrência: UpdateCommand afetou 0 dos registros 1 esperados.  O erro acontecia, pois o parâmetro para não gerar ficha de registro para estagiário se encontrava marcado e o funcionário possuía número de ficha de registro informada, desta forma o sistema limpava os dados da ficha de registro deixando o cadastro do funcionário em modo de edição, porém dentro do Vitae, os componentes de endereço confirmavam as alterações feitas na ficha de registro pelo labore, porém não salvavam as mesmas no banco, sendo assim o erro acontecia. |
| **Solução/Implementação:** | Foi ajustado no RMVitae, para que o mesmo confirme as alterações do CEP somente quando o registro que lido no momento ainda não tenha sido alterado por outro fonte. |
| **Tickets relacionados:** | 868098 |

divs
