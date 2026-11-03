---
article_id: 18897439300631
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 1002f5447c7499d33cf142bf1ced3b6889ea10f2b6b3a3637554aed13ae4f037
fetched_at: '2026-06-28T22:39:09.630377+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA180 - Validação
  de campos de medidas de comprimento e peso no Complemento do Produto
type: support-article
updated_at: '2023-12-11T18:46:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18897439300631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA180-Valida%C3%A7%C3%A3o-de-campos-de-medidas-de-comprimento-e-peso-no-Complemento-do-Produto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18897430948119) Tempo aproximado para leitura: **00:01:10 min** **Dúvida**Os campos no SB5 referentes a medidas de comprimento são em metros ou centímetros?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Nesta documentação vamos destrinchar todos os campos que podem gerar duvidas sobre como é a medida de comprimento deles:

Campos **B5\_COMPR, B5\_ESPESS, B5\_ALTURA e B5\_LARG**: Estes 4 campos não têm validação de metros ou centímetros, isso vai depender do viés que o cliente vai utilizar esse campo.  
   
Campos **B5\_ECCOMP, B5\_ECLARGU e B5\_ECPROFU:** Estes campos são específicos para integrações mesmo, e todos eles são **em metros**:

Campos **B5\_COMPRLC, B5\_LARGLC e B5\_ALTURLC:** Estes campos não tem validação de metros ou centímetros, mas eles são confrontados com a capacidade do Endereço Físico (MATA015) para produtos que possuem este controle. Temos detalhes deste cenário na documentação: [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação do Help MA265CAPAC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403501623703-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-Help-MA265CAPAC-)

Campos **B5\_PESO e B5\_PESOBRU**: Não existe um peso padrão para os campos. Normalmente eles são consumidos na venda, mas não tem um caráter informativo do tipo do peso (Kilo, Gramas, etc).

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)

*[**Peso, Volume e Espécie** no Pedido de Vendas e Documento de Saída](http://tdn.totvs.com/pages/releaseview.action?pageId=225264487)*
