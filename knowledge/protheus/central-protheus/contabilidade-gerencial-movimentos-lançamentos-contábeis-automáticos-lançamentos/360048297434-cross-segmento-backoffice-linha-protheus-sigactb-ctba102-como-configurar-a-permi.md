---
article_id: 360048297434
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 230d436451d5bfe7ae9fe29cedd8fc469ed71c6b1654c7f3eb1b026975ed330e
fetched_at: '2026-06-28T22:40:32.431126+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102  Como  Configurar
  a Permissão para Exportação de Lançamento Contábil em Planilha Excel '
type: support-article
updated_at: '2022-03-10T11:40:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048297434-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Como-Configurar-a-Permiss%C3%A3o-para-Exporta%C3%A7%C3%A3o-de-Lan%C3%A7amento-Cont%C3%A1bil-em-Planilha-Excel
---

**Dúvida**

 Como configurar a permissão para Exportação de lançamento contábil em Planilha excel?

Após  localizar um lançamento , realizar alteração e  seleciona o botão  outras ações.

![cid:image008.png@01D63019.065A5FB0](https://atendimento.totvs.com/attachments/token/lWF13NaskpFn9SZvXFW4642NN/?name=image002.png)

Ao clicar  em exportar ao Excel.

![cid:image009.png@01D63019.065A5FB0](https://atendimento.totvs.com/attachments/token/dRW48LIlb9F9zE80tjtwrI9rG/?name=image003.png)

 Sistema apresenta a mensagem

Help :SEMPERM

Problema :Usuário sem permissão para Utilizar esta rotina

![cid:image007.png@01D63019.065A5FB0](https://atendimento.totvs.com/attachments/token/uxI31TDrq4H6nVBPKikOYqdFj/?name=image001.png)

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**

Primeiramente verificar o**Cadastro de Usuários (CFGA510)**

**1.** Acesse o **Configurador (SIGACFG);**  
**2.** Usuário > Senhas > **Usuários;**  
**3.** Selecione o Usuário > **Alterar;**  
**4.** Aba **Restrições de acesso** > **Acessos;**  
**5.** Verifique se os Acessos '**170 - Exportar telas para Excel (Mod1 e 3)** está Marcado**;![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072478233/mceclip3.png)**

Caso no cadastro de usuário esteja correto, verifique no **Cadastro de Grupos (CFGA520)**

**1.**Acesse o**Configurador (SIGACFG);  
2.**Usuário > Senhas >**Grupos;  
3.**Selecione o Grupo >**Alterar;  
4.**Aba**Restrições de acesso**>**Acessos;****5.** Verifique se os Acessos '**170 - Exportar telas para Excel (Mod1 e 3)** está Habilitado**;![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072478233/mceclip3.png)**
