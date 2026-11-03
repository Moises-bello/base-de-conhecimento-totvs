---
article_id: 29377900545175
category: RH - Desoneração
content_hash: fb9187de063e5379fa16ecfa473b878f084ac4b458582260c6ba2d27612e3f33
fetched_at: '2026-06-28T22:43:42.233046+00:00'
product: protheus
section_id: 360003109152
source: central-protheus
title: RH - Linha Protheus - GPE - Novo Calculo da Desoneração 2025 para empresas
  com desoneração Mista que possui 95% ou mais do faturamento desonerado
type: support-article
updated_at: '2025-01-21T16:27:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29377900545175-RH-Linha-Protheus-GPE-Novo-Calculo-da-Desonera%C3%A7%C3%A3o-2025-para-empresas-com-desonera%C3%A7%C3%A3o-Mista-que-possui-95-ou-mais-do-faturamento-desonerado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29377900519191) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como será efetuado o calculo da reoneração progressiva da folha de pagamento para empresas com desoneração Mista a partir de 2025 e que possui 95% ou mais do faturamento desonerado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

**1.** Preencher os campos Aliquota Folha Desonerada e Aliquota s/ Faturamento na tabela S037 (caminho Atualização / Definições de Calculo / Manutenção de Tabelas) conforme a legislação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29377900521239)

A tabela S033 permaneceu inalterada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29377906906007)

**2.** Cálculo da folha de pagamento

Calcule a folha de pagamento, efetue a conferencia e ajustes necessários.  
**OBS:** Neste passo a verba de ID 0148 (INSS Empresa) não será apresentada.

Folha Individual

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29377900528023)

Folha Geral

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29377900531351)

**3.** Cálculo da Desoneração

Após a conferencia da folha e ajustes efetuados, rodar a desoneração através do caminho Miscelânea / Cálculos / Desoneração Folha.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29377906908311)

**OBS:** Caso não possua o módulo Faturamento, ou não tenha a configuração da desoneração no módulo faturamento, a Tabela S033 deve ser preenchida antes de calcular a desoneração e o parâmetro Verificar Integração deverá ser preenchido com "NÃO"

Caso possua o modulo Faturamento configurado para a desoneração o campo Verificar Integração deverá ser preenchido com "Faturamento" e a tabela S033 será preenchida automaticamente após finalização do processo.

**4.** Log de ocorrências do cálculo da desoneração

Após a finalização do cálculo da desoneração será gerado o log de ocorrências conforme a Tabela S037 e S033.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29377906909719)

**OBS:** Pela regra da Receita federal, empresas com mais de 95% do faturamento desonerado são consideradas 100% desoneradas, portanto, o cálculo da verba de ID 0148 referente a folha desonerada será calculada com base na folha cheia, sem abatimentos. Da mesma forma, a verba de ID 0973 terá como base não apenas a receita desonerada cadastrada na tabela S033 (Tipo de Receita = 1), mas também a receita onerada (Tipo de Receita = 2).

**5.** Verificação dos valores na folha de pagamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29377906910487)

Memória de cálculo

**INSS Empresa - ID 0148**  
(verba 703) 67.334,08 + (verba 704) 3.706,92 = 71.041,00 \* 5% = **3.552,05** (verba 747)

**INSS Faturamento - ID 0973**  
Tipo Receita 1 1.658.277,33 + Tipo Receita 2 70.000,00 \* 4,5% = 77.772,48 \* 80% = **62.217,99** (verba 879)

**Observações**:

- Após calcular a desoneração **não** é necessário realizar novamente o cálculo da folha para assumir os valores de desoneração, pois esse processo é realizado durante o cálculo da desoneração.

- Para que a verba de ID 0973 (INSS Faturamento) seja apresentada no relatório da folha é necessário que  o parâmetro Impr. Total Filial esteja parametrizado com "**SIM**".

**Saiba mais:**

[Artigos RH -  Desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109152-RH-Desonera%C3%A7%C3%A3o)

<https://tdn.totvs.com/pages/releaseview.action?pageId=892132807>
