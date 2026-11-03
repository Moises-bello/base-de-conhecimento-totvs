---
content_hash: cc7daafbd0d19dda3775901d08fdb17e3fa7c477d00964f211ac9226fff7557a
fetched_at: '2026-06-29T00:08:40.932168+00:00'
page_id: '286517719'
product: rm
source: tdn-rm
title: RMCTB00003_Alteração do Campo "Tem Distribuição Gerencial"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286517719
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Alteração do campo "Tem Distribuição Gerencial" |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do Processo** Processo que altera a situação gerencial de uma conta contábil, incluindo ou excluindo o rateio gerencial da conta selecionada:                   **Regras Gerais**  1 - Selecione a conta a ser alterada ou informe o reduzido ao acessar o processo:                              2 - Acesse o filtro para selecionar outras contas a serem alteradas:                              **Parametrização Necessária**  1 - A conta gerencial e o percentual devem ser informados quando a opção selecionada for "passará a ter distribuição gerencial". O percentual dos rateios deve sempre fechar em 100%.  Deve-se observar também que para contas contábeis globais somente contas gerenciais globais podem ser utilizadas:                              2 - Quando a opção Deixará de ter distribuição gerencial for marcada, o sistema irá retirar da base de dados todos os rateios da conta contábil selecionada: |
| **Observações:** | Quando a conta passar a ter distribuição gerencial e tiver rateios diferentes para cada conta, recomenda-se executar o processo separadamente, visto que o rateio selecionado será aplicado para todas as contas da lista. |
