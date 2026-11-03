---
article_id: 20757877386647
category: eSocial - Tabelas/Não Periódicos
content_hash: 1e38d7078a03caaa6a378ff54691fd6a0d4902276e312fe4f45562d4c57e4977
fetched_at: '2026-06-28T22:47:10.446397+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro no envio do S-2200 ou S-2206: Grupo #39;Informacoes
  relacionadas ao aprendiz#39; deve ser preenchido'
type: support-article
updated_at: '2024-01-22T11:23:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20757877386647-RH-RM-FOP-eSocial-Erro-no-envio-do-S-2200-ou-S-2206-Grupo-39-Informacoes-relacionadas-ao-aprendiz-39-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20757877358103) Tempo aproximado para leitura: 00:02:00 min  
  
**Ocorrência**  
Ao envio o XML do S-2200 ou S-2206, ocorre o erro: **Grupo #39;Informacoes relacionadas ao aprendiz#39; deve ser preenchido. Verifique as condições de preenchimento no leiaute.** **Localização: /eSocial/evtAdmissao/vinculo/infoRegimeTrab/infoCeletista**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20757877366295)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir dos patches 12.1.2302.235, 12.1.2306.182, 12.1.2310.116 e superiores  
  
**Causa**  
Esse incidente geralmente ocorre quando está sendo enviado a admissão ou alteração contratual de um funcionário estagiário no leiaute S-1.2 e o grupo **aprend**, que é obrigatório nesse caso, não foi informado.  
  
**Solução**  
Para solucionar o incidente, é necessário preencher os dados do aprendiz, presentes na aba **Dados do Aprendiz**, dentro da área **Registro** do cadastro do funcionário. A aba **Dados do Aprendiz** será habilitada sempre que for informada a categoria eSocial **103**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20757877370135)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20757867986839)

No documento abaixo você poderá verificar todo o **processo de admissão de aprendiz**, bem como as **orientações** sobre **cada um dos campos** da tela acima:

* [Contratação de Aprendiz - Leiaute S-1.2](https://tdn.totvs.com/pages/releaseview.action?pageId=795092070)

**Importante**  
O envio do Leiaute **S-1.2** é **obrigatório** a partir de 22/01/2024.

É possível realizar a alteração de vários registros ao mesmo tempo através do menu **Administração de Pessoal | Alterações Cadastrais | Alteração Campos do Cadastro**. Basta selecionar as opções desejadas e informar uma fórmula para alteração global.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20757867987607)

**Saiba mais**  
Para mais informações, acesse:

* [Alterações para atender ao Leiaute S-1.2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18576806660119)
* [RH Informa](https://informa.totvs.com/rh/)
