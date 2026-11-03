---
article_id: 10287789597463
category: SIGAEST - CUSTOS
content_hash: 5576c94eb8455053abe7937e9cb7817d443752f96dbe8baaf0500db44127fc04
fetched_at: '2026-06-28T22:39:02.151898+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Erro ao
  processar custo médio - A rotina MATA330 está desatualizada
type: support-article
updated_at: '2025-03-12T12:25:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10287789597463-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Erro-ao-processar-custo-m%C3%A9dio-A-rotina-MATA330-est%C3%A1-desatualizada
---

**Dúvida**Ao processar o custo médio, é informado que "A rotina MATA330 está desatualizada", e logo acima informa uma procedure contábil, como corrigir?

"*Incompatibilidade*

*Controle 011 ref. rotina MATA330*

*Controle 013 ref. procedure CTB20\_01\_01*

*A rotina MATA330 está desatualizada*"  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Provavelmente o HELP de seu ambiente, pode não estar com as ultimas atualizações necessárias, pois o mesmo pode ser genérico, a mensagem informar que a rotina MATA330 está desatualizada, se já validou se a sua rotina MATA330 esta com a ultima atualização, a sugestão é que valide se a rotina do "Contábil" e procedure "CTB020\_01\_01" informadas no HELP, estão atualizada?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10287612433559)

Por exemplo, se sua rotina MATA330 esta atualizada, caso seus HELPs estejam atualizados, a informação seria diretamente para com o erro em questão:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10287658098327)

**Então oque fazer quando se é apresentado o primeiro HELP?**

- Validar se a rotina MATA330 esta atualizada, se sim, verifique então sua procedure e rotinas contábeis, e atualize seus HELPs.

**O que fazer quando se é apresentado o segundo HELP?**

- O Help ja informa oque deve ser realizado, apontando diretamente o problema na desatualização da procedure, basta atualiza-la.

**Mas como eu atualizo os HELPS do ambiente?**

- Basta seguir o procedimento do boletim:

[Framework - Linha Protheus - FRAME - Atualização de Help](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028969891-Framework-Linha-Protheus-FRAME-Atualiza%C3%A7%C3%A3o-de-Help)

**Mas como eu atualizo as procedures do ambiente?**

- Basta seguir o procedimento do boletim:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como instalar as Stored Procedures?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009382821-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-instalar-as-Stored-Procedures-)

**E se o problema for na desatualização da rotina MATA330? como eu atualizo a rotina?**

- Primeiro você precisa baixar o pacote de atualização, abaixo contém um link, com a atualização de todos os módulos do Protheus, acesse-o e depois selecione o modulo desejado, e baixe o pacote para atualização.

[Atualizações Protheus Módulos](https://tdn.totvs.com/pages/releaseview.action?pageId=550332596#OINF0011.2-Atualiza%C3%A7%C3%B5esProtheus-Modulos)

**Depois que baixei o pacote para atualização, como eu atualizo esse pacote no ambiente?**

-Basta seguir o exemplo, conforme boletim link abaixo:

[Como aplicar pacote via VSCODE no ambiente?](https://github.com/totvs/tds-vscode/blob/HEAD/docs/apply-patch.md)

Todo e qualquer tipo de atualização, sempre se deve realizar backup e feito primeiramente em base teste, essa é uma premissa de boas praticas.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
