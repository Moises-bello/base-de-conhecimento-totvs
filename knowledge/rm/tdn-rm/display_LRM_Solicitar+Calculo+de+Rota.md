---
content_hash: add38eda3e24039e40eb8260ed945a6de25cef77a8e5bd44eb0cb142c78b9416
fetched_at: '2026-06-29T00:09:59.327260+00:00'
page_id: '452718299'
product: rm
source: tdn-rm
title: Solicitar Calculo de Rota
type: documentation
url: https://tdn.totvs.com/display/LRM/Solicitar+Calculo+de+Rota
version: 3
---

**Solicitar Calculo de Rota**

Este processo tem a finalidade de enviar o endereço dos candidatos e das seções selecionadas para o webservice do Sat Rotas para serem roteirizados.

Para executar o processo o usuário seleciona os candidatos que deseja solicitar o cálculo e executa o processo. Durante a execução do processo deverão ser informadas as seções dos candidatos, ao concluir o processo as informações serão enviadas para o sistema do SatRotas.

Este processo poderá ser executado em quaisquer etapas do processo seletivo e mais de uma vez, caso necessário.

Exemplo:

• Candidatos selecionados: José e Maria

• Sites selecionados: Alegria e Lapa

Resultado do processo:

1. Cód 001 – Rota do Endereço José versus Endereço Site Alegria

2. Cód 002 – Rota do Endereço José versus Endereço Site Lapa 3.

Cód 003 – Rota do Endereço Maria versus Endereço Site Alegria

4. Cód 004 – Rota do Endereço Maria versus Endereço Site Lapa

Após a execução do assistente, o sistema grava os identificadores dos pedidos de solicitação de cálculo de rotas (ID Rota), de acordo com a quantidade de destinos selecionados. Para o caso de reprocessamento, as informações previamente geradas deverão ser substituídas pela última roteirização.

**Dica:**

Para evitar erros no calculo de rotas o endereço dos candidatos e das seções deve estar corretamente preenchidos.
