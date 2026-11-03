---
content_hash: 913d1c452fccccf54a3c05675ae73067ea1509738c2eb28f04b62a31d0a911e4
fetched_at: '2026-06-29T00:08:10.826994+00:00'
page_id: '240982767'
product: rm
source: tdn-rm
title: MAN0002_Tipo_Movimento_OS_Terceiros
type: documentation
url: https://tdn.totvs.com/display/LRM/MAN0002_Tipo_Movimento_OS_Terceiros
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Manutenção (RMOfficina) |
| **Versões:** | A partir da versão 11.82 |
| **Ocorrência:** | Parametrização do Tipo de Movimento de Ordem de Serviço de Terceiros |
| **Ambiente:** | Como parametrizar o Tipo de Movimento de Ordem de Serviço de Terceiros |
| **Passo a passo:** | **Parametrização do Tipo de Movimento de Ordem de Serviço de Terceiros**    A parametrização do Tipo de Movimento de Ordem de Serviço de Terceiros é basicamente a mesma do Tipo de Movimento de Ordem de Serviço convencional, entretanto, é necessário realizar uma parametrização no RMOfficina para definir que esse Movimento será considerado como Ordem de Serviço de Terceiros:   * A Série do Movimento de ser do Tipo “OS”; * A Edição da Numeração deve estar como “Mostra”; * Usuário possuir permissão no Tipo de Movimento;        * Os campos de **Data Emissão, Data de Saída, Data de Autorização e Data de Término** são preenchidos de forma automática pelo Sistema após realizar as alterações do Status da Ordem de Serviço, dessa forma, o Tipo de Movimento deve ser parametrizado conforme a imagem abaixo no RMNucleus na Etapa Mov – Datas 1/2 e 2/2:          * No RMNucleus, acessar o menu Cadastros | Segurança | Usuários, editar o nome do usuário em questão e acessar a opção Anexos | Permissões por Tipo de Movimento. O Usuário deverá ter permissões no Tipo de Movimento para realizar a inclusão:        * **IMPORTANTE:** Acessar o RMOfficina menu Cadastros | Tipos de Movimento, editar o Tipo de Movimento de Ordem de Serviço de Terceiros e realizar a seguinte parametrização: |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
