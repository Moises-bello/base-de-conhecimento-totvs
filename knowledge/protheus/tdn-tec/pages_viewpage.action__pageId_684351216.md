---
content_hash: f078c0bc2df438a7204091983f4a6a1099c47ece09a55e82e274953fe7196952
fetched_at: '2026-07-02T19:24:27.856538+00:00'
page_id: '684351216'
product: protheus
source: tdn-tec
title: Correção - Caractere hífen ocultado em campos com máscara 9
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=684351216
version: 1
---

Correção - Caractere hífen ocultado em campos com máscara 9

|  |  |
| --- | --- |
| Situação | Durante o carregamento e exibição de dados provenientes do banco em campos de formulários ou de relatórios que tenham Picture de formação ou utilizam a função Transform() com a máscara 9, o caractere hífen não era exibido caso ele estivesse contido nos dados do campo em questão. |
| Ocorrência | Foi verificado que alguns relatórios não exibiam o hífen separador do campo de telefone, nos casos onde o hífen fazia parte da informação gravada no banco de dados e não o hífen da máscara de exibição. |
| Correção | O SmartClient recebeu um ajuste para tratar a exibição do caractere hífen em campos com máscara 9 somente no momento de entrada de dados do usuário como no momento da digitação ou por ação de copy/paste (permitir a entrada somente na primeira posição do campo onde indica número negativo). |
| Informações adicionais | * Referente à ocorrência: DTCLIENT01-3348 * Disponível em builds iguais ou superiores a 20.3.0.4 |
