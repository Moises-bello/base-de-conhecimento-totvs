---
content_hash: ebebc438cebdd4518fdd9a310999277a6c5e564313597cfbff34bfda1d11ea87
fetched_at: '2026-06-29T00:09:00.882662+00:00'
page_id: '370607671'
product: rm
source: tdn-rm
title: 2686822 DSAUGHFATF-545 DT Script do CODLABORATORIO Brasindice apagando vínculo
  dos produtos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370607671
version: 2
---

# Erro na Atualização do Layout Brasíndice

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Importação / Atualização Brasíndice |
| **Situação:** | Ao realizar atualização do sistema para permitir a importação de arquivos Brasíndice disponibilizados no Novo Layout, onde o Código do Laboratório teve o acréscimo de tamanho de três para quatro dígitos, o sistema não mantinha os vínculos já realizados entre os itens Brasíndice e os Produtos cadastrados. |
| **Solução:** | * Foi detectado que era necessário executar a marcação do Script SA.2018.02\_05 gerada pela engenharia para verificar a existência da coluna CODLABORATORIO na tabela SZATENDINTEMGRATIS, para que a mesma seja criada, caso não exista. * A marcação do Script SA.2018.02\_04, que atualiza o layout Brasíndice e que foi disponibilizada como Script Específico na versão 12.1.18, foi corrigida para os casos onde o processo de atualização ainda não havia sido realizada. * Para os casos onde a marcação SA.2018.02\_04 já havia sido exeutada, foi disponibilizada uma nova marcação SA.2018.05\_05, disponibilizada como Script Específico na versão 12.1.20. Essa marcação faz a correção das tabelas atualizadas pela marcação SA.2018.02\_04, quando a mesma estava desatualizada. * A tela da rotina de Importação / Atualização Brasíndice, foi atualizada para tratar os casos onde o Código Laboratório possuí três dígitos. Essa alteração, está disponibilizada a partir do RMSaude (Patch) 12.1.18.032.exe (Gerado em 01/06/2018). |
