---
content_hash: ef96cabe9ae1bb9ede9580d813ce1ae39a36d472e1480bd4cda98e8078369517
fetched_at: '2026-06-29T00:09:52.133202+00:00'
page_id: '438272150'
product: rm
source: tdn-rm
title: DSAUGHSCC-1486 DT TÉCNICA CIRÚRGICA NO REGISTRO DE INFORMAÇÕES CIRÚRGICAS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=438272150
version: 2
---

# TÉCNICA CIRÚRGICA NO REGISTRO DE INFORMAÇÕES CIRÚRGICAS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Registro de Informações Cirúrgicas | SauRegInfCirurgiaAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro de Técnicas Cirúrgicas | SauSurgicalTechniqueAction | |  |  | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | ``` SZTECNICACIRURGICA ```  ``` SZREGINFCIRURGIAPROC ``` |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Possibilitar informar a técnica cirúrgica utilizada para a realização do procedimento no Registro de Informações Cirúrgicas

## Procedimento para Utilização

* Acessar o menu Cadastros / Cuidados com o Paciente / Cirurgias / Técnica Cirúrgica
  + Cadastrar as técnicas cirúrgicas utilizadas, informando se a mesma é Invasiva, minimamente invasiva ou não invasiva
* Acessar o menu Cuidados com o Paciente / Centro Cirúrgica / Registro de Informações Cirúrgicas  
  + Cadastrar uma cirurgia e na aba Procedimentos, clicar em incluir e será exibida a tela dos procedimentos realizados e sua respectiva equipe. Para cada procedimento, pode-se informar a técnica cirúrgica utilizada.
