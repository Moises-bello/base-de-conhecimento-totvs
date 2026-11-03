---
content_hash: 6388974b79d963204c85e61b93799d69d4f37ffa82534a2752f35307c673ca38
fetched_at: '2026-06-29T00:09:15.444721+00:00'
page_id: '421385381'
product: rm
source: tdn-rm
title: Composições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385381
version: 93
---

Roteiro|Cálculo Produção da Equipe Mecânica] de cálculo da produção da equipe mecânica.
\*Fator K Composição:\* Informe o fator k da composição, que caso não informado assumirá o valor default 1. Ao confirmar a utilização do fator k da composição em "Menu Projeto | Construção e Projetos | Projetos | Fator K", esse campo ficará visível em todas as composições. Esse fator será considerado como fator multiplicador dos coeficientes, portanto, altera o valor da composição e, consequentemente o valor do projeto. Esse fator não incide sobre insumos percentuais.
 
\*Grupo DNIT para utilização como composição auxiliar:\*
Deve marcar qual grupo DNIT será considerado no totalizador quando esta composição for utilizada como auxiliar, os tipos disponibilizados são: "Nenhum", "Equipamento", "Mão de Obra", "Material", "Atividades Auxiliares", "Tempo Fixo", "Momento de Transporte". Por default o tipo de composição habilitado será "Nenhum".
\*Recursos:\*
Cadastre as composições e/ou insumos que fazem parte da composição. ]]>

```
Para isso poderá ser feita a inclusão direta ou utilizar os Processos:
```

* Inserir Recurso;
* Inserir Insumos;
* Inserir Composição Auxiliar;  
  Na inclusão direta (botão incluir) digite ou selecione o código ou a descrição e, se desejar, a quantidade dos recursos. Após a escolha do recurso, ele será incluído. Se o insumo não puder ser fracionado, o coeficiente será arredondado (sempre para um valor acima, ou seja, 3,01 será arredondado para 4). Para copiar dados (cabeçalho e recursos) de uma composição para uma nova composição clique no ícone Copiar Composição e siga os seguintes passos:
* Solicitar a inserção de uma composição;
* Informar o seu código, se o cabeçalho não for copiado será necessário informar o código e a unidade antes de copiar os recursos;
* Clicar no ícone "Copiar composição";
* Selecionar o código ou descrição da composição que se deseja copiar;
* Escolher o que será copiado (cabeçalho e/ou recursos);
* Clicar no ícone "Copiar composição selecionada" para efetivar a cópia ou no ícone "Fechar" para desistir.
* **Quantidade:** Quantidade do insumo na composição.   
  A quantidade do recurso pode ser calculada também pelo campo fórmula, essa fórmula é baseada em variáveis cadastradas em Tabelas auxiliares - Variáveis.   
  A variável que será utilizada na fórmula da composição deverá ser incluída na aba variáveis da tela de edição da composição, além das variáveis fixas do sistema, que são:
* FATORKCMP: Fator K da composição;
* PRODUCAOCMP: Produção da composição;
* COEFPROD: Coeficiente produtivo do recurso;
* COEFIMPROD: Coeficiente improdutivo do recurso;
* EQUIPE: Equipe do recurso;
* DMT: DMT do recurso;
* FATORKISM: Fator K do insumo

As funções ARRED, PAR e IMPAR foram implementadas e poderão ser utilizadas no campo fórmula do recurso associado à composição.  
  
**ARRED:** Sempre o retorno total da fórmula ou parte da fórmula contempla o arredondamento, o resultado da função conterá a quantidade de casas decimais definida na fórmula.  
  
SINTAXE:ARRED(EXPRESSÃO, NÚMERO DE CASAS PARA ARREDONDADMENTO)

1º Exemplo:  Função ARRED: A=10 B=3 ARRED(A/B,2)  
O resultado da divisão dos valores das variáveis A e B são arredondados para duas casas decimais.  
Resultado da fórmula A/B=3,333333333  
Com o uso do ARRED: ARRED(A/B,2)=3,33  
  
2º Exemplo: Função ARRED:A=270 e B=7  ARRED(A/B,0)  
O resultado da divisão dos valores é arredondado para o inteiro mais próximo: A/B=38,57142857  
Com o uso do ARRED: ARRED(A/B,0)=39  
  
**PAR:** O resultado da fórmula é um número par. O primeiro par maior que o resultado calculado.  
Exemplo: Se o resultado da fórmula for 2,1, após calcular a composição a quantidade será 4.  
SINTAXE:PAR(VARIAVEL A SER ARREDONDADA PARA O PROXIMO PAR MAIOR DO QUE A VARIÁVEL)  
  
1º Exemplo Função PAR: A=4,1 PAR(A)  
O valor da variável será arredondado para o próximo valor par: PAR(A)=6  
  
2º Exemplo Função PAR: A=10 B=3 PAR(A/B)  
O valor da variável será arredondado para o próximo valor par = PAR(A/B)= 4

**IMPAR:** O resultado da fórmula é um número ímpar. O primeiro impar maior que o resultado calculado. Exemplo: Se o resultado da fórmula for 2,1, após calcular a composição a quantidade será 3.  
  
SINTAXE:IMPAR(VARIAVEL A SER ARREDONDADA PARA O PROXIMO ÍMPAR MAIOR DO QUE A VARIÁVEL)

1º Exemplo Função Impar: A=5,2  
IMPAR(A)  
O valor da variável será arredondado para o próximo valor impar.  
IMPAR(A)=7  
  
2º Exemplo Função Impar: A=10 B=3 IMPAR(A/B)  
O valor da variável será arredondado para o próximo valor Impar: IMPAR(A/B)= 5  
**Atenção:** As funções só são calculadas após terem sido salvas as alterações e calculada a composição.  
Na fórmula a definição da quantidade de casas decimais, deverá ser separada por vírgula.  
**Equipe:** Número de homens / hora. A equipe não altera o custo de uma composição, somente será utilizada no cálculo da duração das tarefas, quando da Integração com o MS Project.  
**Valor Parcial:** Retorna o valor do insumo na composição, somente se o cálculo estiver ativo.  
**Valor sem Leis:** Exibe o valor da composição sem leis sociais e sem o BDI do Projeto.  
**Leis Sociais:** Exibe o valor das leis Sociais na composição.  
**Valor com Leis sem BDI:** Exibe o valor da soma do "Valor sem Leis" com as "Leis Sociais".  
**BDI:** Exibe o valor do BDI aplicado sobre a composição.  
**Valor com BDI:** Exibe o valor da composição com leis sociais e o BDI. Este valor será calculado automaticamente considerando os valores e quantidades de todos os recursos.  
**Coeficiente Improdutivo:** Este campo é calculado de acordo com o valor do Coeficiente Produtivo. A soma dos dois é sempre igual a 1 (100%), e não pode possuir um valor maior que 1, pois ele representa o índice de utilização do equipamento.  
Quando utilizar o Gerador de Relatórios, os campos de D.M.T., coeficientes produtivos e improdutivos devem ser divididos por 10.000.  
**Fator K:** Se estiver utilizando o fator k de insumo e de composição, será feito o cálculo do valor parcial do recurso, o mesmo será arredondado e depois serão aplicados os fatores k's.   
Exemplo:  
a)    Cálculo do Valor com BDI de uma Composição de Custo Unitário

|  |  |  |
| --- | --- | --- |
| **Código** | **Descrição** | **Unidade** |
| 000001 | Escavação de Tubulões | M3 |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Código** | **Equipamento** | **Unidade** | **Quantidade** | **Preço Unitário** | **Valor Parcial** |
| F00002 | Compactador | H | 2,0000 | 30,01 | 60,02 |
| P00001 | Ferramentas | % | 5,0000 | 0,03 | 0,17 |
| M00010 | Areia Comum | M3 | 3,5687 | 2,09 | 7,46 |
| F00001 | Servente | H | 3,1765 | 1,10 | 3,49 |
| T00001 | Caminhão | M3 | 4,8000 | 3,00 | 14,40 |
| V00001 | Mobilização | VB | 2,0000 | 15.749,00 | 31.499,98 |
| 000002 | Escavação para blocos | M3 | 4,2000 | 4,02 | 16,88 |

|  |  |  |
| --- | --- | --- |
| **Código** | **Descrição** | **Unidade** |
| 500000 | Concreto Fck >= 18 Mpa | M3 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Código** | **Equipamento** | **Unid.** | **Quant.** | **Coef. Improd.** | **Coef. Produt.** | **Preço Prod.** | **Preço Improd.** | **Valor Parcial** |
| E00002 | Betoneira | H | 1,0000 | 0,4000 | 0,6000 | 125,99 | 72,00 | 93,60 |
| P00001 | Ferramentas | % | 5,0000 | 1,0000 | 0,0000 | 0,14 | 0,00 | 0,68 |

**Total A:** 94,28

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Código** | **Mão de Obra** | **Unid.** | **Quant.** | **Preço Unit.** | **Valor Parcial** |
| F00001 | Servente | H | 8,0000 | 1,10 | 8,80 |
| F00100 | Pedreiro | H | 2,0000 | 2,44 | 4,88 |

**Total B:** 13,68

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Código** | **Materiais** | **Unid.** | **Quant.** | **Preço Unit.** | **Valor Parcial** |
| M00031 | Areia Lavada | M3 | 0,6000 | 2,09 | 1,25 |
| M00040 | Cimento | Kg | 350,0000 | 0,63 | 220,50 |
| M00038 | Brita n.2 | M3 | 0,9000 | 2,36 | 2,12 |
| 607000 | Fornecimento | T | 2,0000 | 1,03 | 2,06 |

**Total E:** 225,93

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Código** | **Transporte** | **Unid.** | **Quant.** | **D.M.T.** | **Preço Unit** | **Valor Parcial** |
| T00001 | Caminhão | H | 1,0000 | 20,0000 | 3,00 | 60,00 |

**Total F:** 60,00  
**Equipamento A** = 94,28  
**Mão-de-Obra B =** 13,68  
**Produção da Equipe P =** 1,00  
**U Custo Unitário Execução (A+B) /C =** 107,96  
**Materiais C =** 225,93  
**Momento de Transporte F =** 60,00ç  
**Custo Direto (U+C+F) =** 393,89  
**B.D.I. 50,00% =** 196,94  
**Valor Total (Custo Direto + BDI) =** 590,84  
   
**Recursos do grupo DNIT B – Mão-de-obra:** Será o produto da quantidade pelo preço unitário (já com o valor da lei social), (Quantidade x Preço Unitário).  
**Recursos do grupo DNIT C – Materiais:** Será o produto da quantidade pelo preço unitário. (Quantidade x Preço Unitário)  
**Recursos do grupo DNIT F – Momento de Transporte:** Será o produto da quantidade pelo D.M.T Total (DMT (Pav.) + DMT (Terra)) e, ainda, pelo preço unitário, (Quantidade x D.M.T Total x Preço unitário). O valor parcial do insumo, independente do grupo DNIT, é multiplicado também pelo fator k do insumo e pelo fator k da composição se o parâmetro estiver marcado em "Menu Projeto | Construção e Projetos | Projeto | Cálculo | Fator k".  
**Composições auxiliares:** Será o produto da quantidade pelo preço unitário (Quantidade x Preço Unitário). O preço unitário da composição auxiliar também passou por um processo de cálculo como esse. Para essas composições auxiliares também determinamos a qual grupo de custo DNIT elas pertencem, no cadastro da composição principal. Caso a mesma seja do grupo F, o preço parcial da mesma é o produto entre a quantidade e o DMT Total, arredonda-se o valor encontrado e multiplica-se pelo preço unitário (Arredonda (Quantidade x DMT Total)) x Preço Unitário. O valor parcial da composição auxiliar, independente do grupo DNIT, é multiplicado também pelo fator k da composição pai se o parâmetro estiver marcado em "Menu Projeto | Construção e Projetos | Projeto | Cálculo | Fator k".  
Todas as opções referentes aos ícones da barra de ícones podem ser acessadas também clicando com o botão direito do mouse em cima de algum recurso ou pelas combinações de teclas descritas em frente a cada opção.  
 

Anexos

[Recursos da Composição](http://tdn.totvs.com/pages/viewpage.action?pageId=421385550)

[Recursos Consolidados](http://tdn.totvs.com/display/LRM/Recursos+Consolidados)

[Impactos em Composições](http://tdn.totvs.com/pages/viewpage.action?pageId=444617442)

[Detalhes dos Recursos](http://tdn.totvs.com/display/LRM/Detalhes+dos+Recursos)

 Processos

[Alteração Geral](http://tdn.totvs.com/pages/viewpage.action?pageId=421385136)

[Excluir Composições não Utilizadas](http://tdn.totvs.com/pages/viewpage.action?pageId=421385265&moved=true)

[Definir  Preço da Composição](http://tdn.totvs.com/pages/viewpage.action?pageId=421385314)

[Cálculo de Composição](http://tdn.totvs.com/pages/viewpage.action?pageId=421385399&moved=true)

[Copiar dados de outra Composição](http://tdn.totvs.com/pages/viewpage.action?pageId=421385331&moved=true)

[Replanejamento de Índices](http://tdn.totvs.com/pages/viewpage.action?pageId=421385544)

[Gerar Relatório de Modelo Fixo Excel](http://tdn.totvs.com/pages/viewpage.action?pageId=421385271)

[Alteração Geral de Composição](http://tdn.totvs.com/pages/viewpage.action?pageId=421385136&moved=true)
