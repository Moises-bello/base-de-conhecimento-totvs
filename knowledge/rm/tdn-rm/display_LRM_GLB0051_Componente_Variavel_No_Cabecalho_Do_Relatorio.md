---
content_hash: 95b0e85bf34d0ec3a799c3200ce43d4140d66301cc80243507903d865a7ae5fd
fetched_at: '2026-06-29T00:08:10.744347+00:00'
page_id: '240979652'
product: rm
source: tdn-rm
title: GLB0051_Componente_Variavel_No_Cabecalho_Do_Relatorio
type: documentation
url: https://tdn.totvs.com/display/LRM/GLB0051_Componente_Variavel_No_Cabecalho_Do_Relatorio
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 12.1.12 |
| **Ocorrência:** | Diferença do componente Variável nas versões 11.8x e 12.1.xx. Solução utilizando variáveis do contexto nos parâmetros do relatório. |
| **Ambiente:** |  |
| **Passo a passo:** | Nas versões 11.8x, o componente variável utilizado no cabeçalho do relatório é resolvido antes da execução do relatório.  Ou seja, durante a execução do relatório, o Reports contem a informação deste campo para ser utilizado como parâmetro para consultas SQL, procedure e outros.  Exemplo:  O relatório contém um componente variável no cabeçalho do relatório (Desenho: USUARIO)    E como fonte de dados do detalhe uma consulta SQL que recebe como parâmetro o valor do componente variável (:USUARIO)    Nas versões 11.8x o relatório é gerado corretamente, retornando os dados da consulta SQL.    Na versão 12.1.xx, o componente variável é resolvido sobe demanda. Desta forma, o mesmo relatório será gerado em Branco    E no Diagnostico de Execução, será informado que não foi encontrado o valor para o parâmetro da consulta SQL (:USUARIO):     Como solução, foi implementado a partir da versão 12.1.11.106 as variáveis de contexto no parâmetro do relatório.     Criando um parâmetro do relatório com o valor da variável do contexto, o Reports identificará que se trata de uma variável do contexto (não será solicitado o seu preenchimento por parte do usuário que está gerando o relatório) e resolvera o seu valor antes da execução do relatório, sendo assim possível sua utilização nas consultas SQL e procedures.  Desta forma, o relatório é gerado normalmente      Mais informações sobre variáveis do contexto nos parâmetros do relatório no Link:  <http://tdn.totvs.com/x/KdJSDg> |
| **Observações:** |  |
