---
content_hash: e290f78a9a3a59c6287553cd64ab30ead6bc2cf6a9241ba0b9943a22a2bfd567
fetched_at: '2026-06-29T00:08:54.857704+00:00'
page_id: '346500862'
product: rm
source: tdn-rm
title: RMFIS00002_REINF R-1070 - Tabela de Processos Administrativos/Judiciais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=346500862
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal x TAF Totvs Automação Fiscal |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Evento R-1070 - Tabela de Processos Administrativos/Judiciais |
| **Ambiente:** |  |
| **Passo a passo:** | Neste evento devem ser informados os Processos Judiciais e Administrativos que influenciam na apuração dos tributos **e somente aqueles que possuem decisão favorável ao contribuinte**, tanto aqueles de autoria do próprio declarando como o de terceiros que afetem a retenção do tributo.  Quando o processo ainda não estiver transitado em julgamento, o valor do imposto deve ser informado como devido e o valor discutido como suspenso. Durante o andamento do trâmite, o evento deve ser alterado informando o fim da validade da informação anterior e informando o início da validade da nova informação.  As informações desse registro são provenientes do Cadastro de Processo Judicial/Administrativo, desde que ele esteja associado em algum Lançamento Fiscal.  Estas informações são enviadas para o TAF através do Registro T001AB do Layout TAF. Uma vez enviado com sucesso o registro não será mais enviado, a não ser quando algum campo que é controlado pelo [Log de Alterações](http://tdn.totvs.com/display/LRM/FISCAL01-911+DT+REINF+-+Log+Processo+Judicial) for alterado. Neste caso, o registro deve ser reenviado para o TAF para posterior envio ao Fisco.    **IMPORTANTE!** O TAF guarda as informações dos processos por Filial. Portanto, quando um mesmo Processo for referenciado em Lançamentos de mais de uma Filial, ao processar a integração das Filiais, marque o parâmetro "**Gerar Processo Judicial/Administrativo obrigatoriamente**" que está na aba Demais Parâmetros 3 do Processo de Geração dos Registros. |
| **Observações:** | Video do Processo: [HOW TO - TAF - Apurações para geração de XML´s REINF - R1000 e R1070](https://youtu.be/7LWKImXXMQw) |
