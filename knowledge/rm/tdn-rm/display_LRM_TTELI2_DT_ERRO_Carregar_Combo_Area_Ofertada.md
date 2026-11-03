---
content_hash: 413343ad93f341fefe8292e32bbf6b2bef3509cc63d9ffd6faf275a95b31a83a
fetched_at: '2026-06-29T00:06:07.689235+00:00'
page_id: '201737094'
product: rm
source: tdn-rm
title: TTELI2_DT_ERRO_Carregar_Combo_Area_Ofertada
type: documentation
url: https://tdn.totvs.com/display/LRM/TTELI2_DT_ERRO_Carregar_Combo_Area_Ofertada
version: 2
---

# ÁREA OFERTADA (PORTAL)

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Àrea Ofertada* |
| **Situação/Requisito:** | *Em um PS que tem somente uma área ofertada e que aceita mais de uma opção de curso, o combobox onde informa a segunda opção só fica mostrando a mensagem que está Carregando, porem devia ficar em branco mostrando que não tem outro curso.* |
| **Solução/Implementação:** | *Ajuste no comportamento do método responsável por preencher os controles das demais áreas ofertada do candidato, quando o processo seletivo possui apenas uma área disponível, o controle está fixando o valor "Carregando dados. Aguarde...".* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.8* |
