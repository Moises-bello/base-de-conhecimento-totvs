---
article_id: 1500003227881
category: SIGAEST - FECHAMENTO DE ESTOQUE (VIRADA DOS SALDOS)
content_hash: 4de4f50d0c1a545db29d05a16ebd047e376bf480d71704a2fca8a028e1689f7a
fetched_at: '2026-06-28T22:38:52.708787+00:00'
product: protheus
section_id: 1500001538921
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - É possível alterar
  uma Nota Fiscal de Serviço após o Fechamento de Estoque?
type: support-article
updated_at: '2025-03-12T12:27:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003227881-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-alterar-uma-Nota-Fiscal-de-Servi%C3%A7o-ap%C3%B3s-o-Fechamento-de-Estoque
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30504271433367)** Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Após a Virada de Saldos, é possível alterar ou excluir uma NF de Serviço? Pois ela foi feita com TES que não atualiza estoque.  
  
**Ambiente**Microsiga Protheus - Estoque/Custos - A partir da versão 11.80

**Solução**

**Restrição de Alteração de Movimentos de Nota Fiscal em Períodos Encerrados**

Para garantir a segurança e a integridade dos dados no módulo de **Estoque/Custos**, qualquer movimentação relacionada à correção de uma **Nota Fiscal (NF)**, cujo período já tenha sido encerrado, não poderá ser realizada após a **Virada de Saldos**, independentemente do tipo de operação envolvida.

Mesmo nos casos em que determinados movimentos não possuam controle de estoque, existem implicações **legais e fiscais** que inviabilizam a alteração de Notas Fiscais de períodos já fechados. Entre essas implicações, destacam-se:

* **Arquivos fiscais enviados à Receita Federal**
* **Mapas fiscais e demais obrigações acessórias**

Dessa forma, o **Protheus**, em sua configuração padrão, não permite alterações em Notas Fiscais após o encerramento do período. Caso seja necessário realizar qualquer ajuste, a única alternativa disponível é a **reabertura do período correspondente**, não havendo outra opção no padrão do sistema.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Processo de Reabertura de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6420543172247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Processo-de-Reabertura-de-Estoque)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Fechamento de Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012208793-SIGAEST-FECHAMENTO-DE-ESTOQUE-VIRADA-DOS-SALDOS-)
