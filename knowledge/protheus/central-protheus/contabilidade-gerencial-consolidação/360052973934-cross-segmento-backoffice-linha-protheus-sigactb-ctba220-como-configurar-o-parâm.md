---
article_id: 360052973934
category: Contabilidade Gerencial - Consolidação
content_hash: ee8a76f27cce701fabb32203d25a2eae64e597e5052d328a5d67821adbdf447a
fetched_at: '2026-06-28T22:40:56.787612+00:00'
product: protheus
section_id: 1500001548562
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA220 COMO CONFIGURAR
  O PARÂMETRO MV_CONSOLD
type: support-article
updated_at: '2025-04-28T18:19:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052973934-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA220-COMO-CONFIGURAR-O-PAR%C3%82METRO-MV-CONSOLD
---

**Dúvida**

COMO CONFIGURAR O PARAMETRO MV\_CONSOLD  
  
**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11  
  
**Solução**

Exemplo empresa com Gestão

* Existe duas empresa Grupo T1  e  Grupo T2
* que serão consolidadas Grupo T3
* logado na empresa Grupo T3 , o parametro   MV\_CONSOLD = T3M RJ 01 , foi preenchido com os proprios dados da empresa empresa Grupo T3

1) Grupo T1

2) Grupo T2

3) Criar uma nova empresa : Grupo T3

Empresa 3

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088589973)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088589993)

4) Logado na empresa consolidadora configure o parâmetro MV\_CONSOLD com o código da Empresas destino (que é a própria consolidadora).  
  
Na empresa consolidadora o parâmetro  
  
MV\_CONSOLD = CODIGO GRUPO + CODIGO EMPRESA +UNIDADE DE NEGOCIO + FILIAL  
T3M RJ 01

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087449354)

* Dependendo da configuração do  sigamat  possa ser necessário ter com espaço ou sem espaço entre   CODIGO GRUPO + CODIGO EMPRESA +UNIDADE DE NEGOCIO + FILIAL
* Exemplo :  T3M RJ 01  ou  T3MRJ01 ou T3 M RJ 01

5) Logado na empresa consolidadora realize a consolidação a empresa criada receberá as movimentações registradas nas demais empresas

Obs : Apuração não deve ser realizada nas filiais origens antes de consolidar, caso contrario não será gerado saldo das contas de receita e despesa para a empresa consolidadora 

Caso tenha executada a consolidação com as contas de Receita e Despesa já apuradas na filial Origem [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045923434-MP-SIGACTB-ECD-EMPRESA-CONSOLIDADORA-COMO-GERAR-REGISTROS-I350-I355-I150-I155-?source=search)

Saiba mais :

[Documentação Consolidação - CTBA220 - CTBA231](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014649651-MP-SIGACTB-Documenta%C3%A7%C3%A3o-Consolida%C3%A7%C3%A3o-CTBA220-CTBA231?source=search)

[ECD EMPRESA CONSOLIDADORA COMO GERAR REGISTROS I350 - I355 - I150 - I155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045923434-MP-SIGACTB-ECD-EMPRESA-CONSOLIDADORA-COMO-GERAR-REGISTROS-I350-I355-I150-I155-?source=search)

[CTBA220 CONSOLIDACAO GERAL, HELP: MA280FLOCK USO EXCLUSIVO ALIAS CT1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019474452-MP-SIGACTB-CTBA220-CONSOLIDACAO-GERAL-HELP-MA280FLOCK-USO-EXCLUSIVO-ALIAS-CT1?source=search)

[CTBA220 ERRO NA CHAMADA DO PROCESSO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023000092-MP-SIGACTB-CTBA220-ERRO-NA-CHAMADA-DO-PROCESSO?source=search)

[Documentação Consolidação - CTBA220 - CTBA231](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014649651-MP-SIGACTB-Documenta%C3%A7%C3%A3o-Consolida%C3%A7%C3%A3o-CTBA220-CTBA231?source=search)

[CTBA240 Roteiro Consolidação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015139052-MP-SIGACTB-CTBA240-Roteiro-Consolida%C3%A7%C3%A3o?source=search)
