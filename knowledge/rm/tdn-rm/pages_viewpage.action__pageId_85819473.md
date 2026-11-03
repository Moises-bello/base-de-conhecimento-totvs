---
content_hash: 0af3002325281dfae334a6b41d75bbb686ec3b99fce536fdaa3b3bd8d3a623da
fetched_at: '2026-06-29T00:11:54.864735+00:00'
page_id: '85819473'
product: rm
source: tdn-rm
title: RMFIS00004_Gerando a rotina DIEF\PA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=85819473
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:**11.52 |
| **Processo** | **:** | Gerar DIEF\PA |
| **Subprocesso** | **:** | Implementação da rotina DIEF\PA |
| **Data da publicação** | **:** | 16/09/2013 |

## 1.       Passos para implantação da Rotina DIEF\PA

1-      Atualizar a versão da Biblioteca **11.52.58.xxx** e superiores

2-      Versão do Aplicativo TOTVS Gestão Fiscal **11.52.58.xx**e superiores.

3-      Importar o Layout da Rotina

**ESPÉCIE DE DIEF**

A partir de janeiro de 2009, a Instrução Normativa nº 004, de 19 de fevereiro de 2004, prevê somente uma espécie de Declaração, denominada “**DIEF** **mensal**”. A **DIEF** mensal deverá ser entregue, mensalmente, pelos contribuintes do ICMS, observada a orientação de preenchimento prevista no Manual.

**PRAZO DE ENTREGA DA DIEF**

A **DIEF** deverá ser entregue, nas hipóteses de apresentação abaixo, até o dia:

√  normal: 10 do mês seguinte ao da apuração do ICMS;

√  baixa: 10 do mês seguinte a data do pedido de baixa ou paralisação temporária.

 Quando o término do prazo de entrega for sábado, domingo ou feriado, o contribuinte poderá apresentar a DIEF até o primeiro dia útil subsequente à referida data.

**LOCAL DE ENTREGA DA DIEF**

Os arquivos gerados  serão  transmitidos,  por meio  da Internet,  utilizando  o programa **Transferência Eletrônica de Dados - TED** (disponível para download no site da SEFAZ). Para as versões anteriores ao ano de 2006, o programa que transmite a **DIEF** é o **SEFANET** (disponível para download no site da SEFAZ).

**Geração da Rotina**

A Rotina será gerada pelo Gerador de Saída - (Modulo Utilitários|Gerador de Saídas|Layout)

Selecionar o Layout da DIEF – PA. Processos selecionar Gerador de Saídas

É apresentado um caminho Default onde será gerado o arquivo da Rotina, mas o usuário pode alterar.

Tela de Inclusão dos Campos para Geração da Rotina

**Data inicial e Data Final**:

Informe o período de referência o qual se deseja a geração do arquivo.

**Coligada**:Informar a Coligada a qual a Filial pertence.

**Filial**:Informar a Filial a qual se deseja gerar o arquivo

**Classificação de Municípios**:

Informe a Classificação de Municípios que será utilizada na geração da rotina. A Classificação de Município é cadastrada em **Cadastros | Tabelas Auxiliares | Classificação de Município**.

É  necessário utilizar a Classificação do Município do Pará, pois conforme o manual, os códigos deve ser gerados conforme terminado pela SEFAZ.

**Tipo de Declaração**:

01 – Normal | 02 – Substitutiva| 03 – Baixa

**Declaração Sem Movimento**:

1 – Sim (Sem Movimento) | 0 – Não (Com Movimento)

**Tipo de Tributação do Imposto**: 1 – Lucro Presumido| 2 – Simples | 3 – Lucro Real

Este campo é referente a a modalidade de tributação do Imposto de Renda que a empresa utiliza

**Forma de Escrituração do Imposto**: 1 – Caixa| 2 – Escrituração Contábil

Tipo de escrituração adotado pelo contribuinte referente ao Imposto de Renda.

**Anexo III – Delcaração Sem Receitas**: 0 – Não| 1 – Sim

Obs:  Para 2013, informar 0 (zero) – Não.

**Anexo I (Anual) – Declaração Sem Serviço**: 0 – Não | 1 – Sim

**Troca de Município**: 0 – Não|  1 – Sim

Informar se houve troca de Município pelo Contribuinte

**Anexo V- Sem Operações com Cartões de Crédito/Débio**: 0 – Não| 1 – Sim

**Anexo I (Mensal) – Declaração Sem Serviço**: 0 – Não| 1 – Sim

**Valores referente a Estoque**:

* **Livro de Inventário Estoque Inicial e Final do Ano 2012:**

É de preenchimento obrigatório na **DIEF**:

√  normal ou retificadora: no período de 02/2013;

√  de baixa, paralisação temporária e mudança  de Município: nos períodos de 01/2013  e 02/2112. Para os estoques de 2012, os dados a serem informados são os valores registrados em 1º de

janeiro (estoque inicial) e 31 de dezembro (estoque final), do ano de 2012.

* **Livro de Inventário Estoque Inicial e Final do Ano 2013:**

É de preenchimento obrigatório, em qualquer período, nas seguintes situações:

√  Mudança de endereço com alteração do Município de localização do estabelecimento

√  Encerramento (baixa)

√  Pedido de paralisação temporária da atividade econômica

Para os estoques de 2013, os dados a serem informados são os valores registrados em 1º de janeiro (estoque inicial) e a data em que ocorreu o fato (estoque final)

Estoque Inicial – Para Venda (Ano Anterior)

Estoque Inicial – de Uso e Consumo (Ano Anterior)

Estoque de Terceiro (Ano Anterior)

Estoque Final – Para Venda (Ano Anterior)

Estoque Final – de Uso e Consumo (Ano Anterior)

Estoque de Terceiro(Ano Anterior)

Estoque Inicial – Para Venda (Ano Atual)

Estoque Inicial – de Uso e Consumo (Ano Atual)

Estoque de Terceiro (Ano Atual)

Estoque Final – Para Venda (Ano Atual)

Estoque Final – de Uso e Consumo (Ano Atual)

Estoque de Terceiro(Ano Atual)

Após o preencher todos os campos necessários para geração da Rotina| Avançar

Após a geração da Rotina é apresenta tela de execução do processo, o usuário deverá verificar se houve algum erro ou se a geração foi feita com sucesso.

**Para maiores informações:**

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
