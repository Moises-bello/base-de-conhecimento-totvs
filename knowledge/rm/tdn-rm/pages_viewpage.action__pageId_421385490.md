---
content_hash: 52cab4d9f892cd3f255b8b32ff6ff564840816a4fe71abf4c9a4a313f0e6ea77
fetched_at: '2026-06-29T00:09:16.228757+00:00'
page_id: '421385490'
product: rm
source: tdn-rm
title: Funções de Fórmulas usadas no TOTVS Construção Obras e Projetos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385490
version: 11
---

---

O TOTVS Construção Obras e Projetos possui inúmeras funções de fórmulas que podem ser utilizadas na confecção de fórmulas para as mais variadas funcionalidades do sistema, desde uma simples consistência de Projeto ou Planilha quanto em regras de Insumos derivados. Abaixo listamos todas as funções de fórmulas disponíveis para uso, agrupadas por provedor de dados, os chamados Providers:

* **Projeto**
  + Função: **VLRCOLIGADACORRENTE**

    - Contexto: CODCOLIGADA, IDPRJ (Chave primária da tabela MPRJ)
    - Descrição: Retorna identificador da coligada corrente
    - Parâmetros: N/A
  + Função: **COLIGADA**

    - Contexto: CODCOLIGADA, IDPRJ (Chave primária da tabela MPRJ)
    - Descrição: Retorna identificador da coligada corrente
    - Parâmetros: N/A
  + Função: **VLRPARPROJETOC**

    - Contexto: CODCOLIGADA, IDPRJ (Chave primária da tabela MPRJ)
    - Descrição: Valor Parâmetro
    - Parâmetros:

      * NomeParametro - Nome do parâmetro na tabela MPARAMETRO
  + Função: **TABPRJ**

    - Contexto: CODCOLIGADA, IDPRJ (Chave primária da tabela MPRJ)
    - Descrição: Retorna Campos da Tabela de Projeto
    - Parâmetros:

      * CodCampo - Campo da tabela MPRJ
  + Função: **VALORBDIPROJETO**

    - Contexto: CODCOLIGADA, IDPRJ (Chave primária da tabela MPRJ)
    - Descrição: Valor do BDI do Projeto
    - Parâmetros: N/A
  + Função: **CONSISTIRCOTACAOPRJ**

    - Contexto: CODCOLIGADA, IDPRJ (Chave primária da tabela MPRJ)
    - Descrição: Consistir Cotação do Projeto
    - Parâmetros: N/A
  + Função: **TABCOLIG**

    - Contexto: CODCOLIGADA, IDPRJ (Chave primária da tabela MPRJ)
    - Descrição: Retorna um campo da tabela de Coligadas
    - Parâmetros:

      * CodCampo - Campo da tabela GCOLIGADA
  + Função: **NUMDIASEM**

    - Contexto: CODCOLIGADA, IDPRJ (Chave primária da tabela MPRJ)
    - Descrição: Retorna o número de semanas em um intervalo de data
    - Parâmetros:

      * diasem - Dia da semana:

        + DOM - Domingo
        + SEG - Segunda
        + TER - Terça
        + QUA - Quarta
        + QUI - Quinta
        + SEX - Sexta
        + SAB - Sábado
      * dtInicio - Data inicial
      * dtFim - Data final
  + Função: **VALORTOTALPROJETOCOMBDI**

    - Contexto: CODCOLIGADA, IDPRJ (Chave primária da tabela MPRJ)
    - Descrição: Valor Total do Projeto com BDI
    - Parâmetros: N/A
  + Função: **VLRBDIPROJETOC**

    - Contexto: CODCOLIGADA, IDPRJ (Chave primária da tabela MPRJ)
    - Descrição: Valor do BDI do Projeto somente para relatórios com N projetos
    - Parâmetros: N/A
  + Função: **VLRCUSTOPROJETO**

    - Contexto: CODCOLIGADA, IDPRJ (Chave primária da tabela MPRJ)
    - Descrição: Valor Total do Projeto sem BDIs somente para relatórios com N projetos
    - Parâmetros: N/A
  + Função: **VLRPARAMPROJETO**

    - Contexto: CODCOLIGADA, IDPRJ (Chave primária da tabela MPRJ)
    - Descrição: Valor Parâmetro
    - Parâmetros:

      * NomeParametro - Nome do parâmetro na tabela MPARAMETRO
  + Função: **VLRTOTALPROJETOCOMBDIC**

    - Contexto: CODCOLIGADA, IDPRJ (Chave primária da tabela MPRJ)
    - Descrição: Valor Total do Projeto com BDI somente para relatórios com N projetos
    - Parâmetros: N/A
  + Função: **EXISTERECURSOQTDEZEROCMP**

    - Contexto: CODCOLIGADA, IDPRJ (Chave primária da tabela MPRJ)
    - Descrição: Retorna os recursos ativos e com quantidade igual a zero nas composições do projeto
    - Parâmetros: N/A
  + Função: **CAMPOCONSULTA**

    - Contexto: CODCOLIGADA, IDPRJ
    - Descrição: Executa uma consulta SQL apenas uma vez e mantém o resultado em cache, retornando o valor de um campo de um registro específico.
    - Parâmetros: Consulta, Resultado
  + Função: **CAMPOCONSULTA1**

    - Contexto: CODCOLIGADA, IDPRJ
    - Descrição: Executa uma consulta SQL apenas uma vez e mantém o resultado em cache, retornando o valor de um campo de um registro específico.
    - Parâmetros: Consulta, Resultado, Chave, ValorChave
  + Função: **CAMPOCONSULTA2**

    - Contexto: CODCOLIGADA, IDPRJ
    - Descrição: Executa uma consulta SQL apenas uma vez e mantém o resultado em cache, retornando o valor de um campo de um registro específico.
    - Parâmetros: Consulta, Resultado, Chave, ValorChave1, ValorChave2
  + Função: **CAMPOCONSULTA3**

    - Contexto: CODCOLIGADA, IDPRJ
    - Descrição: Executa uma consulta SQL apenas uma vez e mantém o resultado em cache, retornando o valor de um campo de um registro específico.
    - Parâmetros: Consulta, Resultado, Chave, ValorChave1, ValorChave2, ValorChave3
* **Insumos:**
  + Função: **TABMISM**

    - Contexto: CODCOLIGADA, IDPRJ, IDISM (Chave primária da tabela MISM)
    - Descrição: Retorna Campos da Tabela de Insumo
    - Parâmetros:

      * CodCampo - Campo da tabela MISM
  + Função: **TABMISMPORCODIGO**
    - Contexto: CODCOLIGADA, IDPRJ, IDISM (Chave primária da tabela MISM)
    - Descrição: Retorna campos de um insumo através do código do mesmo.
    - Parâmetros:

      * CodCampo - Campo da tabela MISM
  + Função: **EQUALIZDERIVADO**

    - Contexto: CODCOLIGADA, IDPRJ, IDISM (Chave primária da tabela MISM)
    - Descrição: Soma Equalização para Insumos Derivados (Período, Campo)
    - Parâmetros:

      * Periodo - Período
      * CodCampo - Campo da tabela MEQUALIZACAOINSUMO
  + Função: **EQUALIZDERIVADOMAX**

    - Contexto: CODCOLIGADA, IDPRJ, IDISM (Chave primária da tabela MISM)
    - Descrição: Máximo de equalização para Insumos Derivados (Campo)
    - Parâmetros:

      * CodCampo - Campo da tabela MEQUALIZACAOINSUMO
  + Função: **EQUALIZDERIVADOMIN**

    - Contexto: CODCOLIGADA, IDPRJ, IDISM (Chave primária da tabela MISM)
    - Descrição: Mínimo de equalização para Insumos Derivados (Campo)
    - Parâmetros:

      * CodCampo - Campo da tabela MEQUALIZACAOINSUMO
  + Função: **EQUALIZDERIVADOAVG**

    - Contexto: CODCOLIGADA, IDPRJ, IDISM (Chave primária da tabela MISM)
    - Descrição: Média de equalização para Insumos Derivados (Campo)
    - Parâmetros:

      * CodCampo - Campo da tabela MEQUALIZACAOINSUMO
  + Função: **DERIVADOCRONOG**
    - Contexto: CODCOLIGADA, IDPRJ, IDISM (Chave primária da tabela MISM), IDPERIODO;
    - Parâmetros:
      * Identificador do Insumo, Identificador do Período e Campo.
  + Função: **DERIVADOCRONOGDISCIPLINA**
    - Contexto: CODCOLIGADA, IDPRJ, IDISM (Chave primária da tabela MISM), IDPERIODO;
    - Parâmetros:
      * Identificador do Insumo, Identificador do Período e Identificador da Disciplina.
  + Função: **DERIVADOCRONOGCEILING**
    - Contexto: CODCOLIGADA, IDPRJ, IDISM (Chave primária da tabela MISM), IDPERIODO;
    - Parâmetros:
      * Identificador do Insumo, Identificador do Período e Identificador da Disciplina.
  + Função: **DERIVADOCRONOGDISCIPLINACEILING**
    - Contexto: CODCOLIGADA, IDPRJ, IDISM (Chave primária da tabela MISM), IDPERIODO;
    - Parâmetros:
      * Identificador do Insumo, Identificador do Período e Identificador da Disciplina.
* **Composições:**
  + Função: **SOMAGRUPOCUSTOCMP**

    - Contexto: Coligada, Projeto, Identificador da Composição
    - Descrição: Soma valores/quantidade de Insumos do Grupo de Custo (Grupo, Recursivo, Campo)
    - Parâmetros:

      * Grupo: Grupo de Custo desejado
      * Recursivo: Define se deve considerar as composições auxiliares
      * Campo: Nome do campo que será utilizado na soma
  + Função: **SOMAGRUPODNITCMP**

    - Contexto: Coligada, Projeto, Identificador da Composição
    - Descrição: Soma valores/quantidade de Insumos do Grupo de Custo (Grupo, Recursivo, Campo)
    - Parâmetros:

      * Grupo: Grupo de Custo desejado
      * Recursivo: Define se deve considerar as composições auxiliares
      * Campo: Nome do campo que será utilizado na soma
  + Função: **TABRECCMP**

    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo
    - Descrição: Retorna Campos da Tabela de Recursos da Composição
    - Parâmetros:

      * CodCampo: Nome do campo
  + Função: **TABCMP**

    - Contexto: Coligada, Projeto, Identificador da Composição
    - Descrição: Retorna Campos da Tabela de Composição
    - Parâmetros:

      * CodCampo: Nome do campo
  + Função: **TABMCMP**

    - Contexto: Coligada, Projeto, Identificador da Composição
    - Descrição: Retorna Campos da Tabela de Composição
    - Parâmetros:

      * CodCampo: Nome do campo
  + Função: **COMPIMSDERIVADO**

    - Contexto: Coligada, Projeto, Identificador da Composição
    - Descrição: Soma Valores para Insumos Derivados de Valor ou Quantidade na Composição (Campo)
    - Parâmetros:

      * CodCampo: Nome do campo
  + Função: **SOMARECCMPDERIVACAO**

    - Contexto: Coligada, Projeto, Identificador da Composição
    - Descrição: Soma campo de todos os insumos/grupo de custo da regra de derivação
    - Parâmetros:

      * CodCampo: Nome do campo
  + Função: **TABVLRVARCMP**

    - Contexto: Coligada, Projeto, Identificador da Composição
    - Descrição: Recupera o valor da variável na composição
    - Parâmetros:

      * CodCampo: Código da variável
  + Função: **TABCMPCOMPL**

    - Contexto: Coligada, Projeto, Identificador da Composição
    - Descrição: Retorna valor de um campo complementar da tabela de composição
    - Parâmetros:

      * CodCampo: Nome do campo
  + Função: **VALORCOMPOSICAO**

    - Contexto: Coligada, Projeto, Identificador da Composição
    - Descrição: Valor unitário da composição
    - Parâmetros: N/A
  + Função: **VALORLEISSOCIAL**

    - Contexto: Coligada, Projeto, Identificador da Composição
    - Descrição: Valor unitário com Lei Social de uma Composição
    - Parâmetros: N/A
  + Função: **VALORLEISOCIALCMP**

    - Contexto: Coligada, Projeto, Identificador da Composição
    - Descrição: Valor da lei social da composição pelo grupo DNER
    - Parâmetros:

      * GrupoCusto: Grupo DNIT desejado
  + Função: **USACACHEPROVIDERCMP**

    - Contexto: N/A
    - Descrição: Seta a Utilização de Cache para o Provider de Composições
    - Parâmetros: N/A
  + Função: **LIMPACACHEPROVIDERCMP**

    - Contexto: N/A
    - Descrição: Limpa o Cache do Provider de Composições
    - Parâmetros: N/A

* **Recursos de Composições:**
  + Função: **GRUPOCUSTODESCGLOBAL**
    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo, Identificador do Grupo de Custo
    - Descrição: Retorna a descrição do grupo de custo incluindo globais
    - Parâmetros: N/A
  + Função: **CODIGORECURSO**
    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo, Código do Insumo, Código da Composição Auxiliar
    - Descrição: Retorna código do recurso
    - Parâmetros: N/A
  + Função: **DESCRICAORECURSO**
    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo, Descrição do Insumo, Descrição da Composição Auxiliar
    - Descrição: Retorna a descrição do recurso
    - Parâmetros: N/A
  + Função: **DESCRICAORECURSOGLOBAL**
    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo, Descrição do Insumo, Descrição da Composição Auxiliar
    - Descrição: Retorna a descrição do recurso incluindo globais
    - Parâmetros: N/A
  + Função: **UNIDADERECURSO**
    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo, Unidade do Insumo, Unidade da Composição Auxiliar
    - Descrição: Retorna a unidade do recurso
    - Parâmetros: N/A
  + Função: **UNIDADERECURSOGLOBAL**
    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo, Unidade do Insumo, Unidade da Composição Auxiliar
    - Descrição: Retorna a unidade do recurso incluindo global
    - Parâmetros: N/A
  + Função: **PARCIALRECURSO**
    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo
    - Descrição: Retorna o preço parcial do recurso da composição
    - Parâmetros: N/A
  + Função: **VALORINSUMOEMCMP**
    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo
    - Descrição: Valor do insumo em uma composição
    - Parâmetros: N/A
  + Função: **VALORRECURSO**
    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo
    - Descrição: Preço unitário do recurso da composição
    - Parâmetros: N/A
  + Função: **VALORRECURSOIMPR**
    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo
    - Descrição: Preço unitário improdutivo do recurso da composição
    - Parâmetros: N/A
  + Função: **VALORRECURSOSEMLEIS**
    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo
    - Descrição: Valor do recurso da composição sem leis por grupo de custo
    - Parâmetros:
      * GrupoCusto: Grupo de Custo desejado
  + Função: **VALORLEISSOCIAISRECURSO**
    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo
    - Descrição: Preço leis sociais do recurso da composição por grupo de custo
    - Parâmetros:
      * GrupoCusto: Grupo de Custo desejado
  + Função: **VALORTOTALINSUMOEMCMP**
    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo
    - Descrição: Valor total do insumo em uma composição
    - Parâmetros: N/A
  + Função: **VALORKR**
    - Contexto: Coligada, Projeto, Identificador da Composição, Identificador da Composição Auxiliar, Identificador do Insumo
    - Descrição: Valor do K,R de mão de obra do recurso de composição
    - Parâmetros: N/A
  + Função: **USACACHEPROVIDERRECCMP**
    - Contexto: N/A
    - Descrição: Seta a Utilização de Cache para o Provider de Recursos de Composições
    - Parâmetros: N/A
  + Função: **LIMPACACHEPROVIDERRECCMP**
    - Contexto: N/A
    - Descrição: Limpa o Cache do Provider Recursos de Composições
    - Parâmetros: N/A
* **Tarefas:**
  + Função: **TABTRF**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Retorna Campos da Tabela de Tarefa
    - Parâmetros:
      * CodCampo - Campo da tabela MTRF
  + Função: **TABTRFCOMPL**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Retorna valor de um campo complementar da tabela de tarefas
    - Parâmetros:
      * CodCampo - Campo da tabela MTRFCOMPL
  + Função: **TAREFADERIVADOCMP**
    - Descrição: Retorna valor e quantidade das tarefas através da derivação das composições de um insumo.
  + Função: **SOMAGRUPOCUSTOTRF**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Soma valores/quantidade de Insumos do Grupo de Custo (Grupo, Campo)
    - Parâmetros:
      * GrupoCusto - Codigo do Grupo de Custo
      * Campo - Campo da tabela MABCISMTRF
  + Função: **SOMAGRUPODNITTRF**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Soma valores/quantidade de Insumos do Grupo DNIT (Grupo, Campo)
    - Parâmetros:
      * grupoDNIT - Grupo DNIT
      * Campo - Campo da tabela MABCISM
  + Função: **QTDEALOCADAATVSRV**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Quantidade alocada da Atividade e Serviço
    - Parâmetros: N/A
  + Função: **IFCPROPRIEDADE**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Propriedade do objeto associado a tarefa no arquivo IFC. Exemplo: IFCPROPRIEDADE('Grupo', 'Propriedade')
    - Parâmetros:
      * grupo - Nome do grupo de propriedades (PropertySet)
      * propriedade - Nome da propriedade do objeto 3D
  + Função: **EQUALIZDERIVADOETAPA**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Soma Equalização para Insumos Derivados na Etapa (Período, Campo)
    - Parâmetros:
      * Periodo - Número do período
      * CodCampo - Campo da tabela MEQUALIZACAOINSUMO
  + Função: **TABTRFAPROP**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Valor apropriado por tarefa em cada período
    - Parâmetros:
      * Periodo - Número do período
  + Função: **LANCNTPDOCRONOG**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Retorna o valor do período do cronograma
    - Parâmetros:
      * Periodo - Número do período
  + Função: **LRPDOCNTPLAN**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Valor planejado para o período do contrato
    - Parâmetros:
      * TipoBusca
        + 0 - Número do período (Período específico)
        + 1 - Dias corridos (Todos os período até o período corrente)
      * Observação: Deve existir o campo NUMPERIODO no contexto.
  + Função: **VLRPDOCNTMED**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Valor medido para o período do contrato
    - Parâmetros:
      * TipoBusca
        + 0 - Número do período (Período específico)
        + 1 - Dias corridos (Todos os período até o período corrente)
      * Observação: Deve existir o campo NUMPERIODO no contexto.
  + Função: **VLRPDOCNTREAL**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Valor realizado para o período do contrato
    - Parâmetros:
      * TipoBusca
        + 0 - Número do período (Período específico)
        + 1 - Dias corridos (Todos os período até o período corrente)
      * Observação: Deve existir o campo NUMPERIODO no contexto.
  + Função: **VALORTAREFA**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Valor unitário da tarefa
    - Parâmetros: N/A
  + Função: **TABCALENDARIORECURSO**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Retorna Campos da Tabela de Calendário de Recursos
    - Parâmetros:
      * CodCampo - Campo da tabela MEQUIPEPDO
      * Periodo - Identificador do período do cronograma
      * CodIsm - Código do insumo

* + Função: **VLRHORASPRODUTIVASRECURSO**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Valor das Horas Produtivas de um Recurso da Tarefa
    - Parâmetros:
      * Periodo - Identificador do período do cronograma
      * CodIsm - Código do insumo

| ``` Cálculo do total de horas do período da tarefa  Total de horas = (MEQUIPEPDO.NUMDIAS - MEQUIPEPDO.NUMDIASPARADO) * MEQUIPEPDO.NUMHORASTURNO * MEQUIPEPDO.NUMTURNOS * MTAREFA.QTDEEQUIPE                   Número de dias       Número de dias parados      Número de horas do turno   Número de turnos       Quantidade da Equipe   Se Grupo Dner do insumo for "Mão de Obra":  Total de Dias = Total de horas / (MISM.JORNADAPERIODO             + (MISM.JORNADAPERIODO            * MISM.MAXIMOHORAEXTRA            / 100))                                   Jornada do Período de Controle     Jornada do Período de Controle   Percentual Máximo de Hora Extra  Se Grupo Dner do insumo for "Mão de Equipamento":  Total de Dias = Total de horas * (MRECCMP.COEFICIENTEPRODUTIVO / 10000) / (MISM.JORNADAPERIODO            + (MISM.JORNADAPERIODO            * MISM.MAXIMOHORAEXTRA            / 100))                                    Coeficiente produtivo                    Jornada do Período de Controle    Jornada do Período de Controle   Percentual Máximo de Hora Extra           ``` |
| --- |

```

```

* + Função: **VALORTOTALOBRA**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Retorna o valor da obra
    - Parâmetros: N/A
  + Função: **VALORTOTALETAPA**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Retorna o valor total de uma etapa
    - Parâmetros: N/A
  + Função: **CODTAREFASEMOBRA**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Código da Tarefa sem Código da Obra
    - Parâmetros: N/A
  + Função: **QTDEDEOBRA**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Número de Unidades (Quantidade) da Obra
    - Parâmetros: N/A
  + Função: **QTDEDOSERVICO**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Quantidade do serviço considerando quantidade de obra
    - Parâmetros: N/A
  + Função: **VALORINSUMONOPROJETO**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Valor total do insumo no projeto (cálculo da ABC de insumos)
    - Parâmetros: N/A
    - Observação: A tarefa do contexto deve ter o campo IDISM preenchido.
  + Função: **VALORINSUMOTRF**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Retorna o valor unitário do insumo
    - Parâmetros: N/A
    - Observação: A tarefa do contexto deve ter o campo IDISM preenchido
  + Função: **QUANTIDADEHORASISMDERIVADOTRF**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Quantidade de horas do insumo derivado na tarefa por período
    - Parâmetros:
      * numPeriodo - Identificador do período do cronograma
  + Função: **TABMTRFPDO**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF (Chave primária da tabela MTRF)
    - Descrição: Retorna Campos da Tabela de Calendário da Tarefa
    - Parâmetros:
      * codCampo - Campo da tabela MTRFPDO
      * numPeriodo - Identificador do período do cronograma
      * tipoCalendario - Tipo de calendário
* **Contratos:**
  + Função: **A**

    - Contexto: Coligada, Projeto, Identificador do Contrato
    - Descrição: Retorna o Valor com Reajuste - Valor Total Medido
    - Parâmetros:

      * PeriodoMed: Período
      * Classificacao: Classificação do período
  + Função: **B**

    - Contexto: Coligada, Projeto, Identificador do Contrato
    - Descrição: Retorna o Valor sem Reajuste
    - Parâmetros:

      * PeriodoMed: Período
      * Classificacao: Classificação do período
  + Função: **C**

    - Contexto: Coligada, Projeto, Identificador do Contrato
    - Descrição: Retorna o Valor com Reajuste
    - Parâmetros:

      * PeriodoMed: Período
      * Classificacao: Classificação do período
  + Função: **D**

    - Contexto: Coligada, Projeto, Identificador do Contrato
    - Descrição: Retorna o Valor do Reajuste
    - Parâmetros:

      * PeriodoMed: Período
      * Classificacao: Classificação do período
  + Função: **E**

    - Contexto: Coligada, Projeto, Identificador do Contrato

      * Descrição: Retorna o Valor das Retenções
      * Parâmetros:

        + PeriodoMed: Período
        + Classificacao: Classificação do período
  + Função: **F**

    - Contexto: Coligada, Projeto, Identificador do Contrato

      * Descrição: Retorna o Valor das Deduções
      * Parâmetros:

        + PeriodoMed: Período
        + Classificacao: Classificação do período
  + Função: **G**

    - Contexto: Coligada, Projeto, Identificador do Contrato
    - Descrição: Retorna o Valor Total Retido
    - Parâmetros:

      * PeriodoMed: Período
      * Classificacao: Classificação do período
  + Função: **CLIFORDOCONTRATO**

    - Contexto: Coligada, Projeto, Identificador do Contrato
    - Descrição: Retorna o Cliente/Fornecedor do Contrato
    - Parâmetros: N/A
  + Função: **VALORREALCONTRATO**
    - Contexto: Coligada, Projeto, Identificador do Contrato
    - Descrição: Retorna o Valor real do contrato
    - Parâmetros: N/A
  + Função: **VALORREALCONTRATO**

    - Contexto: Coligada, Projeto, Identificador do Contrato
    - Descrição: Retorna o Valor real do contrato
    - Parâmetros: N/A
* **Itens de Contratos:**
  + Função: **MOEDACONTRATOPROJETO**

    - Contexto: Coligada, Projeto, Identificador do Contrato
    - Descrição: Retorna a moeda do contrato ou do projeto
    - Parâmetros: N/A
  + Função: **QTDECONTQTDEPLANILHA**

    - Contexto: Coligada, Projeto, Identificador do Contrato, Identificador do Item do Contrato, Identificador da Tarefa
    - Descrição: Quantidade contratada ou quantidade na planilha
    - Parâmetros: N/A
  + Função: **VALORUNITITEM**

    - Contexto: Coligada, Projeto, Identificador do Contrato, Identificador do Item do Contrato
    - Descrição: Retorna o valor unitário do item de contrato
    - Parâmetros: N/A
* **Períodos de Contratos:**
  + Função: **SOMATORIOTTMEDPDOPRINCIPAL**

    - Contexto: Coligada, Projeto, Identificador do Contrato, Período Medido
    - Descrição: Somatório do total da medição do período principal do contrato
    - Parâmetros: N/A
  + Função: **SOMATORIOTTMEDPDOCOMPLEMENTAR**

    - Contexto: Coligada, Projeto, Identificador do Contrato, Período Medido
    - Descrição: Retorna o somatório do total da medição do período complementar do contrato
    - Parâmetros: N/A
* **Medição de Contratos:**
  + Função: **INTERVALODATASPERIODO**

    - Contexto: Coligada, Projeto, Identificador do Contrato, Identificador do Item do Contrato, Período Medido
    - Descrição: Retorna o intervalo de datas de um período do contrato
    - Parâmetros: N/A
  + Função: **QTDEMEDACUMSERVICO**

    - Contexto: Coligada, Projeto, Identificador do Contrato, Identificador do Item do Contrato, Período Medido
    - Descrição: Retorna a quantidade medida acumulada de um serviço
    - Parâmetros: N/A
  + Função: **VALORMEDACUMSERVICO**

    - Contexto: Coligada, Projeto, Identificador do Contrato, Identificador do Item do Contrato, Período Medido
    - Descrição: Retorna o valor medido acumulado de um serviço
    - Parâmetros: N/A
  + Função: **VALORMEDACUMCONTRATO**

    - Contexto: Coligada, Projeto, Identificador do Contrato, Identificador do Item do Contrato, Período Medido
    - Descrição: Retorna o valor medido acumulado do contrato
    - Parâmetros: N/A
  + Função: **VALORMEDACUMETAPA**

    - Contexto: Coligada, Projeto, Identificador do Contrato, Identificador do Item do Contrato, Período Medido
    - Descrição: Retorna o valor medido acumulado de uma etapa
    - Parâmetros: N/A
  + Função: **VALORPREVETAPA**

    - Contexto: Coligada, Projeto, Identificador do Contrato, Identificador do Item do Contrato, Período Medido
    - Descrição: Retorna o valor previsto de uma etapa
    - Parâmetros: N/A
  + Função: **QTDCONSUMOACUMOBJ**

    - Provider: "Medição de Período de Contrato"
    - Contexto: Coligada, Projeto, Identificador do Contrato, Identificador do Item do Contrato, Período Medido
    - Descrição: Retorna a quantidade consumida acumulada
    - Parâmetros: N/A
  + Função: **VALORCONSUMOACUMOBJ**

    - Contexto: Coligada, Projeto, Identificador do Contrato, Identificador do Item do Contrato, Período Medido
    - Descrição: Retorna o valor Consumido acumulado
    - Parâmetros: N/A
  + Função: **QTDEMEDSERVICO**

    - Contexto: Coligada, Projeto, Identificador do Contrato, Identificador do Item do Contrato, Período Medido
    - Descrição: Quantidade medida de um serviço
    - Parâmetros: N/A
  + Função: **VALORMEDSERVICO**

    - Contexto: Coligada, Projeto, Identificador do Contrato, Identificador do Item do Contrato, Período Medido
    - Descrição: Valor medido de um serviço
    - Parâmetros: N/A
* **Cronograma:**
  + Função: **NUMPERIODO**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF, NUMPERIODO (Chave primária da tabela MTRFPLAN)
    - Descrição: Número do Período
    - Parâmetros: N/A
  + Função: **TABTRFPLAN**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF, NUMPERIODO (Chave primária da tabela MTRFPLAN)
    - Descrição: Retorna Campos da Tabela de Cronograma Planejado
    - Parâmetros:
      * CodCampo - Campo da tabela MTRFPLAN
  + Função: **TABTRFMED**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF, NUMPERIODO (Chave primária da tabela MTRFPLAN)
    - Descrição: Retorna Campos da Tabela de Cronograma Medido
    - Parâmetros:
      * CodCampo - Campo da tabela MTRFMED
  + Função: **TABTRFREAL**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF, NUMPERIODO (Chave primária da tabela MTRFPLAN)
    - Descrição: Retorna Campos da Tabela de Cronograma Realizado
    - Parâmetros:
      * CodCampo - Campo da tabela MTRFREAL
  + Função: **TABTRFPLANDERIVADO**
    - Contexto: CODCOLIGADA, IDPRJ, IDTRF, NUMPERIODO (Chave primária da tabela MTRFPLAN)
    - Descrição: Retorna Campos da Tabela de Cronograma Planejado levando em conta o insumo derivado.
    - Parâmetros:
      * CodCampo - Campo da tabela MTRFPLAN
* **Itens de Folha Tarefa (somente para Folhas Tarefa cuja origem seja a Planilha de Atividades):**
  + Função: **CALCULOPADRAOFOLHATRF**
    - Contexto: CODCOLIGADA, IDPRJ, IDFOLHATAREFA, IDTRF (Chave primária da tabela MFOLHATAREFAITEM)
    - Descrição: Retorna o calculo padrão de quantidade da Folha tarefa
    - Parâmetros: N/A
  + Função: **SALDOQUANTIDADETOTALFOLHATRF**
    - Contexto: CODCOLIGADA, IDPRJ, IDFOLHATAREFA, IDTRF (Chave primária da tabela MFOLHATAREFAITEM)
    - Descrição: Retorna o saldo de quantidade a ser realizado na tarefa
    - Parâmetros: N/A
  + Função: **SALDOQUANTIDADEPERIODOTRFFOLHATRF**
    - Contexto: CODCOLIGADA, IDPRJ, IDFOLHATAREFA, IDTRF (Chave primária da tabela MFOLHATAREFAITEM)
    - Descrição: Retorna o saldo de quantidade a ser realizado no período da tarefa
    - Parâmetros: N/A
  + Função: **DIASUTEISTRFPERTFOLHATRF**
    - Contexto: CODCOLIGADA, IDPRJ, IDFOLHATAREFA, IDTRF (Chave primária da tabela MFOLHATAREFAITEM)
    - Descrição: Retorna a quantidade de dias uteis da tarefa em relação as datas programadas do PERT
    - Parâmetros: N/A
  + Função: **DIASUTEISCRONOGFOLHATRF**
    - Contexto: CODCOLIGADA, IDPRJ, IDFOLHATAREFA, IDTRF (Chave primária da tabela MFOLHATAREFAITEM)
    - Descrição: Retorna a quantidade de dias uteis da tarefa no período em relação as datas da Folha tarefa
    - Parâmetros: N/A
  + Função: **DIASUTEISFOLHATRF**
    - Contexto: CODCOLIGADA, IDPRJ, IDFOLHATAREFA, IDTRF (Chave primária da tabela MFOLHATAREFAITEM)
    - Descrição: Retorna a quantidade de dias uteis da Folha tarefa
    - Parâmetros: N/A

 Como Fazer

---
