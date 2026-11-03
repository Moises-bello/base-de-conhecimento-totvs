---
article_id: 23087787215511
category: eSocial - Tabelas/Não Periódicos
content_hash: 6c7fa914b18281396a65116cbfbc11e32454cfb161e1ad063fb08efbcb189364
fetched_at: '2026-06-28T22:47:10.437403+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Erro na validação do campo 'racaCor'
type: support-article
updated_at: '2024-10-04T14:04:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23087787215511-RH-RM-FOP-eSocial-Erro-na-valida%C3%A7%C3%A3o-do-campo-racaCor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23087787188119) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**Erro na validação do campo 'racaCor': Se dtAdm, dtExercicio, sucessaoVinc/dtTransf ou transfDom/dtTransf (maior data entre elas) for igual ou posterior a [2024-04-22], não pode ser informado o valor [6].  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões

**Causa**

A mensagem de erro ocorre quando esta sendo informado no arquivo XML a Tag 'racaCor' com o código 6:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23087778069527)

Sendo a Data de Admissão, Data da entrada em exercício pelo servidor ou Data da transferência do empregado para o empregador declarante igual ou posterior a [2024-04-22], não pode ser informado o valor [6].

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23087787198487)

**Solução**Para correção da ocorrência será necessario acessar o cadastro do funcionário **Administração de Pessoal | Funcionários| Identificação | Cor Raça** e ajustar para uma descrição valida para o eSocial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23087787200023)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23087778075799)
