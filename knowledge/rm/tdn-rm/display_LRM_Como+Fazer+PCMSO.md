---
content_hash: d58d9f8c088e7bfb345bc724f8ee8e5701505b9343ef9370f2f8453486144c74
fetched_at: '2026-06-29T00:10:09.330213+00:00'
page_id: '452719632'
product: rm
source: tdn-rm
title: Como Fazer PCMSO
type: documentation
url: https://tdn.totvs.com/display/LRM/Como+Fazer+PCMSO
version: 2
---

**Como Fazer PCMSO**

Como padrão, o sistema disponibilizará um modelo de PCMSO baseado em local de trabalho lembrando que cada empresa deve adaptar este modelo a sua própria realidade.

No book de relatórios do sistema serão disponibilizados os itens que compõem o relatório modelo, e para correta geração do mesmo, estes deverão ser importados para o sistema pelo menu  **Gestão| RM Reports | Processos | Importar Estrutura de Relatório.**

**Criando o relatório:**

Para criar o relatório de PCMSO será necessário primeiramente definir o tipo de relatório a ser desenvolvido, para isso o usuário deverá acessar **Relatórios | Tipos de Relatórios**, e incluir um relatório do tipo: "**Saúde**".

Para geração do modelo de PCMSO, com o relatório selecionado clicar em: **Processos | Gerar Modelo de PCMSO**. Caso o cliente deseje alterar o modelo de PCMSO disponibilizado pelo sistema, na aba "Itens do Relatório" será possível incluir itens do tipo texto, onde ao clicar no botão "Editar Texto", será exibido um editor de texto para o usuário digitar suas informações.

Na mesma aba, o usuário poderá incluir um relatório a partir do Gerador.NET. Neste caso, basta selecioná-lo no LOOKUP de relatórios e selecionar o relatório desejado.

**Atenção**

Se a parametrização da origem de exames pendentes for alterada (Opções| Parametrizador| Exames| Origem para exames pendentes), deve-se gerar novamente o modelo do relatório PCMSO, no cadastro de Tipos de Relatório. Essa nova geração se faz necessário para que os exames sejam buscados do local correto de associação. Feito isso, o usuário deverá acessar:   **Relatórios | Relatórios de Saúde** e incluir o relatório criado no passo acima.

Na aba: "**Identificação**", deverão ser preenchidos os campos:

•    Código do Relatório

•    Data Início

•    Data Fim

•    Descrição

•    Código Tipo Relatório

•    Código Local de Trabalho

Caso deseje, o usuário também poderá preencher os campos: Código Filial, Código Seção, Código Função e Código Posto.

**Gerando o relatório -**Para gerar o relatório de PCMSO, o usuário deverá acessar o menu **Relatórios | Relatórios de Saúde**. Ao selecionar o tipo de relatório a ser gerado serão habilitadas a abas:

**Parametrização -**  Onde serão carregados todos os parâmetros esperados pelos relatórios que compõem o tipo. Caso estes já estejam preenchidos na edição do cadastro, aba "Identificação", eles serão automaticamente sugeridos nesta tela.

**Ex**: Se o relatório espera o parâmetro CODSECAO e este campo estiver preenchido na edição, o parâmetro irá recebê-lo como valor. De qualquer forma cabe ao usuário validar esta parametrização ajustando-a sempre que necessário. É obrigatório o preenchimento de todos os parâmetros para a geração do relatório.

**Gerar/Visualizar -**  Trará informações de quando o relatório foi gerado pela última vez e quem o gerou. Ao clicar no botão "Gerar Relatório" o mesmo será gerado conforme o tipo e parametrização selecionada e todos os sub-relatórios de origem no Gerador.NET serão gerados como imagem e por conseqüência não poderão ser alterados. Ao clicar em "Visualizar" o usuário poderá ver o resultado final de seu relatório, as alterações a partir deste ponto não serão gravadas no banco de dados.
