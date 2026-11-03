---
content_hash: 3d2e22d19c0c694f878e5914f2fab6989a113c77357f8005f10159128f484c3e
fetched_at: '2026-06-29T00:10:03.950740+00:00'
page_id: '452719178'
product: rm
source: tdn-rm
title: Configurações Gerais 2/7
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719178
version: 11
---

Nesta aba é possível fazer as Configurações Gerais relacionadas ao eSocial:   
   
   
**Máscara para Matrícula do Trabalhador**  
Conjunto de configurações onde o usuário define como será o formato da Máscara da Matrícula do Trabalhador que irá preencher o campo Matrícula eSocial automaticamente no Cadastro do Funcionário.  
   
A máscara é definida da junção dos caracteres dos 3 campos abaixo:  
·         **Prefixo**: é opcional e seu tamanho mínimo é 1. Por default este campo vem desabilitado e com valor 0. Para habilitar é necessário marcar a opção 'utilizar prefixo'. Marcando esta opção, o campo prefixo referente ao código do prefixo fica habilitado para edição. Somente é permitido preencher este campo com o código com o mesmo tamanho da quantidade de caracteres informada. Este campo pode ser preenchido com alfanumérico.    
   
·         **Coligada**: O campo recebe o tamanho mínimo 3, sendo que um caractere recebe a Letra C. Caso a base tenha alguma coligada de código com tamanho maior que 2, este campo deverá ser preenchido com a quantidade de caracteres do código da coligada +1.   
   
Exemplo: No cliente tem a coligada X com o código 9999, então o campo o campo deverá ser preenchido com o valor 5 e não pode ser menor. Neste caso o campo será de tamanho 5, pois também terá o caractere C.  
   
·         **Sequencial**: O campo recebe o tamanho mínimo 7, sendo que um caractere é referente a Letra S.  
   
Exemplo:  
Desta forma, a Máscara com mínimo de caracteres ficaria assim: PC99S999999  
   
   
   
**Gerar matrícula automaticamente na admissão de funcionário**  
Confirmando este parâmetro ao admitir um funcionário será gerada matrícula para eSocial automaticamente.

* O usuário poderá aumentar a quantidade de caracteres nos três campos, limitando a soma dos três em 30 caracteres. Os valores mínimos carregados por default não podem ser diminuídos.
* Após fazer a configuração e/ou um Cadastro de Funcionário, onde foi inserido uma Matrícula eSocial no cadastro do Funcionário, caso o usuário deseje alterar a Máscara para Matrícula do Trabalhador, o sistema permite, porém exibe uma mensagem que pode causar duplicidade de Matrículas já geradas.
* A configuração de Máscara para Matrícula do Trabalhador deve ser feita por Coligada.

**Utilizar prefixo para identificação eventos de tabela**  
Este parâmetro poderá utilizado quando existir mais de uma coligada com o mesmo CNPJ raiz. Isso ocorre quando a filial é cadastrada como coligada.   
   
Ao marcar esse parâmetro, o campo "Prefixo" e o parâmetro "Utilizar código da coligada como prefixo" serão habilitados.  
Caso escolher o campo "Prefixo" os códigos de identificação dos registros no XML serão alterados e em sua frente serão adicionados esse prefixo. Caso escolher o parâmetro "Utilizar código da coligada como prefixo", o código da coligada será adicionado à frente.   
**Atenção**

1. Esse parâmetro será válido para geração dos eventos S-1010(ideTabRubr), S-1020,(codLotacao) S-1030(codCargo), S-1040(codFuncao), S-1050(codHorContrat) e S-1060(codAmb).
2. A soma da máscara de Lotação Tributária + Prefixo Eventos de Tabelas não poderá ser superior a 30 caracteres.

**Exemplos**

* **Sem a utilização do prefixo**
  1. Parametrizador Parâmetro desmarcado
  2. XML S-1010 Para a rubrica 0001 a TAG (ideTabRubr) retornará o valor "0001".
  3. XML S-1020 Para a lotação C01S000001 a TAG (codLotacao) retornará o valor "C01S000001".
* **Utilizando o prefixo**
  1. Parametrizador Parâmetro marcado e prefixo preenchido com "AA"
  2. XML S-1010 Para a rubrica 0001 a TAG (ideTabRubr) retornará o valor "AA0001".
  3. XML S-1020 Para a lotação C01S000001 a TAG (codLotacao) retornará o valor "AAC01S000001".
* **Prefixo como código da coligada**
  1. Parametrizador Parâmetro marcado e "Utilizar código da coligada como prefixo" marcado. Código da coligada: 1
  2. XML S-1010 Para a rubrica 0001 a TAG (ideTabRubr) retornará o valor "10001".
  3. XML S-1020 Para a lotação C01S000001 a TAG (codLotacao) retornará o valor "1C01S000001".

**Utiliza quebra de CAEPF:**  
Código de quebra utilizado no cadastro de hierarquia de seção para geração do evento S-1005 do eSocial por CAEPF.  
**Observação**: Deverá utilizar a mesma quebra do "Código de quebra para CNPJ". Mais informações [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=659592652)

|  |  |
| --- | --- |
|  | Informações Complementares |

---

eSocial  
[Parametrizador](http://tdn.totvs.com.br/display/LRM/Parametrizador)
