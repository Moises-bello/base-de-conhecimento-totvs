---
article_id: 360021514771
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 0caaa6310b03b6ae116324420da419d9b72133f4d1f35d609ddcf710d428de31
fetched_at: '2026-06-28T22:42:27.924179+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Como habilitar a transferência de pendências
  na rotina de Usuários
type: support-article
updated_at: '2026-04-15T13:12:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021514771-Manufatura-Linha-Protheus-SIGAQNC-Como-habilitar-a-transfer%C3%AAncia-de-pend%C3%AAncias-na-rotina-de-Usu%C3%A1rios
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39763857651735)** Tempo aproximado para leitura: **00:00:30 min**  
  
**Dúvida**  
Como habilitar a transferência de pendências na rotina **QNCA070 - Usuários**?    
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Solução**  
Para que a opção **Transferir** seja apresentada na rotina **QNCA070** em **Outras Ações**, é necessário configurar os parâmetros abaixo:  
- **MV\_QNCTFUN** **- Define se deverá aparecer a opção de transferência no cadastro de usuários** como **S**;  
- **MV\_QNCNTRF - Define o nível do acesso do usuário que poderá transferir lançamentos de fichas de não conformidades e planos de ação.** Preencher com um valor de **0 a 9**.  
  
**Observação**  
O **nível** informado no parâmetro **MV\_QNCNTRF** é configurado no **SIGACFG - Configurador** em **Usuário > Senhas > Usuários**, dentro do cadastro de usuário. Na aba **Parametrização**, verifique qual o conteúdo do campo **Nível global de campos (leitura)**.   
Se, por exemplo, o usuário em questão estiver com conteúdo igual à 5, o conteúdo do parâmetro **MV\_QNCNTRF** deverá ser **menor ou igual** ao nível de usuário no **Configurador**.
