---
article_id: 360012143752
category: Relatórios
content_hash: 2c7a53b2f1bb29263e6da661d64bcc55c9b9e9f173cc0b8cfd8ae673001f012b
fetched_at: '2026-06-28T22:46:39.315671+00:00'
product: rm
section_id: 1500000861642
source: central-rm
title: RH - RM - PTO - Permissão para editar a estrutura do relatório do espelho de
  cartão de Ponto
type: support-article
updated_at: '2025-02-19T13:11:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012143752-RH-RM-PTO-Permiss%C3%A3o-para-editar-a-estrutura-do-relat%C3%B3rio-do-espelho-de-cart%C3%A3o-de-Ponto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16979874174231) Tempo aproximado para leitura:****00:01:00 min****Ocorrência**No módulo **Automação de Ponto**, ao tentar editar a estrutura do relatório do espelho é apresentada a mensagem:   
*Você não tem permissão para editar a estrutura do relatório XXXXXXX-XXXXXXXXXXX. Este é um relatório padrão Totvs*  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 11.82.

**Causa**Esta mensagem é apresentada porque o relatório não foi importado anteriormente, ele terá que ser importado para que seja possível a edição.   
  
**Solução**Para conseguir editar o relatório, realize os seguintes passos:  
  
1. No módulo de **Automação de Ponto** o menu **Gestão| RM Reports** e selecione o código do relatório desejado. Acesse a opção **Processos | Exportar Estrutura do Relatório**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30078904599319)

2. Na tela que será aberta clique em avançar e em executar. Na tela de execução concluída clique na opção salvar o arquivo, (defina uma pasta da sua máquina para salvá-lo). Ao fim do processo será apresentada a informação: Arquivo salvo com sucesso. E para sair da tela clique no botão fechar.

![exportar_relatorio.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/30086583787799)

4. Em seguida efetue o procedimento de importar o mesmo arquivo acessando, **Processos | Importar Estrutura do Relatório.** Será apresentada a mensagem que já existe um relatório, clique na opção: Sobrescrever Existente e clique no botão executar.     
![Importar_relatorio_sobrescrever.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/30086576022679)

6. Ao final do processo será possível editar a estrutura do relatório.
