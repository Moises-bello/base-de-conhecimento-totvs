---
article_id: 39136394719895
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 2c2459ada9340b68595fcf4b68d21336d1888cd635100b304ad86af932182f2d
fetched_at: '2026-06-28T22:39:08.065114+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - cannot find function
  INCCPY in AppMap
type: support-article
updated_at: '2026-03-18T19:27:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39136394719895-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-cannot-find-function-INCCPY-in-AppMap
---

O erro "InterFunctionCall: cannot find function INCCPY in AppMap" ocorre na rotina MATA010 do TOTVS Backoffice (Linha Protheus) a partir da versão 12.1.2410, indicando que a função não está compilada no repositório. A solução é atualizar a rotina MATA010 para a versão mais recente via SHIFT+F6 no ambiente ou baixar os fontes gerais, e validar a função no inspetor de funções.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39136394706711) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**  
Ao utilizar processos que envolvem uso da rotina MATA010, ocorre o erro: InterFunctionCall: cannot find function INCCPY in AppMap  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.2410  
  
**Causa**   
O erro significa que a função não esta compilada no repositorio.  
  
**Solução**  
Atualize a rotina MATA010 com a versão mais recente disponivel, que pode ser obtida acessando a rotina, e então atraves do SHIFT+F6 do ambiente, no menu de atualizações validar o pacote pontual da rotina.  
Ou efetuar o download geral dos fontes.  
[- Acumulado BackOffice conforme sua versão](https://tdn.totvs.com/x/2hgdHw)

Após isso valide, se a função esta disponivel no inspetor de funções.

**Saiba mais:**  
[*Clique aqui para mais informações sobre a MATA010*](https://tdn.totvs.com/display/public/PROT/Produtos+-+MATA010#ProdutosMATA010-PastaCadastrais)  
[*Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)  
[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de envio Messenger para ID de eventos do Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003963562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-envio-Messenger-para-ID-de-eventos-do-Estoque)
