---
content_hash: d4fa0bf7a6032979fddc298f63ff36817299494df22c9c72a864d5c32eef4dcb
fetched_at: '2026-06-29T00:10:09.335481+00:00'
page_id: '452719634'
product: rm
source: tdn-rm
title: Como Fazer PPRA
type: documentation
url: https://tdn.totvs.com/display/LRM/Como+Fazer+PPRA
version: 2
---

**Como Fazer PPRA**

Como padrão, o sistema disponibilizará um modelo de PPRA baseado em local de trabalho lembrando que cada empresa deve adaptar este modelo a sua própria realidade.   
No book de relatórios do sistema serão disponibilizados os itens que compõem o relatório modelo, e para correta geração do mesmo, estes deverão ser importados para o sistema pelo menu   
 **Relatórios | Gerador .Net | Processos | Importar Estrutura de Relatório.**

**Criando o relatório -**Para criar o relatório de PPRA será necessário primeiramente definir o tipo de relatório a ser desenvolvido, para isso o usuário deverá acessar **Relatórios | Tipos de Relatórios**, e incluir um relatório do tipo: **"Segurança"**.

Para geração do modelo de PPRA, com o relatório selecionado clicar em **PROCESSOS | GERAR MODELO DE PPRA**. Caso o cliente deseje alterar o modelo de PPRA disponibilizado pelo sistema, na aba: **"Itens do Relatório"** será possível incluir itens do tipo texto, onde ao clicar no botão: **"Editar Texto",** será exibido um editor de texto para o usuário digitar suas informações.

Na mesma aba, o usuário poderá incluir um relatório a partir do Gerador.NET, neste caso, basta selecioná-lo no LOOKUP de relatórios e selecionar o relatório desejado. Feito isso, o usuário deverá acessar **Relatórios | Relatórios de Segurança** e incluir o relatório criado no passo acima.

Na aba: **"Identificação",** deverão ser preenchidos os campos:

•    Código do Relatório

•    Data Início

•    Data Fim

•    Descrição

•    Código Tipo Relatório

•    Código Local de Trabalho

Caso deseje, o usuário também poderá preencher os campos: Código Filial, Código Seção, Código Função e Código Posto.

**Gerando o relatório -**Para gerar o relatório de PPRA, o usuário deverá acessar o menu **Relatórios | Relatórios de Segurança.**

Ao selecionar o tipo de relatório a ser gerado serão habilitadas a abas:

**Parametrização -**Onde serão carregados todos os parâmetros esperados pelos relatórios que compõem o tipo. Caso estes já estejam preenchidos na edição do cadastro, aba "Identificação", eles serão automaticamente sugeridos nesta tela.

**Ex**: Se o relatório espera o parâmetro CODSECAO e este campo estiver preenchido na edição, o parâmetro irá recebê-lo como valor. De qualquer forma cabe ao usuário validar esta parametrização ajustando-a sempre que necessário. É obrigatório o preenchimento de todos os parâmetros para a geração do relatório.

**Gerar/Visualizar -**Trará informações de quando o relatório foi gerado pela última vez e quem o gerou. Ao clicar no botão "Gerar Relatório" o mesmo será gerado conforme o tipo e parametrização selecionada e todos os sub-relatórios de origem no Gerador.NET serão gerados como imagem e por conseqüência não poderão ser alterados.Ao clicar em "Visualizar" o usuário poderá ver o resultado final de seu relatório, as alterações a partir deste ponto não serão gravadas no banco de dados.
