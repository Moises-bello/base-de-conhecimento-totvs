---
article_id: 20040374503319
category: 'Aplicativo MNTNG '
content_hash: 9f25a117f31473aa5733ac57b23f644e904fbbdb4b0f4046faf3e7f589734836
fetched_at: '2026-06-28T22:42:37.690484+00:00'
product: protheus
section_id: 360010992174
source: central-protheus
title: Manufatura - Linha Protheus - APP MNT - Erro 401 Parâmetro MV_NG1KEY
type: support-article
updated_at: '2024-01-03T16:59:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20040374503319-Manufatura-Linha-Protheus-APP-MNT-Erro-401-Par%C3%A2metro-MV-NG1KEY
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20040374454039) Tempo aproximado para leitura: **00:00:50 min****Ocorrência**No módulo aplicativo **MNT NG**, ao tentar realizar o *login* é apresentada a mensagem de erro: **O parâmetro MV\_NG1KEY - Define chaves utilizadas no aplicativo MNT NG não está preenchido corretamente.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20040374456471)**

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Aplicativo MNTNG - a partir da versão 12.1.2310  
  
**Causa**Para usuários que realizarem a migração de Portal releases **12.12310** ou superiores, o *Alias* **Mingle** deve ser informado no parâmetro **MV\_NG1KEY.**Para novos usuários que não realizaram a migração de ambiente, será necessário configurar o parâmetro **MV\_NG1KEY**, com o *Alias* do ambiente usado na aplicação **MNT NG**.  
**Solução**O parâmetro deve ser preenchido da seguinte forma: **ALIASMINGLE;CNPJ;NOME DA EMPRESA**     
Exemplo de preenchimento: **ALIAS TESTE;99987890091000;Empresa Teste**
