---
content_hash: bd537a96dab45a9398d33f8cd262bb10b1da42945e388ae195ec7c052e49ca0f
fetched_at: '2026-06-29T00:09:15.351105+00:00'
page_id: '421385356'
product: rm
source: tdn-rm
title: Conversão de item de permanência em preço unitário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385356
version: 4
---

---

Este processo realiza um rateio no valor pré - determinado de um item em vários outros itens, conforme alguns critérios de rateio.

**Observação:**

O rateio de um item deverá ser realizado em uma única vez e fechar em 100%.

**O item(Tarefa) que possuem divisão não pode ser convertido.**

Os critérios de rateio são:

**Homem-Hora**: Fórmula definida em Opções - Parâmetros - Totvs Obras e Projetos - Projetos - Cálculo - Orçamento de Montagem.

**Peso:**  Fórmula definida em Opções - Parâmetros - Totvs Obras e Projetos - Projetos - Cálculo - Orçamento de Montagem.

**Linearmente:**  Realiza o rateio de uma forma igual entre os itens.

**Informado manualmente**:  Permite que seja informado um percentual a ser rateado em cada atividade.

**Proporcional ao valor:**  O sistema realiza uma proporcionalidade conforme o valor da tarefa.

O processo é constituído dos seguintes passos:

* Exibição das tarefas selecionadas para o rateio.
* Inclua o tipo de rateio e o percentual que será realizado.

**Observação:**

O total do percentual deve fechar em 100%.

O processo de transformação do item de permanência irá criar uma nova composição, esta composição não poderá ser utilizada como composição auxiliar e nem vinculada à tarefa. O recurso que estava na tarefa originalmente será incluído na composição, como recurso.

**Atenção:**

A nova composição gerada a partir da 'Conversão de item de permanência' é chamada composição de sistema.

Em uma composição de sistema apenas será possível editar os campos:

Código,

Descrição,

Descrição completa,

Campos Livres e

Campos complementares.

A quantidade do item rateado(no recurso da composição) será a quantidade rateada dividido pela quantidade da tarefa que recebeu o rateio.  
   
Neste processo os itens de permanência ficarão inativos na planilha e conseqüentemente o custo não entrará no cálculo do projeto.  
Caso a tarefa esteja sem nome o sistema emite uma mensagem na hora de realizar a conversão "A descrição da composição deve ser informada".

**Exemplo do Cálculo:**

Exemplo de rateio e explicações de arredondamento

Insumo A - R$ 49,00  
Insumo B - R$ 73,00  
Insumo C - R$ 103,00  
Insumo D - R$ 137,00

Teremos cada atividade ligada a um insumo

**Atividade   Quantidade  Recurso   Custo Unit.  Custo Total**Tarefa A       25                  Insumo A     R$ 49,00        R$ 1.225,00  
Tarefa B       51                  Insumo B     R$ 73,00        R$ 3.723,00  
Tarefa C       83                  Insumo C    R$ 103,00       R$ 8.549,00  
Tarefa D       95                  Insumo D    R$ 137,00       R$ 13.015,00  
                                                                                                      Total: R$ 26.512,00

Rateio utilizando o critério linear da Tarefa D nas outras 3 atividades.

Portanto, teremos a quantidade 95 rateada nas outras.

**Atividade  % rateio    Quantidade assumida**Tarefa A         33,33           31,66  
Tarefa B         33,33           31,66  
Tarefa C         33,34           31,68  
                                                            Total: 95,00

Definidas as quantidades que cada atividade deve receber, temos agora que considerar

a quantidade da atividade para definir a quantidade correta a ser incluída na respectiva atividade.

Para a Tarefa A teremos 31,66 dividido por 25, para a B 31,66 dividido por 51 e para a C 31,68 dividido por 83.

**Atividade    Quantidade atividade   Quantidade assumida**Tarefa A           25                                      1,27  
Tarefa B           51                                      0,62  
Tarefa C           83                                      0,38

Sendo assim, esse projeto terá a seguinte estrutura:

**Atividade      Quantidade    Recurso         Custo Unit.      Custo Total**Tarefa A                    25               CMPSIS-A                 R$ 222,99             R$ 5.574,75

**Recursos**               1         Insumo A     R$ 49,00       R$ 49,00  
              1,27     Insumo D     R$ 137,00      R$ 173,99

**Atividade  Quantidade      Recurso     Custo Unit.     Custo Total**Tarefa B          51                  CMPSIS-B        R$ 157,94         R$ 8.054,94

**Recursos**               1        Insumo B     R$ 73,00       R$ 73,00  
              0,62     Insumo D    R$ 137,00       R$ 84,94

**Atividade  Quantidade    Recurso      Custo Unit.     Custo Total**Tarefa C         83                   CMPSIS-C       R$ 155,06         R$ 12.869,98

**Recursos**               1        Insumo C    R$ 103,00      R$ 103,00  
              0,38     Insumo D    R$ 137,00       R$ 52,06

**Atividade  Quantidade     Recurso      Custo Unit.    Custo Total**Tarefa D         95                   CMPSIS-D              -                     -              atividades está desativada

**Recursos**              1        Insumo D    R$ 137,00      R$ 137,00                    

                                                                                 Total: R$ 26.499,67

Note que devido a alguns cálculos que necessitam de arredondamento, em várias situações não é possível gerar exatamente ao valor original do projeto.

Uma composição de sistema não pode ser excluída, simplesmente ao clicar em excluir. Desfazendo a conversão de item de permanência, a composição de sistema é excluída automaticamente.

---
