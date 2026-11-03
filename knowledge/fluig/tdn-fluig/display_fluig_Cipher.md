---
content_hash: e27a47839538ff7ffbc0559fb1d8fdebad250d7f7485f0d319233b9622b00fa9
fetched_at: '2026-06-28T21:35:28.077079+00:00'
page_id: '6066571'
product: fluig
source: tdn-fluig
title: Cipher
type: documentation
url: https://tdn.totvs.com/display/fluig/Cipher
version: 11
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade desse componente é criptografar ou descriptografar informações trafegadas no Fluig | ESB. O componente de criptografia permite que seja possível criptografar e descriptografar mensagens de forma simétrica e assimétrica. As propriedades comuns se encontram na tabela abaixo.

* **Simétrica**: criptografia baseada em algoritmos que dependem de uma mesma chave, denominada chave secreta, que é usada tanto no processo de criptografia quanto no de descriptografia. Somente o emissor e o receptor devem conhecer a chave secreta. Este processo é mais rápido que a criptografia assimétrica.

* **Assimétrica**: criptografia baseada em algoritmos que utilizam duas chaves diferentes, relacionadas matematicamente através de um algoritmo, de forma que o texto cifrado pela chave 1 do par somente poderá ser decifrado pela chave 2 do mesmo par.

As duas chaves envolvidas são denominadas pública e privada. Se a mensagem for criptografada com a chave pública (de domínio comum), somente o receptor que tiver a chave privada pode descriptografar os dados. Isso garante que somente quem tem a posse da chave privada pode abrir a mensagem. Já se a mensagem for criptografada com a chave privada, todos os receptores que tiverem posse da chave pública poderão ler a mensagem e ter a garantia de que quem criptografou a mensagem somente pode ser o detentor da chave privada.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Mode | Selecionar o modo de criptografia.  1. **Symmetric**: para quando a criptografia é feita utilizando um algoritmo e uma senha; 2. **Asymmetric**: para quando a criptografia é feita utilizando uma chave pública ou privada. |
| Action | Selecionar a ação que será realizada.  1. **Encrypt**: quando se deseja criptografar as informações; 2. **Decrypt**: quando se deseja descriptografar as informações. |

O componente possui propriedades específicas para cada modo de criptografia. Para a criptografia Symmetric (simétrica) as seguintes propriedades são habilitadas.

| Campo | Descrição |
| --- | --- |
| Algorithm | Selecionar o algoritmo de criptografia a ser utilizado. Os algoritmos de criptografia mais utilizados são o AES o BLOWFISH, porém o algoritmo deverá ser selecionado considerando qual o algoritmo é utilizado no sistema externo. |
| Password | Inserir a senha para criptografia ou descriptografia. A mesma senha utilizada para criptografar deve ser usada para descriptografar. |

Para a criptografia Asymmetric (assimétrica) as seguintes propriedades são habilitadas.

| Campo | Descrição |
| --- | --- |
| Keystore | Inserir o caminho completo para o diretório no qual se encontram os certificados. |
| Key Alias | Inserir o apelido do certificado dentro do Keystore. |
| Password | Inserir a senha para criptografia ou descriptografia. A mesma senha utilizada para criptografar deve ser usada para descriptografar. |
| Key Type | Selecionar o tipo da chave.  1. **Private**: quando a chave utilizada é uma chave Privada; 2. **Public**: quando a chave utilizada é uma chave Pública. |
