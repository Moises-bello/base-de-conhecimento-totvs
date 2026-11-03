---
article_id: 39469849585431
category: SIGAACD - Automação e Coleta de Dados
content_hash: af6d96a40ffb1ce77c414a1c57235bad1a8ad2029720a1f18aad77e11d9f6dab
fetched_at: '2026-06-28T22:39:13.908163+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAACD - Customizacao
  de etiqueta ACD
type: support-article
updated_at: '2026-04-02T12:49:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39469849585431-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAACD-Customizacao-de-etiqueta-ACD
---

No sistema TOTVS Backoffice Protheus SIGAACD, para incluir logomarca e ajustar tamanho das etiquetas é necessário customizar via Pontos de Entrada (P.E.), pois não há configuração padrão em tela. Recomenda-se o uso do P.E. CBRETEAN para personalização, ou solicitar desenvolvimento específico. A impressão requer impressoras compatíveis com linguagem vt100 e configuração adequada incluindo cadastro no ACDA060, compilação de RDMakes, parâmetros MV\_IACD01 a MV\_IACD04 e saldo disponível no estoque.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39469816910615) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Como colocar logomarca nas etiquetas e configurar o tamanho delas no sistema? Como customizar a etiqueta padrão?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAACD - Todas as versões

**Solução**

Alterações na estrutura da etiqueta, como a inclusão de logomarca ou ajustes de tamanho específicos, são realizadas mediante customizações ou via Pontos de Entrada (P.E.). **Atualmente não existe uma configuração padrão em tela para o mudança de layout das etiquetas.**

**Layout padrão de acordo rdmakes:**

![padraoetiqueta.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39470034332567)

Para personalizar o corpo da etiqueta, recomenda-se a utilização do P.E. **CBRETEAN(**[**Documentação do PE**](https://tdn.totvs.com/x/HvFc)**)**, que oferece flexibilidade para essa personalização via desenvolvimento. Caso essa opção não atenda às necessidades, existem outras alternativas:

* **Via Processo de Desenvolvimento Participativo:** É possível solicitar ao time de Desenvolvimento a criação de um ponto de entrada exclusivo que atenda os requisitos específicos da empresa, [Saiba mais](https://tdn.totvs.com/pages/releaseview.action?pageId=589518919).
* **Via Central Colaborativa:** Você pode registrar uma sugestão de melhoria nesta plataforma para que a equipe de Produto analise a viabilidade de inclusão da funcionalidade de forma nativa.

Além das opções mencionadas, a configuração para impressão de etiquetas no sistema requer uma impressoras que suportam a linguagem vt100.

**Para que a impressão ocorra corretamente, o processo de configuração inclui:**

1. Realizar o cadastro de locais de impressão na rotina [**ACDA060**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016771731-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-configurar-o-ACD-para-imprimir-etiquetas);
2. Efetuar a compilação de [RDMakes](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1152110) específicos para o modelo de impressora utilizado;
3. Configurar os parâmetros relevantes, como **MV\_IACD01** a **MV\_IACD04**;
4. Garantir que o produto possua registros na tabela **SB2** e saldo disponível no campo **B2\_QATU**, pois a impressão depende da existência de saldo em estoque.

**Saiba Mais:**

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)  
[*SIGAACD - Quais Coletores de Dados são homologados para uso no módulo Automação e Coleta de Dados (SIGAACD)?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018771512-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Quais-Coletores-de-Dados-s%C3%A3o-homologados-para-uso-no-m%C3%B3dulo-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados-SIGAACD?source=search)  
[*Configurar impressora para impressão de etiquetas*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas)
