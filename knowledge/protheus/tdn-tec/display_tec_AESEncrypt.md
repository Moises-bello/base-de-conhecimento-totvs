---
content_hash: 091eb9d367156933dcadec23f77977b23b6413d9a2aa229b348e13a82fee3692
fetched_at: '2026-07-02T19:24:25.949336+00:00'
page_id: '515287381'
product: protheus
source: tdn-tec
title: AESEncrypt
type: documentation
url: https://tdn.totvs.com/display/tec/AESEncrypt
version: 16
---

AESEncrypt

Encripta textos usando o algoritmo AES no modo definido.

## Sintaxe

false, < cPlainText >, [ cPassword ], [ cKey ], [ cIV ] )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nCipherID | numérico | Código identificador do modo do algoritmo AES a ser usado na encriptação. | X |  |
| cPlainText | caractere | Texto de entrada a ser encriptado. | X |  |
| cPassword | caractere | Texto auxiliar na geração da key da encriptação. |  |  |
| cKey | caractere | Key da encriptação, conforme o modo do algoritmo AES a ser usado. |  |  |
| cIV | caractere | IV (Vetor de Inicialização) da encriptação, conforme o modo do algoritmo AES a ser usado. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| aResEnc | vetor | Array com o resultado do processo de encriptação. |

trueObservações

* **Modos do algoritmo AES suportados**: a partir dos modos do algoritmo AES suportados, são definidos os códigos identificadores, os tamanho da Key e do IV e a obrigatoriedade do uso do IV:

  | Modo do algoritmo AES | Código Identificador | Tamanho da Key (em bytes) | Tamanho do IV (em bytes) | IV Usado |
  | --- | --- | --- | --- | --- |
  | AES-128 CBC | 0 | 16 | 16 | Sim |
  | AES-192 CBC | 1 | 24 | 16 | Sim |
  | AES-256 CBC | 2 | 32 | 16 | Sim |

* **Regra para uso ou geração da Key**: a key fornecida somente será usada se o password não for fornecido, segundo a seguinte lógica:

  | Password Fornecido | Key Fornecida | Resultado |
  | --- | --- | --- |
  | Sim | Sim | Ignora a Key fornecida, gera a Key usando o password fornecido e a usa. |
  | Sim | Não | Gera a Key usando o password fornecido e a usa. |
  | Não | Sim | Usa a Key fornecida. |
  | Não | Não | Gera a Key e a usa. |

* **Sobre o uso de keys fornecidas**: caso sejam utilizadas keys fornecidas, por razões de segurança da informação, recomenda-se:
  + somente usar keys derivadas a partir de algoritmos apropriados e com componente randômico;
  + não repetir a mesma key para diferentes textos de entrada.

* **Regra para uso ou geração do IV**: para o **modo CBC**:

  | IV Fornecido | Resultado |
  | --- | --- |
  | Sim | Usa o IV fornecido. |
  | Não | Gera o IV e o usa. |

* **Sobre o uso de ivs fornecidos**: para o **modo CBC**, caso sejam utilizados ivs fornecidos, por razões de segurança da informação, recomenda-se:
  + somente usar ivs gerados randomicamente.

* **Formato e conteúdo da array com o resultado da encriptação**:

  | Índice | Nome | Tipo | Descrição | Conteúdo |
  | --- | --- | --- | --- | --- |
  | 1 | nResultCode | numérico | Código identificador do resultado da encriptação. | 0 (zero) em caso de sucesso ou diferente de 0 (zero) em caso de erro. |
  | 2 | cCipherText | caractere | Texto de saída resultado da encriptação. | Texto da entrada encriptado no modo definido em caso de sucesso ou vazio em caso de erro. |
  | 3 | cKeyUsed | caractere | Key usada na encriptação. | Key usada na encriptação em caso de sucesso ou vazio em caso de erro. |
  | 4 | cIVUsed | caractere | IV usado na encriptação. | IV usado na encriptação em caso de sucesso ou vazio em caso de erro. |

* **Códigos identificadores do resultado da encriptação**:

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

* [AESDecrypt](http://tdn.totvs.com.br/display/tec/AESDecrypt)
