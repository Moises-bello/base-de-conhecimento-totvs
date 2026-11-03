---
article_id: 19996675214231
category: Financeiro - Reinf
content_hash: 8b3ffe8b10956bd2199cfba7554bb9b0c227971e02e085dc165d8411fd6e51ca
fetched_at: '2026-06-28T22:37:51.695689+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CPF's rateio de IRRF
  progressivo
type: support-article
updated_at: '2025-10-17T20:05:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19996675214231-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CPF-s-rateio-de-IRRF-progressivo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26493080379287)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**

Como cadastrar o IRRF progressivo?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. No Financeiro (SIGAFIN), acesse **Atualizações / Cadastros / Fornecedores (MATA020)**.

**Aba/cadastrais/ - Campo Tipo:** J - Jurídico

**Aba/Admin/Fin. - Campo CPF IR Progr:** (Informe o CPF principal)

**Aba/Fiscais. -**

**Campo Cálc. IRRF:** configuração do IRRF para o Reinf. Link documentação:

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - IR Simplificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17448867907351-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-IR-Simplificado#:~:text=Trata%2Dse%20da%20Dedu%C3%A7%C3%A3o%20Simplificada,baseado%20na%20tabela%20de%202024)

**Campo** **IRRF Prog:** Sim

**Campo IR Simpl:**1 - Sim

Após o preenchimento dos campos acima em **"Outras** **Ações"**, clicar em **CPFs IR Progr.**

Caso não tenha sido preenchida a **Aba/Admin/Fin**, será exibida a mensagem para preenchimento do campo obrigatório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19996675179927)

Na tela dos cadastros, informar os CPFs, porcentagem e nome

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19996722054551)

**Importante:**   
Soma do percentual de todos os **CPFs** cadastrados deverá ser 100%.

2. Preencher o parâmetro **MV\_RETIRRT = 3208**

Link Documentação:

[Utilização do parâmetro MV\_RETIRRT](https://tdn.totvs.com/pages/releaseview.action?pageId=547241966)

3. Cadastre o título a pagar pela rotina **Contas a Pagar/Documento de Entrada:** informando uma natureza e fornecedor que calculam **IR na emissão**.

4. Ao informar o valor do título, será calculado o valor do IR considerando 100% do valor para o fornecedor. O rateio do IR somente irá ocorrer ao informar o campo **"Gera Dirf"**  = Sim e o **código de retenção** pertencente no parâmetro **[MV\_RETIRRT](https://tdn.totvs.com/x/7j_eI)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19996722061079)

5. Após a inclusão do título, será gerado o **TX** do **IRRF** rateado pelos **CPFs** cadastrados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19997248904855)

6. Ao rodar o extrator fiscal, será gerado o registro **T154** para cada **CPF**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19997263638807)

7. No **Painel do TAF,** serão separados os registros também para cada **CPF**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19997248923543)

**Saiba mais**

[Cadastro de CPF's rateio de IRRF progressivo enviado a DIRF](https://tdn.totvs.com/display/public/PROT/Cadastro+de+CPF%27s+rateio+de+IRRF+progressivo+enviado+a+DIRF)

[IRRF - Divisão dos rendimentos de aluguel entre proprietários](https://tdn.totvs.com/pages/releaseview.action?pageId=527836834)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Como gerar o IRRF no Reinf?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19671600360855)
