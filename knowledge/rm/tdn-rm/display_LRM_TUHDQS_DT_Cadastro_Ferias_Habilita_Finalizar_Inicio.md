---
content_hash: e0091b309bb0ecec1f76a22aed9bb9af0e90d8c718b6f9bb4ee4ee292a45807a
fetched_at: '2026-06-29T00:08:06.957441+00:00'
page_id: '236597586'
product: rm
source: tdn-rm
title: TUHDQS_DT_Cadastro_Ferias_Habilita_Finalizar_Inicio
type: documentation
url: https://tdn.totvs.com/display/LRM/TUHDQS_DT_Cadastro_Ferias_Habilita_Finalizar_Inicio
version: 2
---

# CADASTRO E FÉRIAS HABILITA FINALIZAR NO MÊS DE INÍCIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Férias* |
| **Situação/Requisito:** | *Ao cadastrar férias com periodo de gozo de 01/02/2016 à 01/03/2016 o botão de Finalizar está sendo habilitado no mês de início das Férias, possibilitando assim um lançamento incorreto pelo usuário.*  *Esta inconsistência só ocorre com este periodo de férias, por ser mês de fevereiro em ano bissexto.* |
| **Solução/Implementação:** | *Ajuste no cadastro de férias para somente habilitar o botão Finalizar no mês do fim das férias.*  *Tratamento específico para mês de fevereiro em ano bissexto.* |
| **Chamados   relacionados:** | *TUHDQS, TUVZLC* |
| **Versões/Release:** | *11.82.44, 12.1.12* |
