---
content_hash: f75577c89ab42c03f1544d83433b8823b6c4b3fb78564471eb21d9e12f372246
fetched_at: '2026-06-29T00:10:19.553185+00:00'
page_id: '4815179'
product: rm
source: tdn-rm
title: Importar Gabaritos no Processo Seletivo
type: documentation
url: https://tdn.totvs.com/display/LRM/Importar+Gabaritos+no+Processo+Seletivo
version: 4
---

BLOCK

Importar Gabaritos no Processo Seletivo

FAQ: **Importar Gabaritos no Processo Seletivo**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.20 |

Avaliação

**Processo de Importar Gabaritos no Processo Seletivo**

**[![file-edit](http://lh5.ggpht.com/_G7KXZLoZDsY/TVKdLPDWhJI/AAAAAAAAGWw/USFkf7hJK98/file-edit_thumb%5B8%5D.png?imgmax=800 "file-edit")](http://lh3.ggpht.com/_G7KXZLoZDsY/TVKdKUwzlFI/AAAAAAAAGWs/_bOUA1xy0Q4/s1600-h/file-edit%5B10%5D.png)**Após a execução das provas, os gabaritos preenchidos pelos candidatos serão digitalizados por meio de leitura ótica. A digitalização dos gabaritos é um trabalho feito pela própria instituição ou por um serviço terceirizado.

Para saber a resposta correta da prova para comparar com a do candidato basta uma consulta:

*select \* from BOPCAO where codarea =(x) and codmateria =(x) and indcorreta='T'*.

Para saber a resposta do candidato: *select \* from BHISTRESPPROVA where id=(x)*, esse id deverá ser o mesmo gerado para a pessoa na tabela BEXECPROVA.

Com o resultado da digitalização serão gerados arquivos em formato TXT. O processo de Importar Gabaritos permite que os arquivos gerados sejam lidos para que os dados dos gabaritos sejam introduzidos no sistema.

Solução

**[![ligth-on](http://lh3.ggpht.com/_G7KXZLoZDsY/TVKdL0sJ_6I/AAAAAAAAGW4/kzbTUwm_zPk/ligth-on_thumb%5B2%5D.png?imgmax=800 "ligth-on")](http://lh5.ggpht.com/_G7KXZLoZDsY/TVKdLqS8tQI/AAAAAAAAGW0/lMG8eya7_WU/s1600-h/ligth-on%5B4%5D.png) Como fazer...**

**Acesse: Processo seletivo/Processos/Importar gabaritos**

[![clip_image002](http://lh5.ggpht.com/_G7KXZLoZDsY/TVKdNc7pMkI/AAAAAAAAGXA/N3sQlVPYoGY/clip_image002_thumb%5B3%5D.jpg?imgmax=800 "clip_image002")](http://lh5.ggpht.com/_G7KXZLoZDsY/TVKdM7IXytI/AAAAAAAAGW8/jp2BpzyYx9k/s1600-h/clip_image002%5B10%5D.jpg)

**Pré – requisitos para utilização deste processo**:

Existem dois tipos de arquivos de gabaritos que poderão ser lidos no processo em questão.

O primeiro poderá ser gabaritos com respostas de questões fechadas. Arquivos deste tipo serão gerados de acordo com o layout “Arquivos de Importação de Gabaritos – Questões Fechadas”:

|  |  |  |
| --- | --- | --- |
| **Coluna** | **Descrição** | **Obrigatório?** |
| INDICADOR | Indicador de tipo de arquivo. Para esse layout trará sempre o valor “P” | Sim |
| CODCOLIGADA | Código da coligada | Sim |
| IDPS | Código do processo seletivo | Sim |
| IDETAPA | Código da etapa | Sim |
| NUMERO\_CARTAO | Número do cartão de repostas | Não |
| NUMERO\_INSCRICAO | Número da inscrição | Sim |
| RESPOSTA\_CANDIDATO | Seqüência de respostas do candidato. Respeita a ordem das questões no caderno de prova. Poderá conter:  1 - alternativas à A,B,C,D...;  2 - asterisco "\*" à Quando o candidato marcar mais de uma alternativa para a questão, ou seja, anulou a questão;  3 - espaço em branco à O candidato não marcou nenhuma das alternativas, ou seja, anulou a questão.  Exemplo de conteúdo:  “B \*EEEEDECA BAACBCBEE” | Sim |
| QTD\_QUESTÕES | Quantidade de questões | Sim |

O segundo tipo de arquivo será utilizado para importação de gabaritos com notas de questões abertas. Esse tipo de arquivo será utilizado na leitura de notas redação. Esses arquivos serão gerados de acordo com o layout Arquivos de Importação de Gabaritos - Questões Abertas.

|  |  |  |
| --- | --- | --- |
| **Coluna** | **Descrição** | **Obrigatório?** |
| INDICADOR | Indicador de tipo de arquivo. Para esse layout trará sempre o valor “R” | Sim |
| CODCOLIGADA\_1 | Código da coligada | Sim |
| IDPS\_1 | Código do processo seletivo | Sim |
| IDETAPA\_1 | Código da etapa | Sim |
| NUMERO\_CARTAO\_1 | Número do cartão de respostas | Não |
| NUMERO\_INSCRICAO\_1 | Número da inscrição | Sim |
| C\_1\_R\_1 | Nota da prova aberta número 1 | Sim |
| C\_1\_R\_2 | Nota da prova aberta número 2 | Não |

O assistente exibirá uma tela de configuração:

[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TVKdOTypGlI/AAAAAAAAGXI/egSoi9QsPI4/clip_image002%5B4%5D_thumb%5B2%5D.jpg?imgmax=800 "clip_image002[4]")](http://lh6.ggpht.com/_G7KXZLoZDsY/TVKdN8Bs6aI/AAAAAAAAGXE/GcL5Dkh3yms/s1600-h/clip_image002%5B4%5D%5B4%5D.jpg)

Se o sistema detectar que o arquivo a ser lido é gabarito de questões abertas, ou seja, prova de redação, será apresentado o passo adicional do assistente chamado “Preenchimento padrão para resposta de redação”. Nessa tela o usuário poderá entrar com um texto. Esse texto será armazenado no TOTVS Avaliação e Pesquisa para que seja mantido um histórico sobre qual era a resposta esperada.

[![](http://lh6.ggpht.com/_G7KXZLoZDsY/TVKdP2lcuqI/AAAAAAAAGXQ/HIjw7xMvvBo/clip_image002%5B6%5D_thumb%5B2%5D.jpg?imgmax=800 "clip_image002[6]")](http://lh6.ggpht.com/_G7KXZLoZDsY/TVKdPA5nm0I/AAAAAAAAGXM/EkYRnd7l3xc/s1600-h/clip_image002%5B6%5D%5B4%5D.jpg)

O *Log* do processo irá exibir informações sobre cada um dos gabaritos que foi importado durante a execução. Em caso de falha de importação, o *Log* apresentará também mensagens indicando dos seguintes motivos para cada um dos gabaritos não importado:

1. Não foi encontrado cadernos de provas distribuídos vinculados à inscrição.
2. Gabarito já importado em processamentos anteriores.
3. Dados da linha já processados na execução atual, indicando duplicidade de informações para uma mesma inscrição no arquivo.
4. Número de inscrição que foi obtido da linha no arquivo não existe no processo seletivo que está sendo processado.
5. A inscrição existe, mas está cancelada. Por isso, os dados não são importados.

Após realizar a importação de gabaritos, se for gabarito de questões fechadas o próximo passo será executar a rotina de correção de provas no anexo “Ranking” do cadastro de provas no TOTVS Avaliação e Pesquisa.

Quando a prova for de redação, ou seja, questões abertas, não será necessário executar a correção de provas no TOTVS Avaliação e Pesquisa. Essa rotina é válida somente para provas com questões fechadas.
