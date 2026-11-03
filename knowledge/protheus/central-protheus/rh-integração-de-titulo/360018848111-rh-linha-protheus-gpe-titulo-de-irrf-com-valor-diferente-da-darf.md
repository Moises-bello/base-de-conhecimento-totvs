---
article_id: 360018848111
category: RH - Integração de Titulo
content_hash: 57c7b17acd3fb23fc2852c2367937524a0a0ef389ac5fc8749e4f366d432faf8
fetched_at: '2026-06-28T22:43:36.139458+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE -  Titulo de IRRF com valor diferente da DARF
type: support-article
updated_at: '2025-07-18T13:48:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018848111-RH-Linha-Protheus-GPE-Titulo-de-IRRF-com-valor-diferente-da-DARF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33558177141527)**Tempo aproximado para leitura: 00:03:00 min

**Ocorrência**Titulo de IRRF com valor diferente da DARF, o que verificar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Esse incidente ocorre, pois está errada a  parametrização de Definição do Título de Férias e Rescisão.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** No ambiente Gestão de Pessoal, opção**Miscelânea>Títulos>Definição,** selecione ou inclua o Título de Férias e Rescisão.  
  
Importante!  Ao incluir um título onde deverá buscar a data de vencimento do próprio cálculo, não preencha as informações relacionadas ao vencimento do título na tela inicial das definições deste título.

**2.** Na área **Títulos disponíveis para seleção**, selecione a opção **definido pelo usuário**” e clique em **Definir Título.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014335892)

**3**. O sistema apresenta a tela para definição das regras para geração do título:

No campo **Verbas Disponíveis para Seleção**, localize a(s) verba(s) que será considerada na geração do título, clique na seta > para que fique no quadro **Verbas Selecionadas para a Geração,**no campo **Informações para busca das verbas selecionadas** clique em **Editar.**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014336472)**

**4**. Pesquise a tabela **SRR** e clique em **Salvar**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014339371)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014336872)

**5.** Para tratar a data de vencimento, clique em **Outras Ações>Informações para busca data de****vencimento.**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014339691)

**6.** Selecione o **Campo Data para Vencto e****Campo Data que relaciona o arquivo Atual ao Arquivo SRR (RR\_DATA)** e clique em **Salvar.**

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014337012)

**7.** Desta forma, quando gerar um título de férias ou de rescisão, obedecerá às datas de pagamento do cálculo.  
  
**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
