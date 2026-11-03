---
content_hash: 970ba179710e7a38b7529ce295eab7ea35f96b82f4e18d0e0ec82ab80afe50c6
fetched_at: '2026-06-29T00:09:17.419837+00:00'
page_id: '421388586'
product: rm
source: tdn-rm
title: Layout Retorno de Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388586
version: 8
---

Para realizar o processo de importação do arquivo de retorno de cobrança enviado pelo banco, é necessário que o layout do banco esteja cadastrado.   
No menu *Movimentações Bancárias | Bancos e Agências*, selecione o banco cadastrado e em *Anexo | Layout Bancário* preencha os campos conforme manual do banco ou em *Processos | Importar Layout*. Através das informações do layout, o sistema busca do arquivo bancário os dados para a realizar o processo do retorno de cobrança.

**Nosso Número - Tamanho**

Informe o tamanho do nosso número, ou seja, a quantidade de dígitos que o nosso número terá no código de barras. Os dados desse campo serão utilizados para a geração do nosso número no boleto conforme cada banco. 

**Código de Retorno**

Baixa / Registrado / Recusado / Cancelado

Informe nos campos referente a ação (Baixa / Registrado / Recusado / Cancelado) os códigos válidos do banco. Esses códigos estão disponíveis no manual do banco e pode ser inserido até 20 códigos diferentes em cada um dos campos.

Na importação do arquivo bancário, o sistema lê o código armazenado na posição específica e compara com as informações cadastradas nesse campo e executa o processo alterando o status do boleto para Baixado, Registrado, Recusado ou Cancelado. Abaixo, citamos alguns campos que precisam de preenchimento para que o sistema possa realizar a leitura do arquivo bancário.

Subaba "**Detalhe**"

Nosso Número

Informe a posição inicial e final onde é informado o Nosso Número do boleto, será buscado da linha do arquivo.

Chave do Lançamento

Informe a posição inicial e final onde é informado a Ref. do lançamento, será buscado da linha do arquivo.

Chave do Lançamento 2

Informe a posição inicial e final onde é informado a Ref. do lançamento, será buscado da linha do arquivo.

Valor original

Informe a posição inicial e final onde é informado o valor original do lançamento, será buscado da linha do arquivo.

Valor baixa

Informe a posição inicial e final onde é informado o valor a ser baixado do lançamento, será buscado da linha do arquivo.

Juros

Informe a posição inicial e final onde é informado o valor de juros do lançamento, será buscado da linha do arquivo.

Multa

Informe a posição inicial e final onde é informado o valor de multa do lançamento, será buscado da linha do arquivo.

Desconto

Informe a posição inicial e final onde é informado o valor de desconto do lançamento, será buscado da linha do arquivo.

Código Retorno

Informe a posição inicial e final onde é informado o código de retorno que o banco enviará, podendo ser baixa, registrado, recusado ou cancelado, será buscado da linha do arquivo.

Subaba "**Header**"

Código do Banco

Informe a posição inicial que se encontra o código do Banco no header do arquivo, será buscado da linha do arquivo.

Subaba "**Partilha**" (disponível apenas para o Padrão 400 posições do Banco Santander - Febraban 033)  
  
Código Receptor 1

Informe a posição inicial e final onde é informado o código do Receptor 1, será buscado da linha do arquivo.

Valor Partilha 1

Informe a posição inicial e final onde é informado o valor partilhado do Receptor 1, será buscado da linha do arquivo.

Código Receptor 2

Informe a posição inicial e final onde é informado o código do Receptor 2, será buscado da linha do arquivo.

Valor Partilha 2

Informe a posição inicial e final onde é informado o valor partilhado do Receptor 2, será buscado da linha do arquivo.

Código Receptor 3

Informe a posição inicial e final onde é informado o código do Receptor 3, será buscado da linha do arquivo.

Valor Partilha 3

Informe a posição inicial e final onde é informado o valor partilhado do Receptor 3, será buscado da linha do arquivo.

Código Receptor 4

Informe a posição inicial e final onde é informado o código do Receptor 4, será buscado da linha do arquivo.

Valor Partilha 4

Informe a posição inicial e final onde é informado o valor partilhado do Receptor 4, será buscado da linha do arquivo.
