---
content_hash: 1559d5ae494fd4e7eae6a0e34fedbb9c0f6a5937cba139811704def458c085f5
fetched_at: '2026-06-29T00:08:45.272830+00:00'
page_id: '309413806'
product: rm
source: tdn-rm
title: RMCTB00005_Geração Automática de Orçamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309413806
version: 7
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.17 |
| **Ocorrência:** | Geração Automática de Orçamentos |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do processo:**  Este processo permite gerar novos orçamentos, tomando como base os valores obtidos pela movimentação das contas em um determinado período. Os campos data inicial, final, ano e conta contábil, são essenciais para que os cálculos sejam feitos corretamente.  O período não poderá ultrapassar mais de 12 meses, porém poderá intercalar as datas entre um ano e outro, mas sempre respeitando o limite de até 12 meses.  Como este processo irá buscar a movimentação da conta no determinado período e ano informado, o ideal é verificar se nos lançamentos da respectiva conta, os campos: conta gerencial, centro de custo e departamento estão informados no lançamento. Lembando que deverá Ativar o Filtro, informando o código da filial e departamento, não se esqueça de marcar a opção: Incluir departamentos nulos no filtro, caso a empresa tenha movimentação em que o campo departamento não esteja preenchido.  **DESENVOLVIMENTO/PROCEDIMENTO:**  **1 - Acesse o caminho: Orçamento / Geração Automática de Orçamentos:**              **2 - Informe os principais dados, conforme destacado nas figuras abaixo:**                                                Pelo menos uma filial deve ser selecionada, bem como devem ser incluídos os departamentos nulos se este dado não for informado nos lançamentos.                                                **3 - Não se esqueça de verificar as abas Conta Gerencial e Centro de Custo, caso queira que o orçamento seja criado com estes respectivos campos, conforme abaixo:**  Veja que poderá marcar a opção: Gerar orçamento de acordo com a distribuição gerencial das contas contábeis:      Já na aba:Centro de Custo caso deseje marque a opção: Considerar movimentos sem centros de custo (centros de custo nulos), conforme abaixo:    **4 - Ao final do processo o sistema mostra uma tela com o log do processo. Clique em bloco de notas para verificar os avisos informados no arquivo:** |
| **Observações:** | O orçamento irá ser criado de acordo com as movimentações(lançamentos) da referida conta contábil informada, sendo assim, caso tenha mais de uma conta, esta deverá ser informada na aba: Conta Contábil. |
