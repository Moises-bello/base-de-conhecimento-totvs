---
content_hash: 89c9369fea1bec57ba6eee7e081cafdb518a2bed69dd3584d690dbf1942cbf08
fetched_at: '2026-06-29T00:09:27.429610+00:00'
page_id: '423938519'
product: rm
source: tdn-rm
title: Cadastro da Máscara do Tipo de Objeto de Manutenção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938519
version: 2
---

Máscara do 1º e 2º Identificadores: Para padronizar o preenchimento do 1º e 2º Identificador do Objeto de Manutenção, você poderá utilizar máscaras de dados.   
Cada caractere da lista de regras representa um resultado de máscara diferente nos Identificadores do Objeto de Manutenção.   
Basta preenchê-los no campo das máscaras de acordo com as regras listadas em "Instruções da Máscara".  
Essas máscaras deverão ser criadas preenchendo os campos "Máscara 1º Identificador" e "Máscara 2º Identificador", utilizando os caracteres listados abaixo:

| Máscara | Regra |
| --- | --- |
| **0** | Entre 0-9 (obrigatório) |
| **9** | Entre 0-9 ou espaço (Não obrigatório) |
| **#** | Entre 0-9, (menos), (mais) ou espaço (Não obrigatório) |
| **L** | Entre a-Z, A-Z (Obrigatório) |
| **?** | Entre a-Z, A-Z (Não Obrigatório) |
| **A** | Qualquer caractere alfanumérico (Não Obrigatório) |
| **.** | Separador de decimal |
| **,** | Separador de milhar |
| **:** | Separador de Hora |
| **/** | Separador de Data |
| **$** | Traz o símbolo da Moeda corrente Ex: (R$, US$) |
| **<** | Converte todos os caracteres para caixa baixa |
| **>** | Converte todos os caracteres para caixa alta |
| **\** | Desativa mascara de um caráter especial. |
