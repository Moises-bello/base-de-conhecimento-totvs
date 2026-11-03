---
content_hash: f921d5e95833a3311723dcb9910aec515275d5b54ec8ebd6fe34a5f6e27ccb93
fetched_at: '2026-07-02T19:24:26.670518+00:00'
page_id: '6063701'
product: protheus
source: tdn-tec
title: Directory
type: documentation
url: https://tdn.totvs.com/display/tec/Directory
version: 22
---

Directory

Retorna um array com o conteúdo de um diretório.   
  
Consulte a função  para outras funcionalidades.

Atenção!Esta função só pode ser utilizada no SmartClient HTML (WebApp), utilizando o WegAgent, mais informações [**aqui**](https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent).

## Sintaxe

false, [ cAtributos ], [ uParam1 ], [ lConvertCase ], [ nTypeOrder ] )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cDirEsp | caractere | Indica o diretório para pesquisa.  **São permitidos caracteres do tipo curinga ( \*.\* )**   * Caso especificado um **path sem a unidade de disco**, serão considerados arquivos e diretórios contidos no AppServer, exemplos:  `// Retorna arquivos da raiz do System do AppServer aFiles := aFiles := Directory("/*.*", "D")` `// Retorna arquivos do diretorio de Spool do AppServer aFiles := aFiles := Directory("/spool/*.*", "D")` * Caso esterificado um **path com unidade de disco**, serão considerados arquivos e diretórios contidos na estação de trabalho em que o SmartClient está sendo executado, exemplo:  `// Exemplo para Windows aFiles := Directory(``"c:\tmp\*.*")` `// Exemplo para Linux (obrigatório uso do l:) aFiles := Directory(``"l:/tmp/*.*")` | X |  |
| cAtributos | caractere | Indica quais tipos de arquivos/diretórios devem ser incluídos no array.  **É permitido concatenar atributos.**  No exemplo abaixo retornamos **Diretórios + Arquivos de Sistema + Arquivos entre as posições 10.000 e 20.000**:  `cAtributos``:=``"D" // Inclui diretorios   cAtributos += "S" // Inclui arquivos do sistema` `cAtributos += ":10000"` `// Lista arquivos/diretorios a partir do arquivo de nr 10.000` `aFiles := Directory(``"c:\tmp\10kk\*.*"``, cAtributos)`  Para mais detalhes, consulte a **Tabela A** abaixo: Tabela A  |  |  | | --- | --- | | **Atribuito** | **Significado** | | H | Incluir arquivos ocultos | | S | Incluir arquivos de sistema | | D | Incluir diretórios | | V | Procura pelo volume DOS e exclui outros arquivos **Dada exclusão dos demais tipos de arquivos o parâmetro V deve ser usado com cautela.** | | :N | A partir da build **7.00.131227A-20160630**, visando economia de recursos, a função Directory esta limitada ao **retorno de 10.000 itens**.  Caso necessário visualizar itens que tenham uma "contagem" superior à 10.000 é possível utilizar o Atributo **:**(dois pontos), ele trará itens de uma determinada posição **até o limite de +10.000**, veja o exemplo:  `// Lista arquivos a partir da posição 10.000 (limitado a +10.000) cAtributos := ":10000"`  `aFiles := Directory(``"c:\tmp\10kk\*.*"``, cAtributos)` `... // Lista arquivos a partir da posição 20.000 (limitado a +10.000) cAtributos := ":20000"`  `aFiles := Directory(``"c:\tmp\10kk\*.*"``, cAtributos)` `...` | |  |  |
| uParam1 | numérico | Parâmetro de compatibilidade, não deve ser preenchido. |  |  |
| lConvertCase | lógico | Se verdadeiro (.T.), os nomes de arquivos presentes serão retornados todos em MAIÚSCULO.  Caso falso (.F.), os nomes de arquivos presentes são retornados como estão no disco rígido. |  |  |
| nTypeOrder | numérico | Indica o tipo de **ordenação** do resultado da função.  **\*Apenas em build AppServer superiores a 7.00.131227A.** Para mais detalhes, consulte a **Tabela B** abaixo: Tabela B  |  |  | | --- | --- | | **Parâmetro** | **Tipo de ordenação** | | 1 | Ordenar por nome do arquivo | | 2 | Ordenar por data do arquivo | | 3 | Ordenar por tamanho do arquivo | |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| aRet | vetor | Retorna um array que contém informações sobre cada arquivo / diretório que atenda aos requisitos descritos no parâmetro **cAtributos**, passado na chamada da função.  A **Tabela C** (abaixo), descreve a estrutura do array de retorno:Tabela C  |  |  | | --- | --- | | **Posição** | **Conteúdo** | | 1 | Nome do arquivo | | 2 | Tamanho | | 3 | Data | | 4 | Hora | | 5 | Atributos, exemplo A=Arquivo, D=Diretório | |

## Exemplos

cppEclipseExemplo 1truefalse

## Veja também
