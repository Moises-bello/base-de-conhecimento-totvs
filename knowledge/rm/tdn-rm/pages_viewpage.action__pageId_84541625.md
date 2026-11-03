---
content_hash: d7e3b34e759d94978a1272cc6117632d522a5a4f195c1f3aeed44a6d0e935ec7
fetched_at: '2026-06-29T00:11:50.850962+00:00'
page_id: '84541625'
product: rm
source: tdn-rm
title: RMFIS00001_Controle CIAP - Cálculo CIAP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=84541625
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** *11.5X* |
| **Processo** | **:** | Controle CIAP |
| **Subprocesso** | **:** | Cálculo CIAP - Crédito |
| **Data da publicação** | **:** | 17/09/2013 |

**Introdução**

Controle do Crédito de ICMS do Ativo Permanente - CIAP, destinados a Apuração do Valor Base do crédito de bem do Ativo Permanente.

**Desenvolvimento/Procedimento**

  1. Incluir os bens de ativo. Se possuir o aplicativo TOTVS Gestão Patrimonial a inclusão deverá ser feita pelo mesmo.

***Acesse: Cadastros / Tabelas Auxiliares / Bens***

  2 .Habilitar o campo Controla Ativo Permanente indicar data de início para o cálculo e optar pelos modelos (determinado para cada Estado)

***Acesse: Opções / Parâmetros / Gerais Tabelas /Identificação de Regras de Apuração ICMS / Regras de ICMS por Filial (selecionar a filial) /  Livro CIAP ½.*** Informe a data de inicio e marque a opção CIAP - Modelo C.

3. Editar o Sub Grupos onde serão selecionadas as naturezas de operações de saída que serão consideradas para calculo do CIAP. Informar data inicial e final da vigência do grupo:

***Acesse: Opções / Parâmetros / Processo /Selecionar a opção Calculo do CIAP/ Clicar no ícone Grupos-SubGrupos***

  4. Selecionar Natureza de Operação Final e Inicial e também o que o sistema vai considerar como tributado para o calculo do valor a ser creditado

 5. Selecionar o Subgrupo nos parâmetros referente ao Controlo do CIAP

***Acesse: Opções / Parâmetros / Gerais Tabelas / Cadastros / Natureza de Operação /Identificação de Regras de Apuração ICMS / Regras de ICMS por Filial (selecionar a filial) /  Livro CIAP 2/2***

6 . Incluir natureza fiscal com tipo de ICMS ‘K-Compra de Ativo Imobilizado’ ou tipo ‘T-Compra p/ Ativo Imobilizado Dif. Alíquota’. Incluir também a natureza fiscal com tipo de ICMS ‘W-Complementar’ com  tipo IPI ‘Sem IPI’ para criação do lançamento do crédito 1/48

***Acesse: Cadastros / Natureza de Operação / Cadastro de Natureza Fiscal***

**Descrição do Processo**

* + Incluir lançamento fiscal com natureza fiscal com tipo W-Compra Ativo Imobilizado;
  + Informar o valor do ICMS relativo à aquisição **do bem e a chapa do mesmo** na tela dos itens do lançamento fiscal;
  + Liberar os lotes do período de apuração em que se deseja gerar o CIAP (quando for utilizado);
  + Encerrar o Período de Apuração que será gerado o CIAP;

***Acesse: Lançamentos / Período de Apuração / ICMS***

* + Calcular o CIAP através do ícone(Processos) calcula CIAP no período de apuração; Acesse o período de apuração, selecione-o e acesse Processos/Calculo CIAP.

* + Reabrir o Período de Apuração;
  + Gerar lançamento 1/48 referente ao Crédito do Ativo Imobilizado;

***Acesse: Utilitários / Ativo Imobilizado / Geração de Lançamento – Crédito 1/48***

* + Informar a filial para criação do mesmo;
  + Cadastrar um fornecedor Fictício para esta operação;
  + Informe a espécie a ser gerada;
  + Informar o número do documento a ser gerado;
  + Data LF será o último dia do mês;
  + Selecionar Exercício Fiscal;
  + Natureza Origem Início / Final, deverão ser selecionadas de acordo com os lançamentos relativos à compra do Ativo Imobilizado;
  + A natureza Destino (com o Tipo W-Complementar) deverá ser selecionada para utilização da criação do lançamento Fiscal;

Gerar relatório CIAP – Controle de Ativo Permanente ( o tipo será selecionado conforme determinado pelo Estado)

**Informações Adicionais**

O Cálculo do valor do credito a ser apropriado e calculado através dos lançamentos que foram utilizadas as naturezas selecionadas no Processo CIA. O cálculo é feito da seguinte maneira:

Tributadas e Exportação (Referente aos lançamentos de Saída)

                      : (dividido)

Total das Saídas (Selecionadas no Subgrupos do Processo CIA)

                =

Coeficiente Creditamento

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Coeficiente Creditamento

               x

Saldo Acumulado

              x

Fração Mensal(Valor 1/48)

              =

Crédito a ser Apropriado

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/_layouts/searchresults.aspx?k=CIAP&u=http%3A%2F%2Fwikihelp%2Etotvs%2Ecom%2Ebr%2FWikiHelp)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
