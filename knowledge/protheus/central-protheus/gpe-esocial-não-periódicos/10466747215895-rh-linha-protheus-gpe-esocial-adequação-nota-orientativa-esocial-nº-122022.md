---
article_id: 10466747215895
category: GPE - eSocial - Não Periódicos
content_hash: b9d3c6ee4c59e9b39c165cf7aa14c794769f468945e7c1277a15241c3484223f
fetched_at: '2026-06-28T22:45:04.339103+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Adequação Nota Orientativa eSocial  Nº
  12/2022
type: support-article
updated_at: '2026-06-16T11:26:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10466747215895-RH-Linha-Protheus-GPE-eSocial-Adequa%C3%A7%C3%A3o-Nota-Orientativa-eSocial-N%C2%BA-12-2022
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22902169178263) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Adequação para Nota Orientativa eSocial S-1.0 Nº 12/2022.  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
**§3º**–Quando não for possível que a gestante ou a lactante afastada nos termos do caput deste artigo exerça suas atividades em local salubre na empresa, a hipótese será considerada como gravidez de risco e ensejará a percepção de salário-maternidade, nos termos da Lei nº 8.213, de 24 de julho de 1991, durante todo o período de afastamento.   
Conforme *link*: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-orientativa-s-1-0-12-2022.pdf>  
  
**Solução**

Criada nova rotina para cadastro de **Período de Gestação** - opção disponibilizada em **Outras Opções do Cadastro de Funcionários (GPEA010)** e também dentro das opções de Funcionários da rotina de **Gestão de Funcionários (GPEA011)**.   
  
Inclusão de tratamento para identificar que a funcionária é gestante, e qual o período de gestação, no qual a mesma deve estar alocada em ambiente salubre, porém continuando a receber o adicional de insalubridade.

* A rotina permite **incluir Data Inicial e Final do período de gestação**. A **data inicial deve ser maior ou igual à data inicial do período aberto da folha** e, também **maior ou igual à data de admissão.**
* Rotina **disponível apenas** para cadastros pertencentes ao **sexo feminino (F)**.
* Data Final deve ser **1 dia anterior à saída de licença maternidade**.
* Quando possuir período de gestação cadastrado ativo, **a insalubridade será gravada pelo novo ID de cálculo 1423** Insalubridade Gestante para poder ser feita a dedução do valor pago na GPS.

Utilizar o ID 1423 Insalubridade Gestante para realizar os controles conforme a Nota Orientativa.

Será necessário **criar uma verba correspondente do tipo 3 Base Provento**, para que seja armazenado o mesmo valor da verba com ID 1423, **com natureza 1202 -Adicional de insalubridade** e com o campo **(RV\_INCCP) preenchido com o código 51**, para que o valor informado possa constar como parcela dedutível das contribuições devidas.

Colocar no campo **RV\_CODCORR (Cod.Corresp),** da verba com ID 1423, o código da verba de Base Provento criada.  
  
Para cadastro do Período de Gestação, acesse Atualização > Funcionários > **Funcionários** ou Atualização > Funcionários > **Gestão Funcionários**.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10466710061847)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
