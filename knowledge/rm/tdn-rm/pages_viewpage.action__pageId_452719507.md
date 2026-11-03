---
content_hash: 20ac52f205801e7684b8cb505b5d3ce29e632d38d1b49aa5b5fe9e4361180860
fetched_at: '2026-06-29T00:10:08.082690+00:00'
page_id: '452719507'
product: rm
source: tdn-rm
title: Funções de Relógio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719507
version: 3
---

**Funções de Relógio**

**Código -** Informe um código alfanumérico (números e/ou letras) com até quatro dígitos. O sistema não aceita dois códigos idênticos.

**Descrição -** Forneça a descrição da função gerada pelo relógio.

**Tratamentos -** Forneça o tratamento que o Sistema dará para a função selecionando um dos tipos a seguir:

- Sem funcionalidade: Para desativar uma função cadastrada, utilize o tratamento "Sem funcionalidade", neste campo, clicando na barra de rolagem.

- Considera Batida Entrada: Todas as batidas importadas com esta função serão importadas com a Natureza de Entrada.

- Considera Batida Saída: Todas as batidas importadas com esta função serão importadas com a Natureza de Saída.

- Considera Entrada Abonada: Esta função deve ser utilizada pelos funcionários que chegarem atrasados, para que este atraso seja abonado automaticamente basta utilizar esta função e cadastrar um abono relacionado no campo abaixo.

- Considera Saída Abonada: Esta função deve ser utilizada pelos funcionários que saírem mais cedo, para que este atraso seja abonado automaticamente basta utilizar esta função e cadastrar um abono relacionado no campo abaixo.

- Desconsidera a batida: Com esta função o sistema não importará a batida, pois ela será desconsiderada.

- Batida Como Normal ou Refeição: Esta função deve ser considerada para o sistema importar a batida para a pasta de batidas do funcionário e também será considerada como uma batida desconto de refeição que será importada para pasta de Refeição dentro do cadastro do funcionário. - Desconsidera Batida Refeição: Utilizando esta função o sistema não irá importar a batida de refeição do funcionário.

- Desconsidera Batida Refeição e Normal: Utilizando esta função o sistema não irá importar a batida de refeição e normal do funcionário.

- Considera Apenas Como Refeição: Utilizando esta função o sistema importará apenas como batida de refeição.

-Gera Somente Just.de Ausência: Utilizando esta função o sistema irá gerar uma ocorrência de justificativa de ausência para o funcionário ao realizar a importação de batidas.

**Abono -** Informe o abono a ser considerado

**Atenção:**

Este campo só será habilitado caso os campos considera entrada abonada e considera saída abonada tenham sido selecionados.

**Exemplo:**

Suponha que o layout do relógio de ponto da empresa esteja cadastrado da seguinte forma:

|  |  |  |
| --- | --- | --- |
| Layout do arquivo | Posição | Tamanho |
| Chapa | 1 | 8 |
| Nº Relógio | 24 | 2 |
| Hora | 10 | 5 |
| Dia | 19 | 2 |
| Mês | 21 | 2 |
| Código da Função | 16 | 2 |

Suponha também, que existam duas funções cadastradas:

|  |  |  |  |
| --- | --- | --- | --- |
| Referência | Código | Descrição | Tratamento |
| 1 | F1 | Entrada | Considera a batida como Entrada |
| 2 | F2 | Saída | Considera a batida como Saída |

Além disso, o arquivo gerado pelo relógio de ponto contenha as seguintes linhas:  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 2 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 3  
Coluna-texto: 1234567890 1234567890 1234567890

|  |  |  |  |
| --- | --- | --- | --- |
| 00000245 | 07:47 | F1 | 0402 |
| 00001388 | 07:49 | F1 | 0402 |
| 00000122 | 08:12 | F1 | 0402 |

Colunas:  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 2 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 3  
Coluna-texto: 1234567890 1234567890 1234567890

|  |  |  |  |
| --- | --- | --- | --- |
| 00001388 | 11:55 | F2 | 0402 |
| 00000245 | 12:12 | F2 | 0402 |
| 00000122 | 14:05 | F1 | 0402 |
| 00000245 | 14:07 | F1 | 0402 |
| 00000245 | 17:48 | F2 | 0402 |
| 00001388 | 17:50 | F2 | 0402 |
| 00000122 | 18:01 | F4 | 0402 |

O Sistema irá verificar se existem funções cadastradas no Sistema e, caso haja, irá tratar cada batida importada de acordo com sua função correspondente.  
Supondo que a função de "Saída abonada" tenha sido cadastrada como código F1 e "Entrada abonada" como F2:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Horário | Ent1 | Sai1 | Ent2 | Sai2 |
| 01/03 | 08:00 | 12:00 | 14:00 | 18:00 |
| 02/03 | 08:00 | 12:00 | 14:00 | 18:00 |
| 03/03 | 08:00 | 12:00 | 14:00 | 18:00 |

Batida  
02/03 08:00 12:00 14:00 15:00 17:00 18:00

|  |  |
| --- | --- |
| 00001 | 020308:00 |
| 00001 | 020312:00 |
| 00001 | 020314:00 |
| 00001 | 020315:00F1 |
| 00001 | 020317:00F2 |
| 00001 | 020318:00 |

A pasta de abonos irá trazer, automaticamente, o abono de 15:00 as 17:00h.  
Batida  
02/03 09:00 12:00 14:00 18:00

|  |  |
| --- | --- |
| 00001 | 020309:00F2 |
| 00001 | 020312:00 |
| 00001 | 020314:00 |
| 00001 | 020318:00 |

A pasta de abonos irá trazer, automaticamente, o abono de 08:00h as 09:00h.  
**Observação:** Para o controle correto da função de horas abonadas, a importação das batidas do período deverá ser efetuada de uma só vez, em um único arquivo.  
   
HelpWiki - RH - Automação de Ponto
