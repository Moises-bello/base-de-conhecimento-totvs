---
article_id: 1500003151782
category: Materiais - Compras (SIGACOM)
content_hash: dc22bd12cdabf0735c130e8f7cad1be0258d2ee7f0e1af0df6a4537a7232d8fa
fetched_at: '2026-06-28T22:41:15.929789+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como importar o valor
  do Frete, Seguro e Despesas nas Notas Fiscais de Devolução/Retorno de Mercadorias
  (MATA103)?
type: support-article
updated_at: '2022-05-16T21:23:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003151782-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-importar-o-valor-do-Frete-Seguro-e-Despesas-nas-Notas-Fiscais-de-Devolu%C3%A7%C3%A3o-Retorno-de-Mercadorias-MATA103
---

**Dúvida**Qual configuração para trazer o valor do Frete, Seguro e Despesas as Notas Fiscais de Entrada, de Devolução e de Retorno de Mercadorias ?  
  
**Ambiente**Protheus – Compras – A partir da ver 12  
  
**Solução**

Para trazer ou não o frete que foi inserido na NF de saída, nas Notas Fiscais de Entrada de Devolução e de Retorno de Mercadorias pode ser configurado o parâmetro **MV\_NFEAFSD**.

Ele é composto por 3 posições e deve ser configurado com: “0” (não considera) ou “1” (considera), de acordo com o valor a ser agregado. As posições obedecem a seguinte ordem:

1ª posição = Frete  
2ª posição = Seguro  
3ª posição = Despesas

***Exemplos de Configuração:***  
a) Agregar somente o Frete Configurar o parâmetro como: 100  
b) Agregar somente o Seguro Configurar o parâmetro como: 010  
c) Agregar somente a Despesa Configurar o parâmetro como: 001  
d) Agregar Frete e Despesa Configurar o parâmetro como: 101  
e) Agregar Tudo Configurar o parâmetro como: 111  
f) Não Agrega Configurar o parâmetro como: 000

Para atender esta necessidade, realize os seguintes passos:

1. Acesse o módulo configurador (SIGACFG);  
2. Acesse o caminho Base de Dados - Dicionário - Base de Dados;  
3. Selecione a opção Parâmetros;  
4. Localize o parâmetro ***MV\_NFEAFSD*** e configure conforme a opções acima.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
