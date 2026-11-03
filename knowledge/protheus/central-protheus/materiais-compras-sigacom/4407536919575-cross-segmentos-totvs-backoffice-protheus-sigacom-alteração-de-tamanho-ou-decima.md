---
article_id: 4407536919575
category: Materiais - Compras (SIGACOM)
content_hash: d2bafdbabb67f39baed7826a8a02426c592bf2b65d21463e12bca01bbc1760f1
fetched_at: '2026-06-28T22:41:13.129894+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Alteração de Tamanho
  ou Decimais em campos do Módulo COMPRAS
type: support-article
updated_at: '2022-05-16T22:53:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407536919575-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Altera%C3%A7%C3%A3o-de-Tamanho-ou-Decimais-em-campos-do-M%C3%B3dulo-COMPRAS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**  
Orientação referente Alteração de Tamanho ou Decimais para valores diferentes do padrão no Módulo de COMPRAS  
  
**Ambiente**

Cross Segmento - Totvs Backoffice Protheus – Compras – A partir da versão 11.80  
  
**Solução**O sistema Protheus permite alteração de diversos campos via Configurador no que se refere à tamanho e decimais, de modo a atender a particularidade de cada cliente e sua regra de negócio. No entanto, não há um mapeamento técnico de impacto do aumento para todos os campos do sistema (os que já possuem foram inseridos em "Grupo de campos" que podem ser consultados via Configurador).

A TOTVS não possui um Documento específico para definição de todas as tabelas/campos que são utilizados em sua rotina, e consequentemente, precisam ser alterados para manter a integridade entre suas Tabelas; pois é relativo à cada Cliente, pontualmente, de acordo com os módulos que estão implantados, as rotinas que são utilizadas, as tabelas que são alimentadas e os campos que são de uso.

Sendo assim, caso realize a implementação/ manutenção internamente com sua equipe de TI, ressaltamos a importância de alterar todas as tabelas/ campos utilizados na integração de suas rotinas; a fim de não gerar inconsistência em sua base de dados.

**IMPORTANTE:** Qualquer tratamento relacionado a casas decimais é considerado um desvio do Nativo do Protheus. Portanto, é indicado que qualquer alteração neste sentido seja realizado e documentado por um analista in loco (Consultar diretamente seu ESN) para análise e mapeamento pontual de sua base/ seu cenário, inclusive para as manutenções dessas alterações nas Tabelas (já que com as atualizações podem ser criados novos campos e novas tabelas na base).

Para mais informações sobre aumento de decimais no Protheus, consulte a documentação: <https://tdn.totvs.com/x/twEmDg>

***Saiba Mais :***

[MP - SIGACOM - Pontos de Entrada - Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000169747)

[FAT0068\_Aumento\_de\_Casas\_Decimais\_no\_ambiente\_Faturamento\_SIGAFAT](https://tdn.totvs.com/display/public/PROT/FAT0068_Aumento_de_Casas_Decimais_no_ambiente_Faturamento_SIGAFAT)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
