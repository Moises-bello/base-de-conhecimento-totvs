---
article_id: 10085171604247
category: Originação de Grãos (OG)
content_hash: ed0f263637b2ca26a45430b06ee154f21d8890a425bb2ee1bf7d7b0415c1bf36
fetched_at: '2026-06-28T22:45:41.022305+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Moeda Estrangeira no Contrato de Venda - Configuração/Parâmetros
  da Rotina
type: support-article
updated_at: '2025-04-09T12:12:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10085171604247-Agro-Linha-Protheus-AGR-Moeda-Estrangeira-no-Contrato-de-Venda-Configura%C3%A7%C3%A3o-Par%C3%A2metros-da-Rotina
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20417135102103)*** Tempo aproximado para leitura: **00:01:30 min** **Dúvida**  
Em **Moeda Estrangeira no Contrato de Venda**. Quais são os Parâmetros?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Principais parâmetros:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Descrição** | **Conteúdo padrão** | **Conteúdo exigido para esta rotina** |
| [MV\_AGRA001](https://tdn.totvs.com/pages/viewpage.action?pageId=497914828) | Utiliza novo conceito de comercialização do UBA. | .F. | .T. |
| [MV\_AGRO002](https://tdn.totvs.com/pages/viewpage.action?pageId=370616326) | Utiliza novo modelo de comercialização. | .F. | .T. |
| [MV\_AGRO040](https://tdn.totvs.com/pages/viewpage.action?pageId=519202897) | Retira a obrigatoriedade do Registro de Negócio | .F. | .T. |

**Pré-requisitos:**

* Parâmetros [MV\_AGRA001](https://tdn.totvs.com/pages/viewpage.action?pageId=497914828), [MV\_AGRO002](https://tdn.totvs.com/pages/viewpage.action?pageId=370616326) e [MV\_AGRO040](https://tdn.totvs.com/pages/viewpage.action?pageId=519202897) habilitados;
* Possuir os componentes devidamente cadastrados. Necessário ter definido um componente de resultado;
* Cotações cadastradas para o moeda estrangeira;

**OGA410 - Cadastro de Componentes e Preço**

No módulo de Gestão de Agronegócio, acesse no menu **Atualizações > Comercialização > Precificação > Componente de Preço**.

Na imagem abaixo é apresentado um exemplo do cadastro de componentes. É obrigatório ter um componente de preço do tipo resultado.

**OGA490 - Configuração de****Componentes**

No módulo de Gestão de Agronegócio, acesse no menu **Atualizações > Comercialização > Precificação > Configuração de Componentes.**

Para o componente de resultado é obrigatório definir a fórmula de cálculo, ou seja, como o valor final será gerado.

**OGA490 - Configuração de****Componentes**

No módulo de Gestão de Agronegócio, acesse no menu **Atualizações > Comercialização > Precificação > Configuração de Componentes**.

Para o componente de resultado é obrigatório definir a fórmula de cálculo, ou seja, como o valor final será gerado.

![MECV1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10111195754647)
