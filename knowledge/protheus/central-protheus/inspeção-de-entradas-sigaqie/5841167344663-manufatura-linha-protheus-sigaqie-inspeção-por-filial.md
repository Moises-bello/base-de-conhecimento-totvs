---
article_id: 5841167344663
category: Inspeção de Entradas (SIGAQIE)
content_hash: 5f7c4f8719976e317203820a43a7e0f4b1cd6c031cc375f65147bf9caf9323f6
fetched_at: '2026-06-28T22:42:27.060869+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Inspeção por filial
type: support-article
updated_at: '2022-05-05T20:02:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5841167344663-Manufatura-Linha-Protheus-SIGAQIE-Inspe%C3%A7%C3%A3o-por-filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20 min** **Dúvida**Como parametrizar o produto para ter inspeção por filial?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**Para que um produto tenha inspeção por filial é necessário que a tabela **SB1 - Descrição Genérica do Produto** esteja em modo **Compartilhada**.  
Neste caso, é possível definir por meio da tabela **SBZ - Indicadores de Produtos** qual indicador no produto será diferente para cada filial.  
Para isto, o parâmetro **MV\_ARQPROD - O parâmetro configura se os dados de indicadores de produto serão considerados pela tabela SB1 ou se serão considerados pela da tabela SBZ** deverá ter o conteúdo igual à **SBZ**, e cadastrar o indicador de produtos na rotina **MATA018 - Indicadores de Produtos**, e definir que por exemplo na filial 01, o campo **BZ\_TIPOCQ - Tipo de CQ** terá conteúdo igual à **Q-SigaQuality** e na filial 02, será como **M-Materiais**.  
Assim, o **Controle de Qualidade** para o módulo **SIGAQIE - Inspeção de Entradas** será apenas na filial 01.  
  
**Saiba mais**  
Além da configuração acima, para o produto que estiver com o campo **BZ\_TIPOCQ** igual à **Q**, deverá também ter os demais cadastros citados no artigo [Manufatura - Linha Protheus - SIGAQIE - Cadastros necessários para integrar com o SIGAQIE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020570212-Manufatura-Linha-Protheus-SIGAQIE-Cadastros-necess%C3%A1rios-para-integrar-com-o-SIGAQIE) para que a integração com o módulo **SIGAQIE** ocorra corretamente.
