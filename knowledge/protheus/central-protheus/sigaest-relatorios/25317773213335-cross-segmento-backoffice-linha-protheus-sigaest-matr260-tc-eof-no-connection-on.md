---
article_id: 25317773213335
category: SIGAEST - RELATORIOS
content_hash: 3e0916bbc76cb77649cb3690dc69142e6ccedd189df730b2e3dca9995754435f
fetched_at: '2026-06-28T22:39:06.086428+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR260 - TC_Eof -
  NO CONNECTION on TREPORT:PRINTDIALOG(REPORT01.PRW)
type: support-article
updated_at: '2024-07-31T21:09:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25317773213335-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR260-TC-Eof-NO-CONNECTION-on-TREPORT-PRINTDIALOG-REPORT01-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25317773192855) Tempo aproximado para leitura: **00:02:13 min** **Dúvida**

O que fazer quando ocorre o seguinte error.log na geração do relatório Posição de Estoque (MATR260)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Este error.log pode ser exibido por alguns cenários diferentes. Abaixo, listaremos  as principais causas pelo qual o erro pode ser gerado:

- **Existência de caractere(s) especial(is) dentro dos registros da tabela mencionada no error.log**. Isso pode pode ocorrer devido a utilização de um collation não recomendado para uso do DBAccess. Mais detalhes sobre collation's no próximo tópico.

- **Collation do Banco de Dados divergente do Collation sugerido para um banco homologado com o Protheus**. Para conferir os Collations dos Bancos de Dados versus o Collation recomendado para uso do Protheus, veja este artigo: <https://tdn.totvs.com/display/tec/DBAccess+-+Collation%2C+Character+Type+e+Encoding>

Observação: caso tenha dificuldades de identificar o collation do seu banco de dados, recomendamos o acionamento do DBA da empresa responsável, ou caso tenha o banco de dados hospedado no Cloud da TOTVS, acionar a equipe de DBA do Cloud solicitando a informação.

- **Existência de "sujeira" ao final de campos numéricos (casa decimal) da tabela afetada.** Isso pode ocorrer após uma inserção de registro por fora do DBAccess ou em casos de colunas calculadas.

- **DBAccess desatualizado.** É importante manter o DBAccess na sua ultima atualização de forma ao mesmo, junto ao arquivo dbapi.dll, efetuar corretamente as traduções da camada ADVPL para a camada da linguagem do Banco de Dados utilizado para registro dos dados do ambiente.

DBAccess Linux: [Clique aqui para baixar](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/DBAccess_Linux)

DBAccess Windows: [Clique aqui para baixar](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/DBAccess_Windows)

OBS: Sempre atualizar ambientes primeiramente em ambiente de homologação com backup prévio do RPO ou do diretório afetado.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Relatórios no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)
