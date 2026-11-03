---
content_hash: 2b6299d009bac41ef3ed5319c6ab73d82f8a3124a6ae1790bfed4211652f7317
fetched_at: '2026-06-29T00:08:58.027268+00:00'
page_id: '358458222'
product: rm
source: tdn-rm
title: DT Configuração da Carteira do Convênio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=358458222
version: 90
---

# Leitura da Carteirinha do Convênio do Paciente: Cadastro

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cadastro de Configuração da Carteira do Convênio | ``` SauConfigCarteiraConvAction ``` |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro de Convênios | SauCadGeralConvAction | |
| **Cadastros Iniciais:** | Convênios |
| **Requisito/S****tory/Issue:** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1122 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Tabelas Utilizadas:** | SZCONFIGCARTEIRACONV, SZCADGERAL |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

A partir dessa implementação, é possível estabelecer as regras para que o TOTVS Gestão Hospitalar utilize os  dados contidos nos cartões magnéticos dos usuários de planos de saúde.

## Procedimento para Utilização

1. Acesse **Cadastros / Uso Geral / Convênio**.
2. Selecione um registro de **Convênio / Anexos / Configuração da Carteira do Convênio.**
3. Ao acessar o anexo, será disposta a lista de Correspondências no Sistema por Trilha.
   1. Para cadastrar um registro é necessário preecher os seguintes campos:
   * + \*Trilha: Informação que indica de qual trilha a correspondência no sistema encontra-se;
     + \* \*\*Tamanho Fixo: Informa se as informações possuem tamanho fixo;
     + Sentinela Inicial, Final e Separador: Caractére(s) que representa(m) respectivamente as informações;
     + \*\*Ordem: Informação referente ao posicionamento da da informação dentro da trilha\*\*Posição Inicial e Final: Representação do início e fim do posicionamento da informação dentro da trilha.
     + \*\*Máscara: Máscara de formatação da Data (ex.: dd/MM/yyyy)
     + **\*Campo Obrigatório****\*\*Campo relacionado a um e/ou mais fluxos alternativos (vide abaixo)**Observações

     Quando o campo Tamanho Fixo, encontra-se desmarcado, os campos Separador e Ordem são dispostos para o preenchimento. Caso contrário, são os campos Posição Inicial e Posição Final que serão dispostos.

     O tamanho fixo indica que a informação correspondente inicia e termina em uma posição especifica da trilha Ex.: A Matrícula do Usuário está na trilha 1, entre as posições 10 e 40 da trilha.

## Exemplos de preenchimento

* Campo Tamanho Fixo **Descamarcado.**
* Campo Tamanho Fixo **Marcado.**

  Observações

  Informação: Ao acessar, clicar e/ou passar o mouse sobre os campos Posição Inicial e Posição Final, a seguinte mensagem de auxílio será rapidamente apresentada:

Correspondência no Sistema do tipo Data (Data de nascimento e Validade da Matrícula)

Observações

Exemplos de preenchimento do campo Máscara

* dd/MM/yy → 09/02/93 (9 de fevereiro de 1993)
* dd/MM/yyyy → 09/02/1993 (9 de fevereiro de 1993)
* MM/dd/yy → 02/09/93 (fevereiro, 9 de 1993)

Demais exemplos de montagem de Máscara podem ser encontrados no seguinte guia [Cadeias de caracteres de formato de data e hora personalizado](https://msdn.microsoft.com/pt-br/library/8kb3ddd4(v=vs.110).aspx)

divs
