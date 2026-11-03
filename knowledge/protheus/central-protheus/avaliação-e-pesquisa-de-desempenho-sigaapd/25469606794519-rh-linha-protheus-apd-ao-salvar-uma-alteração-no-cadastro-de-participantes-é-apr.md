---
article_id: 25469606794519
category: Avaliação e Pesquisa de Desempenho (SIGAAPD)
content_hash: c4779993b4e459985719b39842382cbdfc988e3bb7d3345e2ed98b5e2cc53b8f
fetched_at: '2026-06-28T22:42:53.715322+00:00'
product: protheus
section_id: 206956088
source: central-protheus
title: RH - Linha Protheus - APD - Ao salvar uma alteração no Cadastro de Participantes,
  é apresentado o log "Descrição deve ser informada"
type: support-article
updated_at: '2024-08-07T13:09:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25469606794519-RH-Linha-Protheus-APD-Ao-salvar-uma-altera%C3%A7%C3%A3o-no-Cadastro-de-Participantes-%C3%A9-apresentado-o-log-Descri%C3%A7%C3%A3o-deve-ser-informada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25469606775063) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Após salvar uma alteração no Cadastro de Participantes, é apresentado o log "Descrição deve ser informada"  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Avaliação e Pesquisa de Desempenho – Todas as versões  
  
**Solução**Ao alterar um registro qualquer via **APDA020 - Cadastro de Participantes**, pode ser apresentado o *log* de ocorrências a seguir:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25469606776343)  
  
Esta validação, refere-se ao campo Bairro - **RD0\_BAIRRO:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25469606777623)  
  
No exemplo acima, nota-se que na primeira posição do dado, **há um espaço em branco.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25469606779671)  
  
A solução será alterar o dado do **campo RD0\_BAIRRO**, retirando o espaço desnecessário **da primeira posição.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25469638916503)  
  
Assim, a alteração feita no **Cadastro de Participante**, será efetivada.  
  
**Saiba Mais**  
[Artigos Sobre Avaliação Pesquisa e Desempenho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206956088-Avalia%C3%A7%C3%A3o-e-Pesquisa-de-Desempenho-SIGAAPD-)  
[Artigos Sobre Portal Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-Portal-de-Gest%C3%A3o-de-Capital-Humano)
