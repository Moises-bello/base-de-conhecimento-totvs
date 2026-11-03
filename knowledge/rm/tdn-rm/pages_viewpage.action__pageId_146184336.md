---
content_hash: e4dd728994ee148d5fcca8e0959fd732bab82514c664b18834ae8f76bde13fbc
fetched_at: '2026-06-29T00:05:55.848263+00:00'
page_id: '146184336'
product: rm
source: tdn-rm
title: Expressões
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146184336
version: 69
---

# Índice

---

# Expressões

---

Expressão é um objeto que permite de maneira eficiente a manipulação de dados.

### **Trabalhando com expressões**

**1°)** Para inserir uma expressão ao relatório,  acesse a guia/menus  "**Gestão |** Ferramentas de Análise | **RM Reports".**

**2°)** Depois de carregada a visão, selecione o relatório que irá conter expressões.

**3°)** Depois de selecionado o relatório, é necessário editar sua estrutura. Para realizar a edição de estrutura do relatório, clique em **Processos**, em seguida, **Editar Estrutura.**Depois de carregada a visão, clique na funcionalidade **Expressão** localizada no canto esquerdo e adicione ao relatório.

**4°)** Depois de adicionado ao relatório, clique em **Expressão Tarefas**.

**5°)**  Depois de clicado devemos escolher uma **expressão** e um **formato** que encaixe no padrão da expressão escolhida.

**AddDays():****A expressão AddDays inclui o número especificado de dias no valor do operando Data. Se o número de dias for um número negativo, o número especificado de dias será subtraído do valor de Data.**

Para deixar mais claro a objetividade desta expressão, clique no menu "Dados | **Adicionar Fonte de Dados**"**,**em seguida pesquise pela tabela "**PFUNC",** no campo **Pesquisar** na coluna **Tabela da Base.**

Depois de pesquisado, vamos adicionar a tabela **Funcionários.**Clique em "**Totvs Folha de Pagamento** | **Funcionários"**em seguida, "**Adicionar | OK".**

Depois de adicionado a tabela iremos utiliza-la na expressão. Clique novamente em "**Expressão Tarefas |** Expressão **| ...******".****

Ao abrir o **Editor de expressão**, clique em " **Funções** **| Data/Hora | AddDays****”.**

Depois de clicado, é necessário passar parâmetro à expressão selecionada. Clique em  **Parâmetros | Base (Campos da Base) | PFUNC (Funcionários) | DATAADMISSAO (Data de Admissão)**.

Depois de adicionado, acrescente após a virgula uma quantidade de dias, para que a expressão calcule a partir da **Data de Admissão**. Em seguida clique em "**OK".** 

Após clicado, observe que foi acrescentado ao relatório a expressão conforme foi configurada.

Depois de adicionada ao relatório, adicione um formato para a expressão. Clique novamente em "**Expressão Tarefas |** Formato **| ...******".****

Ao abrir o **Editor de Formatar Caracter**, clique em "Categoria **| DataHora |** Tipos Padrão **| (Escolha o formato desejado)**"e clique em "**OK"**.

Após adicionar um formato à expressão, basta salvar o relatório e gerar o mesmo. Observe que a data gerada pela expressão, foi exatamente conforme configurado nos passos acima.

### **Principais Expressões 6°)** Observe abaixo as funções das principais expressões disponíveis.

**AddMonths():**A expressão **AddMonths** inclui o número especificado de meses. Se o número de meses for um número negativo, o número especificado de meses será subtraído.

**Exemplo: AddMonths(31/10/2014,7)    Retorna 31/05/2015**

**AddYears():**A expressão **AddYears** inclui o número especificado de anos. Se o número de anos for um número negativo, o número especificado de anos será subtraído.

**Exemplo: AddYears(31/10/2014,4)    Retorna 31/10/2018**

**Trim()**: A expressão **Trim()** remove os espaços em branco à esquerda e direita.

**Exemplo:****Trim(' TOTVS ')    Retorna TOTVS**

**Upper():**A expressão **Upper()** transforma o texto informado para maiúsculo.

**Exemplo: Upper('totvs')    Retorna TOTVS**

**Lower():**A expressão **Lower()**transforma o texto informado para minúsculo.

**Exemplo: Lower('TOTVS')    Retorna totvs**

**Sqr():**A expressão **Sqr()** retorna o número informado elevado ao quadrado.

**Exemplo: Sqr(3) Retorna 9**

**Sqrt():** A expressão **Sqrt()** retorna a raiz quadrada do número informado.

**Exemplo: Sqrt(3)    Retorna 1,7320508075688**

**Replace():**A expressão **Replace()** substitui as ocorrências de um texto por outro, dentro do texto informado

**Exemplo: Replace('amar','am','trabalh')    Retorna trabalhAR**

**Now():** A expressão **Now()**retorna data e hora do sistema

**Exemplo: Now    Retorna 04/07/2014 09:32**

**DayOfWeek():**A expressão **DayOfWeek()**retorna o dia da semana de uma data.

**Exemplo: DayOfWeek(04/07/2014)    Retorna Sexta-Feira**

**Length():**A expressão **Lenght()**retorna tamanho do texto informado.

**Exemplo: Length('totvs')    Retorna 5**

**Abs():**A expressão **Abs()**retorna o valor absoluto do valor informado.

**Exemplo: Abs(-19)    Retorna 19**

**AddHours():**A expressão **AddHours()**retorna o valor de uma hora somada a um número de horas informado.

**Exemplo: AddHours(12:00,2)    Retorna 14:00**

**AddMiliSeconds():**A expressão **AddMiliSeconds()**retorna o valor de um milissegundo somado a um número de milissegundos informado.

**Exemplo: AddMilliseconds(12:00:00:10,2)    Retorna 12:00:00:12**

**AddMinutes():** A expressão **AddMinutes()**retorna o valor de um minuto somado a um número de minutos informado.

**Exemplo: AddMinutes(18:00,51)    Retorna 18:51**

**AddSeconds():** A expressão**AddSeconds()** retorna o valor de um segundo somado a um número de segundos informado.

**Exemplo: AddSeconds(09:00:00,25)    Retorna 09:00:25**

**Cos():**A expressão **Cos()** retorna o cosseno de um ângulo em radianos.

 **Exemplo: Cos(0.5)    Retorna 0,877582561890373**

****Power():****A expressão **Power()**retorna o número especificado elevado à potência especificada.

**Exemplo: Power(10,2)    Retorna 100**

**Remove():** A expressão **Remove()** remove o número especificado de caracteres desta instância, a partir da posição especificada.

**Exemplo: Remove('TOTVS',0,2)    Retorna TVS**

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Expressões

falsefalse

**Status:** Finalizado

false

**Data:** 26/11/2018

false

**Autores:**
