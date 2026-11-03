---
content_hash: 020263cbdd8f60068a482ef7f93c85cff1790956ffef7795b9ad683f2bf3ffa3
fetched_at: '2026-06-29T00:06:03.522142+00:00'
page_id: '198956045'
product: rm
source: tdn-rm
title: TSOC32_DT_Analise_Curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/TSOC32_DT_Analise_Curricular
version: 1
---

# ANÁLISE CURRICULAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Anásile Curricular* |
| **Situação/Requisito:** | *Erro ao acessar analise curricular no EXE ou historico no portal do aluno. Ocorreu um erro ao efetuar a leitura do registro: String or binary data would be truncated. Este erro se dar que ao abrir a análise curricular, onde o sistema tentava copiar os dados do campo SHISTDISCFACEXT.ANOSEMESTREEXT PLETIVO que tem 16 caracteres para o campo SHISTDISCAPROVESTUDOSORIGEM.PLETIVO que possui apenas 10 caracteres.* |
| **Solução/Implementação:** | **Ajuste para o aumento no tamanho do campo SHISTDISCAPROVESTUDOSORIGEM.PLETIVO de 10 para 16 caracteres, campo que recebe os dados do campo SHISTDISCFACEXT.ANOSEMESTREEXT PLETIVO que possui 16 caracteres, para montar a matriz curricular do aluno.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.41* |
