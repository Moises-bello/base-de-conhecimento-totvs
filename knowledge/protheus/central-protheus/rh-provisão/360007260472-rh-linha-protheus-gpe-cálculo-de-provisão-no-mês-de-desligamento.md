---
article_id: 360007260472
category: RH - Provisão
content_hash: dba3e9177de0df4a5cd9a200f663590a925b41adca659522ce49d009b73ccb1a
fetched_at: '2026-06-28T22:43:55.692490+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de Provisão no mês de Desligamento
type: support-article
updated_at: '2025-06-17T20:33:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007260472-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Provis%C3%A3o-no-m%C3%AAs-de-Desligamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17677306585111)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como realizar o cálculo das Provisões de Férias e 13º Salário, do Mês de Desligamento do Funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

O parâmetro MV\_PROVRES possibilita ao usuário a opção de escolha entre apurar ou não o provisionamento de Férias e Décimo Terceiro Salário no mês de demissão do empregado.

1. A configuração padrão **N** (Não) não calcula a provisão no mês de demissão. Com isso, as baixas de provisão será exatamente exatamente o valor que estiver no campo anterior, como no exemplo abaixo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097803493)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17677192525335)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17677207522839)

Como não está sendo provisionado o mês de desligamento, veja que as Baixas são geradas com o mesmo valor provisionado no mês anterior.

2. A configuração **S** (Sim), calcula os valores que o funcionário garantiu direito no mês do desligamento, e as baixas serão calculadas considerando os valores pagos em rescisão, como no exemplo abaixo.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097803413)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17676934067351)

Veja que as Baixas de Rescisão são maiores do que o provisionado no mês anterior, isso ocorre porque na linha "No Mês" é apresentado o valor do avo garantido do mês de desligamento.  
Assim como no pagamento da rescisão, como as férias não têm incidência sobre os encargos de INSS e FGTS, não é gerada baixa sobre as férias indenizadas e o valor provisionado até o mês fica negativo na linha "No Mês", para que o Saldo Atual seja zerado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17676923033367)

No caso do 13º Salário, como há incidência de INSS e FGTS sobre o 13º salário indenizado em rescisão, será gerada baixa sobre estes encargos.

3. Caso haja a necessidade de alterar o parâmetro após o cálculo das provisões, será necessário Excluir e Reprocessar as provisões apenas para o funcionário Desligado. Para mais informações sobre este processo [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036636774-MP-GPE-Como-Excluir-o-C%C3%A1lculo-das-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio) .

**Observação:** O parâmetro MV\_PROVRES não deverá ser preenchido com aspas.

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
