---
content_hash: 28565886a31ddce7300222bb1a026896b7677e8025c3cd1304a802ae50b8cde9
fetched_at: '2026-06-29T00:10:19.441312+00:00'
page_id: '4813674'
product: rm
source: tdn-rm
title: Contabilização de Movimentação de Baixa de Estoque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813674
version: 6
---

BLOCK

Contabilização de Movimentação de Baixa de Estoque

FAQ: **Contabilização de Movimentação de Baixa de Estoque**

Avaliação

* **Introdução**

Permitir que a contabilização das movimentações de baixa de estoque seja sempre pelo custo médio do item de movimento, evitando assim diferença do valor contabilizado e o custo.

Solução

* **Desenvolvimento/Procedimento**

1. Parametrização do Tipo de Movimento

* Identificar todos os tipos de movimentos de baixa de estoque que geram contabilização.
* Acessar os tipos de movimentos e na etapa **Contabilidade** verificar como esta definido o parâmetro **“Habilita evento Contábil”**, se na Natureza, Natureza Inversa ou Tipo de Movimento.
* Retirar o evento do local definido no item anterior, ou seja, se na Natureza do Movimento, na Natureza Inversa do Movimento ou no Tipo de Movimento.
* Desmarcar o parâmetro **“Contabilização Obrigatória”**.

2. Fórmula do Evento Contábil

- Criar uma fórmula que considere o valor unitário do item conforme controle de custo (custo por filial ou custo por local) e contabilização.

> Se não houve conversão de custo por filial, parâmetro **“Custo por Filial”** desmarcado na etapa **Custo** em Gestão de Estoque / Definições de Estoque e desejar contabilizar por filial, utilizar a fórmula:

> **KQT \* TABITM ('VALORUNITARIO' , 'V')**

> Se houve conversão de custo por filial, parâmetro **“Custo por Filial”** marcado na etapa **Custo** em Gestão de Estoque / Definições de Estoque e desejar contabilizar por filial, utilizar a fórmula:

> **KQT \* TABITM ('VALORUNITGERENCIAL’ , 'V')**

> Se houve conversão de custo por filial, parâmetro **“Custo por Filial”** marcado na etapa **Custo** em Gestão de Estoque / Definições de Estoque e desejar contabilizar por local de estoque, utilizar a fórmula:

> **KQT \* TABITM ('VALORUNITARIO’, 'V')**

***OBS: As sugestões de fórmulas não contemplam todas as informações para a composição do custo ela contempla apenas as informações básicas, sendo assim pode ser alterada conforme necessidade.***

3. Evento Contábil utilizado nas movimentações de baixa de estoque

- Criar ou editar o evento contábil utilizado.

- Incluir ou editar o item de evento responsável pela contabilização do custo do item de movimento e informar a fórmula criada no tópico 2.

- Vale lembrando que a origem da conta fica a critério do usuário, mas a opção **“Aplicar em”** deverá ser Item, por causa do conteúdo da fórmula utilizada.

4. Procedimento utilizado para a contabilização dos movimentos

Após o termino do período definido pela empresa/usuário para contabilização de movimentos, geralmente mensal, os processos abaixo devem ser seguidos.

- Certificar-se que nenhum movimento anterior a data definida pela empresa/usuário será incluído ou alterado;

- Regerar saldos e Custos de todos os produtos ou dos produtos desatualizados. É recomendado marcar o parâmetro “Forçar regeração”. *Explicações sobre este parâmetro: Se marcada define que a data inicial dos movimentos do produto a regerar será a data de fechamento de estoque (parâmetros gerais); caso contrário será a data da primeira alteração de estoque do produto (campo da tabela de produto atualizado na rotina de estoque caso haja uma movimentação que afete estoque anterior à data corrente indicada no campo). Caso esta data de alteração seja menor que a data de fechamento de estoque, será usada sempre esta última. Quando o fechamento do estoque é por saldo, será usada sempre a data de fechamento do saldo regerado;*

- Fechar a data de fechamento de estoque. Lembrando que a partir deste momento não será mais possível alterar ou incluir movimentação anteriores a esta data;

- Criar um filtro por tipo de movimento de baixa de estoque que trate todas as movimentações que não foram contabilizados dentro do período determinado pela empresa/usuário e esteja anteriores a data de fechamento de estoque;

- Selecione todos os movimentos que deseje contabilizar;

- Acesse o menu movimento e clique na opção **“Gerar Contabilização”** em seguida clique em “SIM”;

- Selecione o evento contábil correspondente aos movimentos e clique em OK.

* **Informações Adicionais**

Este é o processo correto para garantir que as contabilizações das notas de baixa de estoque sejam sempre contabilizados pelo custo médio dos itens de movimento, mas para isto é recomendado seguir todo os procedimentos deste documento e evitar de voltar a data de fechamento de estoque, uma vez que a alteração de um movimentos anterior a esta data poderá comprometer a integridade dos valores contabilizados dos custos.

Para maiores informações:

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
