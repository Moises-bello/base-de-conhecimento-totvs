---
article_id: 4413436322839
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 0915bb5fce1165d8ca9d720706adce0a945813daa4689a0290722def4879b3da
fetched_at: '2026-06-28T22:39:09.758768+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -Quais impactos da alteração
  de tamanho ou decimais em campos do Módulo Estoque/Custos?
type: support-article
updated_at: '2021-11-18T14:15:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413436322839-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-impactos-da-altera%C3%A7%C3%A3o-de-tamanho-ou-decimais-em-campos-do-M%C3%B3dulo-Estoque-Custos
---

**Dúvida**Qual impactos e instruções a TOTVS dá sobre a alteração de tamanho ou decimais para valores diferentes do padrão no Módulo de Estoque/Custos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões  
  
**Solução**

O Protheus permite alteração de diversos campos via Configurador no que se refere à tamanho e decimais, de modo a atender a particularidade de cada cliente e sua regra de negócio. No entanto, não há um mapeamento técnico de impacto do aumento para todos os campos do sistema (os que já possuem foram inseridos em "Grupo de campos" que podem ser consultados via Configurador).

A TOTVS não possui um Documento específico para definição de todas as tabelas/campos que são utilizados em sua rotina, e consequentemente, precisam ser alterados para manter a integridade entre suas Tabelas; pois é relativo à cada Cliente, pontualmente, de acordo com os módulos que estão implantados, as rotinas que são utilizadas, as tabelas que são alimentadas e os campos que são de uso.

Sendo assim, caso realize a implementação / manutenção internamente com sua equipe de TI, ressaltamos a importância de alterar todas as tabelas / campos utilizados na integração de suas rotinas, a fim de não gerar inconsistência em sua base de dados.

**IMPORTANTE:** Qualquer tratamento relacionado a casas decimais é considerado um desvio do Nativo do Protheus. **Portanto, é indicado que qualquer alteração neste sentido seja realizado e documentado por um analista especialista de campo (Consultar diretamente seu Executivo de Soluções de Negócios ESN) para análise e mapeamento pontual de sua base e sua regra de negócio, inclusive para as manutenções dessas alterações nas Tabelas ( já que com as atualizações podem ser criados novos campos e novas tabelas na base).**

Para mais informações sobre aumento de decimais no Protheus, consulte também a documentação: [https://tdn.totvs.com/x/twEmDg](https://tdn.totvs.com/display/PROT/FAT0068_Aumento_de_Casas_Decimais_no_ambiente_Faturamento_SIGAFAT)

Relacionado a Custos, [clique aqui](https://tdn.totvs.com/display/PROT/PEST06012+-+MATA330+-+Como+aumentar+a+quantidade+de+Casas+Decimais+para+os+campos+de+CUSTOS) e veja os principais campos envolvidos.

Sobre as tabelas controle de Endereço e Rastreabilidade, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus?source=search) e veja as principais tabelas envolvidas.

**Saiba Mais:**  
*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
