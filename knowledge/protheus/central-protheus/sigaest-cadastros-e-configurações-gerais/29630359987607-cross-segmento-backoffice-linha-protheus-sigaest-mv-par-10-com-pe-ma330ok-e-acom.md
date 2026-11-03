---
article_id: 29630359987607
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: fc4a62a79f24d6d038a7c92630f6cfef338419401b1455155cd264eb52ebb327
fetched_at: '2026-06-28T22:39:09.655693+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MV_PAR 10 com PE MA330OK
  e Acompanha Custos
type: support-article
updated_at: '2025-03-12T12:23:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29630359987607-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MV-PAR-10-com-PE-MA330OK-e-Acompanha-Custos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29630343242007) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como validar o uso do parametro 10 com o ponto de entrada MA330OK, durante o processamento da rotina MATA038 Acompanha custos?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - A Partir da verão 12.1.2310  
  
**Solução**

Durante o processo de fechamento, as etapas de cálculo de custo e contabilização foram separadas para garantir maior controle e evitar interferências entre os processos. Como parte dessa segregação, o parâmetro **MV\_PAR10 (Gerar Lancto. Contabil ?)** é manipulado exclusivamente na etapa de cálculo, assegurando que não haja impacto na etapa de contabilização.

**Armazenamento de Parâmetros**

O valor definido pelo usuário para o parâmetro **MV\_PAR10** é armazenado no grupo de perguntas **MTA331**. Esse registro pode ser visualizado na tabela **D3Y**, especificamente no campo **D3Y\_STRUCT**, dentro da propriedade: **contabilization > mta331**

**Utilização do Ponto de Entrada**

Para manter a compatibilidade e continuidade do processo, é possível continuar utilizando o mesmo ponto de entrada. Para isso, deve-se utilizar a variável private **OJOURNEYLOG** e a propriedade **CIDPARENT**, permitindo a localização do registro correspondente ao fechamento atual na tabela **D3Y**.

**Considerações Finais**

A separação das etapas de cálculo e contabilização melhora a rastreabilidade e evita inconsistências.

A manipulação do parâmetro **MV\_PAR10** ocorre apenas na etapa de cálculo.

O armazenamento na tabela **D3Y** garante a persistência do dado e possibilita consultas posteriores.

A variável **OJOURNEYLOG** e a propriedade **CIDPARENT** devem ser utilizadas para acessar os registros do fechamento atual.

**Documentação do PE** [MA330OK](https://tdn.totvs.com/x/1uNc)

**Saiba mais:**

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
