---
content_hash: 80d5777ca6e355b9372588538316a8977f0e66ce58141b0a2e796ab1bd93d794
fetched_at: '2026-06-29T00:10:36.371607+00:00'
page_id: '532036576'
product: rm
source: tdn-rm
title: Cadastro Campo Complementar
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+Campo+Complementar
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Contábil. |
| **Versões:** | 12.1.20 |
| **Ocorrência:** | Cadastro de Campos Complementares |
| **Ambiente:** |  |
| **Passo a passo:** | **Definição do processo:**  Neste cadastro você poderá criar campos que poderão ser utilizados na inclusão/alteração de:   * Lançamentos; * Centro de Custos; * Contas Contábeis; * Contas Gerenciais.   Para cada tipo de Campo Complementar um processo distinto.  **Parametrização Necessária:**  Os dados devem ser informados conforme a necessidade do usuário, ou seja, podemos ter um campo para ser exibido num relatório específico da empresa, um dado que foi criado em uma obrigação acessória e/ou uma seleção necessária para avaliação de dados que, de outra forma, não poderiam ser extraídos do sistema.    1 - Ao abrir um novo cadastro temos várias opções, como se pode ver na figura abaixo:  Aqui usamos o cadastro do campo Complementar de **Lançamentos**.        2 - Vamos cadastrar um campo para fazer uma seleção aleatória de lançamentos:        3 - Ao cadastrarmos como valor lógico o sistema irá inserir um campo, onde podemos selecionar o dado por meio de uma flag e fazer filtros de acordo com as informações desejadas. Veja na figura abaixo o campo na visão do lançamento:        4 -  Agora iremos cadastrar um campo para as **contas contábeis**, onde iremos informar um texto com dados adicionais da conta:        5 - Após o cadastro já aparece na visão da conta o campo com o texto padrão. Caso desejar informar mais algum texto, o mesmo poderá ser digitado, já que o tamanho deste campo (255) ainda não foi totalmente preenchido: |
| **Observações:** | Ainda temos a opção de Usar **Tabela Dinâmica**.  As tabelas dinâmicas servem para definir um conjunto de dados que podem ser informados em um determinado campo complementar. Por exemplo: foi criado um campo complementar chamado "Digitador", onde deve ser informado o nome das pessoas responsáveis pela digitação (inclusão) das contas. Pode-se criar uma tabela dinâmica com todos os nomes das pessoas que incluem contas e vinculá-la a este campo. No momento da inclusão da conta, para preenchimento do campo "Digitador", seleciona-se o nome da lista previamente cadastrada na Tabela Dinâmica. |
