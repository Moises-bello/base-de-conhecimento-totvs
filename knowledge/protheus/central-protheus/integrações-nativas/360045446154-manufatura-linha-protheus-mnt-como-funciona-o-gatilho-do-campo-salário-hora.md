---
article_id: 360045446154
category: Integrações Nativas
content_hash: bfddd239604068e96c6a857cd992cc8c637b26c20e525a9b3b11191eb60b2995
fetched_at: '2026-06-28T22:42:35.366982+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Como funciona o gatilho do campo Salário
  Hora
type: support-article
updated_at: '2022-05-19T18:15:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045446154-Manufatura-Linha-Protheus-MNT-Como-funciona-o-gatilho-do-campo-Sal%C3%A1rio-Hora
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)** Tempo aproximado para leitura:**00:01:45 min** **Dúvida**Como funciona o gatilho do campo **Salário Hora - T1\_SALARIO**, na rotina **Funcionário da Manutenção - MNTA020**, integrado ao módulo **Gestão de Pessoal - SIGAGPE**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - A partir da versão 12

**Solução**O processo consiste no preenchimento automático do campo **Salário Hora - T1\_SALARIO**com base nas informações contidas na tabela de **Funcionários - SRA**.   
Para utilização deste processo é necessário que os seguintes parâmetros estejam informados:

* **MV\_NGMNTRH** **- Integração Manutenção - MNT com RH**igual a **S** ou **X**;
* **MV\_NGSALHO** **- Define se o campo Salário do Funcionário - T1\_SALARIO da manutenção é integrado com o RH**igual a **S**.

Em seguida, no módulo **Gestão de Pessoal -** **SIGAGPE**, na rotina de **Funcionários -** **GPEA010**, deve-se garantir que o funcionário cadastrado possua os campos **Cod. Processo - RA\_PROCES**e **Salário - RA\_SALARIO**informados. Com o funcionário cadastrado, será necessário incluir um período para o processo, isso deve ser realizado na rotina **Processos - GPEA420**.  
  
Feito isto, no módulo **Manutenção de Ativos -** **SIGAMNT**, ao incluir o funcionário da manutenção pela rotina **Funcionários da Manutenção -** **MNTA020**, informar a matrícula do funcionário no campo **Código Funcionário - T1\_CODFUNC**. Verifique que após este processo, o campo **Salário Hora - T1\_SALARIO**é apresentado fechado e com o conteúdo preenchido.  
  
**Importante**O **Cadastro de Períodos - GPEA400** é obrigatório para clientes que utilizam o **Protheus**, ressalvo os que utilizam a integração **RM x SIGAGPE**, neste caso esse cadastro pode ser desconsiderado.  
  
**Saiba mais**Para informações complementares da integração, verifique [INTEGRAÇÃO GPE X MNT.](https://tdn.totvs.com/pages/viewpage.action?pageId=614701752)
