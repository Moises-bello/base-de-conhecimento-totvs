---
content_hash: e9794c175189e1a6b8a0e8805cefdf6f1189e6c545aff20aca61179390d55974
fetched_at: '2026-06-29T00:10:27.650147+00:00'
page_id: '516630807'
product: rm
source: tdn-rm
title: Compilador de Hemocultura CIH
type: documentation
url: https://tdn.totvs.com/display/LRM/Compilador+de+Hemocultura+CIH
version: 5
---

## 

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela inicial**
4. **Tabelas utilizadas**

PainelVisão Geral

## **01. VISÃO GERAL**

Através dessa funcionalidade, são carregadas todas as internações que contenham culturas de sangue no período informado. Caso existam culturas de sangue colhidos na mesma data, serão verificados seus resultados (germes) e antibiogramas.

Resultados (germes) iguais, com antibiogramas iguais serão "mesclados", resultando em apenas um germe. As amostras dos germes serão somadas. Caso o '' germe1'' tenha sido encontrado na amostra 1 e o mesmo '' germe1'' em outro pedido de mesma data tenha sido encontrado na amostra 2, o '' germe1'' passará a existir em apenas uma cultura, porém nas amostras 1 e 2.

Germes diferentes continuarão sendo mostrados em separado (de acordo com as amostras em que foram isolados).

No final do processo só existirá 1 pedido de cultura de sangue contendo todos os resultados (germes) e antibiogramas de todos os pedidos com a mesma data.

O campo Nº Amostras, no cadastro de Cultura Final, deve exibir o número de amostras que foram compiladas.

O intervalo em minutos configurado parâmetro abaixo, vai definir a tolerância em que as amostras serão consideradas como geradas no mesmo horário.

Exemplo: considerando o parâmetro acima como 30 minutos, se houverem duas amostras geradas na mesma data, uma às 9:00 e outra às 9:25, essas serão compiladas.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Saúde > Controle de Infecção Hospitalar > Utilitários > Processo > Compilador de Hemocultura

Tela Inicial

## **03. TELA INICIAL**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Procedimento para inclusão | 1. No Controle de Infecção Hospitalar acesse Utilitários / Processo/ Compilador de Hemocultura. 2. Preencha o período e clique em Executar. 3. Caso no período informado constem internações que contenham culturas de sangue serão exibidas na tela. |

Tabelas Utilizadas

## **04. TABELAS UTILIZADAS**

SZJPEDIDOCULTURA, SZJRESULTADOCULTURA, SZJANTIBIOGRAMA.
