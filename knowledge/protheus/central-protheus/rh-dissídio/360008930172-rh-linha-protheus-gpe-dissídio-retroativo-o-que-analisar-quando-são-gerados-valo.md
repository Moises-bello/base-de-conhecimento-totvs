---
article_id: 360008930172
category: RH - Dissídio
content_hash: 4092810565fb3c6a2a656a1224cd287f4e6708d15540d2d8fd0084008d00fce6
fetched_at: '2026-06-28T22:43:43.343595+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Dissídio retroativo, o que analisar quando são
  gerados valores negativos de horas extras
type: support-article
updated_at: '2025-08-20T12:30:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008930172-RH-Linha-Protheus-GPE-Diss%C3%ADdio-retroativo-o-que-analisar-quando-s%C3%A3o-gerados-valores-negativos-de-horas-extras
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34313942612119)*****Tempo aproximado para leitura:** **00:01:00 min**

**Dúvida**O que analisar quando no cálculo do dissídio retroativo, o sistema gera valores negativos de horas extras?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Primeiramente verifique se toda parametrização necessária foi realizada, para isso consulte o manual de dissídio retroativo através do *link* abaixo:

<http://tdn.totvs.com/pages/releaseview.action?pageId=220889925>

Como no dissídio o cálculo das verbas são recalculadas da base, devem ser verificadas todas as parametrizações que impactam no cálculo da HE, como carga horária (se na época da folha a base de cálculo foi sobre 30 ou 31 dias), verbas que incorporam ao salário no cálculo da HE e percentual, valide também se na época da folha o cálculo da HE foi feito corretamente.  
  
Após verificar o manual de dissídio e realizar as devidas verificações, verifique também os itens abaixo:

- Valores negativos provém de bases de cálculo atuais menores que as originais, confira se a base de cálculo atual contempla valores de adicionais que não existem mais;  
- Verificar a composição mensal das horas do cadastro de funcionários e compará-las com os campos de dias uteis e DSR do cadastro de períodos (fazer isso com os valores atuais e da época).

Após verificação e atualização, caso o erro persista, por gentileza nos envie as evidências abaixo (selecione um funcionário de exemplo para enviar as informações):  
  
- Informe o conteúdo Mnemônico P\_LMEDFERD (print de tela)  
- Cadastro do funcionários (pasta funcionais)   
- Cadastro do sindicato (pasta dissidio)  
- Acumulado GPEA120 (print de tela referente aos meses que estão com valores incorretos)  
- Parâmetros de cálculo completo (print de tela)  
- Print da tela com o cálculo do dissídio (mês que apresenta erro)  
- Cadastro do período completo ( aba cadastro de período e calendário)  
  
Data dos Fontes:  
GPEXCALC2.PRX   
GPEXCALC3. .PRX   
GPEXFUN.PRX   
GPEXFUN1.PRX   
GPEM020.PRX   
GPEM120.PRX   
GPEM690.PRX   
GPER040.PRX   
GPEXC131.PRX   
GPEXCADI.PRX   
GPEXCAL1.PRX   
GPEXCIMP.PRX   
GPEXINI.PRX   
GPEXSRV.PRX   
GPEXUSUA.PRX   
GPFO1BRA.PRX   
GPFO2BRA.PRX   
GPFORBRA.PRX   
\*Se preferir, envie a relação de todos os fontes, para isso, acesse: Clicar no Shift + F6 > Avançar > Exportar > Dados > Salvar o arquivo e anexar na Evidência.

**Saiba mais**  
Para adquirir maior conhecimento acesse os *links* abaixo  
[RH - Linha Protheus - GPE - Como conferir o cálculo de hora extra](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037322554)  
[https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH\_EXPEDICAO](https://suporte.totvs.com/portal/p/10098/download#000006/P12117/P12117AP/search/RH_ACUMULADO)
