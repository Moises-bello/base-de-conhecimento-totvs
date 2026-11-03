---
content_hash: 597357a0d55f99e24e2f3082cd8880e366a479bde60cc390c1da9ea244b61437
fetched_at: '2026-06-29T00:10:07.911368+00:00'
page_id: '452719470'
product: rm
source: tdn-rm
title: Lotação Tributária - Cadastro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719470
version: 5
---

Conjunto de configurações onde o usuário define como será o formato da Máscara da Lotação Tributária  que irá preencher o campo Código Lotação automaticamente no Cadastro da Lotação Tributaria.  
   
A máscara é definida pela junção dos caracteres dos 3 campos abaixo:  
   
**Prefixo**: é opcional e seu tamanho mínimo é 1. Por default este campo vem desabilitado e com valor 0. Para habilitar é necessário marcar a opção 'utilizar prefixo'. Marcando esta opção, o campo prefixo referente ao código do prefixo fica habilitado para edição. Somente é permitido preencher este campo com o código com o mesmo tamanho da quantidade de caracteres informada. Este campo pode ser preenchido com alfanumérico.  
    
   
**Coligada**: O campo tem como tamanho mínimo 3 e um caractere recebe a Letra C. Caso a base tenha alguma coligada onde o código tem  tamanho maior que 3, este campo deverá ser preenchido como mínimo este valor.   
**Exemplo:** No cliente tem a coligada X com o código 9999, então o campo deve ser preenchido com o valor 5 e não pode ser menor. Neste caso o campo será de tamanho 5, pois também terá o caractere C.  
   
**Sequencial**: O campo recebe o tamanho mínimo 7, sendo que um caractere é referente a Letra S.   
**Exemplo:** Desta forma, a Máscara com mínimo de caracteres ficaria assim: PC999S999999 .  
   
**Código de Quebra de FPAS:**  
Código de quebra utilizado na geração do XML (S-1020)  eSocial .  
O gatilho será gerado para seção que estiver compatível com a quebra de FPAS cadastrada, e com o campo FPAS preenchido.  
Deixando o campo em branco o sistema considera o FPAS da seção centralizadora.  
   
**Observação**: O código de FPAS deve ser maior que o código quebra CNPJ  e menor igual máscara da seção.

**Considera lotação tributária atual para funcionários transferidos sem ônus para cedente no evento S-1200.**

Marcando este parâmetro quando for calculado uma diferença salarial (dissidio SIM) ,ao gerar o S-1200 a tag codLotacao deverá ser preenchida com a lotação atual.

   
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

eSocial

[Parametrizador](http://tdn.totvs.com.br/display/LRM/Parametrizador)
