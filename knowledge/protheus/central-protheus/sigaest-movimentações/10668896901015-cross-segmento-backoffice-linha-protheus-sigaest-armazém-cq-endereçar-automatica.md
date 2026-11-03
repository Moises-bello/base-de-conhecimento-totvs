---
article_id: 10668896901015
category: SIGAEST - MOVIMENTAÇÕES
content_hash: aff9d1a07ba05ce56b85fa254919455d0915bc737c2edcde751bcfb36e074fa9
fetched_at: '2026-06-28T22:38:54.312356+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Armazém CQ endereçar
  automaticamente - MV_DISTAUT - Como configurar?
type: support-article
updated_at: '2025-09-12T12:06:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10668896901015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Armaz%C3%A9m-CQ-endere%C3%A7ar-automaticamente-MV-DISTAUT-Como-configurar
---

No armazém CQ (MV\_CQ) do TOTVS Protheus, é possível distribuir automaticamente produtos com controle de endereço ao receber, configurando o parâmetro MV\_DISTAUT e criando um endereço padrão na rotina MATA015. Esse processo funciona para um único endereço no armazém CQ. Para armazéns padrão, utiliza-se o parâmetro MV\_DISTMOV. Após liberação no CQ, o endereçamento automático no armazém padrão não é nativo, mas pode ser implementado via MsExecAuto() ou ponto de entrada do MATA175.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34890524060695) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
No armazém CQ (MV\_CQ) produtos que utilizam controle de Endereço é possível distribuir automaticamente ao receber nesse Armazém?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões  
  
**Solução**  
Sim, é possível configurando o parâmetro **MV\_DISTAUT**.

Para solucionar essa dúvida, realize os seguintes passos:

1. Crie um Endereço na rotina MATA015 que será padrão no Armazém de CQ (MV\_CQ) exemplo abaixo;

![ENDERE_O_QUALIDADE.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/10669185646871)

2. No módulo Configurador ajustar o parâmetro como no exemplo abaixo;

![PARAMETRO.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/10669227654679)

3. Após essas configurações as notas de entrada e produções enviadas ao CQ, automaticamente são endereçadas no endereço criado e configurado no parâmetro MV\_DISTAUT.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10669472320791)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10669820388759)

***Obs.:*** Esse processo, funciona apenas para *um endereço* no Armazém de CQ.

Caso desejar o funcionamento semelhante nos Armazéns padrões utilizar o parâmetro MV\_DISTMOV, [clique aqui e veja a FAQ com instruções de funcionamento.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021637231-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-endere%C3%A7ar-Produto-diretamente-da-rotina-de-Documento-de-Entrada-automaticamente-)

**Duvidas frequentes:**

Hoje, após a liberação no CQ, tenho que acessar a rotina Endereçar Produtos (MATA265) para endereçar manualmente no armazém padrão. Existe alguma forma de o sistema já realizar esse endereçamento automático?

R: Atualmente, após o item ser liberado no **CQ (MATA175)** e retornar ao armazém padrão, não há recurso nativo no sistema que realize o endereçamento de forma automática.

Como alternativa, é possível utilizar o recurso **MsExecAuto() da rotina MATA265** ou o **Ponto de Entrada do MATA175**, de forma que o endereçamento seja executado no momento da liberação.

Para análise dessa possibilidade, seguem os links de apoio:

* **Pontos de Entrada MATA175:** [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA175 - Pontos de Entrada da rotina Baixa de CQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004325941-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA175-Pontos-de-Entrada-da-rotina-Baixa-de-CQ)
* **MsExecAuto() - MATA265:** [Documentação oficial](https://tdn.totvs.com/pages/releaseview.action?pageId=6087464)

**Saiba Mais:**  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
