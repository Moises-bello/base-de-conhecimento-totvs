---
content_hash: a4b32336f4244f980d597dce9b7cfc5284cfd5e81798c339c7dea1376e36e141
fetched_at: '2026-07-02T19:24:28.496786+00:00'
page_id: '708084124'
product: protheus
source: tdn-tec
title: SmartJob
type: documentation
url: https://tdn.totvs.com/display/tec/SmartJob
version: 6
---

Executa uma rotina em uma nova *thread* sem interface. Consiste em inserir o *Job* em uma fila e somente libera a execução caso existam recursos de CPU e memória confortáveis para executar essa nova *thread*, diferentemente do .

## Configuração via ini (opcional)

|  |
| --- |
| [SMARTJOB] memload=75 minjobs=2 maxjobs=10 |

Utilizando a seção SMARTJOB, é possível configurar a carga máxima de memória da máquina (memload) confortável para se executar um novo *job* da fila, o número mínimo (minjobs) e máximo (maxjobs) de *threads* físicas para atender a fila de *jobs*.  
No exemplo acima, foram empregados os valores de 75% de memória física, 2 *threads* no mínimo e 10 *threads* no máximo.  
Quando não configurados, os valores *default* são, respectivamente, 60, 2 e 16.

## Sintaxe

|  |
| --- |
| `SmartJob( <``cName` `>, <``cEnv` `>, <``lWait` `>, [ parm1,parm2,...parm25 ] )` |

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cEnv | caractere | Indica o nome do ambiente em que o *Job* será executado. | X |  |
| cName | caractere | Indica o nome do *Job* que será executado. | X |  |
| lWait | lógico | Parâmetro de compatibilidade, obrigatório, porém inócuo. Internamente, ele será sempre igual a falso (.F.), ou seja, não espera. | X |  |
| parm1,parm2,...parm25 | qualquer | Os parâmetros (máximo 25 parâmetros) informados a partir deste ponto serão repassados para a função especificada no parâmetro cName. Caso informados parâmetros do tipo B (Code-Block) ou O (Object), no processo de destino receberá NIL. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| Ret | qualquer | Retorna .T. se o SmartJob entrou na fila de processamento ou retorna .F. se houve algum problema de parâmetros ou de entrada na fila. |

## Exemplos

cpp1Exemplo 1true

## Notas Importantes

|  |
| --- |
| * A fila de *SmartJobs* não emprega prioridades, ou seja, é um autêntico FIFO (*Firt in - First Out*); * Quando inserido na fila, um *SmartJob* permanece nela até ganhar a oportunidade de ser executado; * Internamente, quando a fila cresce muito ou está com baixa vazão, o motor de execução pode criar algumas *threads* a mais do que a configuração máxima, a fim de suprir a demanda; * No momento em que a execução de *SmartJobs* retorna à condições propícias e tendo o motor criado *threads* extras, ele mesmo se encarrega de voltar aos valores originais de configuração; * Estando a fila de *jobs* vazia, para economizar recursos, o motor de execução pode ficar sem *threads* ativas (*stand by)*, só as reativando se houver demanda. |

Abrangência  
TOTVS Application Server 17.3.0 ou superior
