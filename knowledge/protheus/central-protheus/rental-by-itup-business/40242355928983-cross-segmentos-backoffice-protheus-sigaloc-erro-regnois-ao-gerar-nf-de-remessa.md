---
article_id: 40242355928983
category: Rental by ItUp Business
content_hash: eea02845b7b973c93faa3c27e8c234e0a2cecb4ff4c23ecc5d9aed5d2df812d5
fetched_at: '2026-06-28T22:36:20.626733+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Erro REGNOIS ao gerar NF
  de remessa
type: support-article
updated_at: '2026-05-05T17:19:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40242355928983-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Erro-REGNOIS-ao-gerar-NF-de-remessa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40242379393303) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Ao tentar gerar uma Nota Fiscal de remessa por meio da rotina **LOCA001**, o sistema apresenta o erro "AJUDA: **REGNOIS** - Não existe registro relacionado a chave informada no alias **SED**, ordenação 1", apontando para um conteúdo inválido no campo Natureza (**C5\_NATUREZ**) da tabela **SC5**.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões]  
  
**Solução**  
O erro ocorre porque o sistema tenta gravar uma natureza financeira que não está cadastrada ou é considerada inválida na tabela de Naturezas (**SED**). No processo do módulo Gestão de Locação (**SIGALOC**), a natureza preenchida neste cenário tem origem na configuração do parâmetro **MV\_LOCX066**. Para correção, é necessário ajustar o parâmetro e informar uma natureza válida e ativa no ambiente.  
  
**Passos:**

1. Acesse o módulo Configurador (**SIGACFG**).
2. Siga pelo menu **Ambiente** > **Cadastros** > **Parâmetros**.
3. Pesquise pelo parâmetro **MV\_LOCX066**.
4. Edite o parâmetro e preencha o seu conteúdo com o código de uma natureza financeira válida existente em seu sistema (tabela **SED**).
5. Salve a alteração.
6. Acesse novamente a rotina **LOCA001** e repita o processo de geração da NF de remessa.

**Saiba Mais:** [***Configurações - Locação - P12***](https://tdn.totvs.com/pages/releaseview.action?pageId=592557488)
