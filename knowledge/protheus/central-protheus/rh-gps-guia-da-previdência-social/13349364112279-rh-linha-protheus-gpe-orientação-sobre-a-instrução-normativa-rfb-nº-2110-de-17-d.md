---
article_id: 13349364112279
category: RH - GPS (Guia da Previdência Social)
content_hash: c1bbc193b312015185d7b5325427b6482313082cea716db50e50b16d910beda4
fetched_at: '2026-06-28T22:43:11.607339+00:00'
product: protheus
section_id: 360011996273
source: central-protheus
title: RH - Linha Protheus - GPE - Orientação sobre a Instrução Normativa RFB Nº 2.110,
  de 17 de Outubro de 2022.
type: support-article
updated_at: '2024-03-27T12:23:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13349364112279-RH-Linha-Protheus-GPE-Orienta%C3%A7%C3%A3o-sobre-a-Instru%C3%A7%C3%A3o-Normativa-RFB-N%C2%BA-2-110-de-17-de-Outubro-de-2022
---

Em Atualizações > Definições de Cálculo > Manutenção Tabelas > **Tabela S035** - **Complemento GPS**  
Lance o valor da Nota Fiscal ou Valor de INSS já recolhido e informe se deseja **deduzir** ou **recolher** utilizando o ID P/ CALCULO que compreende a necessidade:  
**0584** - Compensação – Resíduo meses anteriores  
**0313** - Vl. INSS s/ Vl. Cooperativa  
**0314** - Valor da Fatura  
**0315** - Valor Produtor Rural PF  
**0316**- Valor Produtor Rural PJ

Feito isso o sistema está pronto pra gerar a SEFIP no código de recolhimento 155 ou 150, deve-se observar algumas perguntas da geração do arquivo SEFIP:

A pergunta "Gerar Por" deve estar como Centro de Custo, "Código de GPS da Filial" deve ser informado 2100 ou 2003, 2003 se for optante pelo SIMPLES, 2100 se não for. O código de pagamento da GPS do Centro de Custo deve ser 2208 Obrigatoriamente quando o código de recolhimento for 155. Se for 2100 ou 2003, o Código da GPS do Centro de custo deverá ser o mesmo usado para a GPS da Filial, 2003 ou 2100.

Se a empresa prestar serviço pra tomadores com CEI e tomadores com CNPJ a empresa deverá entregar 2 SEFIPs, um dos tomadores com CEI e outra pra os tomadores com CNPJ. Ou seja, uma 150 e outra 155, a junção das duas conterá os funcionários de toda a empresa.

Não se trata de uma regra do Protheus, é uma regra da Caixa que não aceita gerar uma única SEFIP com dois códigos de Recolhimento (150 e 155), apenas uma de cada vez.

Abaixo o exemplo:   
  
Tabela S035 onde demonstra o valor de 5.000,00 mês de inicio e mês final:![](https://totvssuporte.zendesk.com/attachments/token/XOgsL4RmdduxMePQ5c785vc46/?name=inline436506438.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/ev5LzY9zoir89cUM5AiKRTXAm/?name=inline1355315176.png)

Cadastro da verba com ID 0584: 

![](https://totvssuporte.zendesk.com/attachments/token/A01AyNGx7gfBHw3PVtpoufng8/?name=inline-1927889731.png)

Na aba Incidências o campo**Ded. G. INSS** deve estar com Sim:![](https://totvssuporte.zendesk.com/attachments/token/fJvfQ6innru0u0HinciKdaVz7/?name=inline-2128343638.png)

Ao gerar o relatório de conferência da GPS o valor é apresentado no relatório e consequentemente vai complementar a GPS:![](https://totvssuporte.zendesk.com/attachments/token/MSsjPJ6nSYoXVSmndGVSv2Una/?name=inline564665040.png)

**eSocial x Reinf**

Para o cálculo das Guias feitas pelo DCTFWeb, não existe ação ou campos disponíveis em eventos do eSocial.

O cálculo é feito de forma automática pelo sistema do Governo através de amarração de informações dos eventos gerados no REINF:

**R-2010****Retenções dos Tomadores de Serviços**

**R-2020** **Retenções dos Serviços Prestados**

Os dados de pagamento de benefícios (VT, VR, etc)  devem transitar pela folha de funcionários como rubricas informativas, para que sejam levados ao ambiente do Governo através do evento S-1200 - Folha de Pagamento

Esses funcionário são amarrados nos tomadores de Serviços através do evento S-1020 - Lotações Tributárias

Com base em todas essas informações o DCTFWeb consegue realizar o cálculo da retenção corretamente.

**Saiba Mais:**

<https://www.in.gov.br/en/web/dou/-/instrucao-normativa-rfb-n-2.110-de-17-de-outubro-de-2022-437619362>

<https://tdn.totvs.com/pages/releaseview.action?pageId=747310812>

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054267274-RH-Linha-Protheus-GPE-Como-lan%C3%A7ar-um-valor-complementar-ou-a-deduzir-na-GPS->
