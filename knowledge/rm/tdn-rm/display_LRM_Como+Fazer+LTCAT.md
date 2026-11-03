---
content_hash: 6b3bb7fb437d5076555e4464b4b63dfe6f189c1059034a175e285e97d3628b70
fetched_at: '2026-06-29T00:10:07.312081+00:00'
page_id: '452719398'
product: rm
source: tdn-rm
title: Como Fazer LTCAT
type: documentation
url: https://tdn.totvs.com/display/LRM/Como+Fazer+LTCAT
version: 2
---

**Como Fazer LTCAT**

Como padrão, o sistema disponibilizará um modelo de LTCAT baseado no reconhecimento e avaliação de risco.

No book de relatórios do sistema serão disponibilizados os itens que compõem o relatório modelo, e para correta geração do mesmo, estes deverão ser importados para o sistema pelo menu    
**Relatórios | Gerador .Net | Processos | Importar Estrutura de Relatório.**

**Criando o relatório:**

Para criar o relatório de LTCAT será necessário primeiramente definir o tipo de relatório a ser desenvolvido, para isso o usuário deverá acessar : **Relatórios | Tipos de Relatórios**, e incluir um relatório do tipo: **"LTCAT"**.

Para geração do modelo de LTCAT, com o relatório selecionado clicar em: **PROCESSOS | GERAR MODELO DE LTCAT**. Caso o cliente deseje alterar o modelo de LTCAT disponibilizado pelo sistema, na aba: **"Itens do Relatório"** será possível incluir itens do tipo texto, onde ao clicar no botão: **"Editar Texto",**será exibido um editor de texto para o usuário digitar suas informações.

Na mesma aba, o usuário poderá incluir um relatório a partir do Gerador.NET, neste caso, basta selecioná-lo no LOOKUP de relatórios e selecionar o relatório desejado. Feito isso, o usuário deverá acessar:

**Relatórios | Relatórios de LTCAT** e incluir o relatório criado no passo acima. 

Na aba: **"Identificação",**deverão ser preenchidos os campos:

•    Código do Relatório

•    Data Início

•    Data Fim

•    Descrição

•    Código Tipo Relatório

•    Código Filial

Caso deseje, o usuário também poderá preencher os campos: Código local de trabalho, Código Seção, Código Função e Código Posto. **Gerando o relatório:**  
Para gerar o relatório de LTCAT, o usuário deverá acessar o menu **Relatórios | LTCAT.**

Ao selecionar o tipo de relatório a ser gerado serão habilitadas a abas:

**Parametrização -**Onde serão carregados todos os parâmetros esperados pelos relatórios que compõem o tipo. Caso estes já estejam preenchidos na edição do cadastro, aba "Identificação", eles serão automaticamente sugeridos nesta tela.

Ex: Se o relatório espera o parâmetro CODSECAO e este campo estiver preenchido na edição, o parâmetro irá recebê-lo como valor. De qualquer forma cabe ao usuário validar esta parametrização ajustando-a sempre que necessário. É obrigatório o preenchimento de todos os parâmetros para a geração do relatório.

**Gerar/Visualizar -**Trará informações de quando o relatório foi gerado pela última vez e quem o gerou. Ao clicar no botão "Gerar Relatório" o mesmo será gerado conforme o tipo e parametrização selecionada e todos os sub-relatórios de origem no Gerador.NET serão gerados como imagem e por consequência não poderão ser alterados. Ao clicar em "Visualizar" o usuário poderá ver o resultado final de seu relatório, as alterações a partir deste ponto não serão gravadas no banco de dados.
