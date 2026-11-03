---
article_id: 360060965613
category: RH - Folha de Pagamento
content_hash: e241a695d410e06dbf993a6bd05ab0502b8245ba4f8349c6ed8c322c17f6352e
fetched_at: '2026-06-28T22:44:13.302294+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o cálculo de IRRF para funcionário
  residente no exterior (expatriado)
type: support-article
updated_at: '2025-11-11T17:52:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060965613-RH-Linha-Protheus-GPE-Como-configurar-o-c%C3%A1lculo-de-IRRF-para-funcion%C3%A1rio-residente-no-exterior-expatriado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26192631152919) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como configurar o cálculo de IRRF para funcionário residente no exterior (expatriado)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução** **1.** Na rotina **Funcionários**, pelo caminho **Atualizações** > **Funcionários** > **Funcionários (GPEA010)**, selecione o funcionário residente no exterior em questão e na **aba Endereço**, deixe o campo **Res. Exterior** com **SIM:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013875141)

**2.** Na rotina **Histórico de Contrato**, pelo caminho **Atualizações** >**Funcionários** >**Histórico de Contrato (GPEA900)**, selecione o mesmo funcionário residente no exterior, e na aba **Residente no Exterior** deixe o campo **Calcula IR** com **Não** para **não calcular** o **IR ou com Sim para calcular IR:**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013591682)  
  
**3.** Deixando = não, ao calcular a folha o sistema não calculará o IR do funcionário residente no exterior:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013591782)  
  
Deixando = sim, o Sistema apresentará no cálculo o id de cálculo 0066 com desconto de 25% de IRRF.  
  
**Importante** Os demais campos informados acima são apenas exemplo, devem ser preenchidos de acordo com o contrato do funcionário.

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
