---
article_id: 4406438085271
category: Financeiro - Contas a Pagar
content_hash: b3c3b59d4d3991ef3de3ee708b02e3a1653a89f7598d62f3e08e8af42636f158
fetched_at: '2026-06-28T22:38:07.189711+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA050 - IRRF Pessoa física não
  respeita alíquota da natureza
type: support-article
updated_at: '2023-04-04T02:10:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406438085271-Cross-Segmento-Backoffice-Linha-Protheus-FINA050-IRRF-Pessoa-f%C3%ADsica-n%C3%A3o-respeita-al%C3%ADquota-da-natureza
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03 min** **Dúvida**FINA050 - IRRF Pessoa física não respeita alíquota da natureza

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**Para que a retenção de IRPF acate um percentual fixo ao invés de utilizar a tabela progressiva, o ED\_JURCAP = SIM.

**Fornecedor Pessoa Física**

O sistema considera a **Tabela IRRF**ou pode utilizar a**alíquota da Natureza.**Alíquota da natureza  
Existem algumas operações onde deve-se utilizar uma alíquota diferente da tabela progressiva, para atender essas situações basta informarmos os seguintes campos no cadastro da natureza :  
calculo do IRRF (**ED\_CALCIRF**) = Sim  
Porcentagem do IRRF (**ED\_PERCIRF**) = 10  
Juros capital (**ED\_JURCAP**) = Sim

Exemplos de operações que utilizam uma alíquota diferente da tabela progressiva:  
Juros de Capital Próprio, Rescisão Contratual, Prêmios em Bens ou serviços e etc.

**Exemplo:**

Ao considerar na inclusão de um título a pagar um fornecedor que seja Pessoa Física, foi definido no Cadastro da Natureza um percentual de alíquota 15% no campo **Porc IRRF**, informando ainda o campo **Calcula IRRF** =Sim e o campo Juros Cap. 1=Sim.  
Ao Informar um valor de R$ 10.000,00 o sistema vai apresentar a seguinte informação, o campo valor será recalculado e vai apresentar o valor de R$ 8500,00, na aba de impostos o sistema vai apresentar no campo de **IRRF** o valor de R$ 1500,00 e no campo de Base do **IRRF** o sistema apresenta o valor de R$ 10.000,00.  
No momento da inclusão, o sistema gera um título a pagar do tipo **TX** com o valor do **IRRF** calculado para a União.  
  
**Saiba mais**  
[Contas a Pagar - FINA050 - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Contas+a+Pagar+-+FINA050+-+Financeiro+-+P12) (Aba impostos)  
[IRRF - Retenção de Imposto de Renda Pessoa Jurídica ou Física](https://totvssuporte.zendesk.com/agent/tickets/16705771)
