---
article_id: 360022456591
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 1ca8fd33c1d9d2d1aa6131e0154757634316841c27ee6599bb680d188f842cfd
fetched_at: '2026-06-28T22:39:08.174970+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Conceito e utilização
  de Grade de Produtos no Protheus
type: support-article
updated_at: '2026-05-22T14:32:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022456591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-utiliza%C3%A7%C3%A3o-de-Grade-de-Produtos-no-Protheus
---

O recurso Grade de Produtos no Protheus agiliza o cadastro de produtos com variações, como cor e tamanho, gerando automaticamente os produtos variáveis a partir do principal. É necessário configurar parâmetros como MV\_GRADE, MV\_MASCGRD e MV\_ORDGRDP. O cadastro envolve tabelas para linhas (cores) e colunas (tamanhos) e a criação da grade que combina essas variações, gerando códigos únicos conforme a máscara definida. Produtos gerados mantêm características do produto principal e o sistema diferencia produtos por campo B1\_GRADE.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40210879024535) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Qual o conceito e como funciona o processo de Grade de Produtos (MATA551) no *Protheus*?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O recurso de Grade agiliza o trabalho de cadastramento de produtos que variam em apenas alguns aspectos, mantendo a sua característica principal. Desta forma, não é preciso cadastrar o mesmo produto diversas vezes apenas porque, por exemplo, o produto possui uma variedade de cores. O usuário precisa apenas cadastrar o produto principal e todas as suas variáveis, tais como: cor, modelo, etc, e  
então, o Protheus gera, automaticamente, todos os cadastramentos dos produtos variáveis.

**O que é necessário para utilizar Grades de Produtos?**

Para utilizar a rotina Grades de Produtos é preciso antes efetuar algumas configurações no sistema:

**Configurar os parâmetros:**

"**MV\_GRADE**" - Este parâmetro define se o sistema utilizará grade de produto ou não. Para utilizá-lo, o mesmo deve estar com conteúdo = T

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406744253591)

"**MV\_MASCGRD**" - Define a composição máscara do código de produtos gerados automaticamente.

Em um cenário onde possui o campo B1\_COD de tamanho 15, o parâmetro poderia ficar desta forma:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406750186263)

Onde:

11 = Tamanho do código inicial do Produto

02 = Tamanho do código **da linha** da grade

03 = Tamanho do código **da coluna** da grade

Mais adiante, neste mesmo artigo, traremos um exemplo prático para fixar este conceito.

|  |
| --- |
| **Observação Importante:** |
| **É altamente recomendável definir de forma fixa a usabilidade da codificação do parâmetro MV\_MASCGRD. Pois, em cenários em que o cliente já possui Grades cadastradas e vê a necessidade de alteração da Máscara da Grade, esta alteração afetará as grades anteriormente cadastradas, sendo necessária a criação de nova grade para respeitar a nova codificação da Máscara.** |

"**MV\_ORDGRDP**" -  Indica se os códigos das tabelas de linha e coluna da grade de produtos devem ser ordenados automaticamente. É recomendável estar com conteúdo = .T.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406757934359)

**Cenário para prática da criação de uma Grade de Produtos**

Uma empresa de moda oferece uma variedade de cores e tamanho para calças de moletom. O conteúdo da calça é um só (moletom), mas temos uma variação de cores e tamanhos. As opções são:

* **Tamanhos**
  + 34, 36, 38, 40, 42, 44 e 46
* **Cores**
  + Preta, branca, bege, azul, verde, rosa e amarelo.

**Cadastro da Tabela da Grade**

O primeiro passo será cadastrar as tabelas de Cores e Tamanhos, que são as duas características das calças. Primeiro definimos a tabela matricial (linhas e colunas), onde em nosso exemplo ficará desta forma:

* **Colunas**
  + **Cores**
    - Preta, branca, bege, azul, verde, rosa e amarelo.
* **Linhas**:
  + **Tamanhos**
    - 34, 36, 38, 40, 42, 44 e 46

Para criarmos a tabela, vamos acessar ao **módulo 04 - Estoque Custos -> Atualizações -> Cadastros -> Engenharia ->  Grade de Produtos -> Tabelas (MATA551)** e cadastrarmos as Linhas e Colunas

Cadastro das **Cores** nas linhas:

![tabela_cores_grade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4406762801303)

Cadastro dos **Tamanhos** nas colunas:

![cadastro_colunas_tamanho_grade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4406763104791)

**Cadastro da Grade combinando os dados das linhas e colunas**

Com a tabela feita, o próximo passo é criar a Grade em si para geração dos códigos. Para isso, vamos acessar ao **módulo 04 - Estoque Custos -> Atualizações -> Cadastros -> Engenharia ->  Grade de Produtos -> Grades (MATA550)** e cadastrarmos a Grade.

![cadastro_da_grade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4406753122967)

**Perceba alguns pontos importantes no Cadastro da Grade:**

- O Sistema permite ao usuário cadastrar a combinação que desejar;

- No Cadastro, o usuário delega qual o código para a linha e para coluna para apresentar posteriormente na grade;

- Os cadastros dos produtos serão gerados conforme as marcações da grade. Perceba que no nosso exemplo, nem todos os tamanhos de calça terão todas as cores, logo, não terão cadastros gerados.

- O código do produto (25252525252) é feito à critério do usuário, onde, neste exemplo deixamos com 11 dígitos para concatenar com os 2 dígitos das cores e os 2 dígitos dos tamanhos

**Resultado do Cadastro dos Produtos oriundos da Grade**

Vamos recapitular nossa grade de Produtos:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406763606295)

Perceba que nossos produtos foram cadastrados exatamente igual às marcações da Grade:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406763482903)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406763631255)

**Dissecando a codificação dos produtos (conceito do parâmetro MV\_MASCGRD)**

Em nosso exemplo, o parâmetro MV\_MASCGRD foi configurado como: 11, 02, 02, então:

11 = Tamanho reservado para o código do produto (Calça)

02 = Tamanho reservado para a linha (Cores)

02 = Tamanho reservado para a coluna (Tamanho)

**Exemplo**

A  calça verde tamanho 40 tem o código **2525252525****05****93**, onde:

**2525252525**= Corresponde ao tamanho 11 reservado ao **código do produto** (Calça)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406753437975)

**05** = Corresponde ao **código da linha** cadastrada (Verde)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406763850007)

**93** **=**Corresponde ao **código da coluna** cadastrada (Tamanho 40)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406763892759)

**Observações importantes sobre Grade de Produtos:**

* O sistema possibilita incluir, alterar, visualizar e excluir as grades de produtos. Este cadastro possui  
  as principais informações do Cadastro de Produtos - SB1, dispensando qualquer manutenção na rotina de Cadastro de Produtos (MATA010);

* Quando incluída uma referência nova na rotina de Grades (MATA551 -  Arquivo de Referências - SB4), o Sistema gera **um novo produto** para cada ponto de grade (Linha, Coluna) no Cadastro de Produto - SB1. Todos os produtos gerados através da mesma referência de grade possuirão as mesmas características cadastrais (Grupo, Armazém, Tipo Entrada e Saída, Valor Unitário, etc).

* Para diferenciar os produtos cadastrados, através das opções “Grades de Produto” e “Produtos” do  
  menu Atualizar, é utilizado o campo (B1\_GRADE) no Arquivo de Produtos (SB1). Quando o  
  cadastramento é efetuado através da opção “Grades de Produto”, o conteúdo deste campo é “S”;  
  caso contrário é “N” ou “ ”.

* **Não é possível** a inclusão de Grade de produtos para produtos com códigos (B1\_COD) existentes no sistema, ou seja, ao implementar essa funcionalidade, é necessário a criação de código (B4\_COD) específico para cada nova grade.  É apresentado o HELP A550PRODB1 alertando que o produto esta cadastrado como Produto Normal. Esse processo é necessário para manter a integridade dos registros existentes no Cadastro do Produto.

* Ao realizar qualquer alteração ou apenas acessar a rotina **Grade de Produto (MATA550)**, os campos do cadastro do produto na tabela **SB1** (por exemplo, o campo **B1\_POSIPI**) são apagados. O que fazer nesse cenário?

No comportamento padrão, ao alterar ou acessar a **Grade de Produtos** pela rotina **MATA550**, os campos são reajustados conforme a estrutura definida na grade. Esse processo é padrão para produtos que utilizam grade, pois o sistema entende que a grade será atualizada e, consequentemente, realiza o ajuste dos componentes relacionados.

Para evitar que ocorram alterações nos dados do cadastro do produto na SB1, existem duas alternativas:

**1ª alternativa:**  
Preencher de forma padrão o campo **B4\_POSIPI**, pois esse conteúdo será replicado para a tabela **SB1**.

**2ª alternativa:**  
Utilizar o ponto de entrada **A550ALTB1**, permitindo customizar o comportamento para impedir alterações nos dados da tabela **SB1**.

***A550ALTB1 - Alterações na Tabela SB1***

[***https://tdn.totvs.com/x/eCMcEQ***](https://tdn.totvs.com/x/eCMcEQ)

***Saiba mais:***

[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)

[SIGAEST - MATA550 - Pontos de Entrada da rotina Grade de Produtos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11927361595799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA550-Pontos-de-Entrada-da-rotina-Grade-de-Produtos)
