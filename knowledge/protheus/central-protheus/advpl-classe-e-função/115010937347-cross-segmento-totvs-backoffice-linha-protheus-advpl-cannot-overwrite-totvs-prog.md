---
article_id: 115010937347
category: ADVPL - Classe e Função
content_hash: 9345651f4ac8dbd46a8f12a822de00db3d7596d391acac3b265d77e73ad13d3a
fetched_at: '2026-06-28T22:40:14.111226+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Cannot overwrite
  totvs programs
type: support-article
updated_at: '2021-09-01T14:11:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010937347-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cannot-overwrite-totvs-programs
---

**Dúvida**Compilação NFESEFAZ.PRW - Cannot overwrite TOTVS programs, como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Versão 11.80  
  
**Solução**É necessário excluir o rdmake compilado no RPO e compilá-lo novamente para contornar o problema.  
Seguem os procedimentos utilizando o TDS:

* Localize o rdmake no projeto, clique com o botão direito do mouse e selecione a opção 'Excluir fonte(s) do RPO'
* Compile novamente o rdmake

Observação  
Persistindo temos mais dois procedimentos

* cria um novo fonte ADVPL com nome NFESEFAZ.PRW e copie a estrutura para esse fonte.
* Caso persista, na versão P11 aplique o path no link abaixo e descompile e compile o seu fonte NFESEFAZ.PRW

| ATENÇÂO: O Procedimento com o path é somente para o caso NFESEFAZ na Versão P11 |
| --- |

Outros fontes como de relatórios podem exibir a mesma mensagem " Cannot overwrite TOTVS programs " é só descompilar e compilar o seu fonte XXX.PRW  
  
**Saiba mais**

[ADV0006 TDS Compilação NFESEFAZ](http://tdn.totvs.com/display/PROT/ADV0006_TDS_Compilacao_NFESEFAZ_Cannot+overwrite+TOTVS+programs)
