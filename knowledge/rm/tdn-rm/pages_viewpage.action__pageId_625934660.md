---
content_hash: db992ed5441045e7a61440c1fc6f804d157d437df4f4aebd7a54abe54a879ae6
fetched_at: '2026-06-29T00:11:04.261340+00:00'
page_id: '625934660'
product: rm
source: tdn-rm
title: Criar Nova Prescrição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=625934660
version: 15
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Parâmetros**

CRIAR NOVA PRESCRIÇÃOVisão Geral

## **01. VISÃO GERAL**

Funcionalidade que permite ao usuário criar uma nova prescrição.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

No menu de prescrição, caso o usuário não possua uma prescrição vigente, ou que possua, porém esteja dentro do horário de corte definido no cadastro da unidade no RM, o sistema permitirá criar uma prescrição.

Ao clicar em "+ Novo", o usuário poderá criar uma prescrição em branco, onde poderá incluir os itens normalmente conforme o padrão do sistema, ou criar a partir de um .

Ao optar por criar uma nova prescrição a partir de um modelo, o sistema listará os modelos disponíveis para escolha. Dessa forma, o sistema criará a prescrição com os itens do modelo escolhido.

Ao clicar no botão "Copiar prescrição" será exibido na tela todos os itens prescritos. Todos os itens são automaticamente assinalados para cópia e o usuário tem a opção de desmarcar o que não será copiado (exceto o item antibiótico após finalização do uso). 

Ao realizar a cópia, será gerada uma nova prescrição, a partir da anteriormente selecionada. A mesma estará em forma de rascunho e dependerá da liberação do usuário para estar vigente.

Parâmetros

## **03. PARÂMETROS**

Parâmetro que define quantidade de dias de validade da prescrição:

Configurações gerais:

Porém pode ser configurado por unidade via RM Saúde, caso configurado por unidade substituirá o parâmetro geral.

**Comportamentos parametrizados:**

* **Quantidade de dias:**  
  Define a quantidade de dias seguidos que a prescrição terá validade.
* **Hora de início:**  
  Define o período de validade das prescrições aplicando início (valor do parâmetro) e fim (valor do parâmetro - 1 minuto);
* **Hora de corte:**Define o início do período (Hora Corte até Fim de validade) onde será possível criar novas prescrições mesmo existindo prescrições vigentes;  
  Pode aplicar comportamento de ***extensão*** ou ***encurtamento***;  

  ***Extensão*:** Caso dentro do período de corte prescrição passa por extensão da validade,   
  onde não tendo uma prescrição anterior válida passará a ter a validade de *"Quantidade de dias"* + diferença da hora atual e da *"hora de início";  
    
  Exemplo: Hora Inicio: 10:00; Hora Corte: 06:00; Quantidade dias: 1; Utiliza horário de corte para período de validade da prescrição: Sim;  
  Ao criar uma nova prescrição ás 08:00 esta valerá por 26 horas, pois iniciará as 08:00 e terminará as 09:59 do dia seguinte.*

  ***Encurtamento*:** Caso dentro do período de corte prescrição passa por encurtamento da validade,   
  onde não tendo uma prescrição anterior válida e tendo a diferença entre a hora atual e *"hora de início"* maior que 1 hora essa prescrição terá somente esse período de validade.  
    
  *Exemplo: Hora Inicio: 10:00; Hora Corte: 06:00; Quantidade dias: 1; Utiliza horário de corte para período de validade da prescrição: Não;  
  Ao criar uma nova prescrição ás 08:00 esta valerá por 2 horas, pois iniciará as 08:00 e terminará as 09:59 do mesmo dia.*
* **Utiliza horário de corte para período de validade da prescrição:** **MARCADO**, indica que o valor de *"Quantidade de dias"* será utilizado para a data limite de validade da prescrição e ao criar prescrições **dentro do corte** esta poderá passar por processo de ***extensão*;**  
  **DESMARCADO**, indica que a quantidade de dias padrão (1 dia) será utilizado para a data limite de validade da prescrição. e ao criar prescrições **dentro do corte** está poderá passar por processo de ***encurtamento*;**O parâmetro de *"Quantidade de dias"* sempre será utilizado para definir a quantidade de dias de validade.  
   **MARCADO**, indica ao criar prescrições **dentro do corte** esta poderá passar por processo de ***extensão*;**  
  **DESMARCADO**, indica que ao criar prescrições **dentro do corte** está poderá passar por processo de ***encurtamento*;**
