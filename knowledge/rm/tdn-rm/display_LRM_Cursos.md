---
content_hash: 50889c2215ff0dba6ef051ce9a0cc606b4ef941ae2cca0fd2e79468e7f999ce3
fetched_at: '2026-06-29T00:09:36.023333+00:00'
page_id: '425459457'
product: rm
source: tdn-rm
title: Cursos
type: documentation
url: https://tdn.totvs.com/display/LRM/Cursos
version: 32
---

O cadastro de curso difere de acordo com o contexto selecionado. Verifique abaixo as regras de acordo com o [nível de ensino](http://tdn.totvs.com/x/2PtbGQ).  
   
**Contexto Ensino Superior**  
   
**Identificação**  
**Código INEP** Código da Instituição de Ensino no Censo Escolar (INEP). **Configuração do RA** É possível configurar uma máscara para o RA (Registro Acadêmico) do aluno. Todo aluno matriculado nesse curso terá o RA definido de acordo com a máscara informada. Obs.: Esta configuração pode ser definida nos parâmetros do sistema. **Obs.:** A parametrização da máscara do RA do aluno pode ser definida pelo Nível de Ensino ou pelo Curso.  
**Modalidade** É a modalidade do curso ofertado pela Instituição. **Por exemplo: Graduação**  
   
**Capes** A Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES) desempenha papel fundamental na expansão e consolidação da pós-graduação stricto sensu (mestrado e doutorado) em todos os estados da Federação. Para maiores informações consulte o site da [Capes](http://www.capes.gov.br/).  
   
**Presencial/Distância**  
Se o curso é ministrado na modalidade Presencial ou a Distância

**Obs.** A partir das versões 12.1.2410.292, 12.1.2502.195 e 12.1.2506.137, a Instituição passa a contar, além das modalidades Presencial e a Distância, também com a modalidade Semipresencial, ampliando as opções de ensino disponíveis.

Adequação à Reforma Tributária (IBS) - Cursos Semipresenciais

A partir das versões **12.1.2502, 12.1.2506.199 e 12.1.2510.131,** foi disponibilizado o campo **'Regra de emissão da NFe'** para cursos de **Ensino Superior na modalidade Semipresencial.** O preenchimento deste campo é necessário para definir o Local da Operação para cálculo do IBS:

* **Regra EAD:** Considera o município do Aluno como local da operação.
* **Regra Presencial:** Considera o município da Filial como local da operação.

**Escola**  
Algumas instituições de ensino possuem esse conceito, como exemplo: **O curso de Artes Plásticas faz parte da Escola de Artes**  
   
**Área**  
Qual área o curso se enquadra. **Por Exemplo: Biológica - Exatas**  
   
**Máscara da turma**  
O TOTVS Educacional possibilita que a instituição crie uma máscara para as turmas de cada curso. Por Exemplo: Todas as turmas de Direito terão o prefixo "DIR" + um sequencial - Desta forma a instituição consegue manter um padrão.    
A configuração da máscara a ser aplicada é bastante flexível atendendo a necessidade das Instituições de Ensino de acordo com a sua regra de negócio.  
   
No quadro abaixo é demonstrado as possibilidades de personalização.

|  |  |
| --- | --- |
| **CÓDIGO** | **DESCRIÇÃO** |
| **&** | Esse caractere representará o período letivo. Para definir na máscara o período letivo 2022/1, por exemplo deverá ser escrito &&&&&& um símbolo para cada caractere. |
| **#** | Sequencial simples, se o usuário quiser que haja um sequencial para as turmas, basta colocar este símbolo a quantidade de vezes que desejar. |
| **Letras e números** | Poderá ser usado qualquer letra e/ou número na montagem da máscara, exemplo: Imagine que as turmas serão montadas com o nome "TURMA"+ sequencial então:  a máscara será  **TURMA ###** simplesmente. |
| **[ ]** | Todos os códigos listados abaixo, são letras e sinais, para que o sistema entenda-os como  códigos, eles devem estar entre colchetes "**[**" e "**]**". Cada grupo deste será entendido como SESSÃO. |
| **c** | A letra 'c' minúscula, representa o código do curso. Suponha que o código do curso  seja 167. Para defini-lo na máscara, deverá ficar assim **[**ccc**]**. |
| **C** | A letra 'C' MAIÚSCULA, representa o nome do curso, lembrando que cada letra representa um caractere do nome. Para parametrizar uma descrição DIR (DIREITO) deverá ficar assim **[**CCC**]**. |
| **h** | Código da Habilitação. O funcionamento é o mesmo do código do curso |
| **H** | Nome da habilitação. O funcionamento é idêntico ao nome do curso. |
| **m** | Código da Matriz Curricular |
| **O** | Descrição do tipo do turno da turma (Matutino, Vespertino, etc) |
| **M** | Nome da Matriz Curricular |
| **t** | Código do Turno |
| **T** | Nome do Turno |
| **p** | Código do Período da Disciplina |

**Observação:**

As letras utilizadas no quadro acima, se utilizadas fora dos colchetes serão apenas letras comuns, portanto se o usuário precisar utiliza-las como letras, basta não colocar os colchetes que indicam inicio e término de sessão.   
  
**Exemplo:**  
Curso: SISTEMAS DE INFORMAÇÃO   
Habilitação: PROGRAMAÇÃO  
Período Letivo: 2022/1  
Turno: Manhã  
  
Máscara = **[CCC][HHHH]-&&&&&&-[p]-###-[T]**

|  |  |  |
| --- | --- | --- |
| **CÓDIGO** | **DESCRIÇÃO** | **RESULTADO** |
| [CCC] | 3 primeiros caracteres do nome do curso | SIS |
| [HHHH] | 4 primeiros caracteres da habilitação | PROG |
| - | Hífen | - |
| &&&&&& | 6 primeiros caracteres do período letivo | 2022/1 |
| [p] | Caractere do período da disciplina | Período da Disciplina |
| - | Hífen | - |
| ### | Sequência normal, começando com | 001 |
| - | Hífen | - |
| [T] | Primeiro caractere do nome do turno | M |

Portanto a máscara da primeira turma seria: **SISPROG-2022/1-1-001-M**.  
   
Suponha que o usuário queira somente informar a nomenclatura **SISPROG**, ao invés do Nome do Curso + Habilitação, seria necessário somente escrever **SISPROG** (sem os colchetes) para que a máscara fosse parametrizada com a escrita da nomenclatura.  
   
Obs.: Para que seja utilizado as máscaras parametrizadas, o campo **TURMA** no cadastro de [Turma](http://tdn.totvs.com/x/yP1bGQ) e/ou [Turma/Disciplina](http://tdn.totvs.com/x/C-9bGQ) precisa estar com o valor **ZERO** ao se fazer o cadastro.  
   
Exemplificando essa regra:

1. Se o campo Turma estiver com valor diferente de **ZERO**, o sistema utiliza o que foi cadastrado;
2. Se o campo Turma estiver com valor igual a **ZERO**, o sistema procura no cadastro do curso em questão e monta o código da turma de acordo com a máscara parametrizada.
3. Se não houver máscara parametrizada, o sistema informa que a máscara não foi cadastrada.

| **Observação importante:** Os códigos gerados para as turmas podem se repetir em períodos letivos diferentes. |
| --- |

Os colchetes não são considerados na contagem do número de caracteres na máscara da turma no cadastro do curso, ou seja, se a máscara informada for [ c ], então ao invés de contar 3 caracteres, irá contar apenas um. Entretanto, uma validação foi inserida para quando a máscara informada gerar um código de turma maior que 20 caracteres, uma mensagem será exibida para o usuário, informando tal situação. Além disso, um ícone de informação foi colocado ao lado do campo de máscara, com intuito de mostrar todas as opções disponíveis de personalização da máscara, com isso, não é mais exibido estas opções parando o ponteiro do mouse em cima do campo, e sim parando o ponteiro em cima do ícone.

A partir da versão 12.1.2510.127, houve uma alteração na máscara do curso**:** o número sequencial passou a ser iniciado pela combinação *Período Letivo/Curso*.  
Além disso, foi incluída uma nova *tag* [O], que corresponde à descrição do tipo de turno.

A partir da versão 12.1.2510, o campo *Modalidade* passa a se chamar *Nível/Categoria*. Já o campo *Presencial/Distância* foi renomeado para *Modalidade*.

Sequencial do código da turma

A partir das versões **12.1.2510,** foi criada nova aba separada para o cadastro da máscara da turma, bem como novo campo de tipo de sequencial:

* **Período letivo e curso:** Sequencial único para combinação de período letivo e curso
* **Regra Presencial:** Sequencial único para combinação de período letivo, curso e período da disciplina. **Obs**: Se a definição parametrizada for por **Período Letivo/Curso/Período**, deve-se validar se essa tag **Período [p]** está na máscara pois ela passa a ser obrigatória.

Foi disponibilizado um parâmetro que permite definir se o valor sequencial é **numérico** ou **alfabético**.

Por padrão, o comportamento atual — **sequencial numérico** — permanece configurado como valor *default*, garantindo compatibilidade com os modelos existentes.

### Comportamento do sequencial

* **Numérico**:  
  Quando houver mais de uma tag `#` consecutiva, o valor deve ser preenchido com zeros à esquerda, respeitando a quantidade de caracteres definida, e incrementado de forma sequencial.  
  *Exemplo:* `##` → `01`, `02`, `03`, ...
* **Alfabético**:  
  Não há preenchimento com caracteres adicionais. Tanto a utilização de `#` quanto de `##` gera inicialmente o valor `A`, seguido de `B`, `C`, e assim sucessivamente.

Funcionalidade disponível a partir da versão 12.1.2510.157.

 Informações Complementares

---

 Veja Também

---

[Boletim Técnico - Máscara da turma](http://tdn.totvs.com/download/attachments/147816888/EDU_BT_Mascara_Turma_001453.pdf?version=1&modificationDate=1405368013000)
