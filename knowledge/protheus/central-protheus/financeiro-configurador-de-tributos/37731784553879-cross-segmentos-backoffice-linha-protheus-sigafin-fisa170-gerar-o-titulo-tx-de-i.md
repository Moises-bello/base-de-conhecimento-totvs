---
article_id: 37731784553879
category: Financeiro - Configurador de Tributos
content_hash: 65d2b3c635df0ed32ca39e4a8f4000f25b86c1a76e7f5ba743924c631a17ebeb
fetched_at: '2026-06-28T22:37:46.231226+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Gerar o titulo
  TX de IR sem cumulatividade
type: support-article
updated_at: '2026-01-16T20:27:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37731784553879-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Gerar-o-titulo-TX-de-IR-sem-cumulatividade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37731784544535) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Geração do título TX de IR sem cumulatividade para valor inferior a R$ 10,00 via Configurador de Tributos  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Para o cadastro da regra de cumulatividade no Configurador de Tributos do Financeiro (por exemplo a cumulatividade do IR), é necessário cadastrar a regra de cumulatividade e vinculá-la à(s) regra(s) Financeira(s) do(s) tributo(s) que a compõem.

Como os cadastros de **Regra de Retenção** e a **Regra Financeira** não permitem alterações, só versionamentos, o ideal é que o **1º passo** seja cadastrar a regra de **cumulatividade**, vinculando ao menos uma (1)**Regra Financeira** existente, só para realizar o vinculo dessa **Regra de Retenção**. Por último, uma vez que todas as **Regras Financeiras** estiverem cadastradas, retorne até a **Regra de Cumulatividade** e altere-a, realizando o vinculo com as regras financeiras definitivas.

1. **Exemplo de um cadastro de Regra de Título**

   No cadastro de título, incluir dados do(s) título(s) que será gerado no módulo Financeiro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37732598485271)

No cadastro de **cumulatividade**, vamos cadastrar um código para a cumulatividade do **IR** e vincular uma regra qualquer, apenas para conclusão do cadastro.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37732569947159)

Uma vez cadastrada a cumulatividade, podemos vincular essa mesma regra à regra de retenção do **IR****.**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/37732598486807)**

No cadastro de **Regra Financeira**, atrelar essa regra de Retenção que será utilizada com a regra de cumulatividade. Assim:  
  
Aba Dados Gerais:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37732569949079)

Aba Regra Gerais:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37732598489111)

Por último, vinculamos essas regras Financeira ao cadastro da regra de cumulatividade inicialmente cadastrada. Assim:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37732598490263)

**2. Cadastro de fornecedor.**  
No **cadastro do fornecedor**, criado sem configuração de impostos, vincule a **regra financeira** em **Outras Ações → Tipos de Retenções**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37734417139095)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37734390008983)

**3. Cadastro da natureza.**  
No**cadastro de** **natureza,** criado sem parametrização de impostos, vincule a **regra financeira** em **"Tipo de retenção x natureza",**conforme exemplo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37734390010263)  
  
**4.**Exemplo de inclusão de um título no **Contas a Pagar**, utilizando a configuração da rotina **FISA170 – Configurador de Tributos**, com a geração dos impostos **IR com valor menor que R$ 10,00**  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37734390015255)

**Saiba mais**  
[Regra de cumulatividade de tributo](https://tdn.totvs.com/display/public/PROT/Regra+de+cumulatividade+de+tributo)  
[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com/display/PROT/Configurador+de+Tributos+-+Regras+Financeiras#01-01)  
[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
