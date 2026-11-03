---
article_id: 360018059072
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b4c78e8181d1e17c98759bceea5903ed86f6c2b557ac057d84f42e6c9f170a33
fetched_at: '2026-06-28T22:38:31.290199+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Mensagem A261NONNR ao gerar Doc de Saída
type: support-article
updated_at: '2021-04-28T15:55:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018059072-MP-FAT-Mensagem-A261NONNR-ao-gerar-Doc-de-Sa%C3%ADda
---

**Dúvida**

Ao preparar um documento de saída sistema exibe o Help **A261NONNR** e não fatura.   
   
 **Ambiente**

Microsiga Protheus - a partir da versão 11.

**Solução**

Essa mensagem ocorre quando não ha registro do armazém na tabela de "Cadastro de Armazéns (NNR)".

Esta ocorrência somente acontece quando os parâmetros **MV\_CONTERC** / **MV\_ALMTERC** estão habilitados em sua base de dados, abaixo segue o resumo sobre a funcionalidade destes parâmetros:

No processo de controle de material em poder de terceiros, o parâmetro “MV\_CONTERC”, possui a finalidade de ativar o controle do armazém de poder de terceiros, estabelecendo que todo o material enviado para poder de terceiros, seja transferido para o armazém de transito definido no parâmetro.”MV\_ALMTERC”, para que o sistema possa controlar o custo médio do produto que está em poder de terceiros, apurando o valor do custo desses produtos através do custo médio atual.

Para solucionar a ocorrência do help "A261NONNR" verifique se o armazém informado no parâmetro MV\_ALMTERC existe na tabela **NNR** ou acesse o cadastro de armazéns "**AGRA045**"

SAIBA MAIS: **[Mensagem\_A261NONNR \_ao\_gerar\_Doc\_de\_Saida](http://tdn.totvs.com/display/PROT/FAT0193_Mensagem_A261NONNR+_ao_gerar_Doc_de_Saida)**
