---
article_id: 360036517133
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 8f4fbc93f9f0055caa73e5e70cc6e1c7547c6e5b442236db8f51e4312c0a5a05
fetched_at: '2026-06-28T22:37:21.731368+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Dashboard de Contratos
type: support-article
updated_at: '2026-05-11T20:08:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036517133-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Dashboard-de-Contratos
---

O Dashboard de contratos é um produto que tem por objetivo simplificar o processo de gestão de contratos. Construído em parceria com o UX Lab TOTVS, o produto apresenta uma interface mais limpa e intuitiva desenvolvida com o TOTVS HTML Framework.

É compatível com o módulo Gestão de Contratos, não sendo necessário nenhum processo de migração.

Visão do Painel Geral de Contratos:

![image2019-8-15_14-13-58.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047076794)

**Pré-requisitos:**

Para utilizar o dashboard de contratos os requisitos são:

* Protheus versão 12.1.23 ou superior
* Binário lobo-guará
* SmartClient versão 17.3.0.7 ou superior
* Application Server versão 17.3.0.13 ou superior
* Lib: versão 20190705 ou superior
* Web Service Rest configurado
* Licença TOTVS l

Abaixo em "***Saiba Mais***" contém mais informações sobre o processo, lembrando que para o correto funcionamento do Dashboard de Contratos deve estar com o REST  "ativo" ou "no Ar" para o Protheus em questão.

Para dúvidas nas configurações de REST, orientamos o contato junto ao Suporte Framework que presta suporte a esta ferramenta do Protheus.

**Obs1:**

Devido a Tecnologia utilizada POUI, o Portal de Contratos não considera os metadados do Dicionário de dados(SX3), as alterações realizadas no dicionário, como por exemplo aumento de tamanho de campo , dessa forma só funciona com os tamanhos disponibilizados no padrão do sistema.

**Obs2:**

Da mesma forma, devido a tecnologia POUI na qual está embarcada a rotina de Dashboard de Contratos, a utilização de Inicializadores Padrão no Dicionário de Dados, não possui funcionalidade na inclusão de Contratos através da rotina de Dashboard de Contratos, e neste caso recomenda-se a inclusão do contrato pela rotina Manutenção de Contratos (CNTA300).

**Obs3:**

Atualmente a rotina de Dashboard de Contratos não possui Pontos de Entrada disponíveis, para possibilidade de customizações em seu processo ou em sua tela.

**Obs4:**

Ao alterar a empresa ou filial, os dados não são carregados conforme a filial selecionada.  
Foi removido as opções de filtro de seleção de empresas/filiais, visto que não existia esta opção configurada para o projeto padrão.

Veja mais no documento técnico do produto: [Ao alterar a empresa ou filial, os dados não são carregados](https://tdn.totvs.com/pages/releaseview.action?pageId=965452253)

***Saiba Mais:***

[Dashboard de Contratos](https://tdn.totvs.com/x/0kw4Hg)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
