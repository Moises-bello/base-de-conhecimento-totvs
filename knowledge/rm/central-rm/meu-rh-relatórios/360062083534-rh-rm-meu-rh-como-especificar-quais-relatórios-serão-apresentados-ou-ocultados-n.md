---
article_id: 360062083534
category: Meu RH - Relatórios
content_hash: ef976f160c4a14205d4652624af3a33828cd5c07859f266e33ed0f1ef9f6da50
fetched_at: '2026-06-28T22:47:31.000527+00:00'
product: rm
section_id: 1500000861762
source: central-rm
title: RH - RM - Meu RH - Como especificar quais relatórios serão apresentados ou
  ocultados no Meu RH
type: support-article
updated_at: '2024-07-29T14:57:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062083534-RH-RM-Meu-RH-Como-especificar-quais-relat%C3%B3rios-ser%C3%A3o-apresentados-ou-ocultados-no-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22328221934231) Tempo aproximado para leitura: 00:05:00 min**

**Dúvida**  
Como especificar quais relatórios serão apresentados ou ocultados no Meu RH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH – 12.1.32  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

**1.** Para exibir relatórios dos produtos RH (Folha de Pagamento, Gestão de Pessoas e Ponto) no Meu RH acesse a guia **Gestão | Ferramentas de Análise | RM Reports**. Selecione o relatório desejado na listagem de relatórios e clique no ícone “Editar”, ou tecle “Control + Enter”. No formulário das propriedades do relatório, na opção “Tipo”, pesquise e selecione o tipo especificado.

Os tipos para cada categoria podem ser "Dados da minha equipe" ou "Meus dados", conforme informado abaixo: *(Obs.: Disponível a partir do patch 12.1.31.215)*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414745701783)

|  |  |
| --- | --- |
| **Categorias** | **Tipos** |
| **Folha de Pagamento** | 152 - Meus dados  153 - Dados da minha equipe |
| **Gestão de Pessoas** | 149 - Meus dados  150 - Dados da minha equipe |
| **Ponto** | 154 - Meus dados  155 - Dados da minha equipe |

Com esta funcionalidade poderá ser gerado vários tipos de relatórios, tais como:

* Comunicado para os colaboradores
* Formulários para preenchimentos
* Relatórios estratégicos utilizando a matrícula do funcionário
* Relatórios estratégicos para os gestores

**1.1** Após isso, os relatórios já serão apresentados na aba Relatórios do Meu RH.

**2.** Caso queira restringir um certo relatório à apenas alguns funcionários, acesse o perfil associado ao(s) usuário(s) do Meu RH  > Acesso a Relatórios/Planilhas> Criar um Grupo de relatórios

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003747802)

**Aviso:** Após criar os grupos de relatórios/planilhas, todos os usuários que estiverem associados ao perfil pertencerão aos grupos dele também. Para cada grupo será cadastrado o nível de permissão de alteração e emissão dos relatórios/planilhas.

**3.** Retorne à guia Gestão| RM Reports > Selecione o relatório desejado na listagem de relatórios e clique no ícone “Editar”, ou tecle “Control + Enter”. No formulário das propriedades do relatório, na opção “Grupo”, pesquise e selecione o grupo desejado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003797961)

**3.1** Para alterar o nível de acesso do relatório, modifique o valor do campo “Nível de Acesso” de acordo com o nível de segurança planejado.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003797981)

**Importante**

Serão listados para escolha de “Grupo” somente os grupos de relatório que estiverem associados ao perfil do usuário que estiver configurando esta segurança, exceto se o usuário for supervisor no módulo.

O sistema não permitirá que seja atribuído ao “Nível de Acesso” valor maior que o “Nível de Alteração” definido no grupo selecionado associado ao perfil do usuário que estiver configurando esta segurança.

**>** Os relatórios poderão ser gerados através de filtros como (coligada e chapa) ou sem passagem de filtros para os relatórios de comunicados por exemplo:

**>** Caso o Meu RH esteja sendo utilizado através de um navegador em um computador (que não seja de uso pessoal - como um quiosque), alertamos que os downloads (arquivos de informe de rendimentos) ficarão na máquina e, se não forem eliminados, poderão ser acessados por outros usuários!

A partir do release 2406 o Menu **outros** aonde são listado relatórios de outros produtos não será mais apresentado por padrão.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24654675592471)  
  
Para que os relatórios de outros produtos sejam listados para o usuário, além de seguir os passos acima para exibir a estrutura, é necessário habilitar o parâmetro "Exibir Relatórios do tipo Outros".

**Modulo Folha de pagamento / aba configurações / Parametrizador / RM Portal / Localize e edite o grupo de quiosque utilizado pelos funcionários / Etapa Portal Meu RH.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24654707525143)

Após a parametrização reinicie todos os serviços de host RM do ambiente do portal. Após reinicie também o IIS.

**Saiba mais**  
[Grupos de Relatórios](https://tdn.totvs.com.br/pages/releaseview.action?pageId=61934230#GruposdeRelat%C3%B3rios-Cria%C3%A7%C3%A3odosGruposporPerfil)

[Personalizar Permissões de Funcionalidade no Meu RH](https://tdn.totvs.com/pages/viewpage.action?pageId=287067720)
