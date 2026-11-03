---
content_hash: c40a38fe2862bd95912e2e0152c5f2830db5845e1996ea455ab02542e1032521
fetched_at: '2026-06-29T00:08:18.785254+00:00'
page_id: '266969686'
product: rm
source: tdn-rm
title: TUUA21_DT_Media_Com_Maiores_Valores_Por_Competencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TUUA21_DT_Media_Com_Maiores_Valores_Por_Competencia
version: 2
---

# CÁLCULO DE MÉDIA CONSIDERAR MAIORES VALORES POR COMPETÊNCIA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Média* | *Cálculo de Média* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Média** | *Cálculo de Média* | | **Férias**  *13o.Salário*  *Rescisão*  *Salário Maternidade*  *Funções de Fórmula* | **Cálculo de Férias**  *Cálculo da 13o. Salário*  *Cálculo de Rescisão*  *Cálculo de Salário Maternidade*  *CALCMED, MEDCOMISS, CALCMEDJOR* | |
| **Cadastros Iniciais:** | *Sindicato* |
| **Parâmetro(s):** | *Considera soma total da competência para buscar maiores valores* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *TUUA21* |
| **Requisito (ISSUE):** | *Folha* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |
| **Tabelas Utilizadas:** | *PSINDMED* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Estava havendo diferença de comportamento na opção, existente na parametrização do Sindicato, de considerar maiores valores na media, entre o cálculo .Net e o cálculo antigo em Dephi.   
No cálculo em .Net busca os maiores valores acumulados por grupo de média, e em Delphi somava todos os valores da competência para fazer a apuração.

Foi criado um parâmetro para possibilitar os dois comportamentos.

Na aba de Media de cada tipo de cálculo no Sindicato, foi criado o parâmetro "Considera soma total da competência para buscar maiores valores".

Segue um exemplo de utilização do parâmetro:

3 eventos incidem em Média:

0082 - Hora Extra 50%   - Evento tipo Hora  - Incide em Media no Grupo 1  
0083 - Hora Extra 100% - Evento tipo Hora  - Incide em Media no Grupo 1  
0084 - Comissão             - Evento tipo Valor - Incide em Media no Grupo 2

Competência atual 06/2016.  
Cálculo dos últimos 5 meses, considerando os 3 maiores valores.

Ficha Financeira

  01/2016                              
    0082 - Hora Extra 50%   - 200   Total Grupo 1 = 700   Total da competência = 1000  
    0083 - Hora Extra 100% - 500  
    0084 - Comissão            - 300   Total Grupo 2 = 300

  02/2016  
    0082 - Hora Extra 50%   - 400   Total Grupo 1 = 500   Total da competência = 1300  
    0083 - Hora Extra 100% - 100  
    0084 - Comissão             - 800   Total Grupo 2 = 800

  03/2016  
    0082 - Hora Extra 50%   - 100   Total Grupo 1 = 600   Total da competência = 800  
    0083 - Hora Extra 100% - 500  
    0084 - Comissão             - 200   Total Grupo 2 = 200

  04/2016  
    0082 - Hora Extra 50%   - 600   Total Grupo 1 = 800   Total da competência = 1200  
    0083 - Hora Extra 100% - 200  
    0084 - Comissão             - 400   Total Grupo 2 = 400

  05/2016  
    0082 - Hora Extra 50%   - 200   Total Grupo 1 = 300   Total da competência = 900  
    0083 - Hora Extra 100% - 100  
    0084 - Comissão             - 600   Total Grupo 2 = 600

Com o parâmetro marcado, serão consideradas as competências, onde as somas totais dos valores são os maiores.  
Ou seja, meses 01, 02 e 04/2016

Grupo 1  
  01/2016                              
    0082 - Hora Extra 50%   - 200   Total Grupo 1 = 700 + 500 + 800 = 2000 / 3 = 666,67  
    0083 - Hora Extra 100% - 500

  02/2016  
    0082 - Hora Extra 50%   - 400     
    0083 - Hora Extra 100% - 100

  04/2016  
    0082 - Hora Extra 50%   - 600     
    0083 - Hora Extra 100% - 200

Grupo 2  
  01/2016                              
    0084 - Comissão            - 300   Total Grupo 2 = 300 + 800 + 400 = 1500 / 3 = 500,00

  02/2016  
    0084 - Comissão            - 800

  04/2016  
    0084 - Comissão            - 400

Com o parâmetro desmarcado, a apuração dos maiores valores irá verificar os totais por grupo.  
Ou seja, meses 01, 03 e 04/2016 para o Grupo 1, e meses 02, 04 e 05 para o Grupo 2.

Grupo 1  
  01/2016                              
    0082 - Hora Extra 50%   - 200   Total Grupo 1 = 700 + 600 + 800 = 2100 / 3 = 700,00  
    0083 - Hora Extra 100% - 500

  03/2016  
    0082 - Hora Extra 50%   - 100  
    0083 - Hora Extra 100% - 500

  04/2016  
    0082 - Hora Extra 50%   - 600  
    0083 - Hora Extra 100% - 200

Grupo 2  
  02/2016  
    0084 - Comissão            - 800   Total Grupo 2 = 800 + 400 + 600 = 1800 / 3 = 600,00

  04/2016  
    0084 - Comissão            - 400

  05/2016  
    0084 - Comissão            - 600

Obs. Para não haver confusão de nomenclatura com o novo parâmetro criado, o parâmetro (já existente) "Considera maiores valores por Grupo" foi alterado para "Compara maior média por grupo". Esta informação deverá ser ajustada no help.
