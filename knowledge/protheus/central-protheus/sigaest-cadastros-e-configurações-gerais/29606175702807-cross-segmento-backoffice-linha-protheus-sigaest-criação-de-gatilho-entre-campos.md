---
article_id: 29606175702807
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 6467ed041358548fa9ec820beb7fdb881712cd438b853784bdb06dda62039cc4
fetched_at: '2026-06-28T22:39:08.186681+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Criação de gatilho
  entre campos da mesma tabela
type: support-article
updated_at: '2025-03-12T12:22:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29606175702807-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Cria%C3%A7%C3%A3o-de-gatilho-entre-campos-da-mesma-tabela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29606166964887) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como criar um gatilho para levar uma informação de um campo à outro da mesma tabela?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Solução**Primeiramente é necessário definir de qual campo a informação partirá e para qual campo ela será levada, pois os campos precisam ser do mesmo tipo e precisam possuir tamanho compatível.

No teste abaixo criamos um campo de usuário chamado "Custom UM" (B1\_XUM), que deverá receber o conteúdo do campo padrão "Unidade de Medida" (B1\_UM):

![Gatilho 01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29606175648791)

Agora acessamos o módulo Configurador (SIGACFG) e acessamos o menu "Base de Dados", depois "Dicionário" e depois "Gatilhos", onde podem ser visualizados todos os gatilhos do sistema:

![Gatilho 02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29606166972439)

Em seguida vamos incluir um novo gatilho (através da opção em destaque na imagem abaixo) e faremos o preenchimento:

* Campo: Campo de Origem do Dado
* Cnt. Dominio: Campo que receberá a informação
* Regra: Regra para preenchimento

Caso necessite de mais informações sobre os demais campos desta tela acesse:

[Gatilhos (CFGX037 - SIGACFG)](https://tdn.totvs.com/x/uiWbEg)

![Gatilho 03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29606175663383)

Ao salva o gatilho criado basta acessar a rotina e verificar que a informação inserida em um campo, assim que concluir a inserção saindo do campo, será gatilhada para o outro campo:

![Gatilho 04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29606175669399)

Saiba mais:

* [Criação de gatilho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021876611-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cria%C3%A7%C3%A3o-de-gatilho)
* [Como criar um gatilho em MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051029514-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-criar-um-gatilho-em-MVC)
* [Retirar o gatilho (SX7) de uma rotina MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020439811-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Retirar-o-gatilho-SX7-de-uma-rotina-MVC)
* [Gatilho entre tabelas em rotina mvc](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018867011-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Gatilho-entre-tabelas-em-rotina-mvc)
* [Como utilizar gatilhos para preenchimento dos campos em rotinas MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018580812-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-utilizar-gatilhos-para-preenchimento-dos-campos-em-rotinas-MVC)
* [Retornar o campo que esta sendo alterado em rotina MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019002512-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Retornar-o-campo-que-esta-sendo-alterado-em-rotina-MVC)
* [Gatilho do cabeçalho para o item na rotina MATA415](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025839851-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Gatilho-do-cabe%C3%A7alho-para-o-item-na-rotina-MATA415)
* [Execução de Gatilho sem a necessidade de enter no campo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019797791-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Execu%C3%A7%C3%A3o-de-Gatilho-sem-a-necessidade-de-enter-no-campo)
* [Instrução não cabe no campo do gatilho ou formulas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020884771-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Instru%C3%A7%C3%A3o-n%C3%A3o-cabe-no-campo-do-gatilho-ou-formulas)
* [Criando gatilho com User Function para validar a execução em rotina especifica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021541971-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Criando-gatilho-com-User-Function-para-validar-a-execu%C3%A7%C3%A3o-em-rotina-especifica)
