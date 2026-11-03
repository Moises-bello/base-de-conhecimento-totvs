---
content_hash: 1bc4e57e8e0fc19ca4ac0dcbaf2abc98f59ee0af24aa8a361d5e194192c5976d
fetched_at: '2026-06-29T00:08:19.972376+00:00'
page_id: '267803003'
product: rm
source: tdn-rm
title: TVOJDZ_DT_Informacao_Ferias_Dobro_Cadastro_De_Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/TVOJDZ_DT_Informacao_Ferias_Dobro_Cadastro_De_Ferias
version: 108
---

# CADASTRO DE FÉRIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Férias* |
| **Situação/Requisito:** | Quando o funcionário tem afastamentos longos que fazem com que ultrapasse dois períodos aquisitivos sem gozar férias, o sistema apresenta a mensagem de férias em dobro no cadastro do funcionário mesmo que o parâmetro 'Interrompe contagem do período para pagamento de férias em dobro nos afastamentos L- I - P - T', no módulo PARAMETRIZADOR, opção 'Férias -> Férias em Dobro', esteja marcado.     Neste caso, quando o parâmetro está marcado, a mensagem não deve ser apresentada no cadastro do funcionário. |
| **Solução/Implementação:** | *Sistema passa a considerar o parâmetro 'Interrompe contagem do período para pagto de férias em dobro nos afastamentos L- I - P - T' no cadastro de férias.* |
| **Chamados relacionados:** | *TVOJDZ* |

divs
