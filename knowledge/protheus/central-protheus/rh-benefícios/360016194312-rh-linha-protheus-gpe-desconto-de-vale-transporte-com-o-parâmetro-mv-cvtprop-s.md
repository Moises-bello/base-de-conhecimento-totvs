---
article_id: 360016194312
category: RH - Benefícios
content_hash: 4820aedcc62a049cf957ff34f526f0ad5d2b8e72652c60f5d37bc54ef6bf0606
fetched_at: '2026-06-28T22:44:03.904796+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Desconto de Vale Transporte com o parâmetro MV_CVTPROP
  = S
type: support-article
updated_at: '2025-09-05T18:46:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016194312-RH-Linha-Protheus-GPE-Desconto-de-Vale-Transporte-com-o-par%C3%A2metro-MV-CVTPROP-S
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26984766070935) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como o sistema calcula o Vale Transporte quando o parâmetro **MV\_CVTPROP** está com o conteúdo = **S**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**

Para que o sistema considere o parâmetro **MV\_CVTPROP**, é preciso que o parâmetro **MV\_CVTUSO** esteja configurado com "1".

Para configurar o parâmetro acesse o Configurador SIGACFG em **Ambiente> Cadastros> Parâmetros**. O parâmetro **MV\_CVTPROP** configurado com "**S"** (Saldo), o sistema efetuará o cálculo de base de **VT** e Dias trabalhados para mensalistas da seguinte forma: Salário mês / dias do período \* Dias Saldo Mês

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26984796681495)

**Exemplo:**

Funcionário com salário de R$2500,00, teve gozo de 15 dias de férias (01/09/2024 à 15/09/2024), trabalhando do dia 16/09/2022 até 30/09/2022.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26984796682519)

Nesse exemplo o sistema irá calcular a quantidade de VT a receber em cima dos dias úteis, realmente trabalhados (Neste exemplo, 11 dias). E o desconto funcionário será feito sobre os 15 dias restantes do mês, contando sábado e domingo.

R$2500,00/30\*15= 1250,00\*6%= 75,00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26984796685207)

- Dias do Período: Será definido se o parâmetro **MV\_DIASPER** estiver com **1** ou **2**.

* Se estiver com **1**, irá buscar os dias do período do campo **RCF\_DPERIO**.
* Se estiver com **2**, ele efetuará outra condição que é: se o tipo de pagamento for Mensalista, ele buscará o conteúdo do mnemônico **P\_QTDIAMES**, senão ele busca o conteúdo do mnemônico **P\_NTOTDIAS**.

**Saiba Mais:**  
[RH - Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597251-RH-Benef%C3%ADcios)  
[RH - Linha Protheus - GPE - Como utilizar parâmetro MV\_CVTPROP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014665512-RH-Linha-Protheus-GPE-Como-utilizar-par%C3%A2metro-MV-CVTPROP?source=search)  
[RH - Linha Protheus - GPE - Como utilizar parâmetro MV\_CVTUSO no cálculo do vale transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014877491-RH-Linha-Protheus-GPE-Como-utilizar-par%C3%A2metro-MV-CVTUSO-no-c%C3%A1lculo-do-vale-transporte?source=search)  
[RH - Linha Protheus - GPE - Como Cadastrar e Calcular o Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029037011-RH-Linha-Protheus-GPE-Como-Cadastrar-e-Calcular-o-Vale-Transporte?source=search)
