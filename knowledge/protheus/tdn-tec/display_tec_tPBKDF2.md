---
content_hash: 57373b096814220f9920313def2ce3b2b1a87da6f8b2c41b9d2b3e21b1dde9ed
fetched_at: '2026-07-02T19:24:28.658413+00:00'
page_id: '804058043'
product: protheus
source: tdn-tec
title: tPBKDF2
type: documentation
url: https://tdn.totvs.com/display/tec/tPBKDF2
version: 15
---

# Classe tPBKDF2

PBKDF2 (Password-Based Key Derivation Function 2) é um algoritmo de derivação de chave amplamente utilizado que é projetado para aumentar a segurança de senhas e chaves mestras.

Ele é amplamente adotado em cenários de segurança, incluindo o armazenamento seguro de senhas e a geração de chaves criptográficas.

Este padrão é útil em contextos onde é necessário garantir a integridade e a confidencialidade das informações, como em transações financeiras ou dados sensíveis.  
Para maiores informações, recomenda-se a leitura da RFC2898: <https://datatracker.ietf.org/doc/html/rfc2898#section-5.2>

##### Observações

##### Exemplo

User Function testpbkdf2()

  Local oTokenPBKDF2 := Nil

  //Criando classe do PBKDF2  
  oTokenPBKDF2:= tPBKDF2():New()  
    
  //Informação da release utilizada da openssl  
  conout("release: " + oTokenPBKDF2:release() )  
    
  //Parâmetro obrigatório, senha para iniciar a criptografia.   
  oTokenPBKDF2:setPassword("password")  
    
  //Parâmetro obrigatório, salt podendo ser string ou base64  
  oTokenPBKDF2:setSalt("salt")  
    
  //Número de iteração, quantidade de rodadas de criptografia! RFC 2898 sugere no mínimo 1000. Quanto maior mais difícil será desfazer via força bruta.  
  oTokenPBKDF2:setIteration(10000)  
    
  //Tamanho do buffer da chave de saída em **bytes**.  
  //8  bytes ou 64  bits  
  //16 bytes ou 128 bits  
  //32 bytes ou 256 bits  
  //64 bytes ou 512 bits  
  oTokenPBKDF2:setKeylength(16)  
    
  //Função de digest usado na criptografia. Ex: SHA1, SHA256, SHA512  
  oTokenPBKDF2:setDigest("SHA256")  
    
  //Função obrigatório usada para chamar a criptografia  
  oTokenPBKDF2:encrypt()   
    
  //Funções de retorno  
  //Neste caso saída com 32 caracteres (hexdecimal) 2 caracteres por byte.   
  conout("Retorno em formato Hexadecimal : " + cValToChar( oTokenPBKDF2:getKeyHex() ))  
  conout("Retorno em formato Raw : " + cValToChar( oTokenPBKDF2:getKeyRaw() ))    
  conout("Retorno em formato BASE64 : " + cValToChar( oTokenPBKDF2:getKeyBase64() ))    
  conout("Retorno em formato BASE64 Url Safe: " + cValToChar( oTokenPBKDF2:getKeyUrl\_Base64() ))    
    
  //Importante sempre destruir a classe para evitar aumento de memoria no Appserver.  
  FreeObj(oTokenPBKDF2)

Return

```

```

##### Abrangência

20.3.2.3

---

### Construtores

#### New

Cria um objeto tPBKDF2 para configuração, criação, assinatura e manipulação de assinaturas.

##### Sintaxe

```
tPBKDF2():New()
```

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| oObj | object | Nova instância da classe tPBKDF2 |

##### Exemplos

```
    Local oTokenPBKDF2 := tPBKDF2():New()
```

---

### Métodos

A classe expõe os seguintes métodos:

#### setPassword

Ajusta a senha que será utilizado na criptografia.

##### Sintaxe

```
setPassword( < cAlgo > )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cAlgo | character | Password usado na criptografia | X |  |

##### Exemplos

```
     oTokenPBKDF2:setPassword("password")
```

---

#### setSalt

Ajusta o Salt ou palavra de derivação utilizada na criptografia.

##### Sintaxe

```
setSalt( < cAlgo > )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cAlgo | character | salt usado na criptografia | X |  |

##### Exemplos

```
    oTokenPBKDF2:setSalt("salt")
```

---

#### setIteration

Ajusta o número de iterações utilizadas na criptografia, quanto maior o valor mais recurso será utilizado do processador e irá demorar mais para ser processado.  
O número mínimo é de 1 e o valor recomendado é 1000.

##### Sintaxe

```
setIteration( < citeration > )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| `citeration` | numérico | Número de iterações, rodadas de criptografia, a RFC 2898 sugere o uso de no mínimo 1000, default é 1000. |  |  |

##### Exemplos

```
    oTokenPBKDF2:setIteration(10000)
```

---

#### setKeylength

Ajusta o tamanho do buffer de saída em bytes, mínimo é de 8 bytes e máximo de 64 bytes.

##### Sintaxe

```
setKeylength( < ckeylength > )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| `ckeylength` | numérico | Tamanho da chave de saída, em bytes.  8  bytes ou 64  bits 16 bytes ou 128 bits 32 bytes ou 256 bits 64 bytes (Valor Máximo) ou 512 bits | X |  |

##### Exemplos

```
    oTokenPBKDF2:setKeylength(16)
```

---

#### setDigest

Ajusta a função de digestão utilizado na criptografia.

##### Sintaxe

```
setDigest( < cdigest > )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| `cdigest` | character | Função de digestão usada na criptografia. Padrão: SHA256 SHA1, SHA224, SHA256, SHA384, SHA512, SHA512\_224, SHA512\_256, SHA3\_224, SHA3\_256, SHA3\_384, SHA3\_512. |  |  |

##### Exemplos

```
    oTokenPBKDF2:setDigest("SHA256")
```

---

#### encrypt

Função deve ser chamada obrigatoriamente após os ajustes acima.

##### Sintaxe

```
encrypt()
```

##### Exemplos

```
    oTokenPBKDF2:encrypt() 
```

---

#### Funções de retorno.

#### getKeyHex

Função de retorno da criptografia em Hexadecimal, 2 caracteres por byte em maiúsculo os bytes são definidos no setKeyLength.

##### Sintaxe

```
getKeyHex()
```

##### Exemplos

```
    oTokenPBKDF2:getKeyHex()
```

---

#### getKeyRaw

Função de retorno da criptografia em formato RAW.

##### Sintaxe

```
getKeyRaw()
```

##### Exemplos

```
    oTokenPBKDF2:getKeyRaw()
```

---

#### getKeyBase64

Função de retorno da criptografia em formato Base64 (RFC1521).

##### Sintaxe

```
getKeyBase64()
```

##### Exemplos

```
    oTokenPBKDF2:getKeyBase64()
```

---

#### getKeyUrl\_Base64

Função de retorno da criptografia em formato Base64 URL Applications (RFC4648).

##### Sintaxe

```
getKeyUrl_Base64()
```

##### Exemplos

```
    oTokenPBKDF2:getKeyUrl_Base64()
```

---

#### release

Obtém a versão da lib da openssl utilizada.

##### Sintaxe  oTokenPBKDF2:release()

```
release()
```

##### Exemplos

```
    conout("Versão da openssl: " + oTokenPBKDF2:release())
```

---

#### getLastError

Obtém o registro de erro da última operação executada sem sucesso.

##### Sintaxe  oTokenPBKDF2:`getLastError`()

```
getLastError()
```

##### Exemplos

`conout("Erro na geração da criptografia. Error: " + oTokenPBKDF2:getLastError())  
  
Saída de erros, todos serão impresso no console.log.`

| Causa | Erros |
| --- | --- |
| setPassword não informado. | `PBKDF2 The password is not provided.` |
| setSalt não informado. | `PBKDF2 The salt is missing.` |
| setSalt contém mais de 64 caracteres. | `PBKDF2 The salt size is greater than 64, too large.` |
| setIteration informado menor que 1. | `PBKDF2 The minimum number of iterations is 1.` |
| setKeylength informado menor que 8. | `PBKDF2 The minimum key size is 8 bytes or 64 bits.` |
| setKeylength informado maior que 8. | `PBKDF2 The maximum key size is 64 bytes or 512 bits.` |
| setDigest invalido, consulte a lista da documentação. | `PBKDF2 Invalid digest.` |
| Erro ao gerar o PBKDF2 | `PKCS5_PBKDF2_HMAC_SHA1 failed.` |

```

```

---

```

```

Testes de iteration e tempo médio de execução.

Abaixo consta um exemplo de reprodução, aumentando as iterações "iteration" demonstrando que quanto maior o número mais demora para terminar o processamento.  
Em caso de utilização de maquinas mais fracas o tempo aumentará, podendo dar a falsa impressão de lentidão no Application Server.

Tempo médio:

9.999.999 iterations 11 segundos. 

99.999.999 iterations 1 minuto e 45 segundos. 

999.999.999 iterations 17 minuto e 29 segundos.
