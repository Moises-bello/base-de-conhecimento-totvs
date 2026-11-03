---
content_hash: 2e7d9ba494167b526ec98aac43a854b84e8d76bb97f5fbadfdf2338e20233eeb
fetched_at: '2026-06-29T00:10:19.498667+00:00'
page_id: '4814964'
product: rm
source: tdn-rm
title: Integração Gestão de Relacionamentos de Clientes  x Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4814964
version: 5
---

BLOCK

Integração Gestão de Relacionamentos de Clientes x Educacional

FAQ:  **Integração Gestão de Relacionamentos de Clientes x Educacional**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.82 |

Solução

[![jabber_original](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaC85ktApI/AAAAAAAAD0k/8tWJkUabP4g/jabber_original_thumb%5B5%5D.png?imgmax=800 "jabber_original")](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaC8FVMZYI/AAAAAAAAD0g/nuYmy2PYApk/s1600-h/jabber_original%5B9%5D.png)**Como fazer…**

  **Acesse: TOTVS Gestão de Relacionamentos de Clientes** e selecione WorkFlow / Tipos

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) Crie um novo tipo de atendimento e associe o serviço (Serviços Educacionais (RM Classis Net)) no serviço do tipo de atendimento.  
Caso este serviço não apareça para vinculação, deve-se rodar um script na base de dados para criação do mesmo:

> INSERT INTO HSERVICODOTIPOATENDIMENTO VALUES (10,'Serviços Educacionais (RM Classis Net)', 'CN', 'RM.Edu.ServicosCRMEB')

O tipo de atendimento deve ter um prazo inicial e final.

[![](http://lh4.ggpht.com/_G7KXZLoZDsY/TOaDBW8kcRI/AAAAAAAAD08/gj7BG05rimI/clip_image002%5B4%5D_thumb%5B3%5D.jpg?imgmax=800 "clip_image002[4]")](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAiYyboI/AAAAAAAAD04/HMle4R_d5UE/s1600-h/clip_image002%5B4%5D%5B5%5D.jpg)

[![clip_image004](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDCvHCdII/AAAAAAAAD1E/6QLBG_p_XKM/clip_image004_thumb%5B2%5D.jpg?imgmax=800 "clip_image004")](http://lh5.ggpht.com/_G7KXZLoZDsY/TOaDCObambI/AAAAAAAAD1A/ExuHsn5Ydcg/s1600-h/clip_image004%5B7%5D.jpg)

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) Para o tipo de atendimento, deve-se definir um local de entrega. Veja esse anexo, nele informa-se: Código da filial, Localidade e Descrição do local.

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) Ainda no cadastro do Tipo de Atendimento é necessário definir uma etapa para o atendimento.

Veja no anexo *Etapa*, caso esta etapa seja a primeira, no ato da solicitação via portal é obrigatório marcar que esta é a primeira etapa de um possível fluxo.

Deve haver um cadastro para cada etapa do atendimento, e para cada etapa, podem-se definir as ações do atendimento, campos obrigatórios, etc.

[![clip_image006](http://lh5.ggpht.com/_G7KXZLoZDsY/TOaDD4UXJUI/AAAAAAAAD1M/q9CA_utti1s/clip_image006_thumb%5B1%5D.jpg?imgmax=800 "clip_image006")](http://lh5.ggpht.com/_G7KXZLoZDsY/TOaDDfdRFVI/AAAAAAAAD1I/ftwN6zGA5gA/s1600-h/clip_image006%5B6%5D.jpg)

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) No cadastro do tipo de atendimento Anexo *Fluxo de etapas*, defini-se um fluxo para as etapas criadas anteriormente. (Qual é a primeira, a segunda e assim por diante).

Neste caso, define-se a Primeira etapa como Abertura de Atendimento e a próxima etapa como Fechamento do Atendimento.

[![](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaDFAj_lJI/AAAAAAAAD1U/TGocs2gyMBs/clip_image002%5B6%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[6]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TOaDEgCAixI/AAAAAAAAD1Q/ERAZWnwjp_A/s1600-h/clip_image002%5B6%5D%5B3%5D.jpg)

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) Para os tipos de Atendimento podem ser definidos parâmetros a serem utilizados nas solicitações via Portal ou TOTVS Gestão de Relacionamentos de Clientes.

Os parâmetros são cadastrados em *Cadastros / Atendimentos / Parâmetros*.

Para definir quais os parâmetros deseja usar nos atendimentos, dentro do tipo de atendimento em *Anexo / Parâmetro do tipo de atendimento* pode-se vincular o mesmo ao tipo de atendimento.

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) Para que um Tipo de Atendimento esteja disponível no Educacional e no Portal é necessário que haja um Grupo definido para o tipo de atendimento. O cadastro é feito em *Cadastros / Atendimentos / Grupo de atendimento*.

Neste caminho, faz-se um vínculo entre o tipo de atendimento e o grupo a ser utilizado.

[![](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaDGxao4DI/AAAAAAAAD1c/KOqulVgwn4Q/clip_image002%5B8%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[8]")](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDFsV2_gI/AAAAAAAAD1Y/fe9acDVlPXk/s1600-h/clip_image002%5B8%5D%5B3%5D.jpg)

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) Para que um tipo de atendimento esteja disponível no Portal para um determinado aluno, é necessário verificar se o perfil associado a ele possui liberação ao atendimento em questão.

[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TOaDI3X3A8I/AAAAAAAAD1k/Z97W4T2ceQ8/clip_image004%5B4%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image004[4]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TOaDH9D3-XI/AAAAAAAAD1g/tVWLhgG5KH0/s1600-h/clip_image004%5B4%5D%5B3%5D.jpg)

Se o Tipo de atendimento não estiver marcado, o mesmo não será apresentado no portal para que seja efetuada a solicitação.

**Acesse: TOTVS Educacional**

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) No TOTVS Educacional deve haver uma configuração no tipo de atendimento vinculando-o a algum serviço cadastrado. A configuração é feita no caminho: Atividades Acadêmicas / CRM / *Configurações*.

Clique em Novo e vincule o tipo de atendimento criado anteriormente no TOTVS Gestão de Relacionamentos de Clientes ao tipo de serviço.

[![clip_image008](http://lh5.ggpht.com/_G7KXZLoZDsY/TOaDLRBp2qI/AAAAAAAAD10/-Cq5oLFr5S0/clip_image008_thumb%5B1%5D.jpg?imgmax=800 "clip_image008")](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDLCVYMzI/AAAAAAAAD1w/0ECJffOvYWw/s1600-h/clip_image008%5B4%5D.jpg)

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) Para Geração de serviço extra, o parâmetro ‘Inserir serviço extra e gerar lançamento ao abrir atendimento’, deve estar marcado.Nos parâmetros do Sistema em: Configurações / Parâmetros / integração / Atendimento, deve haver um atendente responsável para abertura de atendimentos.

A data de vencimento pode ser definida de três formas:

> 1. Vencimento definido para o Período Letivo, para atendimentos solicitados até a data cadastrada. Pode-se definir também a parcela que será gerada com o serviço extra para o aluno solicitante.

[![clip_image010](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDNSTnF-I/AAAAAAAAD18/4KTV8huDNm4/clip_image010_thumb%5B1%5D.jpg?imgmax=800 "clip_image010")](http://lh4.ggpht.com/_G7KXZLoZDsY/TOaDMgIfGZI/AAAAAAAAD14/byKcl7XUWOA/s1600-h/clip_image010%5B4%5D.jpg)

> 2. Vencimento calculado automaticamente a partir da data de solicitação, com o número de dias indicados pelo usuário: o parâmetro ‘Calcular automaticamente a data de vencimento da parcela’ deve ser selecionado, e o número de dias deve ser preenchido abaixo.

[![clip_image003](http://lh4.ggpht.com/_G7KXZLoZDsY/TOaDO8VufwI/AAAAAAAAD2E/uNe8yaQ_9wQ/clip_image003_thumb%5B2%5D.jpg?imgmax=800 "clip_image003")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaDOPZ3tRI/AAAAAAAAD2A/p0IkilerJn4/s1600-h/clip_image003%5B5%5D.jpg)

> 3. Para contratos de Vencimento Fixo, tal data pode ser preservada independente da definição escolhida – que continua a valer para os demais contratos: basta marcar o parâmetro ‘Utilizar a data de vencimento de contratos com dia fixo’.

**Gerando solicitação pelo Portal:**

**Acesse:** **TOTVS RM PORTAL**

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) Efetue o login no portal. Entre no Educacional. Selecione o contexto do aluno.

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) Entre no menu Solicitação - Grupo de Atendimento.

[![clip_image005](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaDQcgWapI/AAAAAAAAD2M/hWvgHtYvQMQ/clip_image005_thumb%5B4%5D.jpg?imgmax=800 "clip_image005")](http://lh5.ggpht.com/_G7KXZLoZDsY/TOaDPSdJg6I/AAAAAAAAD2I/2b9vMQ-ZvGA/s1600-h/clip_image005%5B7%5D.jpg)

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) Selecione o Tipo de Atendimento.

[![](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaDSIAvlWI/AAAAAAAAD2U/16IJ8drkSAI/clip_image002%5B13%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[13]")](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDRhGWUWI/AAAAAAAAD2Q/aQ-NKi1HGt0/s1600-h/clip_image002%5B13%5D%5B3%5D.jpg)

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) Verifique os dados da solicitação, clique em SOLICITAR.

[![](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDTwR5k_I/AAAAAAAAD2c/Frn0eCZ5OhE/clip_image002%5B15%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[15]")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaDS-XootI/AAAAAAAAD2Y/tp7aL8pAJlY/s1600-h/clip_image002%5B15%5D%5B3%5D.jpg)

Após estes passos, um lançamento extra deve ser gerado no respectivo contrato do aluno.

[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TOaDVeOVF9I/AAAAAAAAD2k/EZmpnaR3_xk/clip_image004%5B10%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image004[10]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TOaDUf8pp7I/AAAAAAAAD2g/wP5nrYRtzGM/s1600-h/clip_image004%5B10%5D%5B3%5D.jpg)

**Gerando solicitação pelo Executável**

**Acesse:** **TOTVS Educacional** através do menu:

*Secretaria/Integração CRM/ Solicitações de atendimentos*.

Ou pela Nova MDI *Atividades Acadêmicas/Solicitações de atendimentos*.

[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TOaDWvFIFAI/AAAAAAAAD2s/sMvyHWuhfas/clip_image002%5B17%5D_thumb%5B2%5D.jpg?imgmax=800 "clip_image002[17]")](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDWMNgrCI/AAAAAAAAD2o/zWqmXbbHvYY/s1600-h/clip_image002%5B17%5D%5B4%5D.jpg)

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) Através do executável, o usuário pode solicitar um atendimento de forma semelhante ao portal, porém com mais possibilidades

Pode-se criar um atendimento para um aluno sem que ele tenha matrícula no Período letivo, utilizando apenas os dados do contrato para atendimentos que gerem cobrança.

[![nav-prefs](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDAE0o9YI/AAAAAAAAD00/KSFlRBX-14g/nav-prefs_thumb%5B3%5D.png?imgmax=800 "nav-prefs")](http://lh6.ggpht.com/_G7KXZLoZDsY/TOaC-4DIrGI/AAAAAAAAD0w/7f-UVXbhUds/s1600-h/nav-prefs%5B5%5D.png) Sendo um tipo de atendimento parametrizado para ‘Inserir serviço extra e gerar lançamento ao abrir atendimento’, é possível escolher o número da parcela e cota no qual se deseja incluir um serviço extra para o aluno, além de alterar o valor do serviço, a data de vencimento e o tipo da parcela - bastando que o usuário possua permissão para ‘alterar dados financeiros da solicitação de atendimentos’.

**[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TOaDYxsPoHI/AAAAAAAAD20/xhV_JX5LUSk/clip_image002%5B19%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[19]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TOaDX91DniI/AAAAAAAAD2w/-F0eiRjDO78/s1600-h/clip_image002%5B19%5D%5B3%5D.jpg)**

**Permissão do usuário educacional:**

Parametrização no perfil dos usuários do Educacional em: *Cadastros / Segurança / Perfis / Anexo Parâmetros Educacionais*.

**[![](http://lh3.ggpht.com/_G7KXZLoZDsY/TOaDaSWvD2I/AAAAAAAAD28/G6AhPvJS3Po/clip_image002%5B21%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[21]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TOaDZstkNNI/AAAAAAAAD24/mBAyWzKB9Ko/s1600-h/clip_image002%5B21%5D%5B3%5D.jpg)**

Ao final do processo, será gerado um atendimento na Integração **TOTVS Gestão de Relacionamentos de Clientes** (RM Agilis), de acordo com a configuração escolhida
