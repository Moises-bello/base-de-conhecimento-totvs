---
content_hash: 1bfc1f2782b2681ed66bba9798845a7e9ee48a1f1f67e352baeb984a70e251b3
fetched_at: '2026-06-29T00:08:38.985200+00:00'
page_id: '286004174'
product: rm
source: tdn-rm
title: 1075052 MSAU-12173 DT Observações como Justificativa de Recurso de Glosa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286004174
version: 104
---

# Observações como justificativa de recurso de glosa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Faturamento | Faturamento de recurso de glosa | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle® e SQL Sever® |

## Descrição

Criado parâmetro para que ao gerar o XML de recurso de glosa, na tag de justificativa de glosa seja enviado o texto digitado no campo observações da tela de recurso de glosa.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações do patch especifico da versão 12.1.16 previsto para o dia 04/08/2017

## Procedimento para Utilização

       1.           Cadastros > Faturamento > Condições contratuais com convênio > Selecionar um convênio > Eletrônico III - TISS > Sub aba "Geral II", marque o parâmetro "Utiliza o campo observação do recurso de glosa como justificativa na geração do XML de Recurso de Glosa";

       2.            Na tela de recurso de glosa, selecione o item a ser apresentado no XML de recurso e preencha o campo de observações do recurso.

       3.      Ao gerar o XML de recurso de glosa, a tag de justificativa virá preenchida com o texto digitado no campo de observações do recurso de glosa.

divs
