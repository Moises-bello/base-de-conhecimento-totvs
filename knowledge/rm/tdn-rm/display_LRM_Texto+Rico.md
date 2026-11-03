---
content_hash: 7d9306bc71290ecb3dc04ae1b496b58cb74fcdcae340ec89f3bb84c3abdc7429
fetched_at: '2026-06-29T00:05:55.934787+00:00'
page_id: '147817270'
product: rm
source: tdn-rm
title: Texto Rico
type: documentation
url: https://tdn.totvs.com/display/LRM/Texto+Rico
version: 48
---

# Índice:

---

.\*ndice:

# Objetivo:

---

Esta página tem a finalidade de relatar a forma de uso e funcionalidades do controle Texto Rico.

# Introdução

---

O Texto Rico é um dos melhores controles do Totvs Reports. Com ele é possível criar grandes textos e em posições definidas mesclar o texto com informações da base de dados retornados através de campos da base ou consultas SQL.

# Utilização

---

O controle Texto Rico é localizado na barra de ***"Caixa de Ferramentas | Controles Avançados | Texto Rico"***.

Se a "Caixa de Ferramenta" estiver oculta. Acesse o menu ***"Exibição | Janelas"*** e habilitar a opção:

Depois de selecionado o controle, pressione o botão direito do mouse e o mantendo pressionado, arraste o controle para o corpo do relatório.

false

***Inserindo informações;***

***Há formas diferentes de inserir informações no controle Texto Rico.***

Controle - Texto RicoUtilizando arquivo RTF

Um método fácil de incluir um texto no controle Texto Rico seria utilizar o Microsoft Word para elaborar o texto e em seguida incluir esse arquivo no controle.

Abaixo temos um exemplo de texto, elaborado no Word, que será utilizado como contrato de trabalho. Lembramos que o arquivo deve ser salvo na extensão RTF.

Tendo o arquivo criado, selecionamos o controle e clicamos sobre sua Smart tag. Dentre as opções que serão apresentadas a seguir selecione “Carregar Arquivo”, será disponibilizado em sequência uma caixa de diálogo do Windows para que seja selecionado o arquivo salvo.

Feita a inserção do texto através do arquivo RTF, selecione o controle e através dos marcadores expanda as dimensões do controle para que o texto possa ser visualizado.

Vamos trocar a marcação (Nome) que incluímos no RTF pelo campo da base que irá retornar o nome do funcionário.

Para incluir um campo da base no contexto do Texto Rico o comando deve ser da seguinte forma: **Colchete** + **Nome do Campo** + **colchete**. Exemplo: **[PFUNC.NOME****]**. Na sequência geraremos o relatório para verificar o resultado.

Notem que o nome "*Itamar Mendes da Silveira*" foi incluso no texto do controle Texto Rico.

Incluindo Texto Manualmente

Para incluir um texto manualmente selecione o controle Texto Rico e dê dois cliques sobre o mesmo. Habilitará o seu conteúdo para digitação.

Como exemplo incluiremos o texto “Empregado” mais o campo que retornará o nome do funcionário.

Caso queira finalizar a edição basta clicar fora do controle. Na sequencia geramos o relatório para validar a troca do comando pelo nome do funcionário.

Incluindo Outros Controles

Para incluir outros controles ou campos que não pertencem a tabela máster do grupo, no texto do Texto Rico. Devemos incluir o controle no relatório, acessar suas propriedades e colocar no comando o valor atribuído a propriedade “Nome”.

No exemplo abaixo incluímos o campo “GCOLIGADA.NOME” e o controle “Expressão” Na estrutura do relatório. Selecionamos cada um dos controles e teclando F4 acessamos a propriedade de cada um. O campo que retorna o nome da coligada possui o valor "Nome1" na propriedade nome e o controle expressão da página recebeu o nome "Expressão1".

Na sequencia editamos o controle Texto Rico com dois cliques e incluímos os comandos no texto.

Conferindo o resultado das alterações gerando o relatório.

Editando a Fonte

Para editarmos a fonte do texto incluso no controle Texto Rico ***devemos ignorar*** a opção de fonte existente nas ***propriedades do controle***. Elas ***não são validas*** para esse controle.

Para edição selecione o controle e acesse a guia “Layout”. Os agrupadores “Fonte” e “Alinhamento” serão as ferramentas utilizadas para essas alterações.

Selecionado o comando selecione a guia “Layout” e altere as propriedades. Em nossa simulação utilizaremos: Fonte Verdana, tamanho 10, negrito e itálico.

Geramos o relatório para verificar o resultado da formatação.

---

falseNotas:

* O grupo do relatório onde será incluso o controle de Texto Rico ***deve possuir uma tabela ou consulta SQL*** atribuída ***como máster*** do grupo.
* Somente os campos pertencentes a ***tabela máster podem ser inclusos diretamente no controle Texto Rico*** utilizando sua nomenclatura ***TABELA.COLUNA***. Tabelas secundárias ou demais controles devem utilizar sua propriedade “NOME”.
* Outros controles e campos da tabela secundaria devem ser configurados para não ficarem visíveis. Para que as informações não sejam impressas duplicadas..
* Quando o controle de Texto Rico ***contém conteúdo RTF ou está vinculado a algum dado***, a formatação ***não é obtida no controle***, mas sim diretamente do RTF ou do dado. Se não houver definição da fonte no RTF ou dado, aplica-se a formatação default **Times New Roman**.
falseDicas:

Caso queira alterar o espaçamento entre linhas, copie o texto incluso no controle Texto Rico e cole no Microsoft Word. Faça as alterações de espaçamento entre linhas conforme o desejado e copie o texto ajustado do Word para o contexto do Texto Rico novamente. Salve as alterações e gere o relatório para validar as modificações.

Limitação de design

Visite este conteúdo para mais informações sobre problemas e soluções relacionadas ao Texto Rico.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Texto Rico

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
