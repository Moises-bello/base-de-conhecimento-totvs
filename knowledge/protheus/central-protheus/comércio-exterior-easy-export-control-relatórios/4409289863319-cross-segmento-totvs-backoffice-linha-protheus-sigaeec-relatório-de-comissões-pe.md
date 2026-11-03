---
article_id: 4409289863319
category: Comércio Exterior - Easy Export Control - Relatórios
content_hash: 31b5d8f2aea464ea677cb4da2d312308e44824edd7f06d26afe4250a39e12e1b
fetched_at: '2026-06-28T22:36:59.898697+00:00'
product: protheus
section_id: 1500001538161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Relatório de Comissões
  Pendentes
type: support-article
updated_at: '2021-09-23T14:57:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409289863319-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Relat%C3%B3rio-de-Comiss%C3%B5es-Pendentes
---

**Dúvida**Há algum relatório dentro no SIGAEEC que exiba as comissões lançadas por processo, e seus agentes?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**No menu Relatórios em português do módulo de exportação, temos a opção **Comissão Pendentes** onde será gerado as comissões pendentes.

O relatório pode ser filtrado por data inicial até a data final, Representante, Exportador, Fabricante e o tipo de comissão (0-Todos, 1- Remeter ,2- Conta Gráfica, 3 - Deduzir Fatura).  
![comiss_o_pendente_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409288966295/comiss_o_pendente_1.png)

Uma vez preenchido as informações, será gerado um relatório no formato paisagem onde são levadas as informações do processo incluindo o agente, a comissão e o processo​.

![comiss_o_pendente_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409281313687/comiss_o_pendente_2.png)

Para que este relatório seja gerado é necessário compilar o rdmake **EECPRL07\_RDM**  em seu ambiente assim como ter o arquivo **REL07.RPT** dentro da pasta Crystal, no servidor (diretório raiz do protheus\_data).  Estes arquivos estão disponíveis no pacote da expedição continua do comércio exterior  
  
**Saiba mais**  
[Pacote de atualizações de comércio exterior](https://tdn.totvs.com/pages/releaseview.action?pageId=526987588)
