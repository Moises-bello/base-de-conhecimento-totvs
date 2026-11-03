---
article_id: 35678783969303
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 6edc653fc9179ed237cab4fa37bb85788b4b0b3a708d67925dc9bf05d824d0c3
fetched_at: '2026-06-28T22:40:32.509244+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA960 - Opção de Verificação
  de saldo gera o help Internal Server Erro.
type: support-article
updated_at: '2025-12-17T23:01:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35678783969303-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA960-Op%C3%A7%C3%A3o-de-Verifica%C3%A7%C3%A3o-de-saldo-gera-o-help-Internal-Server-Erro
---

**Dúvida**  
Opção de Verificação de saldo gera o help Internal Server Erro.  
  
Ambiente  
Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade Gerencial - a partir da versão 12.1.2410

**Ocorrência apresentada: Help Internal Server Erro**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35678783936279)

**Solução:**

Este help ocorre devido a desatualização da procedure 29 na configuração, que pode estar com Status: "**Desatualizado ou Incompatível**"

**Para correção deve:**

**Acessar o Configurador (SIGACFG) -**> base de dados -> Stored Procedure:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35678783937303)

Ao ser aberta a tela do gerenciador de procedure, selecione a empresa que esta utilizando no campo superior esquerdo, e verifique o Status da procedure:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35678783937943)

Caso esteja como **desatualizada ou incompatível**, deve realizar a atualização conforme abaixo:  
  
  
**1°** Aplique o pacote de atualização dos fontes, que acionam a procedure:

[Pacotes de Atualização - Contabilidade Gerencial - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)

**2°** Após aplicação do pacote realizar o processo de Atualização do procedure:

Na tela de procedure:

1° Marque grupo de empresa utilizado;

2° Marque a procedure que será atualizada;

3° Selecione a caixinha com a Seta Verde;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35678783938583)

Ao finalizar a atualização será apresentada tela que a procedure foi instalada com Sucesso:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35678783939351)

E o Status será apresentado como atualizado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35678816259991)

**3°** Após atualização da procedure valide novamente o uso da rotina.

**Saiba mais:**

[Stored Procedures - Novo gerenciador de pacotes - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes)

#### [Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA960 - Fechamento Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34334419010839-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA960-Fechamento-Cont%C3%A1bil)
