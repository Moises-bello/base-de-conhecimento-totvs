---
content_hash: 0669eafda90e8e2dd14d7f6e49f4603aa588d26f3f4e34b1445ea776421a2172
fetched_at: '2026-06-29T00:09:50.186971+00:00'
page_id: '435105432'
product: rm
source: tdn-rm
title: Geração do Resíduo Anual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105432
version: 1
---

**Geração do Resíduo Anual**

---

O processos de Resíduo Anual é o acumulo do valor reajustado durante um período de 12 meses, que é acumulado e gerado em uma parcela única de Resíduo no final do período. Esta parcela de Resíduo é gerada no Plano de Financiamento e a mesma poderá sofrer reajustes monetários e de juros.  
A parametrização do Componente de Resíduo Anual é feita na Geração do Plano de Retorno, pois o mesmo gerará um nova parcela.

* Parametrizações:  
     
  No cadastro do Componente no campo Surgimento do Componente, deverá marcar a opção Na Geração do Plano de Financiamento.  
     
  Para gerar a parcela de resíduo, é necessário cadastrar uma nova venda com a modalidade de venda parametrizada para Resíduo Anual.  
  Na geração do Plano de Financiamento, observe a parametrização do Componente de Resíduo anual na aba Condições de Venda, o mesmo deve ser parametrizado com as *flags* do campo Reajuste sobre o "Resíduo da Parcela Quitada" marcadas.  
     
  Ainda na aba Condições de Venda, é importante atentar-se para a periodicidade dos componentes de correção monetária (antes e após), devem conter sempre uma periodicidade mensal de 12 meses.
* Observação: O componente Principal tem que ser do tipo Modelo Padrão para que ocorra o resíduo.  
     
  Após a geração do Plano de Financiamento, é necessário realizar o primeiro Reajuste Monetário, neste exemplo, o reajuste será feito em 01/01/2010.  
  Depois do Reajuste Monetário, realize a baixa da parcela reajustada.  
  Em seguida, realize o Reajuste do Resíduo e a quitação da parcela referente ao mês do Reajuste até completar o período de 12 parcelas mensais quitadas.  
     
  Após realizar os processos acima descritos, é necessário realizar a Geração da Parcela de Resíduo, para o mesmo.  
  Acesse o menu Contratos | Contratos de Vendas e Aluguéis | Selecione a venda desejada | Processos | Gerar Parcela de Resíduo.  
     
  Ao acessar a opção Gerar Parcela de Resíduo, o sistema abrirá a tela para gerar a parcela de resíduo. Nesta tela, o sistema traz todas as parcelas da venda que estão quitadas, e traz a descrição do resíduo calculado em cada parcela.  
     
  No campo Parcela Resíduo, após a seleção das parcelas, o sistema traz as descrições da parcela nova que será gerado no Plano de Financiamento. O valor da mesma consiste da soma do Resíduo Calculado em cada reajuste, número da parcela, grupo da parcela e o vencimento das mesmas (conforme parametrizado).
