---
article_id: 4410823845271
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 7f3f387422f6656b641ede0a06753b1fd20147b6594db8f97cf397847bc108ac
fetched_at: '2026-06-28T22:39:09.737459+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Qual o tamanho de
  imagem padrão para o Cadastro do Produto?
type: support-article
updated_at: '2025-05-16T13:46:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410823845271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Qual-o-tamanho-de-imagem-padr%C3%A3o-para-o-Cadastro-do-Produto
---

**Dúvida**Existe um tamanho de imagem em pixels mais adequado para visualização da foto no Cadastro de Produto?   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Neste artigo demostraremos as informações padrões de layout de imagem do produto.

**Tamanho padrão para imagens a serem inseridas no sistema são:**

* Tamanho: 1 MB
* Dimensões: 140 pixels de altura x 136 pixels de largura

**Tipos de imagens:**

* \*.jpeg
* \*.bmp

**O repositório de imagens pode ser utilizado das  seguintes  formas:**

* \*.BMI:  Arquivo onde fica armazenado o Índice do repositório.
* \*.BMR:  Arquivo onde fica armazenado o Memo do repositório.
* \*.BMD:  Arquivo propriamente dito (como se fosse um dbf).

**Observações**:

- Somente imagens com tamanho máximo de 1MB são suportadas;

- Quando o parâmetro MV\_REPOSIT é acionado, os arquivos SIGAADV permanecem intactos, não são alterados;

- Ao trocar o repositório de imagens dos arquivos locais para o banco de dados, as imagens permanecem no arquivo SIGAADV.BMD. Os arquivos somente são copiados para o banco de dados ao utilizar a rotina de Importação;

- As imagens são gravadas dentro da tabela PROTHEUS\_REPOSIT no Banco de Dados;

- No padrão, não é possível incluir uma Imagem sem que ela esteja previamente vinculada no repositório de imagens do Configurador.

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como incluo imagem no Cadastro de Produtos?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004815932-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-incluo-imagem-no-Cadastro-de-Produtos-)

*[Clique aqui e veja mais artigos sobre Cadastro e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
