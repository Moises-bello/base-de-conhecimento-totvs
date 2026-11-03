---
content_hash: 48b077b3fee1adf33a78f5eaa7cf6ccfb1de0f98f9bc814b8ffea295ce635d3d
fetched_at: '2026-06-29T00:08:15.827257+00:00'
page_id: '244925107'
product: rm
source: tdn-rm
title: 2. Evento Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244925107
version: 7
---

|  |  |
| --- | --- |
| Descrição | Evento Contábil |
| Observações | Para que seja possível definir como será a contabilização será utilizado o recurso de Evento Contábil que sofrerá alterações afim de atender a demanda de Locação / Arrendamento. |

# 2.1. Processo

Serão criados duas novas opções de processos no cadastro do Evento Contábil, são elas: "Aluguel: Contrato"  e "Aluguel: Rescisão" .

A contabilização pode ser feita de duas formas: Padrão e Linear. Esta definição será feita no cadastro do contrato de locação.

Para processos de locação serão gerados lançamentos contábeis mês a mês, conforme mês da prestação de serviço.

# 2.2. Buscar Filial / Depto em

No recurso de buscar Filial / Depto devem ser fornecidas as opções de:

* Contrato de Locação: busca a filial e o departamento dos parâmetros de integração financeira associado ao contrato de locação que está sendo contabilizado, se a arquitetura for alterada copiando os dados dos parâmetros de integração para o contrato de locação este default deve ser alterado para buscar direto do contrato de locação no campo responsável pelo valor replicado.
* Default Contábil: busca a filial e o departamento, do default contábil, da partida que está sendo processada;
* Evento Contábil: busca a filial e o departamento, do evento contábil que está sendo processado.

O evento contábil permite que mais de um default seja marcado, e neste caso deve ser respeitada a ordem de execução ou a ordem da lista de opções.

 Mesmo havendo mais de uma fonte de consulta para o default, pode ser que nenhum dado seja encontrado, quando este caso acontecer o processo de contabilização deve retornar Erro e informar ao usuário que determinado dado não foi encontrado.

# 2.3. Buscar Centro de Custo em

No recurso de buscar Centro de Custo em devem ser fornecidas as opções de:

* Contrato de Locação: busca centro (s) de custo (s) dos parâmetros de integração financeira associado ao contrato de locação que está sendo contabilizado, se a arquitetura for alterada copiando os dados dos parâmetros de integração para o contrato de locação este default deve ser alterado para buscar direto do contrato de locação no campo responsável pelo valor replicado.
* Default Contábil: busca o centro de custo, do  default contábil, da partida que está sendo processada;
* Evento Contábil: busca o centro de custo, do evento contábil que está sendo processado;
* Rateio do Contrato: busca o default contábil do rateio de centro de custo do contrato de locação. A consulta pode retornar mais de um centro de custo e neste caso deve ser considerado a proporção % do centro de custo;

 O evento contábil permite que mais de um default seja marcado, e neste caso deve ser respeitada a ordem de execução.

 Mesmo havendo mais de uma fonte de consulta para o default, pode ser que nenhum dado seja encontrado, quando este caso acontecer o processo de contabilização deve retornar Erro e informar ao usuário qual dados não foi encontrado.

O recurso “Aplicar Centro de Custo em” permanece com os defaults existentes (Nenhum, contas de débito, contas de crédito, Contas de Débito e Credito e nenhum).

 As opções abaixo devem estar habilitadas e com funcionamento padrão.

* “Agrupa Partida Contábil”
* “Não Ajusta Automaticamente o valor da contabilização”
* “Não arredondar valor processado pela formula”

# 2.4. Item Contábil

Serão feitas as seguintes alterações no item do evento contábil.

## 2.4.1. Aplicar

No item Contábil a opção “Aplicar” será disponibilizado nas seguintes opções:

1. Contrato de Locação (incluído Escalonamento);
2. Item do contrato de locação;
3. Rateio de Centro de Custo;
4. Evento Financeiro; (somente para o processo de Locação – Evento Financeiro)
5. Rescisão. (somente para o processo de Locação – Rescisão)  
     
     

   Novas opções podem ser acrescidas em tempo de projeto afim de atender novos cenários que forem identificados.

   Não será possível deixar a opção em branco;

## 2.4.2. Buscar Default em

As tabelas default dependem do valor escolhido para a opção “Aplicar”. Na opções de tabela default, para o campo “Buscar Default em” devem ser criadas as seguintes opções:

1. **Contrato de Locação**
   1. Cliente / Fornecedor
   2. Filial
   3. Centro de Custo
   4. Departamento
   5. Natureza Financeira Orçamentária Pagar
   6. Natureza Financeira Orçamentária Receber
   7. Tipo de Documento Pagar
   8. Tipo de Documento Receber
   9. Conta Caixa
   10. Contrato de Locação
   11. Tipo de Contrato
   12. Parâmetro de Integração Financeira
   13. Tipo de Evento Financeiro
2. **Item do contrato de locação**  
   1. Cliente / Fornecedor
   2. Filial
   3. Centro de Custo
   4. Natureza Financeira Orçamentária Pagar
   5. Natureza Financeira Orçamentária Receber
   6. Tipo de Documento Pagar
   7. Tipo de Documento Receber
   8. Contrato de Locação
   9. Imóvel
3. **Rateio de Centro de Custo**  
   1. Centro de Custo
4. **Evento Financeiro**  
   1. Cliente / Fornecedor
   2. Filial
   3. Centro de Custo
   4. Departamento
   5. Natureza Financeira Orçamentária Pagar
   6. Natureza Financeira Orçamentária Receber
   7. Tipo de Documento Pagar
   8. Tipo de Documento Receber
   9. Conta caixa
   10. Modelo de Contrato
   11. Tipo de Contrato
   12. Parâmetro de Integração Financeira
   13. Tipo de Evento Financeiro
5. **Rescisão**  
   1. Cliente / Fornecedor
   2. Filial
   3. Centro de Custo
   4. Departamento
   5. Natureza Financeira Orçamentária Pagar
   6. Natureza Financeira Orçamentária Receber
   7. Tipo de Documento Pagar
   8. Tipo de Documento Receber
   9. Contrato de Locação
   10. Modelo de Contrato
   11. Parâmetro de Integração Financeira
   12. Tipo de Evento Financeiro

## 2.4.3. Valor

Serão disponibilizados no evento contábil os seguintes Valores de contabilização:

1. Contrato de Locação e Rateio de Centro de Custo
   1. Valor Total do Contrato.
   2. Valor Final.
   3. Valor de Desconto.
   4. Valor Final Anteior.
   5. Valor de Resíduo.
   6. Valor da Taxa de Administração.
   7. Valor da Taxa de Intermediação.
2. Item do contrato de locação
   1. Valor.
   2. Valor Anterior.
3. Evento Financeiro.
   1. Valor do Evento Financeiro.
4. Rescisão
   1. Valor do Desconto - Locador
   2. Valor da Rescisão - Locador
   3. Valor Final da Rescisão - Locador
   4. Valor do Desconto - Locatário
   5. Valor da Rescisão - Locatário
   6. Valor Final da Rescisão - Locatário

Valores Linearizados disponíveis  quando Aplicado em Contrato de Locação, Item do contrato de locação e Rateio de Centro de Custo

|  |  |
| --- | --- |
| **Valores Default** | **Origem/ Calculo** |
| **Receita Linear** | RL = (∑período (VO\* ia) ) /iT |
| **Desconto Linear** | DL= (∑período (VO\* D)\* ia) /iT |
| **Receita Liquida** | Rec = ((VO+VR)\*(- D))+VO+VR |
| **Provisão de Receita Linear** | PRL=( Rec -(-DL) |
| **Provisão de Linearização** | PL= (RL+ (-DL) ) –Rec |

*As variáveis nas fórmulas acima apresentadas serão identificadas no tópico Modelos Contábeis.*

*Novas opções podem ser acrescidas em tempo de projeto afim de atender novos cenários que forem identificados.*

## 2.4.4. Funções de Fórmula

Assim como os valores padrões fornecidos pelo evento contábil novas funções de formula deverão ser criadas para permitir a utilização de fórmulas com maior aderência.

 Serão opções de Funções de Fórmula:

Serão opções de Funções de Fórmula:

* Receita Linear;
* Desconto Linear;
* Receita Liquida;
* Provisão de Receita Linear;
* Provisão de Linearização;
* Provisão de Desconto Linear;
* Valor Total do Contrato;
* Valor Final;
* Valor de Desconto;
* Valor de Reajuste;
* Valor Final Antes do Reajuste;
* Valor Final Depois do Reajuste;
* Valor de Resíduo;
* Receita Linear;
* Desconto Linear;
* Receita Liquida do Contrato;
* Provisão de Receita Linear;
* Provisão de Linearização;
* Valor Original da Parcela ;
* Valor Liquido da Parcela;
* Valor do Evento Financeiro;
* Valor da Taxa de Administração (provisionada);
* Valor da Taxa de Intermediação (provisionada);
* Dados da Tabela de Contrato de Locação (já Existe);
* Dados da Tabela de Item do Contrato de Locação (já Existe);
* Dados da Tabela do Imóvel do Contrato de Locação;
* Dados da Tabela de Rateio de Centro de Custo (em contexto);
* Dados da Tabela de Reajuste do Item e do Contrato de Locação (em contexto);
* Dados da Tabela do Evento Financeiro (em contexto);
* Dados da Tabela de Escalonamento (em contexto);

*Opções podem ser acrescidas ou excluídas em tempo de projeto afim de atender novos cenários que forem identificados.*
