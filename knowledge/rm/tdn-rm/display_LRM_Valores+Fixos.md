---
content_hash: 065a7c8a8f4d6f4152222fd156efb024417f546efa8e4d6aab4a6a14cd157b88
fetched_at: '2026-06-29T00:10:11.152719+00:00'
page_id: '452719953'
product: rm
source: tdn-rm
title: Valores Fixos
type: documentation
url: https://tdn.totvs.com/display/LRM/Valores+Fixos
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Valores Fixos**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Nesta pasta, incluímos e/ou editamos valores fixos, que são aplicados com frequência na movimentação (por exemplo: valor do salário família, valor do salário mínimo, ticket, etc), definindo, também, o período de vigência de tais valores. 

**Observação**

Não será copiada a tabela de valores fixos para outra coligada quando na coligada destino existir interseção de datas com o mesmo código. Porém, é possível sobrepor os valores fixos da coligada destino se as datas de início, fim, código e finalidade forem iguais e as mudanças só ocorrerem para os campos Nome e Valor.

**Exemplo**

Código SMIN com interseção 01/04/2006 a 31/03/2007. 

Se o usuário tentar copiar de outra coligada onde já existia um valor com o mesmo código SMIN, com mesma finalidade e a mesma com interseção 01/04/2006 a 31/12/2007, não será realizada a cópia enquanto o valor fixo da coligada destino não for excluído ou as datas não forem alteradas.  
 

**Atenção**

Caso seja criado um valor fixo com finalidade igual à Taxa de CPMF para salário família o valor informado no campo "Valor" será a porcentagem a ser acrescida no valor do salário família do funcionário.

## **02. EXEMPLO DE UTILIZAÇÃO**

**Exemplo utilizando** [Cálculo do IRRF Simplificado](https://tdn.totvs.com/pages/viewpage.action?pageId=761006653)

11Valor fixo de Valor deduzir por dependente

Cadastro do valor fixo de valor deduzir por dependente no imposto de renda:

No cálculo do Imposto de Renda será utilizado o valor fixo que a competência do cálculo está dentro da vigência. Para isso será utilizado o código e a Finalidade dentro do cadastro. Por esse motivo, sempre que o valor for alterado deve ser criado novo valor fixo com o mesmo código e vigências diferentes.

              Calculando evento: 0004 - IRRF

              Código de Cálculo 4 - Prioridade 83              

                     Base de IRRF: 

                         Proventos = 5.885,11

                         Descontos = 0,00

                         Valor Dedutível = 0,00

                         Base Líquida = 5.885,11                         

                     Nro. dependentes de IRRF: 0

                    **Valor a deduzir por dependentes: 189,59**

                     Valor do INSS: 660,09

                     Base de IRRF: 5.225,02

                     Limite Superior da Faixa na Tabela de IRRF: 99.999.999.999,00

                     Percentual da Faixa na Tabela de IRRF: 27,5000 %

                     Valor a Deduzir da Faixa na Tabela de IRRF: 884,96

                     Valor do IRRF: Base(5.225,02) \* 27,5000% - 884,96 = 551,920500

                     Valor do evento: 551,92

2Exemplo utilizando fórmula

**Utilizando valor fixo em fórmula**

Desconto do ticket refeição na empresa tem a seguinte característica: Valor do Ticket \* 20%

Poderíamos cadastrar um valor fixo com as seguintes características: 

Código: 001 Nome: Ticket Valor fixo = 10,00 

No cadastro de fórmulas, montaremos a seguinte fórmula: F(001) \* 0.20 

Na Janela de Edição do Evento (pasta Identificação) foi cadastrado o desconto "Vale Refeição", informando-se essa fórmula. 

Ao lançar esse evento na movimentação, o sistema calculará "R$ 2,00" a ser considerado por ticket para os funcionários.

## **03. TELA Valores Fixos**

**Principais Campos e Parâmetros**

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Código | Pode haver dois ou mais Códigos iguais, desde que os períodos de vigência sejam diferentes e com a mesma finalidade |
| Nome | Descrição do valor fixo |
| Início de Vigência | Início de Vigência do valor fixo |
| Fim de Vigências | Fim de Vigência do valor fixo |
| Valor | Valor do valor fixo |
| Finalidade | A finalidade orientará o sistema na aplicação do valor fixo. Valores definidos como "Sem finalidade específica" podem ser usados em fórmulas. |
| Atualiza final de vigência na liberação de competência | Atualiza final de vigência na liberação de competência |

## **04. TABELAS UTILIZADAS**

* PVALFIX
