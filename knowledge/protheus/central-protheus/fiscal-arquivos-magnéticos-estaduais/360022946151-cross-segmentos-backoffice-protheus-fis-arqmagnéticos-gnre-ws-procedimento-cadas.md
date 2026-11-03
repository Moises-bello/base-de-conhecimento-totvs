---
article_id: 360022946151
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 09154655969bfa48d838680dd5cc989ae143ecf744a4db1e67d7e7bf207d612f
fetched_at: '2026-06-28T22:42:11.721370+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GNRE WS - PROCEDIMENTO
  CADASTRO DE INFORMAÇÕES EXTRAS.
type: support-article
updated_at: '2023-04-18T21:27:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022946151-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GNRE-WS-PROCEDIMENTO-CADASTRO-DE-INFORMA%C3%87%C3%95ES-EXTRAS
---

**Dúvida**COMO REALIZAR O CADASTRO DE INFORMAÇÕES EXTRAS.cadastrar O DE INFORMAÇÕES EXTRAS.

**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80

**Solução**

 Através da rotina **GNRE WS ( FISA095 )** acesse : Ações Relacionadas / Inf. Extras:

![GNRE_1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360020298191/GNRE_1.JPG)

Nesta rotina é possível realizar a importação do arquivo .csv que contém informações extras do ambiente de homologação, porém para obter o cadastro atualizado e de produção é necessário realizar a Sincronização através do TSS exemplificado nos próximos passos.

Importação tabela de Homologação – Clique em Ações Relacionadas / Importação.

**![GNRE_2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360020412992/GNRE_2.JPG)**

Informe o Caminho onde encontra-se o arquivo .csv:

**![GNRE_3.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360020413092/GNRE_3.JPG)**

Conclusão da importação da tabela.

![GNRE_4.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360020413172/GNRE_4.JPG)

**Importante**

Através desta rotina é possível realizar a inclusão, alteração e exclusão de um arquivo cadastrado.

# **Sincronização:**

Em **Ações Relacionadas** clique em **Sincronizar**:

             Obs. é necessário obter o TSS ativo para realizar esta sincronização.

![GNRE_5.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360020298591/GNRE_5.JPG)

![GNRE_6.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360020298611/GNRE_6.JPG)

 Verifique que a atualização da tabela é realizada com sucesso.

**Importante**

O campo Atualiza informa quem realizou a inclusão ou alteração do item (1=Import;2=TSS;3=Usuário). Caso o campo esteja com a opção 3 - Usuário, não será realizada a sincronização ou importação dos dados.

**Informações Técnicas**

**![GNRE_7.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360020413432/GNRE_7.JPG)**
