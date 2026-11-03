---
content_hash: c9bf4984a323db519d5b3b736630c29e6b5701c737c9e3bdf738390a55972e9b
fetched_at: '2026-06-29T00:08:08.413814+00:00'
page_id: '238033257'
product: rm
source: tdn-rm
title: ER_PCREQ-10086_Melhorias_Mashup
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10086_Melhorias_Mashup
version: 115
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Framework | **Módulo** | Mashups |
| **Segmento Executor** |  | | |
| **Projeto1** | FRW\_002 | **IRM1** | PCREQ-10030 |
| **Requisito1** | PCREQ-10086 | **Subtarefa1** | PDR\_FRW\_FRW002-223 |
| **Chamado2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

 *Indentificar todos os Mashups que atualmente não estão funcionando e implementar as melhorias necessárias no Engine de Mashups para permitir estas correções.*

### Definição da Regra de Negócio

Após análise foram identificados problemas nos seguintes Mashups:

* Correios - Pesquisa CEP do Endereço
* Correios - Tarifas do Sedex
* Sintegra
  + Acre
  + Amapá
  + Distrito Federal
  + Espírito Santo
  + Goiás
  + Maranhão
  + Mato Grosso
  + Mato Grosso do Sul
  + Piauí
  + Rio de Janeiro
  + Rio Grande do Sul
  + Rondônia
  + Roraima
  + Santa Catarina
  + Tocantins

### Conclusão

Serão criadas melhorias no engine de Mashup para permitir a utilização do controle WebBrowser em alternativa ao uso do HttpWebRequest pois o mesmo é capaz de executar o código Javascript das páginas que contem mecanismos de captcha baseados em requisições Ajax como o Recaptcha.

Será criada uma nova atividade chamada MashupWebBrowser que faz a requisição e retorna dados dos elementos da página para os resultados do Mashup.

Será implementada a propriedade UseWebBrowser na atividade de requisição para permitir o uso deste mecanismo em conjunto com a atividade Parser.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
