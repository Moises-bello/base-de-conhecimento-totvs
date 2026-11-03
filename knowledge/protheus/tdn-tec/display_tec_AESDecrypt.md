---
content_hash: 9f078527f011d8c156fc5de86ef7dccac067837b1aaf0fe8b08fc3c8e72c799d
fetched_at: '2026-07-02T19:24:25.961922+00:00'
page_id: '515290099'
product: protheus
source: tdn-tec
title: AESDecrypt
type: documentation
url: https://tdn.totvs.com/display/tec/AESDecrypt
version: 6
---

AESDecrypt

Decripta textos usando o algoritmo AES no modo definido.

## Sintaxe

false, < cCipherText >, < cKey >, [ cIV ] )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nCipherID | numérico | Código identificador do modo do algoritmo AES a ser usado na decriptação. | X |  |
| cCipherText | caractere | Texto de entrada a ser decriptado. | X |  |
| cKey | caractere | Key da decriptação, conforme o modo do algoritmo AES a ser usado. | X |  |
| cIV | caractere | IV (Vetor de Inicialização) da decriptação, conforme o modo do algoritmo AES a ser usado. **Obrigatório para o modo CBC.** |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| aResDec | vetor | Array com o resultado do processo de decriptação. |

trueObservações

* **Modos do algoritmo AES suportados**: a partir dos modos do algoritmo AES suportados, são definidos os códigos identificadores, os tamanho da Key e do IV e a obrigatoriedade do uso do IV:

  | Modo do algoritmo AES | Código Identificador | Tamanho da Key (em bytes) | Tamanho do IV (em bytes) | IV Usado |
  | --- | --- | --- | --- | --- |
  | AES-128 CBC | 0 | 16 | 16 | Sim |
  | AES-192 CBC | 1 | 24 | 16 | Sim |
  | AES-256 CBC | 2 | 32 | 16 | Sim |

* **Sobre o uso de keys fornecidas**: ao utilizar keys fornecidas, por razões de segurança da informação, recomenda-se:
  + somente usar keys derivadas a partir de algoritmos apropriados e com componente randômico;
  + não repetir a mesma key para diferentes textos de entrada.

* **Sobre o uso de ivs fornecidos**: para o **modo CBC**, ao utilizar ivs fornecidos, por razões de segurança da informação, recomenda-se:
  + uso obrigatório de ivs para o **modo CBC**.
  + somente usar ivs gerados randomicamente.

* **Formato e conteúdo da array com o resultado da decriptação**:

  | Índice | Nome | Tipo | Descrição | Conteúdo |
  | --- | --- | --- | --- | --- |
  | 1 | nResultCode | numérico | Código identificador do resultado da decriptação. | 0 (zero) em caso de sucesso ou diferente de 0 (zero) em caso de erro. |
  | 2 | cPlainText | caractere | Texto de saída resultado da decriptação. | Texto da entrada decriptado no modo definido em caso de sucesso ou vazio em caso de erro. |

* **Códigos identificadores do resultado da decriptação**:

  | Código | Significado |
  | --- | --- |
  | 0 | Sucesso. |
  | 1 | Erro de código identificador do modo do algoritmo de criptografia inválido. |
  | 2 | Erro de comprimento da key fornecida é inválido para o modo definido. |
  | 3 | Erro de comprimento do iv fornecido é inválido para o modo definido. |
  | 4 | Erro de geração da key: erro gerando o salt. |
  | 5 | Erro de geração da key: erro derivando a key. |
  | 6 | Erro de geração do iv: erro gerando o iv. |
  | 7 | Erro de texto encriptado vazio. |
  | 8 | Erro de encriptação: o conteúdo de um ou mais dos parâmetros de entrada não corresponde ao esperado. |
  | 9 | Erro de decriptação: o conteúdo de um ou mais dos parâmetros de entrada não corresponde ao esperado. |
  | 10 | Erro de código de erro desconhecido. |

## Exemplos

* Exemplo 1: criptografia AES-128 CBC usando key gerada a partir do password fornecido e IV gerado randômico:

  cppEclipsetruefalse"
  Local cPassword := ""
  Local cKeyUsed := ""
  Local cIVUsed := ""
  Local cCipherText := ""
  Local aResEnc := {}
  Local aResDec := {}
  aResEnc := AESEncrypt( nCipherID, cPlainText, cPassword )
  VarInfo( "AESEncrypt", aResEnc )
  // AESEncrypt -> ARRAY ( 4) [...]
  // AESEncrypt[1] -> N ( 15) [ 0.0000]
  // AESEncrypt[2] -> C ( 32) []
  // AESEncrypt[3] -> C ( 16) []
  // AESEncrypt[4] -> C ( 16) []
  cCipherText := aResEnc[2]
  cKeyUsed := aResEnc[3]
  cIVUsed := aResEnc[4]
  aResDec := AESDecrypt( nCipherID, cCipherText, cKeyUsed, cIVUsed )
  VarInfo( "AESDecrypt", aResDec )
  // AESDecrypt -> ARRAY ( 2) [...]
  // AESDecrypt[1] -> N ( 15) [ 0.0000]
  // AESDecrypt[2] -> C ( 16) []
  Return
  ]]>
* Exemplo 2: criptografia AES-128 CBC usando key fornecida e IV fornecido:

  cppEclipsetruefalse"
  Local cKeyInput := ""
  Local cIVInput := ""
  Local cKeyUsed := ""
  Local cIVUsed := ""
  Local cCipherText := ""
  Local aResEnc := {}
  Local aResDec := {}
  aResEnc := AESEncrypt( nCipherID, cPlainText, , cKeyInput, cIVInput )
  VarInfo( "AESEncrypt", aResEnc )
  // AESEncrypt -> ARRAY ( 4) [...]
  // AESEncrypt[1] -> N ( 15) [ 0.0000]
  // AESEncrypt[2] -> C ( 32) []
  // AESEncrypt[3] -> C ( 16) []
  // AESEncrypt[4] -> C ( 16) []
  cCipherText := aResEnc[2]
  cKeyUsed := aResEnc[3]
  cIVUsed := aResEnc[4]
  aResDec := AESDecrypt( nCipherID, cCipherText, cKeyUsed, cIVUsed )
  VarInfo( "AESDecrypt", aResDec )
  // AESDecrypt -> ARRAY ( 2) [...]
  // AESDecrypt[1] -> N ( 15) [ 0.0000]
  // AESDecrypt[2] -> C ( 16) []
  Return
  ]]>

## Abrangência

Disponível no AppServer a partir da build 17.3.0.15

## Veja também

* [AESEncrypt](http://tdn.totvs.com.br/display/tec/AESEncrypt)
