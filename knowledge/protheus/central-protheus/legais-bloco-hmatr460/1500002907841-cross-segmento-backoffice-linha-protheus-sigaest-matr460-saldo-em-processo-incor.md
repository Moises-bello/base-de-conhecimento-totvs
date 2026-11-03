---
article_id: 1500002907841
category: LEGAIS - BLOCO H/MATR460
content_hash: 508b6dd9390f8bc1b0bc4f153364f69f84824fc847d6f96e64783e8fdce34461
fetched_at: '2026-06-28T22:42:15.156668+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Saldo "Em
  Processo" incorreto. O que fazer?
type: support-article
updated_at: '2023-06-29T18:10:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002907841-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Saldo-Em-Processo-incorreto-O-que-fazer
---

**Dúvida**

Ao emitir o relatório MATR460 (Inventário Modelo 7) está sendo impresso, na seção "Em Processo", valores incoerentes/incorretos. Como identificar para ajustar?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17

**Solução**

O Saldo em Processo nada mais é do que um saldo de um produto que está sendo processado para seu consumo gerar um Produto Acabado. Normalmente OPs cujas Matérias Primas ainda estão em processo de consumo para geração do Produto Acabado.

O Saldo em Processo do P7 tem duas premissas:

* Consideração do Armazém de Apropriação Indireta (MV\_LOCPROC) quando ativado o parâmetro MV\_M460PRC;
* Consideração de produtos que estão sendo consumidos em um processo de um Produto Final.

Desta forma, avalie:

- Data da parametrização do Relatório P7 precisa obrigatoriamente estar de acordo com o MATR989, com uma observação: Armazém de Apropriação Indireta (MV\_LOCPROC) **não aparece no relatório MATR989**;

- O filtro de armazéns é extremamente importante. Usando um exemplo onde possui armazém de Apropriação Indireta (99) e em outro armazém ele ter sido requisitado para OP (01), é de extrema importância saber analisar os números impressos, como o exemplo abaixo:

Temos o Produto MP62 onde temos um saldo de 30 itens requisitados para uma OP e 5 no Armazém de Apropriação Indireta. Se emitirmos o relatório Saldo em Processo - MATR989 filtrando todos os armazéns, veremos que só é impresso o saldo requisitado para a OP:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15663680895511)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15663648181015)

Agora, emitindo o P7, vejamos que a seção "Em Processo" agrupa o saldo Requisitado para a OP (30) + Saldo do Armazém de Processo (5)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15663648184983)

- Desta forma, a recomendação é de que, caso tenha Armazém de Apropriação Indireta, **identificar via SB9/SB2 qual o saldo correto e filtrar o P7 só do mesmo armazém,** desta forma conseguirá identificar se a diferença é de fato no Saldo em Processo do P7 ou se está apenas imprimindo conforme os dados nas tabelas;

- Caso não utilize, recomendamos avaliar o produto no relatório MATR989 para melhor entendimento, nos armazéns, se existem saldos requisitados para OPs.

**Importante:** Avaliar o parâmetro **MV\_R460PRC**:

Este parâmetro é utilizado pelo relatório **Registro de Inventário P7** para indicar se, no momento do cálculo dos Saldos em Processo, o Sistema deve utilizar:

* O cálculo novo (1) = o Sistema considera os saldos em processo proporcionais, ou seja, quando feito um apontamento de produção parcial, a quantidade não apontada permanece sendo considerada como saldo em processo;
* O cálculo antigo (2) = o Sistema não considera mais os saldos em processo quando feito um apontamento de produção, mesmo que parcial.

Se de fato identificar uma divergência do saldo "Em Processo" impresso no MATR460 e não conseguir diagnosticar de onde ela possa estar surgindo, considere a possibilidade de atualizar o seu ambiente de Estoque/Custos com o pacote acumulado:

***Pacotes acumulados Estoque/Custos:***

[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=522000602)

OBS: Aplicar sempre primeiramente em ambiente de homologação.

**Saiba mais:**

[MP - SIGAEST - Parâmetros (SX6) relacionados ao relatório MATR460 - Registro de Inventário Modelo 7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Par%C3%A2metros-SX6-relacionados-ao-relat%C3%B3rio-MATR460-Registro-de-Invent%C3%A1rio-Modelo-7?source=search)

*[MP - SIGAEST - P7 - Montagem da seção "Saldo em Processo"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061473074)*

[*Clique aqui e veja mais artigos sobre o Relatório MATR460(P7) no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)
