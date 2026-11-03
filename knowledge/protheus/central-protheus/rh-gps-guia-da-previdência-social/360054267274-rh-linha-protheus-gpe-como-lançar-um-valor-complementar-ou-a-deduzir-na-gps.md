---
article_id: 360054267274
category: RH - GPS (Guia da Previdência Social)
content_hash: 9516315124adad32414c66a7a9023d105f709567fe649a4e399df35a9c03a925
fetched_at: '2026-06-28T22:43:11.563559+00:00'
product: protheus
section_id: 360011996273
source: central-protheus
title: RH - Linha Protheus - GPE - Como lançar um valor complementar ou a deduzir  na
  GPS
type: support-article
updated_at: '2025-10-20T12:41:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054267274-RH-Linha-Protheus-GPE-Como-lan%C3%A7ar-um-valor-complementar-ou-a-deduzir-na-GPS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33057825944087) Tempo aproximado para leitura: 00:01:00 min**  
**Dúvida**Como lançar um valor complementar ou a deduzir na GPS?  
  
**Ambiente**TTOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
**1**.Em >Atualizações >Definições de Cálculo >Manutenção Tabelas >**Tabela S035** - **Complemento GPS**  
Lance o valor da Nota Fiscal ou Valor de INSS já recolhido e informe se deseja **deduzir** ou **recolher** utilizando o ID P/ CALCULO que compreende a necessidade:  
**0584** - Compensação – Resíduo meses anteriores  
**0313** - Vl. INSS s/ Vl. Cooperativa  
**0314** - Valor da Fatura  
**0315** - Valor Produtor Rural PF  
**0316** - Valor Produtor Rural PJ

**OBS**: Para o valor lançado ser deduzido da guia, na tabela S035 o campo Rec./Ded. deverá ser preenchido com **D**.

Para o valor lançado ser recolhido na guia, na tabela S035 o campo Rec./Ded. deverá ser preenchido com **R**.

**2**. Feito isso, o sistema está pronto pra gerar a SEFIP no código de recolhimento 155 ou 150, deve-se observar algumas perguntas da geração do arquivo SEFIP:

- "Gerar Por" deve estar como Centro de Custo;  
- "Código de GPS da Filial" deve ser informado 2100 ou 2003, 2003 se for optante pelo SIMPLES, 2100 se não for;  
- O código de pagamento da GPS do Centro de Custo deve ser 2208 obrigatoriamente quando o código de recolhimento for 155;  
- Se for 2100 ou 2003, o Código da GPS do Centro de custo deverá ser o mesmo usado para a GPS da Filial, 2003 ou 2100.  
  
Abaixo o exemplo:   
  
Tabela S035 onde demonstra o valor de 5.000,00 mês de inicio e mês final:![](https://totvssuporte.zendesk.com/attachments/token/XOgsL4RmdduxMePQ5c785vc46/?name=inline436506438.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/ev5LzY9zoir89cUM5AiKRTXAm/?name=inline1355315176.png)

Cadastro da verba com ID 0584: ![](https://totvssuporte.zendesk.com/attachments/token/A01AyNGx7gfBHw3PVtpoufng8/?name=inline-1927889731.png)

Na aba Incidências o campo **Ded. G. INSS** deve estar com Sim:![](https://totvssuporte.zendesk.com/attachments/token/fJvfQ6innru0u0HinciKdaVz7/?name=inline-2128343638.png)

Ao gerar o relatório de conferência da GPS o valor é apresentado no relatório e consequentemente vai complementar a GPS:![](https://totvssuporte.zendesk.com/attachments/token/MSsjPJ6nSYoXVSmndGVSv2Una/?name=inline564665040.png)

**Saiba Mais:** <https://tdn.totvs.com/display/public/PROT/FGTS>
