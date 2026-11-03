---
content_hash: 3c20a0ffafc9d4b437756ac171a996afe4a16271e8ce982ee892f4d2478ddb3e
fetched_at: '2026-06-29T00:09:32.697466+00:00'
page_id: '425458902'
product: rm
source: tdn-rm
title: Importar gabaritos
type: documentation
url: https://tdn.totvs.com/display/LRM/Importar+gabaritos
version: 5
---

A digitalização dos gabaritos é um trabalho feito pela própria instituição ou por um serviço terceirizado. Com o resultado da digitalização, serão gerados arquivos em formato TXT. O processo de importação permite que os arquivos gerados sejam lidos para que os dados dos gabaritos sejam introduzidos no sistema. Existem dois tipos de arquivos de gabaritos que poderão ser lidos no processo em questão.

O primeiro tipo conterá dados de gabaritos com respostas de questões fechadas. Será validado o IDPS do processo seletivo, ID Etapa de cada área ofertada e o Número de inscrição. Sem estas informações, ocorrerá inconsistência de dados durante o processo e não será realizado com sucesso.

Se o sistema for parametrizado para não realizar importação de notas de candidatos ausentes no dia da prova, ocorrerá também a validação da presença dos candidatos, se o mesmo for ausente não terá a sua nota importada.

Lembrando que as respostas do candidato são comparadas a resposta correta da prova vinculada a Área ofertada, esta prova é cadastrada e corrigida no TOTVS Avaliação e Pesquisa. Para saber a resposta do candidato basta um select \* from BHISTRESPPROVA where id=, esse id deverá ser o mesmo gerado para a pessoa na tabela BEXECPROVA. Com o resultado da digitalização serão gerados arquivos em formato TXT.

O processo de Importar Gabaritos permite que os arquivos gerados sejam lidos para que os dados dos gabaritos sejam introduzidos no sistema.

Segue o layout da Importação de Gabaritos respostas de questões fechadas:

|  |  |  |
| --- | --- | --- |
| Coluna | Descrição | Obrigatório? |
| INDICADOR | Indicador de tipo de arquivo. Para esse layout trará o valor "P" | Sim |
| CODCOLIGADA | Código da coligada | Sim |
| IDPS | Código do processo seletivo | Sim |
| IDETAPA | Código da etapa | Sim |
| NUMERO\_CARTAO | Número do cartão de repostas | Sim |
| NUMERO\_INSCRICAO | Número da inscrição | Sim |
| RESPOSTA\_CANDIDATO | Seqüência de respostas do candidato. Respeita a ordem das questões no caderno de prova. Poderá conter:  1 - alternativas => A, B, C, D;  2 - asterisco "\*" => Quando o candidato marcar mais de uma alternativa para a questão, ou seja, anulou a questão;  3 - espaço em branco => O candidato não marcou nenhuma das alternativas, ou seja, anulou a questão.  Exemplo de conteúdo: "B \*EEEEDECA BAACBCBEE" | Sim |
| QTD\_QUESTÕES | Quantidade de questões | Sim |

**Ex.:**

INDICADOR;CODCOLIGADA;IDPS;IDETAPA;NUMERO\_CARTAO;NUMERO\_INSCRICAO;RESPOSTA\_CANDIDATO;QTD\_QUESTOES

P;1;29;40;1;1;ABCDEABCD;10

O segundo tipo de arquivo será utilizado para importação de gabaritos com notas de questões abertas. Esse tipo de arquivo será utilizado na leitura de notas redação. Esses arquivos serão gerados de acordo com o layout "Arquivos de Importação de Gabaritos - Questões Abertas".

|  |  |  |
| --- | --- | --- |
| Coluna | Descrição | Obrigatório? |
| INDICADOR | Indicador de tipo de arquivo. Para esse layout trará o valor "R" | Sim |
| CODCOLIGADA\_1 | Código da coligada | Sim |
| IDPS\_1 | Código do processo seletivo | Sim |
| IDETAPA\_1 | Código da etapa | Sim |
| NUMERO\_CARTAO\_1 | Número do cartão de respostas | Sim |
| NUMERO\_INSCRICAO\_1 | Número da inscrição | Sim |
| C\_1\_R\_1 | Nota da prova aberta número 1 | Sim |
| C\_1\_R\_2 | Nota da prova aberta número 2 | Não |

**Ex.:**  
   
INDICADOR;CODCOLIGADA\_1;IDPS\_1;IDETAPA\_1;NUMERO\_CARTAO\_1;NUMERO\_INSCRICAO\_1;C\_1\_R\_1;C\_1\_R\_2; R;1;29;39;1;1;1;5;  
   
Quando o sistema detectar que o arquivo a ser lido é gabarito de questões abertas ou redação, será apresentado o passo adicional do assistente chamado "Preenchimento padrão para resposta de redação".

Nessa tela o usuário poderá entrar com um texto. Esse texto será armazenado no TOTVS Avaliação e Pesquisa para que seja mantido um histórico sobre qual era a resposta esperada.   
   
Após executar o processo, o *Log* do processo irá exibir informações sobre cada um dos gabaritos que foi importado. Em caso de falha de importação, o *Log* apresentará também mensagens indicando os possíveis motivos para cada um dos gabaritos não importado:

1. Não foi encontrado cadernos de provas distribuídos vinculados à inscrição.
2. Gabarito já importado em processamentos anteriores.
3. Dados da linha já processados na execução atual, indicando duplicidade de informações para uma mesma inscrição no arquivo.
4. Número de inscrição que foi obtido da linha no arquivo não existe no processo seletivo que está sendo processado.
5. A inscrição existe, mas está cancelada. Por isso, os dados não são importados.

**Pré - requisitos do processo**:  
A instituição deverá ter enviado os gabaritos para a gráfica e recebido os arquivos com os dados digitalizados após a leitura.  
Candidato deve possuir registro de presença
