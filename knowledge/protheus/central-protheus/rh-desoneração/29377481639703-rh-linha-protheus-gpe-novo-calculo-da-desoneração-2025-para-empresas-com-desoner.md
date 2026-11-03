---
article_id: 29377481639703
category: RH - Desoneração
content_hash: b101e1e2986db3233bf1d1a4746b2ccf3a8f3439cd41ab1e61b357cf9ad93f75
fetched_at: '2026-06-28T22:43:42.226833+00:00'
product: protheus
section_id: 360003109152
source: central-protheus
title: RH - Linha Protheus - GPE - Novo Calculo da Desoneração 2025 para empresas
  com desoneração Mista
type: support-article
updated_at: '2025-10-10T12:32:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29377481639703-RH-Linha-Protheus-GPE-Novo-Calculo-da-Desonera%C3%A7%C3%A3o-2025-para-empresas-com-desonera%C3%A7%C3%A3o-Mista
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29377488364183) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como será efetuado o calculo da reoneração progressiva da folha de pagamento para empresas com desoneração Mista a partir de 2025?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

**1.** Preencher os campos Aliquota Folha Desonerada e Aliquota s/ Faturamento na tabela S037 (caminho Atualização / Definições de Calculo / Manutenção de Tabelas) conforme a legislação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29377488364567)

A tabela S033 permaneceu inalterada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29377481618199)

**2.** Cálculo da folha de pagamento

Calcule a folha de pagamento, efetue a conferencia e ajustes necessários.  
**OBS:** Neste passo a verba de ID 0148 (INSS Empresa) não será apresentada.

Folha Individual

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29377488366615)

Folha Geral

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29377481621527)

**3.** Cálculo da Desoneração

Após a conferencia da folha e ajustes efetuados, rodar a desoneração através do caminho Miscelânea / Cálculos / Desoneração Folha.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29377488368791)

**OBS:** Caso não possua o módulo Faturamento, ou não tenha a configuração da desoneração no módulo faturamento, a Tabela S033 deve ser preenchida antes de calcular a desoneração e o parâmetro Verificar Integração deverá ser preenchido com "NÃO"

Caso possua o modulo Faturamento configurado para a desoneração o campo Verificar Integração deverá ser preenchido com "Faturamento" e a tabela S033 será preenchida automaticamente após finalização do processo.

**4.** Log de ocorrências do cálculo da desoneração

Após a finalização do cálculo da desoneração será gerado o log de ocorrências conforme a Tabela S037 e S033.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29377488369815)

- **Calculo da alíquota reduzida dos 20% (folha onerada) não houve alteração**

Tipo da Receita 2 (não desonerada conforme Tabela S033) = **830.000,00**   
>Receita Total = 1.658.277,33 (valor base para cálculo receita tipo 1) + 830.000,00 (valor base para cálculo receita tipo 2) = **2.488.277,33**  
>Receitas de Outras atividades / Receita Bruna Total = 830.000,00 / 2.488.277,33 = 0,3335641  
>Coeficiente de redução = 0,3335641  
>Alíquota Padrão = 20% conforme a tabela S037  
>Coeficiente de redução X Alíquota padrão = 0,3335641 x 20% = 6,67%  
>Alíquota reduzida = **6,67%**

- **Calculo da alíquota sobre a folha desonerada**

Tipo da Receita 1 (desonerada conforme Tabela S033) = **1.658.277,33**  
>Receita Total = 1.658.277,33 (valor base para cálculo receita tipo 1) + 830.000,00 (valor base para cálculo receita tipo 2) = **2.488.277,33**  
>Receitas Desoneradas / Receita Bruna Total = 1.658.277,33 / 2.488.277,33 = 0,6664359  
>Coeficiente de redução = 0,6664359  
>Alíquota Desonerada = 5% conforme a tabela S037  
>Coeficiente de redução X Alíquota Desonerada = 0,6664359 x 5% = 3,3325%  
>Alíquota Desonerada = **3,3325%**

**5.** Verificação dos valores na folha de pagamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29377488370455)

Memória de cálculo

**INSS Empresa - ID 0148**

Base INSS \* Aliquota Reduzida

(verba 703) 67.334,08 + (verba 704) 3.706,92 = 71.041,00 \* 6,67% = **4.738,43**

Base INSS \* Aliquota Desonerada

(verba 703) 67.334,08 + (verba 704) 3.706,92 = 71.041,00 \* 3,3325% = **2.367,44**

**Total INSS Empresa - ID 0148**

4.738,65 + 2.367,22 = **7.105,87** (verba 747)

**INSS Faturamento - ID 0973**

Contribuição Devida tabela S033 \* 80%

74.622,48 \* 80% = **59.697,98** (verba 879)

**Observações**:

- Após calcular a desoneração **não** é necessário realizar novamente o cálculo da folha para assumir os valores de desoneração, pois esse processo é realizado durante o cálculo da desoneração.

- Para que a verba de ID 0973 (INSS Faturamento) seja apresentada no relatório da folha é necessário que  o parâmetro Impr. Total Filial esteja parametrizado com "**SIM**".

**Saiba mais:**

[Artigos RH -  Desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109152-RH-Desonera%C3%A7%C3%A3o)

<https://tdn.totvs.com/pages/releaseview.action?pageId=892132807>
