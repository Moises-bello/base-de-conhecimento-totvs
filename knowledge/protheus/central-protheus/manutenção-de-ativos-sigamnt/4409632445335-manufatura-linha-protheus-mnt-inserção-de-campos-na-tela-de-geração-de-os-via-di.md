---
article_id: 4409632445335
category: Manutenção de Ativos (SIGAMNT)
content_hash: acf5cf4dad53240dfe88cc51879dfc33c21ad7ce10a116d56cf0ad2ffb840913
fetched_at: '2026-06-28T22:42:34.153362+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Inserção de campos na tela de geração de
  O.S. via Distribuição de S.S.
type: support-article
updated_at: '2021-09-29T20:30:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409632445335-Manufatura-Linha-Protheus-MNT-Inser%C3%A7%C3%A3o-de-campos-na-tela-de-gera%C3%A7%C3%A3o-de-O-S-via-Distribui%C3%A7%C3%A3o-de-S-S
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como é realizada a inserção de campos na tela de geração de **O.S. - Ordem de Serviço** por meio da distribuição de **S.S. - Solicitação de Serviço**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Para inserir os campos na tela de geração de **O.S.** via **Distribuição de S.S. - MNTA295** é necessário utilizar três pontos de entrada, o **MNTA2952**, o **MNTA2954** e o **MNTA2955**.  
  
**Saiba mais**  
Para informações complementares a respeito dos pontos de entrada e o objetivo de cada um deles, verifique os *links*:   
  
[DT PE MNTA2954 Geracao de Ordem de Servico](https://tdn.totvs.com/display/PROT/DT+PE+MNTA2954+Geracao+de+Ordem+de+Servico)  
Declarar variáveis utilizadas na criação dos campos que serão inseridos em tela e/ou iniciar o campo de **Serviço** + **Descrição do serviço** automaticamente. As variáveis declaradas neste ponto de entrada, serão utilizadas nos pontos de entrada apresentados abaixo.  
  
[DT PE MNTA2955 Geracao de Ordem de Servico](https://tdn.totvs.com/display/PROT/DT+PE+MNTA2955+Geracao+de+Ordem+de+Servico)  
Inclusão dos campos escolhidos pelo usuário em tela.  
  
[DT PE MNTA2952 Gravacao de Ordem de Servico](https://tdn.totvs.com/display/PROT/DT+PE+MNTA2952+Gravacao+de+Ordem+de+Servico)  
Salva as informações dos campos incluídos pelo usuário no ponto de entrada **MNTA2955**.
