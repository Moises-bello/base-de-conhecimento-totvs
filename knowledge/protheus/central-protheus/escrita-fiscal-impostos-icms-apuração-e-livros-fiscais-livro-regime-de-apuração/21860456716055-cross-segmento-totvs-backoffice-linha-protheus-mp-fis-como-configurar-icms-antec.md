---
article_id: 21860456716055
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 25d69bd120f36fa2dacc53bc735828f09398d803c98ca76b497067ec79f7c727
fetched_at: '2026-06-28T22:39:22.109343+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - MP FIS Como configurar
  ICMS Antecipado RS IN4123?
type: support-article
updated_at: '2026-05-25T18:16:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21860456716055-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-MP-FIS-Como-configurar-ICMS-Antecipado-RS-IN4123
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21860442052247) Tempo aproximado para leitura: 05:00**min**  
  
**Dúvida**  
Como configurar ICMS Antecipado RS IN4123?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Fazer as configurações abaixo:

Configurador CFG  
MV\_ESTADO = RS  
MV\_IN4123 = {"RS001503":"RS021401"}  
MV\_USASPED = .T. - para gerar o bloco E no Sped Fiscal  
MV\_CONFAPU = .T.  
MV\_ICMPAD = 17  
MV\_P9SPED = .F.  
MV\_P9AUTO = .F.  
   
No SM0 a empresa precisa ser RS  
Ter inscrição estadual e CNPJ  
   
Os códigos de lançamento da apuração do ICMS  
RS001503  
RS021401  
Precisam estar dentro da tabela CDO, onde podem ser inseridos da seguinte forma:   
   
1a ) Rotina mata964 de forma manual  
![](https://totvssuporte.zendesk.com/attachments/token/WzMHaN9oh87P3WIePnXJgIOl7/?name=image.png)  
2a) Importando a tabela 51 do Site do Sped e rodando o U\_IMPSPED  
[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como atualizar os códigos de ajuste/lançamentos manuais da apuração de ICMS (tabelas 51 "CDO" e 53 "CC6")?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021994671-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-atualizar-os-c%C3%B3digos-de-ajuste-lan%C3%A7amentos-manuais-da-apura%C3%A7%C3%A3o-de-ICMS-tabelas-51-CDO-e-53-CC6?source=search)  
   
A configuração da TES pode ser de TRÊS formas:  
   
**1) Compra para Consumo**  
Calcula ICMS = Sim  
L. Fiscal ICMS =Outros  
Calc. Dif ICM = Sim  
Material de Consumo = Sim  
Antecip. ICMS = Sim  
   
![](https://totvssuporte.zendesk.com/attachments/token/3YsiQe4I0OQnOtw7ptHhod0Ye/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/EUf48424uRJKmNLprjfgfzQdZ/?name=image.png)  
Reflexo usado o padrão do U\_IMPSPED 00000050  
   
**2) Compra para Industrialização ou Comercialização:**  
Calcula ICMS = Sim  
L. Fiscal ICMS = Diferente de Não  
Calc. Dif ICM = Não  
Material de Consumo = Não  
Antecip. ICMS = Sim  
MKP icm comp = não  
Marg solid = em branco  
   
![](https://totvssuporte.zendesk.com/attachments/token/mP6jrDtrfIjL5zT9kShYJ3QMX/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/B1eEAuquCsmJfkgA9FzZVAaFX/?name=image.png)  
   
**3) Compra com ICMS-ST:**  
Para que o cálculo da Antecipação tributária total (ICMS-ST) seja feito, siga as instruções:

1. No **Livros Fiscais (SIGAFIS)** acesse **Atualizações/** **Cadastro de TES (MATA080)**configure o campo
2. Informe o campo **Antecipação Tribut. ICMS (F4\_ANTICMS)** tratando-se de estabelecimento atacadista, inclusive distribuidor.
3. Para o valor da Antecipação tributária total (ICMS-ST) ser apresentado corretamente na apuração de ICMS-ST, preencha o campo **Solidário na Observação (F4\_OBSSOL)** com **SIM**.
4. MKP ICM COMP = não
5. Marg solid = nunca

   
Cadastro de produtos  
Solid entrada = 0,01  
   
![](https://totvssuporte.zendesk.com/attachments/token/ivJub5nigzwvbjSO5nM6XnOBS/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/u8bxTgowDHRO7lkP36oRvCITc/?name=image.png)  
   
Apuração do ICMS mês 03/2024  
   
Considera Filiais = sim  
de 01  
até 01  
Seleciona Filiais = sim  
   
![](https://totvssuporte.zendesk.com/attachments/token/HxOb85rz8bXcjcKVEKoB1uKdV/?name=image.png)  
   
Apuração do ICMS mês 04/2024  
![](https://totvssuporte.zendesk.com/attachments/token/Nh9Bs1IWq2lXnZKj0FjFg7Eg4/?name=image.png)  
   
Relatório de correção  
![](https://totvssuporte.zendesk.com/attachments/token/4DuY3SGPn3MnuovtptJ0riboa/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/3gY41Oxhszy0CbWKap2wrrmiO/?name=image.png)  
   
O sistema calculou o ICMS antecipado das três situações, mercadoria para consumo, mercadoria para revenda e ICMS antecipado  
   
Após a entrada das notas fiscais, os campos F3\_VALANTI / F3\_ANTICMS ficaram preenchidos.
