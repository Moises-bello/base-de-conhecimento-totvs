---
article_id: 5224648508183
category: eSocial - Gerar XML/ Integração Evento
content_hash: 64a415e8493d8c961082c0248eb344af8dce194f4c9e85bdb75ed3cf3f1fbd24
fetched_at: '2026-06-28T22:47:12.191046+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar o S-1200:  Necessário preencher o
  parâmetro Evento Antecipação Primeira Parcela 13º nas Férias'
type: support-article
updated_at: '2024-06-26T15:12:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5224648508183-RH-RM-FOP-eSocial-Erro-ao-gerar-o-S-1200-Necess%C3%A1rio-preencher-o-par%C3%A2metro-Evento-Antecipa%C3%A7%C3%A3o-Primeira-Parcela-13%C2%BA-nas-F%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:00 min**

**Ocorrência**Ao gerar evento S-1200 para funcionários que tiveram antecipação de férias é exibido o erro **Necessário preencher o parâmetro Evento Antecipação Primeira Parcela 13º nas Férias nos Parâmetros Gerais do eSocial!****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da 12.1.31.193, 12.1.32.131 e 12.1.33  
  
**Causa**O erro ocorre pois o campo **Evento Antecipação Primeira 13º nas Férias (Provento)** localizado no menu **Configurações | Parametrizador | eSocial | Configurações Gerais 7/7** não está preenchido.

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5224565355415/Capturar.PNG)

**Solução**Para correção dessa ocorrência, siga os passos abaixo:

1. Crie o evento como **Provento,** sem **incidências em FGTS 13, sem código de cálculo** e insira-o no campo supracitado; 

2. Faça a edição do gatilho do S-1010 que será gerado na fila de eventos do eSocial. Informe no campo **Competência** um mês e ano igual ou anterior ao período de apuração do S-1200;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6573981344151/mceclip1.png)

3. Gere o XML do S-1010 e faça a transmissão para o governo;  
4. Em seguida, gere novamente o evento S-1200 e transmita ao governo.

 

**Importante**  
A TOTVS não orienta qual natureza de rubrica deve ser informada nas verbas, ficando tal escolha a cargo da própria empresa. O que podemos orientar é que a natureza esteja condizente com o Anexo I do Layout eSocial utilizado.  
  
**Saiba mais**  
Para maiores informações, acesse:  
     • [S-1200 e S-1210: Recibo de Férias no leiaute S-1.0](https://tdn.totvs.com/pages/viewpage.action?pageId=627729108)  
     • [Configurações Gerais 7/7](https://tdn.totvs.com/pages/releaseview.action?pageId=645896860)
