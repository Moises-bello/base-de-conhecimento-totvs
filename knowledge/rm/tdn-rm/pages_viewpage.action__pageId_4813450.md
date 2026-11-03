---
content_hash: 34bd0742c22ef391cd825d7988342513b0e0719b8b0d4f76764b9637928bd656
fetched_at: '2026-06-29T00:10:19.351690+00:00'
page_id: '4813450'
product: rm
source: tdn-rm
title: Gráfico - Consumo de materiais por centro de custo no mês
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813450
version: 6
---

BLOCK

Gráfico - Consumo de materiais por centro de custo no mês

FAQ: **Gráfico - Consumo de materiais por centro de custo no mês**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.20 |

Avaliação

***Como Fazer***

Como parametrizar o sistema para utilizar gráficos como anexo do produto informando o consumo deste produto por Centro de Custo.

Solução

***Descrição do Processo***

Tem por finalidade a obtenção de informação em forma gráfica como anexo do produto.

É necessário que haja um critério para configuração dos Gráficos, visto que, ao utilizar uma consulta SQL muito complexa o desempenho do sistema pode ficar comprometido na execução deste gráfico.

O Gráfico será visualizado manualmente através dos Anexos do Produto, obedecendo à configuração realizada no mesmo e o retorno da consulta SQL.

Importante:

- Para configurar o Gráfico o usuário deverá acessar o aplicativo através da **Nova MDI**.

- Caso a consulta vinculada ao gráfico não retorne nenhum valor o sistema emitirá a seguinte mensagem:

[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQJLtf-j1xI/AAAAAAAAFIo/LjVhngK_Z5A/image_thumb%5B1%5D.png?imgmax=800 "image")](http://lh3.ggpht.com/_G7KXZLoZDsY/TQJLstAyOuI/AAAAAAAAFIk/aW0miJrK-D8/s1600-h/image%5B1%5D.png)

***Parametrizações Necessárias***

Acessar diretório **| CORPORERM\RM.NET |** e clicar no ícone |[![image](http://lh5.ggpht.com/_G7KXZLoZDsY/TQJLun4g-qI/AAAAAAAAErk/5K_RHofJ4Ds/image_thumb%5B1%5D.png?imgmax=800 "image")](http://lh6.ggpht.com/_G7KXZLoZDsY/TQJLtzN4lPI/AAAAAAAAErg/W3SiYOfhRvs/s1600-h/image%5B5%5D.png) | para acessar Nova MDI. A seguir clicar no ícone |[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQJLwF9o_EI/AAAAAAAAErs/Xe5p0VuVQtk/image_thumb%5B2%5D.png?imgmax=800 "image")](http://lh3.ggpht.com/_G7KXZLoZDsY/TQJLvBCkBhI/AAAAAAAAEro/TfUzFmS3vsk/s1600-h/image%5B8%5D.png) | e escolher opção **| Serviços Globais |**

Acessar o menu **| Gestão | Visões de Dados |** **Inserir |** e cadastrar Consulta SQL que será considerada para geração deste Gráfico com o conteúdo:

**SELECT** TP.CODIGOPRD, TP.NOMEFANTASIA, **ROUND** (**SUM**(TR.PERCENTUAL\*TI.QUANTIDADE/100),2) **AS** QUANTIDADE\_CONSUMIDA, GC.CODCCUSTO, GC.NOME

**FROM** TITMMOVRATCCU TR

**INNER** **JOIN** TITMMOV TI

**ON** TR.IDMOV = TI.IDMOV

**AND** TR.CODCOLIGADA = TI.CODCOLIGADA

**AND** TR.NSEQITMMOV = TI.NSEQITMMOV

**INNER** **JOIN** TPRD TP

**ON** TI.IDPRD = TP.IDPRD

**AND** TR.CODCOLIGADA = TI.CODCOLIGADA

**AND** TP.IDPRD=:IDPRD

**INNER** **JOIN** GCCUSTO GC

**ON** TR.CODCCUSTO = GC.CODCCUSTO

**AND** TR.CODCOLIGADA = TI.CODCOLIGADA

**INNER** **JOIN** TMOV TM

**ON** TI.IDMOV = TM.IDMOV

**AND** TR.CODCOLIGADA = TI.CODCOLIGADA

**AND** **DATEPART**(MM, TM.DATASAIDA) = **DATEPART**(MM, **GETDATE**())

**INNER** **JOIN** TTMV TT

**ON** TM.CODTMV = TT.CODTMV

**AND** TT.CLASSIFICACAO = '04.04.05'

**AND** TT.CODCOLIGADA = TI.CODCOLIGADA

**GROUP BY** TP.CODIGOPRD, TP.NOMEFANTASIA, GC.CODCCUSTO, GC.NOME

Importante:

- A consulta em questão demonstra a quantidade de materiais consumida por Centro de Custo no mês corrente, levando em consideração os tipos de movimentos cuja etapa **| Mov-Identificação |,** parâmetro **|** **Classificação |** está informado *Baixa de Estoque**,*** que no banco de dados corresponde a *'04.04.05'* .

Acessar menu **| Gestão**, clicar no ícone |[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQJLxbJHlnI/AAAAAAAAEr0/v3ADqyddXEg/image_thumb%5B3%5D.png?imgmax=800 "image")](http://lh6.ggpht.com/_G7KXZLoZDsY/TQJLwtCBYwI/AAAAAAAAErw/PFxE5lnuN1k/s1600-h/image%5B11%5D.png) | e escolher opção **| Incluir |** para cadastrar e configurar o Gráfico.

Ao escolher opção “Incluir Gráfico” será apresentada tela com parametrizações específicas para geração do Gráfico, onde deve ser informado:

**Aba – Identificação**

Preencher Título, Descrição, Categoria, Fonte de Dados e a Consulta SQL.

**- Consulta SQL:** campo de preenchimento obrigatório, onde o usuário tem que referenciar a consulta SQL inclusa anteriormente, onde o resultado apresentado vai determinar a montagem do Gráfico.

[![image](http://lh4.ggpht.com/_G7KXZLoZDsY/TQJLzFBdQ2I/AAAAAAAAFI4/tt-Kjb77XCw/image12_thumb.png?imgmax=800 "image")](http://lh3.ggpht.com/_G7KXZLoZDsY/TQJLyX9rnoI/AAAAAAAAFIw/1wfENj5qwFM/s1600-h/image12%5B1%5D.png)

|  |
| --- |
| O usuário deve clicar em [image](http://lh4.ggpht.com/_G7KXZLoZDsY/TQJL0AaldaI/AAAAAAAAEsA/18MyMKcU5sA/s1600-h/image%5B17%5D.png)  e escolher a sentença SQL inclusa anteriormente no aplicativo para este fim. Esta consulta vai selecionar os movimentos que se adequam ao resultado da consulta para geração do Gráfico.  Se a consulta em questão utilizar parâmetros o usuário deverá informá-los no momento de execução do gráfico ou na parametrização do Gráfico como anexo do Produto. |

Tela Configurada

[![image](http://lh6.ggpht.com/_G7KXZLoZDsY/TQJL4fUqddI/AAAAAAAAFJM/gOayHxL8gSo/image18_thumb.png?imgmax=800 "image")](http://lh6.ggpht.com/_G7KXZLoZDsY/TQJL2ZYWt_I/AAAAAAAAFJA/SkfocwmrrcE/s1600-h/image18%5B1%5D.png)

Importante:

Ao salvar a tela acima, o sistema perguntará se o usuário deseja executar o assistente de configuração de gráfico.

[![image](http://lh4.ggpht.com/_G7KXZLoZDsY/TQJL7ET9agI/AAAAAAAAFJY/Z0lk6zLTNQs/image21_thumb.png?imgmax=800 "image")](http://lh6.ggpht.com/_G7KXZLoZDsY/TQJL51-MypI/AAAAAAAAFJQ/HxnlkVgl9rw/s1600-h/image21%5B1%5D.png)

***Configuração do Gráfico***

Depois de feitas parametrizações anteriores, o Gráfico deverá ser modelado através do wizard para sua execução posterior.

**Primeira etapa:**

Informar o tipo de gráfico a ser utilizado, no exemplo PIZZA.

[![image](http://lh4.ggpht.com/_G7KXZLoZDsY/TQJL-WAQL7I/AAAAAAAAFJs/o6NoG2ZdEpc/image24_thumb.png?imgmax=800 "image")](http://lh4.ggpht.com/_G7KXZLoZDsY/TQJL8XFAjhI/AAAAAAAAFJg/u36lmiaAc7k/s1600-h/image24%5B1%5D.png)

**Segunda etapa:**

Nessa etapa, especificam-se os dados que serão visíveis no gráfico (legenda, valores, etc.)

[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQJMDQLXC9I/AAAAAAAAFJ4/IB_rAFApBpw/image27_thumb.png?imgmax=800 "image")](http://lh5.ggpht.com/_G7KXZLoZDsY/TQJMCe-9IrI/AAAAAAAAFJw/FN3HZ8DwcdE/s1600-h/image27%5B1%5D.png)

**Terceira etapa:**

Definição de títulos.

***Gráfico Anexo ao Produto***

Após a criação e configuração do gráfico, este deve ser identificado com anexo do produto, uma vez que na consulta SQL é passado por parâmetro o IDPRD do produto.

Acessar o menu | **Produto** | para listagem dos produtos cadastrados na base de dados. Ainda no cadastrado de produto, menu | **Anexos** | **Gráficos** | **Inserir Gráfico**, onde será acionado um wizard para configuração do anexo do produto.

**Primeira etapa:**

Informação do Gráfico criado anteriormente e que será o anexo do produto.

[![image](http://lh5.ggpht.com/_G7KXZLoZDsY/TQJMFppA6EI/AAAAAAAAFKI/ytKV1bU9OkU/image30_thumb.png?imgmax=800 "image")](http://lh4.ggpht.com/_G7KXZLoZDsY/TQJMEA5pFzI/AAAAAAAAFKE/qEN1_F47lsg/s1600-h/image30%5B1%5D.png)

**Segunda etapa:**

Identificação dos parâmetros passados na consulta SQL e que serão necessários para montagem do gráfico. No exemplo, o Valor passado será o IDPRD.

[![image](http://lh5.ggpht.com/_G7KXZLoZDsY/TQJMIgNkb8I/AAAAAAAAFKc/N-ylaNf_1qE/image33_thumb.png?imgmax=800 "image")](http://lh6.ggpht.com/_G7KXZLoZDsY/TQJMHZ4OngI/AAAAAAAAFKM/uRLNzLREUpw/s1600-h/image33%5B1%5D.png)

**Terceira etapa:**

Definição do(s) perfil(s) que terá acesso ao anexo configurado.
