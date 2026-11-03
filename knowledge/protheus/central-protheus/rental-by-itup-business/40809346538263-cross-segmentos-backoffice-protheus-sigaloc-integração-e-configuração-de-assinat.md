---
article_id: 40809346538263
category: Rental by ItUp Business
content_hash: 3d0db891aa1e704336d50fd21a1c750616a9c060aad4df81e749584b2d67d6a3
fetched_at: '2026-06-28T22:36:20.653108+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Integração e configuração
  de assinatura digital SIGALOC x TAE
type: support-article
updated_at: '2026-05-28T20:59:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40809346538263-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Integra%C3%A7%C3%A3o-e-configura%C3%A7%C3%A3o-de-assinatura-digital-SIGALOC-x-TAE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40809329866775) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como realizar a integração e configurar o processo de envio de documentos para assinatura digital (TOTVS Assinatura Eletrônica - TAE) a partir do módulo Locação de Equipamentos (SIGALOC)?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões  
  
**Solução**  
A funcionalidade permite o envio direto de documentos (como propostas, contratos e termos de serviço) associados a um orçamento no **TOTVS RENTAL** (**SIGALOC**) para a plataforma **TOTVS** Assinatura Eletrônica (**TAE**). Para garantir a rastreabilidade e a validade jurídica, é obrigatório configurar previamente os parâmetros de integração e o agendamento (Schedule) para o retorno automático do status das assinaturas.

Passos

1. Acesse o módulo **Configurador** (**SIGACFG**) e verifique a existência e o preenchimento dos seguintes parâmetros (crie-os, caso não existam):

* **MV\_LOCX313**: Local dos arquivos no banco de conhecimento Rental.
* **MV\_USRTAE**: Usuário do TOTVS Assinatura Eletrônica.
* **MV\_PWTAE**: Senha do usuário do **TAE**.
* **MV\_TAEBASE**: Ambiente do **TAE**.
* **MV\_MULTDIR**: Ativa a gravação em subpastas na rotina do Banco de Conhecimento (**.T.** ou **.F.**).

2. Configure o Schedule no sistema para a função **LOCA001D8**(). Este agendamento é o responsável por garantir a atualização correta dos status de retorno dos documentos (Enviado, Pendente, Assinado, Rejeitado, Finalizado).
3. Caso necessário, acesse o cadastro de Tipo de Documento (**tabela FPC**) e configure se o envio do documento ao **TAE** deverá bloquear a geração do contrato ou da nota de remessa.
4. No módulo **SIGALOC**, acesse a rotina de orçamento e direcione-se à aba "Documentos".
5. Clique em "**Outras Ações**" > "**Banco de Conhecimento**" e realize a inclusão do arquivo que deverá ser assinado.
6. Ainda na aba "**Documentos**", insira o código do documento a ser enviado e preencha as informações obrigatórias dos contatos aprovadores, incluindo **e-mail**, **CPF**, **função** e **ação a ser realizada**.
7. Confirme a gravação do orçamento.
8. Na tela inicial de navegação dos orçamentos, posicione no registro recém-criado, clique em "**Outras Ações**" e selecione "**Ass. Digital**".
9. Efetue o login na interface do T**OTVS Assinatura Eletrônica**, selecione o respectivo documento e clique em "**Confirmar**".
10. O sistema enviará o documento à plataforma e os assinantes receberão um e-mail com as instruções de validação e aprovação. O status será atualizado automaticamente na linha do documento vinculado ao orçamento conforme o avanço das assinaturas.

Saiba mais: [***Integração TAE Rental***](https://tdn.totvs.com/pages/viewpage.action?pageId=899193937)
