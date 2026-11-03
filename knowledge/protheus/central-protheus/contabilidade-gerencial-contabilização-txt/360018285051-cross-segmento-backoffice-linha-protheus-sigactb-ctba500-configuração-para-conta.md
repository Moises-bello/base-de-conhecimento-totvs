---
article_id: 360018285051
category: Contabilidade Gerencial - Contabilização txt
content_hash: 1c0acff3d4d3bc92e7852e16fc5d67f32d609967b067b53685f98e68b9f8767f
fetched_at: '2026-06-28T22:40:55.411546+00:00'
product: protheus
section_id: 1500001537521
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA500 Configuração
  para contabilização TXT
type: support-article
updated_at: '2022-08-11T17:32:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018285051-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA500-Configura%C3%A7%C3%A3o-para-contabiliza%C3%A7%C3%A3o-TXT
---

**Dúvida**CTBA500 Configuração para contabilização TXT  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

A contabilização TXT parte de um lançamento contábil, portanto a numeração dos lançamentos padronizados utilizados nesta rotina devem estar entre **001** e **499**. Os números acima de **499** são referentes aos lançamentos automáticos de outros módulos e, portanto, não são utilizados.  
  
O arquivo TXT deve ter o tamanho do registro configurado nos parâmetros da rotina, sendo que não é necessário haver posições fixas na linha de detalhe. A única exceção se refere ao código do Lançamento Padrão associado que deve estar obrigatoriamente gravado nas 3 primeiras posições de cada linha.  
  
Para acessar uma determinada informação, é necessário utilizar nos lançamentos padronizados as funções **LerStr** e**LerVal** que são responsáveis pela leitura no arquivo TXT, retornando dados de tipo caracter e numérico, respectivamente.  
  
Sintaxe:

LerStr( ExpN1, ExpN2 ) -> Lê uma expressão do arquivo texto e grava no arquivo de contabilização como uma expressão do tipo caracter.  
LerVal( ExpN1, ExpN2 ) -> Lê uma expressão do arquivo texto e grava no arquivo de contabilização como uma expressão do tipo numérico.  
LerData( ExpN1, ExpN2 ) -> Lê uma expressão do arquivo texto e permite alterar a data do lançamento contábil. Esta função poderá ser colocada em qualquer campo do LP, pois sua função é somente alterar a Data do Lançamento Contábil, a partir de uma data gravada no arquivo texto.  
  
O parâmetro ExpN1 se refere a posição inicial do campo dentro do registro e o ExpN2, ao tamanho do campo.  
  
Configurando  
·    Crie o seguinte LP no cadastro Lançamentos Padronizados:

|  |  |
| --- | --- |
| **Campo** | **Conteúdo** |
| Cod Lanc Pad | 001 |
| Sequencial | 001 |
| Descrição | Lançamento TXT |
| Tipo Lcto | Partida Dobrada |
| Cta Débito | LERSTR(10,20) |
| Cta Crédito | LERSTR(50,20) |
| Vlr Moeda 1 | LERVAL(80,17) |
| Histórico | LERSTR(100,40) |
| Origem Lcto | LERDATA(140,10) |

·    Configure o arquivo Texto para que:  
·    O Código do LP 001 esteja nas primeiras 3 posições de cada linha do arquivo.  
·    As Contas Débito iniciem na coluna 10 de cada linha.  
·    As Contas Crédito iniciem na coluna 50 de cada linha.  
·    O Valor do lançamento inicie na coluna 80.  
·    O Histórico do Lançamento inicie na coluna 100.  
·    Neste caso, a Data do Lançamento Contábil é manipulada pela função LERDATA, que lê uma data válida iniciando na coluna 140. Observe que o campo **Origem Lcto** não tem ligação alguma com este comando.

* Instruções para montagem do TXT

<https://tdn.totvs.com/pages/releaseview.action?pageId=6068476>

**Saiba mais**

[CTBA500 Estrutura de arquivo txt](http://tdn.totvs.com/pages/releaseview.action?pageId=135496233)

[CTBA500 Sintaxe](http://tdn.totvs.com/pages/releaseview.action?pageId=6068432)
