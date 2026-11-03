---
article_id: 19851633304087
category: Financeiro - Consultas / Relatórios
content_hash: b5de26e51c42e7cfd300aba2ed676e23349f2e88fccc21cb7dc5b21e10bf3e67
fetched_at: '2026-06-28T22:37:58.372514+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  FINR133 - Conceito
  do relatório Aging Contas a Receber
type: support-article
updated_at: '2026-03-25T14:44:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19851633304087-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR133-Conceito-do-relat%C3%B3rio-Aging-Contas-a-Receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19851573929879) Tempo aproximado para leitura: **00:06 min**  
  
**Dúvida**  
Qual o conceito do relatório AGING para carteira contas a receber?

**Ambiente**

Cross Segmento - TOTVS Backoffice Linha Protheus- Financeiro - Todas as versões.  
  
**Solução**

Exemplo de conceito:

Dois clientes que estão com as dívidas em dia. Um deles honrou seus pagamentos na data de vencimento, já o segundo atrasou alguns pagamentos.  
Com o "Aging" é possível visualizar o atraso do cliente 2.

**Procedimentos**

Para imprimir o relatório de **FINR133 - Aging**:

1. No menu do Módulo Financeiro selecionar a opção **Relatórios > Contas a Receber > Aging.**
2. Para configurar os dados a serem impressos no relatório, selecionar a opção **Outras Ações > Parâmetros.**
3. Ao selecionar a opção, o sistema apresenta uma tela com os campos para seleção de dados.
4. Preencha os parâmetros conforme orientação do help e confirme para prosseguir.
5. Solicite a impressão e confirme

**Tabelas Utilizadas**

| Tabela | Descrição |
| --- | --- |
| SA1 | Cliente |
| SE1 | Contas a Receber |
| SE5 | Movimentação Bancaria |

Quando utilizado o parâmetro 8 (Tipo de Intervalo) como "Informado" mostra o grupo de perguntas "**FI133B**", conforme a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19851602976791)

Cada conteúdo será usado para preencher o cabeçalho de colunas alteráveis da Posições 7 até 18.

**Casos de uso**

**Data Base : 01/07/2015**  
**Filial: Empresa 01 / Filial 01 - Matriz**

## **Títulos a Receber:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19851892894103)

Parâmetros preenchidos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19851939160343)

Detalhamento:

1 e 2 - É a faixa de clientes, por código (todos os clientes);  
3 e 4 - É a faixa de emissão dos títulos (títulos emitidos de 01/07/2015 a 31/07/2015);  
5 - Modo Analítico mostrará detalhes dos títulos

6,7,8 e 9 - Irá moldar o cabeçalho das colunas com datas e as linhas com valores dos títulos

10 - Define para usar a "moeda 1"  
11 - Seleciona apenas os títulos com "moeda 1"  
12 - Relaciona também os cheques  
13 - Usa o valor da "moeda 1" na data de referencia  
14 - Seleciona apenas títulos da filial atual (Empresa 01 / Filial 01 )

**Observe a seguir:**

A seleção acima dará o seguinte resultado:

Cabeçalho de colunas fixas: Posições (1) Filial Ori, (2) Vencto Real, (3) Tipo, (4) Prefixo, (5) No.titulo,

(6) Parcela, (19) Saldo e (20) TPSALDO

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19851939175575)

Cabeçalho de colunas alteráveis: Posições 7 à 18

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19851939191447)

**Explicação:**

O parâmetro 6 ( Data de referencia ) igual à 01/07/2015, determina a data que será mostrada na coluna. A coluna iniciou no dia 01/07/2015 porque o parâmetro 7 está como zero.

Nota: O parâmetro 9  pode conter 0 ou 1 que irão causar o mesmo efeito, deixando o intervalo igual a um.

**Usando parâmetro 8 para "dias" e parâmetro 7 com valores diferentes:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19851892942871)

***Nota: - O valor máximo a ser considerado no "parâmetro 7" é 10. Superior a 10, ainda assim será considerado o valor 10.***

**Usando parâmetro 8 para "meses":**

Cabeçalho de colunas alteráveis: Posições 7 à 18

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19851892955287)

**Usando parâmetro 8 para "meses" e parâmetro 7 com valores diferentes:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19851892974231)**

**Usando o parâmetro 8 como "dias" e variando o conteúdo do parâmetro 9 (Intervalo ):**

Cabeçalho de colunas alteráveis: Posições 7 à 18

Usando parâmetro 9 (Intervalo) = 5

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19852149044375)

Usando parâmetro 9 (Intervalo) = 10

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19852149055639)

Usando parâmetro 9 (Intervalo) = 20

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19852149067927)

Usando o parâmetro 8 como "Informado", o sistema desconsidera o parâmetro 9 e solicita todas as datas a serem consideradas.

**Nota: - Obrigatoriamente, uma das 11 datas deve coincidir com conteúdo do parâmetro 6 (Data de Referencia) , e neste exemplo é a "Data Intervalo 01".**

**Saiba mais**

[FINR133 - Aging Contas a Receber](https://tdn.totvs.com/display/PROT/FINR133+-+Aging)
