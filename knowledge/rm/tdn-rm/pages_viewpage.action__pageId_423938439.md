---
content_hash: 22f3a6ddf4ef98251bb5038b4a9f6e75c43b7fc09ebb53a0e9213823f3fcd9b2
fetched_at: '2026-06-29T00:09:27.144365+00:00'
page_id: '423938439'
product: rm
source: tdn-rm
title: Itens Gerenciais - Itens Evento - Eventos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938439
version: 5
---

O valor contábil dos lançamentos gerados na contabilização de um processo pode ser rateado, ou seja, dividido proporcionalmente para uma ou mais contas gerenciais.   
O rateio gerencial somente será possível para a conta contábil utilizada no lançamento que possuir distribuição gerencial (campo "Tem distribuição Gerencial" no cadastro da conta).  
Para cada conta contábil (item de evento) podem-se incluir vários itens gerenciais (rateios), sendo que a soma dos valores rateados deve ser igual ao valor lançado na conta contábil correspondente.

Na janela principal é possível visualizar o cadastro geral dos Itens Gerenciais.   
Ao acessar uma das opções, Incluir ou Editar, o sistema abrirá uma janela de edição com todos os dados do Item Gerencial a ser incluído ou alterado.   
Através desta janela é possível definir como será o rateio contábil, incluindo os defaults dos itens gerenciais.

**Origem da Conta:**   
Selecione qual será a origem das contas gerenciais, ou seja, de qual local as contas gerenciais serão buscadas para receberem o rateio.

Os campos disponíveis nesta tela irão mudar dependendo da opção aqui selecionada. Se, por exemplo, a opção selecionada for Default Tabelas, deve-se em seguida informar em qual "Tabela" o sistema deverá buscar a conta gerencial. Se a opção selecionada for Informar Conta, em seguida deve-se informar a conta gerencial que receberá o rateio.

**Aplicar:**   
Informe onde o rateio gerencial a ser gerado será aplicado. A opção aqui selecionada dirá qual a abrangência ou incidência em que o rateio será gerado.

**Descrição:**Informe uma descrição para identificar este item na janela principal onde se visualiza o cadastro geral dos Itens Gerenciais.

**Percentual:**   
Este campo somente será apresentado se na pasta de identificação do evento foi selecionado "Percentual" para calcular o valor contábil do lançamento.   
Informe o percentual a ser rateado para a conta gerencial deste item. Este percentual incidirá sobre o valor contábil calculado para o item de evento (conta contábil) correspondente.

**Fórmula:**   
Este campo somente será apresentado se na pasta de identificação do evento foi selecionado "Fórmula" para calcular o valor contábil do lançamento.   
Informe a fórmula que deverá ser utilizada para se chegar ao valor a ser rateado para a conta gerencial deste item.
