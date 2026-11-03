---
article_id: 1500004656001
category: SIGAEST - LEGAIS
content_hash: f473db799a03a29d2d143a03b3d837ed3d9539e55acc4849011bb088bb1e9f0d
fetched_at: '2026-06-28T22:38:51.940394+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: MP - SIGAEST - MATR460 - É possível imprimir no relatório P7 apenas produtos
  de Tipos específicos?
type: support-article
updated_at: '2021-04-28T15:12:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004656001-MP-SIGAEST-MATR460-%C3%89-poss%C3%ADvel-imprimir-no-relat%C3%B3rio-P7-apenas-produtos-de-Tipos-espec%C3%ADficos
---

**Dúvida**É possível emitir o relatório P7 (Inventário Mod 7) ignorando ou filtrando apenas tipos de produtos (B1\_TIPO) específicos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**Para este cenário, basta efetuar a personalização do relatório MATR460. Veja abaixo.

No nosso exemplo, **não queremos** que produtos do tipo **MC** sejam considerados na impressão do P7.

No Inventário Mod. 7, clicando em "Personalizar", você consegue fazer o filtro desejado (desconsiderar B1\_TIPO = MC) na impressão. Veja a imagem abaixo de como será feito:

![](https://totvssuporte.zendesk.com/attachments/token/nZ2Co6LDTpQ8YY420IZYnMfAJ/?name=inline565052216.png)

Clicando em Filtro -> Selecione a tabela SB1 -> Campo "Tipo" com a condição **Diferente De** = MC.   
  
Com isso, basta Adicionar, Salvar e dar um OK para tirar o P7 novamente.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre o relatório MATR460 (P7)*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)
