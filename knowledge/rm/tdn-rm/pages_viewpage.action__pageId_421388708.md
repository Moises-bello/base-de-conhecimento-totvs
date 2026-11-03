---
content_hash: b0f75cf8cfdad0db094e295bfbc7b4c00f849eff4cde44490b997d341058df96
fetched_at: '2026-06-29T00:09:18.492112+00:00'
page_id: '421388708'
product: rm
source: tdn-rm
title: FIN - Retorno de Custódia de Cheques
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388708
version: 5
---

A importação do retorno de Custódia de Cheques consiste em atualizar dados do Extrato de Caixa por meio de importação de arquivos disponibilizados pela rede Bancária. Neste processo, o registro do extrato correspondente ao cheque custodiado será atualizado para “Custodiado”, “Recusado”, “Compensado” ou outros em função do propósito do arquivo, ou seja, de acordo com o Código de Movimento do retorno ou Código de Ocorrência presente no arquivo de retorno.

**Tipo do Arquivo de Retorno**

Retorno de Custódia

Esta opção deverá ser utilizada na importação de retorno de Custódia de arquivos fornecidos por todos os Bancos que adotarem o padrão CNAB240 com adequações próprias e aos demais formatos de arquivos de retorno de Custódia de tamanhos diversificados.

Retorno de Custódia CNAB240

Essa opção deverá ser utilizada na importação de retorno de Custódia de arquivos fornecidos por qualquer banco que adotar o “Padrão Febraban CNAB240” sem adequações próprias e demais formatos de arquivos de retorno de Custódia de tamanhos diversificados.

**Observação**

Se no arquivo de retorno disponibilizado por outros bancos existir alguma informação em posições diferente, exemplo, valor na posição 70 a 84, será preciso optar pelo tipo de retorno "Retorno de Custódia" e não por "Retorno de Custódia CNAB240", mesmo que o arquivo de retorno tenha 240 colunas.

**Importação do arquivo**

É necessário indicar o local onde encontra-se o arquivo de retorno a ser importado e o banco que gerou o arquivo. A importação será através do menu Movimentações Bancárias | Integração Bancária | Retorno Bancário | Retorno | Custódia de Cheques. Selecione tipo do arquivo, o arquivo e o banco de custódia.
