---
article_id: 4418117626391
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 5e7184c40aa59d7f3938f099dd67b6777d7ff893820487ae64c1a3b394bfe030
fetched_at: '2026-06-28T22:39:09.727714+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Qual a finalidade
  do parâmetro MV_ARQPROD?
type: support-article
updated_at: '2023-03-15T13:14:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418117626391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Qual-a-finalidade-do-par%C3%A2metro-MV-ARQPROD
---

**Dúvida**Qual a finalidade do parâmetro MV\_ARQPROD ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões  
  
**Solução**

O parâmetro configura se os dados de indicadores de produto serão considerados pela tabela SB1, ou serão considerados pela da tabela SBZ.

Ao utilizar a tabela de cadastro de produtos **SB1 compartilhada entre Filiais e por exemplo**, precisa que em determinada Filial não utilize o controle de Endereço devem ***habilitar o parâmetro MV\_ARQPROD = SBZ.***

A tabela ***SBZ é exclusiva*** e trata os dados informados na rotina

***[INDICADORES DE PRODUTOS (MATA019)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021908151-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA019-Indicador-de-Produtos) para cada filial como indicado***.

Validar também a configuração do parâmetro MV\_ARQPROP:

Se .F.= Considera o parâmetro MV\_ARQPROD,

Se .T.= Verifica o preenchimento dos campos

Saiba Mais:  
[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
