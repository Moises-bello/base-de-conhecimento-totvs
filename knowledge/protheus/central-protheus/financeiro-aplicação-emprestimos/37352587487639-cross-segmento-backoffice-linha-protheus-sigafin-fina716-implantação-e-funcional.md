---
article_id: 37352587487639
category: Financeiro - Aplicação / Emprestimos
content_hash: d15907755008777ed5a0c4cc64547c6334c04a9f95f2ce523b094be0b3ad6137
fetched_at: '2026-06-28T22:37:59.445474+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA716 - Implantação
  e Funcionalidades
type: support-article
updated_at: '2026-01-05T10:38:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37352587487639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Implanta%C3%A7%C3%A3o-e-Funcionalidades
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37352587481495) Tempo aproximado para leitura: **01:00 min**  
  
**Dúvida**  
Como realizar a implantação e quais as funcionalidades da rotina FINA716 (Aplicações e Empréstimos)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - a partir da release 12.1.2210  
  
**Solução**

As rotinas de **Aplicações** e **Empréstimos** foram revitalizadas com o objetivo de proporcionar uma melhor usabilidade e experiência ao usuário. A nova interface foi desenvolvida em **Angular**, utilizando componentes da biblioteca **PO-UI**.

Para o correto funcionamento da rotina **FINA716**, é obrigatório que o ambiente esteja na **release 12.1.2210 ou superior**, além de possuir a **Porta Multiprotocolo** devidamente configurada.

Caso alguma dessas condições não seja atendida, a rotina pode não funcionar conforme o esperado.

#### **Configuração da Porta Multiprotocolo (Appserver.ini)**

Para habilitar o uso de rotinas em PO-UI, realize os ajustes abaixo no arquivo de configuração do servidor:

1. Na seção **[GENERAL]**, inclua a chave App\_Environment com o nome do ambiente   
   (Ex: App\_Environment =P12\_PRODUCAO);
2. Na seção **[DRIVERS]**, habilite a chave MultiProtocolPort=1;
3. Por padrão, a conexão SSL é ativa. Para desabilitá-la, utilize a chave MultiProtocolPortSecure=0.

---

### **Funcionalidades da Rotina FINA716**

* [**Aplicações (Disponível a partir da release 12.1.2510)**](Aplica%C3%A7%C3%B5es%20-%20FINA716%20-%20Release%2012.1.2510%20e%20superiores)**:** Permite o controle de aplicações financeiras, possibilitando a inclusão, alteração e o resgate diretamente pelo ERP.
* [**Empréstimos (Disponível a partir da release 12.1.2510)**](https://tdn.totvs.com/pages/releaseview.action?pageId=684987254)**:** Gestão de contratos de empréstimos, permitindo o controle de inclusão, alteração e pagamentos das parcelas.
* [**Apropriação**](https://tdn.totvs.com/pages/releaseview.action?pageId=684987454)**:**

  + **Via Menu:** Realiza a contabilização dos ganhos (rendimentos) ou juros a pagar (empréstimos).
  + **Apropriação de IR (Come-cotas):** Acessada via aplicação específica para apropriar o IR com base no rendimento ou realizar o processo de come-cotas.
* [**Cadastro de Templates:**](https://tdn.totvs.com/display/public/PROT/Cadastro+de+templates+-+FINA716) Permite flexibilizar os cálculos de juros e taxas (como o CDI). O usuário pode configurar fórmulas personalizadas ou utilizar os modelos padrão do sistema.

**How To | Aplicações e Empréstimos**

   
**Webinar TOTVS | FINA716 Aplicação Empréstimo**  
<https://www.youtube.com/watch?v=CD9zIz2hHmw>
