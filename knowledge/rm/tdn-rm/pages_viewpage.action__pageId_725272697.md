---
content_hash: 1ae92ba29edfeefa2f364bca804506c2ea2f1ee669722022d368e5867ee310fc
fetched_at: '2026-06-29T00:11:27.413717+00:00'
page_id: '725272697'
product: rm
source: tdn-rm
title: Relatórios do Aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=725272697
version: 9
---

Funcionalidade disponível a partir da versão 12.1.2302.

Para realizar a emissão do relatórios , é necessário que seja feita a importação dos relatórios na MDI no RM Reports.

## Permissão

Para que seja exibido o menu "Relatórios" para o usuário é necessário dar a permissão no item no perfil de usuários, conforme exibido abaixo, através do caminho Educacional | Educacional (Portal) | Gestão Educacional | Painel do Aluno |Relatórios.

## Parametrização

Para definir os relatórios que serão disponibilizados nesta tela. Acesse o menu Configurações| Parâmetros | RM Portal |Portal Gestão Educacional | Painel do Aluno | 

## Menu Relatórios

O menu Relatórios, exibe a lista de todos os relatórios disponíveis para o aluno conforme parametrização acima. Em cada um deles é possível gerar o relatório clicando no botão "Emitir relatório".

É possível filtrar a exibição por tipos de relatórios, selecionando os tipos "ALUNO", "SECRETARIA" ou  "FINANCEIRO" 

**Observação!**

Somente selecione relatórios que possuam tabela master correta de acordo com o tipo do relatório, pois é assim que o portal irá passar os filtros para a execução do relatório.

**Tabela Master para cada tipo de relatório:**

**Tipo Secretaria**  
      Campos chaves da tabela SMATRICPL(CODCOLIGADA, IDPERLET, IDHABILITACAOFILIAL, RA)  
**Tpo Aluno**  
      Campos chaves da tabela SALUNO(CODCOLIGADA, RA)  
**Tipo Tesouraria**  
      Campos chaves da tabela SCONTRATO(CODCOLIGADA, RA, IDPERLET, CODCONTRATO)
