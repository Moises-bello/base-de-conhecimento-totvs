---
article_id: 20821830336023
category: eSocial - Gerar XML/ Integração Evento
content_hash: 0c747ba1862def464d2162a63872850e165959d4eed19fcf77f71a4d2a92e806
fetched_at: '2026-06-28T22:47:11.940466+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao gerar o XML S-2200 ou S-2206 ocorre o erro: O
  campo ''indAprend'' do registro ''aprend'' é obrigatório e não está preenchido.'
type: support-article
updated_at: '2025-12-29T14:20:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20821830336023-RH-RM-FOP-eSocial-Ao-gerar-o-XML-S-2200-ou-S-2206-ocorre-o-erro-O-campo-indAprend-do-registro-aprend-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20821830293399) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao gerar o XML S-2200 ou S-2206 ocorre o erro: O campo 'indAprend' do registro 'aprend' é obrigatório e não está preenchido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20821798550551)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Esse incidente geralmente ocorre quando está sendo gerado a admissão ou alteração contratual de um funcionário estagiário no leiaute S-1.2 e o grupo **aprend**, que é obrigatório nesse caso, não foi informado.  
  
**Solução**  
Para solucionar o incidente, é necessário preencher os dados do aprendiz, presentes na aba **Dados do Aprendiz**, dentro da área **Registro** do cadastro do funcionário. A aba **Dados do Aprendiz** será habilitada sempre que for informada a categoria eSocial **103**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20821798560791)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20821798567063)

No documento abaixo você poderá verificar todo o **processo de admissão de aprendiz**, bem como as **orientações** sobre **cada um dos campos** da tela acima:

* [Contratação de Aprendiz - Leiaute S-1.2](https://tdn.totvs.com/pages/releaseview.action?pageId=795092070)

**Importante**  
O envio do Leiaute **S-1.2** é **obrigatório** a partir de 22/01/2024.

É possível realizar a alteração de vários registros ao mesmo tempo através do menu **Administração de Pessoal | Alterações Cadastrais | Alteração Campos do Cadastro**. Basta selecionar as opções desejadas e informar uma fórmula para alteração global.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20821830314391)

**Saiba mais**  
Para mais informações, acesse:

* [Alterações para atender ao Leiaute S-1.2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18576806660119)
* [RH Informa](https://informa.totvs.com/rh/)
