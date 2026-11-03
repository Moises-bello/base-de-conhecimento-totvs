---
article_id: 360025693413
category: RH - Contabilização
content_hash: 61c1693a844af3c9f7a451445b5122884450c24ebe28a674211013e39a4281a1
fetched_at: '2026-06-28T22:43:45.984759+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: 'RH - Linha Protheus - GPE - Mensagem: Não existem verbas a serem contabilizadas
  na filial - Verifique se os lançamentos padrões do PCO estão definidos'
type: support-article
updated_at: '2025-07-31T19:05:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025693413-RH-Linha-Protheus-GPE-Mensagem-N%C3%A3o-existem-verbas-a-serem-contabilizadas-na-filial-Verifique-se-os-lan%C3%A7amentos-padr%C3%B5es-do-PCO-est%C3%A3o-definidos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33856738917527)** Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**O que verificar quando apresenta a mensagem: "Não existem verbas a serem contabilizadas na filial - Verifique se os lançamentos padrões do PCO estão definidos"?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Essa mensagem é apresentada, pois o parâmetro MV\_PCOINTE está ativo, embora não utilize o Planejamento de Controle Orçamentário para contabilização da folha:  **![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040536813)**  
1) **Acesse no Configurador:** Base de Dados->Dicionário-> Base de Dados-> Parâmetros   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039703894)

2) Selecione a opção de busca:![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040535473)

3) Digite no campo de busca o nome do parâmetro: **MV\_PCOINTE**  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039704074)  
4) Desabilite o parâmetro , configurando como "2", uma vez que não é utilizado o plano de contas orçamentário na contabilização: ![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039704134)

5) Refaça o processo de contabilização.

**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
