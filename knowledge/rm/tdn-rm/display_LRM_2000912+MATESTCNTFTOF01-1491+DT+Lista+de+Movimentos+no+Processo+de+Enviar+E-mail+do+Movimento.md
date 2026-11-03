---
content_hash: 780b44ba9c1741c634e4e68be8e49c08e72eb056d31e0f17c40468bc35cf187b
fetched_at: '2026-06-29T00:08:49.503228+00:00'
page_id: '330837060'
product: rm
source: tdn-rm
title: 2000912 MATESTCNTFTOF01-1491 DT Lista de Movimentos no Processo de Enviar E-mail
  do Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/2000912+MATESTCNTFTOF01-1491+DT+Lista+de+Movimentos+no+Processo+de+Enviar+E-mail+do+Movimento
version: 1
---

# LISTA DE MOVIMENTOS NO XML DE PARÂMETROS DO PROCESSO DE ENVIAR E-MAIL DO MOVIMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção & Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Enviar E-mail do Movimento. |
| **Situação/Requisito:** | Ao gerar os parâmetros do processo de **Enviar E-mail do Movimento** através da utilização do recurso da Fórmula Visual não era carregado a Lista de Movimentos selecionados na visão, no XML de execução do processo.  Desta forma, não era possível realizar uma validação mais avançada com a utilização de Fórmula Visuais no processo, uma vez que não se conhecia o(s) registro(s) selecionado(s). |
| **Solução/Implementação:** | Adicionado no XML de parâmetros para a execução do processo a Lista de Movimentos com o Código da Coligada (**CodColigada**) e o Identificador do Movimento (**IdMov**) para os registros selecionados na visão. |
| **Conversores e Parâmetros:** | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros do Tipo de Movimento | Etapa Mov - Impressão 2/2 | Marcar o parâmetro **Envia E-mail**. |
| **Tickets relacionados:** | 2000912. |
| **Requisito:** | MATESTCNTFTOF01-1491. |
| **Documento de Referência:** | [Documentos - Fórmula Visual](http://tdn.totvs.com/pages/viewpage.action?pageId=237383316)  [Utilizando a atividade "Transformar registro em XML"](http://tdn.totvs.com/pages/viewpage.action?pageId=287077065) |
