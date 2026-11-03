---
article_id: 25537037823255
category: SIGAEST - CUSTOS
content_hash: de0091f3cf8729483425565bd1357ca384f0c77c49e92c98e8b1a84ce2c70325
fetched_at: '2026-06-28T22:39:02.230952+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 MATA331 Campo
  Documento CT2_DOC é possível criar para cada item contabilizado?
type: support-article
updated_at: '2025-03-12T12:27:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25537037823255-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-MATA331-Campo-Documento-CT2-DOC-%C3%A9-poss%C3%ADvel-criar-para-cada-item-contabilizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25537048688279) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**

Ao contabilizar pelo Custo Médio (MATA330) ou pela rotina de Contabilização (MATA331) **é gerado um Documento *(CT2\_DOC)* para todo o processamento**, é possível criar um registro de Documento para cada linha de item contabilizado?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque/Custos - Todas as versões

**Solução**

Para esse cenário avalair os parâmetros MV\_NUMLIN e MV\_NUMMAN:

**- [MV\_NUMLIN](https://tdn.totvs.com/x/WJlc) -** Limita o número de linhas por documento em lançamentos contábeis de integração vindo de outros módulos. O limite máximo para o parâmetro é de 35657 linhas

**- [MV\_NUMMAN](https://tdn.totvs.com/x/WZlc) -** Define o número de linhas por documento a ser utilizado para Lançamentos Contábeis Manuais

**- Observação importante:** Avaliar se no momento da Contabilização (MATA331) ou processamento do Recálculo do Custo Médio (MATA330) o parâmetro Mostra lançamento Contábil Estiver igual a Sim e definir 1 documento por linha nos parâmetros, exibirá Documento a Documento podendo comprometer a performance da rotina. Nesse caso, **mantenha essa pergunta igual a Não**. Veja print de exemplo abaixo.

![MATA330 PERGUNTA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/25538554197271)

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGACTB - CTBA105 - MV\_NUMLIN MV\_NUMMAN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006753632-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA105-MV-NUMLIN-MV-NUMMAN?source=search)
