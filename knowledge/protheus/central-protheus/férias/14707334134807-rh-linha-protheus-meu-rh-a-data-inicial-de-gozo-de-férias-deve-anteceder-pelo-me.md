---
article_id: 14707334134807
category: FÉRIAS
content_hash: d69a1c5ea184a7232ad3802cf6a8f54e2a3a6512283a0e1ee23a4840da35a1f1
fetched_at: '2026-06-28T22:44:34.528289+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - Meu RH - A data inicial de gozo de férias, deve anteceder
  pelo menos 2 dias ao DSR / Feriado
type: support-article
updated_at: '2026-06-05T11:56:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14707334134807-RH-Linha-Protheus-Meu-RH-A-data-inicial-de-gozo-de-f%C3%A9rias-deve-anteceder-pelo-menos-2-dias-ao-DSR-Feriado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25651001025303) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Incluir uma solicitação de Férias apresenta a mensagem "A data inicial de gozo de férias, deve anteceder pelo menos 2 dias ao DSR"  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões.  
  
**Solução**  
Ao solicitar férias via Meu RH, é necessário **atentar-se à data de início**, que não é permitida que se inicie de **1 a 2 dias antes do DSR definido no Turno do funcionário**.  
  
O Meu RH irá trazer este *log* de ocorrências, no momento em que as férias forem solicitadas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14707211522839)  
  
Para validar esta data, temos duas rotinas onde será feita a análise:  
1 - no módulo SIGAGPE, rotina **Atualizações -> Definições de Cálculo -> Períodos**  
2 - no módulo SIGAPON rotina **Atualizações -> Cadastro de Ponto -> Tabela de Horário Padrão**  
  
No caso do exemplo acima, dia **16/06/2023 é uma sexta-feira**, ou seja, **2 dias antes do DSR** daquela semana, que seria **dia 18/06/2023**, dado um turno padrão, 5x2 de segunda a sexta, sábado compensado e domingo DSR, sendo neste caso, necessário **iniciar pelo menos dia 15/06/2023** o gozo das férias.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14707188535191)  
  
A **mesma validação** seria feita se, o início das férias fosse **dois dias antes de um Feriado**, cadastrado no módulo do Ponto Eletrônico, na rotina **Atualizações -> Cadastro de Ponto -> Feriado**  
  
Neste caso, dia **08/06/2023 é Feriado**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14707278693911)  
  
**O parâmetro MV\_REFTRAB** também precisará estar cadastrado corretamente, este por sua vez, trará ao **Protheus e ao App Meu RH**, as diretrizes da **Reforma Trabalhista**, segue conteúdo necessário do parâmetro:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25651016084375)  
  
  
**Saiba Mais:**  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
