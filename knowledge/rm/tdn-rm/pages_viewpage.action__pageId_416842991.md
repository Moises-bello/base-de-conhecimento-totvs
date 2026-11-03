---
content_hash: 97806be79846ad8ca2c7677b4d7e433f795b9100ceb7eb446f47ce7e8f45d504
fetched_at: '2026-06-29T00:09:12.243676+00:00'
page_id: '416842991'
product: rm
source: tdn-rm
title: Como realizar o processo de retificação dos eventos S-2200, S-2205, S-2206,
  S-2300 e S-2306?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=416842991
version: 42
---

# Objetivo:

---

Nas versões anteriores o processo de retificação dos eventos S-2200, S-2205, S-2206, S-2300 e S-2306 era realizado somente através do TAF. A partir das versões 12.1.21.128, 12.1.20.386 e 12.1.19.387, foi disponibilizado um módulo para geração da retificação destes eventos através TOTVS Folha de Pagamento.

Para realizar o processo de retificação destes eventos o usuário deverá executar os seguintes passos:

1true1Passo 1Passo 1

Acesse o menu Folha de Pagamento | eSocial | Processos | Outros Processos | Retificação de Eventos do Funcionário

2Passo 2Passo 2

Selecione a chapa desejada para que sejam listados todos eventos com status **10-Aceito RET** desse funcionário, e em seguida selecione qual(is) evento(s) deseja retificar e clique em avançar.

3Passo 3Passo 3

Nesta tela poderemos realizar as seguintes operações:

2true1EdiçãoEdição

A esquerda da tela serão disponibilizados os campos para a retificação (conforme leiaute do xml do eSocial). Para editá-los basta selecionar o grupo e o campo desejado.

A direita será habilitado o campo selecionado para que possa informar o novo valor.

Lembrando que este campo é dinâmico, ou seja, não será apresentado o lookup da tabela, o usuário deverá digitar o valor e ao avançar o sistema irá validar a existência do registro na tabela.

**Atenção:**

* + Caso escolha mais de um evento do mesmo tipo, as tags serão preenchidas com o mesmo valor.  
    **Exemplo:**   
    Ao retificar dois eventos S-2206 o sistema apresentará somente uma árvore (grupos e tags) para esse evento, caso necessite retificar a tag de 'codCargo', ela será alterada nos dois XML's.
  + O sistema mostra os campos obrigatórios para preenchimento, estes não poderão ser excluídos, somente editados. Caso adicione algum grupo que possua um campo obrigatório e ele não esteja preenchido o sistema não gerará o xml.

Os campos Multivalorados (conteúdo composto por mais de um valor) são construídos de acordo com os valores preenchidos na grid. A grid se comporta de duas formas:

* + - Ao clicar em "Carregar dados XML" é retornado as informações existentes do xml selecionado.
      * Poderá ser feito a edição ou exclusão dos registros em cada linha apresentada.
      * Caso tenha selecionado mais de um xml do mesmo tipo o sistema trará as informações do primeiro xml conforme data do evento.

* + - Pode-se escolher por realizar a inclusão de uma nova lista ao invés de carregar os dados existentes.   
      **Atenção:** Ao incluir uma nova lista os dados do xml(s) anterior(es) será(ão) substituído(s).

2ExclusãoExclusão

Para realizar uma retificação excluindo um campo ou grupo do xml, basta selecionar o grupo na árvore e clicar no campo desejado, em seguida escolha a opção **Deletar**.

Após a exclusão, o campo será ~~rasurado~~ conforme legenda. Será possível cancelar a exclusão selecionando o campo novamente e clicando em desfazer.

3Copia de valores para XMLs relacionadosCopia de valores para XMLs relacionados

Caso tenha escolhido mais de um registro para realizar a retificação e entre eles possua um registro pai, o sistema habilitará o campo "replicar valor", que servirá para replicar o valor de um campo digitado no registro pai para o registro filho.

**Exemplo:** Alteração do campo 'nisTrab' no evento S-2200 (Registro Pai). Ao clicar no botão "Replicar Valor", o sistema irá retificar a tag 'nisTrab' também dos registros S-2205 e S-2206.

4Passo 4Passo 4

Nesta tela o sistema apresenta um comparativo das tags que foram alteradas. Verifique as alterações e caso esteja de acordo clique em "Avançar" e em sequência "Executar".

**Observação:**

O usuário poderá agrupar os campos para visualização do comparativo conforme desejado.

Processo foi executado com sucesso, sistema irá apresentar um log com ID's dos eventos que foram retificados e os ID's correspondentes de sua retificação.

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.22 |
| 12.1.21 |
| 12.1.20 |
| 12.1.19 |

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autor:**
