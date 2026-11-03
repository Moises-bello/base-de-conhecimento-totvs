---
article_id: 360052920234
category: RH - Folha de Pagamento
content_hash: ae8944dae7e80edc960a240a9ea938e691647c8ab17693a5223bfee4581ddc25
fetched_at: '2026-06-28T22:44:13.289534+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o cálculo da insalubridade sobre
  salário mínimo
type: support-article
updated_at: '2024-09-11T20:19:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052920234-RH-Linha-Protheus-GPE-Como-configurar-o-c%C3%A1lculo-da-insalubridade-sobre-sal%C3%A1rio-m%C3%ADnimo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26308301964567) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como configurar o cálculo da insalubridade sobre salário mínimo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que o cálculo da insalubridade seja sobre salário mínimo, é necessário parametrizar no cadastro de sindicato conforme abaixo:  
**IMPORTANTE: Esta alteração deve ser feita com a Data Base do sistema no primeiro dia do mês do inicio do cálculo!**

1. Entre na rotina Sindicato (caminho >Atualização >Cadastros >Sindicato), posicione no Sindicato em questão e clique em Alterar:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088384593)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088384693)  
  
2. O valor do **salário minimo** deve ser informado em Manutenção de Tabelas > **S004**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087243874)**

3. Cadastro do funcionário - Aba Peric/ Insal. > informar o Grau da insalubridade a ser paga para o funcionário.

Informando o grau, automaticamente o sistema irá gatilhar as horas Mês do funcionário

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087244014)**

4. Cálculo da folha:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087244274)

Base de cálculo: 1.045,00 \* 40% = 418,00

**Saiba Mais**

[RH - Linha Protheus - GPE - Alteração no cadastro do Sindicato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052464393-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%A3o-no-cadastro-do-Sindicato)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
