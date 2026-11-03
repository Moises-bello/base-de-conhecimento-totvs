---
content_hash: b09043ae1387066dd346ad07b4a0ce12c51d5d4c92d7451db9593279faced3cd
fetched_at: '2026-06-29T00:08:41.245307+00:00'
page_id: '286519674'
product: rm
source: tdn-rm
title: RMCTB00009_Alteração da Máscara Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286519674
version: 12
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Alteração da Máscara Contábil |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do Processo**  Com o crescimento das empresas ou mudanças estruturais nas mesmas, pode haver a necessidade de mudança na máscara das contas contábeis. Assim, esta rotina objetiva facilitar o processo de alteração do plano, para que o mesmo atenda às necessidades das organizações.  **Regras Gerais**  Desde que o usuário ainda não tenha cadastrado nenhuma conta no grupo que deseja alterar, o sistema permitirá o aumento/diminuição de dígitos e/ou níveis das máscaras.  Se alguma conta do grupo a ser alterado já tiver sido cadastrada, o sistema permitirá apenas o aumento de dígitos e/ou níveis das máscaras.  **Parametrização Necessária**  1 - Para executar a rotina acesse o menu Cadastros/Contábil/Alteração da Máscara Contábil, conforme abaixo:        2 - Seguindo as regras supracitadas informe o grupo e a nova máscara das contas:                              **Informações importantes**  Para aumentar uma máscara, deve ser observado o seguinte:  - O 1º nível, não poderá ter mais que 1 caractere.  - Caso você esteja utilizando conta global, você deverá manter a mesma máscara em todas as coligadas.  - As contas que já foram cadastradas como ANALÍTICAS não se transformarão em SINTÉTICAS automaticamente, quando você aumentar os níveis da conta (isso é muito importante).  Exemplos:  Conta com máscara antiga (#.#.#.#.###) 1.1.1.1.001  Se você aumentar um nível no plano de contas ficando (#.#.#.#.###.###), você não poderá criar a conta 1.1.1.1.001.001, pois a 1.1.1.1.001 é Analítica. Para cadastrar a conta 1.1.1.1.000.001, você terá que primeiro criar a 1.1.1.1.000 como Sintética e depois criar a 1.1.1.1.000.001 como Analítica.  Conta com máscara antiga (#.#.#.#.###) 1.1.1.1.001  Se você aumentar o nº de caracteres de um nível existente (#.##.##.##.#####) o sistema completará o nº da conta com "0" (1.01.01.01.00001).  **Observação**  Se ano passado e este ano enviou as rotinas contábeis usando as contas que deseja alterar, para o ano que vem, será necessário para a ECD/ECF por exemplo a inclusão do registro I157, onde o usuário deverá transportar o saldo da conta antiga para a conta atual.  Peça ao contador para verificar as demais rotinas que usam conta contábeis e que esta alteração poderá causar algum impacto.  **Importante**  Quando o parâmetro Acessa Contas Globais estiver marcado, o processo deverá ser executado em todas as outras coligadas que têm esse parâmetro marcado.  Veja na figura abaixo: |
