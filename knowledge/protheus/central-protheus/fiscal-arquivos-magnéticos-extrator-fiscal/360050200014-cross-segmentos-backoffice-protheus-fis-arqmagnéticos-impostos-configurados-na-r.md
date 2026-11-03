---
article_id: 360050200014
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: b42c1094365b8751b8067a961c7398ddb0eec19ebb684a72806e7377ff37efa8
fetched_at: '2026-06-28T22:42:07.819601+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Impostos Configurados
  na Rotina de Configurador de Tributos não Estão Sendo Integrados no TAF
type: support-article
updated_at: '2025-04-03T17:55:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050200014-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Impostos-Configurados-na-Rotina-de-Configurador-de-Tributos-n%C3%A3o-Est%C3%A3o-Sendo-Integrados-no-TAF
---

**Dúvida**  
Impostos Configurados na Rotina de Configurador de Tributos não Estão Sendo Integrados no TAF  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Os impostos configurados na rotina do Configurador de Tributos é integrado ao TAF através da execução do Extrator Fiscal.  
  
Para que os impostos sejam gravados na integração com o TAF deverão estar vinculado com o ID TOTVS no cadastro do Tributo corretamente.  
  
Abaixo documentação referente o configurador de tributos contendo informações sobre o ID Totvs:   
  
<https://tdn.totvs.com/display/public/PROT/FIS0095_Configurador_de_Tributos>  
  
Seção **Identificador - ID TOTVS:**  
  
**Id. Tributo**= Neste campo preenchemos o código que identifica o tributo genérico, chamaremos este código de ID TOTVS.  
  
O conceito do ID TOTVS é que seja possível a identificação de um tributo genérico, trata-se de um ID com numeração fixa e gerada de forma automática pela sistema. Basicamente este ID faz o chamado “De Para” de um tributo genérico que possui código aleatório definido pelo usuário com um tributo real e conhecido.  
Somente preencha este campo quando for necessário demonstrar o valor do tributo genérico em alguma obrigação acessória, como por exemplo o SPED Fiscal, caso contrário não há necessidade de preenchimento.  
   
Os tributos são calculados e gravados na tabela F2D - (Tributos Genéricos Calculados) através do campo F2D\_TRIB com o código do tributo corretamente, o Extrator faz a ligação dos códigos para descobrir qual é o tributo, feita a gravação, busca as informações desta tabela para levar para o TAF.   
   
O conteúdo do campo F2D\_TRIB deverá ser igual o conteúdo do campo da F2B - (Regra Tributária).  
  
Na tabela F2D terá o código da regra (F2B), não terá do tributo pai F2E - (Cadastro de Tributo) Através do código da regra é possível chegar no código do tributo pai.

**Sobre o compartilhamento das tabelas F2B e F2D:**

A tabela F2D grava o documento fiscal que obteve o calculo referente os tributos configurados na rotina FISA170 - Configurador e Tributos. (Tratamento semelhante a gravação da tabela SFT).  
  
A tabela F2D deve estar cadastrada como exclusiva, pois o vinculo é feito por documento fiscal.

A tabela F2B é a tabela de regras e a rotina FISA170 possibilita que seja configurado uma regra de cálculo para várias filiais, portanto a mesma pode ser cadastrada como compartilhada.   
  
Abaixo link contendo documentação na integra referente a rotina de Configurador de Tributos:

<https://tdn.totvs.com/display/public/PROT/FIS0095_Configurador_de_Tributos>
