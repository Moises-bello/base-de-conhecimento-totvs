---
content_hash: 9d443dfb0973e874d87e29e9e3564e57e2d6510e3b5d7a501cbb212fdbd17839
fetched_at: '2026-06-29T00:06:18.928158+00:00'
page_id: '219689297'
product: rm
source: tdn-rm
title: TTQJQT_DT_Envio_de_PDF_Dacte_Por_Email
type: documentation
url: https://tdn.totvs.com/display/LRM/TTQJQT_DT_Envio_de_PDF_Dacte_Por_Email
version: 1
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | NF.01.0002 | NF-E ENVIAR XML POR EMAIL | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | TTQJQT |
| **Requisito (ISSUE):** | MOV000085 - Envio de emails pelo gerador |
| **País(es):** | *N/A* |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | *TCTE* |
| **Sistema(s) Operacional(is):** |  |
| **Versões/Release:** | 12.1.8 |

## Descrição

Implementação do processo de envio de PDF do DACTE por e-mail.

Na tela de configuração do envio de e-mail do CT-e, será disponibilizado um checkbox para que o usuário decida se também deseja enviar o PDF do DACT-e além do XML. Caso essa opção seja marcada será habilitado um campo para que o usuário selecione o report que deseja enviar. Após selecionado o report será gerado internamente e enviado por e-mail no formato PDF.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações **12.1.8** deste chamado.

## Procedimento para Utilização

       1.            No Totvs Gestão de Estoque, Compras e Faturamento acesse a aba **Vendas** e clique em**Faturamento -> Conhecimento de Transporte Eletrônico.**

       2.            Selecione um Conhecimento de Transporte com status = Autorizado.

       3.            Selecione **Processos > Envio de CTe por E-mail**

       4.            Ao abrir a tela, marque a opção **Enviar relatório DACTE em PDF** e selecione o relatório. Caso exista algum Relatório definido como padrão nos parametros do Tipo de Movimento, o mesmo será selecionado automaticamente, embora o usuário possa escolher outro..

       5.            Execute o processo e o e-mail será enviado com o PDF e o XML do CT-e.

divs
