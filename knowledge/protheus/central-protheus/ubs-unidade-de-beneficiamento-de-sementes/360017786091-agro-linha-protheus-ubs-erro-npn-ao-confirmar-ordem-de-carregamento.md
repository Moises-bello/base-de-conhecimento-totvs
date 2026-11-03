---
article_id: 360017786091
category: UBS - Unidade de Beneficiamento de Sementes
content_hash: 1036a3d2f92369f778e4bfea7379127145be47b1ace3f0d5e931aec83050e004
fetched_at: '2026-06-28T22:45:34.802508+00:00'
product: protheus
section_id: 360005696194
source: central-protheus
title: Agro - Linha Protheus - UBS - Erro NPN ao confirmar ordem de carregamento
type: support-article
updated_at: '2025-06-20T15:38:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017786091-Agro-Linha-Protheus-UBS-Erro-NPN-ao-confirmar-ordem-de-carregamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22238759861143)** Tempo aproximado para leitura:**00:01:00 min  
  
Ocorrência**Na rotina de **AGRA900 -****Ordem de Carregamento**, ao tentar confirmar o registro ocorre o incidente: **Cannot insert duplicate key row in object 'dbo.NPN010' with unique index 'NPN010\_UNQ'**.  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBS - Unidade de Beneficiamento de Sementes - Versão 12  
  
**Causa**Esse incidente ocorre porque o conteúdo da coluna **X2\_UNICO**, referente à tabela **NPN**, está inconsistente.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Acesse o **APSDU**, abra o arquivo **SX2** e filtre pela tabela **NPN**;

**2.** Altere o conteúdo existente na coluna **X2\_UNICO** para o conteúdo a seguir: **NPN\_FILIAL+NPN\_ORDEMC+NPN\_ITEM+NPN\_CODAC+NPN\_ITEMAC**;

**3.** Acesse a tabela **NPN**, **TopConnect**, faça uma cópia e depois efetue o *drop* da tabela;

**4.** Acesse o **SIGAMDI/ADV**, abra a rotina de **Ordem de Carregamento - AGRA900**, clique em **Incluir** e depois cancele a Inclusão (Esse processo é feito para que a tabela seja recriada);

**5.** Feche o **SIGAMDI/ADV**, acesse novamente o **APSDU** e efetue um *Append* dos dados que foram copiados.  
  
**Importante**  
É necessário acesso exclusivo ao sistema para efetuar esta alteração.
