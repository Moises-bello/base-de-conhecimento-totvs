---
article_id: 360062945273
category: SIGAEST - CUSTOS
content_hash: 3d8d1e6249df31a7c9370d68cce5bcf504e0613885e909496c436171541f874e
fetched_at: '2026-06-28T22:39:02.441559+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: 'Cross Segmentos - Backoffice (Linha Protheus) - SIGAEST - Custo em Partes:
  Wizard para Criação dos Campos'
type: support-article
updated_at: '2023-10-16T21:03:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062945273-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAEST-Custo-em-Partes-Wizard-para-Cria%C3%A7%C3%A3o-dos-Campos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18315048036631) Tempo aproximado para leitura: 00:05:00 min**

**Dúvida**

Como criar os campos para uso do conceito de "Custo em Partes" através do Wizard?

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - SIGAEST - A partir da versão 12.1.17

**Solução**

**Procedimento para Implementação:**

**1- Antes de executar Wizard ESTW001 é imprescindível:**

* Realizar o backup da base de dados do produto que será executado o Wizard e dos dicionários de dados SXs.
* Essa rotina deve ser executada em modo exclusivo, ou seja, nenhum usuário deve estar utilizando o sistema.
* Caso houver alguma instância do Protheus em execução o *Wizard* apresentará a seguinte mensagem: "Erro ao abrir o SM0 exclusivo".
* Se os dicionários de dados possuírem índices personalizados (criados pelo usuário), antes de executar o *Wizard*, certifique-se de que estão identificados pelo *nickname*. Caso o *Wizard* necessite criar índices, irá adicioná-los a partir da ordem original instalada pelo Protheus, o que poderá sobrescrever índices personalizados, caso não estejam identificados pelo *nickname*.
* Possuir compilado no Repositório de Objetos o **[Ponto de Entrada MA3310CP](https://tdn.totvs.com/pages/releaseview.action?pageId=6087631)** para definição das regras do Custo em Partes. Caso não houver o Ponto de Entrada compilado o LOG de atualização exibirá a mensagem: "O ponto de entrada MA330CP não está compilado no repositório."

**2 -Em Microsiga Protheus Smartclient, digite U\_ESTW001 e clique em "Ok"**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101322314)

**3 - Após confirmar será apresentada tela com detalhes sobre a atualização do dicionário. Clique em Sim para seguir com a atualização.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002440002)

**4 - Ao final do processamento será apresentado o LOG de atualização. Confirme para finalizar o processo.**

**Observação:** Se os campos forem criados com sucesso, o LOG exibirá o nome das tabelas atualizadas, caso o Wizard não tenha criado os campos ou os mesmos já existirem no ambiente, o LOG não mostrará o nome das tabelas atualizadas.

|  |  |
| --- | --- |
| **Tabelas Atualizadas** | SB2 - Saldos em Estoque |
| SB6 - Saldos em poder de terceiros |
| SB9 - Saldos Iniciais |
| SC2 - Ordens de Produção |
| SD1 - Itens das NFs de Entrada |
| SD2 - Itens das NFs de Saída |
| SD3 - Movimentos Internos |
| SO0 - Saldos Iniciais por OP |

**Saiba mais:**

* *[Wizard para criação dos campos quando utilizado o conceito Custo em Partes](https://tdn.totvs.com/x/Z4U0Fg)*
* *[MP - SIGAEST - Custo em Partes - Conceito e Configuração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062926213-MP-SIGAEST-Custo-em-Partes-Conceito-e-Configura%C3%A7%C3%A3o)*
* *[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)*
