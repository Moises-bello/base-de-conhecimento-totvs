---
article_id: 360017468072
category: RH - Cálculo PLR
content_hash: 2f81d15391bccec2b555237d6d8b2de53211fdeb36720fb264a15587278fdd14
fetched_at: '2026-06-28T22:43:12.901746+00:00'
product: protheus
section_id: 360010855894
source: central-protheus
title: RH - Linha Protheus - GPE - Parametrização do cálculo de IR para valores de
  PLR
type: support-article
updated_at: '2026-02-10T17:58:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017468072-RH-Linha-Protheus-GPE-Parametriza%C3%A7%C3%A3o-do-c%C3%A1lculo-de-IR-para-valores-de-PLR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24990230294295) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Parametrização do cálculo de IR para valores do roteiro PLR*.*  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Causa**  
Ao efetuar o cálculo de PLR, foi apresentado a base de IR maior do que o valor pago ao funcionário, devido a data errada no campo Ano Ref. Cál. no cadastro de sindicatos.

**Solução**  
**1.** Cadastre o IR da PLR em **Atualizações> Definições Cálculo> Manutenção Tabelas (GPEA320)> S044-Tabela de IR para PLR:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38303627470103)

**2.** Cadastre as verbas com os IDs de PLR em **Atualizações > Definições cálculo >Verbas (GPEA040)**. As informações contidas nesta rotina serão armazenadas na tabela**SRV.**  
- Cadastre uma verba com ID p/ Cálculo**0151** - Pagamento PLR - **Verba de Provento**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24990230299031)**  
  
- Cadastre uma verba com ID p/ Cálculo**0152** - IRRF PLR - **Verba de Desconto**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24990241115159)**  
  
- Cadastre uma verba com ID p/ Cálculo**0300** - Ded. Dep. IR PLR - **Verba de Base (Provento)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24990241117463)**  
  
- Cadastre uma verba com ID p/ Cálculo**0835**- Base IRRF PLR - **Verba de Base (Provento)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24990241123351)**  
  
- Cadastre uma verba com ID p/ Cálculo**0836** - Liquido PLR - **Verba de Base (Provento)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24990230307735)**  
  
- Cadastre uma verba com ID p/ Cálculo **1279** - Desconto 1ª parcela PLR - **Verba de Desconto**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24990230310423)

Para realizar a **conferência** das **bases** de cálculo do **PLR**, realize os seguintes passos:  
  
**1.** No Módulo SIGAGPE, acesse **Cadastro > Consulta > Genérico** [RH - Linha Protheus - GPE - Como gerar tabela em planilha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060836073-RH-Linha-Protheus-GPE-Como-gerar-tabela-em-planilha?source=search);  
  
**2.** Busque a tabela **SRD - Histórico de movimento**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24990241129751)  
**3.** Exp. CSV (Exporte os dados em excel) e filtre a **verba provento** correspondente ao **pagamento do PLR (id 0151)** e matricula do funcionário que está sendo calculado para identificar se já existe um pagamento anterior referente ao PLR no mesmo ano.   
  
**4.** Acesse o cadastro de **sindicatos** veja se na aba **PLR,** no campo **Ano Ref. Cál.** está preenchido de acordo com o ano que refere o pagamento.   

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406210667543)  
  
O sistema buscará na tabela SRD, referente ao ano calendário que está sendo realizado o pagamento da verba de id 0151 (coluna RD\_DTREF), para que possa realizar a base de cálculo do imposto de renda.

**Saiba Mais**

[RH - Cálculo PLR](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010855894-RH-C%C3%A1lculo-PLR)
