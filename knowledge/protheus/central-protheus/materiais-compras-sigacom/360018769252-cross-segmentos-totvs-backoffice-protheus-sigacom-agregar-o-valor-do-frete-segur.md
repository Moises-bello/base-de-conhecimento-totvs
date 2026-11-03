---
article_id: 360018769252
category: Materiais - Compras (SIGACOM)
content_hash: 1dac516777edbf772bd1b66866319630096e436da24e43d9b6edbae7b2db52cc
fetched_at: '2026-06-28T22:41:13.109146+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Agregar o valor do
  Frete, Seguro e Despesas nas Notas Fiscais de Entrada de Devolução e de Retorno
  de Mercadorias.
type: support-article
updated_at: '2023-06-02T11:21:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018769252-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Agregar-o-valor-do-Frete-Seguro-e-Despesas-nas-Notas-Fiscais-de-Entrada-de-Devolu%C3%A7%C3%A3o-e-de-Retorno-de-Mercadorias
---

**Dúvida**Configuração para agregar o valor do Frete, Seguro e Despesas as Notas Fiscais de Entrada, de Devolução e de Retorno de Mercadorias.

**Ambiente**

Microsiga Protheus - Compras - a partir da versão P11.80

**Solução**

O parâmetro é composto por 3 posições e deve ser configurado com: “0” (não considera) ou “1” (considera), de acordo com o valor a ser agregado. As posições obedecem a seguinte ordem:

1ª posição = Frete  
2ª posição = Seguro  
3ª posição = Despesas

Exemplos de Configuração:  
a) Agregar somente o Frete Configurar o parâmetro como: 100  
b) Agregar somente o Seguro Configurar o parâmetro como: 010  
c) Agregar somente a Despesa Configurar o parâmetro como: 001  
d) Agregar Frete e Despesa Configurar o parâmetro como: 101  
e) Agregar Tudo Configurar o parâmetro como: 111  
f) Não Agrega Configurar o parâmetro como: 000

Para atender esta necessidade, realize os seguintes passos:

1. Acesse o módulo configurador(SIGACFG);  
2. Acesse o caminho Base de Dados - Dicionário - Base de Dados;  
3. Selecione a opção Parâmetros;  
4. Localize o parâmetro MV\_NFEAFSD e configure conforme acima.

***Saiba Mais :***

[MV\_NFEAFSD - Parâmetro para definir Frete Seguro ou Despesa na Devolução de Vendas](https://tdn.totvs.com/pages/releaseview.action?pageId=237388656)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documento de Entrada - Frete no total da nota de Devolução](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025024033)

[MP - SIGACOM - Pontos de entrada do Documento de Entrada - MATA103](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006469332)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
