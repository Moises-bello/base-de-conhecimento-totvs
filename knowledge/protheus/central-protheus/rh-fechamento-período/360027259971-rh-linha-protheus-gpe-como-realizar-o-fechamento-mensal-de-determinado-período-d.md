---
article_id: 360027259971
category: RH - Fechamento Período
content_hash: 97458f2a1dd498d4ddb8e37854de9e4889da016c96e087c0c9c2f2c27ad22b81
fetched_at: '2026-06-28T22:43:24.436437+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar o fechamento mensal de determinado
  período da folha
type: support-article
updated_at: '2025-05-12T13:08:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027259971-RH-Linha-Protheus-GPE-Como-realizar-o-fechamento-mensal-de-determinado-per%C3%ADodo-da-folha
---

![relogio.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22324204610583) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como fazer o fechamento mensal de determinado período da folha?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Versão 12.  
  
**Solução**O **Fechamento da folha** deve ser executado somente após todos os processos mencionados neste artigo serem efetuados e a folha conferida, pois após o fechamento da mesma, não orientamos a reabertura por conta dos encargos já calculados e para manter a integridade das informações.  
  
Para mais informações dos processos a serem efetuados, segue artigos relacionadas:  
  
-**Fluxo de Cálculo e processos**: [RH - Linha Protheus - GPE - Fluxo de cálculos e processos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004341792)  
- **Integração de Roteiros com a Folha**: [RH - Linha Protheus - GPE - Integração dos roteiros com a folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027259251)  
- **Como efetuar o cálculo da Folha**: [RH - Linha Protheus - GPE - Como efetuar o cálculo da folha de pagamento na versão 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026974232)  
  
Após todos os procedimentos acima mencionados, para executar o fechamento, acesse a rotina **GPEM120**: **Miscelânea > Fechamentos > Período (GPEM120)**, onde após preenchimento do campo **Processo** e **Período** o Sistema abrirá uma tela para seleção dos **Roteiros** que serão encerrados, conforme imagem abaixo:

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360026772152)

Deverá **marcar** os **roteiros** a serem fechados e **executar** a rotina.  
  
O parâmetro **MV\_FECFOL** permite ou não o fechamento do roteiro FOL ou AUT **junto** com outro (s) roteiro (s), devendo o usuário fechar **todos** os roteiros para em seguida fechar o roteiro FOL/AUT individualmente.  
  
Porém para que o **roteiro** em questão seja encerrado, o mesmo deve existir para o mês seguinte também, caso contrário o sistema apresentará o *log* abaixo:

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360026772272)

Nesse exemplo, para que consiga fechar o **roteiro** de **VTR - Vale Transporte,** do mês 10/2017 precisa ter o roteiro em questão já cadastrado para o mês 11/2017 no cadastro de **Períodos - GPEA400: Atualizações > Definições de Cálculo > Períodos**.  
  
Após o cadastro dos **roteiros** necessários, basta executar novamente o **Fechamento**.   
  
Ao processar corretamente, o Sistema levará todas as informações do **Movimento Mensal - tabela SRC** para o **Acumulado - tabela SRD**, atualizará as informações do funcionário, como o **Controle dias de Direito**, **Ausências,** **Valores Futuros** caso possua, e atualizará o cadastro de **Períodos**.

**Saiba Mais:**

[RH - Linha Protheus - GPE - Passo a passo para o processo de fechamento da folha:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057785494?source=search)

[RH - Linha Protheus - GPE - Após fechamento do período, Sistema não atualiza status para Fechado no cadastro de períodos:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414532770711?source=search)

[RH - Linha Protheus - GPE - Melhoria de performance no fechamento mensal com MV\_CALCTHD ativo:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050884333?source=search)

[RH - Linha Protheus - GPE - Implementação de GRID no Fechamento de Período:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19124711142679?source=search)

[RH - Linha Protheus - GPE - Implementação do Multi Thread no fechamento da folha:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034908554?source=search)

[RH - Fechamento Período](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909793-RH-Fechamento-Per%C3%ADodo)
