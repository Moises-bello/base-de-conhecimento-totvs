---
article_id: 15836657894679
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: d6e59812d344cfa86da93bf23f74b08ea965b75ba5d629c331bf39041cdd2a85
fetched_at: '2026-06-28T22:38:48.157397+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - A rotina
  de Acompanha custos não possui mais o parâmetro Contabiliza on-line por(Ambas, Consumo,
  Produção)?
type: support-article
updated_at: '2023-07-06T20:40:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15836657894679-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-A-rotina-de-Acompanha-custos-n%C3%A3o-possui-mais-o-par%C3%A2metro-Contabiliza-on-line-por-Ambas-Consumo-Produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15836700272151) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Na nova rotina (Acompanha Custos) não existe mais o parâmetro "Contabiliza on-line por" = (Ambas, Consumo, Produção) como existia no processo antigo de Recálculo do Custo Médio (MATA330)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Na nova rotina de Fechamento de Estoque, ao preencher o parametro: "Gerar Lançamento contábil = Sim", ao iniciar a nova Jornada de Fechamento, irá aparecer as opções abaixo que é exatamente a mesma opção da rotina Recálculo do Custo Médio (MATA330):  
   
   
   
![](https://totvssuporte.zendesk.com/attachments/token/R69PENyuvmrMqpRmxqhgtj4aO/?name=image.png)  
   
Se o usuário preencher a opção "Contabilizar Padrão", seria o equivalente à opção "Ambas" na rotina de Custo Médio (MATA330).  
   
Ou seja o sistema vai recalcular e contabilizar por consumo e produção ao mesmo tempo.  
   
Agora se o usuário colocar: "**Contabilização por Consumo e Produção**", o sistema realiza o processamento do custo por consumo e contabiliza, depois processa por produção e contabiliza. Esse processo ocorre durante a Contabilização.  
   
![](https://totvssuporte.zendesk.com/attachments/token/VxDvScNsfJgdKIUFrNxX3RzxX/?name=image.png)  
   
É o mesmo processo, porém numa única interface, no MATA038 é possível processar o custo por consumo, produção e contabilização num único processamento, diferente de processar o custo diretamente pelo MATA330 onde nesse caso era necessário realizar o processamento duas vezes.  
   
Se o usuário desejar processar novamente o **consumo**, deverá sair da rotina antes de iniciar o processamento da **produção**, cancelar o fechamento e iniciar novamente o processamento.  
   
Já para **produção,** poderá processar novamente de forma individual, bastando ativar a opção nos parâmetros antes de iniciar a jornada de fechamento.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre a rotina Acompanha Custos (MATA038) no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação para inicia a rotina Acompanha Custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5240908654999)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O que é a rotina Acompanha Custos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5065773526039)*

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de parâmetros Acompanha Custos - Jornada de Fechamento*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5065941471767)
