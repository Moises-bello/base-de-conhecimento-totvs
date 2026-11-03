---
content_hash: ea8cd6e9dbca63c720b7ae008629c75871f15237b7cf6eb16a3d37603125fdbe
fetched_at: '2026-06-29T00:06:09.454778+00:00'
page_id: '203754773'
product: rm
source: tdn-rm
title: TSYTY3_DT_Geracao_Sefip_Campo_CEP_Responsavel
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYTY3_DT_Geracao_Sefip_Campo_CEP_Responsavel
version: 1
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *SEFIP* |
| **Situação/Requisito:** | Na tela de Responsavel na geração do SEFIP, a máscara do CEP só é aplicada após digitarmos o primeiro caractere no campo, fazendo com que o cursor volte para o início, induzindo o usuário ao erro. |
| **Solução/Implementação:** | Foi alterada a tela para aplicar a máscara do CEP assim que a tela fosse carregada pela primeira vez, permitindo que o campo seja preenchido corretamente. |
| **Chamados relacionados:** | TSYTY3 |
| **Versões/Release:** | *11.82.41* |
