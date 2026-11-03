---
content_hash: b634fc7232ff1e1658c4059534e0940a83fc8a8a52d685d30f6d813ce84116c1
fetched_at: '2026-06-29T00:08:31.830645+00:00'
page_id: '273312413'
product: rm
source: tdn-rm
title: RMEDU00002_Relatório para impressão na Analise Curricular do Aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273312413
version: 3
---

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional |
| **Versões:** | 12.1.16 |
| **Observações:** | Impressão de Relatórios na Analise Curricular do Aluno |

Ao acessar a Analise Curricular do aluno o sistema disponibiliza a opção para impressão dos dados, para tal é necessário a utilização de um relatório.

A seguir demonstraremos os preceitos básicos para a criação do Relatório a ser utilizado.

1º Criação do Relatório

Criar um relatórios do Tipo 132 – Histórico Escolar

2º Vincular tabela master no Detalhe 1 do relatório

Inserir a tabela SHISTHABILITACAOALUNO no detalhe 1 do relatório como Master

3º Inserção dos campos necessários para fazer vinculo com os parâmetros do Provedor de Dados

Inserir os campos da tabela CODCOLIGADA, IDHABILITACAOFILIAL, RA (O RA DEVE SER INSERIDO DUAS VEZES) SHISTHABILITACAOALUNO, para fazer vínculo com os parâmetros obrigatórios do provedor de dados.

4º Criar um Subdetalhe

5º Inserir o Provider “Analise Curricular” no subdetalhe

7º Vincular os campos da tabela inseridos no Detalhe 1 com os parâmetros do provider.

A passagem dos campos para os parâmetros do provider devem ser realizada com bastante atenção pois são os mesmos que vão garantir que o provedor seja devidamente executado, observe que temos os parâmetros RA1 e RA2, por este motivo tivemos que inserir duas vezes o RA no detalhe 1 do relatório.

8º Após vincular os parâmetros arrastamos alguns campos do provider para o SubDetalhe do relatórios para garantir que o mesmo estivesse sendo executado.

9º Geração do Relatório pela Analise Curricular do Aluno

10º Relatório gerado com a execução correta do detalhe 1 e do SubDetalhe
