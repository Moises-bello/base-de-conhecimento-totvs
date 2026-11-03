---
article_id: 39477405904791
category: Contabilidade Gerencial - Visão Gerencial
content_hash: 2921f424b9c66270fcc9025fe2a9a0f4e36a72ca15e28c8c412868a4ff4b434f
fetched_at: '2026-06-28T22:40:50.690247+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial
  (SIGACTB) - Funcionalidade do campo Coluna na rotina CTBA161
type: support-article
updated_at: '2026-04-02T18:08:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39477405904791-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Contabilidade-Gerencial-SIGACTB-Funcionalidade-do-campo-Coluna-na-rotina-CTBA161
---

**Dúvida**   
Qual é a funcionalidade do campo Coluna na rotina CTBA161 e qual o seu propósito na configuração dos relatórios contábeis?

**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial (SIGACTB) - Versão 12

**Solução**   
A rotina CTBA161 é utilizada para a configuração de Livros Contábeis no módulo de Contabilidade Gerencial (SIGACTB). Ela permite definir a estrutura de impressão e exibição dos livros (como Diário e Razão), determinando quais informações serão apresentadas e em qual formato.

[Cross Segmento - Backoffice Linha Protheus - CTBA130 Relatórios que não são herdadas a visão gerencial atrelada ao Cod. Config.Livro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018525532-Cross-Segmento-Backoffice-Linha-Protheus-CTBA130-Relat%C3%B3rios-que-n%C3%A3o-s%C3%A3o-herdadas-a-vis%C3%A3o-gerencial-atrelada-ao-Cod-Config-Livro)

O campo Coluna, dentro desta rotina, tem a funcionalidade de determinar o posicionamento horizontal no layout de impressão. Ele indica em qual coluna específica da página o valor, a descrição ou o totalizador correspondente àquela linha configurada será impresso. A correta parametrização deste campo garante o alinhamento adequado dos dados gerados no relatório contábil.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39477436525847)

Segue abaixo os relatórios que utilizam essa configuração:

| **Relatório** | **Código da Rotina** | **Finalidade** |
| --- | --- | --- |
| **Balanço Patrimonial** | [`CTBA500`](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-Registro-J100) | Exibe a situação patrimonial da empresa com base na estrutura de ativos, passivos e patrimônio líquido definida na visão. |
| **DRE (Dem. de Resultados)** | [CTBR510](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028247351-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-configurar-o-DRE-registro-J150-da-ECD) | Demonstra a apuração do lucro ou prejuízo, utilizando as amarrações de contas de receita e despesa da visão. |
| **DFC (Fluxo de Caixa)** | [CTBR560](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007113571-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR560-Demonstrativo-Fluxo-de-Caixa-DFC) | Utiliza a visão gerencial para classificar as movimentações financeiras em atividades operacionais, de investimento e financiamento. |
| **DVA (Valor Adicionado)** | `CTBR570` | Gera o demonstrativo de valor adicionado com base na configuração de colunas e linhas da visão. |
| **Relatórios customizados** | [CTBR040](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019129131-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR040-Contas-Dedutoras-antes-e-ap%C3%B3s-Apura%C3%A7%C3%A3o-de-Resultado)  CTBR130 | Relatórios que podem herdar a configuração do código de livro contábil atrelado à visão. |

**Saiba Mais:**

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como importar Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007545672-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-importar-Vis%C3%A3o-Gerencial)

[Visão Gerencial (CTBA161)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001548642-Contabilidade-Gerencial-Vis%C3%A3o-Gerencial)
