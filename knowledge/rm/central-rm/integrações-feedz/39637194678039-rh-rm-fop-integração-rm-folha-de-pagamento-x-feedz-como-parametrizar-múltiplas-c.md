---
article_id: 39637194678039
category: Integrações - Feedz
content_hash: 62321b5b52f7e0edf8426628cfb9910733e3b1d10937ee77d1ccfdd4751d2b36
fetched_at: '2026-06-28T22:46:41.399061+00:00'
product: rm
section_id: 28212337440791
source: central-rm
title: RH - RM - FOP - Integração RM Folha de Pagamento x Feedz - Como parametrizar
  múltiplas coligadas para uma única base Feedz
type: support-article
updated_at: '2026-04-10T14:26:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39637194678039-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Como-parametrizar-m%C3%BAltiplas-coligadas-para-uma-%C3%BAnica-base-Feedz
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39637187406615) Tempo aproximado para leitura: **00:02:00min**  
  
**Dúvida**  
Como realizar a parametrização da integração entre TOTVS RM Folha de pagamento e Feedz para múltiplas coligadas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2310  
  
**Solução**  
Para que a integração funcione corretamente com múltiplas coligadas utilizando um único token/base da feedz, é obrigatório que os parâmetros de concatenação estejam ativos no RM. No módulo**Folha de pagamento** acesse **Configurações** **|** **Parametrizador | Integrações** | **TOTVS RH Performance e Metas / Feedz**. Na tela de parametrização da **Feedz**, marque os seguintes parâmetros:

* **Concatenar Descrição do Cargo (Descrição + Código);**
* **Concatenar Descrição do Departamento (Descrição + Código);**
* **Concatenar Descrição da Unidade (Descrição + Código);**
* **Concatenar o Código da Coligada no Cargo / Departamento / Unidade / Matrícula;**

Para informações detalhadas sobre estes parâmetros, consulte nossa documentação: [Integração RM X Feedz](https://tdn.totvs.com.br/pages/releaseview.action?pageId=785614408#1-1)

Caso estes parâmetros não estejam marcados em um cenário de múltiplas coligadas impede que o sistema diferencie as origens dos dados (coligadas e filiais), resultando nos seguintes problemas:

* **Sobrescrita de dados:** O envio de informações de uma coligada apagará os dados enviados anteriormente por outra coligada.
* **Erros de duplicidade:** Ocorrem conflitos no processamento devido a registros (como chapas, cargos e departamentos) que possuem o mesmo código ou descrição em coligadas distintas.

**Observação:** Caso a empresa opte por não utilizar a concatenação para preservar a visualização visual dos dados na plataforma, a alternativa recomendada é a utilização de bases segregadas, o que requer um token de integração exclusivo para cada coligada.

**Saiba mais:**  
[**RH - RM - FOP - Integração RM Folha de Pagamento x Feedz - Como parametrizar a integração do RM com a FEEDZ**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29912740330391-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Como-parametrizar-a-integra%C3%A7%C3%A3o-do-RM-com-a-FEEDZ)
