---
content_hash: d51f5d839203087b632a4802731a293855bf13df48962e3f7d431b8f286f13ba
fetched_at: '2026-06-29T00:09:33.438666+00:00'
page_id: '425459027'
product: rm
source: tdn-rm
title: Importar notas inconsistentes do ENEM
type: documentation
url: https://tdn.totvs.com/display/LRM/Importar+notas+inconsistentes+do+ENEM
version: 9
---

Este processo tem como objetivo importar as notas objetiva e de redação dos candidatos, que durante a validação dos dados realizado pelo INEP foi identificado que alguns destes estavam diferentes dos gravados na base de dados do INEP. Portanto, para estes candidatos o INEP enviará um arquivo com layout específico, contendo os dados que os candidatos informaram no momento da inscrição e os que estavam na base do INEP. Este arquivo será do tipo "Diferenças".

**Diferenças**: Este arquivo contém as diferenças entre os dados informados no arquivo enviado pela instituição e aqueles constantes nas bases do INEP.  Para cada inscrição de candidato existem duas linhas. A primeira contém os dados da forma que foram solicitados e o primeiro campo indica as coincidências encontradas e tem o formato abaixo:   
 Coincidências; Ano; Número da inscrição; Nome do inscrito; Nome da mãe; Documento; Órgão expedidor; UF documento; Data nascimento

Descrição das coincidências:

|  |  |
| --- | --- |
| Código | Descrição |
| 1 | Número de inscrição |
| 2 | Nome do inscrito |
| 3 | Nome da mãe |
| 4 | Número do documento |
| 5 | Data de nascimento |

A linha seguinte contém os dados da forma em que se encontra cadastrada no banco de dados do INEP. Segue o formato abaixo:  
Ano; Número da inscrição; Nome do inscrito; Nome da mãe; Documento; Órgão expedidor; UF documento; Data nascimento; Nota objetiva; Nota redação; Situação (Presente ou Faltou)

Exemplo:  
1245;  
2002; 200201368245; ADRIANE RENAU BASTOS; FATIMA K BASTOS; 0985382686; SSP; BA; 08/03/1984  
2002; 200201368245; ADRIANE RENAU BASTOS; FATIMA KENAU BASTOS; 0985382686; SSP; BA; 08/03/1984; 99; 0; Presente  
No caso do exemplo acima indica que o nome da mãe não coincidiu, pois não existe a coincidência número 3.  
\*Utilizando o processo{\*}: Na tela "verificar os candidatos com problemas de inconsistências" dividem-se as informações em duas partes. A superior mostra os dados existentes na base de dados do INEP e na parte inferior os existentes na base do processo seletivo. Desta forma é possível comparar todas as colunas e verificar as diferenças entre elas.  
Para importar as notas destes candidatos será necessário clicar na coluna com o símbolo "\[x\]", na parte superior da tela, e, em seguida, clicar no botão "Avançar". O processo irá gravar estas notas nas inscrições destes candidatos.  
\*Pré - requisitos do processo{\*}:  
**a)** Existir áreas de interesse ofertadas configuradas para utilizar o ENEM.  
**b)** Existir inscrições onde os candidatos tenham informado o número de inscrição no ENEM e ano de referência.  
**c)** Ter recebido do INEP o arquivo do tipo "Diferenças".
