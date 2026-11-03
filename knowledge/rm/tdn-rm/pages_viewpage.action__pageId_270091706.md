---
content_hash: c00686176e8ee9f6e0aff08a2cb4e49862b52daec8e0f09a9fe817f0af1c4ff1
fetched_at: '2026-06-29T00:08:23.788625+00:00'
page_id: '270091706'
product: rm
source: tdn-rm
title: TICKET_97786_DT_Patrimônio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270091706
version: 113
---

# Cadastro de Patrimônio

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *Totvs Gestão Patrimonial.* |
| **Função:** | *Cadastro de Patrimônio.* |
| **Situação/Requisito:** | Ao selecionar o fleg patrimônio Agregado, em preferência de usuário, sistema não apresenta o código do patrimônio agregado ao clicar em novo.     TESTES: 1) acesse > menu > utilitários > Preferencia > marque o preferência > ( patrimônio agregado )     2) edita um patrimônio que tenha um o campo patrimônio agregado a preenchido > clique em novo > o campo patrimônio agregado do novo patrimônio vem em branco  *.* |
| **Solução/Implementação:** | \* Implementar a regra de patrimônio agregado onde um patrimonio só pode ser agregado à outro patrimonio e um terceiro somente pode ser agregado à um terceiro. \* Implementar as validações da preferencia do usuário referente ao tipo de patrimônio ao ser selecionado a opção "Novo" no cadastro de patrimônio \* Implementar o carregamento do tipo de patrimônio quando o patrimônio origem estiver com o patrimônio agregado para que as validações possam ser aplicadas no momento de salvar o patrimônio destino. |
| **Conversores e Parâmetros:** | *N/A.* |
| **Tickets relacionados:** | *N/A.* |
| **Requisito (informe o requisito relacionado):** | *N/A.* |

divs
