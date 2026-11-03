---
content_hash: bfaf5fec25c7450b6f933d9ec0ff76da67599194d3945686430a7cb0c5d10af4
fetched_at: '2026-07-02T19:24:26.002109+00:00'
page_id: '519714889'
product: protheus
source: tdn-tec
title: 10.1 Assistentes de Código
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519714889
version: 3
---

Este assistente o auxiliará na criação de programas AdvPL com funcionalidades específicas conforme as informações fornecidas.

1. Selecione o Local (Tela 74 A) onde o arquivo-fonte será salvo;  
     
     
                      Tela 74: Tipos de assistentes no Assistente de Código
2. Informe o **Nome do Fonte** (Tela 74 B)
3. Selecione o **Tipo de Assistente** (Tela 74 C)
4. Acione o botão Próximo (Tela 74 D).

Conforme o **Tipo de Assistente** selecionado, você será guiado por uma ou mais páginas para complementar os dados necessários para a geração do arquivo-fonte.

# Assistente de código: Cadastro

Este tipo de assistente o auxilia a criar arquivo-fonte, capazes de efetuar manutenção de dados em tabelas.

*Tela 75: Definição de tipo de template com informações primordiais*

1. *Selecione o tipo template*, em **Cadastro - Tipo de arquivo**(Tela 75 A), conforme a origem da definição da tabela.  
   1. Arquivo padrão *–*utilizado quando a definição da tabela é a mesma do dicionário de dados, preenchendo os dados solicitados.  
      * **Parâmetros** – identifica uma *Pergunte* definida no dicionário de dados do *Protheus*;
      * **Alias** (Tela 75 B) – no caso de arquivo padrão, este será utilizado para localizar as definições no dicionário de dados, caso seja arquivo específico este será utilizado para identificar a área de trabalho (*select area*);
      * A ordem de apresentação dos dados é definido por uma das opções:  
        + **Utilize índice padrão** (Tela 75 C)– indica qual o número do índice do dicionário de dados, associado ao alias, que será utilizado ;
        + **Utiliza índice temporário** (Tela 75 D) – informe uma expressão AdvPL válida para indicar a ordem dos dados. Este índice é de uso temporário, sendo eliminado após o seu uso.
   2. Arquivo específico – utilizado para uma estrutura livre da tabela.

               *Tela 76: Definição da estrutura para tipo de arquivo específico*

* **Parâmetros** (Tela 76 A) – identifica uma *Pergunte* definida no dicionário de dados do *Protheus*;
* **Estrutura** (Tela 76 B) - utilizado para definir a estrutura da tabela. Utilize os botões a direita para adicionar ou remover atributos (campos).
* **Indexado** (Tela 76 C) – se marcado indica que a tabela será ordenada pela expressão *AdvPL* informada em **Chave**.

2.  Após preencher os dados, avance para a página seguinte;  
3.  Nesta página do assistente de código, você complementa os dados, podendo detalhar funcionalidades.  
  
*Tela 77: Definição do template de cadastro*  
  
*4. Selecione o template*de cadastro (Tela 76 A), conforme a visualização e comportamento desejado:  
*a) axCadastro – Cadastro Padronizado*, irá utilizar a função *axCadastro* da biblioteca AdvPL  
*b) Mbrowse – definindo opções,* irá utilizar a função *mBrowse* da biblioteca AdvPL  
  
5. Nas abas logo abaixo, você efetua algumas customizações:  
    a)Aba "Botões" (Tela 78)- utilizada somente pela opção de *template* Mbrowse e permite adicionar ou remover funcionalidades a tela utilizando os botões do lado direito;

                                            Tela 78: Configuração de botões para mBrowse  
  
 b)Aba "Campos" (Tela 79) - permiti você indicar quais campos e customizar alguns atributos. Caso não especifique, será utilizado todos os campos definidos no dicionário de dados ou na definição de tabela customizada.

                                                      Tela 79: Seleção de campos e atributos

c) Configurações (Tela 80)– permiti definir propriedades opcionais.

*Tela 80: Configurações opcionais do assistente*

* Titulo – informe o titulo a ser utilizado na janela;
* Campo Diferenciador – expressão *AdvPL*, utilizada pela *mBrowse* para agrupar os dados

Ao preencher todos os dados obrigatórios solicitados, finalize. Você obterá algo semelhante a Tela 81. Localize a entrada de função *user function* e coloque um nome mais significativo, salve e compile.

                                 *Tela 81: Exemplo de código gerado pelo Assistente*

# **Assistente de código: Geração de Arquivo Texto**

Este tipo de assistente o auxilia a criar arquivos-fontes, capazes de gerar arquivos textos a partir de uma tabela de dados.

*Tela 82: Assistente para Geração de Arquivo Texto*

1. Selecione o tipo *template*, em **Geração de TXT - Tipo de arquivo** (Tela 82 A), conforme a origem da definição da tabela.  
   1. Arquivo padrão *–*utilizado quando a definição da tabela é a mesma do dicionário de dados, preenchendo os dados solicitados.  
      * **Parâmetros** – identifica uma *Pergunte* definida no dicionário de dados do *Protheus*;
      * **Alias** (Tela 82 B) – no caso de arquivo padrão, este será utilizado para localizar as definições no dicionário de dados, caso seja arquivo específico este será utilizado para identificar a área de trabalho (*select area*);
      * A ordem de leitura dos dados é definido por uma das opções:  
        + **Utilize índice padrão** (Tela 82 C)– indica qual o número do índice do dicionário de dados, associado ao alias, que será utilizado ;
        + **Utiliza índice temporário** (Tela 82 D) – informe uma expressão AdvPL válida para indicar a ordem dos dados. Este índice é de uso temporário, sendo eliminado após o seu uso.                                        Tela 83: Definição de arquivo específico
   2. Arquivo específico – utilizado para uma estrutura livre da tabela.  
      * **Parâmetros** (Tela 83 A)– identifica uma *Pergunte* definida no dicionário de dados do *Protheus*;
      * **Estrutura** (Tela 83 B) - utilizado para definir a estrutura da tabela. Utilize os botões a direita para adicionar ou remover atributos (campos).
      * **Indexado** (Tela 83 C) – se marcado indica que a tabela será ordenada pela expressão *AdvPL* informada em **Chave**.
2. Após preencher os dados, avance para a página seguinte;
3. Nesta página do assistente de código, você complementa os dados detalhando como será o arquivo texto.

Arquivo Texto (Tela 84) - Indique a origem dos demais dados, podendo ser:  
  
  
                  Tela 84: Definição do formato do arquivo texto definido

* Definido (Tela 84 A) – os valores são fixos e informados logo abaixo;

1. * + Parametrizado (Tela 85 A)– os valores serão lidos a partir de uma variável (normalmente de escopo privado (*private*).  
         
                       Tela 85: Definição do formato do arquivo-texto parametrizado
     + Informe os demais campos conforme solicitado (Tela 84 B e C, Tela 85 B e C)  
         
       b) Posições – será utilizado para definir o *layout* do arquivo de saída.  
         
       Defina o *layout* informando os dados Campo, posição, tamanho, número de decimais e tipo. Para adicionar ou remover campos, utilize os botões do lado direito.

                                                   Tela 86: Definição do *layout* do arquivo de saída

Ao preencher todos os dados obrigatórios solicitados, finalize. Você obterá algo semelhante a Tela 87. Localize a entrada de função user function e coloque um nome mais significativo, salve e compile.

*Tela 87: Tela após a execução do Assistente de Geração de Arquivo Texto*

# Assistente de código: Importação de Arquivo Texto

Este tipo de assistente o auxilia a criar arquivos-fontes, capazes de importar arquivos textos e gravando-os em uma tabela de dados.

                         *Tela 88: Assistente para importação de arquivos textos*

1. Selecione o tipo *template*, em **Importação de TXT - Tipo de arquivo**(Tela 88 A), conforme a origem da definição da tabela.  
   1. Arquivo padrão *–*utilizado quando a definição da tabela é a mesma do dicionário de dados, preenchendo os dados solicitados.  
      * **Parâmetros** – identifica uma *Pergunte* definida no dicionário de dados do *Protheus*;
      * **Alias** (Tela 88 B) – no caso de arquivo padrão, este será utilizado para localizar as definições no dicionário de dados, caso seja arquivo específico este será utilizado para identificar a área de trabalho (*select area*);
      * A ordem de leitura dos dados é definido por uma das opções:  
        + **Utilize índice padrão** (Tela 88 C)– indica qual o número do índice do dicionário de dados, associado ao alias, que será utilizado ;
        + **Utiliza índice temporário** (Tela 88 D) – informe uma expressão AdvPL válida para indicar a ordem dos dados. Este índice é de uso temporário, sendo eliminado após o seu uso.

Arquivo específico – utilizado para uma estrutura livre da tabela.  
  
  
*Tela 89: Parâmetros para importação do arquivo texto definido*

* + **Parâmetros** (Tela 89 A) – identifica uma *Pergunte* definida no dicionário de dados do *Protheus*;
  + **Estrutura** (Tela 89 B) - utilizado para definir a estrutura da tabela. Utilize os botões a direita para adicionar ou remover atributos (campos).
  + **Indexado** (Tela 89 C) – se marcado indica que a tabela será ordenada pela expressão *AdvPL* informada em **Chave**.

2. Após preencher os dados, avance para a página seguinte;  
3. Nesta página do assistente de código, você complementa os dados detalhando como é o arquivo texto de entrada.

a) Arquivo Texto (89) - Indique a origem dos demais dados, podendo ser:

* + 1. - Definido (Tela 89 A) – os valores são fixos e informados logo abaixo;
       - Parametrizado (Tela 90 A) – os valores serão lidos a partir de uma variável (normalmente de escopo privado (*private*)).  
           
           
                      Tela 90: Definição dos parâmetros para importação de arquivo texto
       - Informe os demais campos conforme solicitado (Tela 89 B e C, Tela 90 B e C)b)  Posições – será utilizado para definir o *layout*do arquivo de saída.

                                                              Tela 91: Definição do *layout* do arquivo de saída

Defina o *layout* informando os dados Campo, posição, tamanho, número de decimais e tipo. Para adicionar ou remover campos, utilize os botões do lado direito.

             *Tela 92: Código gerado pelo assistente para importação de arquivos textos*

*Ao preencher todos os dados obrigatórios solicitados, finalize. Você obterá algo semelhante a Tela 92. Localize a entrada de função user function* e coloque um nome mais significativo, salve e compile.

# Assistente de código: Processamento genérico

Este tipo de assistente o auxilia a criar arquivos-fontes, com um esqueleto para processamentos genéricos.

      *Tela 93: Iniciando o assistente de código para processamento genérico*

1. Selecione o tipo *template*, em **Processamento Genérico - Tipo de arquivo** (Tela 93 A), conforme a origem da definição da tabela.  
   1. Arquivo padrão *–*utilizado quando a definição da tabela é a mesma do dicionário de dados, preenchendo os dados solicitados.  
      * **Parâmetros** – identifica uma *Pergunte* definida no dicionário de dados do *Protheus*;
      * **Alias** (Tela 93 B) – no caso de arquivo padrão, este será utilizado para localizar as definições no dicionário de dados, caso seja arquivo específico este será utilizado para identificar a área de trabalho (*select area*);
      * A ordem de leitura dos dados é definido por uma das opções:  
        + **Utilize índice padrão** (Tela 93 C)– indica qual o número do índice do dicionário de dados, associado ao alias, que será utilizado ;
        + **Utiliza índice temporário** (Tela 93 D) – informe uma expressão *AdvPL* válida para indicar a ordem dos dados. Este índice é de uso temporário, sendo eliminado após o seu uso.
   2. Arquivo específico – utilizado para uma estrutura livre da tabela.  
        
      *Tela 94 : Configuração de arquivo específico*  
        
      * **Parâmetros** (Tela 94 A)– identifica uma *Pergunte* definida no dicionário de dados do *Protheus*;
      * **Estrutura** (Tela 94 B) - utilizado para definir a estrutura da tabela. Utilize os botões a direita para adicionar ou remover atributos (campos).
      * **Indexado** (Tela 94 C) – se marcado indica que a tabela será ordenada pela expressão *AdvPL* informada em **Chave**.
2. Após preencher os dados, finalize.

Ao preencher todos os dados obrigatórios solicitados, finalize. Você obterá algo semelhante a Tela 95. Localize a entrada de função *user function* e coloque um nome mais significativo, salve e compile.

              *Tela 95 : Janela após execução do assistentes para processamento genérico*
