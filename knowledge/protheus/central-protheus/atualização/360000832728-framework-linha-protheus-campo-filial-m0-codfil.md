---
article_id: 360000832728
category: Atualização
content_hash: 8e24161d8b7e0bb830dfbb8cb8c9dbcaaa40097961e4f72eefbbbded1583d32d
fetched_at: '2026-06-28T22:42:21.199646+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus  - Campo Filial - M0_CODFIL
type: support-article
updated_at: '2024-03-26T13:19:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000832728-Framework-Linha-Protheus-Campo-Filial-M0-CODFIL
---

**Ocorrência**Customizações não retornam o tamanho do campo M0\_CODFIL corretamente  
  
**Ambiente**Protheus - Customização - Versão 12  
  
**Causa**Alteração de comportamento na estrutura do campo a partir da LIB de 16/03/2018  
  
**Solução**A partir da LIB de 16/03/2018, a estrutura do campo **Filial** (M0\_CODFIL) no arquivo sigamat.emp teve uma mudança de comportamento, já inicializando com **tamanho de 12 caracteres**.  
  
Para quem utiliza customização apontando diretamente o campo **M0\_CODFIL**, recomendamos que referencie a **função** que retorna o tamanho do campo (**FWSizeFilial**), ao invés de chamar o campo diretamente.
