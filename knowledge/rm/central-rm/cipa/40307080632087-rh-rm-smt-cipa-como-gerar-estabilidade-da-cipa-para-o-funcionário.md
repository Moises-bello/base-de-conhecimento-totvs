---
article_id: 40307080632087
category: CIPA
content_hash: 262a4e19a93182bda1c0f4d3b478aa8379b1b27e6f3336975b95f8c9d744f7a2
fetched_at: '2026-06-28T22:47:37.632671+00:00'
product: rm
section_id: 1500001076482
source: central-rm
title: 'RH - RM - SMT - CIPA: Como gerar estabilidade da CIPA para o Funcionário'
type: support-article
updated_at: '2026-05-07T18:02:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40307080632087-RH-RM-SMT-CIPA-Como-gerar-estabilidade-da-CIPA-para-o-Funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40307047395607) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Qual o processo correto para geração da estabilidade da CIPA no RM, garantindo que o funcionário eleito como representante dos empregados tenha a estabilidade criada automaticamente na Folha de Pagamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Segurança e Saúde Ocupacional - Todas as versões.  
  
**Solução**  
Regras para geração da Estabilidade da CIPA:  
  
**1. Cadastro do Funcionário como Candidato da Eleição da CIPA**

* Para que o funcionário seja eleito representante da CIPA através do processo de apuração da eleição, é obrigatório que ele esteja previamente cadastrado como **Candidato** na eleição da comissão.  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40307047397911)
* Ao realizar a inclusão manual de representantes dos empregados na CIPA, o sistema também valida se o funcionário consta como candidato na eleição da comissão.
* O funcionário somente poderá ser incluído como representante dos empregados se estiver cadastrado no anexo de candidatos da eleição da respectiva comissão.  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40307047398807)

**2. Geração Automática da Estabilidade**

A estabilidade do representante da CIPA será criada automaticamente na Folha de Pagamento somente quando:

* O representante for eleito pelo processo de apuração da eleição da CIPA; ou
* O representante for incluído manualmente como Representante dos Empregados na comissão.

**3. Como o sistema calcula a estabilidade da CIPA**

A estabilidade do representante da CIPA é calculada considerando:

* Vigência da comissão da CIPA;
* Mais 1 ano adicional de estabilidade.

O cálculo pode ocorrer de duas formas:  
  
**1 – Utilizando Convenção da CIPA parametrizada no SSO**

Quando o módulo SSO estiver parametrizado para utilizar a convenção da CIPA, o sistema definirá automaticamente a vigência da comissão.

Exemplo:

* Convenção parametrizada no RM: 1 ano
* Vigência da CIPA: 01/01/2026 até 01/01/2027
* Término da estabilidade do representante: 01/01/2028

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40307047399447)

Resultado:

O sistema calcula automaticamente:

* Vigência da CIPA;
* Mais 1 ano de estabilidade para o representante eleito.

**2 – Sem parametrização de Convenção da CIPA**

Quando não houver parametrização da convenção no sistema, a vigência da comissão deverá ser informada manualmente.

Mesmo nesse cenário, o sistema continuará aplicando a regra:  
**Vigência da CIPA + 1 ano de estabilidade.**

Exemplo:

* Vigência da CIPA: 01/01/2026 até 01/01/2027
* Término da estabilidade do representante: 01/01/2028

⚠️**Importante**  
Antes de validar a geração da estabilidade, confirme:

* O funcionário está cadastrado como candidato da eleição;
* O representante foi eleito pela apuração ou incluído manualmente como representante dos empregados;
* A comissão da CIPA possui vigência corretamente definida;
* A parametrização da convenção da CIPA está correta no SSO (quando utilizada).

**Saiba Mais**

Para maiores informações, acesse:  
- [RH - RM - SMT - Representante CIPA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019180312)  
- [RH - RM - SMT - Representantes Empregado e Representantes Empregador na CIPA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5866827935639)  
- [RH - RM - SMT - Dúvidas frequentes: CIPA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27279685429911)
