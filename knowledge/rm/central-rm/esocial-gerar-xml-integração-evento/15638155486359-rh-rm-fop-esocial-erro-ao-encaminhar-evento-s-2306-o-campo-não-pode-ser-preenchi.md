---
article_id: 15638155486359
category: eSocial - Gerar XML/ Integração Evento
content_hash: 7fb503d029b85760c7d838aebf9ac3d6ee9db3aca54f72af7bfc4d1bec709b0d
fetched_at: '2026-06-28T22:47:12.183418+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao encaminhar evento S-2306: O campo não pode
  ser preenchido: Natureza da atividade'
type: support-article
updated_at: '2026-06-15T13:09:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15638155486359-RH-RM-FOP-eSocial-Erro-ao-encaminhar-evento-S-2306-O-campo-n%C3%A3o-pode-ser-preenchido-Natureza-da-atividade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15638134871703) Tempo aproximado para leitura: **00:02:30 min**  
  
**Ocorrência**  
Ao tentar integrar o evento S-2306 ocorre o **Erro código 2: O campo não pode ser preenchido: Natureza da atividade. Localização: /eSocial/evtTSVAltContr/infoTSVAlteracao/natAtividade.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
O erro ocorre ao encaminhar o S-2306 no qual o autônomo possuí uma categoria eSocial onde a Natureza da Atividade (Trabalho Urbano ou Trabalho Rural) não deve ser informada no eSocial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15637592299159)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o portal do Governo e identifique qual é o código da categoria que consta cadastrada para o autônomo;  
2. Identifique no RM o autônomo com erro, acesse o cadastro do mesmo e vá na aba **Registro** e confira se o código da categoria eSocial consta condizente com o do governo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15637916174359)

2.1. Caso não esteja condizente com o portal do governo, será necessário realizar a adequação;  
2.2. Caso esteja condizente, verifique em **Anexo - Históricos - Histórico da Categoria eSocial** se consta algum outro histórico de categoria cadastrado incorretamente, se sim, será necessário excluir o histórico incorreto;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15638006665751)

3. Gere novamente o XML e identifique se a tag natAtividade não foi gerada e integre com o governo.

**Saiba mais**  
Para mais informações, acesse:

* [Histórico da Categoria eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=517137481#1-2)
