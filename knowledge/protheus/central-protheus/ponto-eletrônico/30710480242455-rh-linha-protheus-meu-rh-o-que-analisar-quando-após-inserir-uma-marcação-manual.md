---
article_id: 30710480242455
category: PONTO ELETRÔNICO
content_hash: 38e97d2f03ab9810b4291af24b1a6096d864f85f520c5a5a774cf5f4d00a2f7e
fetched_at: '2026-06-28T22:44:36.461328+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - O que analisar quando após inserir uma marcação
  manual, esta não é demonstrada no Espelho de Ponto
type: support-article
updated_at: '2026-06-23T21:07:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30710480242455-RH-Linha-Protheus-Meu-RH-O-que-analisar-quando-ap%C3%B3s-inserir-uma-marca%C3%A7%C3%A3o-manual-esta-n%C3%A3o-%C3%A9-demonstrada-no-Espelho-de-Ponto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30710480213015) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**O que analisar quando após inserir uma marcação manual, esta não é demonstrada no Espelho de Ponto no Meu RH  
  
**Ambiente**TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**Esta inconsistência ocorre, pois na **Tabela de Horário Padrão** vinculada ao Turno de Trabalho deste funcionário, está preenchida de forma incorreta.  
  
Tendo na imagem abaixo como exemplo, um funcionário com horário comercial:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30710480213399)

* **todos os dias, inclusive sábado e domingo** precisam estar preenchidos
* Limite inferior 8,00 em todos os dias, pois das 00:00 (primeiro minuto do dia) até as 08:00 (início da jornada), temos 08 horas exatas
* Limite superior 5,59 em todos os dias, pois das 18:00 (fim da jornada) até as 23:59 (último minuto do dia), temos 05 horas e 59 minutos de intervalo

Além da tabela de horário padrão ser a causadora do cenário, **outros pontos** precisam ser analisados:

* parâmetro **MV\_COLMARC** preenchido com conteúdo 4
* **troca de turno** para este funcionário realizada no 1º dia do próximo período de apontamento
* **períodos de apontamentos** fechados corretamente
* **MV\_PAPONTA e MV\_PONMES** com o período de apontamento aberto correto
* parâmetro [**MV\_MRHDPER**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5223165502359) configurado para demonstração do período futuro

Para as marcações já gravadas incorretamente na SP8, os ajustes acima descritos não terão impactos, sendo necessário via rotina **Lançamentos > Integrados - PONA280**, realizar os ajustes.  
  
Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30710451258135)  
 **Saiba Mais:  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
