---
article_id: 360025646234
category: Ferramentas
content_hash: caf7afb2b043efc5ba35a47d66a363764da543dbfb50ee3ca52feb8f5737f062
fetched_at: '2026-06-28T22:42:18.068720+00:00'
product: protheus
section_id: 360000075448
source: central-protheus
title: Framework - Linha Protheus - Salvar Filtro na Consulta Genérica
type: support-article
updated_at: '2024-05-09T11:16:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025646234-Framework-Linha-Protheus-Salvar-Filtro-na-Consulta-Gen%C3%A9rica
---

**Dúvida**Como fazer para salvar um filtro na Consulta Genérica?  
   
 **Ambiente**Protheus - SmartClient - A partir da versão 11  
   
**Solução**No padrão, não é possível salvar os filtros configurados na rotina de Consulta Genérica. Porém, pode-se criar uma Consulta e Salvar em Arquivo, conforme procedimento abaixo:  
  
1. Abra a opção **Genéricos**   
2. Selecione a tabela desejada e clique em **OK**  
3. Clique em **Dicionário**   
4. Selecione os campos desejados   
5. Clique em **Arquivo**   
6. Selecione novamente a tabela que você abriu   
7. Clique em **Salvar** e preencha os campos **Arquivo** (nome do relatório) e **Descrição**.   
8. Clique em OK, a mensagem "Consulta salva no arquivo nomedorelatorio.C4W" aparecerá, clique em **OK**  
9. Clique em **Cancelar**   
10. Clique em **Sair**   
11. Acesse novamente a rotina de **Genéricos**   
12. Selecione a Tabela utilizada anteriormente   
13. Clique na opção **Abrir**  
14. Procure pelo nome do Relatório dado anteriormente  
15. Clique em **OK**  
16. Verifique se suas alterações estão todas salvas  
  
Observação: Sempre que for abrir o relatório salvo, você **deve** abrir a tabela com a opção **Abrir**, caso contrário, se você clicar em **OK,** o sistema irá abrir a tabela sem as suas alterações.  
  
Outra possibilidade é criar um Filtro Inteligente no Configurador. Abaixo, documentação a respeito:  
<http://tdn.totvs.com/display/PROT/Filtros+Inteligentes+-+Como+criar>
