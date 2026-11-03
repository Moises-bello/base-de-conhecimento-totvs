---
article_id: 25695132849175
category: LEGAIS - BLOCO H/MATR460
content_hash: 0708e6667dad0b222d296655c48150e248477365f16266c6f118046a8209c0f3
fetched_at: '2026-06-28T22:42:15.151536+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Por que
  o Livro de Inventário P7 não pode ser impresso em formato de tabela?
type: support-article
updated_at: '2025-03-12T12:27:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25695132849175-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Por-que-o-Livro-de-Invent%C3%A1rio-P7-n%C3%A3o-pode-ser-impresso-em-formato-de-tabela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25695163382295) Tempo aproximado para leitura: **00:01:10 min** **Dúvida**Por que o Livro de Inventário P7 não pode ser impresso em formato de tabela?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**O Livro de Inventário modelo P7 é o antigo "livro físico de Inventario modelo 7", onde muitas empresas passaram (e ainda passam) por auditorias onde, por meio do Livro de Inventário, a empresa justifica para o auditor o seu inventário de Estoque, contendo: Produto, Situação (Estoque Proprio, de terceiros em meu poder, meu em poder de terceiros), Unidade, Valores Unitário e Total.

Esse livro contem um Leiaute que comporte todos esses dados em uma estrutura específica onde cada valor é escrito (impresso hoje em dia). Para atender este leiaute, a TOTVS estabeleceu que as formas de impressão, de forma a manter o leiaute padrão legislativo, é:

- Impresso em tela;

- Em formato PDF;

- Em formato ODF;

- Em formato HTML;

- Planilha Excel (Normal ou Suprimindo linhas brancas e totais)

**Exemplo de como o P7 fica em formato Planilha - Normal (todo conteudo fica em uma única célula):**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25695132840471)

**Exemplo de como o P7 fica em formato Planilha -  Suprime Linhas Brancas e Totais (também com todo conteúdo ficando em uma única célula):**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25695163386135)**

Portanto, de fato este comportamento não se trata de uma limitação da rotina em si, mas sim um comportamento que atende a um padrão legislativo, onde clientes que tentam imprimir em formato de tabela ou formato de tabela XLSX são retornados com a seguinte mensagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25695163387543)

Então, para o padrão ser mantido, o relatório não pode ser impresso em formato de tabelas porque mudaria o leiaute do qual ele foi estabelecido em sua concepção legal/fiscal.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460)*
