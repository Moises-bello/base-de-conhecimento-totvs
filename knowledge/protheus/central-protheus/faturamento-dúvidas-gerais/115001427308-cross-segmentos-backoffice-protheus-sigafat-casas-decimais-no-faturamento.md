---
article_id: 115001427308
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 686120dd5717dda86082275a03ccd06f9ccc68cec353557dfc7ae6283693ff37
fetched_at: '2026-06-28T22:38:28.783964+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Casas decimais no Faturamento
type: support-article
updated_at: '2025-10-14T14:13:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001427308-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Casas-decimais-no-Faturamento
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35488274204951) Tempo aproximado para leitura: **00:03:00 min******

**Dúvida**

Como efetuar o aumento de casas decimais no Protheus ou quais as inconsistências relacionadas à alteração?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

O aumento de casas decimais no Protheus é uma questão delicada. Quando realizado sem os devidos critérios ou não recebe a devida manutenção, estas alterações podem impactar em:

* Perda de casas decimais finais em cálculos encadeados;
* Valores divergentes entre Itens do Pedido (SC6), Liberações de itens (SC9) e Documento de Saída (SD2);
* Cálculos incorretos que podem atribuir desconto/acréscimo indevido;
* Alertas que impedem o processo (A410UNIDIF, A100VALOR, A410TOTAL, A415TOTAL).

Importante ressaltar que qualquer tratamento relacionado a casas decimais é considerado um desvio do Nativo do Protheus.  
Portanto, é **altamente** **indicado** que qualquer alteração neste sentido seja realizado e documentado por um **especialista técnico do serviço** (Consultar diretamente seu ESN) mediante análise do cenário e validação completa da base de dados.

**Procedimentos recomendados:**

1 - Utilizar o recurso de **Grupos de Campos Numéricos** para realizar ajustes de tamanho e casas decimais, essa ferramenta garante a padronização entre as tabelas envolvidas;

2 - Validar o processo em ambiente de homologação;

3 - Documentar alterações realizadas, registrando os campos, tabelas e novos tamanhos/decimais definidos, para controle e rastreabilidade;

4 - Efetuar backup da base antes da aplicação em produção.

**Saiba mais**:

* **[Grupo de Campos Numéricos](https://tdn.totvs.com/x/JVo9L)**
* [**How To | MP - SIGAFAT - Grupos de Campos Numéricos**](https://www.youtube.com/watch?v=BXPL4BPr668)
* **[Aumento de Casas Decimais no ambiente Faturamento SIGAFAT](https://tdn.totvs.com/x/twEmDg)**
