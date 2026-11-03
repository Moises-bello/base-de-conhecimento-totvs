---
article_id: 360025041052
category: Originação de Grãos (OG)
content_hash: ac2cfea49b67e3228a324d93242130354391de55843f9365d51abf166fc4bdd4
fetched_at: '2026-06-28T22:45:37.380345+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: 'Agro - Linha Protheus - AGR - Aviso "Help: SERIE - Serie NF" no Romaneio com
  Pesagem OGA250'
type: support-article
updated_at: '2025-06-21T15:39:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025041052-Agro-Linha-Protheus-AGR-Aviso-Help-SERIE-Serie-NF-no-Romaneio-com-Pesagem-OGA250
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20654073875607)***Tempo aproximado para leitura: **00:00:55 min****Ocorrência**Ao tentar confirmar um romaneio, na rotina **OGA250 - Romaneio com Pesagem**, é apresentada a mensagem "Help: SERIE Problema: Favor preencher o campo "SerieNF" ou informar um conteúdo para a série no parâmetro MV\_OGASERE".

![Screenshot_1__1_.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023820052)

**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
 **Causa**Esse incidente ocorre porque para que o Romaneio seja confirmado corretamente é necessário que seja inserida a informação referente à **Série da Nota Fiscal**.  
  
 **Solução**Para que o romaneio seja confirmado corretamente sem que essa mensagem seja exibida é necessário que seja inserida a informação referente à **Série da Nota Fiscal**. Essa informação pode ser incluída de duas formas.

* A primeira forma para inserir essa informação é pelo campo **Série NF**, no registro do próprio romaneio que necessita ser confirmado.

![Screenshot_2__1_.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023821912)

* A outra maneira para inserir essa informação é por meio do parâmetro **MV\_OGASERE - Define a série padrão a ser utilizada na geração dos documentos de entrada**. Ao definir a informação da série pelo parâmetro, todas as Notas Fiscais geradas pela rotina de Romaneio assumirão a informação da série definida no parâmetro.

**Importante:**Esse procedimento é válido tanto para o controle de numeração de notas realizado pela tabela **SD9 - Controle de Numeração Doc**, quanto para o controle de numeração de notas realizado pela tabela **SX5 - Tabelas**.  
Esse procedimento é necessário para a geração de Notas Fiscais nas rotinas**OGA250** e **OGA251 - Romaneio sem Pesagem**.
