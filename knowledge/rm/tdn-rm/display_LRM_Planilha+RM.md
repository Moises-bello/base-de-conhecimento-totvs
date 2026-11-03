---
content_hash: 9691badbe3cf5ac37523b377682c2e158cc10ac95a92fd5c5c7b5986b9c4d630
fetched_at: '2026-06-29T00:08:12.773998+00:00'
page_id: '243648305'
product: rm
source: tdn-rm
title: Planilha RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Planilha+RM
version: 48
---

# Índice:

---

.\*ndice:

# Objetivo

---

O objetivo deste documento é apresentar as funcionalidades da Planilha RM.

# Introdução

---

     No módulo de Planilhas da aplicação existem duas funcionalidades distintas:

     A primeira, denominada de Planilha .Net. Ela se integra com o Microsoft Excel, consumindo recursos de Consulta SQL e Fórmula, além de uma API de integração para leitura e gravação de informações neste formato.

     A segunda, objeto desta documentação e denominada de Planilha RM. É uma planilha eletrônica independente da instalação do Microsoft Excel, que permite a consulta de informações da Base de Dados através de Consultas SQL cadastradas e a manipulação destes resultados através de funções sobre as linhas e colunas.

     Cada um dos Tipos de Planilha apresentados possui um designer diferente para manipulação das planilhas criadas.

# Tela de Visão do Cadastro de Planilhas

---

     A visão de Planilhas é fundamentalmente uma árvore com as planilhas cadastradas de forma hierárquica, permitindo ao usuário editar, criar e excluir planilhas de acordo com as permissões de segurança do sistema. 

     Além de todas as funcionalidades padrões existentes em todas as telas do sistema, a Planilha possui três específicas:

* **Exportação de Planilha**: permite exportar uma planilha cadastrada no RM e salvá-la no computador.
* **Importação de Planilha**: permite importar uma planilha que foi exportada anteriormente no sistema.
* **Geração de Planilhas em Lote.**

# Janela de Edição do Cadastro de Planilhas

---

A tela de edição de Planilhas é responsável pelo cadastro das informações referentes à uma planilha. Os campos disponíveis para alteração estão dispostos a seguir:

* **Nome**: Texto que representa o nome da planilha na base de dados;
* **Tipo**: Define se a planilha é Excel ou uma Planilha RM;
* **Observação**: Texto para descrever as informações contidas dentro da planilha e o seu propósito;
* **Grupo de Planilhas**: Define o Grupo ao qual a planilha pertence para efeitos de segurança; (Para maiores informações consulte: [Grupos de Relatório](http://tdn.totvs.com/x/lgqxAw))
* **Nível de Acesso**: Define qual o Nível mínimo de Acesso necessário para visualizar e alterar a planilha;
* **Planilha Mestre**: Define qual a planilha Mestre/Pai para hierarquização e exibição na visão em forma de árvore;
* **Versão**: Versão em que a planilha foi criada;
* **Visível a todas as coligadas**: Define se a planilha vai estar visível independente da coligada que estiver selecionada no contexto.

# Tela de Designer da Planilha RM

---

A janela de designer da Planilha RM irá disponibilizar as seguintes funcionalidades:

**AGRUPAMENTO SALVAR:**

* **Salvar Planilha**: Salva a planilha carregada no Banco de Dados. Este botão não é visível caso a planilha não tenha sido carregada do Banco de Dados.
* **Salvar como Excel**: Exporta um cópia da planilha no formato Excel para o computador.
* **Visualizar Impressão**: Visualiza a planilha em modo de impressão.
* **Imprimir**: Imprime a planilha.

Importante: 

Consultas SQL e Stored Procedures não são exportadas. 

Observação

Ao salvar uma Planilha RM pela primeira vez, seu tempo de salvamento será maior a partir da Versão 12.1.17.124.

Isso ocorre pois temos implementado um código que remove "lixos" das planilhas, que basicamente são células em branco e que não são utilizadas causando uma queda na performance. Porém, após ser salva pela primeira vez, nas próximas vezes a planilha será salva praticamente instantaneamente.

**AGRUPAMENTO OPERAÇÕES:**

* **Colar:** Transfere para a planilha os valores que estão na sua areá de transferência
* **Recortar:** Recorta o conteúdo da(s) célula(s) selecionada(s) para a Área de Trabalho
* **Copiar:** Copia o conteúdo da(s) célula(s) selecionada(s) para a Área de Trabalho
* **Pincel**: Copia o formato da seleção corrente para a área de trabalho.
* **Operações**:

1. **Adicionar Linha:** Adiciona uma nova linha à planilha
2. **Remover Linha:** Remove a linha selecionada da planilha
3. **Adicionar Coluna:** Adiciona uma nova coluna à planilha
4. **Remover Coluna**: Remove a coluna selecionada da planilha
5. **Adicionar página**: Adiciona uma nova página à planilha
6. **Remover página**: Remove a página selecionada da planilha
7. **Renomear página**: Renomeie a página selecionada da planilha
8. **Bloquear/Desbloquear página:**Bloqueia a planilha, não permitindo nenhum tipo de edição.

* **Definir Senha:** Permite definir uma senha para a planilha. Com a definição da senha, quando outros usuários abrirem essa planilha será solicitada a digitação da senha correta para que seja possível fazer qualquer alteração. O usuário que definiu a senha não precisará digitá-la novamente para acessá-la. Entretanto, qualquer usuário que a conheça poderá definir uma nova senha.

**AGRUPAMENTO FONTE:**

* **Seleção de Fonte**: Define qual o nome da fonte usado na(s) célula(s) selecionada(s)
* **Bordas**:

1. **Borda Inferior**: Aplica a borda Inferior na(s) célula(s) selecionada(s)
2. **Borda Superior**: Aplica a borda Superior na(s) célula(s) selecionada(s)
3. **Borda da Esquerda**: Aplica a borda Esquerda na(s) célula(s) selecionada(s)
4. **Borda da Direita**: Aplica a borda Direita na(s) célula(s) selecionada(s)
5. **Sem borda**: Remove todas as bordas da(s) célula(s) selecionada(s)
6. **Todas as Bordas**: Aplica as bordas Inferior, Superior, Esquerda, Direita, Horizontal e Vertical na(s) célula(s) selecionada(s)
7. **Borda de Contorno**: Aplica as bordas Inferior, Superior, Esquerda e Direita na(s) célula(s) selecionada(s)

* **Seleção do Tamanho da Fonte**: Define qual o tamanho da fonte usado na(s) célula(s) selecionada(s)
* **Negrito**: Aplica ou remove o estilo Negrito na fonte usada na(s) célula(s) selecionada(s)
* **Itálico**: Aplica ou remove o estilo Itálico na fonte usada na(s) célula(s) selecionada(s)
* **Sublinhado**: Aplica ou remove o estilo Sublinhado na fonte usada na(s) célula(s) selecionada(s)
* **Seleção de Cor da Fonte**: Define qual a cor da fonte usado na(s) célula(s) selecionada(s)

**AGRUPAMENTO ALINHAMENTO:**

* **Alinhamento Vertical Superior**: Alinha o conteúdo da(s) célula(s) selecionada(s) no canto Superior
* **Alinhamento Vertical Central**: Alinha o conteúdo da(s) célula(s) selecionada(s) centralmente
* **Alinhamento Vertical Inferior**: Alinha o conteúdo da(s) célula(s) selecionada(s) no canto Inferior
* **Alinhamento Horizontal Esquerdo**: Alinha o conteúdo da(s) célula(s) selecionada(s) à Esquerda
* **Alinhamento Horizontal Central**: Alinha o conteúdo da(s) célula(s) selecionada(s) centralmente
* **Alinhamento Horizontal Direito**: Alinha o conteúdo da(s) célula(s) selecionada(s) à Direita
* **Quebrar texto automaticamente**: Tornar todo o conteúdo de uma célula visível, exibindo-o em várias linhas
* **Mesclar / Desfazer Mesclagem**: Associa/Desassocia um conjunto de células selecionadas em uma maior

**AGRUPAMENTO VISÕES DE DADOS E VARIÁVEIS:**

* **Visões de Dados**:

1. **Reexecutar Consultas SQL da célula**: Reexecuta todas as consultas SQL associadas à todas as células.
2. **V****isualizar Consulta SQL da Célula**: Visualiza o texto da Consulta SQL associado a uma determinada célula.
3. **Associar Consulta SQL à Célula**: Associa uma Consulta SQL a uma determinada célula, fazendo com que seu resultado seja apresentado nas células adjacentes à direita (colunas) e abaixo (linhas). Uma Consulta SQL associada à uma célula pode conter parâmetros que referenciem outras células. Além disso, os parâmetros também podem referenciar variáveis do Contexto, como Cód. Coligada, Cód. Filial, Id. do Projeto, Cód. Sistema, etc.  
   Veja como criar [consultas com parâmetros dentro da planilha](http://tdn.totvs.com/x/t-aFDg) ou como adicionar [Stored Procedure na planilha](http://tdn.totvs.com/x/ygJvBg).
4. **Desassociar Consulta SQL à Célula**: Remove a consulta SQL de uma determinada célula
5. **Ordem de Execução das Consultas SQL na Planilha**: Define a ordem em que as Consultas SQL associadas às células da planilha serão executadas.
6. **Reexecutar todas as consultas SQL da planilha**: Reexecuta todas as consultas SQL vinculadas a planilha.
7. **Recalcular Automaticamente**: Recalcula todas as consultas SQL vinculadas a planilha automaticamente, sempre que os parâmetros da consulta forem alterados.

* **Associar Variável à Célula**: Permite vincular variáveis de execução do TOTVS Obras e Projetos à planilha.

**BARRA DE FÓRMULAS:**

 A barra de Fórmulas permite a edição da fórmula associada à célula. 

 As fórmulas utilizadas na Planilha RM são as mesmas utilizadas no Excel, para consulta-las clique [aqui](http://office.microsoft.com/en-us/excel-help/excel-functions-alphabetical-list-HA010277524.aspx?CTT=3). 

# Classificar e Filtrar

---

A combinação das teclas **CTRL + SHIFT + L** permite ativar a funcionalidade de filtragem para um intervalo da planilha ou tabela.

FiltroclassificarClassificarfiltrarFiltrar

# Opções de Formatar

---

Existe hoje a opção de formatar na células da planilha, como opções de formatação, hoje nós temos:

* **Geral:**Células com formato "Geral" não possuem formato de número específico
* **Texto:**A categoria "Texto" exibe células com formato de texto mesmo quando houver um número na célula. A célula que recebe a formatação de texto é exibida exatamente como digitada.
* **Data:**Os formatos de "Data" exibem números de série de datas e horas como valores de data. Caso o usuário queira exibir o formato de data e hora na mesma célula e necessário utilizar o formato especial.

           

* **Especial:** Os formatos de "Especial" são úteis para valores padrões na célula. Exemplo:
  + **Opção de máscara para data e/ou horas:** É utilizado as letras "**d = dia**", "**m = mês**" e "**y = ano**" para representar a data e as letras "**h = hora**", "**m = minutos**" e "**s = segundos**" para representar a hora como opções de formatação de Data/Hora.   
    É possível utilizar a formatação das letras em qualquer ordem. 

    **Exemplo:** "dd/mm/yyyy hh:mm:ss = 15/08/1991 00:00:00"
  + **Opção de Máscara para Moeda:** É utilizado o  "**#**" para definir o formato da moeda.   
    Para utilização de um caractere qualquer, como por exemplo o sifão, é necessário colocar esse caractere entre aspas duplas (")

**Exemplo:** "R$" ##.###,## = R$ 5.609,51"

                        

Observação

 O idioma padrão da Planilha RM é o Inglês. Portanto, para que as funções de fórmula funcionem corretamente, elas ***devem ser escritas em Inglês***.

*A partir da versão **12.1.23 não será mais possível o uso da Planilha.Net como RMPart nos Cenários**. Permanecendo a inclusão de [Planilhas RM](http://tdn.totvs.com/x/MceFDg) somente.*

*A partir da versão **12.1.27.144** as Planilhas RM serão fechadas sempre que o contexto da aplicação for alterado. Este comportamento foi adotado por questões de segurança, uma vez que todas as permissões são recarregadas no momento da troca de contexto e o usuário poderia acessar um recurso na planilha que ele não possui permissão no módulo de origem.*

 ***Veja os principais conteúdos::***
