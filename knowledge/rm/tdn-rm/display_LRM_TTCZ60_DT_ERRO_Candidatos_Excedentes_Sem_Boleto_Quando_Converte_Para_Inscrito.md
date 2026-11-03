---
content_hash: f06295c2d1fd9f14f3e5cc8dbbe940131d0103ce87a1219aa3eec7fa2a57b286
fetched_at: '2026-06-29T00:06:07.869322+00:00'
page_id: '201739511'
product: rm
source: tdn-rm
title: TTCZ60_DT_ERRO_Candidatos_Excedentes_Sem_Boleto_Quando_Converte_Para_Inscrito
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCZ60_DT_ERRO_Candidatos_Excedentes_Sem_Boleto_Quando_Converte_Para_Inscrito
version: 1
---

# CADASTRO DE CANDIDATOS EXCEDENTES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Candidatos Excedentes* |
| **Situação/Requisito:** | *Em um PS marcado para inscrever excedentes, inscrito alguns candidatos como excedente, porem caso depois de ter inscrito os excedentes aumentar o número de vagas na área ofertada, o sistema não gera boleto para os excedentes que conseguiram a vaga. Ao alterar o número de vagas no cadastro de área ofertada o sistema deveria gerar os boletos.* |
| **Solução/Implementação:** | *Implementado método que verifica se existem vagas não preenchidas no registro da área de interesse, e caso existam candidatos excedentes, converte-os para inscritos.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.8* |
