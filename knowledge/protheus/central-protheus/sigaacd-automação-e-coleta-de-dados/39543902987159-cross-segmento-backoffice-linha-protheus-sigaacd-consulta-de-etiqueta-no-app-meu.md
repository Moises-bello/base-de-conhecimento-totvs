---
article_id: 39543902987159
category: SIGAACD - Automação e Coleta de Dados
content_hash: 5d13da45e98df1d76f7754e529260444943f7847b4b0075ce324856e4bd21cf7
fetched_at: '2026-06-28T22:39:12.669522+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Consulta de Etiqueta
  no APP Meu Coletor de Dados
type: support-article
updated_at: '2026-05-04T20:23:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39543902987159-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Consulta-de-Etiqueta-no-APP-Meu-Coletor-de-Dados
---

A rotina de Consulta de Etiquetas no aplicativo Meu Coletor de Dados permite consultar saldo e informações de produtos via leitura ou digitação da etiqueta, similar à tecla F4 no Protheus. Disponível a partir da versão 3.1.13, a consulta exige conexão online com o sistema para acessar dados atualizados, não utilizando a tabela de etiquetas (CB0).

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39543934710039) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Como funciona a rotina de **Consulta de Etiqueta** no aplicativo Meu Coletor de Dados e quais são suas principais características?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAACD.

**Solução**

**Veja nosso vídeo instrutivo sobre como realizar  a Consulta de Etiqueta no Meu Coletor de Dados:**

A rotina de Consulta de Etiquetas foi desenvolvida para permitir que os operadores de estoque realizem a consulta de informações de um produto de forma ágil, diretamente pelo aplicativo. A funcionalidade é equivalente à consulta realizada através da tecla F4 na rotina de Cadastro de Produtos (MATA010) no Protheus.

O motivo da rotina se chamar **Consulta de Etiqueta** pois a consulta de saldo de um produto É através da leitura ou digitação de sua etiqueta.

**As principais características da rotina são:**

* **Objetivo:** Consultar o saldo e informações do produto através da leitura ou digitação de sua etiqueta (campos B1\_COD ou B1\_CODBAR).
* **Base de Dados:** A consulta não utiliza a tabela de etiquetas (CB0).
* **Disponibilidade:** A rotina está disponível para uso geral dos clientes a partir da versão **3.1.13** do aplicativo Meu Coletor de Dados.
* Não possui informação no guia de referência do app: <https://tdn.totvs.com/pages/viewpage.action?pageId=506994322>

**Passos**

1. Acesse o aplicativo Meu Coletor de Dados (versão 3.1.13 ou superior) em sua PlayStore.
2. Selecione o menu Consulta de Etiqueta.
3. Realize a leitura do código de barras ou digite o código do produto/EAN.
4. O sistema retornará as informações de saldo e dados do produto conforme configurado no ERP.
5. Detalhes com imagens passo a passo > [Consulta etiqueta](https://tdn.totvs.com/x/1PZ_Pg)

A funcionalidade **Consulta de Etiqueta** requer que o dispositivo coletor esteja conectado online ao sistema de retaguarda no momento da consulta.  
Caso o coletor esteja off-line ou sem comunicação com a retaguarda, a consulta de etiqueta não poderá ser realizada, pois não haverá acesso às informações atualizadas do produto.

**Saiba Mais**

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)  
[*SIGAACD - Quais Coletores de Dados são homologados para uso no módulo Automação e Coleta de Dados (SIGAACD)?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018771512-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Quais-Coletores-de-Dados-s%C3%A3o-homologados-para-uso-no-m%C3%B3dulo-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados-SIGAACD?source=search)  
[*Configurar impressora para impressão de etiquetas*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas)
