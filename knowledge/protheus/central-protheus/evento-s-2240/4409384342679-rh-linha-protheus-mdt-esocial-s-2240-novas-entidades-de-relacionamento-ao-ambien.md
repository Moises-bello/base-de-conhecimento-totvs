---
article_id: 4409384342679
category: Evento S-2240
content_hash: 39abc0295fd7a1b279e2f1afa3c1e3201dfacc2575d533315f42da9afa082030
fetched_at: '2026-06-28T22:45:23.691428+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Novas Entidades de Relacionamento
  ao Ambiente Físico
type: support-article
updated_at: '2025-03-03T18:06:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409384342679-RH-Linha-Protheus-MDT-eSocial-S-2240-Novas-Entidades-de-Relacionamento-ao-Ambiente-F%C3%ADsico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372480332567)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como configurar o Ambiente Físico para relacionamento de novas entidades?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Foi liberado uma melhoria para atender alguns cenários de exposição dos trabalhadores.  
  
Criado o parâmetro **MV\_NG2EAMB** e das entidades departamento, função, tarefa e funcionário para relacionamento com o ambiente físico, onde junto com a entidade de **centro de custo** já existente, possibilite a escolha do relacionamento a ser considerado para buscar as informações do ambiente em que o funcionário trabalha e enviar ao eSocial através da tag <infoAmb>.  
  
Consulte links para mais informações:  
[RH - Linha Protheus - MDT - eSocial - S-2240 - Orientações gerais sobre o Ambiente Físico no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407190841751)  
  
[RH - Linha Protheus - MDT - Não aparece a grid conforme melhoria de novas entidades de relacionamento ao Ambiente Físico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409385321751)  
  
**1. Ambiente x Centro de Custo** (tabela TOQ):  
  
Como apontado anteriormente, essa é a opção que virá por padrão e é a considerada atualmente. Ao selecionar essa opção, no cadastro de ambientes físicos será apresentada uma grid para poder relacionar os centros de custo ao ambiente, conforme exemplificado na imagem abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409390468759)  
  
Ao enviar o evento S-2240 ao eSocial, o sistema buscará o centro de custo do funcionário definido no campo "Centro Custo" (RA\_CC) do cadastro de funcionários (GPEA010) e através desse centro de custo irá buscar o ambiente a que ele está vinculado através da tabela TOQ, responsável por salvar o relacionamento entre o ambiente e o centro de custo. Tendo encontrado as informações do ambiente, o sistema enviará na tag <infoAmb> ao eSocial. Em "Outras Ações", existe o botão "Centros de Custo", que abrirá uma tela com um Markbrowse para facilitar a seleção dos centros de custo a serem vinculados com o ambiente.  
  
**2. Ambiente x Departamento** (tabela TOR):  
  
Ao selecionar essa opção, no cadastro de ambientes físicos será apresentada uma grid para poder relacionar os departamentos ao ambiente, conforme exemplificado na imagem abaixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409384654743)  
  
Ao enviar o evento S-2240 ao eSocial, o sistema buscará o departamento do funcionário definido no campo "Cod. Depto. " (RA\_DEPTO) do cadastro de funcionários (GPEA010) e através desse departamento irá buscar o ambiente a que ele está vinculado através da tabela TOR, responsável por salvar o relacionamento entre o ambiente e o departamento. Tendo encontrado as informações do ambiente, o sistema enviará na tag <infoAmb> ao eSocial. Em "Outras Ações", existe o botão "Departamentos", que abrirá uma tela com um Markbrowse para facilitar a seleção dos departamentos a serem vinculados com o ambiente.  
  
**3. Ambiente x Função** (tabela TOS):  
  
Ao selecionar essa opção, no cadastro de ambientes físicos será apresentada uma grid para poder relacionar as funções ao ambiente, conforme exemplificado na imagem abaixo:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409390551575)  
  
Ao enviar o evento S-2240 ao eSocial, o sistema buscará a função do funcionário definido no campo "Cod. Funcao" (RA\_CODFUNC) do cadastro de funcionários (GPEA010) e através dessa função irá buscar o ambiente a que ele está vinculada através da tabela TOS, responsável por salvar o relacionamento entre o ambiente e a função. Tendo encontrado as informações do ambiente, o sistema enviará na tag <infoAmb> ao eSocial. Em "Outras Ações", existe o botão "Funções", que abrirá uma tela com um Markbrowse para facilitar a seleção das funções a serem vinculados com o ambiente.  
  
**4. Ambiente x Tarefa** (tabela TOT):  
  
Ao selecionar essa opção, no cadastro de ambientes físicos será apresentada uma grid para poder relacionar as tarefas ao ambiente, conforme exemplificado na imagem abaixo:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409384850711)  
  
Ao enviar o evento S-2240 ao eSocial, o sistema buscará a tarefa a que o funcionário está vinculado através da rotina de Tarefas por Funcionário (MDTA090) e através dessa tarefa irá buscar o ambiente a que ela está vinculada através da tabela TOT, responsável por salvar o relacionamento entre o ambiente e a tarefa. Tendo encontrado as informações do ambiente, o sistema enviará na tag <infoAmb> ao eSocial. Em "Outras Ações", existe o botão "Tarefas", que abrirá uma tela com um Markbrowse para facilitar a seleção das tarefas a serem vinculadas com o ambiente.  
  
**5. Ambiente x Funcionário** (tabela TOU):  
  
Ao selecionar essa opção, no cadastro de ambientes físicos será apresentada uma grid para poder relacionar os funcionários ao ambiente, conforme exemplificado na imagem abaixo:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409384823191)  
  
Ao enviar o evento S-2240 ao eSocial, o sistema buscará o ambiente a que o funcionário está vinculado através da tabela TOU, responsável por salvar o relacionamento entre o ambiente e o funcionário. Tendo encontrado as informações do ambiente, o sistema enviará na tag <infoAmb> ao eSocial.   
Em "Outras Ações", existe o botão "Funcionários", que abrirá uma tela com um Markbrowse para facilitar a seleção dos funcionários a serem vinculados com o ambiente.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409390796695)  
  
Na tela de seleção dos funcionários, em "Outras Ações", existe o botão "Filtrar" que abrirá uma tela para a composição de um filtro a ser aplicado sobre os funcionários apresentados no Markbrowse, dessa forma é possível selecionar o centro de custo, departamento, função e tarefa dos funcionários para realizar a filtragem.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409385044503)  
  
Nos campos de centro de custo, departamento, função e tarefa do filtro é possível selecionar apenas um código ou pressionar a tecla F10 para que o sistema abra um novo Markbrowse para selecionar mais de um código para cada campo. Abaixo, está exemplificada a tela de filtragem dos funcionários:  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409385107607)  
  
É necessário atualizar o dicionário de dados do Acumulado MDT:   
[RH - Linha Protheus - MDT - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo medicina e segurança do trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773-RH-Linha-Protheus-MDT-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-medicina-e-seguran%C3%A7a-do-trabalho?source=search)  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
