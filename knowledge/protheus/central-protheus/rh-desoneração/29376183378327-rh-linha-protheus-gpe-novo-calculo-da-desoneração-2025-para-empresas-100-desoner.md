---
article_id: 29376183378327
category: RH - Desoneração
content_hash: 2c25a2679d63b83858f7ad94ef4721423e998f70f0cdad22b8a905914e5fcee6
fetched_at: '2026-06-28T22:43:42.217560+00:00'
product: protheus
section_id: 360003109152
source: central-protheus
title: RH - Linha Protheus - GPE - Novo Calculo da Desoneração 2025 para empresas
  100% desonerada
type: support-article
updated_at: '2025-06-02T13:25:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29376183378327-RH-Linha-Protheus-GPE-Novo-Calculo-da-Desonera%C3%A7%C3%A3o-2025-para-empresas-100-desonerada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29376183345559) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como será efetuado o calculo da reoneração progressiva da folha de pagamento para empresas 100% desonerada a partir de 2025?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução** **1.** Preencher os campos Aliquota Folha Desonerada e Aliquota s/ Faturamento na tabela S037 (caminho Atualização / Definições de Calculo / Manutenção de Tabelas) conforme a legislação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29376186179863)

A tabela S033 permaneceu inalterada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29376186181783)

**2.** Cálculo da folha de pagamento

Calcule a folha de pagamento, efetue a conferencia e ajustes necessários.  
**OBS:** Neste passo a verba de ID 0148 (INSS Empresa) não será apresentada.

Folha Individual

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29376183349911)

Folha Geral

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29376186184471)

**3.** Cálculo da Desoneração

Após a conferencia da folha e ajustes efetuados, rodar a desoneração através do caminho Miscelânea / Cálculos / Desoneração Folha.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29376186186007)

**OBS:** Caso não possua o módulo Faturamento, ou não tenha a configuração da desoneração no módulo faturamento, a Tabela S033 deve ser preenchida antes de calcular a desoneração e o parâmetro Verificar Integração deverá ser preenchido com "NÃO"

Caso possua o modulo Faturamento configurado para a desoneração o campo Verificar Integração deverá ser preenchido com "Faturamento" e a tabela S033 será preenchida automaticamente após finalização do processo.

**4.** Log de ocorrências do cálculo da desoneração

Após a finalização do cálculo da desoneração será gerado o log de ocorrências conforme a Tabela S037 e S033.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29376186186903)

**5.** Verificação dos valores na folha de pagamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29376186188439)

Memória de cálculo

**INSS Empresa - ID 0148**  
(verba 703) 67.334,08 + (verba 704) 3.706,92 = 71.041,00 \* 5% = **3.552,05** (verba 747)

**INSS Faturamento - ID 0973**  
Contribuição Devida Tabela S033 74.622,48 \* 80% = **59.697,98** (verba 879)

**Observações**:

- Após calcular a desoneração **não** é necessário realizar novamente o cálculo da folha para assumir os valores de desoneração, pois esse processo é realizado durante o cálculo da desoneração.

- Para que a verba de ID 0973 (INSS Faturamento) seja apresentada no relatório da folha é necessário que  o parâmetro Impr. Total Filial esteja parametrizado com "**SIM**".

**Saiba mais:**

[Artigos RH -  Desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109152-RH-Desonera%C3%A7%C3%A3o)

<https://tdn.totvs.com/pages/releaseview.action?pageId=892132807>
