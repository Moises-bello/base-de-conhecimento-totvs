---
article_id: 37565957361815
category: Financeiro - Reinf
content_hash: 94a073713e94118328b32edbec92d98fffe535711b1f48eac55837fe8d0905bd
fetched_at: '2026-06-28T22:37:51.839481+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Lei 15.270/2025
  - Reforma do Imposto de Renda 2026 - Tributação sobre a distribuição de lucros e
  dividendos para titulo com o origem do modulo Financeiro
type: support-article
updated_at: '2026-02-05T12:19:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37565957361815-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Lei-15-270-2025-Reforma-do-Imposto-de-Renda-2026-Tributa%C3%A7%C3%A3o-sobre-a-distribui%C3%A7%C3%A3o-de-lucros-e-dividendos-para-titulo-com-o-origem-do-modulo-Financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37565957335447) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como será a tributação sobre a distribuição de lucros e dividendos para titulo com o origem do modulo Financeiro - Lei 15.270/2025 - Reforma do Imposto de Renda 2026 ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Para configurar um **título a pagar** para calcular **IRRF** sobre **lucros e dividendos**, ou seja, quando o pagamento for superior a R$ 50 mil por beneficiário/fornecedor (conforme a Lei 15.270/2025) e sem a utilização do [Configurador de Tributos](https://tdn.totvs.com/pages/releaseview.action?pageId=448600884), realize os passos a seguir:

**1.** Cadastre uma Natureza Financeira (tabela SED) com as seguintes características:

* Calcula IRRF (**ED\_CALCIRF**) igual a  '**S=Sim**'
* Porc. IRRF (**ED\_PERCIRF**) igual a '**10%**'
* Juros Cap. (**ED\_JURCAP**) igual a '**1=Sim**

**2.** No cadastro de fornecedor preencher o campo **Tipo (A2\_TIPO) igual a "F= Pessoa Física"** e o campo **Cálc. IRRF (A2\_CALCIRF) igual a  '2= IRRF Baixa'**

* Na inclusão do título a pagar, preencha:  
  O código de retenção "**1841**" de lucros/dividendos no campo Cód. Retenção (**E2\_CODRET**). O preenchimento desse campo tem influencia no calculo de cumulatividade do tributo;
* O código da natureza de rendimento "**12001**" no campo Nat. Rendimento (**FKF\_NATREN**).  O preenchimento desse campo tem influencia no envio dos dados para o TAF referente a entrega do EFD-Reinf

**Importante:** Para pagamentos abaixo de R$ **50.000,00**, deve ser utilizada uma natureza configurada para **não realizar retenção de IR**;

**3.** Necessário o ambiente estar com o patch de atualização segue os links   
  
12.1.2210:<https://r.totvs.io/p/1233206> ;   
12.1.2310:<https://r.totvs.io/p/1233207> ;   
12.1.2410:<https://r.totvs.io/p/1233208> ;   
12.1.2510:<https://r.totvs.io/p/1233205> ;

**Obs.** informamos que está previso para o mês de fevereiro a disponibilização de um pacote de atualização que contemplará a evolução do sistema para atender a nova legislação quando utilizado via Configurador de Tributos. Nesse novo formato, será possível parametrizar o valor limite, permitindo que o sistema realize o cálculo de forma automática. Para casos onde continuará sendo utilizado o formato de cálculo legado (via TES e/ou natureza) os lançamentos deverão utilizar as devidas naturezas previamente cadastradas e configuradas.  
  
**Saiba mais:**  
[Lei 15.270/2025 - Reforma do Imposto de Renda 2026](https://tdn.totvs.com/pages/viewpage.action?pageId=1027817283)  
<https://www.totvs.com/blog/fiscal-clientes/nova-lei-do-irpf-reducao-para-baixa-renda-e-tributacao-minima-para-altas-rendas/>

[Cálculo de IRRF para fornecedor pessoa física s/ tabela progressiva (ED\_JURCAP)](https://tdn.totvs.com/pages/viewpage.action?pageId=756477961)

[IRRF de autônomo com dedução simplificada (MP 1.171/2023)](https://tdn.totvs.com/pages/viewpage.action?pageId=773900973)

[IRRF - Tabela Progressiva de Cálculo de Imposto de Renda Pessoa Física](https://tdn.totvs.com/pages/viewpage.action?pageId=695202577)

[Utilização dos parâmetros MV\_F15270A, MV\_F15270B, MV\_F15270C, MV\_F15270D e MV\_F15270E](https://tdn.totvs.com/pages/viewpage.action?pageId=1027818954)
