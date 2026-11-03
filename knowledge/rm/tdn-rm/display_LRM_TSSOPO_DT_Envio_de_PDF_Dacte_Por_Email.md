---
content_hash: a659b82ff5aa9ce3758011dc015f3eaa8d9c5f5dc5b5f3583b5f36db0a1ffbd9
fetched_at: '2026-06-29T00:06:05.601975+00:00'
page_id: '201725324'
product: rm
source: tdn-rm
title: TSSOPO_DT_Envio_de_PDF_Dacte_Por_Email
type: documentation
url: https://tdn.totvs.com/display/LRM/TSSOPO_DT_Envio_de_PDF_Dacte_Por_Email
version: 2
---

# E DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | CTE.004 | CT-E - RELATORIO | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados relacionados** | TSSOPO |
| **Requisito (ISSUE):** | MOV000159 - Conhecimento de Transporte - CTRC e CT-e |
| **País(es):** | *N/A* |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas utilizadas:** | TCTE, GFONTEDADOS |
| **Sistema(s) operacional(is):** |  |
| **Versões/Release:** | 11.82.40, 11.82,41 e 12.1.8 |

## Descrição

Implementação do processo de envio de PDF do DACTE por e-mail.

Na tela de configuração do envio de e-mail do CT-e, será disponibilizado um checkbox para que o usuário decida se também deseja enviar o PDF do DACT-e além do XML. Caso essa opção seja marcada será habilitado um campo para que o usuário selecione o report que deseja enviar. Após selecionado o report será gerado internamente e enviado por e-mail no formato PDF.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações **11.82.41** ou **12.1.7** deste chamado.

A implementação está disponível também no patch específico 11.82.40.103 ou superior.

## Procedimento para Utilização

       1.            No Totvs Gestão de Estoque, Compras e Faturamento acesse a aba **Vendas** e clique em **Faturamento -> Conhecimento de Transporte Eletrônico.**

       2.            Selecione um Conhecimento de Transporte com status = Autorizado.

       3.            Selecione **Processos > Envio de CTe por E-mail**

       4.            Ao abrir a tela, marque a opção **Enviar relatório DACTE em PDF** e selecione o relatório. Caso exista algum Relatório definido como padrão nos parametros do Tipo de Movimento, o mesmo será selecionado automaticamente, embora o usuário possa escolher outro..

       5.            Execute o processo e o e-mail será enviado com o PDF e o XML do CT-e.
