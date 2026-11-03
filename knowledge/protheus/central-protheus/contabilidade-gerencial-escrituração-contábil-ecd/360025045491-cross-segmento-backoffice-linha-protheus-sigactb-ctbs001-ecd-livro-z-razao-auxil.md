---
article_id: 360025045491
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 98e7727d3b771c693138476177d52259fb96a846df766b3becf679c4ed811e76
fetched_at: '2026-06-28T22:40:44.834208+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - ECD  LIVRO
  Z - RAZAO AUXILIAR DAS SUBCONTAS (RAS)
type: support-article
updated_at: '2021-11-03T18:12:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025045491-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-LIVRO-Z-RAZAO-AUXILIAR-DAS-SUBCONTAS-RAS
---

**Dúvida**Como configurar o Razão Auxiliar das Subcontas (Livro Z RAS)?  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 11.80.  
  
  
**Solução**

As empresas obrigadas a transmitir o livro razão auxiliar das subcontas (deverá ser utilizado o livro “Z”) deverão utilizar os livros “R” (diário com escrituração resumida) ou “B” (balancetes diários e balanços) como principais, tendo em vista que o livro “G” (diário geral) não aceita livros auxiliares.

Se a geração do livro RAS for para manter somente a guarda do livro a escrituração principal poderá ser o livro G e o auxiliar como o Z, sem transmitir, permanecendo com a guardo do livro caso a Receita Federal solicite.

Deverá ser adotado o modelo padronizado de razão auxiliar das subcontas (as informações devem ser preenchidas nos registros I030 e I500 a I555), conforme abaixo.

Naturezas do livro a serem informadas no campo 4 do registro I030:

- RAZAO SUBCONTAS: RAZ\_AUX\_SUBCTA\_CTB.TXT

Para o Livro Z contendo o Razão Auxiliar de Subcontas como facilitador criamos um leiaute de importação de dados via configurador utilizando a ferramenta MILE para o cadastro de Layout Auxiliar acessado via menu SIGACTB em Atualizações / Escrituração Contábil / Cadastros / Layout Auxiliar.

Para importar o leiaute do MILE:

-gravar o arquivo RAZ\_AUX\_SUBCTA\_CFG\_MILE.XML do pacote da ECD no diretório /System

-acessar o configurador (SIGACFG)

-Em Aceleradores / MILE / Layouts pressionar Ações Relacionadas Layouts / Importar

-Selecionar o Arquivo RAZ\_AUX\_SUBCTA\_CFG\_MILE.XML

Também disponibilizamos 2 arquivos textos como exemplo preparados para ser importado via ferramenta MILE para o cadastro de Layout Auxiliar em Escrituração Contabil / Cadastros:

**[RAZAO\_AUXILIAR\_DAS\_SUBCONTAS](https://tdn.totvs.com/pages/releaseview.action?pageId=235331339)**

Observação: Verificar campos que estão fixos no txt com relação ao código do leiaute e caso já exista na base esse código de leiaute alterar o txt para um novo código.

O arquivo RAZ\_AUX\_SUBCTA\_CTB.TXT será utilizado para importação do leiaute relativo ao Razão Auxiliar de Subcontas a ser apresentado via Livro Z da ECD e o código deste será solicitado ao pressionar botão Importar Razão na tela principal da geração da revisão da ECD.

Maiores informações sobre a ferramenta MILE pode ser obtida no link:

<http://tdn.totvs.com.br/display/framework/MILE+-+Model+Integrator+Layout+Engine>

Manual ECD 2019:

<http://sped.rfb.gov.br/arquivo/show/2911>
