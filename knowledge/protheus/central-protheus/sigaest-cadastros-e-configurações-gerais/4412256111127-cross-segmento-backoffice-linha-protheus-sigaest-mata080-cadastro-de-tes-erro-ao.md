---
article_id: 4412256111127
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 64f020b3aaa5cbb3cbcba47ebfb7a2ab98977e65bc7f2c3bb43d65754cdb87e0
fetched_at: '2026-06-28T22:39:07.973825+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -   MATA080 - Cadastro
  de TES - Erro ao alterar o campo Atu.Estoque '
type: support-article
updated_at: '2022-07-01T20:31:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412256111127-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA080-Cadastro-de-TES-Erro-ao-alterar-o-campo-Atu-Estoque
---

**Ocorrência**Erro ao alterar o campo Atu.Estoque - F4\_ESTOQUE de "N - Não" para "S - Sim":

"Este campo não pode ser alterado pois esta TES foi utilizada em registros dos determinados arquivos: SD1"

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**  
Ao alterar o campo F4\_ESTOQUE de uma TES que já foi utilizada anteriormente em alguma emissão de nota, o sistema irá retornar o seguinte help:    
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412239488151/mceclip0.png)  
  
**Solução**

Existem campos dentro do cadastro de TES que, se alterados, podem gerar futuramente saldos incorretos em virtude de rotinas que acertam os saldos (Ex: Refaz Saldos). No caso de estoque, a rotina visualiza a configuração atual do TES, então, num exemplo em que notas que entraram não movimentando o estoque passariam a ter o saldo considerado, porque a configuração atual está para movimentar.

Para contornar essa solução o mais indicado é criar um outro TES com as mesmas configurações, porém movimentando o estoque. E a partir da implantação do saldo de estoque, o novo TES passa a ser utilizado quando necessário.

**Saiba Mais:**  
*[Clique aqui e veja mais artigos sobre Cadastros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
