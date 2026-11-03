---
article_id: 10009192812823
category: RH - Folha de Pagamento
content_hash: e94dcabe53b60cd7c4fba15bd1f533fe1149c66a46edc5e75a0b192d5503dbbf
fetched_at: '2026-06-28T22:44:12.087673+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de horas extras sobre folha de comissionado
  misto sem comissão no mês
type: support-article
updated_at: '2024-09-12T11:29:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10009192812823-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-horas-extras-sobre-folha-de-comissionado-misto-sem-comiss%C3%A3o-no-m%C3%AAs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26319618447511) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**Sistema efetua a geração indevida da hora extra sobre comissão.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Com a configuração de verbas efetuada conforme a documentação disponível em [Hora Extra - Como é efetuado o cálculo de horas extras do empregado comissionista](https://tdn.totvs.com/pages/viewpage.action?pageId=245172200), caso o comissionado misto de categoria M (Mensalista) não tenha recebido comissão no mês e tenha recebido hora extra, o sistema efetua a geração indevida da hora extra sobre comissão.  
  
**Solução**Para distinguir uma hora extra de comissão de uma hora extra "normal", além do campo RV\_HE preenchido com S (Sim), será necessário configurar o novo campo **RV\_HECOMIS** com 1 (Sim).

Dessa forma, o sistema conseguirá distinguir a situação mencionada acima e evitará a geração da hora extra de comissão configurada no código correspondente de funcionário comissionado misto de categoria M no mês que não tenha recebido comissão.  
  
Observação:

Além do patch de atualização, será necessário a da execução do **UPDDISTR** com o dicionário liberado no pacote de expedição do módulo RH a partir de **XX/11/2021** para os releases iguais ou superiores a versão 12.1.25. Para release 12.1.17 ou anteriores, o ajuste deverá ser feito **manualmente**.  
  
Criação dos campos abaixo na tabela SRV no dicionário SX3:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10014124311703)

**Saiba Mais:**

[Atualizador de dicionário e base de dados - UPDDISTR](https://tdn.totvs.com/pages/viewpage.action?pageId=181965468).

[Hora Extra - Como é efetuado o cálculo de horas extras do empregado comissionista](https://tdn.totvs.com/pages/viewpage.action?pageId=245172200).

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
