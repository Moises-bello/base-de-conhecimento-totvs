---
article_id: 39322881181335
category: PCO - Cadastros
content_hash: fc36ca931f6c26fd66673297794cae10be85698a65eed5b73acaf43f1b13decd
fetched_at: '2026-06-28T22:37:12.926652+00:00'
product: protheus
section_id: 1500001550802
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPCO - Como desabilitar
  o ponto de lançamento para não integrar com PCO
type: support-article
updated_at: '2026-03-30T13:08:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39322881181335-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAPCO-Como-desabilitar-o-ponto-de-lan%C3%A7amento-para-n%C3%A3o-integrar-com-PCO
---

Para desabilitar o ponto de lançamento e impedir a integração com o PCO no TOTVS Protheus, deve-se acessar a rotina de Cadastro de Processos (PCOA030) ou Bloqueio por processo (PCOA035), alterar o ponto de lançamento, remover a flag de uso e salvar a alteração dentro da tela interna do ponto de lançamento. Salvar na tela externa grava apenas dados do cadastro principal.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39322897501463) Tempo aproximado para leitura: 00:05 min  
  
**Dúvida**  
Como desabilitar o ponto de lançamento para que não ocorra a integração com o PCO (Planejamento e Controle Orçamentário)?  
  
**Ambiente**

**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPCO - A paritr da Versão 12**  
  
**Solução**  
Para desabilitar o ponto de lançamento e impedir a integração com o PCO, deve-se remover a flag de uso diretamente na opção de alteração do ponto de lançamento.

É importante destacar a regra de gravação desta rotina: ao desmarcar a flag, a alteração deve ser confirmada e salva dentro da própria tela interna do ponto de lançamento. A opção de salvar disponível na tela anterior (externa) tem a finalidade exclusiva de gravar as informações do cadastro principal, e não as configurações específicas do ponto de lançamento.

1. Acesse a rotina de Lançamento por Processos (PCOA030) ou Bloqueio por processo (PCOA035)
2. Posicione no processo de sistema desejado e clique na opção para **Alterar**.
3. Acesse a tela de alteração do ponto de lançamento.
4. Localize e remova a marcação da flag de uso do respectivo ponto de lançamento.
5. Confirme e salve a alteração **dentro desta mesma tela interna**.
6. Retorne à tela externa. Caso tenha modificado algum dado do cadastro do processo, utilize o botão de salvar externo apenas para estas informações da tela principal.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39322897504279)

   **Saiba Mais**  
   [Configuração de Lançamentos por Processo (PCOA030)](https://tdn.totvs.com/pages/releaseview.action?pageId=691437643)  
   [Bloqueios por processos (PCOA035 - SIGAPCO)](https://tdn.totvs.com/pages/releaseview.action?pageId=312175424)
