---
article_id: 4411512345111
category: Inspeção de Entradas (SIGAQIE)
content_hash: 01f84c1abc59a60eff3c010b5bf943424ce76b143f840b9ff51f9b12ecf8bfbb
fetched_at: '2026-06-28T22:42:27.089114+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Não gerou inspeção na tabela QEK
type: support-article
updated_at: '2023-10-02T14:26:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411512345111-Manufatura-Linha-Protheus-SIGAQIE-N%C3%A3o-gerou-inspe%C3%A7%C3%A3o-na-tabela-QEK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17963892277783) Tempo aproximado para leitura: **00:01:45 min** **Dúvida**O documento de entrada foi incluído, mas não gerou a inspeção na tabela **QEK - Resultado a Inspecionar**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**Esta situação ocorre quando o produto informado no documento de entrada não possui os cadastros necessários para realizar a integração com o módulo **SIGAQIE - Inspeção de Entradas** ou quando o campo **Tipo CQ** da aba **CQ** da rotina **MATA010 - Produtos** está com o conteúdo igual à **M - Materiais**.  
Para solucionar esta situação, verifique qual é o conteúdo do campo **Tipo CQ**.  
Se o campo estiver como **M - Materiais**, indica que o produto não tem a parametrização básica para ser realizada a integração com o **SIGAQIE**.   
  
Porém, se o campo **Tipo CQ** estiver com o conteúdo igual à **Q - SigaQuality**, ao incluir o documento de entrada, serão verificados os cadastros citados no artigo abaixo, e caso o produto não tenha todos os cadastros, o documento de entrada será incluído e exibida uma mensagem em tela ao usuário, indicando qual é o motivo deste documento não ser integrado com o **SIGAQIE**.   
Além disso, esta mensagem será registrada também na rotina **QIEA183 - Importação** e tabela **QEP - Importação**, para ser possível ajustar o cadastro deste produto e após, realizar a importação deste registro por meio do **QIEA183** na opção **Importar**.   
Depois da importação realizada com sucesso, o registro a ser inspecionado estará disponível na rotina **QIEA215 - Resultado** e tabela **QEK**.  
  
**Saiba mais**  
No artigo [Manufatura - Linha Protheus - SIGAQIE - Cadastros necessários para integrar com o SIGAQIE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020570212-Manufatura-Linha-Protheus-SIGAQIE-Cadastros-necess%C3%A1rios-para-integrar-com-o-SIGAQIE) temos especificado quais são as parametrizações para que este produto seja integrado com o **SIGAQIE**.
