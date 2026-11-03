---
content_hash: 30a92952d396c0b2cdc0419a37db84b2a424ffeec8c42eb34f4d4a8b4e3e8880
fetched_at: '2026-06-29T00:10:07.187114+00:00'
page_id: '452719371'
product: rm
source: tdn-rm
title: Exemplo de cálculo da Gestão por Quadrantes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719371
version: 2
---

**Exemplo de cálculo da Gestão por Quadrantes**

**1) Criação das competências e seus itens de performance: Acompanhamento| Competências| Dicionário de Competências.**  
   
Competência: Desenvolvimento de Pessoas  
Tipo: Comportamental  
Sem itens de performance relacionados.  
   
Competência: Análise e Solução de Problemas  
Tipo: Comportamental  
Itens de Performance:  
                Trabalha com metodologia e desenvolve soluções permanentes – **peso padrão = 3**  
                Resolve vários problemas ao mesmo tempo organizando-se em função de prioridades e cumprimento de prazos – **peso padrão = 4**  
   
Competência: Busca por Realização  
Tipo: Comportamental  
Itens de Performance:  
                Atinge resultados com qualidade – **peso padrão = 3**  
                Identifica necessidade de melhorias e modifica métodos de trabalho – **peso padrão = 5**  
   
**Observação**: Considera somente os Itens de Performance ativos.  
   
**2) Verificar quem serão os avaliados na Avaliação de Desempenho. Neste exemplo, vamos considerar os funcionários que tenham a função "Gerente Administrativo e Financeiro". No exemplo, apenas um funcionário.**  
   
**3) Definição das competências - Vínculo "Função" - Gerente Administrativo e Financeiro: Acompanhamento| Mapa de Conhecimento| Definição por Competências.**  
   
Tipo de Vínculo: Função  
   
Competência: Desenvolvimento de Pessoas  
Graduação: Aplicação   
Tipo: Exigido   
  
Competência: Análise e Solução de Problemas  
Graduação: Especialização   
Tipo: Exigido   
   
Competência: Busca por Realização  
Graduação: Compreensão   
Tipo: Desejado   
   
**Observação**:  
Graduação das competências  
00001    Consciência  
00002    Compreensão  
00003    Aplicação  
00004    Especialização  
00005    Domínio  
   
**4) Criação das metas a serem consideradas na Avaliação de Desempenho: Acompanhamento| Gestão de Metas.**  
   
Criação da Meta Agrupadora e Meta Valor, sendo que na composição da meta Agrupadora = 100% da meta Valor.  
   
**5) Criação da Avaliação de Desempenho: Acompanhamento| Avaliações de Desempenho.**  
   
Itens a avaliar:  
Competências Comportamentais  
Metas  
   
Considerar Competências por: Função  
   
**6) Respondendo a Avaliação de Desempenho: Totvs Portal| Recursos Humanos| Gestão por Competências| Avaliação de Desempenho.**  
   
Competência: Desenvolvimento de Pessoas – Supera   
Competência: Análise e Solução de Problemas – Atende Parcialmente   
Competência: Busca por Realização – Supera   
Meta – Atende Parcialmente   
   
**Observação**:  
Escala de Avaliação  
1 - Não Atende    
2 - Atende Parcialmente   
3 - Atende           
4 - Supera                        (Ponto de Corte)  
5 - Supera com excelência           
   
O ponto de corte pode ser definido de acordo com a necessidade do cliente.  
   
**7) Cálculo da Avaliação de Desempenho**  
   
- Cálculo da nota obtida em cada Competência:  
   
Peso do Item de Performance x Valor da Nota obtida na Avaliação / Soma dos pesos dos itens de performance  
 

|  |
| --- |
| Fórmula: **NC = (pIP1 \* VN1) + (pIP2 \* VN2) + ...(pIPn \* VNn)+** |
| **(pIP1 + pIP2 + ...+pIPn)** |

Onde,  
NC = Nota da Competência  
pIP = Peso do Item de Performance  
VN = Valor da Nota Obtida na Avaliação  
   
   
Desenvolvimento de Pessoas  
(1x 4)/1 = **4**  
   
Análise e Solução de Problemas  
Trabalha com metodologia e desenvolve soluções permanentes – peso padrão = 3  
            Resolve vários problemas ao mesmo tempo organizando-se em função de prioridades e cumprimento de prazos – peso padrão = 4  
(3x 2) + (4 x 2)/ (3+ 4) = 6 + 8 / 7 = **2**  
   
Busca por Realização  
Atinge resultados com qualidade – peso padrão = 3  
            Identifica necessidade de melhorias e modifica métodos de trabalho – peso padrão = 5  
(3x 4) + (5x 4)/ (3+ 5) = 12 + 20/ 8 = **4**  
   
Meta  
(1x 2)/ 1 = **2**  
   
- Cálculo da nota obtida na Avaliação:  
   
Soma das notas das competências / Número de competências  
   
(4 + 2 + 4)/ 3 = 10 / 3 = **3,33**  
   
**Atenção**:  
No cálculo citado foi encontrado o valor 3,33, a NC seria 3,0 ao invés de 4,0, pois 3,33 está entre 3,0 e 4,0.  
   
**8) Fechar avaliação de desempenho: Acompanhamento| Avaliações de Desempenho| Processos| Fechar avaliação de desempenho.**  
   
Avaliação finalizada.  
Funcionário recebe as seguintes competências:  
Desenvolvimento de Pessoas – Graduação: Aplicação  
Análise e Solução de Problemas – Graduação: Consciência  
Busca por Realização – Graduação: Compreensão  
   
Respeitando as seguintes regras:  
   
- **Nota obtida corresponde ao ponto de corte:**

Se o funcionário possuir a competência, a graduação será alterada para a graduação da definição do Mapa de Conhecimento;  
Se o funcionário não possuir a competência, será concedida a competência na graduação da definição do Mapa de Conhecimento.

- **Nota obtida está acima do ponto de corte:**

Se o funcionário possuir a competência numa graduação abaixo da graduação exigida / desejada, a graduação do funcionário será elevada para o nível da graduação da definição do Mapa de Conhecimento;   
Se o funcionário possuir a competência na mesma graduação exigida / desejada, a graduação do funcionário será elevada em um nível;   
Se o funcionário possuir a competência numa graduação acima da graduação exigida / desejada, nada será feito;  
Se o funcionário não possuir a competência, será concedida a competência na graduação da definição do Mapa de Conhecimento.   
   
- **Nota obtida está abaixo do ponto de corte:**

Se o funcionário possuir a competência numa graduação abaixo da graduação exigida / desejada, nada será feito;   
Se o funcionário possuir a competência na mesma graduação ou acima da exigida / desejada, a graduação do funcionário é reduzida um nível da graduação abaixo da graduação atual do funcionário;  
Se o funcionário não possuir a competência, será concedida a competência na graduação mínima.  
   
**Observação:**  
Se o parâmetro "Atualizar competências de acordo com a graduação definida na escala" estiver marcado, as regras acima mudam e são consideradas as graduações definidas diretamente na escala.  
   
**9) Criação da Gestão por Quadrantes: Acompanhamento| Gestão por Quadrantes.**  
   
Marcar o flag "Orientado a potencial e resultado".  
Marcar o flag "Utiliza participantes de Avaliações de Desempenho".  
Na aba "Avaliações" associar a Avaliação de Desempenho criada anteriormente (passo 5).  
Definir os quadrantes (exemplo):  
            01 – Quadrante padrão  
            02 – Alto Potencial| Baixo Resultado  
                        % Exigido: 25%   
                        Intervalo de pontuação potencial: 50,01 a 100%  
                        Intervalo de pontuação resultado: 0 a 50%  
03 – Alto Potencial| Alto Resultado  
                        % Exigido: 25%   
                        Intervalo de pontuação potencial: 50,01 a 100%  
                        Intervalo de pontuação resultado: 50,01 a 100%  
04 – Baixo Potencial| Baixo Resultado  
                        % Exigido: 25%   
                        Intervalo de pontuação potencial: 0 a 50%  
                        Intervalo de pontuação resultado: 0 a 50%  
05 – Baixo Potencial| Alto Resultado  
                        % Exigido: 25%   
                        Intervalo de pontuação potencial: 0 a 50%  
                        Intervalo de pontuação resultado: 50,01 a 100%  
   
**10) Verificação da alocação do funcionário nos quadrantes: Totvs Portal| Recursos Humanos| Gestão por Quadrantes.**  
   
**Percentual potencial = Soma das notas das competências \* 100 / Nota máxima obtida nas competências**  
   
(4 + 2 + 4) \* 100 / 15  
10 \* 100 / 15  = **66,6 %**  
   
**Percentual resultado = Soma das notas das metas \* 100 / Nota máxima obtida nas metas**  
   
2 \* 100 / 5 = **40%**  
   
Levando em consideração os quadrantes criados anteriormente:  
Percentual potencial: 66,6%  
Percentual resultado: 40%  
**O funcionário será alocado no quadrante 02 - Alto Potencial| Baixo Resultado.**  
   
**Observação****:**  
Nota máxima obtida nas competências: Maior nota possível da escala x Número de competências  
Escala de avaliação: 5 - Supera com excelência  
5 x 3 = 15  
   
Nota máxima obtida nas metas: Maior nota possível da escala  
Escala de avaliação: 5 - Supera com excelência  
   
**Atenção****:**  
- Os funcionários que não tiveram a sua Avaliação de Desempenho respondida, serão enquadrados no "Quadrante Padrão".
