---
article_id: 37117146635543
category: esocial - Periódicos
content_hash: 1b75c50fe8f6f799cd467b852baa184033730b3cadb81aa893543422a6634f11
fetched_at: '2026-06-28T22:47:09.173681+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Base de INSS sobre o 13º salário - Apuração Contribuição
  Patronal - Empresa Desonerada
type: support-article
updated_at: '2026-04-08T20:55:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37117146635543-RH-RM-FOP-eSocial-Base-de-INSS-sobre-o-13%C2%BA-sal%C3%A1rio-Apura%C3%A7%C3%A3o-Contribui%C3%A7%C3%A3o-Patronal-Empresa-Desonerada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37117146618519) Tempo aproximado para leitura: 00:03:00 min**  
  
**Dúvida**  
Base de INSS sobre o 13º salário, há apuração de Contribuição Patronal em empresas desoneradas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
  
**Solução**  
Conforme a **Lei nº 14.973/2024**, **não há incidência de Contribuição Patronal de INSS** (art. 22, incisos I e III, da Lei nº 8.212/1991) **sobre o 13º salário para empresas optantes pela desoneração da folha de pagamento**.

Mesmo com a **reoneração gradual da folha mensal a partir de 2025**, o **13º salário permanece isento da cota patronal** durante o período de transição (**2025 a 2027**). Portanto, a **ausência de INSS patronal no cálculo do 13º é comportamento esperado e correto no sistema**, desde que a empresa esteja devidamente enquadrada como desonerada.

**Importante:** A não incidência da Contribuição Patronal **aplica-se exclusivamente às empresas desoneradas**. Para empresas **oneradas**, o cálculo permanece com a **alíquota normal**.

**Regras por Enquadramento**

1. Empresas Oneradas (Regime Geral)

* **INSS Patronal:** Incide normalmente à alíquota de **20%** sobre a folha mensal **e sobre o 13º salário**.
* **RAT e Terceiros:** Incidem normalmente sobre a base do **13º salário**.

2. Empresas Desoneradas (Regime de Transição – 2025 a 2027)

* **Folha Mensal:** Sujeita à reoneração gradual, conforme abaixo:
  + **2025:** 5%
  + **2026:** 10%
  + **2027:** 15%
* **13º Salário:** **Não há incidência de Contribuição Patronal** de INSS sobre o 13º salário durante o período de transição.
* **Identificação no eSocial:** A base do 13º isenta da cota patronal é identificada pelo **Tipo de Valor 51** no evento **S-5001**.

**Validação no RM**

Para validar corretamente esse cenário no **TOTVS RM**, siga os passos abaixo:

1. Verificar o enquadramento da empresa

* Acesse o **cadastro da empresa** no RM;
* Confirme se a empresa está **optante pela desoneração da folha** no período do cálculo.

2. Validar as rubricas do 13º salário

* Acesse o **cadastro das rubricas** utilizadas no 13º;
* Confirme a **classificação correta para 13º salário**;
* Verifique a **incidência de INSS**, garantindo que **não haja cálculo de INSS patronal** para empresas desoneradas.

3. Analisar o cálculo do 13º salário

* Execute o cálculo da **1ª ou 2ª parcela do 13º**;
* Confirme que o sistema calcula **apenas as contribuições do empregado**, quando aplicável;
* Verifique que **não é gerado INSS patronal**.

4. Validar os eventos no eSocial

* Analise os eventos periódicos do 13º salário (**S-1200 / S-1210**);
* Confirme que a **base de INSS** não apresenta valores de **cota patronal**.

5. Conferir a apuração na DCTFWeb

* Acesse a **DCTFWeb** do período do 13º;
* Verifique que **não há débito de INSS patronal** relacionado ao 13º salário.

**Importante:**

A **ausência de INSS patronal sobre o 13º salário** para empresas **desoneradas** está **em conformidade com a legislação vigente** e **não caracteriza erro de cálculo ou falha de parametrização** no TOTVS RM. Para empresas **oneradas**, o recolhimento do INSS patronal sobre o 13º salário **permanece obrigatório**, conforme regra geral.

**Link para maiores informações**  
<https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-orientativa-s-1-3-01-2024.pdf>
