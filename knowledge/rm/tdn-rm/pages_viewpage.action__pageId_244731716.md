---
content_hash: e9d68b2f4c3bf3954917f5b1fe7184db13344f03a02b45c686537ccbe8e3041a
fetched_at: '2026-06-29T00:08:15.125379+00:00'
page_id: '244731716'
product: rm
source: tdn-rm
title: Importação_Dados_CEST
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244731716
version: 8
---

# Importação de Dados CEST

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | Linha RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Importação Dados CEST | Importação Dados CEST |        |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Processo no cadastro de Produtos (Nucleos) | Produtos | |  |  | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Chamados Relacionados** | TTWLQ7 |
| **Requisito (ISSUE):** | FIS000434 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | SQLServer e Oracle |
| **Tabelas Utilizadas:** | TPRDFISCAL, TPRODUTO |
| **Sistema(s) Operacional(is):** |  |
| **Versões/Release:** | *12.1.13* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** | *12.1.13* |

## Objetivo

Especificar as regras de negócio e o comportamento do Sistema ao importar código CEST para o sistema.

## Premissas

Este novo processo chamado ‘Importação de Dados CEST’ é responsável por importar dados para tela Produto | Dados Fiscais e atualizar o  campo ‘Código CEST’.

## Definição da Regra de Negócio

* Deverá ser criado um arquivo no formato .CSV cuja primeira coluna seja o NCM (com máscara ou sem máscara) e a segunda coluna seja o Código CEST (com máscara ou sem máscara).

Ex:                 ***NCM;CEST;***

***3815.12.10;02.002.00;***

***39181000;02.002.00;***

***3923.30.00;0200200;***

***39263000;0200200;***

***7009;0200200;***

* Este processo está preparado para receber NCM incompleto onde se comportará da seguinte forma: Poderá ter só o início do NCM e o CEST será aplicado para todos os produtos de mesma raiz de NCM. Por exemplo, se no arquivo tiver o NCM 7009, o CEST equivalente deverá ser aplicado para os produtos de NCM 7009.01.01, 7009.01.02, etc.
* Poderá também indicar se deseja alterar os dados já existentes na base ou executar somente sobre os registros que não tenham o Código CEST já preenchido.
* O processo permite que seja selecionado registros (Produtos) na visão para os quais deseja inserir os dados, mas caso não seja selecionado registro nenhum, a importação será feita para todos os registros (Produtos).
* Registros com mesmo código CEST não serão alterados.
* Se forem passados vários arquivos.csv e se estes arquivos tiverem NCM iguais, irá permanecer o código CEST do ultimo arquivo.

## Descrição detalhada do processo

1. O usuário cria um arquivo no formato .CSV cuja primeira coluna seja o NCM (com máscara ou sem máscara) e a segunda coluna seja o Código CEST (com máscara ou sem máscara);
2. O usuário navega até a  tela | BackOffice | Gestão Fiscal | Cadastros | Produtos;
3. O usuário seleciona os registros (Produtos) na visão para os quais deseja atualizar os dados, mas caso não seja selecionado registro nenhum, a atualização será executada para todos os registros;
4. O usuário aciona o processo 'Importação Dados CEST';
5. Na tela do processo, o usuário seleciona os arquivos .CSV criados;
6. Marcar ou não o campo ‘Sobrescrever código CEST’;
7. Clicar em executar;
8. O sistema irá percorrer cada linha de cada arquivo, buscando ‘Produto/Dados Fiscais’ com  mesmo ‘NCM’;
9. Ao encontrar, o sistema irá atualizar o ‘Código CEST’ em ‘Produto | Dados Fiscais | campo Código CEST’;
   1. Se o campo ‘Sobrescrever código CEST’ estiver marcado o sistema irá atualizar todos os registros, sobrescrevendo os valores já existentes;
   2. Se o campo ‘Sobrescrever código CEST’ não tiver marcado o sistema irá atualizar apenas os registros que não estão preenchidos;
10. Registros com mesmo código CEST não serão alterados;
11. Fim do processo;
