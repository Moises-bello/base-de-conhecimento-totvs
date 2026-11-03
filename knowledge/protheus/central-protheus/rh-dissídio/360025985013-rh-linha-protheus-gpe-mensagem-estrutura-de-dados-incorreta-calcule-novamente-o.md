---
article_id: 360025985013
category: RH - Dissídio
content_hash: 3528e40d1ec9db44801945b23305e4db363d2d3c717ea9f1228d9c3e610b3dc9
fetched_at: '2026-06-28T22:43:43.164164+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE -  Mensagem "Estrutura de dados incorreta. Calcule
  novamente o dissidio."
type: support-article
updated_at: '2025-05-22T13:55:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025985013-RH-Linha-Protheus-GPE-Mensagem-Estrutura-de-dados-incorreta-Calcule-novamente-o-dissidio
---

**Ocorrência**No módulo Gestão de Pessoal, ao executar a geração do do dissídio é apresentada  a mensagem "Estrutura de dados incorreta. Calcule novamente o dissidio."  
  
**Ambiente**Microsiga Protheus – Gestão de Pessoal – A partir da versão 11.80  
  
**Causa**Esta mensagem é apresentada em duas situações:

1 - quando existem registros na RHH com o campo **RHH\_MESANO com 0 ou em branco**. Estes registros são visualizados pelo banco de dados ou via Consulta Genérica desde que a tabela esteja no menu;

2 - quando existem linhas em branco na tabela RHH;  
  
**Solução**1 - No banco de dados, realize uma query para localizar registros com o campo RHH\_MESANO em branco ou com conteúdo 0 e realize a manutenção.  Pela Consulta Genérica poderá ser verificado no caminho Consultas> Cadastros> Genéricos;

2 - No banco de dados, abra a tabela RHH e verifique se existem linhas em branco, realize a manutenção.  Pela Consulta Genérica poderá ser verificado no caminho Consultas> Cadastros> Genéricos;

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Manual dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034578653-RH-Linha-Protheus-GPE-Manual-diss%C3%ADdio-retroativo-?source=search)
