---
article_id: 17085161309335
category: RH - Dissídio
content_hash: 96662bbcf9c9aabf5d75f060f03bf89a039a785f5ed937418e25f4c99f7c1ce8
fetched_at: '2026-06-28T22:43:43.412932+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - O que deve ser verificado quando forem apresentadas
  verbas de salário com valores negativos no cálculo do dissídio para horistas
type: support-article
updated_at: '2025-08-13T18:05:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17085161309335-RH-Linha-Protheus-GPE-O-que-deve-ser-verificado-quando-forem-apresentadas-verbas-de-sal%C3%A1rio-com-valores-negativos-no-c%C3%A1lculo-do-diss%C3%ADdio-para-horistas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17085180465559) Tempo aproximado para leitura: **00:01:00 min****Dúvida**O que deve ser verificado quando forem apresentadas verbas de salário com valores negativos no cálculo do dissídio para horistas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**  
1) Efetue o cálculo da coluna origem , dividindo o salário ou base pelo valor do salário hora:  
R$ 2.641,57 (salário) / 11,62 (valor hora) = 227,33 (horas) -  Nesta situação chegamos na quantidade de horas que foram utilizadas no cálculo de salário na folha de pagamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17160021688727)

2) Em seguida faremos a mesma conta, agora com a coluna do valor calculado no dissídio.   
R$ 2.670,80 (salário) / 12,14 (valor hora) = 220,00 (horas)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17160214678295)**

Veja que a quantidade de horas não é compatível com o cálculo realizado na folha de pagamento (ORIGEM).

Este erro. tem uma incidência maior que erro, quando possui no mesmo processo mensalistas e horistas, onde ao invés de **cadastrar em processos diferentes ou criar um período para os horistas,** realiza-se a alteração no cadastro de períodos, calculando os mensalistas com 30 e os horistas com 31.  
  
Acesse Atualizações -> Definições de Cálculo -> Períodos e verifique o campo Dias Cálculo. No print abaixo vemos um caso para mês de 31 dias que foi usado para calcular a folha mas sofreu alteração para cálculo dos mensalistas. Como a rotina de dissídio reprocessa a  folha de pagamento com o novo salário ajustado, efetua o cálculo com 30 dias gerando incorretamente as diferenças a pagar no dissídio.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17160521439895)

Para tratar essa situação deve ser aplicada a mesma regra da folha de pagamento:

1) Dar manutenção na tabela RCF ajustado os dias de cálculo e efetuar o cálculo somente categoria horistas;  
2) Caso tenha necessidade de calcular mensalistas, dar manutenção novamente e calcular somente categoria mensalistas

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como calcular dissídio retroativo para funcionários horistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9004537077143-RH-Linha-Protheus-GPE-Como-calcular-diss%C3%ADdio-retroativo-para-funcion%C3%A1rios-horistas)

[RH - Linha Protheus - GPE - Como parametrizar e calcular o dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034578653-RH-Linha-Protheus-GPE-Como-parametrizar-e-calcular-o-diss%C3%ADdio-retroativo)
