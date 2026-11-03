---
content_hash: 372d48362ee4749fddaf87471ed841b24c49a700ac7b9133cc02aba4294cc96b
fetched_at: '2026-06-29T00:08:54.761886+00:00'
page_id: '346491380'
product: rm
source: tdn-rm
title: 1726266 MATESTCNTFTOF01-1801 DT Campo Complementar Relatório Delphi
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=346491380
version: 3
---

# RELATÓRIO COM CAMPO COMPLEMENTAR DE REPRESENTANTE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Relatório Delphi. |
| **Situação/Requisito:** | Ao criar um relatório simples onde no mesmo possui apenas a tabela de Representantes (TRPR), ao inserir a tabela de Campo Complementar do Representante (TRPRCOMPL) é apresentado o erro: A tabela "Representantes" não referencia a tabela "Dados Complementares de Representante". Provavelmente a tabela master do grupo está configurada incorretamente ou não tem sentido manter estas tabelas no mesmo grupo. |
| **Solução/Implementação:** | Atualizar a tabela de Ligações dos Relatórios, para que seja permitido utilizar os Dados Complementares de Representante com a tabela de Representantes. |
| **Conversores e Parâmetros:** | Versão 12.1.21: o Atualizador de Base de Dados RM irá aplicar o ajuste.  Versões inferiores à 12.1.21: entre em contato com o Suporte TOTVS e solicite a disponibilização do script que atualiza a tabela de Ligações dos Relatórios. Executar o script em uma base de homologação e assim que validados os dados, replicar para produção.  Guia para execução do script: <http://tdn.totvs.com/display/public/rm/Executor+de+Scripts+RM> |
| **Tickets relacionados:** | 1726266. |
| **Requisito:** | Relatórios. |
| **Documento de Referência:** | Não se aplica. |
